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
    DefaultInformationMetric: Optional[float]
    DefaultInformationMetricType: Optional[str]
    DefaultInformationOriginate: Optional[str]
    DefaultInformationRouteMap: Optional[str]
    DefaultMetric: Optional[float]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    LogNeighbourChanges: Optional[str]
    RouterId: Optional[str]
    SpfTimers: Optional[str]
    Vdomparam: Optional[str]
    Area: Optional[Sequence["_AreaDefinition"]]
    Ospf6Interface: Optional[Sequence["_Ospf6InterfaceDefinition"]]
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
            DefaultInformationMetric=json_data.get("DefaultInformationMetric"),
            DefaultInformationMetricType=json_data.get("DefaultInformationMetricType"),
            DefaultInformationOriginate=json_data.get("DefaultInformationOriginate"),
            DefaultInformationRouteMap=json_data.get("DefaultInformationRouteMap"),
            DefaultMetric=json_data.get("DefaultMetric"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            LogNeighbourChanges=json_data.get("LogNeighbourChanges"),
            RouterId=json_data.get("RouterId"),
            SpfTimers=json_data.get("SpfTimers"),
            Vdomparam=json_data.get("Vdomparam"),
            Area=deserialize_list(json_data.get("Area"), AreaDefinition),
            Ospf6Interface=deserialize_list(json_data.get("Ospf6Interface"), Ospf6InterfaceDefinition),
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
    IpsecAuthAlg: Optional[str]
    IpsecEncAlg: Optional[str]
    KeyRolloverInterval: Optional[float]
    NssaDefaultInformationOriginate: Optional[str]
    NssaDefaultInformationOriginateMetric: Optional[float]
    NssaDefaultInformationOriginateMetricType: Optional[str]
    NssaRedistribution: Optional[str]
    NssaTranslatorRole: Optional[str]
    StubType: Optional[str]
    Type: Optional[str]
    IpsecKeys: Optional[Sequence["_IpsecKeysDefinition"]]
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
            IpsecAuthAlg=json_data.get("IpsecAuthAlg"),
            IpsecEncAlg=json_data.get("IpsecEncAlg"),
            KeyRolloverInterval=json_data.get("KeyRolloverInterval"),
            NssaDefaultInformationOriginate=json_data.get("NssaDefaultInformationOriginate"),
            NssaDefaultInformationOriginateMetric=json_data.get("NssaDefaultInformationOriginateMetric"),
            NssaDefaultInformationOriginateMetricType=json_data.get("NssaDefaultInformationOriginateMetricType"),
            NssaRedistribution=json_data.get("NssaRedistribution"),
            NssaTranslatorRole=json_data.get("NssaTranslatorRole"),
            StubType=json_data.get("StubType"),
            Type=json_data.get("Type"),
            IpsecKeys=deserialize_list(json_data.get("IpsecKeys"), IpsecKeysDefinition),
            Range=deserialize_list(json_data.get("Range"), RangeDefinition),
            VirtualLink=deserialize_list(json_data.get("VirtualLink"), VirtualLinkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AreaDefinition = AreaDefinition


@dataclass
class IpsecKeysDefinition(BaseModel):
    AuthKey: Optional[str]
    EncKey: Optional[str]
    Spi: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IpsecKeysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpsecKeysDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthKey=json_data.get("AuthKey"),
            EncKey=json_data.get("EncKey"),
            Spi=json_data.get("Spi"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpsecKeysDefinition = IpsecKeysDefinition


@dataclass
class RangeDefinition(BaseModel):
    Advertise: Optional[str]
    Id: Optional[float]
    Prefix6: Optional[str]

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
            Prefix6=json_data.get("Prefix6"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangeDefinition = RangeDefinition


@dataclass
class VirtualLinkDefinition(BaseModel):
    Authentication: Optional[str]
    DeadInterval: Optional[float]
    HelloInterval: Optional[float]
    IpsecAuthAlg: Optional[str]
    IpsecEncAlg: Optional[str]
    KeyRolloverInterval: Optional[float]
    Name: Optional[str]
    Peer: Optional[str]
    RetransmitInterval: Optional[float]
    TransmitDelay: Optional[float]
    IpsecKeys: Optional[Sequence["_IpsecKeysDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualLinkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualLinkDefinition"]:
        if not json_data:
            return None
        return cls(
            Authentication=json_data.get("Authentication"),
            DeadInterval=json_data.get("DeadInterval"),
            HelloInterval=json_data.get("HelloInterval"),
            IpsecAuthAlg=json_data.get("IpsecAuthAlg"),
            IpsecEncAlg=json_data.get("IpsecEncAlg"),
            KeyRolloverInterval=json_data.get("KeyRolloverInterval"),
            Name=json_data.get("Name"),
            Peer=json_data.get("Peer"),
            RetransmitInterval=json_data.get("RetransmitInterval"),
            TransmitDelay=json_data.get("TransmitDelay"),
            IpsecKeys=deserialize_list(json_data.get("IpsecKeys"), IpsecKeysDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualLinkDefinition = VirtualLinkDefinition


@dataclass
class Ospf6InterfaceDefinition(BaseModel):
    AreaId: Optional[str]
    Authentication: Optional[str]
    Bfd: Optional[str]
    Cost: Optional[float]
    DeadInterval: Optional[float]
    HelloInterval: Optional[float]
    Interface: Optional[str]
    IpsecAuthAlg: Optional[str]
    IpsecEncAlg: Optional[str]
    KeyRolloverInterval: Optional[float]
    Mtu: Optional[float]
    MtuIgnore: Optional[str]
    Name: Optional[str]
    NetworkType: Optional[str]
    Priority: Optional[float]
    RetransmitInterval: Optional[float]
    Status: Optional[str]
    TransmitDelay: Optional[float]
    IpsecKeys: Optional[Sequence["_IpsecKeysDefinition"]]
    Neighbor: Optional[Sequence["_NeighborDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Ospf6InterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ospf6InterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            AreaId=json_data.get("AreaId"),
            Authentication=json_data.get("Authentication"),
            Bfd=json_data.get("Bfd"),
            Cost=json_data.get("Cost"),
            DeadInterval=json_data.get("DeadInterval"),
            HelloInterval=json_data.get("HelloInterval"),
            Interface=json_data.get("Interface"),
            IpsecAuthAlg=json_data.get("IpsecAuthAlg"),
            IpsecEncAlg=json_data.get("IpsecEncAlg"),
            KeyRolloverInterval=json_data.get("KeyRolloverInterval"),
            Mtu=json_data.get("Mtu"),
            MtuIgnore=json_data.get("MtuIgnore"),
            Name=json_data.get("Name"),
            NetworkType=json_data.get("NetworkType"),
            Priority=json_data.get("Priority"),
            RetransmitInterval=json_data.get("RetransmitInterval"),
            Status=json_data.get("Status"),
            TransmitDelay=json_data.get("TransmitDelay"),
            IpsecKeys=deserialize_list(json_data.get("IpsecKeys"), IpsecKeysDefinition),
            Neighbor=deserialize_list(json_data.get("Neighbor"), NeighborDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ospf6InterfaceDefinition = Ospf6InterfaceDefinition


@dataclass
class NeighborDefinition(BaseModel):
    Cost: Optional[float]
    Ip6: Optional[str]
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
            Ip6=json_data.get("Ip6"),
            PollInterval=json_data.get("PollInterval"),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NeighborDefinition = NeighborDefinition


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
        )


# work around possible type aliasing issues when variable has same name as a model
_RedistributeDefinition = RedistributeDefinition


@dataclass
class SummaryAddressDefinition(BaseModel):
    Advertise: Optional[str]
    Id: Optional[float]
    Prefix6: Optional[str]
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
            Prefix6=json_data.get("Prefix6"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SummaryAddressDefinition = SummaryAddressDefinition


