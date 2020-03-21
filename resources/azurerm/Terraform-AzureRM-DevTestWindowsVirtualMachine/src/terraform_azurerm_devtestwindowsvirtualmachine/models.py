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
    AllowClaim: Optional[bool]
    DisallowPublicIpAddress: Optional[bool]
    Fqdn: Optional[str]
    Id: Optional[str]
    LabName: Optional[str]
    LabSubnetName: Optional[str]
    LabVirtualNetworkId: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    Notes: Optional[str]
    Password: Optional[str]
    ResourceGroupName: Optional[str]
    Size: Optional[str]
    StorageType: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    UniqueIdentifier: Optional[str]
    Username: Optional[str]
    GalleryImageReference: Optional[Sequence["_GalleryImageReference"]]
    InboundNatRule: Optional[Sequence["_InboundNatRule"]]
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
            AllowClaim=json_data.get("AllowClaim"),
            DisallowPublicIpAddress=json_data.get("DisallowPublicIpAddress"),
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            LabName=json_data.get("LabName"),
            LabSubnetName=json_data.get("LabSubnetName"),
            LabVirtualNetworkId=json_data.get("LabVirtualNetworkId"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Password=json_data.get("Password"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Size=json_data.get("Size"),
            StorageType=json_data.get("StorageType"),
            Tags=json_data.get("Tags"),
            UniqueIdentifier=json_data.get("UniqueIdentifier"),
            Username=json_data.get("Username"),
            GalleryImageReference=json_data.get("GalleryImageReference"),
            InboundNatRule=json_data.get("InboundNatRule"),
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
class GalleryImageReference:
    Offer: Optional[str]
    Publisher: Optional[str]
    Sku: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GalleryImageReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GalleryImageReference"]:
        if not json_data:
            return None
        return cls(
            Offer=json_data.get("Offer"),
            Publisher=json_data.get("Publisher"),
            Sku=json_data.get("Sku"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GalleryImageReference = GalleryImageReference


@dataclass
class InboundNatRule:
    BackendPort: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InboundNatRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InboundNatRule"]:
        if not json_data:
            return None
        return cls(
            BackendPort=json_data.get("BackendPort"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InboundNatRule = InboundNatRule


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


