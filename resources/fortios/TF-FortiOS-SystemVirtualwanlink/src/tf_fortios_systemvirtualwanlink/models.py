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
    DynamicSortSubtable: Optional[str]
    FailDetect: Optional[str]
    Id: Optional[str]
    LoadBalanceMode: Optional[str]
    NeighborHoldBootTime: Optional[float]
    NeighborHoldDown: Optional[str]
    NeighborHoldDownTime: Optional[float]
    Status: Optional[str]
    Vdomparam: Optional[str]
    FailAlertInterfaces: Optional[Sequence["_FailAlertInterfacesDefinition"]]
    HealthCheck: Optional[Sequence["_HealthCheckDefinition"]]
    Members: Optional[Sequence["_MembersDefinition"]]
    Neighbor: Optional[Sequence["_NeighborDefinition"]]
    Service: Optional[Sequence["_ServiceDefinition"]]
    Zone: Optional[Sequence["_ZoneDefinition"]]

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
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            FailDetect=json_data.get("FailDetect"),
            Id=json_data.get("Id"),
            LoadBalanceMode=json_data.get("LoadBalanceMode"),
            NeighborHoldBootTime=json_data.get("NeighborHoldBootTime"),
            NeighborHoldDown=json_data.get("NeighborHoldDown"),
            NeighborHoldDownTime=json_data.get("NeighborHoldDownTime"),
            Status=json_data.get("Status"),
            Vdomparam=json_data.get("Vdomparam"),
            FailAlertInterfaces=deserialize_list(json_data.get("FailAlertInterfaces"), FailAlertInterfacesDefinition),
            HealthCheck=deserialize_list(json_data.get("HealthCheck"), HealthCheckDefinition),
            Members=deserialize_list(json_data.get("Members"), MembersDefinition),
            Neighbor=deserialize_list(json_data.get("Neighbor"), NeighborDefinition),
            Service=deserialize_list(json_data.get("Service"), ServiceDefinition),
            Zone=deserialize_list(json_data.get("Zone"), ZoneDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FailAlertInterfacesDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FailAlertInterfacesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailAlertInterfacesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailAlertInterfacesDefinition = FailAlertInterfacesDefinition


@dataclass
class HealthCheckDefinition(BaseModel):
    AddrMode: Optional[str]
    Diffservcode: Optional[str]
    DnsRequestDomain: Optional[str]
    Failtime: Optional[float]
    HaPriority: Optional[float]
    HttpAgent: Optional[str]
    HttpGet: Optional[str]
    HttpMatch: Optional[str]
    Interval: Optional[float]
    Name: Optional[str]
    PacketSize: Optional[float]
    Password: Optional[str]
    Port: Optional[float]
    ProbeCount: Optional[float]
    ProbePackets: Optional[str]
    ProbeTimeout: Optional[float]
    Protocol: Optional[str]
    Recoverytime: Optional[float]
    SecurityMode: Optional[str]
    Server: Optional[str]
    SlaFailLogPeriod: Optional[float]
    SlaPassLogPeriod: Optional[float]
    SystemDns: Optional[str]
    ThresholdAlertJitter: Optional[float]
    ThresholdAlertLatency: Optional[float]
    ThresholdAlertPacketloss: Optional[float]
    ThresholdWarningJitter: Optional[float]
    ThresholdWarningLatency: Optional[float]
    ThresholdWarningPacketloss: Optional[float]
    UpdateCascadeInterface: Optional[str]
    UpdateStaticRoute: Optional[str]
    Members: Optional[Sequence["_MembersDefinition"]]
    Sla: Optional[Sequence["_SlaDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            AddrMode=json_data.get("AddrMode"),
            Diffservcode=json_data.get("Diffservcode"),
            DnsRequestDomain=json_data.get("DnsRequestDomain"),
            Failtime=json_data.get("Failtime"),
            HaPriority=json_data.get("HaPriority"),
            HttpAgent=json_data.get("HttpAgent"),
            HttpGet=json_data.get("HttpGet"),
            HttpMatch=json_data.get("HttpMatch"),
            Interval=json_data.get("Interval"),
            Name=json_data.get("Name"),
            PacketSize=json_data.get("PacketSize"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            ProbeCount=json_data.get("ProbeCount"),
            ProbePackets=json_data.get("ProbePackets"),
            ProbeTimeout=json_data.get("ProbeTimeout"),
            Protocol=json_data.get("Protocol"),
            Recoverytime=json_data.get("Recoverytime"),
            SecurityMode=json_data.get("SecurityMode"),
            Server=json_data.get("Server"),
            SlaFailLogPeriod=json_data.get("SlaFailLogPeriod"),
            SlaPassLogPeriod=json_data.get("SlaPassLogPeriod"),
            SystemDns=json_data.get("SystemDns"),
            ThresholdAlertJitter=json_data.get("ThresholdAlertJitter"),
            ThresholdAlertLatency=json_data.get("ThresholdAlertLatency"),
            ThresholdAlertPacketloss=json_data.get("ThresholdAlertPacketloss"),
            ThresholdWarningJitter=json_data.get("ThresholdWarningJitter"),
            ThresholdWarningLatency=json_data.get("ThresholdWarningLatency"),
            ThresholdWarningPacketloss=json_data.get("ThresholdWarningPacketloss"),
            UpdateCascadeInterface=json_data.get("UpdateCascadeInterface"),
            UpdateStaticRoute=json_data.get("UpdateStaticRoute"),
            Members=deserialize_list(json_data.get("Members"), MembersDefinition),
            Sla=deserialize_list(json_data.get("Sla"), SlaDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckDefinition = HealthCheckDefinition


@dataclass
class MembersDefinition(BaseModel):
    SeqNum: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MembersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MembersDefinition"]:
        if not json_data:
            return None
        return cls(
            SeqNum=json_data.get("SeqNum"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MembersDefinition = MembersDefinition


@dataclass
class SlaDefinition(BaseModel):
    HealthCheck: Optional[str]
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SlaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlaDefinition"]:
        if not json_data:
            return None
        return cls(
            HealthCheck=json_data.get("HealthCheck"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlaDefinition = SlaDefinition


@dataclass
class NeighborDefinition(BaseModel):
    HealthCheck: Optional[str]
    Ip: Optional[str]
    Member: Optional[float]
    Role: Optional[str]
    SlaId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NeighborDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NeighborDefinition"]:
        if not json_data:
            return None
        return cls(
            HealthCheck=json_data.get("HealthCheck"),
            Ip=json_data.get("Ip"),
            Member=json_data.get("Member"),
            Role=json_data.get("Role"),
            SlaId=json_data.get("SlaId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NeighborDefinition = NeighborDefinition


@dataclass
class ServiceDefinition(BaseModel):
    AddrMode: Optional[str]
    BandwidthWeight: Optional[float]
    Default: Optional[str]
    DscpForward: Optional[str]
    DscpForwardTag: Optional[str]
    DscpReverse: Optional[str]
    DscpReverseTag: Optional[str]
    DstNegate: Optional[str]
    EndPort: Optional[float]
    Gateway: Optional[str]
    HealthCheck: Optional[str]
    HoldDownTime: Optional[float]
    Id: Optional[float]
    InputDeviceNegate: Optional[str]
    InternetService: Optional[str]
    JitterWeight: Optional[float]
    LatencyWeight: Optional[float]
    LinkCostFactor: Optional[str]
    LinkCostThreshold: Optional[float]
    Member: Optional[float]
    Mode: Optional[str]
    Name: Optional[str]
    PacketLossWeight: Optional[float]
    Protocol: Optional[float]
    QualityLink: Optional[float]
    Role: Optional[str]
    RouteTag: Optional[float]
    SlaCompareMethod: Optional[str]
    SrcNegate: Optional[str]
    StandaloneAction: Optional[str]
    StartPort: Optional[float]
    Status: Optional[str]
    Tos: Optional[str]
    TosMask: Optional[str]
    Dst: Optional[Sequence["_DstDefinition"]]
    Dst6: Optional[Sequence["_Dst6Definition"]]
    Groups: Optional[Sequence["_GroupsDefinition"]]
    InputDevice: Optional[Sequence["_InputDeviceDefinition"]]
    InternetServiceAppCtrl: Optional[Sequence["_InternetServiceAppCtrlDefinition"]]
    InternetServiceAppCtrlGroup: Optional[Sequence["_InternetServiceAppCtrlGroupDefinition"]]
    InternetServiceCtrl: Optional[Sequence["_InternetServiceCtrlDefinition"]]
    InternetServiceCtrlGroup: Optional[Sequence["_InternetServiceCtrlGroupDefinition"]]
    InternetServiceCustom: Optional[Sequence["_InternetServiceCustomDefinition"]]
    InternetServiceCustomGroup: Optional[Sequence["_InternetServiceCustomGroupDefinition"]]
    InternetServiceGroup: Optional[Sequence["_InternetServiceGroupDefinition"]]
    InternetServiceId: Optional[Sequence["_InternetServiceIdDefinition"]]
    InternetServiceName: Optional[Sequence["_InternetServiceNameDefinition"]]
    PriorityMembers: Optional[Sequence["_PriorityMembersDefinition"]]
    Sla: Optional[Sequence["_SlaDefinition"]]
    Src: Optional[Sequence["_SrcDefinition"]]
    Src6: Optional[Sequence["_Src6Definition"]]
    Users: Optional[Sequence["_UsersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            AddrMode=json_data.get("AddrMode"),
            BandwidthWeight=json_data.get("BandwidthWeight"),
            Default=json_data.get("Default"),
            DscpForward=json_data.get("DscpForward"),
            DscpForwardTag=json_data.get("DscpForwardTag"),
            DscpReverse=json_data.get("DscpReverse"),
            DscpReverseTag=json_data.get("DscpReverseTag"),
            DstNegate=json_data.get("DstNegate"),
            EndPort=json_data.get("EndPort"),
            Gateway=json_data.get("Gateway"),
            HealthCheck=json_data.get("HealthCheck"),
            HoldDownTime=json_data.get("HoldDownTime"),
            Id=json_data.get("Id"),
            InputDeviceNegate=json_data.get("InputDeviceNegate"),
            InternetService=json_data.get("InternetService"),
            JitterWeight=json_data.get("JitterWeight"),
            LatencyWeight=json_data.get("LatencyWeight"),
            LinkCostFactor=json_data.get("LinkCostFactor"),
            LinkCostThreshold=json_data.get("LinkCostThreshold"),
            Member=json_data.get("Member"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            PacketLossWeight=json_data.get("PacketLossWeight"),
            Protocol=json_data.get("Protocol"),
            QualityLink=json_data.get("QualityLink"),
            Role=json_data.get("Role"),
            RouteTag=json_data.get("RouteTag"),
            SlaCompareMethod=json_data.get("SlaCompareMethod"),
            SrcNegate=json_data.get("SrcNegate"),
            StandaloneAction=json_data.get("StandaloneAction"),
            StartPort=json_data.get("StartPort"),
            Status=json_data.get("Status"),
            Tos=json_data.get("Tos"),
            TosMask=json_data.get("TosMask"),
            Dst=deserialize_list(json_data.get("Dst"), DstDefinition),
            Dst6=deserialize_list(json_data.get("Dst6"), Dst6Definition),
            Groups=deserialize_list(json_data.get("Groups"), GroupsDefinition),
            InputDevice=deserialize_list(json_data.get("InputDevice"), InputDeviceDefinition),
            InternetServiceAppCtrl=deserialize_list(json_data.get("InternetServiceAppCtrl"), InternetServiceAppCtrlDefinition),
            InternetServiceAppCtrlGroup=deserialize_list(json_data.get("InternetServiceAppCtrlGroup"), InternetServiceAppCtrlGroupDefinition),
            InternetServiceCtrl=deserialize_list(json_data.get("InternetServiceCtrl"), InternetServiceCtrlDefinition),
            InternetServiceCtrlGroup=deserialize_list(json_data.get("InternetServiceCtrlGroup"), InternetServiceCtrlGroupDefinition),
            InternetServiceCustom=deserialize_list(json_data.get("InternetServiceCustom"), InternetServiceCustomDefinition),
            InternetServiceCustomGroup=deserialize_list(json_data.get("InternetServiceCustomGroup"), InternetServiceCustomGroupDefinition),
            InternetServiceGroup=deserialize_list(json_data.get("InternetServiceGroup"), InternetServiceGroupDefinition),
            InternetServiceId=deserialize_list(json_data.get("InternetServiceId"), InternetServiceIdDefinition),
            InternetServiceName=deserialize_list(json_data.get("InternetServiceName"), InternetServiceNameDefinition),
            PriorityMembers=deserialize_list(json_data.get("PriorityMembers"), PriorityMembersDefinition),
            Sla=deserialize_list(json_data.get("Sla"), SlaDefinition),
            Src=deserialize_list(json_data.get("Src"), SrcDefinition),
            Src6=deserialize_list(json_data.get("Src6"), Src6Definition),
            Users=deserialize_list(json_data.get("Users"), UsersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceDefinition = ServiceDefinition


@dataclass
class DstDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstDefinition = DstDefinition


@dataclass
class Dst6Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dst6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dst6Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dst6Definition = Dst6Definition


@dataclass
class GroupsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupsDefinition = GroupsDefinition


@dataclass
class InputDeviceDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputDeviceDefinition = InputDeviceDefinition


@dataclass
class InternetServiceAppCtrlDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceAppCtrlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceAppCtrlDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceAppCtrlDefinition = InternetServiceAppCtrlDefinition


@dataclass
class InternetServiceAppCtrlGroupDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceAppCtrlGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceAppCtrlGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceAppCtrlGroupDefinition = InternetServiceAppCtrlGroupDefinition


@dataclass
class InternetServiceCtrlDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceCtrlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceCtrlDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceCtrlDefinition = InternetServiceCtrlDefinition


@dataclass
class InternetServiceCtrlGroupDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceCtrlGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceCtrlGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceCtrlGroupDefinition = InternetServiceCtrlGroupDefinition


@dataclass
class InternetServiceCustomDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceCustomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceCustomDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceCustomDefinition = InternetServiceCustomDefinition


@dataclass
class InternetServiceCustomGroupDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceCustomGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceCustomGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceCustomGroupDefinition = InternetServiceCustomGroupDefinition


@dataclass
class InternetServiceGroupDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceGroupDefinition = InternetServiceGroupDefinition


@dataclass
class InternetServiceIdDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceIdDefinition = InternetServiceIdDefinition


@dataclass
class InternetServiceNameDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceNameDefinition = InternetServiceNameDefinition


@dataclass
class PriorityMembersDefinition(BaseModel):
    SeqNum: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PriorityMembersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PriorityMembersDefinition"]:
        if not json_data:
            return None
        return cls(
            SeqNum=json_data.get("SeqNum"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PriorityMembersDefinition = PriorityMembersDefinition


@dataclass
class SrcDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcDefinition = SrcDefinition


@dataclass
class Src6Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Src6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Src6Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Src6Definition = Src6Definition


@dataclass
class UsersDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UsersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsersDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsersDefinition = UsersDefinition


@dataclass
class ZoneDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZoneDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZoneDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZoneDefinition = ZoneDefinition


