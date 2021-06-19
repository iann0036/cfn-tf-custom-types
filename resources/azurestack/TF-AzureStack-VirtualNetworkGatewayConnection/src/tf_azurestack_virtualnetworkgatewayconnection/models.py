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
    AuthorizationKey: Optional[str]
    EnableBgp: Optional[bool]
    ExpressRouteCircuitId: Optional[str]
    Id: Optional[str]
    LocalNetworkGatewayId: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PeerVirtualNetworkGatewayId: Optional[str]
    ResourceGroupName: Optional[str]
    RoutingWeight: Optional[float]
    SharedKey: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Type: Optional[str]
    VirtualNetworkGatewayId: Optional[str]

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
            AuthorizationKey=json_data.get("AuthorizationKey"),
            EnableBgp=json_data.get("EnableBgp"),
            ExpressRouteCircuitId=json_data.get("ExpressRouteCircuitId"),
            Id=json_data.get("Id"),
            LocalNetworkGatewayId=json_data.get("LocalNetworkGatewayId"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PeerVirtualNetworkGatewayId=json_data.get("PeerVirtualNetworkGatewayId"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RoutingWeight=json_data.get("RoutingWeight"),
            SharedKey=json_data.get("SharedKey"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Type=json_data.get("Type"),
            VirtualNetworkGatewayId=json_data.get("VirtualNetworkGatewayId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


