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
    AutomationAccountName: Optional[str]
    Content: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    JobSchedule: Optional[Sequence["_JobScheduleDefinition2"]]
    Location: Optional[str]
    LogProgress: Optional[bool]
    LogVerbose: Optional[bool]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    RunbookType: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    PublishContentLink: Optional[Sequence["_PublishContentLinkDefinition"]]
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
            AutomationAccountName=json_data.get("AutomationAccountName"),
            Content=json_data.get("Content"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            JobSchedule=deserialize_list(json_data.get("JobSchedule"), JobScheduleDefinition2),
            Location=json_data.get("Location"),
            LogProgress=json_data.get("LogProgress"),
            LogVerbose=json_data.get("LogVerbose"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RunbookType=json_data.get("RunbookType"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            PublishContentLink=deserialize_list(json_data.get("PublishContentLink"), PublishContentLinkDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class JobScheduleDefinition2(BaseModel):
    JobScheduleId: Optional[str]
    Parameters: Optional[Sequence["_JobScheduleDefinition"]]
    RunOn: Optional[str]
    ScheduleName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JobScheduleDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JobScheduleDefinition2"]:
        if not json_data:
            return None
        return cls(
            JobScheduleId=json_data.get("JobScheduleId"),
            Parameters=deserialize_list(json_data.get("Parameters"), JobScheduleDefinition),
            RunOn=json_data.get("RunOn"),
            ScheduleName=json_data.get("ScheduleName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JobScheduleDefinition2 = JobScheduleDefinition2


@dataclass
class JobScheduleDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JobScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JobScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JobScheduleDefinition = JobScheduleDefinition


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
class PublishContentLinkDefinition(BaseModel):
    Uri: Optional[str]
    Version: Optional[str]
    Hash: Optional[Sequence["_HashDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PublishContentLinkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublishContentLinkDefinition"]:
        if not json_data:
            return None
        return cls(
            Uri=json_data.get("Uri"),
            Version=json_data.get("Version"),
            Hash=deserialize_list(json_data.get("Hash"), HashDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublishContentLinkDefinition = PublishContentLinkDefinition


@dataclass
class HashDefinition(BaseModel):
    Algorithm: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HashDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HashDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HashDefinition = HashDefinition


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


