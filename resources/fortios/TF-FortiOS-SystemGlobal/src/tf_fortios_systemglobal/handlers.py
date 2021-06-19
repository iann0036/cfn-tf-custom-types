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
TYPE_NAME = "TF::FortiOS::SystemGlobal"

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
                state_str = s3client.get_object(Bucket=statebucketname, Key="state/fortios_system_global/{}.model.json".format(trackingid))['Body'].read()
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
                'terraformTypeName': 'fortios_system_global',
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/fortios_system_global/{}.model.json".format(model.tfcfnid))['Body'].read()
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
                'terraformTypeName': 'fortios_system_global',
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/fortios_system_global/{}.model.json".format(model.tfcfnid))['Body'].read()
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
                'terraformTypeName': 'fortios_system_global',
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/fortios_system_global/{}.model.json".format(model.tfcfnid))['Body'].read()
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
            Prefix='state/fortios_system_global/'
        )['Contents']

        for state_object in state_objects:
            if state_object['Key'].endswith(".model.json"):
                model = ResourceModel(tfcfnid=state_object['Key'].replace(".model.json", ""), AdminConcurrent=None, AdminConsoleTimeout=None, AdminHstsMaxAge=None, AdminHttpsPkiRequired=None, AdminHttpsRedirect=None, AdminHttpsSslVersions=None, AdminLockoutDuration=None, AdminLockoutThreshold=None, AdminLoginMax=None, AdminMaintainer=None, AdminPort=None, AdminRestrictLocal=None, AdminScp=None, AdminServerCert=None, AdminSport=None, AdminSshGraceTime=None, AdminSshPassword=None, AdminSshPort=None, AdminSshV1=None, AdminTelnet=None, AdminTelnetPort=None, Admintimeout=None, Alias=None, AllowTrafficRedirect=None, AntiReplay=None, ArpMaxEntry=None, Asymroute=None, AuthCert=None, AuthHttpPort=None, AuthHttpsPort=None, AuthKeepalive=None, AuthSessionLimit=None, AutoAuthExtensionDevice=None, AutorunLogFsck=None, AvAffinity=None, AvFailopen=None, AvFailopenSession=None, BatchCmdb=None, BlockSessionTimer=None, BrFdbMaxEntry=None, CertChainMax=None, CfgRevertTimeout=None, CfgSave=None, CheckProtocolHeader=None, CheckResetRange=None, CliAuditLog=None, CloudCommunication=None, CltCertReq=None, ComplianceCheck=None, ComplianceCheckTime=None, CpuUseThreshold=None, CsrCaAttribute=None, DailyRestart=None, DefaultServiceSourcePort=None, DeviceIdentificationActiveScanDelay=None, DeviceIdleTimeout=None, DhParams=None, DnsproxyWorkerCount=None, Dst=None, EndpointControlFdsAccess=None, EndpointControlPortalPort=None, Failtime=None, FazDiskBufferSize=None, FdsStatistics=None, FdsStatisticsPeriod=None, FecPort=None, FgdAlertSubscription=None, Fortiextender=None, FortiextenderDataPort=None, FortiextenderVlanMode=None, FortiipamIntegration=None, FortiservicePort=None, FortitokenCloud=None, GuiAllowDefaultHostname=None, GuiCertificates=None, GuiCustomLanguage=None, GuiDateFormat=None, GuiDateTimeSource=None, GuiDeviceLatitude=None, GuiDeviceLongitude=None, GuiDisplayHostname=None, GuiFirmwareUpgradeSetupWarning=None, GuiFirmwareUpgradeWarning=None, GuiForticareRegistrationSetupWarning=None, GuiFortigateCloudSandbox=None, GuiFortisandboxCloud=None, GuiIpv6=None, GuiLinesPerPage=None, GuiTheme=None, GuiWirelessOpensecurity=None, HonorDf=None, Hostname=None, Id=None, IgmpStateLimit=None, IkeEmbryonicLimit=None, Interval=None, IpSrcPortRange=None, IpsAffinity=None, IpsecAsicOffload=None, IpsecHmacOffload=None, IpsecSoftDecAsync=None, Ipv6AcceptDad=None, Ipv6AllowAnycastProbe=None, Ipv6AllowTrafficRedirect=None, IrqTimeAccounting=None, Language=None, Ldapconntimeout=None, LldpReception=None, LldpTransmission=None, LogSslConnection=None, LogUuidAddress=None, LogUuidPolicy=None, LoginTimestamp=None, LongVdomName=None, ManagementVdom=None, MaxDlpstatMemory=None, MaxRouteCacheSize=None, McTtlNotchange=None, MemoryUseThresholdExtreme=None, MemoryUseThresholdGreen=None, MemoryUseThresholdRed=None, MiglogAffinity=None, MiglogdChildren=None, MultiFactorAuthentication=None, MulticastForward=None, NdpMaxEntry=None, PerUserBal=None, PerUserBwl=None, PolicyAuthConcurrent=None, PostLoginBanner=None, PreLoginBanner=None, PrivateDataEncryption=None, ProxyAuthLifetime=None, ProxyAuthLifetimeTimeout=None, ProxyAuthTimeout=None, ProxyCipherHardwareAcceleration=None, ProxyKxpHardwareAcceleration=None, ProxyReAuthenticationMode=None, ProxyWorkerCount=None, RadiusPort=None, RebootUponConfigRestore=None, Refresh=None, Remoteauthtimeout=None, ResetSessionlessTcp=None, RestartTime=None, RevisionBackupOnLogout=None, RevisionImageAutoBackup=None, ScanunitCount=None, SecurityRatingResultSubmission=None, SecurityRatingRunOnSchedule=None, SendPmtuIcmp=None, SnatRouteChange=None, SpecialFile23Support=None, SsdTrimDate=None, SsdTrimFreq=None, SsdTrimHour=None, SsdTrimMin=None, SsdTrimWeekday=None, SshCbcCipher=None, SshHmacMd5=None, SshKexSha1=None, SshMacWeak=None, SslMinProtoVersion=None, SslStaticKeyCiphers=None, SslvpnCipherHardwareAcceleration=None, SslvpnEmsSnCheck=None, SslvpnKxpHardwareAcceleration=None, SslvpnMaxWorkerCount=None, SslvpnPluginVersionCheck=None, StrictDirtySessionCheck=None, StrongCrypto=None, SwitchController=None, SwitchControllerReservedNetwork=None, SysPerfLogInterval=None, TcpHalfcloseTimer=None, TcpHalfopenTimer=None, TcpOption=None, TcpTimewaitTimer=None, Tftp=None, Timezone=None, TpMcSkipPolicy=None, TrafficPriority=None, TrafficPriorityLevel=None, TwoFactorEmailExpiry=None, TwoFactorFacExpiry=None, TwoFactorFtkExpiry=None, TwoFactorFtmExpiry=None, TwoFactorSmsExpiry=None, UdpIdleTimer=None, UrlFilterAffinity=None, UrlFilterCount=None, UserDeviceStoreMaxDevices=None, UserDeviceStoreMaxUsers=None, UserServerCert=None, VdomAdmin=None, VdomMode=None, Vdomparam=None, VipArpRange=None, VirtualServerCount=None, VirtualServerHardwareAcceleration=None, WadAffinity=None, WadCsvcCsCount=None, WadCsvcDbCount=None, WadMemoryChangeGranularity=None, WadSourceAffinity=None, WadWorkerCount=None, WifiCaCertificate=None, WifiCertificate=None, Wimax4gUsb=None, WirelessController=None, WirelessControllerPort=None)

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
