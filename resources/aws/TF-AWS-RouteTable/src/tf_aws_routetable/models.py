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
    Arn: Optional[str]
    Id: Optional[str]
    OwnerId: Optional[str]
    PropagatingVgws: Optional[Sequence[str]]
    Route: Optional[Sequence["_RouteDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    VpcId: Optional[str]

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
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            OwnerId=json_data.get("OwnerId"),
            PropagatingVgws=json_data.get("PropagatingVgws"),
            Route=deserialize_list(json_data.get("Route"), RouteDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RouteDefinition(BaseModel):
    CarrierGatewayId: Optional[str]
    CidrBlock: Optional[str]
    DestinationPrefixListId: Optional[str]
    EgressOnlyGatewayId: Optional[str]
    GatewayId: Optional[str]
    InstanceId: Optional[str]
    Ipv6CidrBlock: Optional[str]
    LocalGatewayId: Optional[str]
    NatGatewayId: Optional[str]
    NetworkInterfaceId: Optional[str]
    TransitGatewayId: Optional[str]
    VpcEndpointId: Optional[str]
    VpcPeeringConnectionId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteDefinition"]:
        if not json_data:
            return None
        return cls(
            CarrierGatewayId=json_data.get("CarrierGatewayId"),
            CidrBlock=json_data.get("CidrBlock"),
            DestinationPrefixListId=json_data.get("DestinationPrefixListId"),
            EgressOnlyGatewayId=json_data.get("EgressOnlyGatewayId"),
            GatewayId=json_data.get("GatewayId"),
            InstanceId=json_data.get("InstanceId"),
            Ipv6CidrBlock=json_data.get("Ipv6CidrBlock"),
            LocalGatewayId=json_data.get("LocalGatewayId"),
            NatGatewayId=json_data.get("NatGatewayId"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            TransitGatewayId=json_data.get("TransitGatewayId"),
            VpcEndpointId=json_data.get("VpcEndpointId"),
            VpcPeeringConnectionId=json_data.get("VpcPeeringConnectionId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteDefinition = RouteDefinition


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


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


