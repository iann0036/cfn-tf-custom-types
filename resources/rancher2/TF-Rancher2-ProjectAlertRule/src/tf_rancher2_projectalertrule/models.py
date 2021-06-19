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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    GroupId: Optional[str]
    GroupIntervalSeconds: Optional[float]
    GroupWaitSeconds: Optional[float]
    Id: Optional[str]
    Inherited: Optional[bool]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    ProjectId: Optional[str]
    RepeatIntervalSeconds: Optional[float]
    Severity: Optional[str]
    MetricRule: Optional[Sequence["_MetricRuleDefinition"]]
    PodRule: Optional[Sequence["_PodRuleDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    WorkloadRule: Optional[Sequence["_WorkloadRuleDefinition"]]

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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            GroupId=json_data.get("GroupId"),
            GroupIntervalSeconds=json_data.get("GroupIntervalSeconds"),
            GroupWaitSeconds=json_data.get("GroupWaitSeconds"),
            Id=json_data.get("Id"),
            Inherited=json_data.get("Inherited"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            ProjectId=json_data.get("ProjectId"),
            RepeatIntervalSeconds=json_data.get("RepeatIntervalSeconds"),
            Severity=json_data.get("Severity"),
            MetricRule=deserialize_list(json_data.get("MetricRule"), MetricRuleDefinition),
            PodRule=deserialize_list(json_data.get("PodRule"), PodRuleDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            WorkloadRule=deserialize_list(json_data.get("WorkloadRule"), WorkloadRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


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
class MetricRuleDefinition(BaseModel):
    Comparison: Optional[str]
    Description: Optional[str]
    Duration: Optional[str]
    Expression: Optional[str]
    ThresholdValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MetricRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Description=json_data.get("Description"),
            Duration=json_data.get("Duration"),
            Expression=json_data.get("Expression"),
            ThresholdValue=json_data.get("ThresholdValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricRuleDefinition = MetricRuleDefinition


@dataclass
class PodRuleDefinition(BaseModel):
    Condition: Optional[str]
    PodId: Optional[str]
    RestartIntervalSeconds: Optional[float]
    RestartTimes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PodRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PodRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            PodId=json_data.get("PodId"),
            RestartIntervalSeconds=json_data.get("RestartIntervalSeconds"),
            RestartTimes=json_data.get("RestartTimes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PodRuleDefinition = PodRuleDefinition


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


@dataclass
class WorkloadRuleDefinition(BaseModel):
    AvailablePercentage: Optional[float]
    Selector: Optional[Sequence["_SelectorDefinition"]]
    WorkloadId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkloadRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkloadRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailablePercentage=json_data.get("AvailablePercentage"),
            Selector=deserialize_list(json_data.get("Selector"), SelectorDefinition),
            WorkloadId=json_data.get("WorkloadId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkloadRuleDefinition = WorkloadRuleDefinition


@dataclass
class SelectorDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelectorDefinition = SelectorDefinition


