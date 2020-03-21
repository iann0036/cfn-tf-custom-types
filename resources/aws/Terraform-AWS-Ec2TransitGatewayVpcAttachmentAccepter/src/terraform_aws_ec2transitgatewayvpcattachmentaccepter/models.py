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
    DnsSupport: Optional[str]
    Ipv6Support: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    TransitGatewayAttachmentId: Optional[str]
    TransitGatewayDefaultRouteTableAssociation: Optional[bool]
    TransitGatewayDefaultRouteTablePropagation: Optional[bool]
    TransitGatewayId: Optional[str]
    VpcId: Optional[str]
    VpcOwnerId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DnsSupport=json_data.get("DnsSupport"),
            Ipv6Support=json_data.get("Ipv6Support"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=json_data.get("Tags"),
            TransitGatewayAttachmentId=json_data.get("TransitGatewayAttachmentId"),
            TransitGatewayDefaultRouteTableAssociation=json_data.get("TransitGatewayDefaultRouteTableAssociation"),
            TransitGatewayDefaultRouteTablePropagation=json_data.get("TransitGatewayDefaultRouteTablePropagation"),
            TransitGatewayId=json_data.get("TransitGatewayId"),
            VpcId=json_data.get("VpcId"),
            VpcOwnerId=json_data.get("VpcOwnerId"),
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


