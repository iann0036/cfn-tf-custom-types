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
    AllocationPolicy: Optional[str]
    DeviceProvisioningHostName: Optional[str]
    Id: Optional[str]
    IdScope: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    ServiceOperationsHostName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    LinkedHub: Optional[Sequence["_LinkedHub"]]
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
            AllocationPolicy=json_data.get("AllocationPolicy"),
            DeviceProvisioningHostName=json_data.get("DeviceProvisioningHostName"),
            Id=json_data.get("Id"),
            IdScope=json_data.get("IdScope"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ServiceOperationsHostName=json_data.get("ServiceOperationsHostName"),
            Tags=json_data.get("Tags"),
            LinkedHub=json_data.get("LinkedHub"),
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
class LinkedHub:
    AllocationWeight: Optional[float]
    ApplyAllocationPolicy: Optional[bool]
    ConnectionString: Optional[str]
    Location: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LinkedHub"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinkedHub"]:
        if not json_data:
            return None
        return cls(
            AllocationWeight=json_data.get("AllocationWeight"),
            ApplyAllocationPolicy=json_data.get("ApplyAllocationPolicy"),
            ConnectionString=json_data.get("ConnectionString"),
            Location=json_data.get("Location"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinkedHub = LinkedHub


@dataclass
class Sku:
    Capacity: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Sku"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sku"]:
        if not json_data:
            return None
        return cls(
            Capacity=json_data.get("Capacity"),
            Name=json_data.get("Name"),
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


