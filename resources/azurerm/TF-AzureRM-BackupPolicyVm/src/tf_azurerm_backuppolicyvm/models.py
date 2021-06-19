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
    InstantRestoreRetentionDays: Optional[float]
    Name: Optional[str]
    RecoveryVaultName: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Timezone: Optional[str]
    Backup: Optional[Sequence["_BackupDefinition"]]
    RetentionDaily: Optional[Sequence["_RetentionDailyDefinition"]]
    RetentionMonthly: Optional[Sequence["_RetentionMonthlyDefinition"]]
    RetentionWeekly: Optional[Sequence["_RetentionWeeklyDefinition"]]
    RetentionYearly: Optional[Sequence["_RetentionYearlyDefinition"]]
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
            InstantRestoreRetentionDays=json_data.get("InstantRestoreRetentionDays"),
            Name=json_data.get("Name"),
            RecoveryVaultName=json_data.get("RecoveryVaultName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Timezone=json_data.get("Timezone"),
            Backup=deserialize_list(json_data.get("Backup"), BackupDefinition),
            RetentionDaily=deserialize_list(json_data.get("RetentionDaily"), RetentionDailyDefinition),
            RetentionMonthly=deserialize_list(json_data.get("RetentionMonthly"), RetentionMonthlyDefinition),
            RetentionWeekly=deserialize_list(json_data.get("RetentionWeekly"), RetentionWeeklyDefinition),
            RetentionYearly=deserialize_list(json_data.get("RetentionYearly"), RetentionYearlyDefinition),
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
class BackupDefinition(BaseModel):
    Frequency: Optional[str]
    Time: Optional[str]
    Weekdays: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_BackupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupDefinition"]:
        if not json_data:
            return None
        return cls(
            Frequency=json_data.get("Frequency"),
            Time=json_data.get("Time"),
            Weekdays=json_data.get("Weekdays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupDefinition = BackupDefinition


@dataclass
class RetentionDailyDefinition(BaseModel):
    Count: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionDailyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionDailyDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionDailyDefinition = RetentionDailyDefinition


@dataclass
class RetentionMonthlyDefinition(BaseModel):
    Count: Optional[float]
    Weekdays: Optional[Sequence[str]]
    Weeks: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionMonthlyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionMonthlyDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Weekdays=json_data.get("Weekdays"),
            Weeks=json_data.get("Weeks"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionMonthlyDefinition = RetentionMonthlyDefinition


@dataclass
class RetentionWeeklyDefinition(BaseModel):
    Count: Optional[float]
    Weekdays: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionWeeklyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionWeeklyDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Weekdays=json_data.get("Weekdays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionWeeklyDefinition = RetentionWeeklyDefinition


@dataclass
class RetentionYearlyDefinition(BaseModel):
    Count: Optional[float]
    Months: Optional[Sequence[str]]
    Weekdays: Optional[Sequence[str]]
    Weeks: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionYearlyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionYearlyDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Months=json_data.get("Months"),
            Weekdays=json_data.get("Weekdays"),
            Weeks=json_data.get("Weeks"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionYearlyDefinition = RetentionYearlyDefinition


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


