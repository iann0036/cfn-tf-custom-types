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
    AcceleratedNetworking: Optional[bool]
    ActiveStandby: Optional[bool]
    AggressiveFailureDetection: Optional[bool]
    Algo: Optional[str]
    AllowBurst: Optional[bool]
    AppCachePercent: Optional[float]
    AppCacheThreshold: Optional[float]
    AppLearningMemoryPercent: Optional[float]
    ArchiveShmLimit: Optional[float]
    AsyncSsl: Optional[bool]
    AsyncSslThreads: Optional[float]
    AutoRebalance: Optional[bool]
    AutoRebalanceCapacityPerSe: Optional[Sequence[float]]
    AutoRebalanceCriteria: Optional[Sequence[str]]
    AutoRebalanceInterval: Optional[float]
    AutoRedistributeActiveStandbyLoad: Optional[bool]
    AvailabilityZoneRefs: Optional[Sequence[str]]
    BgpStateUpdateInterval: Optional[float]
    BufferSe: Optional[float]
    CloudRef: Optional[str]
    CompressIpRulesForEachNsSubnet: Optional[bool]
    ConfigDebugsOnAllCores: Optional[bool]
    ConnectionMemoryPercentage: Optional[float]
    CoreShmAppCache: Optional[bool]
    CoreShmAppLearning: Optional[bool]
    CpuReserve: Optional[bool]
    CpuSocketAffinity: Optional[bool]
    CustomSecuritygroupsData: Optional[Sequence[str]]
    CustomSecuritygroupsMgmt: Optional[Sequence[str]]
    DataNetworkId: Optional[str]
    DatascriptTimeout: Optional[float]
    DedicatedDispatcherCore: Optional[bool]
    Description: Optional[str]
    DisableAviSecuritygroups: Optional[bool]
    DisableCsumOffloads: Optional[bool]
    DisableFlowProbes: Optional[bool]
    DisableGro: Optional[bool]
    DisableSeMemoryCheck: Optional[bool]
    DisableTso: Optional[bool]
    DiskPerSe: Optional[float]
    DistributeLoadActiveStandby: Optional[bool]
    DistributeQueues: Optional[bool]
    DistributeVnics: Optional[bool]
    DpAggressiveHbFrequency: Optional[float]
    DpAggressiveHbTimeoutCount: Optional[float]
    DpHbFrequency: Optional[float]
    DpHbTimeoutCount: Optional[float]
    EnableGratarpPermanent: Optional[bool]
    EnableHsmPriming: Optional[bool]
    EnableMultiLb: Optional[bool]
    EnablePcapTxRing: Optional[bool]
    EphemeralPortrangeEnd: Optional[float]
    EphemeralPortrangeStart: Optional[float]
    ExtraConfigMultiplier: Optional[float]
    ExtraSharedConfigMemory: Optional[float]
    FlowTableNewSynMaxEntries: Optional[float]
    FreeListSize: Optional[float]
    GratarpPermanentPeriodicity: Optional[float]
    HaMode: Optional[str]
    HandlePerPktAttack: Optional[bool]
    HardwaresecuritymodulegroupRef: Optional[str]
    HeapMinimumConfigMemory: Optional[float]
    HmOnStandby: Optional[bool]
    HostAttributeKey: Optional[str]
    HostAttributeValue: Optional[str]
    HostGatewayMonitor: Optional[bool]
    Hypervisor: Optional[str]
    Id: Optional[str]
    IgnoreRttThreshold: Optional[float]
    IngressAccessData: Optional[str]
    IngressAccessMgmt: Optional[str]
    InstanceFlavor: Optional[str]
    LeastLoadCoreSelection: Optional[bool]
    LicenseTier: Optional[str]
    LicenseType: Optional[str]
    LogDisksz: Optional[float]
    LogMallocFailure: Optional[bool]
    MaxConcurrentExternalHm: Optional[float]
    MaxCpuUsage: Optional[float]
    MaxMemoryPerMempool: Optional[float]
    MaxNumSeDps: Optional[float]
    MaxPublicIpsPerLb: Optional[float]
    MaxQueuesPerVnic: Optional[float]
    MaxRulesPerLb: Optional[float]
    MaxScaleoutPerVs: Optional[float]
    MaxSe: Optional[float]
    MaxVsPerSe: Optional[float]
    MemReserve: Optional[bool]
    MemoryForConfigUpdate: Optional[float]
    MemoryPerSe: Optional[float]
    MgmtNetworkRef: Optional[str]
    MinCpuUsage: Optional[float]
    MinScaleoutPerVs: Optional[float]
    MinSe: Optional[float]
    MinimumConnectionMemory: Optional[float]
    NLogStreamingThreads: Optional[float]
    Name: Optional[str]
    NonSignificantLogThrottle: Optional[float]
    NumDispatcherCores: Optional[float]
    NumFlowCoresSumChangesToIgnore: Optional[float]
    ObjsyncPort: Optional[float]
    OpenstackAvailabilityZones: Optional[Sequence[str]]
    OpenstackMgmtNetworkName: Optional[str]
    OpenstackMgmtNetworkUuid: Optional[str]
    OsReservedMemory: Optional[float]
    PcapTxMode: Optional[str]
    PcapTxRingRdBalancingFactor: Optional[float]
    PerApp: Optional[bool]
    PerVsAdmissionControl: Optional[bool]
    PlacementMode: Optional[str]
    RebootOnPanic: Optional[bool]
    ResyncTimeInterval: Optional[float]
    SeBandwidthType: Optional[str]
    SeDelayedFlowDelete: Optional[bool]
    SeDeprovisionDelay: Optional[float]
    SeDpHmDrops: Optional[float]
    SeDpIsolation: Optional[bool]
    SeDpIsolationNumNonDpCpus: Optional[float]
    SeDpMaxHbVersion: Optional[float]
    SeDpVnicQueueStallEventSleep: Optional[float]
    SeDpVnicQueueStallThreshold: Optional[float]
    SeDpVnicQueueStallTimeout: Optional[float]
    SeDpVnicRestartOnQueueStallCount: Optional[float]
    SeDpVnicStallSeRestartWindow: Optional[float]
    SeDpdkPmd: Optional[float]
    SeFlowProbeRetries: Optional[float]
    SeFlowProbeRetryTimer: Optional[float]
    SeHyperthreadedMode: Optional[str]
    SeIpEncapIpc: Optional[float]
    SeKniBurstFactor: Optional[float]
    SeL3EncapIpc: Optional[float]
    SeLro: Optional[bool]
    SeMpRingRetryCount: Optional[float]
    SeMtu: Optional[float]
    SeNamePrefix: Optional[str]
    SePcapLookahead: Optional[bool]
    SePcapPktCount: Optional[float]
    SePcapPktSz: Optional[float]
    SePcapQdiscBypass: Optional[bool]
    SePcapReinitFrequency: Optional[float]
    SePcapReinitThreshold: Optional[float]
    SeProbePort: Optional[float]
    SeRumSamplingNavInterval: Optional[float]
    SeRumSamplingNavPercent: Optional[float]
    SeRumSamplingResInterval: Optional[float]
    SeRumSamplingResPercent: Optional[float]
    SeSbDedicatedCore: Optional[bool]
    SeSbThreads: Optional[float]
    SeThreadMultiplier: Optional[float]
    SeTunnelMode: Optional[float]
    SeTunnelUdpPort: Optional[float]
    SeTxBatchSize: Optional[float]
    SeTxqThreshold: Optional[float]
    SeUdpEncapIpc: Optional[float]
    SeUseDpdk: Optional[float]
    SeVnicTxSwQueueFlushFrequency: Optional[float]
    SeVnicTxSwQueueSize: Optional[float]
    SeVsHbMaxPktsInBatch: Optional[float]
    SeVsHbMaxVsInPkt: Optional[float]
    SelfSeElection: Optional[bool]
    ShmMinimumConfigMemory: Optional[float]
    SignificantLogThrottle: Optional[float]
    SslPreprocessSniHostname: Optional[bool]
    TenantRef: Optional[str]
    TransientSharedMemoryMax: Optional[float]
    UdfLogThrottle: Optional[float]
    UseHyperthreadedCores: Optional[bool]
    UseObjsync: Optional[bool]
    UseStandardAlb: Optional[bool]
    Uuid: Optional[str]
    VcenterDatastoreMode: Optional[str]
    VcenterDatastoresInclude: Optional[bool]
    VcenterFolder: Optional[str]
    VcpusPerSe: Optional[float]
    VsHostRedundancy: Optional[bool]
    VsScaleinTimeout: Optional[float]
    VsScaleinTimeoutForUpgrade: Optional[float]
    VsScaleoutTimeout: Optional[float]
    VsSeScaleoutAdditionalWaitTime: Optional[float]
    VsSeScaleoutReadyTimeout: Optional[float]
    VsSwitchoverTimeout: Optional[float]
    VssPlacementEnabled: Optional[bool]
    WafMempool: Optional[bool]
    WafMempoolSize: Optional[float]
    CustomTag: Optional[Sequence["_CustomTagDefinition"]]
    GcpConfig: Optional[Sequence["_GcpConfigDefinition"]]
    InstanceFlavorInfo: Optional[Sequence["_InstanceFlavorInfoDefinition"]]
    Iptables: Optional[Sequence["_IptablesDefinition"]]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    MgmtSubnet: Optional[Sequence["_MgmtSubnetDefinition"]]
    ObjsyncConfig: Optional[Sequence["_ObjsyncConfigDefinition"]]
    RealtimeSeMetrics: Optional[Sequence["_RealtimeSeMetricsDefinition"]]
    SeDosProfile: Optional[Sequence["_SeDosProfileDefinition"]]
    SeGroupAnalyticsPolicy: Optional[Sequence["_SeGroupAnalyticsPolicyDefinition"]]
    SeRlProp: Optional[Sequence["_SeRlPropDefinition"]]
    SeTracertPortRange: Optional[Sequence["_SeTracertPortRangeDefinition"]]
    ServiceIp6Subnets: Optional[Sequence["_ServiceIp6SubnetsDefinition"]]
    ServiceIpSubnets: Optional[Sequence["_ServiceIpSubnetsDefinition"]]
    VcenterClusters: Optional[Sequence["_VcenterClustersDefinition"]]
    VcenterDatastores: Optional[Sequence["_VcenterDatastoresDefinition"]]
    VcenterHosts: Optional[Sequence["_VcenterHostsDefinition"]]
    Vcenters: Optional[Sequence["_VcentersDefinition"]]
    VipAsg: Optional[Sequence["_VipAsgDefinition"]]
    VssPlacement: Optional[Sequence["_VssPlacementDefinition"]]

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
            AcceleratedNetworking=json_data.get("AcceleratedNetworking"),
            ActiveStandby=json_data.get("ActiveStandby"),
            AggressiveFailureDetection=json_data.get("AggressiveFailureDetection"),
            Algo=json_data.get("Algo"),
            AllowBurst=json_data.get("AllowBurst"),
            AppCachePercent=json_data.get("AppCachePercent"),
            AppCacheThreshold=json_data.get("AppCacheThreshold"),
            AppLearningMemoryPercent=json_data.get("AppLearningMemoryPercent"),
            ArchiveShmLimit=json_data.get("ArchiveShmLimit"),
            AsyncSsl=json_data.get("AsyncSsl"),
            AsyncSslThreads=json_data.get("AsyncSslThreads"),
            AutoRebalance=json_data.get("AutoRebalance"),
            AutoRebalanceCapacityPerSe=json_data.get("AutoRebalanceCapacityPerSe"),
            AutoRebalanceCriteria=json_data.get("AutoRebalanceCriteria"),
            AutoRebalanceInterval=json_data.get("AutoRebalanceInterval"),
            AutoRedistributeActiveStandbyLoad=json_data.get("AutoRedistributeActiveStandbyLoad"),
            AvailabilityZoneRefs=json_data.get("AvailabilityZoneRefs"),
            BgpStateUpdateInterval=json_data.get("BgpStateUpdateInterval"),
            BufferSe=json_data.get("BufferSe"),
            CloudRef=json_data.get("CloudRef"),
            CompressIpRulesForEachNsSubnet=json_data.get("CompressIpRulesForEachNsSubnet"),
            ConfigDebugsOnAllCores=json_data.get("ConfigDebugsOnAllCores"),
            ConnectionMemoryPercentage=json_data.get("ConnectionMemoryPercentage"),
            CoreShmAppCache=json_data.get("CoreShmAppCache"),
            CoreShmAppLearning=json_data.get("CoreShmAppLearning"),
            CpuReserve=json_data.get("CpuReserve"),
            CpuSocketAffinity=json_data.get("CpuSocketAffinity"),
            CustomSecuritygroupsData=json_data.get("CustomSecuritygroupsData"),
            CustomSecuritygroupsMgmt=json_data.get("CustomSecuritygroupsMgmt"),
            DataNetworkId=json_data.get("DataNetworkId"),
            DatascriptTimeout=json_data.get("DatascriptTimeout"),
            DedicatedDispatcherCore=json_data.get("DedicatedDispatcherCore"),
            Description=json_data.get("Description"),
            DisableAviSecuritygroups=json_data.get("DisableAviSecuritygroups"),
            DisableCsumOffloads=json_data.get("DisableCsumOffloads"),
            DisableFlowProbes=json_data.get("DisableFlowProbes"),
            DisableGro=json_data.get("DisableGro"),
            DisableSeMemoryCheck=json_data.get("DisableSeMemoryCheck"),
            DisableTso=json_data.get("DisableTso"),
            DiskPerSe=json_data.get("DiskPerSe"),
            DistributeLoadActiveStandby=json_data.get("DistributeLoadActiveStandby"),
            DistributeQueues=json_data.get("DistributeQueues"),
            DistributeVnics=json_data.get("DistributeVnics"),
            DpAggressiveHbFrequency=json_data.get("DpAggressiveHbFrequency"),
            DpAggressiveHbTimeoutCount=json_data.get("DpAggressiveHbTimeoutCount"),
            DpHbFrequency=json_data.get("DpHbFrequency"),
            DpHbTimeoutCount=json_data.get("DpHbTimeoutCount"),
            EnableGratarpPermanent=json_data.get("EnableGratarpPermanent"),
            EnableHsmPriming=json_data.get("EnableHsmPriming"),
            EnableMultiLb=json_data.get("EnableMultiLb"),
            EnablePcapTxRing=json_data.get("EnablePcapTxRing"),
            EphemeralPortrangeEnd=json_data.get("EphemeralPortrangeEnd"),
            EphemeralPortrangeStart=json_data.get("EphemeralPortrangeStart"),
            ExtraConfigMultiplier=json_data.get("ExtraConfigMultiplier"),
            ExtraSharedConfigMemory=json_data.get("ExtraSharedConfigMemory"),
            FlowTableNewSynMaxEntries=json_data.get("FlowTableNewSynMaxEntries"),
            FreeListSize=json_data.get("FreeListSize"),
            GratarpPermanentPeriodicity=json_data.get("GratarpPermanentPeriodicity"),
            HaMode=json_data.get("HaMode"),
            HandlePerPktAttack=json_data.get("HandlePerPktAttack"),
            HardwaresecuritymodulegroupRef=json_data.get("HardwaresecuritymodulegroupRef"),
            HeapMinimumConfigMemory=json_data.get("HeapMinimumConfigMemory"),
            HmOnStandby=json_data.get("HmOnStandby"),
            HostAttributeKey=json_data.get("HostAttributeKey"),
            HostAttributeValue=json_data.get("HostAttributeValue"),
            HostGatewayMonitor=json_data.get("HostGatewayMonitor"),
            Hypervisor=json_data.get("Hypervisor"),
            Id=json_data.get("Id"),
            IgnoreRttThreshold=json_data.get("IgnoreRttThreshold"),
            IngressAccessData=json_data.get("IngressAccessData"),
            IngressAccessMgmt=json_data.get("IngressAccessMgmt"),
            InstanceFlavor=json_data.get("InstanceFlavor"),
            LeastLoadCoreSelection=json_data.get("LeastLoadCoreSelection"),
            LicenseTier=json_data.get("LicenseTier"),
            LicenseType=json_data.get("LicenseType"),
            LogDisksz=json_data.get("LogDisksz"),
            LogMallocFailure=json_data.get("LogMallocFailure"),
            MaxConcurrentExternalHm=json_data.get("MaxConcurrentExternalHm"),
            MaxCpuUsage=json_data.get("MaxCpuUsage"),
            MaxMemoryPerMempool=json_data.get("MaxMemoryPerMempool"),
            MaxNumSeDps=json_data.get("MaxNumSeDps"),
            MaxPublicIpsPerLb=json_data.get("MaxPublicIpsPerLb"),
            MaxQueuesPerVnic=json_data.get("MaxQueuesPerVnic"),
            MaxRulesPerLb=json_data.get("MaxRulesPerLb"),
            MaxScaleoutPerVs=json_data.get("MaxScaleoutPerVs"),
            MaxSe=json_data.get("MaxSe"),
            MaxVsPerSe=json_data.get("MaxVsPerSe"),
            MemReserve=json_data.get("MemReserve"),
            MemoryForConfigUpdate=json_data.get("MemoryForConfigUpdate"),
            MemoryPerSe=json_data.get("MemoryPerSe"),
            MgmtNetworkRef=json_data.get("MgmtNetworkRef"),
            MinCpuUsage=json_data.get("MinCpuUsage"),
            MinScaleoutPerVs=json_data.get("MinScaleoutPerVs"),
            MinSe=json_data.get("MinSe"),
            MinimumConnectionMemory=json_data.get("MinimumConnectionMemory"),
            NLogStreamingThreads=json_data.get("NLogStreamingThreads"),
            Name=json_data.get("Name"),
            NonSignificantLogThrottle=json_data.get("NonSignificantLogThrottle"),
            NumDispatcherCores=json_data.get("NumDispatcherCores"),
            NumFlowCoresSumChangesToIgnore=json_data.get("NumFlowCoresSumChangesToIgnore"),
            ObjsyncPort=json_data.get("ObjsyncPort"),
            OpenstackAvailabilityZones=json_data.get("OpenstackAvailabilityZones"),
            OpenstackMgmtNetworkName=json_data.get("OpenstackMgmtNetworkName"),
            OpenstackMgmtNetworkUuid=json_data.get("OpenstackMgmtNetworkUuid"),
            OsReservedMemory=json_data.get("OsReservedMemory"),
            PcapTxMode=json_data.get("PcapTxMode"),
            PcapTxRingRdBalancingFactor=json_data.get("PcapTxRingRdBalancingFactor"),
            PerApp=json_data.get("PerApp"),
            PerVsAdmissionControl=json_data.get("PerVsAdmissionControl"),
            PlacementMode=json_data.get("PlacementMode"),
            RebootOnPanic=json_data.get("RebootOnPanic"),
            ResyncTimeInterval=json_data.get("ResyncTimeInterval"),
            SeBandwidthType=json_data.get("SeBandwidthType"),
            SeDelayedFlowDelete=json_data.get("SeDelayedFlowDelete"),
            SeDeprovisionDelay=json_data.get("SeDeprovisionDelay"),
            SeDpHmDrops=json_data.get("SeDpHmDrops"),
            SeDpIsolation=json_data.get("SeDpIsolation"),
            SeDpIsolationNumNonDpCpus=json_data.get("SeDpIsolationNumNonDpCpus"),
            SeDpMaxHbVersion=json_data.get("SeDpMaxHbVersion"),
            SeDpVnicQueueStallEventSleep=json_data.get("SeDpVnicQueueStallEventSleep"),
            SeDpVnicQueueStallThreshold=json_data.get("SeDpVnicQueueStallThreshold"),
            SeDpVnicQueueStallTimeout=json_data.get("SeDpVnicQueueStallTimeout"),
            SeDpVnicRestartOnQueueStallCount=json_data.get("SeDpVnicRestartOnQueueStallCount"),
            SeDpVnicStallSeRestartWindow=json_data.get("SeDpVnicStallSeRestartWindow"),
            SeDpdkPmd=json_data.get("SeDpdkPmd"),
            SeFlowProbeRetries=json_data.get("SeFlowProbeRetries"),
            SeFlowProbeRetryTimer=json_data.get("SeFlowProbeRetryTimer"),
            SeHyperthreadedMode=json_data.get("SeHyperthreadedMode"),
            SeIpEncapIpc=json_data.get("SeIpEncapIpc"),
            SeKniBurstFactor=json_data.get("SeKniBurstFactor"),
            SeL3EncapIpc=json_data.get("SeL3EncapIpc"),
            SeLro=json_data.get("SeLro"),
            SeMpRingRetryCount=json_data.get("SeMpRingRetryCount"),
            SeMtu=json_data.get("SeMtu"),
            SeNamePrefix=json_data.get("SeNamePrefix"),
            SePcapLookahead=json_data.get("SePcapLookahead"),
            SePcapPktCount=json_data.get("SePcapPktCount"),
            SePcapPktSz=json_data.get("SePcapPktSz"),
            SePcapQdiscBypass=json_data.get("SePcapQdiscBypass"),
            SePcapReinitFrequency=json_data.get("SePcapReinitFrequency"),
            SePcapReinitThreshold=json_data.get("SePcapReinitThreshold"),
            SeProbePort=json_data.get("SeProbePort"),
            SeRumSamplingNavInterval=json_data.get("SeRumSamplingNavInterval"),
            SeRumSamplingNavPercent=json_data.get("SeRumSamplingNavPercent"),
            SeRumSamplingResInterval=json_data.get("SeRumSamplingResInterval"),
            SeRumSamplingResPercent=json_data.get("SeRumSamplingResPercent"),
            SeSbDedicatedCore=json_data.get("SeSbDedicatedCore"),
            SeSbThreads=json_data.get("SeSbThreads"),
            SeThreadMultiplier=json_data.get("SeThreadMultiplier"),
            SeTunnelMode=json_data.get("SeTunnelMode"),
            SeTunnelUdpPort=json_data.get("SeTunnelUdpPort"),
            SeTxBatchSize=json_data.get("SeTxBatchSize"),
            SeTxqThreshold=json_data.get("SeTxqThreshold"),
            SeUdpEncapIpc=json_data.get("SeUdpEncapIpc"),
            SeUseDpdk=json_data.get("SeUseDpdk"),
            SeVnicTxSwQueueFlushFrequency=json_data.get("SeVnicTxSwQueueFlushFrequency"),
            SeVnicTxSwQueueSize=json_data.get("SeVnicTxSwQueueSize"),
            SeVsHbMaxPktsInBatch=json_data.get("SeVsHbMaxPktsInBatch"),
            SeVsHbMaxVsInPkt=json_data.get("SeVsHbMaxVsInPkt"),
            SelfSeElection=json_data.get("SelfSeElection"),
            ShmMinimumConfigMemory=json_data.get("ShmMinimumConfigMemory"),
            SignificantLogThrottle=json_data.get("SignificantLogThrottle"),
            SslPreprocessSniHostname=json_data.get("SslPreprocessSniHostname"),
            TenantRef=json_data.get("TenantRef"),
            TransientSharedMemoryMax=json_data.get("TransientSharedMemoryMax"),
            UdfLogThrottle=json_data.get("UdfLogThrottle"),
            UseHyperthreadedCores=json_data.get("UseHyperthreadedCores"),
            UseObjsync=json_data.get("UseObjsync"),
            UseStandardAlb=json_data.get("UseStandardAlb"),
            Uuid=json_data.get("Uuid"),
            VcenterDatastoreMode=json_data.get("VcenterDatastoreMode"),
            VcenterDatastoresInclude=json_data.get("VcenterDatastoresInclude"),
            VcenterFolder=json_data.get("VcenterFolder"),
            VcpusPerSe=json_data.get("VcpusPerSe"),
            VsHostRedundancy=json_data.get("VsHostRedundancy"),
            VsScaleinTimeout=json_data.get("VsScaleinTimeout"),
            VsScaleinTimeoutForUpgrade=json_data.get("VsScaleinTimeoutForUpgrade"),
            VsScaleoutTimeout=json_data.get("VsScaleoutTimeout"),
            VsSeScaleoutAdditionalWaitTime=json_data.get("VsSeScaleoutAdditionalWaitTime"),
            VsSeScaleoutReadyTimeout=json_data.get("VsSeScaleoutReadyTimeout"),
            VsSwitchoverTimeout=json_data.get("VsSwitchoverTimeout"),
            VssPlacementEnabled=json_data.get("VssPlacementEnabled"),
            WafMempool=json_data.get("WafMempool"),
            WafMempoolSize=json_data.get("WafMempoolSize"),
            CustomTag=deserialize_list(json_data.get("CustomTag"), CustomTagDefinition),
            GcpConfig=deserialize_list(json_data.get("GcpConfig"), GcpConfigDefinition),
            InstanceFlavorInfo=deserialize_list(json_data.get("InstanceFlavorInfo"), InstanceFlavorInfoDefinition),
            Iptables=deserialize_list(json_data.get("Iptables"), IptablesDefinition),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            MgmtSubnet=deserialize_list(json_data.get("MgmtSubnet"), MgmtSubnetDefinition),
            ObjsyncConfig=deserialize_list(json_data.get("ObjsyncConfig"), ObjsyncConfigDefinition),
            RealtimeSeMetrics=deserialize_list(json_data.get("RealtimeSeMetrics"), RealtimeSeMetricsDefinition),
            SeDosProfile=deserialize_list(json_data.get("SeDosProfile"), SeDosProfileDefinition),
            SeGroupAnalyticsPolicy=deserialize_list(json_data.get("SeGroupAnalyticsPolicy"), SeGroupAnalyticsPolicyDefinition),
            SeRlProp=deserialize_list(json_data.get("SeRlProp"), SeRlPropDefinition),
            SeTracertPortRange=deserialize_list(json_data.get("SeTracertPortRange"), SeTracertPortRangeDefinition),
            ServiceIp6Subnets=deserialize_list(json_data.get("ServiceIp6Subnets"), ServiceIp6SubnetsDefinition),
            ServiceIpSubnets=deserialize_list(json_data.get("ServiceIpSubnets"), ServiceIpSubnetsDefinition),
            VcenterClusters=deserialize_list(json_data.get("VcenterClusters"), VcenterClustersDefinition),
            VcenterDatastores=deserialize_list(json_data.get("VcenterDatastores"), VcenterDatastoresDefinition),
            VcenterHosts=deserialize_list(json_data.get("VcenterHosts"), VcenterHostsDefinition),
            Vcenters=deserialize_list(json_data.get("Vcenters"), VcentersDefinition),
            VipAsg=deserialize_list(json_data.get("VipAsg"), VipAsgDefinition),
            VssPlacement=deserialize_list(json_data.get("VssPlacement"), VssPlacementDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomTagDefinition(BaseModel):
    TagKey: Optional[str]
    TagVal: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomTagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomTagDefinition"]:
        if not json_data:
            return None
        return cls(
            TagKey=json_data.get("TagKey"),
            TagVal=json_data.get("TagVal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomTagDefinition = CustomTagDefinition


@dataclass
class GcpConfigDefinition(BaseModel):
    BackendDataVpcNetworkName: Optional[str]
    BackendDataVpcProjectId: Optional[str]
    BackendDataVpcSubnetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GcpConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcpConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BackendDataVpcNetworkName=json_data.get("BackendDataVpcNetworkName"),
            BackendDataVpcProjectId=json_data.get("BackendDataVpcProjectId"),
            BackendDataVpcSubnetName=json_data.get("BackendDataVpcSubnetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcpConfigDefinition = GcpConfigDefinition


@dataclass
class InstanceFlavorInfoDefinition(BaseModel):
    Cost: Optional[str]
    DiskGb: Optional[float]
    EnhancedNw: Optional[bool]
    Id: Optional[str]
    IsRecommended: Optional[bool]
    MaxIp6sPerNic: Optional[float]
    MaxIpsPerNic: Optional[float]
    MaxNics: Optional[float]
    Name: Optional[str]
    Public: Optional[bool]
    RamMb: Optional[float]
    Vcpus: Optional[float]
    Meta: Optional[Sequence["_MetaDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceFlavorInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceFlavorInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Cost=json_data.get("Cost"),
            DiskGb=json_data.get("DiskGb"),
            EnhancedNw=json_data.get("EnhancedNw"),
            Id=json_data.get("Id"),
            IsRecommended=json_data.get("IsRecommended"),
            MaxIp6sPerNic=json_data.get("MaxIp6sPerNic"),
            MaxIpsPerNic=json_data.get("MaxIpsPerNic"),
            MaxNics=json_data.get("MaxNics"),
            Name=json_data.get("Name"),
            Public=json_data.get("Public"),
            RamMb=json_data.get("RamMb"),
            Vcpus=json_data.get("Vcpus"),
            Meta=deserialize_list(json_data.get("Meta"), MetaDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceFlavorInfoDefinition = InstanceFlavorInfoDefinition


@dataclass
class MetaDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetaDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetaDefinition = MetaDefinition


@dataclass
class IptablesDefinition(BaseModel):
    Chain: Optional[str]
    Table: Optional[str]
    Rules: Optional[Sequence["_RulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IptablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IptablesDefinition"]:
        if not json_data:
            return None
        return cls(
            Chain=json_data.get("Chain"),
            Table=json_data.get("Table"),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IptablesDefinition = IptablesDefinition


@dataclass
class RulesDefinition(BaseModel):
    Action: Optional[str]
    InputInterface: Optional[str]
    OutputInterface: Optional[str]
    Proto: Optional[str]
    Tag: Optional[str]
    DnatIp: Optional[Sequence["_DnatIpDefinition"]]
    DstIp: Optional[Sequence["_DstIpDefinition"]]
    DstPort: Optional[Sequence["_DstPortDefinition"]]
    SrcIp: Optional[Sequence["_SrcIpDefinition"]]
    SrcPort: Optional[Sequence["_SrcPortDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            InputInterface=json_data.get("InputInterface"),
            OutputInterface=json_data.get("OutputInterface"),
            Proto=json_data.get("Proto"),
            Tag=json_data.get("Tag"),
            DnatIp=deserialize_list(json_data.get("DnatIp"), DnatIpDefinition),
            DstIp=deserialize_list(json_data.get("DstIp"), DstIpDefinition),
            DstPort=deserialize_list(json_data.get("DstPort"), DstPortDefinition),
            SrcIp=deserialize_list(json_data.get("SrcIp"), SrcIpDefinition),
            SrcPort=deserialize_list(json_data.get("SrcPort"), SrcPortDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class DnatIpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnatIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnatIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnatIpDefinition = DnatIpDefinition


@dataclass
class DstIpDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DstIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstIpDefinition = DstIpDefinition


@dataclass
class IpAddrDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddrDefinition = IpAddrDefinition


@dataclass
class DstPortDefinition(BaseModel):
    End: Optional[float]
    Start: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DstPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstPortDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstPortDefinition = DstPortDefinition


@dataclass
class SrcIpDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SrcIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcIpDefinition = SrcIpDefinition


@dataclass
class SrcPortDefinition(BaseModel):
    End: Optional[float]
    Start: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SrcPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcPortDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcPortDefinition = SrcPortDefinition


@dataclass
class LabelsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class MgmtSubnetDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MgmtSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MgmtSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MgmtSubnetDefinition = MgmtSubnetDefinition


@dataclass
class ObjsyncConfigDefinition(BaseModel):
    ObjsyncCpuLimit: Optional[float]
    ObjsyncHubElectInterval: Optional[float]
    ObjsyncReconcileInterval: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ObjsyncConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjsyncConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ObjsyncCpuLimit=json_data.get("ObjsyncCpuLimit"),
            ObjsyncHubElectInterval=json_data.get("ObjsyncHubElectInterval"),
            ObjsyncReconcileInterval=json_data.get("ObjsyncReconcileInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjsyncConfigDefinition = ObjsyncConfigDefinition


@dataclass
class RealtimeSeMetricsDefinition(BaseModel):
    Duration: Optional[float]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RealtimeSeMetricsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RealtimeSeMetricsDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RealtimeSeMetricsDefinition = RealtimeSeMetricsDefinition


@dataclass
class SeDosProfileDefinition(BaseModel):
    ThreshPeriod: Optional[float]
    ThreshInfo: Optional[Sequence["_ThreshInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SeDosProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeDosProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            ThreshPeriod=json_data.get("ThreshPeriod"),
            ThreshInfo=deserialize_list(json_data.get("ThreshInfo"), ThreshInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeDosProfileDefinition = SeDosProfileDefinition


@dataclass
class ThreshInfoDefinition(BaseModel):
    Attack: Optional[str]
    MaxValue: Optional[float]
    MinValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ThreshInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThreshInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Attack=json_data.get("Attack"),
            MaxValue=json_data.get("MaxValue"),
            MinValue=json_data.get("MinValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThreshInfoDefinition = ThreshInfoDefinition


@dataclass
class SeGroupAnalyticsPolicyDefinition(BaseModel):
    MetricsEventThresholds: Optional[Sequence["_MetricsEventThresholdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SeGroupAnalyticsPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeGroupAnalyticsPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            MetricsEventThresholds=deserialize_list(json_data.get("MetricsEventThresholds"), MetricsEventThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeGroupAnalyticsPolicyDefinition = SeGroupAnalyticsPolicyDefinition


@dataclass
class MetricsEventThresholdsDefinition(BaseModel):
    MetricsEventThresholdType: Optional[str]
    ResetThreshold: Optional[float]
    WatermarkThresholds: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricsEventThresholdsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricsEventThresholdsDefinition"]:
        if not json_data:
            return None
        return cls(
            MetricsEventThresholdType=json_data.get("MetricsEventThresholdType"),
            ResetThreshold=json_data.get("ResetThreshold"),
            WatermarkThresholds=json_data.get("WatermarkThresholds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricsEventThresholdsDefinition = MetricsEventThresholdsDefinition


@dataclass
class SeRlPropDefinition(BaseModel):
    MsfNumStages: Optional[float]
    MsfStageSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SeRlPropDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeRlPropDefinition"]:
        if not json_data:
            return None
        return cls(
            MsfNumStages=json_data.get("MsfNumStages"),
            MsfStageSize=json_data.get("MsfStageSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeRlPropDefinition = SeRlPropDefinition


@dataclass
class SeTracertPortRangeDefinition(BaseModel):
    End: Optional[float]
    Start: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SeTracertPortRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeTracertPortRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeTracertPortRangeDefinition = SeTracertPortRangeDefinition


@dataclass
class ServiceIp6SubnetsDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceIp6SubnetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceIp6SubnetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceIp6SubnetsDefinition = ServiceIp6SubnetsDefinition


@dataclass
class ServiceIpSubnetsDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceIpSubnetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceIpSubnetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceIpSubnetsDefinition = ServiceIpSubnetsDefinition


@dataclass
class VcenterClustersDefinition(BaseModel):
    ClusterRefs: Optional[Sequence[str]]
    Include: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_VcenterClustersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VcenterClustersDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterRefs=json_data.get("ClusterRefs"),
            Include=json_data.get("Include"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VcenterClustersDefinition = VcenterClustersDefinition


@dataclass
class VcenterDatastoresDefinition(BaseModel):
    DatastoreName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VcenterDatastoresDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VcenterDatastoresDefinition"]:
        if not json_data:
            return None
        return cls(
            DatastoreName=json_data.get("DatastoreName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VcenterDatastoresDefinition = VcenterDatastoresDefinition


@dataclass
class VcenterHostsDefinition(BaseModel):
    HostRefs: Optional[Sequence[str]]
    Include: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_VcenterHostsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VcenterHostsDefinition"]:
        if not json_data:
            return None
        return cls(
            HostRefs=json_data.get("HostRefs"),
            Include=json_data.get("Include"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VcenterHostsDefinition = VcenterHostsDefinition


@dataclass
class VcentersDefinition(BaseModel):
    VcenterFolder: Optional[str]
    VcenterRef: Optional[str]
    NsxtClusters: Optional[Sequence["_NsxtClustersDefinition"]]
    NsxtDatastores: Optional[Sequence["_NsxtDatastoresDefinition"]]
    NsxtHosts: Optional[Sequence["_NsxtHostsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VcentersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VcentersDefinition"]:
        if not json_data:
            return None
        return cls(
            VcenterFolder=json_data.get("VcenterFolder"),
            VcenterRef=json_data.get("VcenterRef"),
            NsxtClusters=deserialize_list(json_data.get("NsxtClusters"), NsxtClustersDefinition),
            NsxtDatastores=deserialize_list(json_data.get("NsxtDatastores"), NsxtDatastoresDefinition),
            NsxtHosts=deserialize_list(json_data.get("NsxtHosts"), NsxtHostsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VcentersDefinition = VcentersDefinition


@dataclass
class NsxtClustersDefinition(BaseModel):
    ClusterIds: Optional[Sequence[str]]
    Include: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NsxtClustersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NsxtClustersDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterIds=json_data.get("ClusterIds"),
            Include=json_data.get("Include"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NsxtClustersDefinition = NsxtClustersDefinition


@dataclass
class NsxtDatastoresDefinition(BaseModel):
    DsIds: Optional[Sequence[str]]
    Include: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NsxtDatastoresDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NsxtDatastoresDefinition"]:
        if not json_data:
            return None
        return cls(
            DsIds=json_data.get("DsIds"),
            Include=json_data.get("Include"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NsxtDatastoresDefinition = NsxtDatastoresDefinition


@dataclass
class NsxtHostsDefinition(BaseModel):
    HostIds: Optional[Sequence[str]]
    Include: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NsxtHostsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NsxtHostsDefinition"]:
        if not json_data:
            return None
        return cls(
            HostIds=json_data.get("HostIds"),
            Include=json_data.get("Include"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NsxtHostsDefinition = NsxtHostsDefinition


@dataclass
class VipAsgDefinition(BaseModel):
    Configuration: Optional[Sequence["_ConfigurationDefinition"]]
    Policy: Optional[Sequence["_PolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VipAsgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VipAsgDefinition"]:
        if not json_data:
            return None
        return cls(
            Configuration=deserialize_list(json_data.get("Configuration"), ConfigurationDefinition),
            Policy=deserialize_list(json_data.get("Policy"), PolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VipAsgDefinition = VipAsgDefinition


@dataclass
class ConfigurationDefinition(BaseModel):
    Zones: Optional[Sequence["_ZonesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Zones=deserialize_list(json_data.get("Zones"), ZonesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationDefinition = ConfigurationDefinition


@dataclass
class ZonesDefinition(BaseModel):
    SubnetUuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZonesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZonesDefinition"]:
        if not json_data:
            return None
        return cls(
            SubnetUuid=json_data.get("SubnetUuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZonesDefinition = ZonesDefinition


@dataclass
class PolicyDefinition(BaseModel):
    DnsCooldown: Optional[float]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Suspend: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsCooldown=json_data.get("DnsCooldown"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Suspend=json_data.get("Suspend"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyDefinition = PolicyDefinition


@dataclass
class VssPlacementDefinition(BaseModel):
    CoreNonaffinity: Optional[float]
    NumSubcores: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VssPlacementDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VssPlacementDefinition"]:
        if not json_data:
            return None
        return cls(
            CoreNonaffinity=json_data.get("CoreNonaffinity"),
            NumSubcores=json_data.get("NumSubcores"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VssPlacementDefinition = VssPlacementDefinition


