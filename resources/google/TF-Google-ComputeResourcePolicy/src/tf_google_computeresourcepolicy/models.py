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
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    SelfLink: Optional[str]
    GroupPlacementPolicy: Optional[Sequence["_GroupPlacementPolicyDefinition"]]
    InstanceSchedulePolicy: Optional[Sequence["_InstanceSchedulePolicyDefinition"]]
    SnapshotSchedulePolicy: Optional[Sequence["_SnapshotSchedulePolicyDefinition"]]
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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            SelfLink=json_data.get("SelfLink"),
            GroupPlacementPolicy=deserialize_list(json_data.get("GroupPlacementPolicy"), GroupPlacementPolicyDefinition),
            InstanceSchedulePolicy=deserialize_list(json_data.get("InstanceSchedulePolicy"), InstanceSchedulePolicyDefinition),
            SnapshotSchedulePolicy=deserialize_list(json_data.get("SnapshotSchedulePolicy"), SnapshotSchedulePolicyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GroupPlacementPolicyDefinition(BaseModel):
    AvailabilityDomainCount: Optional[float]
    Collocation: Optional[str]
    VmCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_GroupPlacementPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupPlacementPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityDomainCount=json_data.get("AvailabilityDomainCount"),
            Collocation=json_data.get("Collocation"),
            VmCount=json_data.get("VmCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupPlacementPolicyDefinition = GroupPlacementPolicyDefinition


@dataclass
class InstanceSchedulePolicyDefinition(BaseModel):
    ExpirationTime: Optional[str]
    StartTime: Optional[str]
    TimeZone: Optional[str]
    VmStartSchedule: Optional[Sequence["_VmStartScheduleDefinition"]]
    VmStopSchedule: Optional[Sequence["_VmStopScheduleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceSchedulePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceSchedulePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            ExpirationTime=json_data.get("ExpirationTime"),
            StartTime=json_data.get("StartTime"),
            TimeZone=json_data.get("TimeZone"),
            VmStartSchedule=deserialize_list(json_data.get("VmStartSchedule"), VmStartScheduleDefinition),
            VmStopSchedule=deserialize_list(json_data.get("VmStopSchedule"), VmStopScheduleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceSchedulePolicyDefinition = InstanceSchedulePolicyDefinition


@dataclass
class VmStartScheduleDefinition(BaseModel):
    Schedule: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VmStartScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VmStartScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            Schedule=json_data.get("Schedule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VmStartScheduleDefinition = VmStartScheduleDefinition


@dataclass
class VmStopScheduleDefinition(BaseModel):
    Schedule: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VmStopScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VmStopScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            Schedule=json_data.get("Schedule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VmStopScheduleDefinition = VmStopScheduleDefinition


@dataclass
class SnapshotSchedulePolicyDefinition(BaseModel):
    RetentionPolicy: Optional[Sequence["_RetentionPolicyDefinition"]]
    Schedule: Optional[Sequence["_ScheduleDefinition"]]
    SnapshotProperties: Optional[Sequence["_SnapshotPropertiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotSchedulePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotSchedulePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            RetentionPolicy=deserialize_list(json_data.get("RetentionPolicy"), RetentionPolicyDefinition),
            Schedule=deserialize_list(json_data.get("Schedule"), ScheduleDefinition),
            SnapshotProperties=deserialize_list(json_data.get("SnapshotProperties"), SnapshotPropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotSchedulePolicyDefinition = SnapshotSchedulePolicyDefinition


@dataclass
class RetentionPolicyDefinition(BaseModel):
    MaxRetentionDays: Optional[float]
    OnSourceDiskDelete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxRetentionDays=json_data.get("MaxRetentionDays"),
            OnSourceDiskDelete=json_data.get("OnSourceDiskDelete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionPolicyDefinition = RetentionPolicyDefinition


@dataclass
class ScheduleDefinition(BaseModel):
    DailySchedule: Optional[Sequence["_DailyScheduleDefinition"]]
    HourlySchedule: Optional[Sequence["_HourlyScheduleDefinition"]]
    WeeklySchedule: Optional[Sequence["_WeeklyScheduleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            DailySchedule=deserialize_list(json_data.get("DailySchedule"), DailyScheduleDefinition),
            HourlySchedule=deserialize_list(json_data.get("HourlySchedule"), HourlyScheduleDefinition),
            WeeklySchedule=deserialize_list(json_data.get("WeeklySchedule"), WeeklyScheduleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleDefinition = ScheduleDefinition


@dataclass
class DailyScheduleDefinition(BaseModel):
    DaysInCycle: Optional[float]
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DailyScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DailyScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            DaysInCycle=json_data.get("DaysInCycle"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DailyScheduleDefinition = DailyScheduleDefinition


@dataclass
class HourlyScheduleDefinition(BaseModel):
    HoursInCycle: Optional[float]
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HourlyScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HourlyScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            HoursInCycle=json_data.get("HoursInCycle"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HourlyScheduleDefinition = HourlyScheduleDefinition


@dataclass
class WeeklyScheduleDefinition(BaseModel):
    DayOfWeeks: Optional[Sequence["_DayOfWeeksDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WeeklyScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeeklyScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            DayOfWeeks=deserialize_list(json_data.get("DayOfWeeks"), DayOfWeeksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeeklyScheduleDefinition = WeeklyScheduleDefinition


@dataclass
class DayOfWeeksDefinition(BaseModel):
    Day: Optional[str]
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DayOfWeeksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DayOfWeeksDefinition"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DayOfWeeksDefinition = DayOfWeeksDefinition


@dataclass
class SnapshotPropertiesDefinition(BaseModel):
    GuestFlush: Optional[bool]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    StorageLocations: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            GuestFlush=json_data.get("GuestFlush"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            StorageLocations=json_data.get("StorageLocations"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotPropertiesDefinition = SnapshotPropertiesDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


