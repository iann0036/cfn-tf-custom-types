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
    Id: Optional[str]
    InstanceGroupManager: Optional[str]
    MinimalAction: Optional[str]
    MostDisruptiveAllowedAction: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    RemoveInstanceStateOnDestroy: Optional[bool]
    Zone: Optional[str]
    PreservedState: Optional[Sequence["_PreservedStateDefinition"]]
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
            Id=json_data.get("Id"),
            InstanceGroupManager=json_data.get("InstanceGroupManager"),
            MinimalAction=json_data.get("MinimalAction"),
            MostDisruptiveAllowedAction=json_data.get("MostDisruptiveAllowedAction"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            RemoveInstanceStateOnDestroy=json_data.get("RemoveInstanceStateOnDestroy"),
            Zone=json_data.get("Zone"),
            PreservedState=deserialize_list(json_data.get("PreservedState"), PreservedStateDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PreservedStateDefinition(BaseModel):
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Disk: Optional[Sequence["_DiskDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PreservedStateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PreservedStateDefinition"]:
        if not json_data:
            return None
        return cls(
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Disk=deserialize_list(json_data.get("Disk"), DiskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PreservedStateDefinition = PreservedStateDefinition


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class DiskDefinition(BaseModel):
    DeleteRule: Optional[str]
    DeviceName: Optional[str]
    Mode: Optional[str]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteRule=json_data.get("DeleteRule"),
            DeviceName=json_data.get("DeviceName"),
            Mode=json_data.get("Mode"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskDefinition = DiskDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


