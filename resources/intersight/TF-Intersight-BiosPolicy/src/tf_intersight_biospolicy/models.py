# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    AccountMoid: Optional[str]
    AcsControlGpu1state: Optional[str]
    AcsControlGpu2state: Optional[str]
    AcsControlGpu3state: Optional[str]
    AcsControlGpu4state: Optional[str]
    AcsControlGpu5state: Optional[str]
    AcsControlGpu6state: Optional[str]
    AcsControlGpu7state: Optional[str]
    AcsControlGpu8state: Optional[str]
    AcsControlSlot11state: Optional[str]
    AcsControlSlot12state: Optional[str]
    AcsControlSlot13state: Optional[str]
    AcsControlSlot14state: Optional[str]
    AdditionalProperties: Optional[str]
    AdjacentCacheLinePrefetch: Optional[str]
    AdvancedMemTest: Optional[str]
    AllUsbDevices: Optional[str]
    Altitude: Optional[str]
    Ancestors: Optional[Sequence["_AncestorsDefinition"]]
    AspmSupport: Optional[str]
    AssertNmiOnPerr: Optional[str]
    AssertNmiOnSerr: Optional[str]
    AutoCcState: Optional[str]
    AutonumousCstateEnable: Optional[str]
    BaudRate: Optional[str]
    BmeDmaMitigation: Optional[str]
    BootOptionNumRetry: Optional[str]
    BootOptionReCoolDown: Optional[str]
    BootOptionRetry: Optional[str]
    BootPerformanceMode: Optional[str]
    BurstAndPostponedRefresh: Optional[str]
    CbsCmnApbdis: Optional[str]
    CbsCmnCpuCpb: Optional[str]
    CbsCmnCpuGenDowncoreCtrl: Optional[str]
    CbsCmnCpuGlobalCstateCtrl: Optional[str]
    CbsCmnCpuL1streamHwPrefetcher: Optional[str]
    CbsCmnCpuL2streamHwPrefetcher: Optional[str]
    CbsCmnCpuSmee: Optional[str]
    CbsCmnCpuStreamingStoresCtrl: Optional[str]
    CbsCmnDeterminismSlider: Optional[str]
    CbsCmnEfficiencyModeEn: Optional[str]
    CbsCmnFixedSocPstate: Optional[str]
    CbsCmnGnbNbIommu: Optional[str]
    CbsCmnGnbSmuDfCstates: Optional[str]
    CbsCmnGnbSmucppc: Optional[str]
    CbsCmnMemCtrlBankGroupSwapDdr4: Optional[str]
    CbsCmnMemMapBankInterleaveDdr4: Optional[str]
    CbsCmncTdpCtl: Optional[str]
    CbsCpuCcdCtrlSsp: Optional[str]
    CbsCpuCoreCtrl: Optional[str]
    CbsCpuSmtCtrl: Optional[str]
    CbsDbgCpuSnpMemCover: Optional[str]
    CbsDbgCpuSnpMemSizeCover: Optional[str]
    CbsDfCmnAcpiSratL3numa: Optional[str]
    CbsDfCmnDramNps: Optional[str]
    CbsDfCmnMemIntlv: Optional[str]
    CbsDfCmnMemIntlvSize: Optional[str]
    CbsSevSnpSupport: Optional[str]
    CdnEnable: Optional[str]
    CdnSupport: Optional[str]
    ChannelInterLeave: Optional[str]
    CiscoAdaptiveMemTraining: Optional[str]
    CiscoDebugLevel: Optional[str]
    CiscoOpromLaunchOptimization: Optional[str]
    CiscoXgmiMaxSpeed: Optional[str]
    CkeLowPolicy: Optional[str]
    ClassId: Optional[str]
    ClosedLoopThermThrotl: Optional[str]
    CmciEnable: Optional[str]
    ConfigTdp: Optional[str]
    ConfigTdpLevel: Optional[str]
    ConsoleRedirection: Optional[str]
    CoreMultiProcessing: Optional[str]
    CpuEnergyPerformance: Optional[str]
    CpuFrequencyFloor: Optional[str]
    CpuPerformance: Optional[str]
    CpuPowerManagement: Optional[str]
    CrQos: Optional[str]
    CreateTime: Optional[str]
    CrfastgoConfig: Optional[str]
    DcpmmFirmwareDowngrade: Optional[str]
    DemandScrub: Optional[str]
    Description: Optional[str]
    DirectCacheAccess: Optional[str]
    DomainGroupMoid: Optional[str]
    DramClockThrottling: Optional[str]
    DramRefreshRate: Optional[str]
    DramSwThermalThrottling: Optional[str]
    EadrSupport: Optional[str]
    EdpcEn: Optional[str]
    EnableClockSpreadSpec: Optional[str]
    EnableMktme: Optional[str]
    EnableSgx: Optional[str]
    EnableTme: Optional[str]
    EnergyEfficientTurbo: Optional[str]
    EngPerfTuning: Optional[str]
    EnhancedIntelSpeedStepTech: Optional[str]
    EpochUpdate: Optional[str]
    EppEnable: Optional[str]
    EppProfile: Optional[str]
    ExecuteDisableBit: Optional[str]
    ExtendedApic: Optional[str]
    FlowControl: Optional[str]
    Frb2enable: Optional[str]
    HardwarePrefetch: Optional[str]
    HwpmEnable: Optional[str]
    Id: Optional[str]
    ImcInterleave: Optional[str]
    IntelDynamicSpeedSelect: Optional[str]
    IntelHyperThreadingTech: Optional[str]
    IntelSpeedSelect: Optional[str]
    IntelTurboBoostTech: Optional[str]
    IntelVirtualizationTechnology: Optional[str]
    IntelVtForDirectedIo: Optional[str]
    IntelVtdCoherencySupport: Optional[str]
    IntelVtdInterruptRemapping: Optional[str]
    IntelVtdPassThroughDmaSupport: Optional[str]
    IntelVtdatsSupport: Optional[str]
    IohErrorEnable: Optional[str]
    IohResource: Optional[str]
    IpPrefetch: Optional[str]
    Ipv4http: Optional[str]
    Ipv4pxe: Optional[str]
    Ipv6http: Optional[str]
    Ipv6pxe: Optional[str]
    KtiPrefetch: Optional[str]
    LegacyOsRedirection: Optional[str]
    LegacyUsbSupport: Optional[str]
    LlcPrefetch: Optional[str]
    LomPort0state: Optional[str]
    LomPort1state: Optional[str]
    LomPort2state: Optional[str]
    LomPort3state: Optional[str]
    LomPortsAllState: Optional[str]
    LvDdrMode: Optional[str]
    MakeDeviceNonBootable: Optional[str]
    MemoryBandwidthBoost: Optional[str]
    MemoryInterLeave: Optional[str]
    MemoryMappedIoAbove4gb: Optional[str]
    MemoryRefreshRate: Optional[str]
    MemorySizeLimit: Optional[str]
    MemoryThermalThrottling: Optional[str]
    MirroringMode: Optional[str]
    MmcfgBase: Optional[str]
    ModTime: Optional[str]
    Moid: Optional[str]
    Name: Optional[str]
    NetworkStack: Optional[str]
    NumaOptimized: Optional[str]
    NvmdimmPerformConfig: Optional[str]
    ObjectType: Optional[str]
    Onboard10gbitLom: Optional[str]
    OnboardGbitLom: Optional[str]
    OnboardScuStorageSupport: Optional[str]
    OnboardScuStorageSwStack: Optional[str]
    OperationMode: Optional[str]
    Organization: Optional[Sequence["_OrganizationDefinition"]]
    OsBootWatchdogTimer: Optional[str]
    OsBootWatchdogTimerPolicy: Optional[str]
    OsBootWatchdogTimerTimeout: Optional[str]
    OutOfBandMgmtPort: Optional[str]
    Owners: Optional[Sequence[str]]
    PackageCstateLimit: Optional[str]
    PanicHighWatermark: Optional[str]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PartialCacheLineSparing: Optional[str]
    PartialMirrorModeConfig: Optional[str]
    PartialMirrorPercent: Optional[str]
    PartialMirrorValue1: Optional[str]
    PartialMirrorValue2: Optional[str]
    PartialMirrorValue3: Optional[str]
    PartialMirrorValue4: Optional[str]
    PatrolScrub: Optional[str]
    PatrolScrubDuration: Optional[str]
    PcIeRasSupport: Optional[str]
    PcIeSsdHotPlugSupport: Optional[str]
    PchUsb30mode: Optional[str]
    PciOptionRoMs: Optional[str]
    PciRomClp: Optional[str]
    PcieAriSupport: Optional[str]
    PciePllSsc: Optional[str]
    PcieSlotMraid1linkSpeed: Optional[str]
    PcieSlotMraid1optionRom: Optional[str]
    PcieSlotMraid2linkSpeed: Optional[str]
    PcieSlotMraid2optionRom: Optional[str]
    PcieSlotMstorraidLinkSpeed: Optional[str]
    PcieSlotMstorraidOptionRom: Optional[str]
    PcieSlotNvme1linkSpeed: Optional[str]
    PcieSlotNvme1optionRom: Optional[str]
    PcieSlotNvme2linkSpeed: Optional[str]
    PcieSlotNvme2optionRom: Optional[str]
    PcieSlotNvme3linkSpeed: Optional[str]
    PcieSlotNvme3optionRom: Optional[str]
    PcieSlotNvme4linkSpeed: Optional[str]
    PcieSlotNvme4optionRom: Optional[str]
    PcieSlotNvme5linkSpeed: Optional[str]
    PcieSlotNvme5optionRom: Optional[str]
    PcieSlotNvme6linkSpeed: Optional[str]
    PcieSlotNvme6optionRom: Optional[str]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    PopSupport: Optional[str]
    PostErrorPause: Optional[str]
    PostPackageRepair: Optional[str]
    ProcessorC1e: Optional[str]
    ProcessorC3report: Optional[str]
    ProcessorC6report: Optional[str]
    ProcessorCstate: Optional[str]
    Profiles: Optional[Sequence["_ProfilesDefinition"]]
    Psata: Optional[str]
    PstateCoordType: Optional[str]
    PuttyKeyPad: Optional[str]
    PwrPerfTuning: Optional[str]
    QpiLinkFrequency: Optional[str]
    QpiLinkSpeed: Optional[str]
    QpiSnoopMode: Optional[str]
    RankInterLeave: Optional[str]
    RedirectionAfterPost: Optional[str]
    SataModeSelect: Optional[str]
    SelectMemoryRasConfiguration: Optional[str]
    SelectPprType: Optional[str]
    SerialPortAenable: Optional[str]
    Sev: Optional[str]
    SgxAutoRegistrationAgent: Optional[str]
    SgxEpoch0: Optional[str]
    SgxEpoch1: Optional[str]
    SgxFactoryReset: Optional[str]
    SgxLePubKeyHash0: Optional[str]
    SgxLePubKeyHash1: Optional[str]
    SgxLePubKeyHash2: Optional[str]
    SgxLePubKeyHash3: Optional[str]
    SgxLeWr: Optional[str]
    SgxPackageInfoInBandAccess: Optional[str]
    SgxQos: Optional[str]
    SharedScope: Optional[str]
    SinglePctlEnable: Optional[str]
    Slot10linkSpeed: Optional[str]
    Slot10state: Optional[str]
    Slot11linkSpeed: Optional[str]
    Slot11state: Optional[str]
    Slot12linkSpeed: Optional[str]
    Slot12state: Optional[str]
    Slot13state: Optional[str]
    Slot14state: Optional[str]
    Slot1linkSpeed: Optional[str]
    Slot1state: Optional[str]
    Slot2linkSpeed: Optional[str]
    Slot2state: Optional[str]
    Slot3linkSpeed: Optional[str]
    Slot3state: Optional[str]
    Slot4linkSpeed: Optional[str]
    Slot4state: Optional[str]
    Slot5linkSpeed: Optional[str]
    Slot5state: Optional[str]
    Slot6linkSpeed: Optional[str]
    Slot6state: Optional[str]
    Slot7linkSpeed: Optional[str]
    Slot7state: Optional[str]
    Slot8linkSpeed: Optional[str]
    Slot8state: Optional[str]
    Slot9linkSpeed: Optional[str]
    Slot9state: Optional[str]
    SlotFlomLinkSpeed: Optional[str]
    SlotFrontNvme10linkSpeed: Optional[str]
    SlotFrontNvme10optionRom: Optional[str]
    SlotFrontNvme11linkSpeed: Optional[str]
    SlotFrontNvme11optionRom: Optional[str]
    SlotFrontNvme12linkSpeed: Optional[str]
    SlotFrontNvme12optionRom: Optional[str]
    SlotFrontNvme13optionRom: Optional[str]
    SlotFrontNvme14optionRom: Optional[str]
    SlotFrontNvme15optionRom: Optional[str]
    SlotFrontNvme16optionRom: Optional[str]
    SlotFrontNvme17optionRom: Optional[str]
    SlotFrontNvme18optionRom: Optional[str]
    SlotFrontNvme19optionRom: Optional[str]
    SlotFrontNvme1linkSpeed: Optional[str]
    SlotFrontNvme1optionRom: Optional[str]
    SlotFrontNvme20optionRom: Optional[str]
    SlotFrontNvme21optionRom: Optional[str]
    SlotFrontNvme22optionRom: Optional[str]
    SlotFrontNvme23optionRom: Optional[str]
    SlotFrontNvme24optionRom: Optional[str]
    SlotFrontNvme2linkSpeed: Optional[str]
    SlotFrontNvme2optionRom: Optional[str]
    SlotFrontNvme3linkSpeed: Optional[str]
    SlotFrontNvme3optionRom: Optional[str]
    SlotFrontNvme4linkSpeed: Optional[str]
    SlotFrontNvme4optionRom: Optional[str]
    SlotFrontNvme5linkSpeed: Optional[str]
    SlotFrontNvme5optionRom: Optional[str]
    SlotFrontNvme6linkSpeed: Optional[str]
    SlotFrontNvme6optionRom: Optional[str]
    SlotFrontNvme7linkSpeed: Optional[str]
    SlotFrontNvme7optionRom: Optional[str]
    SlotFrontNvme8linkSpeed: Optional[str]
    SlotFrontNvme8optionRom: Optional[str]
    SlotFrontNvme9linkSpeed: Optional[str]
    SlotFrontNvme9optionRom: Optional[str]
    SlotFrontSlot5linkSpeed: Optional[str]
    SlotFrontSlot6linkSpeed: Optional[str]
    SlotGpu1state: Optional[str]
    SlotGpu2state: Optional[str]
    SlotGpu3state: Optional[str]
    SlotGpu4state: Optional[str]
    SlotGpu5state: Optional[str]
    SlotGpu6state: Optional[str]
    SlotGpu7state: Optional[str]
    SlotGpu8state: Optional[str]
    SlotHbaLinkSpeed: Optional[str]
    SlotHbaState: Optional[str]
    SlotLom1link: Optional[str]
    SlotLom2link: Optional[str]
    SlotMezzState: Optional[str]
    SlotMlomLinkSpeed: Optional[str]
    SlotMlomState: Optional[str]
    SlotMraidLinkSpeed: Optional[str]
    SlotMraidState: Optional[str]
    SlotN10state: Optional[str]
    SlotN11state: Optional[str]
    SlotN12state: Optional[str]
    SlotN13state: Optional[str]
    SlotN14state: Optional[str]
    SlotN15state: Optional[str]
    SlotN16state: Optional[str]
    SlotN17state: Optional[str]
    SlotN18state: Optional[str]
    SlotN19state: Optional[str]
    SlotN1state: Optional[str]
    SlotN20state: Optional[str]
    SlotN21state: Optional[str]
    SlotN22state: Optional[str]
    SlotN23state: Optional[str]
    SlotN24state: Optional[str]
    SlotN2state: Optional[str]
    SlotN3state: Optional[str]
    SlotN4state: Optional[str]
    SlotN5state: Optional[str]
    SlotN6state: Optional[str]
    SlotN7state: Optional[str]
    SlotN8state: Optional[str]
    SlotN9state: Optional[str]
    SlotRaidLinkSpeed: Optional[str]
    SlotRaidState: Optional[str]
    SlotRearNvme1linkSpeed: Optional[str]
    SlotRearNvme1state: Optional[str]
    SlotRearNvme2linkSpeed: Optional[str]
    SlotRearNvme2state: Optional[str]
    SlotRearNvme3linkSpeed: Optional[str]
    SlotRearNvme3state: Optional[str]
    SlotRearNvme4linkSpeed: Optional[str]
    SlotRearNvme4state: Optional[str]
    SlotRearNvme5state: Optional[str]
    SlotRearNvme6state: Optional[str]
    SlotRearNvme7state: Optional[str]
    SlotRearNvme8state: Optional[str]
    SlotRiser1linkSpeed: Optional[str]
    SlotRiser1slot1linkSpeed: Optional[str]
    SlotRiser1slot2linkSpeed: Optional[str]
    SlotRiser1slot3linkSpeed: Optional[str]
    SlotRiser2linkSpeed: Optional[str]
    SlotRiser2slot4linkSpeed: Optional[str]
    SlotRiser2slot5linkSpeed: Optional[str]
    SlotRiser2slot6linkSpeed: Optional[str]
    SlotSasState: Optional[str]
    SlotSsdSlot1linkSpeed: Optional[str]
    SlotSsdSlot2linkSpeed: Optional[str]
    Smee: Optional[str]
    SmtMode: Optional[str]
    Snc: Optional[str]
    SnoopyModeFor2lm: Optional[str]
    SnoopyModeForAd: Optional[str]
    SparingMode: Optional[str]
    SrIov: Optional[str]
    StreamerPrefetch: Optional[str]
    SvmMode: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TerminalType: Optional[str]
    TpmControl: Optional[str]
    TpmPendingOperation: Optional[str]
    TpmSupport: Optional[str]
    Tsme: Optional[str]
    TxtSupport: Optional[str]
    UcsmBootOrderRule: Optional[str]
    UfsDisable: Optional[str]
    UmaBasedClustering: Optional[str]
    UsbEmul6064: Optional[str]
    UsbPortFront: Optional[str]
    UsbPortInternal: Optional[str]
    UsbPortKvm: Optional[str]
    UsbPortRear: Optional[str]
    UsbPortSdCard: Optional[str]
    UsbPortVmedia: Optional[str]
    UsbXhciSupport: Optional[str]
    VersionContext: Optional[Sequence["_VersionContextDefinition3"]]
    VgaPriority: Optional[str]
    VmdEnable: Optional[str]
    VolMemoryMode: Optional[str]
    WorkLoadConfig: Optional[str]
    XptPrefetch: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccountMoid=json_data.get("AccountMoid"),
            AcsControlGpu1state=json_data.get("AcsControlGpu1state"),
            AcsControlGpu2state=json_data.get("AcsControlGpu2state"),
            AcsControlGpu3state=json_data.get("AcsControlGpu3state"),
            AcsControlGpu4state=json_data.get("AcsControlGpu4state"),
            AcsControlGpu5state=json_data.get("AcsControlGpu5state"),
            AcsControlGpu6state=json_data.get("AcsControlGpu6state"),
            AcsControlGpu7state=json_data.get("AcsControlGpu7state"),
            AcsControlGpu8state=json_data.get("AcsControlGpu8state"),
            AcsControlSlot11state=json_data.get("AcsControlSlot11state"),
            AcsControlSlot12state=json_data.get("AcsControlSlot12state"),
            AcsControlSlot13state=json_data.get("AcsControlSlot13state"),
            AcsControlSlot14state=json_data.get("AcsControlSlot14state"),
            AdditionalProperties=json_data.get("AdditionalProperties"),
            AdjacentCacheLinePrefetch=json_data.get("AdjacentCacheLinePrefetch"),
            AdvancedMemTest=json_data.get("AdvancedMemTest"),
            AllUsbDevices=json_data.get("AllUsbDevices"),
            Altitude=json_data.get("Altitude"),
            Ancestors=deserialize_list(json_data.get("Ancestors"), AncestorsDefinition),
            AspmSupport=json_data.get("AspmSupport"),
            AssertNmiOnPerr=json_data.get("AssertNmiOnPerr"),
            AssertNmiOnSerr=json_data.get("AssertNmiOnSerr"),
            AutoCcState=json_data.get("AutoCcState"),
            AutonumousCstateEnable=json_data.get("AutonumousCstateEnable"),
            BaudRate=json_data.get("BaudRate"),
            BmeDmaMitigation=json_data.get("BmeDmaMitigation"),
            BootOptionNumRetry=json_data.get("BootOptionNumRetry"),
            BootOptionReCoolDown=json_data.get("BootOptionReCoolDown"),
            BootOptionRetry=json_data.get("BootOptionRetry"),
            BootPerformanceMode=json_data.get("BootPerformanceMode"),
            BurstAndPostponedRefresh=json_data.get("BurstAndPostponedRefresh"),
            CbsCmnApbdis=json_data.get("CbsCmnApbdis"),
            CbsCmnCpuCpb=json_data.get("CbsCmnCpuCpb"),
            CbsCmnCpuGenDowncoreCtrl=json_data.get("CbsCmnCpuGenDowncoreCtrl"),
            CbsCmnCpuGlobalCstateCtrl=json_data.get("CbsCmnCpuGlobalCstateCtrl"),
            CbsCmnCpuL1streamHwPrefetcher=json_data.get("CbsCmnCpuL1streamHwPrefetcher"),
            CbsCmnCpuL2streamHwPrefetcher=json_data.get("CbsCmnCpuL2streamHwPrefetcher"),
            CbsCmnCpuSmee=json_data.get("CbsCmnCpuSmee"),
            CbsCmnCpuStreamingStoresCtrl=json_data.get("CbsCmnCpuStreamingStoresCtrl"),
            CbsCmnDeterminismSlider=json_data.get("CbsCmnDeterminismSlider"),
            CbsCmnEfficiencyModeEn=json_data.get("CbsCmnEfficiencyModeEn"),
            CbsCmnFixedSocPstate=json_data.get("CbsCmnFixedSocPstate"),
            CbsCmnGnbNbIommu=json_data.get("CbsCmnGnbNbIommu"),
            CbsCmnGnbSmuDfCstates=json_data.get("CbsCmnGnbSmuDfCstates"),
            CbsCmnGnbSmucppc=json_data.get("CbsCmnGnbSmucppc"),
            CbsCmnMemCtrlBankGroupSwapDdr4=json_data.get("CbsCmnMemCtrlBankGroupSwapDdr4"),
            CbsCmnMemMapBankInterleaveDdr4=json_data.get("CbsCmnMemMapBankInterleaveDdr4"),
            CbsCmncTdpCtl=json_data.get("CbsCmncTdpCtl"),
            CbsCpuCcdCtrlSsp=json_data.get("CbsCpuCcdCtrlSsp"),
            CbsCpuCoreCtrl=json_data.get("CbsCpuCoreCtrl"),
            CbsCpuSmtCtrl=json_data.get("CbsCpuSmtCtrl"),
            CbsDbgCpuSnpMemCover=json_data.get("CbsDbgCpuSnpMemCover"),
            CbsDbgCpuSnpMemSizeCover=json_data.get("CbsDbgCpuSnpMemSizeCover"),
            CbsDfCmnAcpiSratL3numa=json_data.get("CbsDfCmnAcpiSratL3numa"),
            CbsDfCmnDramNps=json_data.get("CbsDfCmnDramNps"),
            CbsDfCmnMemIntlv=json_data.get("CbsDfCmnMemIntlv"),
            CbsDfCmnMemIntlvSize=json_data.get("CbsDfCmnMemIntlvSize"),
            CbsSevSnpSupport=json_data.get("CbsSevSnpSupport"),
            CdnEnable=json_data.get("CdnEnable"),
            CdnSupport=json_data.get("CdnSupport"),
            ChannelInterLeave=json_data.get("ChannelInterLeave"),
            CiscoAdaptiveMemTraining=json_data.get("CiscoAdaptiveMemTraining"),
            CiscoDebugLevel=json_data.get("CiscoDebugLevel"),
            CiscoOpromLaunchOptimization=json_data.get("CiscoOpromLaunchOptimization"),
            CiscoXgmiMaxSpeed=json_data.get("CiscoXgmiMaxSpeed"),
            CkeLowPolicy=json_data.get("CkeLowPolicy"),
            ClassId=json_data.get("ClassId"),
            ClosedLoopThermThrotl=json_data.get("ClosedLoopThermThrotl"),
            CmciEnable=json_data.get("CmciEnable"),
            ConfigTdp=json_data.get("ConfigTdp"),
            ConfigTdpLevel=json_data.get("ConfigTdpLevel"),
            ConsoleRedirection=json_data.get("ConsoleRedirection"),
            CoreMultiProcessing=json_data.get("CoreMultiProcessing"),
            CpuEnergyPerformance=json_data.get("CpuEnergyPerformance"),
            CpuFrequencyFloor=json_data.get("CpuFrequencyFloor"),
            CpuPerformance=json_data.get("CpuPerformance"),
            CpuPowerManagement=json_data.get("CpuPowerManagement"),
            CrQos=json_data.get("CrQos"),
            CreateTime=json_data.get("CreateTime"),
            CrfastgoConfig=json_data.get("CrfastgoConfig"),
            DcpmmFirmwareDowngrade=json_data.get("DcpmmFirmwareDowngrade"),
            DemandScrub=json_data.get("DemandScrub"),
            Description=json_data.get("Description"),
            DirectCacheAccess=json_data.get("DirectCacheAccess"),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            DramClockThrottling=json_data.get("DramClockThrottling"),
            DramRefreshRate=json_data.get("DramRefreshRate"),
            DramSwThermalThrottling=json_data.get("DramSwThermalThrottling"),
            EadrSupport=json_data.get("EadrSupport"),
            EdpcEn=json_data.get("EdpcEn"),
            EnableClockSpreadSpec=json_data.get("EnableClockSpreadSpec"),
            EnableMktme=json_data.get("EnableMktme"),
            EnableSgx=json_data.get("EnableSgx"),
            EnableTme=json_data.get("EnableTme"),
            EnergyEfficientTurbo=json_data.get("EnergyEfficientTurbo"),
            EngPerfTuning=json_data.get("EngPerfTuning"),
            EnhancedIntelSpeedStepTech=json_data.get("EnhancedIntelSpeedStepTech"),
            EpochUpdate=json_data.get("EpochUpdate"),
            EppEnable=json_data.get("EppEnable"),
            EppProfile=json_data.get("EppProfile"),
            ExecuteDisableBit=json_data.get("ExecuteDisableBit"),
            ExtendedApic=json_data.get("ExtendedApic"),
            FlowControl=json_data.get("FlowControl"),
            Frb2enable=json_data.get("Frb2enable"),
            HardwarePrefetch=json_data.get("HardwarePrefetch"),
            HwpmEnable=json_data.get("HwpmEnable"),
            Id=json_data.get("Id"),
            ImcInterleave=json_data.get("ImcInterleave"),
            IntelDynamicSpeedSelect=json_data.get("IntelDynamicSpeedSelect"),
            IntelHyperThreadingTech=json_data.get("IntelHyperThreadingTech"),
            IntelSpeedSelect=json_data.get("IntelSpeedSelect"),
            IntelTurboBoostTech=json_data.get("IntelTurboBoostTech"),
            IntelVirtualizationTechnology=json_data.get("IntelVirtualizationTechnology"),
            IntelVtForDirectedIo=json_data.get("IntelVtForDirectedIo"),
            IntelVtdCoherencySupport=json_data.get("IntelVtdCoherencySupport"),
            IntelVtdInterruptRemapping=json_data.get("IntelVtdInterruptRemapping"),
            IntelVtdPassThroughDmaSupport=json_data.get("IntelVtdPassThroughDmaSupport"),
            IntelVtdatsSupport=json_data.get("IntelVtdatsSupport"),
            IohErrorEnable=json_data.get("IohErrorEnable"),
            IohResource=json_data.get("IohResource"),
            IpPrefetch=json_data.get("IpPrefetch"),
            Ipv4http=json_data.get("Ipv4http"),
            Ipv4pxe=json_data.get("Ipv4pxe"),
            Ipv6http=json_data.get("Ipv6http"),
            Ipv6pxe=json_data.get("Ipv6pxe"),
            KtiPrefetch=json_data.get("KtiPrefetch"),
            LegacyOsRedirection=json_data.get("LegacyOsRedirection"),
            LegacyUsbSupport=json_data.get("LegacyUsbSupport"),
            LlcPrefetch=json_data.get("LlcPrefetch"),
            LomPort0state=json_data.get("LomPort0state"),
            LomPort1state=json_data.get("LomPort1state"),
            LomPort2state=json_data.get("LomPort2state"),
            LomPort3state=json_data.get("LomPort3state"),
            LomPortsAllState=json_data.get("LomPortsAllState"),
            LvDdrMode=json_data.get("LvDdrMode"),
            MakeDeviceNonBootable=json_data.get("MakeDeviceNonBootable"),
            MemoryBandwidthBoost=json_data.get("MemoryBandwidthBoost"),
            MemoryInterLeave=json_data.get("MemoryInterLeave"),
            MemoryMappedIoAbove4gb=json_data.get("MemoryMappedIoAbove4gb"),
            MemoryRefreshRate=json_data.get("MemoryRefreshRate"),
            MemorySizeLimit=json_data.get("MemorySizeLimit"),
            MemoryThermalThrottling=json_data.get("MemoryThermalThrottling"),
            MirroringMode=json_data.get("MirroringMode"),
            MmcfgBase=json_data.get("MmcfgBase"),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            NetworkStack=json_data.get("NetworkStack"),
            NumaOptimized=json_data.get("NumaOptimized"),
            NvmdimmPerformConfig=json_data.get("NvmdimmPerformConfig"),
            ObjectType=json_data.get("ObjectType"),
            Onboard10gbitLom=json_data.get("Onboard10gbitLom"),
            OnboardGbitLom=json_data.get("OnboardGbitLom"),
            OnboardScuStorageSupport=json_data.get("OnboardScuStorageSupport"),
            OnboardScuStorageSwStack=json_data.get("OnboardScuStorageSwStack"),
            OperationMode=json_data.get("OperationMode"),
            Organization=deserialize_list(json_data.get("Organization"), OrganizationDefinition),
            OsBootWatchdogTimer=json_data.get("OsBootWatchdogTimer"),
            OsBootWatchdogTimerPolicy=json_data.get("OsBootWatchdogTimerPolicy"),
            OsBootWatchdogTimerTimeout=json_data.get("OsBootWatchdogTimerTimeout"),
            OutOfBandMgmtPort=json_data.get("OutOfBandMgmtPort"),
            Owners=json_data.get("Owners"),
            PackageCstateLimit=json_data.get("PackageCstateLimit"),
            PanicHighWatermark=json_data.get("PanicHighWatermark"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PartialCacheLineSparing=json_data.get("PartialCacheLineSparing"),
            PartialMirrorModeConfig=json_data.get("PartialMirrorModeConfig"),
            PartialMirrorPercent=json_data.get("PartialMirrorPercent"),
            PartialMirrorValue1=json_data.get("PartialMirrorValue1"),
            PartialMirrorValue2=json_data.get("PartialMirrorValue2"),
            PartialMirrorValue3=json_data.get("PartialMirrorValue3"),
            PartialMirrorValue4=json_data.get("PartialMirrorValue4"),
            PatrolScrub=json_data.get("PatrolScrub"),
            PatrolScrubDuration=json_data.get("PatrolScrubDuration"),
            PcIeRasSupport=json_data.get("PcIeRasSupport"),
            PcIeSsdHotPlugSupport=json_data.get("PcIeSsdHotPlugSupport"),
            PchUsb30mode=json_data.get("PchUsb30mode"),
            PciOptionRoMs=json_data.get("PciOptionRoMs"),
            PciRomClp=json_data.get("PciRomClp"),
            PcieAriSupport=json_data.get("PcieAriSupport"),
            PciePllSsc=json_data.get("PciePllSsc"),
            PcieSlotMraid1linkSpeed=json_data.get("PcieSlotMraid1linkSpeed"),
            PcieSlotMraid1optionRom=json_data.get("PcieSlotMraid1optionRom"),
            PcieSlotMraid2linkSpeed=json_data.get("PcieSlotMraid2linkSpeed"),
            PcieSlotMraid2optionRom=json_data.get("PcieSlotMraid2optionRom"),
            PcieSlotMstorraidLinkSpeed=json_data.get("PcieSlotMstorraidLinkSpeed"),
            PcieSlotMstorraidOptionRom=json_data.get("PcieSlotMstorraidOptionRom"),
            PcieSlotNvme1linkSpeed=json_data.get("PcieSlotNvme1linkSpeed"),
            PcieSlotNvme1optionRom=json_data.get("PcieSlotNvme1optionRom"),
            PcieSlotNvme2linkSpeed=json_data.get("PcieSlotNvme2linkSpeed"),
            PcieSlotNvme2optionRom=json_data.get("PcieSlotNvme2optionRom"),
            PcieSlotNvme3linkSpeed=json_data.get("PcieSlotNvme3linkSpeed"),
            PcieSlotNvme3optionRom=json_data.get("PcieSlotNvme3optionRom"),
            PcieSlotNvme4linkSpeed=json_data.get("PcieSlotNvme4linkSpeed"),
            PcieSlotNvme4optionRom=json_data.get("PcieSlotNvme4optionRom"),
            PcieSlotNvme5linkSpeed=json_data.get("PcieSlotNvme5linkSpeed"),
            PcieSlotNvme5optionRom=json_data.get("PcieSlotNvme5optionRom"),
            PcieSlotNvme6linkSpeed=json_data.get("PcieSlotNvme6linkSpeed"),
            PcieSlotNvme6optionRom=json_data.get("PcieSlotNvme6optionRom"),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            PopSupport=json_data.get("PopSupport"),
            PostErrorPause=json_data.get("PostErrorPause"),
            PostPackageRepair=json_data.get("PostPackageRepair"),
            ProcessorC1e=json_data.get("ProcessorC1e"),
            ProcessorC3report=json_data.get("ProcessorC3report"),
            ProcessorC6report=json_data.get("ProcessorC6report"),
            ProcessorCstate=json_data.get("ProcessorCstate"),
            Profiles=deserialize_list(json_data.get("Profiles"), ProfilesDefinition),
            Psata=json_data.get("Psata"),
            PstateCoordType=json_data.get("PstateCoordType"),
            PuttyKeyPad=json_data.get("PuttyKeyPad"),
            PwrPerfTuning=json_data.get("PwrPerfTuning"),
            QpiLinkFrequency=json_data.get("QpiLinkFrequency"),
            QpiLinkSpeed=json_data.get("QpiLinkSpeed"),
            QpiSnoopMode=json_data.get("QpiSnoopMode"),
            RankInterLeave=json_data.get("RankInterLeave"),
            RedirectionAfterPost=json_data.get("RedirectionAfterPost"),
            SataModeSelect=json_data.get("SataModeSelect"),
            SelectMemoryRasConfiguration=json_data.get("SelectMemoryRasConfiguration"),
            SelectPprType=json_data.get("SelectPprType"),
            SerialPortAenable=json_data.get("SerialPortAenable"),
            Sev=json_data.get("Sev"),
            SgxAutoRegistrationAgent=json_data.get("SgxAutoRegistrationAgent"),
            SgxEpoch0=json_data.get("SgxEpoch0"),
            SgxEpoch1=json_data.get("SgxEpoch1"),
            SgxFactoryReset=json_data.get("SgxFactoryReset"),
            SgxLePubKeyHash0=json_data.get("SgxLePubKeyHash0"),
            SgxLePubKeyHash1=json_data.get("SgxLePubKeyHash1"),
            SgxLePubKeyHash2=json_data.get("SgxLePubKeyHash2"),
            SgxLePubKeyHash3=json_data.get("SgxLePubKeyHash3"),
            SgxLeWr=json_data.get("SgxLeWr"),
            SgxPackageInfoInBandAccess=json_data.get("SgxPackageInfoInBandAccess"),
            SgxQos=json_data.get("SgxQos"),
            SharedScope=json_data.get("SharedScope"),
            SinglePctlEnable=json_data.get("SinglePctlEnable"),
            Slot10linkSpeed=json_data.get("Slot10linkSpeed"),
            Slot10state=json_data.get("Slot10state"),
            Slot11linkSpeed=json_data.get("Slot11linkSpeed"),
            Slot11state=json_data.get("Slot11state"),
            Slot12linkSpeed=json_data.get("Slot12linkSpeed"),
            Slot12state=json_data.get("Slot12state"),
            Slot13state=json_data.get("Slot13state"),
            Slot14state=json_data.get("Slot14state"),
            Slot1linkSpeed=json_data.get("Slot1linkSpeed"),
            Slot1state=json_data.get("Slot1state"),
            Slot2linkSpeed=json_data.get("Slot2linkSpeed"),
            Slot2state=json_data.get("Slot2state"),
            Slot3linkSpeed=json_data.get("Slot3linkSpeed"),
            Slot3state=json_data.get("Slot3state"),
            Slot4linkSpeed=json_data.get("Slot4linkSpeed"),
            Slot4state=json_data.get("Slot4state"),
            Slot5linkSpeed=json_data.get("Slot5linkSpeed"),
            Slot5state=json_data.get("Slot5state"),
            Slot6linkSpeed=json_data.get("Slot6linkSpeed"),
            Slot6state=json_data.get("Slot6state"),
            Slot7linkSpeed=json_data.get("Slot7linkSpeed"),
            Slot7state=json_data.get("Slot7state"),
            Slot8linkSpeed=json_data.get("Slot8linkSpeed"),
            Slot8state=json_data.get("Slot8state"),
            Slot9linkSpeed=json_data.get("Slot9linkSpeed"),
            Slot9state=json_data.get("Slot9state"),
            SlotFlomLinkSpeed=json_data.get("SlotFlomLinkSpeed"),
            SlotFrontNvme10linkSpeed=json_data.get("SlotFrontNvme10linkSpeed"),
            SlotFrontNvme10optionRom=json_data.get("SlotFrontNvme10optionRom"),
            SlotFrontNvme11linkSpeed=json_data.get("SlotFrontNvme11linkSpeed"),
            SlotFrontNvme11optionRom=json_data.get("SlotFrontNvme11optionRom"),
            SlotFrontNvme12linkSpeed=json_data.get("SlotFrontNvme12linkSpeed"),
            SlotFrontNvme12optionRom=json_data.get("SlotFrontNvme12optionRom"),
            SlotFrontNvme13optionRom=json_data.get("SlotFrontNvme13optionRom"),
            SlotFrontNvme14optionRom=json_data.get("SlotFrontNvme14optionRom"),
            SlotFrontNvme15optionRom=json_data.get("SlotFrontNvme15optionRom"),
            SlotFrontNvme16optionRom=json_data.get("SlotFrontNvme16optionRom"),
            SlotFrontNvme17optionRom=json_data.get("SlotFrontNvme17optionRom"),
            SlotFrontNvme18optionRom=json_data.get("SlotFrontNvme18optionRom"),
            SlotFrontNvme19optionRom=json_data.get("SlotFrontNvme19optionRom"),
            SlotFrontNvme1linkSpeed=json_data.get("SlotFrontNvme1linkSpeed"),
            SlotFrontNvme1optionRom=json_data.get("SlotFrontNvme1optionRom"),
            SlotFrontNvme20optionRom=json_data.get("SlotFrontNvme20optionRom"),
            SlotFrontNvme21optionRom=json_data.get("SlotFrontNvme21optionRom"),
            SlotFrontNvme22optionRom=json_data.get("SlotFrontNvme22optionRom"),
            SlotFrontNvme23optionRom=json_data.get("SlotFrontNvme23optionRom"),
            SlotFrontNvme24optionRom=json_data.get("SlotFrontNvme24optionRom"),
            SlotFrontNvme2linkSpeed=json_data.get("SlotFrontNvme2linkSpeed"),
            SlotFrontNvme2optionRom=json_data.get("SlotFrontNvme2optionRom"),
            SlotFrontNvme3linkSpeed=json_data.get("SlotFrontNvme3linkSpeed"),
            SlotFrontNvme3optionRom=json_data.get("SlotFrontNvme3optionRom"),
            SlotFrontNvme4linkSpeed=json_data.get("SlotFrontNvme4linkSpeed"),
            SlotFrontNvme4optionRom=json_data.get("SlotFrontNvme4optionRom"),
            SlotFrontNvme5linkSpeed=json_data.get("SlotFrontNvme5linkSpeed"),
            SlotFrontNvme5optionRom=json_data.get("SlotFrontNvme5optionRom"),
            SlotFrontNvme6linkSpeed=json_data.get("SlotFrontNvme6linkSpeed"),
            SlotFrontNvme6optionRom=json_data.get("SlotFrontNvme6optionRom"),
            SlotFrontNvme7linkSpeed=json_data.get("SlotFrontNvme7linkSpeed"),
            SlotFrontNvme7optionRom=json_data.get("SlotFrontNvme7optionRom"),
            SlotFrontNvme8linkSpeed=json_data.get("SlotFrontNvme8linkSpeed"),
            SlotFrontNvme8optionRom=json_data.get("SlotFrontNvme8optionRom"),
            SlotFrontNvme9linkSpeed=json_data.get("SlotFrontNvme9linkSpeed"),
            SlotFrontNvme9optionRom=json_data.get("SlotFrontNvme9optionRom"),
            SlotFrontSlot5linkSpeed=json_data.get("SlotFrontSlot5linkSpeed"),
            SlotFrontSlot6linkSpeed=json_data.get("SlotFrontSlot6linkSpeed"),
            SlotGpu1state=json_data.get("SlotGpu1state"),
            SlotGpu2state=json_data.get("SlotGpu2state"),
            SlotGpu3state=json_data.get("SlotGpu3state"),
            SlotGpu4state=json_data.get("SlotGpu4state"),
            SlotGpu5state=json_data.get("SlotGpu5state"),
            SlotGpu6state=json_data.get("SlotGpu6state"),
            SlotGpu7state=json_data.get("SlotGpu7state"),
            SlotGpu8state=json_data.get("SlotGpu8state"),
            SlotHbaLinkSpeed=json_data.get("SlotHbaLinkSpeed"),
            SlotHbaState=json_data.get("SlotHbaState"),
            SlotLom1link=json_data.get("SlotLom1link"),
            SlotLom2link=json_data.get("SlotLom2link"),
            SlotMezzState=json_data.get("SlotMezzState"),
            SlotMlomLinkSpeed=json_data.get("SlotMlomLinkSpeed"),
            SlotMlomState=json_data.get("SlotMlomState"),
            SlotMraidLinkSpeed=json_data.get("SlotMraidLinkSpeed"),
            SlotMraidState=json_data.get("SlotMraidState"),
            SlotN10state=json_data.get("SlotN10state"),
            SlotN11state=json_data.get("SlotN11state"),
            SlotN12state=json_data.get("SlotN12state"),
            SlotN13state=json_data.get("SlotN13state"),
            SlotN14state=json_data.get("SlotN14state"),
            SlotN15state=json_data.get("SlotN15state"),
            SlotN16state=json_data.get("SlotN16state"),
            SlotN17state=json_data.get("SlotN17state"),
            SlotN18state=json_data.get("SlotN18state"),
            SlotN19state=json_data.get("SlotN19state"),
            SlotN1state=json_data.get("SlotN1state"),
            SlotN20state=json_data.get("SlotN20state"),
            SlotN21state=json_data.get("SlotN21state"),
            SlotN22state=json_data.get("SlotN22state"),
            SlotN23state=json_data.get("SlotN23state"),
            SlotN24state=json_data.get("SlotN24state"),
            SlotN2state=json_data.get("SlotN2state"),
            SlotN3state=json_data.get("SlotN3state"),
            SlotN4state=json_data.get("SlotN4state"),
            SlotN5state=json_data.get("SlotN5state"),
            SlotN6state=json_data.get("SlotN6state"),
            SlotN7state=json_data.get("SlotN7state"),
            SlotN8state=json_data.get("SlotN8state"),
            SlotN9state=json_data.get("SlotN9state"),
            SlotRaidLinkSpeed=json_data.get("SlotRaidLinkSpeed"),
            SlotRaidState=json_data.get("SlotRaidState"),
            SlotRearNvme1linkSpeed=json_data.get("SlotRearNvme1linkSpeed"),
            SlotRearNvme1state=json_data.get("SlotRearNvme1state"),
            SlotRearNvme2linkSpeed=json_data.get("SlotRearNvme2linkSpeed"),
            SlotRearNvme2state=json_data.get("SlotRearNvme2state"),
            SlotRearNvme3linkSpeed=json_data.get("SlotRearNvme3linkSpeed"),
            SlotRearNvme3state=json_data.get("SlotRearNvme3state"),
            SlotRearNvme4linkSpeed=json_data.get("SlotRearNvme4linkSpeed"),
            SlotRearNvme4state=json_data.get("SlotRearNvme4state"),
            SlotRearNvme5state=json_data.get("SlotRearNvme5state"),
            SlotRearNvme6state=json_data.get("SlotRearNvme6state"),
            SlotRearNvme7state=json_data.get("SlotRearNvme7state"),
            SlotRearNvme8state=json_data.get("SlotRearNvme8state"),
            SlotRiser1linkSpeed=json_data.get("SlotRiser1linkSpeed"),
            SlotRiser1slot1linkSpeed=json_data.get("SlotRiser1slot1linkSpeed"),
            SlotRiser1slot2linkSpeed=json_data.get("SlotRiser1slot2linkSpeed"),
            SlotRiser1slot3linkSpeed=json_data.get("SlotRiser1slot3linkSpeed"),
            SlotRiser2linkSpeed=json_data.get("SlotRiser2linkSpeed"),
            SlotRiser2slot4linkSpeed=json_data.get("SlotRiser2slot4linkSpeed"),
            SlotRiser2slot5linkSpeed=json_data.get("SlotRiser2slot5linkSpeed"),
            SlotRiser2slot6linkSpeed=json_data.get("SlotRiser2slot6linkSpeed"),
            SlotSasState=json_data.get("SlotSasState"),
            SlotSsdSlot1linkSpeed=json_data.get("SlotSsdSlot1linkSpeed"),
            SlotSsdSlot2linkSpeed=json_data.get("SlotSsdSlot2linkSpeed"),
            Smee=json_data.get("Smee"),
            SmtMode=json_data.get("SmtMode"),
            Snc=json_data.get("Snc"),
            SnoopyModeFor2lm=json_data.get("SnoopyModeFor2lm"),
            SnoopyModeForAd=json_data.get("SnoopyModeForAd"),
            SparingMode=json_data.get("SparingMode"),
            SrIov=json_data.get("SrIov"),
            StreamerPrefetch=json_data.get("StreamerPrefetch"),
            SvmMode=json_data.get("SvmMode"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TerminalType=json_data.get("TerminalType"),
            TpmControl=json_data.get("TpmControl"),
            TpmPendingOperation=json_data.get("TpmPendingOperation"),
            TpmSupport=json_data.get("TpmSupport"),
            Tsme=json_data.get("Tsme"),
            TxtSupport=json_data.get("TxtSupport"),
            UcsmBootOrderRule=json_data.get("UcsmBootOrderRule"),
            UfsDisable=json_data.get("UfsDisable"),
            UmaBasedClustering=json_data.get("UmaBasedClustering"),
            UsbEmul6064=json_data.get("UsbEmul6064"),
            UsbPortFront=json_data.get("UsbPortFront"),
            UsbPortInternal=json_data.get("UsbPortInternal"),
            UsbPortKvm=json_data.get("UsbPortKvm"),
            UsbPortRear=json_data.get("UsbPortRear"),
            UsbPortSdCard=json_data.get("UsbPortSdCard"),
            UsbPortVmedia=json_data.get("UsbPortVmedia"),
            UsbXhciSupport=json_data.get("UsbXhciSupport"),
            VersionContext=deserialize_list(json_data.get("VersionContext"), VersionContextDefinition3),
            VgaPriority=json_data.get("VgaPriority"),
            VmdEnable=json_data.get("VmdEnable"),
            VolMemoryMode=json_data.get("VolMemoryMode"),
            WorkLoadConfig=json_data.get("WorkLoadConfig"),
            XptPrefetch=json_data.get("XptPrefetch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AncestorsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AncestorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AncestorsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AncestorsDefinition = AncestorsDefinition


@dataclass
class OrganizationDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OrganizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrganizationDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrganizationDefinition = OrganizationDefinition


@dataclass
class ParentDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParentDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParentDefinition = ParentDefinition


@dataclass
class PermissionResourcesDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PermissionResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PermissionResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PermissionResourcesDefinition = PermissionResourcesDefinition


@dataclass
class ProfilesDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProfilesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProfilesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProfilesDefinition = ProfilesDefinition


@dataclass
class TagsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class VersionContextDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InterestedMos: Optional[Sequence["_VersionContextDefinition"]]
    NrVersion: Optional[str]
    ObjectType: Optional[str]
    RefMo: Optional[Sequence["_VersionContextDefinition2"]]
    Timestamp: Optional[str]
    VersionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition3"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            InterestedMos=deserialize_list(json_data.get("InterestedMos"), VersionContextDefinition),
            NrVersion=json_data.get("NrVersion"),
            ObjectType=json_data.get("ObjectType"),
            RefMo=deserialize_list(json_data.get("RefMo"), VersionContextDefinition2),
            Timestamp=json_data.get("Timestamp"),
            VersionType=json_data.get("VersionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition3 = VersionContextDefinition3


@dataclass
class VersionContextDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition = VersionContextDefinition


@dataclass
class VersionContextDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition2 = VersionContextDefinition2


