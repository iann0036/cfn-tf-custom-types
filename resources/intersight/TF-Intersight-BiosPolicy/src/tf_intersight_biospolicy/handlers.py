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
TYPE_NAME = "TF::Intersight::BiosPolicy"

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
                state_str = s3client.get_object(Bucket=statebucketname, Key="state/intersight_bios_policy/{}.model.json".format(trackingid))['Body'].read()
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
                'providerFullName': 'CiscoDevNet/intersight',
                'providerTypeName': 'intersight',
                'terraformTypeName': 'intersight_bios_policy',
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/intersight_bios_policy/{}.model.json".format(model.tfcfnid))['Body'].read()
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
                'providerFullName': 'CiscoDevNet/intersight',
                'providerTypeName': 'intersight',
                'terraformTypeName': 'intersight_bios_policy',
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/intersight_bios_policy/{}.model.json".format(model.tfcfnid))['Body'].read()
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
                'providerFullName': 'CiscoDevNet/intersight',
                'providerTypeName': 'intersight',
                'terraformTypeName': 'intersight_bios_policy',
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
        state_str = s3client.get_object(Bucket=statebucketname, Key="state/intersight_bios_policy/{}.model.json".format(model.tfcfnid))['Body'].read()
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
            Prefix='state/intersight_bios_policy/'
        )['Contents']

        for state_object in state_objects:
            if state_object['Key'].endswith(".model.json"):
                model = ResourceModel(tfcfnid=state_object['Key'].replace(".model.json", ""), AccountMoid=None, AcsControlGpu1state=None, AcsControlGpu2state=None, AcsControlGpu3state=None, AcsControlGpu4state=None, AcsControlGpu5state=None, AcsControlGpu6state=None, AcsControlGpu7state=None, AcsControlGpu8state=None, AcsControlSlot11state=None, AcsControlSlot12state=None, AcsControlSlot13state=None, AcsControlSlot14state=None, AdditionalProperties=None, AdjacentCacheLinePrefetch=None, AdvancedMemTest=None, AllUsbDevices=None, Altitude=None, Ancestors=None, AspmSupport=None, AssertNmiOnPerr=None, AssertNmiOnSerr=None, AutoCcState=None, AutonumousCstateEnable=None, BaudRate=None, BmeDmaMitigation=None, BootOptionNumRetry=None, BootOptionReCoolDown=None, BootOptionRetry=None, BootPerformanceMode=None, BurstAndPostponedRefresh=None, CbsCmnApbdis=None, CbsCmnCpuCpb=None, CbsCmnCpuGenDowncoreCtrl=None, CbsCmnCpuGlobalCstateCtrl=None, CbsCmnCpuL1streamHwPrefetcher=None, CbsCmnCpuL2streamHwPrefetcher=None, CbsCmnCpuSmee=None, CbsCmnCpuStreamingStoresCtrl=None, CbsCmnDeterminismSlider=None, CbsCmnEfficiencyModeEn=None, CbsCmnFixedSocPstate=None, CbsCmnGnbNbIommu=None, CbsCmnGnbSmuDfCstates=None, CbsCmnGnbSmucppc=None, CbsCmnMemCtrlBankGroupSwapDdr4=None, CbsCmnMemMapBankInterleaveDdr4=None, CbsCmncTdpCtl=None, CbsCpuCcdCtrlSsp=None, CbsCpuCoreCtrl=None, CbsCpuSmtCtrl=None, CbsDbgCpuSnpMemCover=None, CbsDbgCpuSnpMemSizeCover=None, CbsDfCmnAcpiSratL3numa=None, CbsDfCmnDramNps=None, CbsDfCmnMemIntlv=None, CbsDfCmnMemIntlvSize=None, CbsSevSnpSupport=None, CdnEnable=None, CdnSupport=None, ChannelInterLeave=None, CiscoAdaptiveMemTraining=None, CiscoDebugLevel=None, CiscoOpromLaunchOptimization=None, CiscoXgmiMaxSpeed=None, CkeLowPolicy=None, ClassId=None, ClosedLoopThermThrotl=None, CmciEnable=None, ConfigTdp=None, ConfigTdpLevel=None, ConsoleRedirection=None, CoreMultiProcessing=None, CpuEnergyPerformance=None, CpuFrequencyFloor=None, CpuPerformance=None, CpuPowerManagement=None, CrQos=None, CreateTime=None, CrfastgoConfig=None, DcpmmFirmwareDowngrade=None, DemandScrub=None, Description=None, DirectCacheAccess=None, DomainGroupMoid=None, DramClockThrottling=None, DramRefreshRate=None, DramSwThermalThrottling=None, EadrSupport=None, EdpcEn=None, EnableClockSpreadSpec=None, EnableMktme=None, EnableSgx=None, EnableTme=None, EnergyEfficientTurbo=None, EngPerfTuning=None, EnhancedIntelSpeedStepTech=None, EpochUpdate=None, EppEnable=None, EppProfile=None, ExecuteDisableBit=None, ExtendedApic=None, FlowControl=None, Frb2enable=None, HardwarePrefetch=None, HwpmEnable=None, Id=None, ImcInterleave=None, IntelDynamicSpeedSelect=None, IntelHyperThreadingTech=None, IntelSpeedSelect=None, IntelTurboBoostTech=None, IntelVirtualizationTechnology=None, IntelVtForDirectedIo=None, IntelVtdCoherencySupport=None, IntelVtdInterruptRemapping=None, IntelVtdPassThroughDmaSupport=None, IntelVtdatsSupport=None, IohErrorEnable=None, IohResource=None, IpPrefetch=None, Ipv4http=None, Ipv4pxe=None, Ipv6http=None, Ipv6pxe=None, KtiPrefetch=None, LegacyOsRedirection=None, LegacyUsbSupport=None, LlcPrefetch=None, LomPort0state=None, LomPort1state=None, LomPort2state=None, LomPort3state=None, LomPortsAllState=None, LvDdrMode=None, MakeDeviceNonBootable=None, MemoryBandwidthBoost=None, MemoryInterLeave=None, MemoryMappedIoAbove4gb=None, MemoryRefreshRate=None, MemorySizeLimit=None, MemoryThermalThrottling=None, MirroringMode=None, MmcfgBase=None, ModTime=None, Moid=None, Name=None, NetworkStack=None, NumaOptimized=None, NvmdimmPerformConfig=None, ObjectType=None, Onboard10gbitLom=None, OnboardGbitLom=None, OnboardScuStorageSupport=None, OnboardScuStorageSwStack=None, OperationMode=None, Organization=None, OsBootWatchdogTimer=None, OsBootWatchdogTimerPolicy=None, OsBootWatchdogTimerTimeout=None, OutOfBandMgmtPort=None, Owners=None, PackageCstateLimit=None, PanicHighWatermark=None, Parent=None, PartialCacheLineSparing=None, PartialMirrorModeConfig=None, PartialMirrorPercent=None, PartialMirrorValue1=None, PartialMirrorValue2=None, PartialMirrorValue3=None, PartialMirrorValue4=None, PatrolScrub=None, PatrolScrubDuration=None, PcIeRasSupport=None, PcIeSsdHotPlugSupport=None, PchUsb30mode=None, PciOptionRoMs=None, PciRomClp=None, PcieAriSupport=None, PciePllSsc=None, PcieSlotMraid1linkSpeed=None, PcieSlotMraid1optionRom=None, PcieSlotMraid2linkSpeed=None, PcieSlotMraid2optionRom=None, PcieSlotMstorraidLinkSpeed=None, PcieSlotMstorraidOptionRom=None, PcieSlotNvme1linkSpeed=None, PcieSlotNvme1optionRom=None, PcieSlotNvme2linkSpeed=None, PcieSlotNvme2optionRom=None, PcieSlotNvme3linkSpeed=None, PcieSlotNvme3optionRom=None, PcieSlotNvme4linkSpeed=None, PcieSlotNvme4optionRom=None, PcieSlotNvme5linkSpeed=None, PcieSlotNvme5optionRom=None, PcieSlotNvme6linkSpeed=None, PcieSlotNvme6optionRom=None, PermissionResources=None, PopSupport=None, PostErrorPause=None, PostPackageRepair=None, ProcessorC1e=None, ProcessorC3report=None, ProcessorC6report=None, ProcessorCstate=None, Profiles=None, Psata=None, PstateCoordType=None, PuttyKeyPad=None, PwrPerfTuning=None, QpiLinkFrequency=None, QpiLinkSpeed=None, QpiSnoopMode=None, RankInterLeave=None, RedirectionAfterPost=None, SataModeSelect=None, SelectMemoryRasConfiguration=None, SelectPprType=None, SerialPortAenable=None, Sev=None, SgxAutoRegistrationAgent=None, SgxEpoch0=None, SgxEpoch1=None, SgxFactoryReset=None, SgxLePubKeyHash0=None, SgxLePubKeyHash1=None, SgxLePubKeyHash2=None, SgxLePubKeyHash3=None, SgxLeWr=None, SgxPackageInfoInBandAccess=None, SgxQos=None, SharedScope=None, SinglePctlEnable=None, Slot10linkSpeed=None, Slot10state=None, Slot11linkSpeed=None, Slot11state=None, Slot12linkSpeed=None, Slot12state=None, Slot13state=None, Slot14state=None, Slot1linkSpeed=None, Slot1state=None, Slot2linkSpeed=None, Slot2state=None, Slot3linkSpeed=None, Slot3state=None, Slot4linkSpeed=None, Slot4state=None, Slot5linkSpeed=None, Slot5state=None, Slot6linkSpeed=None, Slot6state=None, Slot7linkSpeed=None, Slot7state=None, Slot8linkSpeed=None, Slot8state=None, Slot9linkSpeed=None, Slot9state=None, SlotFlomLinkSpeed=None, SlotFrontNvme10linkSpeed=None, SlotFrontNvme10optionRom=None, SlotFrontNvme11linkSpeed=None, SlotFrontNvme11optionRom=None, SlotFrontNvme12linkSpeed=None, SlotFrontNvme12optionRom=None, SlotFrontNvme13optionRom=None, SlotFrontNvme14optionRom=None, SlotFrontNvme15optionRom=None, SlotFrontNvme16optionRom=None, SlotFrontNvme17optionRom=None, SlotFrontNvme18optionRom=None, SlotFrontNvme19optionRom=None, SlotFrontNvme1linkSpeed=None, SlotFrontNvme1optionRom=None, SlotFrontNvme20optionRom=None, SlotFrontNvme21optionRom=None, SlotFrontNvme22optionRom=None, SlotFrontNvme23optionRom=None, SlotFrontNvme24optionRom=None, SlotFrontNvme2linkSpeed=None, SlotFrontNvme2optionRom=None, SlotFrontNvme3linkSpeed=None, SlotFrontNvme3optionRom=None, SlotFrontNvme4linkSpeed=None, SlotFrontNvme4optionRom=None, SlotFrontNvme5linkSpeed=None, SlotFrontNvme5optionRom=None, SlotFrontNvme6linkSpeed=None, SlotFrontNvme6optionRom=None, SlotFrontNvme7linkSpeed=None, SlotFrontNvme7optionRom=None, SlotFrontNvme8linkSpeed=None, SlotFrontNvme8optionRom=None, SlotFrontNvme9linkSpeed=None, SlotFrontNvme9optionRom=None, SlotFrontSlot5linkSpeed=None, SlotFrontSlot6linkSpeed=None, SlotGpu1state=None, SlotGpu2state=None, SlotGpu3state=None, SlotGpu4state=None, SlotGpu5state=None, SlotGpu6state=None, SlotGpu7state=None, SlotGpu8state=None, SlotHbaLinkSpeed=None, SlotHbaState=None, SlotLom1link=None, SlotLom2link=None, SlotMezzState=None, SlotMlomLinkSpeed=None, SlotMlomState=None, SlotMraidLinkSpeed=None, SlotMraidState=None, SlotN10state=None, SlotN11state=None, SlotN12state=None, SlotN13state=None, SlotN14state=None, SlotN15state=None, SlotN16state=None, SlotN17state=None, SlotN18state=None, SlotN19state=None, SlotN1state=None, SlotN20state=None, SlotN21state=None, SlotN22state=None, SlotN23state=None, SlotN24state=None, SlotN2state=None, SlotN3state=None, SlotN4state=None, SlotN5state=None, SlotN6state=None, SlotN7state=None, SlotN8state=None, SlotN9state=None, SlotRaidLinkSpeed=None, SlotRaidState=None, SlotRearNvme1linkSpeed=None, SlotRearNvme1state=None, SlotRearNvme2linkSpeed=None, SlotRearNvme2state=None, SlotRearNvme3linkSpeed=None, SlotRearNvme3state=None, SlotRearNvme4linkSpeed=None, SlotRearNvme4state=None, SlotRearNvme5state=None, SlotRearNvme6state=None, SlotRearNvme7state=None, SlotRearNvme8state=None, SlotRiser1linkSpeed=None, SlotRiser1slot1linkSpeed=None, SlotRiser1slot2linkSpeed=None, SlotRiser1slot3linkSpeed=None, SlotRiser2linkSpeed=None, SlotRiser2slot4linkSpeed=None, SlotRiser2slot5linkSpeed=None, SlotRiser2slot6linkSpeed=None, SlotSasState=None, SlotSsdSlot1linkSpeed=None, SlotSsdSlot2linkSpeed=None, Smee=None, SmtMode=None, Snc=None, SnoopyModeFor2lm=None, SnoopyModeForAd=None, SparingMode=None, SrIov=None, StreamerPrefetch=None, SvmMode=None, Tags=None, TerminalType=None, TpmControl=None, TpmPendingOperation=None, TpmSupport=None, Tsme=None, TxtSupport=None, UcsmBootOrderRule=None, UfsDisable=None, UmaBasedClustering=None, UsbEmul6064=None, UsbPortFront=None, UsbPortInternal=None, UsbPortKvm=None, UsbPortRear=None, UsbPortSdCard=None, UsbPortVmedia=None, UsbXhciSupport=None, VersionContext=None, VgaPriority=None, VmdEnable=None, VolMemoryMode=None, WorkLoadConfig=None, XptPrefetch=None)

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
