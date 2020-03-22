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
    Active: Optional[bool]
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
    Recurrence: Optional[Sequence["_Recurrence"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Active=json_data.get("Active"),
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
            Recurrence=json_data.get("Recurrence"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Recurrence:
    Period: Optional[float]
    Type: Optional[str]
    UntilDate: Optional[float]
    UntilOccurrences: Optional[float]
    WeekDays: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Recurrence"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Recurrence"]:
        if not json_data:
            return None
        return cls(
            Period=json_data.get("Period"),
            Type=json_data.get("Type"),
            UntilDate=json_data.get("UntilDate"),
            UntilOccurrences=json_data.get("UntilOccurrences"),
            WeekDays=json_data.get("WeekDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Recurrence = Recurrence


