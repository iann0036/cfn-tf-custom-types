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
    Active: Optional[bool]
    ActiveChildId: Optional[float]
    Disabled: Optional[bool]
    End: Optional[float]
    EndDate: Optional[str]
    Id: Optional[str]
    Message: Optional[str]
    MonitorId: Optional[float]
    MonitorTags: Optional[Sequence[str]]
    Scope: Optional[Sequence[str]]
    Start: Optional[float]
    StartDate: Optional[str]
    Timezone: Optional[str]
    Recurrence: Optional[Sequence["_RecurrenceDefinition"]]

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
            Active=json_data.get("Active"),
            ActiveChildId=json_data.get("ActiveChildId"),
            Disabled=json_data.get("Disabled"),
            End=json_data.get("End"),
            EndDate=json_data.get("EndDate"),
            Id=json_data.get("Id"),
            Message=json_data.get("Message"),
            MonitorId=json_data.get("MonitorId"),
            MonitorTags=json_data.get("MonitorTags"),
            Scope=json_data.get("Scope"),
            Start=json_data.get("Start"),
            StartDate=json_data.get("StartDate"),
            Timezone=json_data.get("Timezone"),
            Recurrence=deserialize_list(json_data.get("Recurrence"), RecurrenceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RecurrenceDefinition(BaseModel):
    Period: Optional[float]
    Rrule: Optional[str]
    Type: Optional[str]
    UntilDate: Optional[float]
    UntilOccurrences: Optional[float]
    WeekDays: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RecurrenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecurrenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Period=json_data.get("Period"),
            Rrule=json_data.get("Rrule"),
            Type=json_data.get("Type"),
            UntilDate=json_data.get("UntilDate"),
            UntilOccurrences=json_data.get("UntilOccurrences"),
            WeekDays=json_data.get("WeekDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecurrenceDefinition = RecurrenceDefinition


