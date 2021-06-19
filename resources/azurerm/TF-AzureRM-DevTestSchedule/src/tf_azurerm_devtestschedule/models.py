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
    LabName: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TaskType: Optional[str]
    TimeZoneId: Optional[str]
    DailyRecurrence: Optional[Sequence["_DailyRecurrenceDefinition"]]
    HourlyRecurrence: Optional[Sequence["_HourlyRecurrenceDefinition"]]
    NotificationSettings: Optional[Sequence["_NotificationSettingsDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    WeeklyRecurrence: Optional[Sequence["_WeeklyRecurrenceDefinition"]]

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
            LabName=json_data.get("LabName"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TaskType=json_data.get("TaskType"),
            TimeZoneId=json_data.get("TimeZoneId"),
            DailyRecurrence=deserialize_list(json_data.get("DailyRecurrence"), DailyRecurrenceDefinition),
            HourlyRecurrence=deserialize_list(json_data.get("HourlyRecurrence"), HourlyRecurrenceDefinition),
            NotificationSettings=deserialize_list(json_data.get("NotificationSettings"), NotificationSettingsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            WeeklyRecurrence=deserialize_list(json_data.get("WeeklyRecurrence"), WeeklyRecurrenceDefinition),
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
class DailyRecurrenceDefinition(BaseModel):
    Time: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DailyRecurrenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DailyRecurrenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Time=json_data.get("Time"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DailyRecurrenceDefinition = DailyRecurrenceDefinition


@dataclass
class HourlyRecurrenceDefinition(BaseModel):
    Minute: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HourlyRecurrenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HourlyRecurrenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Minute=json_data.get("Minute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HourlyRecurrenceDefinition = HourlyRecurrenceDefinition


@dataclass
class NotificationSettingsDefinition(BaseModel):
    Status: Optional[str]
    TimeInMinutes: Optional[float]
    WebhookUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            TimeInMinutes=json_data.get("TimeInMinutes"),
            WebhookUrl=json_data.get("WebhookUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationSettingsDefinition = NotificationSettingsDefinition


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


@dataclass
class WeeklyRecurrenceDefinition(BaseModel):
    Time: Optional[str]
    WeekDays: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_WeeklyRecurrenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeeklyRecurrenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Time=json_data.get("Time"),
            WeekDays=json_data.get("WeekDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeeklyRecurrenceDefinition = WeeklyRecurrenceDefinition


