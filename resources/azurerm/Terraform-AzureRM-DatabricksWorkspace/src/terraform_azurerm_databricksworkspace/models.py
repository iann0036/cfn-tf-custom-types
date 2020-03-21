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
    Location: Optional[str]
    ManagedResourceGroupId: Optional[str]
    ManagedResourceGroupName: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Sku: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    CustomParameters: Optional[Sequence["_CustomParameters"]]
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
            Location=json_data.get("Location"),
            ManagedResourceGroupId=json_data.get("ManagedResourceGroupId"),
            ManagedResourceGroupName=json_data.get("ManagedResourceGroupName"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Sku=json_data.get("Sku"),
            Tags=json_data.get("Tags"),
            CustomParameters=json_data.get("CustomParameters"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
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


@dataclass
class CustomParameters:
    NoPublicIp: Optional[bool]
    PrivateSubnetName: Optional[str]
    PublicSubnetName: Optional[str]
    VirtualNetworkId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomParameters"]:
        if not json_data:
            return None
        return cls(
            NoPublicIp=json_data.get("NoPublicIp"),
            PrivateSubnetName=json_data.get("PrivateSubnetName"),
            PublicSubnetName=json_data.get("PublicSubnetName"),
            VirtualNetworkId=json_data.get("VirtualNetworkId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomParameters = CustomParameters


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


