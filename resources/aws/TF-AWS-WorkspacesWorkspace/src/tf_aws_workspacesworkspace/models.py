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
    BundleId: Optional[str]
    ComputerName: Optional[str]
    DirectoryId: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[str]
    RootVolumeEncryptionEnabled: Optional[bool]
    State: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    UserName: Optional[str]
    UserVolumeEncryptionEnabled: Optional[bool]
    VolumeEncryptionKey: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]
    WorkspaceProperties: Optional[Sequence["_WorkspacePropertiesDefinition"]]

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
            BundleId=json_data.get("BundleId"),
            ComputerName=json_data.get("ComputerName"),
            DirectoryId=json_data.get("DirectoryId"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            RootVolumeEncryptionEnabled=json_data.get("RootVolumeEncryptionEnabled"),
            State=json_data.get("State"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            UserName=json_data.get("UserName"),
            UserVolumeEncryptionEnabled=json_data.get("UserVolumeEncryptionEnabled"),
            VolumeEncryptionKey=json_data.get("VolumeEncryptionKey"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            WorkspaceProperties=deserialize_list(json_data.get("WorkspaceProperties"), WorkspacePropertiesDefinition),
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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


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


@dataclass
class WorkspacePropertiesDefinition(BaseModel):
    ComputeTypeName: Optional[str]
    RootVolumeSizeGib: Optional[float]
    RunningMode: Optional[str]
    RunningModeAutoStopTimeoutInMinutes: Optional[float]
    UserVolumeSizeGib: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WorkspacePropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkspacePropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            ComputeTypeName=json_data.get("ComputeTypeName"),
            RootVolumeSizeGib=json_data.get("RootVolumeSizeGib"),
            RunningMode=json_data.get("RunningMode"),
            RunningModeAutoStopTimeoutInMinutes=json_data.get("RunningModeAutoStopTimeoutInMinutes"),
            UserVolumeSizeGib=json_data.get("UserVolumeSizeGib"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkspacePropertiesDefinition = WorkspacePropertiesDefinition


