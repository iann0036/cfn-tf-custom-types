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
    HubToVitualNetworkTrafficAllowed: Optional[bool]
    Id: Optional[str]
    InternetSecurityEnabled: Optional[bool]
    Name: Optional[str]
    RemoteVirtualNetworkId: Optional[str]
    VirtualHubId: Optional[str]
    VitualNetworkToHubGatewaysTrafficAllowed: Optional[bool]
    Routing: Optional[Sequence["_RoutingDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            HubToVitualNetworkTrafficAllowed=json_data.get("HubToVitualNetworkTrafficAllowed"),
            Id=json_data.get("Id"),
            InternetSecurityEnabled=json_data.get("InternetSecurityEnabled"),
            Name=json_data.get("Name"),
            RemoteVirtualNetworkId=json_data.get("RemoteVirtualNetworkId"),
            VirtualHubId=json_data.get("VirtualHubId"),
            VitualNetworkToHubGatewaysTrafficAllowed=json_data.get("VitualNetworkToHubGatewaysTrafficAllowed"),
            Routing=deserialize_list(json_data.get("Routing"), RoutingDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RoutingDefinition(BaseModel):
    AssociatedRouteTableId: Optional[str]
    PropagatedRouteTable: Optional[Sequence["_PropagatedRouteTableDefinition"]]
    StaticVnetRoute: Optional[Sequence["_StaticVnetRouteDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingDefinition"]:
        if not json_data:
            return None
        return cls(
            AssociatedRouteTableId=json_data.get("AssociatedRouteTableId"),
            PropagatedRouteTable=deserialize_list(json_data.get("PropagatedRouteTable"), PropagatedRouteTableDefinition),
            StaticVnetRoute=deserialize_list(json_data.get("StaticVnetRoute"), StaticVnetRouteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingDefinition = RoutingDefinition


@dataclass
class PropagatedRouteTableDefinition(BaseModel):
    Labels: Optional[Sequence[str]]
    RouteTableIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PropagatedRouteTableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropagatedRouteTableDefinition"]:
        if not json_data:
            return None
        return cls(
            Labels=json_data.get("Labels"),
            RouteTableIds=json_data.get("RouteTableIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropagatedRouteTableDefinition = PropagatedRouteTableDefinition


@dataclass
class StaticVnetRouteDefinition(BaseModel):
    AddressPrefixes: Optional[Sequence[str]]
    Name: Optional[str]
    NextHopIpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StaticVnetRouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticVnetRouteDefinition"]:
        if not json_data:
            return None
        return cls(
            AddressPrefixes=json_data.get("AddressPrefixes"),
            Name=json_data.get("Name"),
            NextHopIpAddress=json_data.get("NextHopIpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticVnetRouteDefinition = StaticVnetRouteDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


