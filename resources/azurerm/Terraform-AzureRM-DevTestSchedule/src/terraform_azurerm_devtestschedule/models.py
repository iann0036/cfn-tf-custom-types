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
    Id: Optional[str]
    LabName: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TaskType: Optional[str]
    TimeZoneId: Optional[str]
    DailyRecurrence: Optional[Sequence["_DailyRecurrence"]]
    HourlyRecurrence: Optional[Sequence["_HourlyRecurrence"]]
    NotificationSettings: Optional[Sequence["_NotificationSettings"]]
    Timeouts: Optional["_Timeouts"]
    WeeklyRecurrence: Optional[Sequence["_WeeklyRecurrence"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            LabName=json_data.get("LabName"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            TaskType=json_data.get("TaskType"),
            TimeZoneId=json_data.get("TimeZoneId"),
            DailyRecurrence=json_data.get("DailyRecurrence"),
            HourlyRecurrence=json_data.get("HourlyRecurrence"),
            NotificationSettings=json_data.get("NotificationSettings"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            WeeklyRecurrence=json_data.get("WeeklyRecurrence"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class DailyRecurrence:
    Time: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DailyRecurrence"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DailyRecurrence"]:
        if not json_data:
            return None
        return cls(
            Time=json_data.get("Time"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DailyRecurrence = DailyRecurrence


@dataclass
class HourlyRecurrence:
    Minute: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HourlyRecurrence"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HourlyRecurrence"]:
        if not json_data:
            return None
        return cls(
            Minute=json_data.get("Minute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HourlyRecurrence = HourlyRecurrence


@dataclass
class NotificationSettings:
    Status: Optional[str]
    TimeInMinutes: Optional[float]
    WebhookUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationSettings"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            TimeInMinutes=json_data.get("TimeInMinutes"),
            WebhookUrl=json_data.get("WebhookUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationSettings = NotificationSettings


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


@dataclass
class WeeklyRecurrence:
    Time: Optional[str]
    WeekDays: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_WeeklyRecurrence"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeeklyRecurrence"]:
        if not json_data:
            return None
        return cls(
            Time=json_data.get("Time"),
            WeekDays=json_data.get("WeekDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeeklyRecurrence = WeeklyRecurrence


