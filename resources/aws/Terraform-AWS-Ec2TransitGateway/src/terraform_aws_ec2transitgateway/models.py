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
    AmazonSideAsn: Optional[float]
    Arn: Optional[str]
    AssociationDefaultRouteTableId: Optional[str]
    AutoAcceptSharedAttachments: Optional[str]
    DefaultRouteTableAssociation: Optional[str]
    DefaultRouteTablePropagation: Optional[str]
    Description: Optional[str]
    DnsSupport: Optional[str]
    Id: Optional[str]
    OwnerId: Optional[str]
    PropagationDefaultRouteTableId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VpnEcmpSupport: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AmazonSideAsn=json_data.get("AmazonSideAsn"),
            Arn=json_data.get("Arn"),
            AssociationDefaultRouteTableId=json_data.get("AssociationDefaultRouteTableId"),
            AutoAcceptSharedAttachments=json_data.get("AutoAcceptSharedAttachments"),
            DefaultRouteTableAssociation=json_data.get("DefaultRouteTableAssociation"),
            DefaultRouteTablePropagation=json_data.get("DefaultRouteTablePropagation"),
            Description=json_data.get("Description"),
            DnsSupport=json_data.get("DnsSupport"),
            Id=json_data.get("Id"),
            OwnerId=json_data.get("OwnerId"),
            PropagationDefaultRouteTableId=json_data.get("PropagationDefaultRouteTableId"),
            Tags=json_data.get("Tags"),
            VpnEcmpSupport=json_data.get("VpnEcmpSupport"),
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


