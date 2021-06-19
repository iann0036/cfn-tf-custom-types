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
    Description: Optional[str]
    ExpiryTime: Optional[str]
    Frequency: Optional[str]
    Id: Optional[str]
    Interval: Optional[float]
    MonthDays: Optional[Sequence[float]]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    StartTime: Optional[str]
    Timezone: Optional[str]
    WeekDays: Optional[Sequence[str]]
    MonthlyOccurrence: Optional[Sequence["_MonthlyOccurrenceDefinition"]]
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
            Description=json_data.get("Description"),
            ExpiryTime=json_data.get("ExpiryTime"),
            Frequency=json_data.get("Frequency"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            MonthDays=json_data.get("MonthDays"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            StartTime=json_data.get("StartTime"),
            Timezone=json_data.get("Timezone"),
            WeekDays=json_data.get("WeekDays"),
            MonthlyOccurrence=deserialize_list(json_data.get("MonthlyOccurrence"), MonthlyOccurrenceDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MonthlyOccurrenceDefinition(BaseModel):
    Day: Optional[str]
    Occurrence: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MonthlyOccurrenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonthlyOccurrenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            Occurrence=json_data.get("Occurrence"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonthlyOccurrenceDefinition = MonthlyOccurrenceDefinition


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


