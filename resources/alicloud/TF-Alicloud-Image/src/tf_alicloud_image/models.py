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
    Architecture: Optional[str]
    Description: Optional[str]
    Force: Optional[bool]
    Id: Optional[str]
    ImageName: Optional[str]
    InstanceId: Optional[str]
    Name: Optional[str]
    Platform: Optional[str]
    ResourceGroupId: Optional[str]
    SnapshotId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    DiskDeviceMapping: Optional[Sequence["_DiskDeviceMappingDefinition"]]
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
            Architecture=json_data.get("Architecture"),
            Description=json_data.get("Description"),
            Force=json_data.get("Force"),
            Id=json_data.get("Id"),
            ImageName=json_data.get("ImageName"),
            InstanceId=json_data.get("InstanceId"),
            Name=json_data.get("Name"),
            Platform=json_data.get("Platform"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            SnapshotId=json_data.get("SnapshotId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            DiskDeviceMapping=deserialize_list(json_data.get("DiskDeviceMapping"), DiskDeviceMappingDefinition),
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
class DiskDeviceMappingDefinition(BaseModel):
    Device: Optional[str]
    DiskType: Optional[str]
    Size: Optional[float]
    SnapshotId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskDeviceMappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskDeviceMappingDefinition"]:
        if not json_data:
            return None
        return cls(
            Device=json_data.get("Device"),
            DiskType=json_data.get("DiskType"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskDeviceMappingDefinition = DiskDeviceMappingDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


