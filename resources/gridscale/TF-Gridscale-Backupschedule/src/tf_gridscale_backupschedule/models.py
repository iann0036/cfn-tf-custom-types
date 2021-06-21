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
    Active: Optional[bool]
    ChangeTime: Optional[str]
    CreateTime: Optional[str]
    Id: Optional[str]
    KeepBackups: Optional[float]
    Name: Optional[str]
    NextRuntime: Optional[str]
    NextRuntimeComputed: Optional[str]
    RunInterval: Optional[float]
    Status: Optional[str]
    StorageBackups: Optional[Sequence["_StorageBackupsDefinition"]]
    StorageUuid: Optional[str]
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
            Active=json_data.get("Active"),
            ChangeTime=json_data.get("ChangeTime"),
            CreateTime=json_data.get("CreateTime"),
            Id=json_data.get("Id"),
            KeepBackups=json_data.get("KeepBackups"),
            Name=json_data.get("Name"),
            NextRuntime=json_data.get("NextRuntime"),
            NextRuntimeComputed=json_data.get("NextRuntimeComputed"),
            RunInterval=json_data.get("RunInterval"),
            Status=json_data.get("Status"),
            StorageBackups=deserialize_list(json_data.get("StorageBackups"), StorageBackupsDefinition),
            StorageUuid=json_data.get("StorageUuid"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class StorageBackupsDefinition(BaseModel):
    CreateTime: Optional[str]
    Name: Optional[str]
    ObjectUuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageBackupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageBackupsDefinition"]:
        if not json_data:
            return None
        return cls(
            CreateTime=json_data.get("CreateTime"),
            Name=json_data.get("Name"),
            ObjectUuid=json_data.get("ObjectUuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageBackupsDefinition = StorageBackupsDefinition


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

