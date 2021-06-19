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
    AllocationPolicy: Optional[str]
    DeviceProvisioningHostName: Optional[str]
    Id: Optional[str]
    IdScope: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    ServiceOperationsHostName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    LinkedHub: Optional[Sequence["_LinkedHubDefinition"]]
    Sku: Optional[Sequence["_SkuDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AllocationPolicy=json_data.get("AllocationPolicy"),
            DeviceProvisioningHostName=json_data.get("DeviceProvisioningHostName"),
            Id=json_data.get("Id"),
            IdScope=json_data.get("IdScope"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ServiceOperationsHostName=json_data.get("ServiceOperationsHostName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            LinkedHub=deserialize_list(json_data.get("LinkedHub"), LinkedHubDefinition),
            Sku=deserialize_list(json_data.get("Sku"), SkuDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class LinkedHubDefinition(BaseModel):
    AllocationWeight: Optional[float]
    ApplyAllocationPolicy: Optional[bool]
    ConnectionString: Optional[str]
    Location: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LinkedHubDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinkedHubDefinition"]:
        if not json_data:
            return None
        return cls(
            AllocationWeight=json_data.get("AllocationWeight"),
            ApplyAllocationPolicy=json_data.get("ApplyAllocationPolicy"),
            ConnectionString=json_data.get("ConnectionString"),
            Location=json_data.get("Location"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinkedHubDefinition = LinkedHubDefinition


@dataclass
class SkuDefinition(BaseModel):
    Capacity: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SkuDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SkuDefinition"]:
        if not json_data:
            return None
        return cls(
            Capacity=json_data.get("Capacity"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SkuDefinition = SkuDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


