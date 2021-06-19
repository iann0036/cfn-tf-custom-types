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
    AbrType: Optional[str]
    AutoCostRefBandwidth: Optional[float]
    Bfd: Optional[str]
    DatabaseOverflow: Optional[str]
    DatabaseOverflowMaxLsas: Optional[float]
    DatabaseOverflowTimeToRecover: Optional[float]
    DefaultInformationMetric: Optional[float]
    DefaultInformationMetricType: Optional[str]
    DefaultInformationOriginate: Optional[str]
    DefaultInformationRouteMap: Optional[str]
    DefaultMetric: Optional[float]
    Distance: Optional[float]
    DistanceExternal: Optional[float]
    DistanceInterArea: Optional[float]
    DistanceIntraArea: Optional[float]
    DistributeListIn: Optional[str]
    DistributeRouteMapIn: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    LogNeighbourChanges: Optional[str]
    RestartMode: Optional[str]
    RestartPeriod: Optional[float]
    Rfc1583Compatible: Optional[str]
    RouterId: Optional[str]
    SpfTimers: Optional[str]
    Vdomparam: Optional[str]
    Area: Optional[Sequence["_AreaDefinition"]]
    DistributeList: Optional[Sequence["_DistributeListDefinition"]]
    Neighbor: Optional[Sequence["_NeighborDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
    OspfInterface: Optional[Sequence["_OspfInterfaceDefinition"]]
    PassiveInterface: Optional[Sequence["_PassiveInterfaceDefinition"]]
    Redistribute: Optional[Sequence["_RedistributeDefinition"]]
    SummaryAddress: Optional[Sequence["_SummaryAddressDefinition"]]

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
            AbrType=json_data.get("AbrType"),
            AutoCostRefBandwidth=json_data.get("AutoCostRefBandwidth"),
            Bfd=json_data.get("Bfd"),
            DatabaseOverflow=json_data.get("DatabaseOverflow"),
            DatabaseOverflowMaxLsas=json_data.get("DatabaseOverflowMaxLsas"),
            DatabaseOverflowTimeToRecover=json_data.get("DatabaseOverflowTimeToRecover"),
            DefaultInformationMetric=json_data.get("DefaultInformationMetric"),
            DefaultInformationMetricType=json_data.get("DefaultInformationMetricType"),
            DefaultInformationOriginate=json_data.get("DefaultInformationOriginate"),
            DefaultInformationRouteMap=json_data.get("DefaultInformationRouteMap"),
            DefaultMetric=json_data.get("DefaultMetric"),
            Distance=json_data.get("Distance"),
            DistanceExternal=json_data.get("DistanceExternal"),
            DistanceInterArea=json_data.get("DistanceInterArea"),
            DistanceIntraArea=json_data.get("DistanceIntraArea"),
            DistributeListIn=json_data.get("DistributeListIn"),
            DistributeRouteMapIn=json_data.get("DistributeRouteMapIn"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            LogNeighbourChanges=json_data.get("LogNeighbourChanges"),
            RestartMode=json_data.get("RestartMode"),
            RestartPeriod=json_data.get("RestartPeriod"),
            Rfc1583Compatible=json_data.get("Rfc1583Compatible"),
            RouterId=json_data.get("RouterId"),
            SpfTimers=json_data.get("SpfTimers"),
            Vdomparam=json_data.get("Vdomparam"),
            Area=deserialize_list(json_data.get("Area"), AreaDefinition),
            DistributeList=deserialize_list(json_data.get("DistributeList"), DistributeListDefinition),
            Neighbor=deserialize_list(json_data.get("Neighbor"), NeighborDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            OspfInterface=deserialize_list(json_data.get("OspfInterface"), OspfInterfaceDefinition),
            PassiveInterface=deserialize_list(json_data.get("PassiveInterface"), PassiveInterfaceDefinition),
            Redistribute=deserialize_list(json_data.get("Redistribute"), RedistributeDefinition),
            SummaryAddress=deserialize_list(json_data.get("SummaryAddress"), SummaryAddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AreaDefinition(BaseModel):
    Authentication: Optional[str]
    DefaultCost: Optional[float]
    Id: Optional[str]
    NssaDefaultInformationOriginate: Optional[str]
    NssaDefaultInformationOriginateMetric: Optional[float]
    NssaDefaultInformationOriginateMetricType: Optional[str]
    NssaRedistribution: Optional[str]
    NssaTranslatorRole: Optional[str]
    Shortcut: Optional[str]
    StubType: Optional[str]
    Type: Optional[str]
    FilterList: Optional[Sequence["_FilterListDefinition"]]
    Range: Optional[Sequence["_RangeDefinition"]]
    VirtualLink: Optional[Sequence["_VirtualLinkDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AreaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AreaDefinition"]:
        if not json_data:
            return None
        return cls(
            Authentication=json_data.get("Authentication"),
            DefaultCost=json_data.get("DefaultCost"),
            Id=json_data.get("Id"),
            NssaDefaultInformationOriginate=json_data.get("NssaDefaultInformationOriginate"),
            NssaDefaultInformationOriginateMetric=json_data.get("NssaDefaultInformationOriginateMetric"),
            NssaDefaultInformationOriginateMetricType=json_data.get("NssaDefaultInformationOriginateMetricType"),
            NssaRedistribution=json_data.get("NssaRedistribution"),
            NssaTranslatorRole=json_data.get("NssaTranslatorRole"),
            Shortcut=json_data.get("Shortcut"),
            StubType=json_data.get("StubType"),
            Type=json_data.get("Type"),
            FilterList=deserialize_list(json_data.get("FilterList"), FilterListDefinition),
            Range=deserialize_list(json_data.get("Range"), RangeDefinition),
            VirtualLink=deserialize_list(json_data.get("VirtualLink"), VirtualLinkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AreaDefinition = AreaDefinition


@dataclass
class FilterListDefinition(BaseModel):
    Direction: Optional[str]
    Id: Optional[float]
    List: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterListDefinition"]:
        if not json_data:
            return None
        return cls(
            Direction=json_data.get("Direction"),
            Id=json_data.get("Id"),
            List=json_data.get("List"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterListDefinition = FilterListDefinition


@dataclass
class RangeDefinition(BaseModel):
    Advertise: Optional[str]
    Id: Optional[float]
    Prefix: Optional[str]
    Substitute: Optional[str]
    SubstituteStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Advertise=json_data.get("Advertise"),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
            Substitute=json_data.get("Substitute"),
            SubstituteStatus=json_data.get("SubstituteStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangeDefinition = RangeDefinition


@dataclass
class VirtualLinkDefinition(BaseModel):
    Authentication: Optional[str]
    AuthenticationKey: Optional[str]
    DeadInterval: Optional[float]
    HelloInterval: Optional[float]
    Md5Key: Optional[str]
    Md5Keychain: Optional[str]
    Name: Optional[str]
    Peer: Optional[str]
    RetransmitInterval: Optional[float]
    TransmitDelay: Optional[float]
    Md5Keys: Optional[Sequence["_Md5KeysDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualLinkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualLinkDefinition"]:
        if not json_data:
            return None
        return cls(
            Authentication=json_data.get("Authentication"),
            AuthenticationKey=json_data.get("AuthenticationKey"),
            DeadInterval=json_data.get("DeadInterval"),
            HelloInterval=json_data.get("HelloInterval"),
            Md5Key=json_data.get("Md5Key"),
            Md5Keychain=json_data.get("Md5Keychain"),
            Name=json_data.get("Name"),
            Peer=json_data.get("Peer"),
            RetransmitInterval=json_data.get("RetransmitInterval"),
            TransmitDelay=json_data.get("TransmitDelay"),
            Md5Keys=deserialize_list(json_data.get("Md5Keys"), Md5KeysDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualLinkDefinition = VirtualLinkDefinition


@dataclass
class Md5KeysDefinition(BaseModel):
    Id: Optional[float]
    KeyString: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Md5KeysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Md5KeysDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            KeyString=json_data.get("KeyString"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Md5KeysDefinition = Md5KeysDefinition


@dataclass
class DistributeListDefinition(BaseModel):
    AccessList: Optional[str]
    Id: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DistributeListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DistributeListDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessList=json_data.get("AccessList"),
            Id=json_data.get("Id"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DistributeListDefinition = DistributeListDefinition


@dataclass
class NeighborDefinition(BaseModel):
    Cost: Optional[float]
    Id: Optional[float]
    Ip: Optional[str]
    PollInterval: Optional[float]
    Priority: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NeighborDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NeighborDefinition"]:
        if not json_data:
            return None
        return cls(
            Cost=json_data.get("Cost"),
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            PollInterval=json_data.get("PollInterval"),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NeighborDefinition = NeighborDefinition


@dataclass
class NetworkDefinition(BaseModel):
    Area: Optional[str]
    Id: Optional[float]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Area=json_data.get("Area"),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class OspfInterfaceDefinition(BaseModel):
    Authentication: Optional[str]
    AuthenticationKey: Optional[str]
    Bfd: Optional[str]
    Cost: Optional[float]
    DatabaseFilterOut: Optional[str]
    DeadInterval: Optional[float]
    HelloInterval: Optional[float]
    HelloMultiplier: Optional[float]
    Interface: Optional[str]
    Ip: Optional[str]
    Md5Key: Optional[str]
    Md5Keychain: Optional[str]
    Mtu: Optional[float]
    MtuIgnore: Optional[str]
    Name: Optional[str]
    NetworkType: Optional[str]
    PrefixLength: Optional[float]
    Priority: Optional[float]
    ResyncTimeout: Optional[float]
    RetransmitInterval: Optional[float]
    Status: Optional[str]
    TransmitDelay: Optional[float]
    Md5Keys: Optional[Sequence["_Md5KeysDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OspfInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OspfInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Authentication=json_data.get("Authentication"),
            AuthenticationKey=json_data.get("AuthenticationKey"),
            Bfd=json_data.get("Bfd"),
            Cost=json_data.get("Cost"),
            DatabaseFilterOut=json_data.get("DatabaseFilterOut"),
            DeadInterval=json_data.get("DeadInterval"),
            HelloInterval=json_data.get("HelloInterval"),
            HelloMultiplier=json_data.get("HelloMultiplier"),
            Interface=json_data.get("Interface"),
            Ip=json_data.get("Ip"),
            Md5Key=json_data.get("Md5Key"),
            Md5Keychain=json_data.get("Md5Keychain"),
            Mtu=json_data.get("Mtu"),
            MtuIgnore=json_data.get("MtuIgnore"),
            Name=json_data.get("Name"),
            NetworkType=json_data.get("NetworkType"),
            PrefixLength=json_data.get("PrefixLength"),
            Priority=json_data.get("Priority"),
            ResyncTimeout=json_data.get("ResyncTimeout"),
            RetransmitInterval=json_data.get("RetransmitInterval"),
            Status=json_data.get("Status"),
            TransmitDelay=json_data.get("TransmitDelay"),
            Md5Keys=deserialize_list(json_data.get("Md5Keys"), Md5KeysDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OspfInterfaceDefinition = OspfInterfaceDefinition


@dataclass
class PassiveInterfaceDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PassiveInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PassiveInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PassiveInterfaceDefinition = PassiveInterfaceDefinition


@dataclass
class RedistributeDefinition(BaseModel):
    Metric: Optional[float]
    MetricType: Optional[str]
    Name: Optional[str]
    Routemap: Optional[str]
    Status: Optional[str]
    Tag: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RedistributeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedistributeDefinition"]:
        if not json_data:
            return None
        return cls(
            Metric=json_data.get("Metric"),
            MetricType=json_data.get("MetricType"),
            Name=json_data.get("Name"),
            Routemap=json_data.get("Routemap"),
            Status=json_data.get("Status"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedistributeDefinition = RedistributeDefinition


@dataclass
class SummaryAddressDefinition(BaseModel):
    Advertise: Optional[str]
    Id: Optional[float]
    Prefix: Optional[str]
    Tag: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SummaryAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SummaryAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Advertise=json_data.get("Advertise"),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SummaryAddressDefinition = SummaryAddressDefinition


