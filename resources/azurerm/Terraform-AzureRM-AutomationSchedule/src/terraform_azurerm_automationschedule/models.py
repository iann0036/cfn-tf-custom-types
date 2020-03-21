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
    AutomationAccountName: Optional[str]
    Description: Optional[str]
    ExpiryTime: Optional[str]
    Frequency: Optional[str]
    Interval: Optional[float]
    MonthDays: Optional[Sequence[float]]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    StartTime: Optional[str]
    Timezone: Optional[str]
    WeekDays: Optional[Sequence[str]]
    MonthlyOccurrence: Optional[Sequence["_MonthlyOccurrence"]]
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
            AutomationAccountName=json_data.get("AutomationAccountName"),
            Description=json_data.get("Description"),
            ExpiryTime=json_data.get("ExpiryTime"),
            Frequency=json_data.get("Frequency"),
            Interval=json_data.get("Interval"),
            MonthDays=json_data.get("MonthDays"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            StartTime=json_data.get("StartTime"),
            Timezone=json_data.get("Timezone"),
            WeekDays=json_data.get("WeekDays"),
            MonthlyOccurrence=json_data.get("MonthlyOccurrence"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MonthlyOccurrence:
    Day: Optional[str]
    Occurrence: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MonthlyOccurrence"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonthlyOccurrence"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            Occurrence=json_data.get("Occurrence"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonthlyOccurrence = MonthlyOccurrence


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


