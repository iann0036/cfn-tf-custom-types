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
    AllowClassicOperations: Optional[bool]
    BandwidthInMbps: Optional[float]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PeeringLocation: Optional[str]
    ResourceGroupName: Optional[str]
    ServiceKey: Optional[str]
    ServiceProviderName: Optional[str]
    ServiceProviderProvisioningState: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Sku: Optional[Sequence["_Sku"]]
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
            AllowClassicOperations=json_data.get("AllowClassicOperations"),
            BandwidthInMbps=json_data.get("BandwidthInMbps"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PeeringLocation=json_data.get("PeeringLocation"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ServiceKey=json_data.get("ServiceKey"),
            ServiceProviderName=json_data.get("ServiceProviderName"),
            ServiceProviderProvisioningState=json_data.get("ServiceProviderProvisioningState"),
            Tags=json_data.get("Tags"),
            Sku=json_data.get("Sku"),
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
class Sku:
    Family: Optional[str]
    Tier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Sku"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sku"]:
        if not json_data:
            return None
        return cls(
            Family=json_data.get("Family"),
            Tier=json_data.get("Tier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sku = Sku


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


