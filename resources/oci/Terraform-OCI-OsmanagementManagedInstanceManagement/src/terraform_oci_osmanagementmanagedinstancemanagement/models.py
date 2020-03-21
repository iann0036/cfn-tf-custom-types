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
    CompartmentId: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    LastBoot: Optional[str]
    LastCheckin: Optional[str]
    ManagedInstanceId: Optional[str]
    OsKernelVersion: Optional[str]
    OsName: Optional[str]
    OsVersion: Optional[str]
    Status: Optional[str]
    UpdatesAvailable: Optional[float]
    ChildSoftwareSources: Optional[Sequence["_ChildSoftwareSources"]]
    ManagedInstanceGroups: Optional[Sequence["_ManagedInstanceGroups"]]
    ParentSoftwareSource: Optional[Sequence["_ParentSoftwareSource"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            LastBoot=json_data.get("LastBoot"),
            LastCheckin=json_data.get("LastCheckin"),
            ManagedInstanceId=json_data.get("ManagedInstanceId"),
            OsKernelVersion=json_data.get("OsKernelVersion"),
            OsName=json_data.get("OsName"),
            OsVersion=json_data.get("OsVersion"),
            Status=json_data.get("Status"),
            UpdatesAvailable=json_data.get("UpdatesAvailable"),
            ChildSoftwareSources=json_data.get("ChildSoftwareSources"),
            ManagedInstanceGroups=json_data.get("ManagedInstanceGroups"),
            ParentSoftwareSource=json_data.get("ParentSoftwareSource"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ChildSoftwareSources:
    Id: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ChildSoftwareSources"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChildSoftwareSources"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChildSoftwareSources = ChildSoftwareSources


@dataclass
class ManagedInstanceGroups:
    DisplayName: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedInstanceGroups"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedInstanceGroups"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedInstanceGroups = ManagedInstanceGroups


@dataclass
class ParentSoftwareSource:
    Id: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParentSoftwareSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParentSoftwareSource"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParentSoftwareSource = ParentSoftwareSource


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


