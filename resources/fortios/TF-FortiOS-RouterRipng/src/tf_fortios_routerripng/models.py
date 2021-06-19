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
    DefaultInformationOriginate: Optional[str]
    DefaultMetric: Optional[float]
    DynamicSortSubtable: Optional[str]
    GarbageTimer: Optional[float]
    Id: Optional[str]
    MaxOutMetric: Optional[float]
    TimeoutTimer: Optional[float]
    UpdateTimer: Optional[float]
    Vdomparam: Optional[str]
    AggregateAddress: Optional[Sequence["_AggregateAddressDefinition"]]
    Distance: Optional[Sequence["_DistanceDefinition"]]
    DistributeList: Optional[Sequence["_DistributeListDefinition"]]
    Interface: Optional[Sequence["_InterfaceDefinition"]]
    Neighbor: Optional[Sequence["_NeighborDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
    OffsetList: Optional[Sequence["_OffsetListDefinition"]]
    PassiveInterface: Optional[Sequence["_PassiveInterfaceDefinition"]]
    Redistribute: Optional[Sequence["_RedistributeDefinition"]]

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
            DefaultInformationOriginate=json_data.get("DefaultInformationOriginate"),
            DefaultMetric=json_data.get("DefaultMetric"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            GarbageTimer=json_data.get("GarbageTimer"),
            Id=json_data.get("Id"),
            MaxOutMetric=json_data.get("MaxOutMetric"),
            TimeoutTimer=json_data.get("TimeoutTimer"),
            UpdateTimer=json_data.get("UpdateTimer"),
            Vdomparam=json_data.get("Vdomparam"),
            AggregateAddress=deserialize_list(json_data.get("AggregateAddress"), AggregateAddressDefinition),
            Distance=deserialize_list(json_data.get("Distance"), DistanceDefinition),
            DistributeList=deserialize_list(json_data.get("DistributeList"), DistributeListDefinition),
            Interface=deserialize_list(json_data.get("Interface"), InterfaceDefinition),
            Neighbor=deserialize_list(json_data.get("Neighbor"), NeighborDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            OffsetList=deserialize_list(json_data.get("OffsetList"), OffsetListDefinition),
            PassiveInterface=deserialize_list(json_data.get("PassiveInterface"), PassiveInterfaceDefinition),
            Redistribute=deserialize_list(json_data.get("Redistribute"), RedistributeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AggregateAddressDefinition(BaseModel):
    Id: Optional[float]
    Prefix6: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AggregateAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggregateAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Prefix6=json_data.get("Prefix6"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggregateAddressDefinition = AggregateAddressDefinition


@dataclass
class DistanceDefinition(BaseModel):
    AccessList6: Optional[str]
    Distance: Optional[float]
    Id: Optional[float]
    Prefix6: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DistanceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DistanceDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessList6=json_data.get("AccessList6"),
            Distance=json_data.get("Distance"),
            Id=json_data.get("Id"),
            Prefix6=json_data.get("Prefix6"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DistanceDefinition = DistanceDefinition


@dataclass
class DistributeListDefinition(BaseModel):
    Direction: Optional[str]
    Id: Optional[float]
    Interface: Optional[str]
    Listname: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DistributeListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DistributeListDefinition"]:
        if not json_data:
            return None
        return cls(
            Direction=json_data.get("Direction"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            Listname=json_data.get("Listname"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DistributeListDefinition = DistributeListDefinition


@dataclass
class InterfaceDefinition(BaseModel):
    Flags: Optional[float]
    Name: Optional[str]
    SplitHorizon: Optional[str]
    SplitHorizonStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Flags=json_data.get("Flags"),
            Name=json_data.get("Name"),
            SplitHorizon=json_data.get("SplitHorizon"),
            SplitHorizonStatus=json_data.get("SplitHorizonStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfaceDefinition = InterfaceDefinition


@dataclass
class NeighborDefinition(BaseModel):
    Id: Optional[float]
    Interface: Optional[str]
    Ip6: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NeighborDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NeighborDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            Ip6=json_data.get("Ip6"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NeighborDefinition = NeighborDefinition


@dataclass
class NetworkDefinition(BaseModel):
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
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class OffsetListDefinition(BaseModel):
    AccessList6: Optional[str]
    Direction: Optional[str]
    Id: Optional[float]
    Interface: Optional[str]
    Offset: Optional[float]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OffsetListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OffsetListDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessList6=json_data.get("AccessList6"),
            Direction=json_data.get("Direction"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            Offset=json_data.get("Offset"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OffsetListDefinition = OffsetListDefinition


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
            Name=json_data.get("Name"),
            Routemap=json_data.get("Routemap"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedistributeDefinition = RedistributeDefinition


