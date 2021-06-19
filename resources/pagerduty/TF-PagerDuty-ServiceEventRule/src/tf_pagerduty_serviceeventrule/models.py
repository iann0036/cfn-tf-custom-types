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
    Disabled: Optional[bool]
    Id: Optional[str]
    Position: Optional[float]
    Service: Optional[str]
    Actions: Optional[Sequence["_ActionsDefinition"]]
    Conditions: Optional[Sequence["_ConditionsDefinition"]]
    TimeFrame: Optional[Sequence["_TimeFrameDefinition"]]
    Variable: Optional[Sequence["_VariableDefinition"]]

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
            Disabled=json_data.get("Disabled"),
            Id=json_data.get("Id"),
            Position=json_data.get("Position"),
            Service=json_data.get("Service"),
            Actions=deserialize_list(json_data.get("Actions"), ActionsDefinition),
            Conditions=deserialize_list(json_data.get("Conditions"), ConditionsDefinition),
            TimeFrame=deserialize_list(json_data.get("TimeFrame"), TimeFrameDefinition),
            Variable=deserialize_list(json_data.get("Variable"), VariableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ActionsDefinition(BaseModel):
    Annotate: Optional[Sequence["_AnnotateDefinition"]]
    EventAction: Optional[Sequence["_EventActionDefinition"]]
    Extractions: Optional[Sequence["_ExtractionsDefinition"]]
    Priority: Optional[Sequence["_PriorityDefinition"]]
    Severity: Optional[Sequence["_SeverityDefinition"]]
    Suppress: Optional[Sequence["_SuppressDefinition"]]
    Suspend: Optional[Sequence["_SuspendDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Annotate=deserialize_list(json_data.get("Annotate"), AnnotateDefinition),
            EventAction=deserialize_list(json_data.get("EventAction"), EventActionDefinition),
            Extractions=deserialize_list(json_data.get("Extractions"), ExtractionsDefinition),
            Priority=deserialize_list(json_data.get("Priority"), PriorityDefinition),
            Severity=deserialize_list(json_data.get("Severity"), SeverityDefinition),
            Suppress=deserialize_list(json_data.get("Suppress"), SuppressDefinition),
            Suspend=deserialize_list(json_data.get("Suspend"), SuspendDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionsDefinition = ActionsDefinition


@dataclass
class AnnotateDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotateDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotateDefinition = AnnotateDefinition


@dataclass
class EventActionDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventActionDefinition = EventActionDefinition


@dataclass
class ExtractionsDefinition(BaseModel):
    Regex: Optional[str]
    Source: Optional[str]
    Target: Optional[str]
    Template: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtractionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtractionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Regex=json_data.get("Regex"),
            Source=json_data.get("Source"),
            Target=json_data.get("Target"),
            Template=json_data.get("Template"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtractionsDefinition = ExtractionsDefinition


@dataclass
class PriorityDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PriorityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PriorityDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PriorityDefinition = PriorityDefinition


@dataclass
class SeverityDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SeverityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeverityDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeverityDefinition = SeverityDefinition


@dataclass
class SuppressDefinition(BaseModel):
    ThresholdTimeAmount: Optional[float]
    ThresholdTimeUnit: Optional[str]
    ThresholdValue: Optional[float]
    Value: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SuppressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SuppressDefinition"]:
        if not json_data:
            return None
        return cls(
            ThresholdTimeAmount=json_data.get("ThresholdTimeAmount"),
            ThresholdTimeUnit=json_data.get("ThresholdTimeUnit"),
            ThresholdValue=json_data.get("ThresholdValue"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SuppressDefinition = SuppressDefinition


@dataclass
class SuspendDefinition(BaseModel):
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SuspendDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SuspendDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SuspendDefinition = SuspendDefinition


@dataclass
class ConditionsDefinition(BaseModel):
    Operator: Optional[str]
    Subconditions: Optional[Sequence["_SubconditionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Subconditions=deserialize_list(json_data.get("Subconditions"), SubconditionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionsDefinition = ConditionsDefinition


@dataclass
class SubconditionsDefinition(BaseModel):
    Operator: Optional[str]
    Parameter: Optional[Sequence["_ParameterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubconditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubconditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Parameter=deserialize_list(json_data.get("Parameter"), ParameterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubconditionsDefinition = SubconditionsDefinition


@dataclass
class ParameterDefinition(BaseModel):
    Path: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterDefinition = ParameterDefinition


@dataclass
class TimeFrameDefinition(BaseModel):
    ActiveBetween: Optional[Sequence["_ActiveBetweenDefinition"]]
    ScheduledWeekly: Optional[Sequence["_ScheduledWeeklyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TimeFrameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeFrameDefinition"]:
        if not json_data:
            return None
        return cls(
            ActiveBetween=deserialize_list(json_data.get("ActiveBetween"), ActiveBetweenDefinition),
            ScheduledWeekly=deserialize_list(json_data.get("ScheduledWeekly"), ScheduledWeeklyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeFrameDefinition = TimeFrameDefinition


@dataclass
class ActiveBetweenDefinition(BaseModel):
    EndTime: Optional[float]
    StartTime: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ActiveBetweenDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActiveBetweenDefinition"]:
        if not json_data:
            return None
        return cls(
            EndTime=json_data.get("EndTime"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActiveBetweenDefinition = ActiveBetweenDefinition


@dataclass
class ScheduledWeeklyDefinition(BaseModel):
    Duration: Optional[float]
    StartTime: Optional[float]
    Timezone: Optional[str]
    Weekdays: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduledWeeklyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledWeeklyDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            StartTime=json_data.get("StartTime"),
            Timezone=json_data.get("Timezone"),
            Weekdays=json_data.get("Weekdays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledWeeklyDefinition = ScheduledWeeklyDefinition


@dataclass
class VariableDefinition(BaseModel):
    Name: Optional[str]
    Type: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VariableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VariableDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VariableDefinition = VariableDefinition


@dataclass
class ParametersDefinition(BaseModel):
    Path: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


