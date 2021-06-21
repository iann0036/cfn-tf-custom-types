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
TYPE_NAME = "TF::FortiOS::FirewallPolicy"

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
                state_str = s3client.get_object(Bucket=statebucketname, Key="state/fortios_firewall_policy/{}.model.json".format(trackingid))['Body'].read()
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
                'providerFullName': 'fortinetdev/fortios',
                'providerTypeName': 'fortios',
                'terraformTypeName': 'fortios_firewall_policy',
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/fortios_firewall_policy/{}.model.json".format(model.tfcfnid))['Body'].read()
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
                'providerFullName': 'fortinetdev/fortios',
                'providerTypeName': 'fortios',
                'terraformTypeName': 'fortios_firewall_policy',
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/fortios_firewall_policy/{}.model.json".format(model.tfcfnid))['Body'].read()
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
                'providerFullName': 'fortinetdev/fortios',
                'providerTypeName': 'fortios',
                'terraformTypeName': 'fortios_firewall_policy',
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/fortios_firewall_policy/{}.model.json".format(model.tfcfnid))['Body'].read()
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
            Prefix='state/fortios_firewall_policy/'
        )['Contents']

        for state_object in state_objects:
            if state_object['Key'].endswith(".model.json"):
                model = ResourceModel(tfcfnid=state_object['Key'].replace(".model.json", ""), Action=None, AntiReplay=None, ApplicationList=None, AuthCert=None, AuthPath=None, AuthRedirectAddr=None, AutoAsicOffload=None, AvProfile=None, BlockNotification=None, CaptivePortalExempt=None, CapturePacket=None, CifsProfile=None, Comments=None, DecryptedTrafficMirror=None, DelayTcpNpuSession=None, DiffservForward=None, DiffservReverse=None, DiffservcodeForward=None, DiffservcodeRev=None, Disclaimer=None, DlpSensor=None, DnsfilterProfile=None, Dsri=None, DstaddrNegate=None, DynamicSortSubtable=None, EmailCollect=None, EmailfilterProfile=None, FileFilterProfile=None, FirewallSessionDirty=None, Fixedport=None, Fsso=None, FssoAgentForNtlm=None, GeoipAnycast=None, GeoipMatch=None, GlobalLabel=None, HttpPolicyRedirect=None, IcapProfile=None, Id=None, IdentityBasedRoute=None, Inbound=None, InspectionMode=None, InternetService=None, InternetServiceNegate=None, InternetServiceSrc=None, InternetServiceSrcNegate=None, Ippool=None, IpsSensor=None, Label=None, LearningMode=None, Logtraffic=None, LogtrafficStart=None, MatchVip=None, MatchVipOnly=None, Name=None, Nat=None, Natinbound=None, Natip=None, Natoutbound=None, Ntlm=None, NtlmGuest=None, Outbound=None, PerIpShaper=None, PermitAnyHost=None, PermitStunHost=None, Policyid=None, ProfileGroup=None, ProfileProtocolOptions=None, ProfileType=None, RadiusMacAuthBypass=None, RedirectUrl=None, ReplacemsgOverrideGroup=None, ReputationDirection=None, ReputationMinimum=None, Rsso=None, RtpNat=None, ScanBotnetConnections=None, Schedule=None, ScheduleTimeout=None, SendDenyPacket=None, ServiceNegate=None, SessionTtl=None, SpamfilterProfile=None, SrcaddrNegate=None, SshFilterProfile=None, SshPolicyRedirect=None, SslMirror=None, SslSshProfile=None, Status=None, TcpMssReceiver=None, TcpMssSender=None, TcpSessionWithoutSyn=None, TimeoutSendRst=None, Tos=None, TosMask=None, TosNegate=None, TrafficShaper=None, TrafficShaperReverse=None, UtmStatus=None, Uuid=None, Vdomparam=None, VlanCosFwd=None, VlanCosRev=None, VlanFilter=None, VoipProfile=None, Vpntunnel=None, WafProfile=None, Wanopt=None, WanoptDetection=None, WanoptPassiveOpt=None, WanoptPeer=None, WanoptProfile=None, Wccp=None, Webcache=None, WebcacheHttps=None, WebfilterProfile=None, WebproxyForwardServer=None, WebproxyProfile=None, Wsso=None, AppCategory=None, AppGroup=None, Application=None, CustomLogFields=None, Devices=None, Dstaddr=None, Dstaddr6=None, Dstintf=None, FssoGroups=None, Groups=None, InternetServiceCustom=None, InternetServiceCustomGroup=None, InternetServiceGroup=None, InternetServiceId=None, InternetServiceName=None, InternetServiceSrcCustom=None, InternetServiceSrcCustomGroup=None, InternetServiceSrcGroup=None, InternetServiceSrcId=None, InternetServiceSrcName=None, NtlmEnabledBrowsers=None, Poolname=None, Poolname6=None, RtpAddr=None, Service=None, SrcVendorMac=None, Srcaddr=None, Srcaddr6=None, Srcintf=None, SslMirrorIntf=None, UrlCategory=None, Users=None)

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