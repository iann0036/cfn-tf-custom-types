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
    Name: Optional[str]
    NodeCount: Optional[float]
    NodeSize: Optional[str]
    NodeSizeFamily: Optional[str]
    SparkEventsFolder: Optional[str]
    SparkLogFolder: Optional[str]
    SparkVersion: Optional[str]
    SynapseWorkspaceId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    AutoPause: Optional[Sequence["_AutoPauseDefinition"]]
    AutoScale: Optional[Sequence["_AutoScaleDefinition"]]
    LibraryRequirement: Optional[Sequence["_LibraryRequirementDefinition"]]
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
            Name=json_data.get("Name"),
            NodeCount=json_data.get("NodeCount"),
            NodeSize=json_data.get("NodeSize"),
            NodeSizeFamily=json_data.get("NodeSizeFamily"),
            SparkEventsFolder=json_data.get("SparkEventsFolder"),
            SparkLogFolder=json_data.get("SparkLogFolder"),
            SparkVersion=json_data.get("SparkVersion"),
            SynapseWorkspaceId=json_data.get("SynapseWorkspaceId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            AutoPause=deserialize_list(json_data.get("AutoPause"), AutoPauseDefinition),
            AutoScale=deserialize_list(json_data.get("AutoScale"), AutoScaleDefinition),
            LibraryRequirement=deserialize_list(json_data.get("LibraryRequirement"), LibraryRequirementDefinition),
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
class AutoPauseDefinition(BaseModel):
    DelayInMinutes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoPauseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoPauseDefinition"]:
        if not json_data:
            return None
        return cls(
            DelayInMinutes=json_data.get("DelayInMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoPauseDefinition = AutoPauseDefinition


@dataclass
class AutoScaleDefinition(BaseModel):
    MaxNodeCount: Optional[float]
    MinNodeCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScaleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScaleDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxNodeCount=json_data.get("MaxNodeCount"),
            MinNodeCount=json_data.get("MinNodeCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScaleDefinition = AutoScaleDefinition


@dataclass
class LibraryRequirementDefinition(BaseModel):
    Content: Optional[str]
    Filename: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LibraryRequirementDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LibraryRequirementDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Filename=json_data.get("Filename"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LibraryRequirementDefinition = LibraryRequirementDefinition


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


