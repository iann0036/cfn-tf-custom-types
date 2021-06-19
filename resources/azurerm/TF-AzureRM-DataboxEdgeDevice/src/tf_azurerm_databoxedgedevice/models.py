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
    DeviceProperties: Optional[Sequence["_DevicePropertiesDefinition"]]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    SkuName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
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
            DeviceProperties=deserialize_list(json_data.get("DeviceProperties"), DevicePropertiesDefinition),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SkuName=json_data.get("SkuName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DevicePropertiesDefinition(BaseModel):
    Capacity: Optional[float]
    ConfiguredRoleTypes: Optional[Sequence[str]]
    Culture: Optional[str]
    HcsVersion: Optional[str]
    Model: Optional[str]
    NodeCount: Optional[float]
    SerialNumber: Optional[str]
    SoftwareVersion: Optional[str]
    Status: Optional[str]
    TimeZone: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DevicePropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DevicePropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Capacity=json_data.get("Capacity"),
            ConfiguredRoleTypes=json_data.get("ConfiguredRoleTypes"),
            Culture=json_data.get("Culture"),
            HcsVersion=json_data.get("HcsVersion"),
            Model=json_data.get("Model"),
            NodeCount=json_data.get("NodeCount"),
            SerialNumber=json_data.get("SerialNumber"),
            SoftwareVersion=json_data.get("SoftwareVersion"),
            Status=json_data.get("Status"),
            TimeZone=json_data.get("TimeZone"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DevicePropertiesDefinition = DevicePropertiesDefinition


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


