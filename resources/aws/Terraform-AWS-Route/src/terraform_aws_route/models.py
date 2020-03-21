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
    DestinationCidrBlock: Optional[str]
    DestinationIpv6CidrBlock: Optional[str]
    DestinationPrefixListId: Optional[str]
    EgressOnlyGatewayId: Optional[str]
    GatewayId: Optional[str]
    InstanceId: Optional[str]
    InstanceOwnerId: Optional[str]
    NatGatewayId: Optional[str]
    NetworkInterfaceId: Optional[str]
    Origin: Optional[str]
    RouteTableId: Optional[str]
    State: Optional[str]
    TransitGatewayId: Optional[str]
    VpcPeeringConnectionId: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DestinationCidrBlock=json_data.get("DestinationCidrBlock"),
            DestinationIpv6CidrBlock=json_data.get("DestinationIpv6CidrBlock"),
            DestinationPrefixListId=json_data.get("DestinationPrefixListId"),
            EgressOnlyGatewayId=json_data.get("EgressOnlyGatewayId"),
            GatewayId=json_data.get("GatewayId"),
            InstanceId=json_data.get("InstanceId"),
            InstanceOwnerId=json_data.get("InstanceOwnerId"),
            NatGatewayId=json_data.get("NatGatewayId"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            Origin=json_data.get("Origin"),
            RouteTableId=json_data.get("RouteTableId"),
            State=json_data.get("State"),
            TransitGatewayId=json_data.get("TransitGatewayId"),
            VpcPeeringConnectionId=json_data.get("VpcPeeringConnectionId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


