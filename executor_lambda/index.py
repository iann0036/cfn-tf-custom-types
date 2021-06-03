import os
import subprocess
import boto3
import re
import json
import time
from uuid import uuid4


def exec_call(args, cwd):
    stdout = None
    stderr = None
    proc = None

    if 'DEBUG_SKIP_EXECUTION' in os.environ and os.environ['DEBUG_SKIP_EXECUTION'] == "true":
        with open('/tmp/terraform.tfstate', 'wb') as f:
            f.write(b'')
        return {}
    
    try:
        proc = subprocess.run(args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=cwd,
            timeout=720,
            check=True)
        stdout = proc.stdout
        stderr = proc.stderr
    except subprocess.TimeoutExpired as e:
        print(e.output)
        print(e)

    if stdout:
        pass # print(stdout.decode('utf-8'))
    if stderr:
        print(stderr.decode('utf-8'))
    if not proc or proc.returncode != 0:
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


def generate_tf(model, logicalId, providerTypeName, providerFullName, terraformTypeName):
    secretsmanagerclient = boto3.client("secretsmanager")

    tf = {
        "terraform": {
            "required_providers": {}
        },
        "provider": {},
        "resource": {}
    }
    tf['terraform']['required_providers'][providerTypeName] = {
        'source': providerFullName
    }
    tf['provider'][providerTypeName] = {}
    tf['resource'][terraformTypeName] = {}
    tf['resource'][terraformTypeName][logicalId] = {}

    if providerTypeName == "aws":
        tf['provider'][providerTypeName]["region"] = os.environ['AWS_REGION']

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
        'status': 'completed'
    }

    try:
        if event['action'] in ["UPDATE", "DELETE"]:
            with open('/tmp/terraform.tfstate', 'wb') as f:
                s3client.download_fileobj(statebucketname, 'state/{}/{}.tfstate'.format(event['terraformTypeName'], trackingid), f)

        tf = generate_tf(event['model'], event['logicalId'], event['providerTypeName'], event['providerFullName'], event['terraformTypeName'])

        print(tf)

        print("Initializing provider")
        exec_call([os.path.dirname(os.path.realpath(__file__)) + '/terraform', 'init', '-input=false', '-no-color'], "/tmp/")
        if event['action'] == "DELETE":
            print("Executing delete")
            exec_call([os.path.dirname(os.path.realpath(__file__)) + '/terraform', 'destroy', '-input=false', '-auto-approve', '-no-color'], "/tmp/")
        else:
            print("Executing create/update")
            exec_call([os.path.dirname(os.path.realpath(__file__)) + '/terraform', 'apply', '-input=false', '-auto-approve', '-no-color'], "/tmp/")

        if event['action'] == "DELETE":
            print("Deleting state S3 objects")
            s3client.delete_object(
                Bucket=statebucketname,
                Key="state/{}/{}.tfstate".format(event['terraformTypeName'], trackingid)
            )
            s3client.delete_object(
                Bucket=statebucketname,
                Key="state/{}/{}.model.json".format(event['terraformTypeName'], trackingid)
            )
        else:
            print("Storing Terraform state")
            with open("/tmp/terraform.tfstate", "rb") as f:
                s3client.upload_fileobj(f, statebucketname, "state/{}/{}.tfstate".format(event['terraformTypeName'], trackingid))
            
            print("Packing return values")
            try:
                event['model']['tfcfnid'] = trackingid
                tfshow = json.loads(exec_call([os.path.dirname(os.path.realpath(__file__)) + '/terraform', 'show', '-json', '-no-color'], "/tmp/"))
                if 'values' in tfshow['values']['root_module']['resources'][0]:
                    for tfreturnname, return_value_value in tfshow['values']['root_module']['resources'][0]['values'].items():
                        return_value_name = tf_to_cfn_str(tfreturnname)
                        if return_value_name in event['returnValues']:
                            if type(return_value_value) in [str, bool, int, float]: # TODO: How does GetAtt handle arrays/objects?
                                event['model'][return_value_name] = return_value_value
                if 'instances' in tfshow['values']['root_module']['resources'][0]:
                    for tfreturnname, return_value_value in tfshow['values']['root_module']['resources'][0]['instances'][0]['attributes'].items():
                        return_value_name = tf_to_cfn_str(tfreturnname)
                        if return_value_name in event['returnValues']:
                            if type(return_value_value) in [str, bool, int, float]: # TODO: How does GetAtt handle arrays/objects?
                                event['model'][return_value_name] = return_value_value
            except:
                pass

            print("Storing model state")
            s3client.put_object(Body=json.dumps(event['model']).encode(), Bucket=statebucketname, Key="state/{}/{}.model.json".format(event['terraformTypeName'], trackingid))

    except Exception as e:
        print(str(e))
        status = {
            'status': 'failed',
            'error': str(e)
        }

    s3client.put_object(Body=json.dumps(status).encode(), Bucket=statebucketname, Key="status/{}.json".format(operationid))

    try:
        os.remove("/tmp/main.tf.json")
    except:
        pass
    try:
        os.remove("/tmp/terraform.tfstate")
    except:
        pass
