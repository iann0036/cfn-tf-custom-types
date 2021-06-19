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
    AccessProfile: Optional[str]
    DelayedRestartTrigger: Optional[float]
    Description: Optional[str]
    DirectlyConnected: Optional[float]
    DynamicCapability: Optional[float]
    DynamicSortSubtable: Optional[str]
    DynamicallyDiscovered: Optional[float]
    FirmwareProvision: Optional[str]
    FirmwareProvisionVersion: Optional[str]
    FlowIdentity: Optional[str]
    FswWan1Admin: Optional[str]
    FswWan1Peer: Optional[str]
    FswWan2Admin: Optional[str]
    FswWan2Peer: Optional[str]
    Id: Optional[str]
    L3Discovered: Optional[float]
    MaxAllowedTrunkMembers: Optional[float]
    MclagIgmpSnoopingAware: Optional[str]
    Name: Optional[str]
    OverrideSnmpCommunity: Optional[str]
    OverrideSnmpSysinfo: Optional[str]
    OverrideSnmpTrapThreshold: Optional[str]
    OverrideSnmpUser: Optional[str]
    OwnerVdom: Optional[str]
    PoeDetectionType: Optional[float]
    PoeLldpDetection: Optional[str]
    PoePreStandardDetection: Optional[str]
    PreProvisioned: Optional[float]
    QosDropPolicy: Optional[str]
    QosRedProbability: Optional[float]
    StagedImageVersion: Optional[str]
    SwitchDeviceTag: Optional[str]
    SwitchDhcpOpt43Key: Optional[str]
    SwitchId: Optional[str]
    SwitchProfile: Optional[str]
    TdrSupported: Optional[str]
    Type: Optional[str]
    Vdomparam: Optional[str]
    Version: Optional[float]
    CustomCommand: Optional[Sequence["_CustomCommandDefinition"]]
    IgmpSnooping: Optional[Sequence["_IgmpSnoopingDefinition"]]
    IpSourceGuard: Optional[Sequence["_IpSourceGuardDefinition"]]
    Mirror: Optional[Sequence["_MirrorDefinition"]]
    N8021xSettings: Optional[Sequence["_N8021xSettingsDefinition"]]
    Ports: Optional[Sequence["_PortsDefinition"]]
    RemoteLog: Optional[Sequence["_RemoteLogDefinition"]]
    SnmpCommunity: Optional[Sequence["_SnmpCommunityDefinition"]]
    SnmpSysinfo: Optional[Sequence["_SnmpSysinfoDefinition"]]
    SnmpTrapThreshold: Optional[Sequence["_SnmpTrapThresholdDefinition"]]
    SnmpUser: Optional[Sequence["_SnmpUserDefinition"]]
    StaticMac: Optional[Sequence["_StaticMacDefinition"]]
    StormControl: Optional[Sequence["_StormControlDefinition"]]
    StpInstance: Optional[Sequence["_StpInstanceDefinition"]]
    StpSettings: Optional[Sequence["_StpSettingsDefinition"]]
    SwitchLog: Optional[Sequence["_SwitchLogDefinition"]]
    SwitchStpSettings: Optional[Sequence["_SwitchStpSettingsDefinition"]]

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
            AccessProfile=json_data.get("AccessProfile"),
            DelayedRestartTrigger=json_data.get("DelayedRestartTrigger"),
            Description=json_data.get("Description"),
            DirectlyConnected=json_data.get("DirectlyConnected"),
            DynamicCapability=json_data.get("DynamicCapability"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            DynamicallyDiscovered=json_data.get("DynamicallyDiscovered"),
            FirmwareProvision=json_data.get("FirmwareProvision"),
            FirmwareProvisionVersion=json_data.get("FirmwareProvisionVersion"),
            FlowIdentity=json_data.get("FlowIdentity"),
            FswWan1Admin=json_data.get("FswWan1Admin"),
            FswWan1Peer=json_data.get("FswWan1Peer"),
            FswWan2Admin=json_data.get("FswWan2Admin"),
            FswWan2Peer=json_data.get("FswWan2Peer"),
            Id=json_data.get("Id"),
            L3Discovered=json_data.get("L3Discovered"),
            MaxAllowedTrunkMembers=json_data.get("MaxAllowedTrunkMembers"),
            MclagIgmpSnoopingAware=json_data.get("MclagIgmpSnoopingAware"),
            Name=json_data.get("Name"),
            OverrideSnmpCommunity=json_data.get("OverrideSnmpCommunity"),
            OverrideSnmpSysinfo=json_data.get("OverrideSnmpSysinfo"),
            OverrideSnmpTrapThreshold=json_data.get("OverrideSnmpTrapThreshold"),
            OverrideSnmpUser=json_data.get("OverrideSnmpUser"),
            OwnerVdom=json_data.get("OwnerVdom"),
            PoeDetectionType=json_data.get("PoeDetectionType"),
            PoeLldpDetection=json_data.get("PoeLldpDetection"),
            PoePreStandardDetection=json_data.get("PoePreStandardDetection"),
            PreProvisioned=json_data.get("PreProvisioned"),
            QosDropPolicy=json_data.get("QosDropPolicy"),
            QosRedProbability=json_data.get("QosRedProbability"),
            StagedImageVersion=json_data.get("StagedImageVersion"),
            SwitchDeviceTag=json_data.get("SwitchDeviceTag"),
            SwitchDhcpOpt43Key=json_data.get("SwitchDhcpOpt43Key"),
            SwitchId=json_data.get("SwitchId"),
            SwitchProfile=json_data.get("SwitchProfile"),
            TdrSupported=json_data.get("TdrSupported"),
            Type=json_data.get("Type"),
            Vdomparam=json_data.get("Vdomparam"),
            Version=json_data.get("Version"),
            CustomCommand=deserialize_list(json_data.get("CustomCommand"), CustomCommandDefinition),
            IgmpSnooping=deserialize_list(json_data.get("IgmpSnooping"), IgmpSnoopingDefinition),
            IpSourceGuard=deserialize_list(json_data.get("IpSourceGuard"), IpSourceGuardDefinition),
            Mirror=deserialize_list(json_data.get("Mirror"), MirrorDefinition),
            N8021xSettings=deserialize_list(json_data.get("N8021xSettings"), N8021xSettingsDefinition),
            Ports=deserialize_list(json_data.get("Ports"), PortsDefinition),
            RemoteLog=deserialize_list(json_data.get("RemoteLog"), RemoteLogDefinition),
            SnmpCommunity=deserialize_list(json_data.get("SnmpCommunity"), SnmpCommunityDefinition),
            SnmpSysinfo=deserialize_list(json_data.get("SnmpSysinfo"), SnmpSysinfoDefinition),
            SnmpTrapThreshold=deserialize_list(json_data.get("SnmpTrapThreshold"), SnmpTrapThresholdDefinition),
            SnmpUser=deserialize_list(json_data.get("SnmpUser"), SnmpUserDefinition),
            StaticMac=deserialize_list(json_data.get("StaticMac"), StaticMacDefinition),
            StormControl=deserialize_list(json_data.get("StormControl"), StormControlDefinition),
            StpInstance=deserialize_list(json_data.get("StpInstance"), StpInstanceDefinition),
            StpSettings=deserialize_list(json_data.get("StpSettings"), StpSettingsDefinition),
            SwitchLog=deserialize_list(json_data.get("SwitchLog"), SwitchLogDefinition),
            SwitchStpSettings=deserialize_list(json_data.get("SwitchStpSettings"), SwitchStpSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomCommandDefinition(BaseModel):
    CommandEntry: Optional[str]
    CommandName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomCommandDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomCommandDefinition"]:
        if not json_data:
            return None
        return cls(
            CommandEntry=json_data.get("CommandEntry"),
            CommandName=json_data.get("CommandName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomCommandDefinition = CustomCommandDefinition


@dataclass
class IgmpSnoopingDefinition(BaseModel):
    AgingTime: Optional[float]
    FloodUnknownMulticast: Optional[str]
    LocalOverride: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IgmpSnoopingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IgmpSnoopingDefinition"]:
        if not json_data:
            return None
        return cls(
            AgingTime=json_data.get("AgingTime"),
            FloodUnknownMulticast=json_data.get("FloodUnknownMulticast"),
            LocalOverride=json_data.get("LocalOverride"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IgmpSnoopingDefinition = IgmpSnoopingDefinition


@dataclass
class IpSourceGuardDefinition(BaseModel):
    Description: Optional[str]
    Port: Optional[str]
    BindingEntry: Optional[Sequence["_BindingEntryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpSourceGuardDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpSourceGuardDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Port=json_data.get("Port"),
            BindingEntry=deserialize_list(json_data.get("BindingEntry"), BindingEntryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpSourceGuardDefinition = IpSourceGuardDefinition


@dataclass
class BindingEntryDefinition(BaseModel):
    EntryName: Optional[str]
    Ip: Optional[str]
    Mac: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BindingEntryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BindingEntryDefinition"]:
        if not json_data:
            return None
        return cls(
            EntryName=json_data.get("EntryName"),
            Ip=json_data.get("Ip"),
            Mac=json_data.get("Mac"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BindingEntryDefinition = BindingEntryDefinition


@dataclass
class MirrorDefinition(BaseModel):
    Dst: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    SwitchingPacket: Optional[str]
    SrcEgress: Optional[Sequence["_SrcEgressDefinition"]]
    SrcIngress: Optional[Sequence["_SrcIngressDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MirrorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MirrorDefinition"]:
        if not json_data:
            return None
        return cls(
            Dst=json_data.get("Dst"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            SwitchingPacket=json_data.get("SwitchingPacket"),
            SrcEgress=deserialize_list(json_data.get("SrcEgress"), SrcEgressDefinition),
            SrcIngress=deserialize_list(json_data.get("SrcIngress"), SrcIngressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MirrorDefinition = MirrorDefinition


@dataclass
class SrcEgressDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcEgressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcEgressDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcEgressDefinition = SrcEgressDefinition


@dataclass
class SrcIngressDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcIngressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcIngressDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcIngressDefinition = SrcIngressDefinition


@dataclass
class N8021xSettingsDefinition(BaseModel):
    LinkDownAuth: Optional[str]
    LocalOverride: Optional[str]
    MaxReauthAttempt: Optional[float]
    ReauthPeriod: Optional[float]
    TxPeriod: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_N8021xSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_N8021xSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            LinkDownAuth=json_data.get("LinkDownAuth"),
            LocalOverride=json_data.get("LocalOverride"),
            MaxReauthAttempt=json_data.get("MaxReauthAttempt"),
            ReauthPeriod=json_data.get("ReauthPeriod"),
            TxPeriod=json_data.get("TxPeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_N8021xSettingsDefinition = N8021xSettingsDefinition


@dataclass
class PortsDefinition(BaseModel):
    AccessMode: Optional[str]
    AggregatorMode: Optional[str]
    AllowedVlansAll: Optional[str]
    ArpInspectionTrust: Optional[str]
    Bundle: Optional[str]
    Description: Optional[str]
    DhcpSnoopOption82Trust: Optional[str]
    DhcpSnooping: Optional[str]
    DiscardMode: Optional[str]
    EdgePort: Optional[str]
    ExportTo: Optional[str]
    ExportToPool: Optional[str]
    ExportToPoolFlag: Optional[float]
    FecCapable: Optional[float]
    FecState: Optional[str]
    FgtPeerDeviceName: Optional[str]
    FgtPeerPortName: Optional[str]
    FiberPort: Optional[float]
    Flags: Optional[float]
    FlowControl: Optional[str]
    FortilinkPort: Optional[float]
    IgmpSnooping: Optional[str]
    IgmpsFloodReports: Optional[str]
    IgmpsFloodTraffic: Optional[str]
    IpSourceGuard: Optional[str]
    IslLocalTrunkName: Optional[str]
    IslPeerDeviceName: Optional[str]
    IslPeerPortName: Optional[str]
    LacpSpeed: Optional[str]
    LearningLimit: Optional[float]
    LldpProfile: Optional[str]
    LldpStatus: Optional[str]
    LoopGuard: Optional[str]
    LoopGuardTimeout: Optional[float]
    MacAddr: Optional[str]
    MaxBundle: Optional[float]
    Mclag: Optional[str]
    MclagIclPort: Optional[float]
    MediaType: Optional[str]
    MemberWithdrawalBehavior: Optional[str]
    MinBundle: Optional[float]
    Mode: Optional[str]
    P2pPort: Optional[float]
    PacketSampleRate: Optional[float]
    PacketSampler: Optional[str]
    PauseMeter: Optional[float]
    PauseMeterResume: Optional[str]
    PoeCapable: Optional[float]
    PoePreStandardDetection: Optional[str]
    PoeStatus: Optional[str]
    PortName: Optional[str]
    PortNumber: Optional[float]
    PortOwner: Optional[str]
    PortPrefixType: Optional[float]
    PortSecurityPolicy: Optional[str]
    PortSelectionCriteria: Optional[str]
    PtpPolicy: Optional[str]
    QosPolicy: Optional[str]
    RpvstPort: Optional[str]
    SampleDirection: Optional[str]
    SflowCounterInterval: Optional[float]
    SflowSampleRate: Optional[float]
    SflowSampler: Optional[str]
    Speed: Optional[str]
    SpeedMask: Optional[float]
    StackingPort: Optional[float]
    Status: Optional[str]
    StickyMac: Optional[str]
    StormControlPolicy: Optional[str]
    StpBpduGuard: Optional[str]
    StpBpduGuardTimeout: Optional[float]
    StpRootGuard: Optional[str]
    StpState: Optional[str]
    SwitchId: Optional[str]
    Type: Optional[str]
    VirtualPort: Optional[float]
    Vlan: Optional[str]
    AllowedVlans: Optional[Sequence["_AllowedVlansDefinition"]]
    ExportTags: Optional[Sequence["_ExportTagsDefinition"]]
    Members: Optional[Sequence["_MembersDefinition"]]
    UntaggedVlans: Optional[Sequence["_UntaggedVlansDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortsDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessMode=json_data.get("AccessMode"),
            AggregatorMode=json_data.get("AggregatorMode"),
            AllowedVlansAll=json_data.get("AllowedVlansAll"),
            ArpInspectionTrust=json_data.get("ArpInspectionTrust"),
            Bundle=json_data.get("Bundle"),
            Description=json_data.get("Description"),
            DhcpSnoopOption82Trust=json_data.get("DhcpSnoopOption82Trust"),
            DhcpSnooping=json_data.get("DhcpSnooping"),
            DiscardMode=json_data.get("DiscardMode"),
            EdgePort=json_data.get("EdgePort"),
            ExportTo=json_data.get("ExportTo"),
            ExportToPool=json_data.get("ExportToPool"),
            ExportToPoolFlag=json_data.get("ExportToPoolFlag"),
            FecCapable=json_data.get("FecCapable"),
            FecState=json_data.get("FecState"),
            FgtPeerDeviceName=json_data.get("FgtPeerDeviceName"),
            FgtPeerPortName=json_data.get("FgtPeerPortName"),
            FiberPort=json_data.get("FiberPort"),
            Flags=json_data.get("Flags"),
            FlowControl=json_data.get("FlowControl"),
            FortilinkPort=json_data.get("FortilinkPort"),
            IgmpSnooping=json_data.get("IgmpSnooping"),
            IgmpsFloodReports=json_data.get("IgmpsFloodReports"),
            IgmpsFloodTraffic=json_data.get("IgmpsFloodTraffic"),
            IpSourceGuard=json_data.get("IpSourceGuard"),
            IslLocalTrunkName=json_data.get("IslLocalTrunkName"),
            IslPeerDeviceName=json_data.get("IslPeerDeviceName"),
            IslPeerPortName=json_data.get("IslPeerPortName"),
            LacpSpeed=json_data.get("LacpSpeed"),
            LearningLimit=json_data.get("LearningLimit"),
            LldpProfile=json_data.get("LldpProfile"),
            LldpStatus=json_data.get("LldpStatus"),
            LoopGuard=json_data.get("LoopGuard"),
            LoopGuardTimeout=json_data.get("LoopGuardTimeout"),
            MacAddr=json_data.get("MacAddr"),
            MaxBundle=json_data.get("MaxBundle"),
            Mclag=json_data.get("Mclag"),
            MclagIclPort=json_data.get("MclagIclPort"),
            MediaType=json_data.get("MediaType"),
            MemberWithdrawalBehavior=json_data.get("MemberWithdrawalBehavior"),
            MinBundle=json_data.get("MinBundle"),
            Mode=json_data.get("Mode"),
            P2pPort=json_data.get("P2pPort"),
            PacketSampleRate=json_data.get("PacketSampleRate"),
            PacketSampler=json_data.get("PacketSampler"),
            PauseMeter=json_data.get("PauseMeter"),
            PauseMeterResume=json_data.get("PauseMeterResume"),
            PoeCapable=json_data.get("PoeCapable"),
            PoePreStandardDetection=json_data.get("PoePreStandardDetection"),
            PoeStatus=json_data.get("PoeStatus"),
            PortName=json_data.get("PortName"),
            PortNumber=json_data.get("PortNumber"),
            PortOwner=json_data.get("PortOwner"),
            PortPrefixType=json_data.get("PortPrefixType"),
            PortSecurityPolicy=json_data.get("PortSecurityPolicy"),
            PortSelectionCriteria=json_data.get("PortSelectionCriteria"),
            PtpPolicy=json_data.get("PtpPolicy"),
            QosPolicy=json_data.get("QosPolicy"),
            RpvstPort=json_data.get("RpvstPort"),
            SampleDirection=json_data.get("SampleDirection"),
            SflowCounterInterval=json_data.get("SflowCounterInterval"),
            SflowSampleRate=json_data.get("SflowSampleRate"),
            SflowSampler=json_data.get("SflowSampler"),
            Speed=json_data.get("Speed"),
            SpeedMask=json_data.get("SpeedMask"),
            StackingPort=json_data.get("StackingPort"),
            Status=json_data.get("Status"),
            StickyMac=json_data.get("StickyMac"),
            StormControlPolicy=json_data.get("StormControlPolicy"),
            StpBpduGuard=json_data.get("StpBpduGuard"),
            StpBpduGuardTimeout=json_data.get("StpBpduGuardTimeout"),
            StpRootGuard=json_data.get("StpRootGuard"),
            StpState=json_data.get("StpState"),
            SwitchId=json_data.get("SwitchId"),
            Type=json_data.get("Type"),
            VirtualPort=json_data.get("VirtualPort"),
            Vlan=json_data.get("Vlan"),
            AllowedVlans=deserialize_list(json_data.get("AllowedVlans"), AllowedVlansDefinition),
            ExportTags=deserialize_list(json_data.get("ExportTags"), ExportTagsDefinition),
            Members=deserialize_list(json_data.get("Members"), MembersDefinition),
            UntaggedVlans=deserialize_list(json_data.get("UntaggedVlans"), UntaggedVlansDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortsDefinition = PortsDefinition


@dataclass
class AllowedVlansDefinition(BaseModel):
    VlanName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedVlansDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedVlansDefinition"]:
        if not json_data:
            return None
        return cls(
            VlanName=json_data.get("VlanName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedVlansDefinition = AllowedVlansDefinition


@dataclass
class ExportTagsDefinition(BaseModel):
    TagName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExportTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExportTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            TagName=json_data.get("TagName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExportTagsDefinition = ExportTagsDefinition


@dataclass
class MembersDefinition(BaseModel):
    MemberName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MembersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MembersDefinition"]:
        if not json_data:
            return None
        return cls(
            MemberName=json_data.get("MemberName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MembersDefinition = MembersDefinition


@dataclass
class UntaggedVlansDefinition(BaseModel):
    VlanName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UntaggedVlansDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UntaggedVlansDefinition"]:
        if not json_data:
            return None
        return cls(
            VlanName=json_data.get("VlanName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UntaggedVlansDefinition = UntaggedVlansDefinition


@dataclass
class RemoteLogDefinition(BaseModel):
    Csv: Optional[str]
    Facility: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    Server: Optional[str]
    Severity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RemoteLogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoteLogDefinition"]:
        if not json_data:
            return None
        return cls(
            Csv=json_data.get("Csv"),
            Facility=json_data.get("Facility"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Server=json_data.get("Server"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoteLogDefinition = RemoteLogDefinition


@dataclass
class SnmpCommunityDefinition(BaseModel):
    Events: Optional[str]
    Id: Optional[float]
    Name: Optional[str]
    QueryV1Port: Optional[float]
    QueryV1Status: Optional[str]
    QueryV2cPort: Optional[float]
    QueryV2cStatus: Optional[str]
    Status: Optional[str]
    TrapV1Lport: Optional[float]
    TrapV1Rport: Optional[float]
    TrapV1Status: Optional[str]
    TrapV2cLport: Optional[float]
    TrapV2cRport: Optional[float]
    TrapV2cStatus: Optional[str]
    Hosts: Optional[Sequence["_HostsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SnmpCommunityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnmpCommunityDefinition"]:
        if not json_data:
            return None
        return cls(
            Events=json_data.get("Events"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            QueryV1Port=json_data.get("QueryV1Port"),
            QueryV1Status=json_data.get("QueryV1Status"),
            QueryV2cPort=json_data.get("QueryV2cPort"),
            QueryV2cStatus=json_data.get("QueryV2cStatus"),
            Status=json_data.get("Status"),
            TrapV1Lport=json_data.get("TrapV1Lport"),
            TrapV1Rport=json_data.get("TrapV1Rport"),
            TrapV1Status=json_data.get("TrapV1Status"),
            TrapV2cLport=json_data.get("TrapV2cLport"),
            TrapV2cRport=json_data.get("TrapV2cRport"),
            TrapV2cStatus=json_data.get("TrapV2cStatus"),
            Hosts=deserialize_list(json_data.get("Hosts"), HostsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnmpCommunityDefinition = SnmpCommunityDefinition


@dataclass
class HostsDefinition(BaseModel):
    Id: Optional[float]
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostsDefinition = HostsDefinition


@dataclass
class SnmpSysinfoDefinition(BaseModel):
    ContactInfo: Optional[str]
    Description: Optional[str]
    EngineId: Optional[str]
    Location: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnmpSysinfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnmpSysinfoDefinition"]:
        if not json_data:
            return None
        return cls(
            ContactInfo=json_data.get("ContactInfo"),
            Description=json_data.get("Description"),
            EngineId=json_data.get("EngineId"),
            Location=json_data.get("Location"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnmpSysinfoDefinition = SnmpSysinfoDefinition


@dataclass
class SnmpTrapThresholdDefinition(BaseModel):
    TrapHighCpuThreshold: Optional[float]
    TrapLogFullThreshold: Optional[float]
    TrapLowMemoryThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SnmpTrapThresholdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnmpTrapThresholdDefinition"]:
        if not json_data:
            return None
        return cls(
            TrapHighCpuThreshold=json_data.get("TrapHighCpuThreshold"),
            TrapLogFullThreshold=json_data.get("TrapLogFullThreshold"),
            TrapLowMemoryThreshold=json_data.get("TrapLowMemoryThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnmpTrapThresholdDefinition = SnmpTrapThresholdDefinition


@dataclass
class SnmpUserDefinition(BaseModel):
    AuthProto: Optional[str]
    AuthPwd: Optional[str]
    Name: Optional[str]
    PrivProto: Optional[str]
    PrivPwd: Optional[str]
    Queries: Optional[str]
    QueryPort: Optional[float]
    SecurityLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnmpUserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnmpUserDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthProto=json_data.get("AuthProto"),
            AuthPwd=json_data.get("AuthPwd"),
            Name=json_data.get("Name"),
            PrivProto=json_data.get("PrivProto"),
            PrivPwd=json_data.get("PrivPwd"),
            Queries=json_data.get("Queries"),
            QueryPort=json_data.get("QueryPort"),
            SecurityLevel=json_data.get("SecurityLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnmpUserDefinition = SnmpUserDefinition


@dataclass
class StaticMacDefinition(BaseModel):
    Description: Optional[str]
    Id: Optional[float]
    Interface: Optional[str]
    Mac: Optional[str]
    Type: Optional[str]
    Vlan: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StaticMacDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticMacDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            Mac=json_data.get("Mac"),
            Type=json_data.get("Type"),
            Vlan=json_data.get("Vlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticMacDefinition = StaticMacDefinition


@dataclass
class StormControlDefinition(BaseModel):
    Broadcast: Optional[str]
    LocalOverride: Optional[str]
    Rate: Optional[float]
    UnknownMulticast: Optional[str]
    UnknownUnicast: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StormControlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StormControlDefinition"]:
        if not json_data:
            return None
        return cls(
            Broadcast=json_data.get("Broadcast"),
            LocalOverride=json_data.get("LocalOverride"),
            Rate=json_data.get("Rate"),
            UnknownMulticast=json_data.get("UnknownMulticast"),
            UnknownUnicast=json_data.get("UnknownUnicast"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StormControlDefinition = StormControlDefinition


@dataclass
class StpInstanceDefinition(BaseModel):
    Id: Optional[str]
    Priority: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StpInstanceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StpInstanceDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StpInstanceDefinition = StpInstanceDefinition


@dataclass
class StpSettingsDefinition(BaseModel):
    ForwardTime: Optional[float]
    HelloTime: Optional[float]
    LocalOverride: Optional[str]
    MaxAge: Optional[float]
    MaxHops: Optional[float]
    Name: Optional[str]
    PendingTimer: Optional[float]
    Revision: Optional[float]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StpSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StpSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            ForwardTime=json_data.get("ForwardTime"),
            HelloTime=json_data.get("HelloTime"),
            LocalOverride=json_data.get("LocalOverride"),
            MaxAge=json_data.get("MaxAge"),
            MaxHops=json_data.get("MaxHops"),
            Name=json_data.get("Name"),
            PendingTimer=json_data.get("PendingTimer"),
            Revision=json_data.get("Revision"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StpSettingsDefinition = StpSettingsDefinition


@dataclass
class SwitchLogDefinition(BaseModel):
    LocalOverride: Optional[str]
    Severity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SwitchLogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SwitchLogDefinition"]:
        if not json_data:
            return None
        return cls(
            LocalOverride=json_data.get("LocalOverride"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SwitchLogDefinition = SwitchLogDefinition


@dataclass
class SwitchStpSettingsDefinition(BaseModel):
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SwitchStpSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SwitchStpSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SwitchStpSettingsDefinition = SwitchStpSettingsDefinition


