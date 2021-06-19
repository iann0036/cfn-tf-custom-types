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
TYPE_NAME = "TF::AVI::Serviceenginegroup"

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
                state_str = s3client.get_object(Bucket=statebucketname, Key="state/avi_serviceenginegroup/{}.model.json".format(trackingid))['Body'].read()
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
                'providerFullName': 'vmware/avi',
                'providerTypeName': 'avi',
                'terraformTypeName': 'avi_serviceenginegroup',
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/avi_serviceenginegroup/{}.model.json".format(model.tfcfnid))['Body'].read()
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
                'providerFullName': 'vmware/avi',
                'providerTypeName': 'avi',
                'terraformTypeName': 'avi_serviceenginegroup',
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/avi_serviceenginegroup/{}.model.json".format(model.tfcfnid))['Body'].read()
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
                'providerFullName': 'vmware/avi',
                'providerTypeName': 'avi',
                'terraformTypeName': 'avi_serviceenginegroup',
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/avi_serviceenginegroup/{}.model.json".format(model.tfcfnid))['Body'].read()
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
            Prefix='state/avi_serviceenginegroup/'
        )['Contents']

        for state_object in state_objects:
            if state_object['Key'].endswith(".model.json"):
                model = ResourceModel(tfcfnid=state_object['Key'].replace(".model.json", ""), AcceleratedNetworking=None, ActiveStandby=None, AggressiveFailureDetection=None, Algo=None, AllowBurst=None, AppCachePercent=None, AppCacheThreshold=None, AppLearningMemoryPercent=None, ArchiveShmLimit=None, AsyncSsl=None, AsyncSslThreads=None, AutoRebalance=None, AutoRebalanceCapacityPerSe=None, AutoRebalanceCriteria=None, AutoRebalanceInterval=None, AutoRedistributeActiveStandbyLoad=None, AvailabilityZoneRefs=None, BgpStateUpdateInterval=None, BufferSe=None, CloudRef=None, CompressIpRulesForEachNsSubnet=None, ConfigDebugsOnAllCores=None, ConnectionMemoryPercentage=None, CoreShmAppCache=None, CoreShmAppLearning=None, CpuReserve=None, CpuSocketAffinity=None, CustomSecuritygroupsData=None, CustomSecuritygroupsMgmt=None, DataNetworkId=None, DatascriptTimeout=None, DedicatedDispatcherCore=None, Description=None, DisableAviSecuritygroups=None, DisableCsumOffloads=None, DisableFlowProbes=None, DisableGro=None, DisableSeMemoryCheck=None, DisableTso=None, DiskPerSe=None, DistributeLoadActiveStandby=None, DistributeQueues=None, DistributeVnics=None, DpAggressiveHbFrequency=None, DpAggressiveHbTimeoutCount=None, DpHbFrequency=None, DpHbTimeoutCount=None, EnableGratarpPermanent=None, EnableHsmPriming=None, EnableMultiLb=None, EnablePcapTxRing=None, EphemeralPortrangeEnd=None, EphemeralPortrangeStart=None, ExtraConfigMultiplier=None, ExtraSharedConfigMemory=None, FlowTableNewSynMaxEntries=None, FreeListSize=None, GratarpPermanentPeriodicity=None, HaMode=None, HandlePerPktAttack=None, HardwaresecuritymodulegroupRef=None, HeapMinimumConfigMemory=None, HmOnStandby=None, HostAttributeKey=None, HostAttributeValue=None, HostGatewayMonitor=None, Hypervisor=None, Id=None, IgnoreRttThreshold=None, IngressAccessData=None, IngressAccessMgmt=None, InstanceFlavor=None, LeastLoadCoreSelection=None, LicenseTier=None, LicenseType=None, LogDisksz=None, LogMallocFailure=None, MaxConcurrentExternalHm=None, MaxCpuUsage=None, MaxMemoryPerMempool=None, MaxNumSeDps=None, MaxPublicIpsPerLb=None, MaxQueuesPerVnic=None, MaxRulesPerLb=None, MaxScaleoutPerVs=None, MaxSe=None, MaxVsPerSe=None, MemReserve=None, MemoryForConfigUpdate=None, MemoryPerSe=None, MgmtNetworkRef=None, MinCpuUsage=None, MinScaleoutPerVs=None, MinSe=None, MinimumConnectionMemory=None, NLogStreamingThreads=None, Name=None, NonSignificantLogThrottle=None, NumDispatcherCores=None, NumFlowCoresSumChangesToIgnore=None, ObjsyncPort=None, OpenstackAvailabilityZones=None, OpenstackMgmtNetworkName=None, OpenstackMgmtNetworkUuid=None, OsReservedMemory=None, PcapTxMode=None, PcapTxRingRdBalancingFactor=None, PerApp=None, PerVsAdmissionControl=None, PlacementMode=None, RebootOnPanic=None, ResyncTimeInterval=None, SeBandwidthType=None, SeDelayedFlowDelete=None, SeDeprovisionDelay=None, SeDpHmDrops=None, SeDpIsolation=None, SeDpIsolationNumNonDpCpus=None, SeDpMaxHbVersion=None, SeDpVnicQueueStallEventSleep=None, SeDpVnicQueueStallThreshold=None, SeDpVnicQueueStallTimeout=None, SeDpVnicRestartOnQueueStallCount=None, SeDpVnicStallSeRestartWindow=None, SeDpdkPmd=None, SeFlowProbeRetries=None, SeFlowProbeRetryTimer=None, SeHyperthreadedMode=None, SeIpEncapIpc=None, SeKniBurstFactor=None, SeL3EncapIpc=None, SeLro=None, SeMpRingRetryCount=None, SeMtu=None, SeNamePrefix=None, SePcapLookahead=None, SePcapPktCount=None, SePcapPktSz=None, SePcapQdiscBypass=None, SePcapReinitFrequency=None, SePcapReinitThreshold=None, SeProbePort=None, SeRumSamplingNavInterval=None, SeRumSamplingNavPercent=None, SeRumSamplingResInterval=None, SeRumSamplingResPercent=None, SeSbDedicatedCore=None, SeSbThreads=None, SeThreadMultiplier=None, SeTunnelMode=None, SeTunnelUdpPort=None, SeTxBatchSize=None, SeTxqThreshold=None, SeUdpEncapIpc=None, SeUseDpdk=None, SeVnicTxSwQueueFlushFrequency=None, SeVnicTxSwQueueSize=None, SeVsHbMaxPktsInBatch=None, SeVsHbMaxVsInPkt=None, SelfSeElection=None, ShmMinimumConfigMemory=None, SignificantLogThrottle=None, SslPreprocessSniHostname=None, TenantRef=None, TransientSharedMemoryMax=None, UdfLogThrottle=None, UseHyperthreadedCores=None, UseObjsync=None, UseStandardAlb=None, Uuid=None, VcenterDatastoreMode=None, VcenterDatastoresInclude=None, VcenterFolder=None, VcpusPerSe=None, VsHostRedundancy=None, VsScaleinTimeout=None, VsScaleinTimeoutForUpgrade=None, VsScaleoutTimeout=None, VsSeScaleoutAdditionalWaitTime=None, VsSeScaleoutReadyTimeout=None, VsSwitchoverTimeout=None, VssPlacementEnabled=None, WafMempool=None, WafMempoolSize=None, CustomTag=None, GcpConfig=None, InstanceFlavorInfo=None, Iptables=None, Labels=None, MgmtSubnet=None, ObjsyncConfig=None, RealtimeSeMetrics=None, SeDosProfile=None, SeGroupAnalyticsPolicy=None, SeRlProp=None, SeTracertPortRange=None, ServiceIp6Subnets=None, ServiceIpSubnets=None, VcenterClusters=None, VcenterDatastores=None, VcenterHosts=None, Vcenters=None, VipAsg=None, VssPlacement=None)

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
