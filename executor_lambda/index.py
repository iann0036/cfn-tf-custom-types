import os
import subprocess
import boto3
import re
import json
from uuid import uuid4


def check_call(args, cwd):
    proc = subprocess.Popen(args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd)
    stdout, stderr = proc.communicate()
    if stdout:
        print(stdout.decode('utf-8'))
    if stderr:
        print(stderr.decode('utf-8'))
    if proc.returncode != 0:
        if stderr:
            err = stderr.decode('utf-8').split('\n')
            err = [ line for line in err if "on main.tf.json line" not in line ]
            err = '\n'.join(err)
            raise Exception(err)
        raise Exception('Non-zero exit code from process call')
    
    return stdout.decode('utf-8')


def tf_to_cfn_str(obj):
    return re.sub(r'(?:^|_)(\w)', lambda x: x.group(1).upper(), obj)


def cfn_to_tf_str(obj):
    return re.sub('([A-Z]{1})', r'_\1', obj).lower()[1:]


def parse_obj(obj):
    if isinstance(obj, list):
        ret = []
        for item in obj:
            ret.append(parse_obj(item))

        if len(ret) > 0 and isinstance(ret[0], dict) and sorted(ret[0].keys()) == ["map_key", "map_value"]:
            mapret = {}
            for mapitem in ret:
                mapret[mapitem['map_key']] = mapitem['map_value']
            return mapret

        return ret
    elif isinstance(obj, dict):
        if obj.keys() == ["IsPropertyDefined"]:
            return {}

        ret = {}
        for prop, value in obj.items():
            ret[cfn_to_tf_str(prop)] = parse_obj(value)

        return ret

    return obj


def generate_tf(model, logicalId, providerTypeName, terraformTypeName):
    secretsmanagerclient = boto3.client("secretsmanager")

    tf = {
        "provider": {},
        "resource": {}
    }
    tf['provider'][providerTypeName] = {}
    tf['resource'][terraformTypeName] = {}
    tf['resource'][terraformTypeName][logicalId] = {}

    try:
        secretstr = secretsmanagerclient.get_secret_value(SecretId="terraform/{}".format(providerTypeName))['SecretString']
        tf["provider"][providerTypeName].update(json.loads(secretstr))
    except:
        pass

    if model: # potentially no properties set
        for prop, value in model.items():
            if value is not None and prop != "tfcfnid":
                tf['resource'][terraformTypeName][logicalId][cfn_to_tf_str(prop)] = parse_obj(value)

    with open("/tmp/main.tf.json", "w") as f:
        f.write(json.dumps(tf, indent=2))

    return tf


def handler(event, context):
    s3client = boto3.client("s3")
    stsclient = boto3.client("sts")

    trackingid = event['trackingId']
    operationid = event['operationId']
    statebucketname = os.environ['BUCKET']

    status = {
        'status': 'completed',
        'returnValues': {}
    }

    try:
        if event['action'] in ["UPDATE", "DELETE"]:
            with open('/tmp/terraform.tfstate', 'wb') as f:
                s3client.download_fileobj(statebucketname, 'state/{}.tfstate'.format(trackingid), f)

        tf = generate_tf(event['model'], event['logicalId'], event['providerTypeName'], event['terraformTypeName'])

        print("Initializing provider")
        check_call([os.path.dirname(os.path.realpath(__file__)) + '/terraform', 'init', '-no-color'], "/tmp/")
        if event['action'] == "DELETE":
            print("Executing delete")
            check_call([os.path.dirname(os.path.realpath(__file__)) + '/terraform', 'destroy', '-auto-approve', '-no-color'], "/tmp/")
        else:
            print("Executing create/update")
            check_call([os.path.dirname(os.path.realpath(__file__)) + '/terraform', 'apply', '-auto-approve', '-no-color'], "/tmp/")

        if event['action'] == "DELETE":
            print("Deleting state S3 object")
            s3client.delete_object(
                Bucket=statebucketname,
                Key="state/{}.tfstate".format(trackingid)
            )
        else:
            print("Storing result")
            with open("/tmp/terraform.tfstate", "rb") as f:
                s3client.upload_fileobj(f, statebucketname, "state/{}.tfstate".format(trackingid))
            
            print("Packing return values")
            try:
                tfshow = json.loads(check_call([os.path.dirname(os.path.realpath(__file__)) + '/terraform', 'show', '-json', '-no-color'], "/tmp/"))
                if 'values' in tfshow['values']['root_module']['resources'][0]:
                    for tfreturnname, tfreturnvalue in tfshow['values']['root_module']['resources'][0]['values'].items():
                        status['returnValues'][tf_to_cfn_str(tfreturnname)] = tfreturnvalue
                if 'instances' in tfshow['values']['root_module']['resources'][0]:
                    for tfreturnname, tfreturnvalue in tfshow['values']['root_module']['resources'][0]['instances'][0]['attributes'].items():
                        status['returnValues'][tf_to_cfn_str(tfreturnname)] = tfreturnvalue
                print(status['returnValues'])
            except:
                pass

    except Exception as e:
        status = {
            'status': 'failed',
            'error': str(e),
            'returnValues': {}
        }

    s3client.put_object(Body=json.dumps(status).encode(), Bucket=statebucketname, Key="status/{}.json".format(operationid))

    os.remove("/tmp/main.tf.json")
    os.remove("/tmp/terraform.tfstate")
