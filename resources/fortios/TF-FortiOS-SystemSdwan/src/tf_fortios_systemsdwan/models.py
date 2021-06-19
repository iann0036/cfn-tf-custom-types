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
    DuplicationMaxNum: Optional[float]
    DynamicSortSubtable: Optional[str]
    FailDetect: Optional[str]
    Id: Optional[str]
    LoadBalanceMode: Optional[str]
    NeighborHoldBootTime: Optional[float]
    NeighborHoldDown: Optional[str]
    NeighborHoldDownTime: Optional[float]
    Status: Optional[str]
    Vdomparam: Optional[str]
    Duplication: Optional[Sequence["_DuplicationDefinition"]]
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
            DuplicationMaxNum=json_data.get("DuplicationMaxNum"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            FailDetect=json_data.get("FailDetect"),
            Id=json_data.get("Id"),
            LoadBalanceMode=json_data.get("LoadBalanceMode"),
            NeighborHoldBootTime=json_data.get("NeighborHoldBootTime"),
            NeighborHoldDown=json_data.get("NeighborHoldDown"),
            NeighborHoldDownTime=json_data.get("NeighborHoldDownTime"),
            Status=json_data.get("Status"),
            Vdomparam=json_data.get("Vdomparam"),
            Duplication=deserialize_list(json_data.get("Duplication"), DuplicationDefinition),
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
class DuplicationDefinition(BaseModel):
    Id: Optional[float]
    PacketDeDuplication: Optional[str]
    PacketDuplication: Optional[str]
    Dstaddr: Optional[Sequence["_DstaddrDefinition"]]
    Dstaddr6: Optional[Sequence["_Dstaddr6Definition"]]
    Dstintf: Optional[Sequence["_DstintfDefinition"]]
    Service: Optional[Sequence["_ServiceDefinition"]]
    ServiceId: Optional[Sequence["_ServiceIdDefinition"]]
    Srcaddr: Optional[Sequence["_SrcaddrDefinition"]]
    Srcaddr6: Optional[Sequence["_Srcaddr6Definition"]]
    Srcintf: Optional[Sequence["_SrcintfDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DuplicationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DuplicationDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            PacketDeDuplication=json_data.get("PacketDeDuplication"),
            PacketDuplication=json_data.get("PacketDuplication"),
            Dstaddr=deserialize_list(json_data.get("Dstaddr"), DstaddrDefinition),
            Dstaddr6=deserialize_list(json_data.get("Dstaddr6"), Dstaddr6Definition),
            Dstintf=deserialize_list(json_data.get("Dstintf"), DstintfDefinition),
            Service=deserialize_list(json_data.get("Service"), ServiceDefinition),
            ServiceId=deserialize_list(json_data.get("ServiceId"), ServiceIdDefinition),
            Srcaddr=deserialize_list(json_data.get("Srcaddr"), SrcaddrDefinition),
            Srcaddr6=deserialize_list(json_data.get("Srcaddr6"), Srcaddr6Definition),
            Srcintf=deserialize_list(json_data.get("Srcintf"), SrcintfDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DuplicationDefinition = DuplicationDefinition


@dataclass
class DstaddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstaddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstaddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstaddrDefinition = DstaddrDefinition


@dataclass
class Dstaddr6Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dstaddr6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dstaddr6Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dstaddr6Definition = Dstaddr6Definition


@dataclass
class DstintfDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstintfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstintfDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstintfDefinition = DstintfDefinition


@dataclass
class ServiceDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceDefinition = ServiceDefinition


@dataclass
class ServiceIdDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceIdDefinition = ServiceIdDefinition


@dataclass
class SrcaddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcaddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcaddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcaddrDefinition = SrcaddrDefinition


@dataclass
class Srcaddr6Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Srcaddr6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Srcaddr6Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Srcaddr6Definition = Srcaddr6Definition


@dataclass
class SrcintfDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcintfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcintfDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcintfDefinition = SrcintfDefinition


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
    DnsMatchIp: Optional[str]
    DnsRequestDomain: Optional[str]
    Failtime: Optional[float]
    FtpFile: Optional[str]
    FtpMode: Optional[str]
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
    QualityMeasuredMethod: Optional[str]
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
    User: Optional[str]
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
            DnsMatchIp=json_data.get("DnsMatchIp"),
            DnsRequestDomain=json_data.get("DnsRequestDomain"),
            Failtime=json_data.get("Failtime"),
            FtpFile=json_data.get("FtpFile"),
            FtpMode=json_data.get("FtpMode"),
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
            QualityMeasuredMethod=json_data.get("QualityMeasuredMethod"),
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
            User=json_data.get("User"),
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
    Id: Optional[float]
    JitterThreshold: Optional[float]
    LatencyThreshold: Optional[float]
    LinkCostFactor: Optional[str]
    PacketlossThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SlaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlaDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            JitterThreshold=json_data.get("JitterThreshold"),
            LatencyThreshold=json_data.get("LatencyThreshold"),
            LinkCostFactor=json_data.get("LinkCostFactor"),
            PacketlossThreshold=json_data.get("PacketlossThreshold"),
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
class ZoneDefinition(BaseModel):
    Name: Optional[str]
    ServiceSlaTieBreak: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZoneDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZoneDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ServiceSlaTieBreak=json_data.get("ServiceSlaTieBreak"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZoneDefinition = ZoneDefinition


