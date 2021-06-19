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
    BdsInstanceId: Optional[str]
    ClusterAdminPassword: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    IsEnabled: Optional[bool]
    NodeType: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    Policy: Optional[Sequence["_PolicyDefinition"]]
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
            BdsInstanceId=json_data.get("BdsInstanceId"),
            ClusterAdminPassword=json_data.get("ClusterAdminPassword"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            IsEnabled=json_data.get("IsEnabled"),
            NodeType=json_data.get("NodeType"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            Policy=deserialize_list(json_data.get("Policy"), PolicyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PolicyDefinition(BaseModel):
    PolicyType: Optional[str]
    Rules: Optional[Sequence["_RulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            PolicyType=json_data.get("PolicyType"),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyDefinition = PolicyDefinition


@dataclass
class RulesDefinition(BaseModel):
    Action: Optional[str]
    Metric: Optional[Sequence["_MetricDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Metric=deserialize_list(json_data.get("Metric"), MetricDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


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
    DurationInMinutes: Optional[float]
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
            DurationInMinutes=json_data.get("DurationInMinutes"),
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


