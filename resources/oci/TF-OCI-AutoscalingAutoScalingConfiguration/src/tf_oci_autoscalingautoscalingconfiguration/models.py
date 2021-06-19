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
    CompartmentId: Optional[str]
    CoolDownInSeconds: Optional[float]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    IsEnabled: Optional[bool]
    MaxResourceCount: Optional[float]
    MinResourceCount: Optional[float]
    TimeCreated: Optional[str]
    AutoScalingResources: Optional[Sequence["_AutoScalingResourcesDefinition"]]
    Policies: Optional[Sequence["_PoliciesDefinition"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            CoolDownInSeconds=json_data.get("CoolDownInSeconds"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            IsEnabled=json_data.get("IsEnabled"),
            MaxResourceCount=json_data.get("MaxResourceCount"),
            MinResourceCount=json_data.get("MinResourceCount"),
            TimeCreated=json_data.get("TimeCreated"),
            AutoScalingResources=deserialize_list(json_data.get("AutoScalingResources"), AutoScalingResourcesDefinition),
            Policies=deserialize_list(json_data.get("Policies"), PoliciesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class AutoScalingResourcesDefinition(BaseModel):
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScalingResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScalingResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScalingResourcesDefinition = AutoScalingResourcesDefinition


@dataclass
class PoliciesDefinition(BaseModel):
    DisplayName: Optional[str]
    IsEnabled: Optional[bool]
    PolicyType: Optional[str]
    Capacity: Optional[Sequence["_CapacityDefinition"]]
    ExecutionSchedule: Optional[Sequence["_ExecutionScheduleDefinition"]]
    ResourceAction: Optional[Sequence["_ResourceActionDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            IsEnabled=json_data.get("IsEnabled"),
            PolicyType=json_data.get("PolicyType"),
            Capacity=deserialize_list(json_data.get("Capacity"), CapacityDefinition),
            ExecutionSchedule=deserialize_list(json_data.get("ExecutionSchedule"), ExecutionScheduleDefinition),
            ResourceAction=deserialize_list(json_data.get("ResourceAction"), ResourceActionDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PoliciesDefinition = PoliciesDefinition


@dataclass
class CapacityDefinition(BaseModel):
    Initial: Optional[float]
    Max: Optional[float]
    Min: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityDefinition"]:
        if not json_data:
            return None
        return cls(
            Initial=json_data.get("Initial"),
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityDefinition = CapacityDefinition


@dataclass
class ExecutionScheduleDefinition(BaseModel):
    Expression: Optional[str]
    Timezone: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExecutionScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExecutionScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Timezone=json_data.get("Timezone"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExecutionScheduleDefinition = ExecutionScheduleDefinition


@dataclass
class ResourceActionDefinition(BaseModel):
    Action: Optional[str]
    ActionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            ActionType=json_data.get("ActionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceActionDefinition = ResourceActionDefinition


@dataclass
class RulesDefinition(BaseModel):
    DisplayName: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    Metric: Optional[Sequence["_MetricDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            Metric=deserialize_list(json_data.get("Metric"), MetricDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class ActionDefinition(BaseModel):
    Type: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class MetricDefinition(BaseModel):
    MetricType: Optional[str]
    Threshold: Optional[Sequence["_ThresholdDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDefinition"]:
        if not json_data:
            return None
        return cls(
            MetricType=json_data.get("MetricType"),
            Threshold=deserialize_list(json_data.get("Threshold"), ThresholdDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDefinition = MetricDefinition


@dataclass
class ThresholdDefinition(BaseModel):
    Operator: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ThresholdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThresholdDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThresholdDefinition = ThresholdDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


