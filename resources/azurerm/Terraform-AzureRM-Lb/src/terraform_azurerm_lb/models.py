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
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PrivateIpAddress: Optional[str]
    PrivateIpAddresses: Optional[Sequence[str]]
    ResourceGroupName: Optional[str]
    Sku: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    FrontendIpConfiguration: Optional[Sequence["_FrontendIpConfiguration"]]
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
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            PrivateIpAddresses=json_data.get("PrivateIpAddresses"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Sku=json_data.get("Sku"),
            Tags=json_data.get("Tags"),
            FrontendIpConfiguration=json_data.get("FrontendIpConfiguration"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class FrontendIpConfiguration:
    Name: Optional[str]
    PrivateIpAddress: Optional[str]
    PrivateIpAddressAllocation: Optional[str]
    PrivateIpAddressVersion: Optional[str]
    PublicIpAddressId: Optional[str]
    PublicIpPrefixId: Optional[str]
    SubnetId: Optional[str]
    Zones: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FrontendIpConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrontendIpConfiguration"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            PrivateIpAddressAllocation=json_data.get("PrivateIpAddressAllocation"),
            PrivateIpAddressVersion=json_data.get("PrivateIpAddressVersion"),
            PublicIpAddressId=json_data.get("PublicIpAddressId"),
            PublicIpPrefixId=json_data.get("PublicIpPrefixId"),
            SubnetId=json_data.get("SubnetId"),
            Zones=json_data.get("Zones"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrontendIpConfiguration = FrontendIpConfiguration


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


