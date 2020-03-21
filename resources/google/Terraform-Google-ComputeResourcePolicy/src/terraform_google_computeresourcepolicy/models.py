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
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    SelfLink: Optional[str]
    SnapshotSchedulePolicy: Optional[Sequence["_SnapshotSchedulePolicy"]]
    Timeouts: Optional["_Timeouts"]
    RetentionPolicy: Optional[Sequence["_RetentionPolicy"]]
    Schedule: Optional[Sequence["_Schedule"]]
    SnapshotProperties: Optional[Sequence["_SnapshotProperties"]]
    DailySchedule: Optional[Sequence["_DailySchedule"]]
    HourlySchedule: Optional[Sequence["_HourlySchedule"]]
    WeeklySchedule: Optional[Sequence["_WeeklySchedule"]]
    DayOfWeeks: Optional[Sequence["_DayOfWeeks"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            SelfLink=json_data.get("SelfLink"),
            SnapshotSchedulePolicy=json_data.get("SnapshotSchedulePolicy"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            RetentionPolicy=json_data.get("RetentionPolicy"),
            Schedule=json_data.get("Schedule"),
            SnapshotProperties=json_data.get("SnapshotProperties"),
            DailySchedule=json_data.get("DailySchedule"),
            HourlySchedule=json_data.get("HourlySchedule"),
            WeeklySchedule=json_data.get("WeeklySchedule"),
            DayOfWeeks=json_data.get("DayOfWeeks"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SnapshotSchedulePolicy:
    RetentionPolicy: Optional[Sequence["_RetentionPolicy"]]
    Schedule: Optional[Sequence["_Schedule"]]
    SnapshotProperties: Optional[Sequence["_SnapshotProperties"]]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotSchedulePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotSchedulePolicy"]:
        if not json_data:
            return None
        return cls(
            RetentionPolicy=json_data.get("RetentionPolicy"),
            Schedule=json_data.get("Schedule"),
            SnapshotProperties=json_data.get("SnapshotProperties"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotSchedulePolicy = SnapshotSchedulePolicy


@dataclass
class RetentionPolicy:
    MaxRetentionDays: Optional[float]
    OnSourceDiskDelete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionPolicy"]:
        if not json_data:
            return None
        return cls(
            MaxRetentionDays=json_data.get("MaxRetentionDays"),
            OnSourceDiskDelete=json_data.get("OnSourceDiskDelete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionPolicy = RetentionPolicy


@dataclass
class Schedule:
    DailySchedule: Optional[Sequence["_DailySchedule"]]
    HourlySchedule: Optional[Sequence["_HourlySchedule"]]
    WeeklySchedule: Optional[Sequence["_WeeklySchedule"]]

    @classmethod
    def _deserialize(
        cls: Type["_Schedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Schedule"]:
        if not json_data:
            return None
        return cls(
            DailySchedule=json_data.get("DailySchedule"),
            HourlySchedule=json_data.get("HourlySchedule"),
            WeeklySchedule=json_data.get("WeeklySchedule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Schedule = Schedule


@dataclass
class DailySchedule:
    DaysInCycle: Optional[float]
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DailySchedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DailySchedule"]:
        if not json_data:
            return None
        return cls(
            DaysInCycle=json_data.get("DaysInCycle"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DailySchedule = DailySchedule


@dataclass
class HourlySchedule:
    HoursInCycle: Optional[float]
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HourlySchedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HourlySchedule"]:
        if not json_data:
            return None
        return cls(
            HoursInCycle=json_data.get("HoursInCycle"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HourlySchedule = HourlySchedule


@dataclass
class WeeklySchedule:
    DayOfWeeks: Optional[Sequence["_DayOfWeeks"]]

    @classmethod
    def _deserialize(
        cls: Type["_WeeklySchedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeeklySchedule"]:
        if not json_data:
            return None
        return cls(
            DayOfWeeks=json_data.get("DayOfWeeks"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeeklySchedule = WeeklySchedule


@dataclass
class DayOfWeeks:
    Day: Optional[str]
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DayOfWeeks"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DayOfWeeks"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DayOfWeeks = DayOfWeeks


@dataclass
class SnapshotProperties:
    GuestFlush: Optional[bool]
    Labels: Optional[Sequence["_Labels"]]
    StorageLocations: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotProperties"]:
        if not json_data:
            return None
        return cls(
            GuestFlush=json_data.get("GuestFlush"),
            Labels=json_data.get("Labels"),
            StorageLocations=json_data.get("StorageLocations"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotProperties = SnapshotProperties


@dataclass
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


