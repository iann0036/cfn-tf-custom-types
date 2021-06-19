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
TYPE_NAME = "TF::Thunder::SlbTemplateClientSsl"

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
                state_str = s3client.get_object(Bucket=statebucketname, Key="state/thunder_slb_template_client_ssl/{}.model.json".format(trackingid))['Body'].read()
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
                'terraformTypeName': 'thunder_slb_template_client_ssl',
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/thunder_slb_template_client_ssl/{}.model.json".format(model.tfcfnid))['Body'].read()
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
                'terraformTypeName': 'thunder_slb_template_client_ssl',
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/thunder_slb_template_client_ssl/{}.model.json".format(model.tfcfnid))['Body'].read()
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
                'terraformTypeName': 'thunder_slb_template_client_ssl',
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/thunder_slb_template_client_ssl/{}.model.json".format(model.tfcfnid))['Body'].read()
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
            Prefix='state/thunder_slb_template_client_ssl/'
        )['Contents']

        for state_object in state_objects:
            if state_object['Key'].endswith(".model.json"):
                model = ResourceModel(tfcfnid=state_object['Key'].replace(".model.json", ""), AdGroupList=None, AlertType=None, AuthSg=None, AuthSgDn=None, AuthSgFilter=None, AuthUsername=None, AuthUsernameAttribute=None, AuthenName=None, Authorization=None, BypassCertIssuerClassListName=None, BypassCertSanClassListName=None, BypassCertSubjectClassListName=None, CachePersistenceListName=None, CaseInsensitive=None, Cert=None, CertAltPartitionShared=None, CertAlternate=None, CertRevokeAction=None, CertSharedStr=None, CertUnknownAction=None, ChainCert=None, ChainCertSharedStr=None, ClassListName=None, ClientAuthCaseInsensitive=None, ClientAuthClassList=None, ClientCertificate=None, CloseNotify=None, Dgversion=None, DhType=None, DirectClientServerAuth=None, DisableSslv3=None, EarlyData=None, EnableTlsAlertLogging=None, ExceptionAdGroupList=None, ExceptionCertificateIssuerClName=None, ExceptionCertificateSanClName=None, ExceptionCertificateSubjectClName=None, ExceptionSniClName=None, ExceptionUserNameList=None, ExpireHours=None, ForwardEncrypted=None, ForwardPassphrase=None, ForwardProxyAltSign=None, ForwardProxyBlockMessage=None, ForwardProxyCaCert=None, ForwardProxyCaKey=None, ForwardProxyCertCacheLimit=None, ForwardProxyCertCacheTimeout=None, ForwardProxyCertExpiry=None, ForwardProxyCertNotReadyAction=None, ForwardProxyCertRevokeAction=None, ForwardProxyCertUnknownAction=None, ForwardProxyCrlDisable=None, ForwardProxyDecryptedDscp=None, ForwardProxyDecryptedDscpBypass=None, ForwardProxyEnable=None, ForwardProxyFailsafeDisable=None, ForwardProxyLogDisable=None, ForwardProxyNoSharedCipherAction=None, ForwardProxyNoSniAction=None, ForwardProxyOcspDisable=None, ForwardProxyRequireSniCertMatched=None, ForwardProxySelfsignRedir=None, ForwardProxySslVersion=None, ForwardProxyVerifyCertFailAction=None, FpAltCert=None, FpAltEncrypted=None, FpAltKey=None, FpAltPassphrase=None, FpAltShared=None, FpCaKeyShared=None, FpCaShared=None, FpCertExtAiaCaIssuers=None, FpCertExtAiaOcsp=None, FpCertExtCrldp=None, FpCertFetchAutonat=None, FpCertFetchAutonatPrecedence=None, FpCertFetchNatpoolName=None, FpCertFetchNatpoolNameShared=None, FpCertFetchNatpoolPrecedence=None, HandshakeLoggingEnable=None, HsmType=None, Id=None, InspectCertificateIssuerClName=None, InspectCertificateSanClName=None, InspectCertificateSubjectClName=None, InspectListName=None, Key=None, KeyAltEncrypted=None, KeyAltPartitionShared=None, KeyAltPassphrase=None, KeyAlternate=None, KeyEncrypted=None, KeyPassphrase=None, KeySharedEncrypted=None, KeySharedPassphrase=None, KeySharedStr=None, LdapBaseDnFromCert=None, LdapSearchFilter=None, LocalLogging=None, Name=None, NoAntiReplay=None, NoSharedCipherAction=None, NonSslBypassL4session=None, NonSslBypassServiceGroup=None, Notafter=None, Notafterday=None, Notaftermonth=None, Notafteryear=None, Notbefore=None, Notbeforeday=None, Notbeforemonth=None, Notbeforeyear=None, OcspStapling=None, OcspstCaCert=None, OcspstOcsp=None, OcspstSg=None, OcspstSgDays=None, OcspstSgHours=None, OcspstSgMinutes=None, OcspstSgTimeout=None, OcspstSrvr=None, OcspstSrvrDays=None, OcspstSrvrHours=None, OcspstSrvrMinutes=None, OcspstSrvrTimeout=None, RenegotiationDisable=None, RequireWebCategory=None, ServerNameAutoMap=None, SessionCacheSize=None, SessionCacheTimeout=None, SessionTicketDisable=None, SessionTicketLifetime=None, SharedPartitionCipherTemplate=None, SharedPartitionPool=None, SniEnableLog=None, SslFalseStartDisable=None, SsliLogging=None, Sslilogging=None, Sslv2BypassServiceGroup=None, TemplateCipher=None, TemplateCipherShared=None, TemplateHsm=None, UserNameList=None, UserTag=None, Uuid=None, VerifyCertFailAction=None, Version=None, BypassCertIssuerMultiClassList=None, BypassCertSanMultiClassList=None, BypassCertSubjectMultiClassList=None, CaCerts=None, CertificateIssuerContainsList=None, CertificateIssuerEndsWithList=None, CertificateIssuerEqualsList=None, CertificateIssuerStartsWithList=None, CertificateList=None, CertificateSanContainsList=None, CertificateSanEndsWithList=None, CertificateSanEqualsList=None, CertificateSanStartsWithList=None, CertificateSubjectContainsList=None, CertificateSubjectEndsWithList=None, CertificateSubjectEqualsList=None, CertificateSubjectStartsWithList=None, CipherWithoutPrioList=None, ClientAuthContainsList=None, ClientAuthEndsWithList=None, ClientAuthEqualsList=None, ClientAuthStartsWithList=None, ContainsList=None, CrlCerts=None, EcList=None, EndsWithList=None, EqualsList=None, ExceptionWebCategory=None, ExceptionWebReputation=None, ForwardProxyTrustedCaLists=None, MultiClassList=None, ReqCaLists=None, ServerNameList=None, StartsWithList=None, WebCategory=None, WebReputation=None)

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
