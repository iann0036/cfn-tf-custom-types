# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    AuthorizationKey: Optional[str]
    EnableBgp: Optional[bool]
    ExpressRouteCircuitId: Optional[str]
    LocalNetworkGatewayId: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PeerVirtualNetworkGatewayId: Optional[str]
    ResourceGroupName: Optional[str]
    RoutingWeight: Optional[float]
    SharedKey: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Type: Optional[str]
    VirtualNetworkGatewayId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AuthorizationKey=json_data.get("AuthorizationKey"),
            EnableBgp=json_data.get("EnableBgp"),
            ExpressRouteCircuitId=json_data.get("ExpressRouteCircuitId"),
            LocalNetworkGatewayId=json_data.get("LocalNetworkGatewayId"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PeerVirtualNetworkGatewayId=json_data.get("PeerVirtualNetworkGatewayId"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RoutingWeight=json_data.get("RoutingWeight"),
            SharedKey=json_data.get("SharedKey"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            VirtualNetworkGatewayId=json_data.get("VirtualNetworkGatewayId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


