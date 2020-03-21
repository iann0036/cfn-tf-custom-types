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
    DefaultRouteTableId: Optional[str]
    OwnerId: Optional[str]
    PropagatingVgws: Optional[Sequence[str]]
    Route: Optional[Sequence["_Route"]]
    Tags: Optional[Sequence["_Tags"]]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DefaultRouteTableId=json_data.get("DefaultRouteTableId"),
            OwnerId=json_data.get("OwnerId"),
            PropagatingVgws=json_data.get("PropagatingVgws"),
            Route=json_data.get("Route"),
            Tags=json_data.get("Tags"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Route:
    CidrBlock: Optional[str]
    EgressOnlyGatewayId: Optional[str]
    GatewayId: Optional[str]
    InstanceId: Optional[str]
    Ipv6CidrBlock: Optional[str]
    NatGatewayId: Optional[str]
    NetworkInterfaceId: Optional[str]
    TransitGatewayId: Optional[str]
    VpcPeeringConnectionId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Route"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Route"]:
        if not json_data:
            return None
        return cls(
            CidrBlock=json_data.get("CidrBlock"),
            EgressOnlyGatewayId=json_data.get("EgressOnlyGatewayId"),
            GatewayId=json_data.get("GatewayId"),
            InstanceId=json_data.get("InstanceId"),
            Ipv6CidrBlock=json_data.get("Ipv6CidrBlock"),
            NatGatewayId=json_data.get("NatGatewayId"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            TransitGatewayId=json_data.get("TransitGatewayId"),
            VpcPeeringConnectionId=json_data.get("VpcPeeringConnectionId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Route = Route


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


