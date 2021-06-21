import logging
import json
import os
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
TYPE_NAME = "TF::Fastly::ServiceV1"

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint


def check_progress(operationid, trackingid, progress, session):
    LOG.warn("Retrieving existing operation status ({})".format(operationid))

    s3client = session.client('s3')
    stsclient = session.client('sts')
    
    callerid = stsclient.get_caller_identity()
    statebucketname = "cfntf-{}-{}".format(os.environ['AWS_REGION'], callerid.get('Account'))

    try:
        result = json.loads(s3client.get_object(Bucket=statebucketname, Key="status/{}.json".format(operationid))['Body'].read())
        s3client.delete_object(Bucket=statebucketname, Key="status/{}.json".format(operationid))

        if result['status'] == 'completed':
            progress.status = OperationStatus.SUCCESS

            # retrieve model
            try:
                state_str = s3client.get_object(Bucket=statebucketname, Key="state/fastly_service_v1/{}.model.json".format(trackingid))['Body'].read()
                if state_str == "":
                    state_str = "{}"
                model_state = json.loads(state_str)
                
                for k,v in model_state.items():
                    setattr(progress.resourceModel, k, v)
            except Exception as e:
                LOG.warn(str(e))

            LOG.warn("Action complete")
        else:
            progress.status = OperationStatus.FAILED
            if 'error' in result:
                progress.message = result['error']
                progress.errorCode = HandlerErrorCode.GeneralServiceException
    except s3client.exceptions.NoSuchKey as e:
        progress.status = OperationStatus.FAILED
        progress.message = str(e)
        progress.errorCode = HandlerErrorCode.NotFound
    except:
        progress.callbackDelaySeconds = 20
        progress.callbackContext = {
            'trackingid': trackingid,
            'operationid': operationid,
        }
    
    return progress


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

    if callback_context.get('operationid'):
        return check_progress(callback_context.get('operationid'), callback_context.get('trackingid'), progress, session)

    LOG.warn("Starting create action")
    
    try:
        lambdaclient = session.client("lambda")

        trackingid = str(uuid4())
        operationid = str(uuid4())

        resolved_model = None
        if model: # potentially no properties set
            resolved_model = model._serialize()
        
        lambdaclient.invoke(
            FunctionName="cfntf-executor",
            InvocationType="Event",
            Payload=json.dumps({
                'action': 'CREATE',
                'trackingId': trackingid,
                'operationId': operationid,
                'model': resolved_model,
                'logicalId': request.logicalResourceIdentifier,
                'providerFullName': 'fastly/fastly',
                'providerTypeName': 'fastly',
                'terraformTypeName': 'fastly_service_v1',
                'returnValues': ["ActiveVersion", "ClonedVersion", "Id"],
            }).encode(),
        )

        progress.resourceModel.tfcfnid = trackingid
        progress.callbackDelaySeconds = 20
        progress.callbackContext = {
            'trackingid': trackingid,
            'operationid': operationid,
        }
    except lambdaclient.exceptions.ResourceNotFoundException as e:
        progress.message = "The execution infrastructure is not available. Read more at https://github.com/iann0036/cfn-tf-custom-types."
        progress.status = OperationStatus.FAILED
        progress.errorCode = HandlerErrorCode.GeneralServiceException
    except Exception as e:
        progress.status = OperationStatus.FAILED
        progress.message = str(e)
        progress.errorCode = HandlerErrorCode.InternalFailure
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

    s3client = session.client('s3')
    stsclient = session.client('sts')
    
    callerid = stsclient.get_caller_identity()
    statebucketname = "cfntf-{}-{}".format(os.environ['AWS_REGION'], callerid.get('Account'))

    if callback_context.get('operationid'):
        return check_progress(callback_context.get('operationid'), callback_context.get('trackingid'), progress, session)

    LOG.warn("Starting update action")
    
    try:
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/fastly_service_v1/{}.model.json".format(model.tfcfnid))['Body'].read()
        if state_str == "":
            state_str = "{}"
        model_state = json.loads(state_str)
    
        lambdaclient = session.client("lambda")

        trackingid = model.tfcfnid
        operationid = str(uuid4())
        
        resolved_model = None
        if model: # potentially no properties set
            resolved_model = model._serialize()
        
        lambdaclient.invoke(
            FunctionName="cfntf-executor",
            InvocationType="Event",
            Payload=json.dumps({
                'action': 'UPDATE',
                'trackingId': trackingid,
                'operationId': operationid,
                'model': resolved_model,
                'logicalId': request.logicalResourceIdentifier,
                'providerFullName': 'fastly/fastly',
                'providerTypeName': 'fastly',
                'terraformTypeName': 'fastly_service_v1',
                'returnValues': ["ActiveVersion", "ClonedVersion", "Id"],
            }).encode(),
        )

        progress.resourceModel.tfcfnid = trackingid
        progress.callbackDelaySeconds = 20
        progress.callbackContext = {
            'trackingid': trackingid,
            'operationid': operationid,
        }
    except s3client.exceptions.NoSuchKey as e:
        progress.message = str(e)
        progress.status = OperationStatus.FAILED
        progress.errorCode = HandlerErrorCode.NotFound
    except lambdaclient.exceptions.ResourceNotFoundException as e:
        progress.message = "The execution infrastructure is not available. Read more at https://github.com/iann0036/cfn-tf-custom-types."
        progress.status = OperationStatus.FAILED
        progress.errorCode = HandlerErrorCode.GeneralServiceException
    except Exception as e:
        progress.message = str(e)
        progress.status = OperationStatus.FAILED
        progress.errorCode = HandlerErrorCode.InternalFailure
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

    s3client = session.client('s3')
    stsclient = session.client('sts')
    
    callerid = stsclient.get_caller_identity()
    statebucketname = "cfntf-{}-{}".format(os.environ['AWS_REGION'], callerid.get('Account'))

    if callback_context.get('operationid'):
        ret = check_progress(callback_context.get('operationid'), callback_context.get('trackingid'), progress, session)
        ret.resourceModel = None
        return ret

    LOG.warn("Starting delete action")
    
    try:
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/fastly_service_v1/{}.model.json".format(model.tfcfnid))['Body'].read()
        if state_str == "":
            state_str = "{}"
        model_state = json.loads(state_str)

        lambdaclient = session.client("lambda")

        trackingid = model.tfcfnid
        operationid = str(uuid4())
        
        resolved_model = None
        if model: # potentially no properties set
            resolved_model = model._serialize()
        
        lambdaclient.invoke(
            FunctionName="cfntf-executor",
            InvocationType="Event",
            Payload=json.dumps({
                'action': 'DELETE',
                'trackingId': trackingid,
                'operationId': operationid,
                'model': resolved_model,
                'logicalId': request.logicalResourceIdentifier,
                'providerFullName': 'fastly/fastly',
                'providerTypeName': 'fastly',
                'terraformTypeName': 'fastly_service_v1',
                'returnValues': ["ActiveVersion", "ClonedVersion", "Id"],
            }).encode(),
        )

        progress.resourceModel.tfcfnid = trackingid
        progress.callbackDelaySeconds = 20
        progress.callbackContext = {
            'trackingid': trackingid,
            'operationid': operationid,
        }
    except s3client.exceptions.NoSuchKey as e:
        progress.message = str(e)
        progress.status = OperationStatus.FAILED
        progress.errorCode = HandlerErrorCode.NotFound
    except lambdaclient.exceptions.ResourceNotFoundException as e:
        progress.message = "The execution infrastructure is not available. Read more at https://github.com/iann0036/cfn-tf-custom-types."
        progress.status = OperationStatus.FAILED
        progress.errorCode = HandlerErrorCode.GeneralServiceException
    except Exception as e:
        progress.message = str(e)
        progress.status = OperationStatus.FAILED
        progress.errorCode = HandlerErrorCode.InternalFailure
    return progress


@resource.handler(Action.READ)
def read_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState

    s3client = session.client('s3')
    stsclient = session.client('sts')
    
    callerid = stsclient.get_caller_identity()
    statebucketname = "cfntf-{}-{}".format(os.environ['AWS_REGION'], callerid.get('Account'))
    
    # retrieve model
    try:
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/fastly_service_v1/{}.model.json".format(model.tfcfnid))['Body'].read()
        if state_str == "":
            state_str = "{}"
        model_state = json.loads(state_str)
        
        for k,v in model_state.items():
            setattr(model, k, v)
        
        return ProgressEvent(
            status=OperationStatus.SUCCESS,
            resourceModel=model,
        )
    except Exception as e:
        LOG.warn(str(e))

    return ProgressEvent(
        status=OperationStatus.FAILED,
        errorCode=HandlerErrorCode.NotFound,
        resourceModel=model,
    )


@resource.handler(Action.LIST)
def list_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    s3client = session.client('s3')
    stsclient = session.client('sts')
    
    callerid = stsclient.get_caller_identity()
    statebucketname = "cfntf-{}-{}".format(os.environ['AWS_REGION'], callerid.get('Account'))
    
    # retrieve models
    try:
        models = []
        state_objects = s3client.list_objects_v2(
            Bucket=statebucketname,
            MaxKeys=1000,
            Prefix='state/fastly_service_v1/'
        )['Contents']

        for state_object in state_objects:
            if state_object['Key'].endswith(".model.json"):
                model = ResourceModel(tfcfnid=state_object['Key'].replace(".model.json", ""), Activate=None, ActiveVersion=None, ClonedVersion=None, Comment=None, DefaultHost=None, DefaultTtl=None, ForceDestroy=None, Id=None, Name=None, VersionComment=None, Acl=None, Backend=None, Bigquerylogging=None, Blobstoragelogging=None, CacheSetting=None, Condition=None, Dictionary=None, Director=None, Domain=None, Dynamicsnippet=None, Gcslogging=None, Gzip=None, Header=None, Healthcheck=None, Httpslogging=None, Logentries=None, LoggingCloudfiles=None, LoggingDatadog=None, LoggingDigitalocean=None, LoggingElasticsearch=None, LoggingFtp=None, LoggingGooglepubsub=None, LoggingHeroku=None, LoggingHoneycomb=None, LoggingKafka=None, LoggingKinesis=None, LoggingLoggly=None, LoggingLogshuttle=None, LoggingNewrelic=None, LoggingOpenstack=None, LoggingScalyr=None, LoggingSftp=None, Papertrail=None, RequestSetting=None, ResponseObject=None, S3logging=None, Snippet=None, Splunk=None, Sumologic=None, Syslog=None, Vcl=None, Waf=None)

                state_str = s3client.get_object(Bucket=statebucketname, Key=state_object['Key'])['Body'].read()
                if state_str == "":
                    state_str = "{}"
                model_state = json.loads(state_str)
                
                for k,v in model_state.items():
                    setattr(model, k, v)
                
                models.append(model)
        
        return ProgressEvent(
            status=OperationStatus.SUCCESS,
            resourceModels=models,
        )
    except Exception as e:
        LOG.warn(str(e))

    return ProgressEvent(
        status=OperationStatus.FAILED,
        errorCode=HandlerErrorCode.InternalFailure,
        resourceModels=[],
    )