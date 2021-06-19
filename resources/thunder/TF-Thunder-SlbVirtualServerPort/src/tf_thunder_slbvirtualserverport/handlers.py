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
TYPE_NAME = "TF::Thunder::SlbVirtualServerPort"

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
                state_str = s3client.get_object(Bucket=statebucketname, Key="state/thunder_slb_virtual_server_port/{}.model.json".format(trackingid))['Body'].read()
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
                'providerFullName': 'a10networks/thunder',
                'providerTypeName': 'thunder',
                'terraformTypeName': 'thunder_slb_virtual_server_port',
                'returnValues': ["Id"],
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/thunder_slb_virtual_server_port/{}.model.json".format(model.tfcfnid))['Body'].read()
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
                'providerFullName': 'a10networks/thunder',
                'providerTypeName': 'thunder',
                'terraformTypeName': 'thunder_slb_virtual_server_port',
                'returnValues': ["Id"],
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/thunder_slb_virtual_server_port/{}.model.json".format(model.tfcfnid))['Body'].read()
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
                'providerFullName': 'a10networks/thunder',
                'providerTypeName': 'thunder',
                'terraformTypeName': 'thunder_slb_virtual_server_port',
                'returnValues': ["Id"],
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/thunder_slb_virtual_server_port/{}.model.json".format(model.tfcfnid))['Body'].read()
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
            Prefix='state/thunder_slb_virtual_server_port/'
        )['Contents']

        for state_object in state_objects:
            if state_object['Key'].endswith(".model.json"):
                model = ResourceModel(tfcfnid=state_object['Key'].replace(".model.json", ""), Action=None, AltProtocol1=None, AltProtocol2=None, AlternatePort=None, AlternatePortNumber=None, Auto=None, ClientipStickyNat=None, ConnLimit=None, CpuCompute=None, DefSelectionIfPrefFailed=None, EnablePlayeridCheck=None, EthFwd=None, EthRev=None, Expand=None, ExtendedStats=None, ForceRoutingMode=None, GslbEnable=None, GtpSessionLb=None, HaConnMirror=None, Id=None, IgnoreGlobal=None, IpMapList=None, Ipinip=None, L7HardwareAssist=None, MemoryCompute=None, MessageSwitching=None, Name=None, NoAutoUpOnAflex=None, NoDestNat=None, NoLogging=None, OnSyn=None, OptimizationLevel=None, PTemplateSipShared=None, PersistType=None, Pool=None, PoolShared=None, PortNumber=None, PortTranslation=None, Precedence=None, Protocol=None, Range=None, Rate=None, RedirectToHttps=None, ReqFail=None, Reset=None, ResetOnServerSelectionFail=None, RtpSipCallIdMatch=None, ScaleoutBucketCount=None, ScaleoutDeviceGroup=None, Secs=None, ServSelFail=None, ServiceGroup=None, SharedPartitionCacheTemplate=None, SharedPartitionClientSslTemplate=None, SharedPartitionConnectionReuseTemplate=None, SharedPartitionDblbTemplate=None, SharedPartitionDiameterTemplate=None, SharedPartitionDnsTemplate=None, SharedPartitionDohTemplate=None, SharedPartitionDynamicServiceTemplate=None, SharedPartitionExternalServiceTemplate=None, SharedPartitionFixTemplate=None, SharedPartitionHttpPolicyTemplate=None, SharedPartitionHttpTemplate=None, SharedPartitionImapPop3Template=None, SharedPartitionPersistCookieTemplate=None, SharedPartitionPersistDestinationIpTemplate=None, SharedPartitionPersistSourceIpTemplate=None, SharedPartitionPersistSslSidTemplate=None, SharedPartitionPolicyTemplate=None, SharedPartitionPool=None, SharedPartitionServerSslTemplate=None, SharedPartitionSmppTemplate=None, SharedPartitionSmtpTemplate=None, SharedPartitionTcp=None, SharedPartitionTcpProxyTemplate=None, SharedPartitionUdp=None, SharedPartitionVirtualPortTemplate=None, SkipRevHash=None, SnatOnVip=None, StatsDataAction=None, SubstituteSourceMac=None, SupportHttp2=None, SynCookie=None, TemplateCache=None, TemplateCacheShared=None, TemplateClientSsh=None, TemplateClientSsl=None, TemplateClientSslShared=None, TemplateConnectionReuse=None, TemplateConnectionReuseShared=None, TemplateDblb=None, TemplateDblbShared=None, TemplateDiameter=None, TemplateDiameterShared=None, TemplateDns=None, TemplateDnsShared=None, TemplateDoh=None, TemplateDohShared=None, TemplateDynamicService=None, TemplateDynamicServiceShared=None, TemplateExternalService=None, TemplateExternalServiceShared=None, TemplateFileInspection=None, TemplateFix=None, TemplateFixShared=None, TemplateFtp=None, TemplateHttp=None, TemplateHttpPolicy=None, TemplateHttpPolicyShared=None, TemplateHttpShared=None, TemplateImapPop3=None, TemplateImapPop3Shared=None, TemplateMqtt=None, TemplatePersistCookie=None, TemplatePersistCookieShared=None, TemplatePersistDestinationIp=None, TemplatePersistDestinationIpShared=None, TemplatePersistSourceIp=None, TemplatePersistSourceIpShared=None, TemplatePersistSslSid=None, TemplatePersistSslSidShared=None, TemplatePolicy=None, TemplatePolicyShared=None, TemplateReqmodIcap=None, TemplateRespmodIcap=None, TemplateScaleout=None, TemplateServerSsh=None, TemplateServerSsl=None, TemplateServerSslShared=None, TemplateSip=None, TemplateSipShared=None, TemplateSmpp=None, TemplateSmppShared=None, TemplateSmtp=None, TemplateSmtpShared=None, TemplateSsli=None, TemplateTcp=None, TemplateTcpProxy=None, TemplateTcpProxyClient=None, TemplateTcpProxyServer=None, TemplateTcpProxyShared=None, TemplateTcpShared=None, TemplateUdp=None, TemplateUdpShared=None, TemplateVirtualPort=None, TemplateVirtualPortShared=None, TrunkFwd=None, TrunkRev=None, UseAlternatePort=None, UseCgnv6=None, UseDefaultIfNoServer=None, UseRcvHopForResp=None, UserTag=None, Uuid=None, View=None, WafTemplate=None, WhenDown=None, WhenDownProtocol2=None, AclIdList=None, AclNameList=None, AflexScripts=None, AuthCfg=None, SamplingEnable=None)

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
