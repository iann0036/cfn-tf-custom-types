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
    CloneDriveId: Optional[str]
    Id: Optional[str]
    Media: Optional[str]
    MountedOn: Optional[Sequence["_MountedOnDefinition"]]
    Name: Optional[str]
    ResourceUri: Optional[str]
    Size: Optional[float]
    Status: Optional[str]
    StorageType: Optional[str]
    Tags: Optional[Sequence[str]]
    Uuid: Optional[str]
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
            CloneDriveId=json_data.get("CloneDriveId"),
            Id=json_data.get("Id"),
            Media=json_data.get("Media"),
            MountedOn=deserialize_list(json_data.get("MountedOn"), MountedOnDefinition),
            Name=json_data.get("Name"),
            ResourceUri=json_data.get("ResourceUri"),
            Size=json_data.get("Size"),
            Status=json_data.get("Status"),
            StorageType=json_data.get("StorageType"),
            Tags=json_data.get("Tags"),
            Uuid=json_data.get("Uuid"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MountedOnDefinition(BaseModel):
    ResourceUri: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MountedOnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MountedOnDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceUri=json_data.get("ResourceUri"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MountedOnDefinition = MountedOnDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


