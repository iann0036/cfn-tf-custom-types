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
    AssignIpv4: Optional[Sequence["_AssignIpv4Definition"]]
    AssignIpv6: Optional[Sequence["_AssignIpv6Definition"]]
    CreationTime: Optional[float]
    Description: Optional[str]
    EnableBroadcast: Optional[bool]
    FlowRules: Optional[str]
    Id: Optional[str]
    Mtu: Optional[float]
    MulticastLimit: Optional[float]
    Name: Optional[str]
    Private: Optional[bool]
    TfLastUpdated: Optional[float]
    AssignmentPool: Optional[Sequence["_AssignmentPoolDefinition"]]
    Route: Optional[Sequence["_RouteDefinition"]]

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
            AssignIpv4=deserialize_list(json_data.get("AssignIpv4"), AssignIpv4Definition),
            AssignIpv6=deserialize_list(json_data.get("AssignIpv6"), AssignIpv6Definition),
            CreationTime=json_data.get("CreationTime"),
            Description=json_data.get("Description"),
            EnableBroadcast=json_data.get("EnableBroadcast"),
            FlowRules=json_data.get("FlowRules"),
            Id=json_data.get("Id"),
            Mtu=json_data.get("Mtu"),
            MulticastLimit=json_data.get("MulticastLimit"),
            Name=json_data.get("Name"),
            Private=json_data.get("Private"),
            TfLastUpdated=json_data.get("TfLastUpdated"),
            AssignmentPool=deserialize_list(json_data.get("AssignmentPool"), AssignmentPoolDefinition),
            Route=deserialize_list(json_data.get("Route"), RouteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AssignIpv4Definition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AssignIpv4Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssignIpv4Definition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssignIpv4Definition = AssignIpv4Definition


@dataclass
class AssignIpv6Definition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AssignIpv6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssignIpv6Definition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssignIpv6Definition = AssignIpv6Definition


@dataclass
class AssignmentPoolDefinition(BaseModel):
    Cidr: Optional[str]
    End: Optional[str]
    Start: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssignmentPoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssignmentPoolDefinition"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssignmentPoolDefinition = AssignmentPoolDefinition


@dataclass
class RouteDefinition(BaseModel):
    Target: Optional[str]
    Via: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteDefinition"]:
        if not json_data:
            return None
        return cls(
            Target=json_data.get("Target"),
            Via=json_data.get("Via"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteDefinition = RouteDefinition


