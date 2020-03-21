import logging
import os, subprocess, json, re
from uuid import uuid4
from typing import Any, MutableMapping, Optional

from cloudformation_cli_python_lib import (
    Action,
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
    Resource,
    SessionProxy,
    exceptions,
)

from .models import ResourceHandlerRequest, ResourceModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "Terraform::Google::CloudSchedulerJob"

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint

def check_call(args, cwd):
    proc = subprocess.Popen(args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd)
    stdout, stderr = proc.communicate()
    LOG.warn(stdout.decode('utf-8'))
    LOG.warn(stderr.decode('utf-8'))
    if proc.returncode != 0:
        raise exceptions.InternalFailure(f"{stderr.decode('utf-8')}")
    
    return stdout

def cfn_to_tf_str(obj):
    return re.sub('([A-Z]{1})', r'_\1', obj).lower()[1:]

def parse_obj(obj):
    if isinstance(obj, dict):
        ret = {}
        for prop, value in obj.items():
            ret[cfn_to_tf_str(prop)] = parse_obj(value)

        return ret

    return obj

@resource.handler(Action.CREATE)
def create_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )

    LOG.warn("Starting create action")
    
    try:
        s3client = session.client("s3")
        stsclient = session.client("sts")
        secretsmanagerclient = session.client("secretsmanager")

        trackingid = str(uuid4())
        callerid = stsclient.get_caller_identity()
        statebucketname = "cfntfstate-{}-{}".format(os.environ['AWS_REGION'], callerid.get('Account'))

        tf = {
            "provider": {
                "google": {}
            },
            "resource": {
                "google_cloud_scheduler_job": {}
            }
        }
        tf['resource']['google_cloud_scheduler_job'][request.logicalResourceIdentifier] = {}

        if "google" == "aws":
            creds = session.credentials
            tf["provider"]["google"] = {
                "access_key": creds.access_key,
                "secret_key": creds.secret_key,
                "token": creds.token
            }

        try:
            secretstr = secretsmanagerclient.get_secret_value(SecretId="terraform/{}".format("google"))['SecretString']
            tf["provider"]["google"].update(json.loads(secretstr))
        except:
            pass

        for prop, value in vars(model).items():
            if value is not None and prop != "tfcfnid":
                tf['resource']['google_cloud_scheduler_job'][request.logicalResourceIdentifier][cfn_to_tf_str(prop)] = parse_obj(value)

        with open("/tmp/main.tf.json", "w") as f:
            f.write(json.dumps(tf, indent=2))

        LOG.warn("Initializing provider")
        check_call([os.path.dirname(os.path.realpath(__file__)) + '/terraform', 'init', '-no-color'], "/tmp/")
        LOG.warn("Executing create")
        check_call([os.path.dirname(os.path.realpath(__file__)) + '/terraform', 'apply', '-auto-approve', '-no-color'], "/tmp/")

        LOG.warn("Storing result")
        with open("/tmp/terraform.tfstate", "rb") as f:
            s3client.upload_fileobj(f, statebucketname, "{}.tfstate".format(trackingid))

        os.remove("/tmp/main.tf.json")
        os.remove("/tmp/terraform.tfstate")

        model.tfcfnid = trackingid

        progress.status = OperationStatus.SUCCESS
    except Exception as e:
        progress.message = str(e)
        progress.status = OperationStatus.FAILED
    return progress


@resource.handler(Action.UPDATE)
def update_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )

    LOG.warn("Starting update action")
    
    try:
        s3client = session.client("s3")
        stsclient = session.client("sts")
        secretsmanagerclient = session.client("secretsmanager")

        trackingid = model.tfcfnid
        callerid = stsclient.get_caller_identity()
        statebucketname = "cfntfstate-{}-{}".format(os.environ['AWS_REGION'], callerid.get('Account'))

        tf = {
            "provider": {
                "google": {}
            },
            "resource": {
                "google_cloud_scheduler_job": {}
            }
        }
        tf['resource']['google_cloud_scheduler_job'][request.logicalResourceIdentifier] = {}

        if "google" == "aws":
            creds = session.credentials
            tf["provider"]["google"] = {
                "access_key": creds.access_key,
                "secret_key": creds.secret_key,
                "token": creds.token
            }

        try:
            secretstr = secretsmanagerclient.get_secret_value(SecretId="terraform/{}".format("google"))['SecretString']
            tf["provider"]["google"].update(json.loads(secretstr))
        except:
            pass

        for prop, value in vars(model).items():
            if value is not None and prop != "tfcfnid":
                tf['resource']['google_cloud_scheduler_job'][request.logicalResourceIdentifier][cfn_to_tf_str(prop)] = parse_obj(value)
        
        LOG.warn(json.dumps(tf))

        with open("/tmp/main.tf.json", "w") as f:
            f.write(json.dumps(tf, indent=2))

        LOG.warn("Initializing provider")
        check_call([os.path.dirname(os.path.realpath(__file__)) + '/terraform', 'init', '-no-color'], "/tmp/")
        LOG.warn("Executing update")
        check_call([os.path.dirname(os.path.realpath(__file__)) + '/terraform', 'apply', '-auto-approve', '-no-color'], "/tmp/")

        LOG.warn("Storing result")
        with open("/tmp/terraform.tfstate", "rb") as f:
            s3client.upload_fileobj(f, statebucketname, "{}.tfstate".format(trackingid))

        progress.status = OperationStatus.SUCCESS
    except Exception as e:
        progress.message = str(e)
        progress.status = OperationStatus.FAILED
    return progress


@resource.handler(Action.DELETE)
def delete_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )

    LOG.warn("Starting delete action")
    
    try:
        s3client = session.client("s3")
        stsclient = session.client("sts")
        secretsmanagerclient = session.client("secretsmanager")

        trackingid = model.tfcfnid
        callerid = stsclient.get_caller_identity()
        statebucketname = "cfntfstate-{}-{}".format(os.environ['AWS_REGION'], callerid.get('Account'))

        with open('/tmp/terraform.tfstate', 'wb') as f:
            s3client.download_fileobj(statebucketname, '{}.tfstate'.format(trackingid), f)

        tf = {
            "provider": {
                "google": {}
            },
            "resource": {
                "google_cloud_scheduler_job": {}
            }
        }
        tf['resource']['google_cloud_scheduler_job'][request.logicalResourceIdentifier] = {}

        if "google" == "aws":
            creds = session.credentials
            tf["provider"]["google"] = {
                "access_key": creds.access_key,
                "secret_key": creds.secret_key,
                "token": creds.token
            }

        try:
            secretstr = secretsmanagerclient.get_secret_value(SecretId="terraform/{}".format("google"))['SecretString']
            tf["provider"]["google"].update(json.loads(secretstr))
        except:
            pass

        for prop, value in vars(model).items():
            if value is not None and prop != "tfcfnid":
                tf['resource']['google_cloud_scheduler_job'][request.logicalResourceIdentifier][cfn_to_tf_str(prop)] = parse_obj(value)
        
        LOG.warn(json.dumps(tf))

        with open("/tmp/main.tf.json", "w") as f:
            f.write(json.dumps(tf, indent=2))
        
        LOG.warn("Initializing provider")
        check_call([os.path.dirname(os.path.realpath(__file__)) + '/terraform', 'init', '-no-color'], "/tmp/")
        LOG.warn("Executing delete")
        check_call([os.path.dirname(os.path.realpath(__file__)) + '/terraform', 'destroy', '-auto-approve', '-no-color'], "/tmp/")

        LOG.warn("Deleting state S3 object")
        s3client.delete_object(
            Bucket=statebucketname,
            Key="{}.tfstate".format(trackingid)
        )

        progress.status = OperationStatus.SUCCESS
    except Exception as e:
        progress.message = str(e)
        progress.status = OperationStatus.FAILED
    return progress


@resource.handler(Action.READ)
def read_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    # TODO: put code here
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=model,
    )


@resource.handler(Action.LIST)
def list_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    # TODO: put code here
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModels=[],
    )