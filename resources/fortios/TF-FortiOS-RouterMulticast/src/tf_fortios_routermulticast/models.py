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
    Id: Optional[str]
    MulticastRouting: Optional[str]
    RouteLimit: Optional[float]
    RouteThreshold: Optional[float]
    Vdomparam: Optional[str]
    Interface: Optional[Sequence["_InterfaceDefinition"]]
    PimSmGlobal: Optional[Sequence["_PimSmGlobalDefinition"]]

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
            Id=json_data.get("Id"),
            MulticastRouting=json_data.get("MulticastRouting"),
            RouteLimit=json_data.get("RouteLimit"),
            RouteThreshold=json_data.get("RouteThreshold"),
            Vdomparam=json_data.get("Vdomparam"),
            Interface=deserialize_list(json_data.get("Interface"), InterfaceDefinition),
            PimSmGlobal=deserialize_list(json_data.get("PimSmGlobal"), PimSmGlobalDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InterfaceDefinition(BaseModel):
    Bfd: Optional[str]
    CiscoExcludeGenid: Optional[str]
    DrPriority: Optional[float]
    HelloHoldtime: Optional[float]
    HelloInterval: Optional[float]
    MulticastFlow: Optional[str]
    Name: Optional[str]
    NeighbourFilter: Optional[str]
    Passive: Optional[str]
    PimMode: Optional[str]
    PropagationDelay: Optional[float]
    RpCandidate: Optional[str]
    RpCandidateGroup: Optional[str]
    RpCandidateInterval: Optional[float]
    RpCandidatePriority: Optional[float]
    RpfNbrFailBack: Optional[str]
    RpfNbrFailBackFilter: Optional[str]
    StateRefreshInterval: Optional[float]
    StaticGroup: Optional[str]
    TtlThreshold: Optional[float]
    Igmp: Optional[Sequence["_IgmpDefinition"]]
    JoinGroup: Optional[Sequence["_JoinGroupDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Bfd=json_data.get("Bfd"),
            CiscoExcludeGenid=json_data.get("CiscoExcludeGenid"),
            DrPriority=json_data.get("DrPriority"),
            HelloHoldtime=json_data.get("HelloHoldtime"),
            HelloInterval=json_data.get("HelloInterval"),
            MulticastFlow=json_data.get("MulticastFlow"),
            Name=json_data.get("Name"),
            NeighbourFilter=json_data.get("NeighbourFilter"),
            Passive=json_data.get("Passive"),
            PimMode=json_data.get("PimMode"),
            PropagationDelay=json_data.get("PropagationDelay"),
            RpCandidate=json_data.get("RpCandidate"),
            RpCandidateGroup=json_data.get("RpCandidateGroup"),
            RpCandidateInterval=json_data.get("RpCandidateInterval"),
            RpCandidatePriority=json_data.get("RpCandidatePriority"),
            RpfNbrFailBack=json_data.get("RpfNbrFailBack"),
            RpfNbrFailBackFilter=json_data.get("RpfNbrFailBackFilter"),
            StateRefreshInterval=json_data.get("StateRefreshInterval"),
            StaticGroup=json_data.get("StaticGroup"),
            TtlThreshold=json_data.get("TtlThreshold"),
            Igmp=deserialize_list(json_data.get("Igmp"), IgmpDefinition),
            JoinGroup=deserialize_list(json_data.get("JoinGroup"), JoinGroupDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfaceDefinition = InterfaceDefinition


@dataclass
class IgmpDefinition(BaseModel):
    AccessGroup: Optional[str]
    ImmediateLeaveGroup: Optional[str]
    LastMemberQueryCount: Optional[float]
    LastMemberQueryInterval: Optional[float]
    QueryInterval: Optional[float]
    QueryMaxResponseTime: Optional[float]
    QueryTimeout: Optional[float]
    RouterAlertCheck: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IgmpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IgmpDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessGroup=json_data.get("AccessGroup"),
            ImmediateLeaveGroup=json_data.get("ImmediateLeaveGroup"),
            LastMemberQueryCount=json_data.get("LastMemberQueryCount"),
            LastMemberQueryInterval=json_data.get("LastMemberQueryInterval"),
            QueryInterval=json_data.get("QueryInterval"),
            QueryMaxResponseTime=json_data.get("QueryMaxResponseTime"),
            QueryTimeout=json_data.get("QueryTimeout"),
            RouterAlertCheck=json_data.get("RouterAlertCheck"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IgmpDefinition = IgmpDefinition


@dataclass
class JoinGroupDefinition(BaseModel):
    Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JoinGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JoinGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JoinGroupDefinition = JoinGroupDefinition


@dataclass
class PimSmGlobalDefinition(BaseModel):
    AcceptRegisterList: Optional[str]
    AcceptSourceList: Optional[str]
    BsrAllowQuickRefresh: Optional[str]
    BsrCandidate: Optional[str]
    BsrHash: Optional[float]
    BsrInterface: Optional[str]
    BsrPriority: Optional[float]
    CiscoCrpPrefix: Optional[str]
    CiscoIgnoreRpSetPriority: Optional[str]
    CiscoRegisterChecksum: Optional[str]
    CiscoRegisterChecksumGroup: Optional[str]
    JoinPruneHoldtime: Optional[float]
    MessageInterval: Optional[float]
    NullRegisterRetries: Optional[float]
    RegisterRateLimit: Optional[float]
    RegisterRpReachability: Optional[str]
    RegisterSource: Optional[str]
    RegisterSourceInterface: Optional[str]
    RegisterSourceIp: Optional[str]
    RegisterSupression: Optional[float]
    RpRegisterKeepalive: Optional[float]
    SptThreshold: Optional[str]
    SptThresholdGroup: Optional[str]
    Ssm: Optional[str]
    SsmRange: Optional[str]
    RpAddress: Optional[Sequence["_RpAddressDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PimSmGlobalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PimSmGlobalDefinition"]:
        if not json_data:
            return None
        return cls(
            AcceptRegisterList=json_data.get("AcceptRegisterList"),
            AcceptSourceList=json_data.get("AcceptSourceList"),
            BsrAllowQuickRefresh=json_data.get("BsrAllowQuickRefresh"),
            BsrCandidate=json_data.get("BsrCandidate"),
            BsrHash=json_data.get("BsrHash"),
            BsrInterface=json_data.get("BsrInterface"),
            BsrPriority=json_data.get("BsrPriority"),
            CiscoCrpPrefix=json_data.get("CiscoCrpPrefix"),
            CiscoIgnoreRpSetPriority=json_data.get("CiscoIgnoreRpSetPriority"),
            CiscoRegisterChecksum=json_data.get("CiscoRegisterChecksum"),
            CiscoRegisterChecksumGroup=json_data.get("CiscoRegisterChecksumGroup"),
            JoinPruneHoldtime=json_data.get("JoinPruneHoldtime"),
            MessageInterval=json_data.get("MessageInterval"),
            NullRegisterRetries=json_data.get("NullRegisterRetries"),
            RegisterRateLimit=json_data.get("RegisterRateLimit"),
            RegisterRpReachability=json_data.get("RegisterRpReachability"),
            RegisterSource=json_data.get("RegisterSource"),
            RegisterSourceInterface=json_data.get("RegisterSourceInterface"),
            RegisterSourceIp=json_data.get("RegisterSourceIp"),
            RegisterSupression=json_data.get("RegisterSupression"),
            RpRegisterKeepalive=json_data.get("RpRegisterKeepalive"),
            SptThreshold=json_data.get("SptThreshold"),
            SptThresholdGroup=json_data.get("SptThresholdGroup"),
            Ssm=json_data.get("Ssm"),
            SsmRange=json_data.get("SsmRange"),
            RpAddress=deserialize_list(json_data.get("RpAddress"), RpAddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PimSmGlobalDefinition = PimSmGlobalDefinition


@dataclass
class RpAddressDefinition(BaseModel):
    Group: Optional[str]
    Id: Optional[float]
    IpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RpAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RpAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Group=json_data.get("Group"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RpAddressDefinition = RpAddressDefinition


