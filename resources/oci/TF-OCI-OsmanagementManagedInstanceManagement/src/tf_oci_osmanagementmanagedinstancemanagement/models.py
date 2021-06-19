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
    CompartmentId: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    LastBoot: Optional[str]
    LastCheckin: Optional[str]
    ManagedInstanceId: Optional[str]
    OsKernelVersion: Optional[str]
    OsName: Optional[str]
    OsVersion: Optional[str]
    Status: Optional[str]
    UpdatesAvailable: Optional[float]
    ChildSoftwareSources: Optional[Sequence["_ChildSoftwareSourcesDefinition"]]
    ManagedInstanceGroups: Optional[Sequence["_ManagedInstanceGroupsDefinition"]]
    ParentSoftwareSource: Optional[Sequence["_ParentSoftwareSourceDefinition"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            LastBoot=json_data.get("LastBoot"),
            LastCheckin=json_data.get("LastCheckin"),
            ManagedInstanceId=json_data.get("ManagedInstanceId"),
            OsKernelVersion=json_data.get("OsKernelVersion"),
            OsName=json_data.get("OsName"),
            OsVersion=json_data.get("OsVersion"),
            Status=json_data.get("Status"),
            UpdatesAvailable=json_data.get("UpdatesAvailable"),
            ChildSoftwareSources=deserialize_list(json_data.get("ChildSoftwareSources"), ChildSoftwareSourcesDefinition),
            ManagedInstanceGroups=deserialize_list(json_data.get("ManagedInstanceGroups"), ManagedInstanceGroupsDefinition),
            ParentSoftwareSource=deserialize_list(json_data.get("ParentSoftwareSource"), ParentSoftwareSourceDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ChildSoftwareSourcesDefinition(BaseModel):
    Id: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ChildSoftwareSourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChildSoftwareSourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChildSoftwareSourcesDefinition = ChildSoftwareSourcesDefinition


@dataclass
class ManagedInstanceGroupsDefinition(BaseModel):
    DisplayName: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedInstanceGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedInstanceGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedInstanceGroupsDefinition = ManagedInstanceGroupsDefinition


@dataclass
class ParentSoftwareSourceDefinition(BaseModel):
    Id: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParentSoftwareSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParentSoftwareSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParentSoftwareSourceDefinition = ParentSoftwareSourceDefinition


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


