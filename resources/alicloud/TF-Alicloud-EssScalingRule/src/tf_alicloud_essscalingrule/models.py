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
    AdjustmentType: Optional[str]
    AdjustmentValue: Optional[float]
    Ari: Optional[str]
    Cooldown: Optional[float]
    DisableScaleIn: Optional[bool]
    EstimatedInstanceWarmup: Optional[float]
    Id: Optional[str]
    MetricName: Optional[str]
    ScalingGroupId: Optional[str]
    ScalingRuleName: Optional[str]
    ScalingRuleType: Optional[str]
    TargetValue: Optional[float]
    StepAdjustment: Optional[Sequence["_StepAdjustmentDefinition"]]

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
            AdjustmentType=json_data.get("AdjustmentType"),
            AdjustmentValue=json_data.get("AdjustmentValue"),
            Ari=json_data.get("Ari"),
            Cooldown=json_data.get("Cooldown"),
            DisableScaleIn=json_data.get("DisableScaleIn"),
            EstimatedInstanceWarmup=json_data.get("EstimatedInstanceWarmup"),
            Id=json_data.get("Id"),
            MetricName=json_data.get("MetricName"),
            ScalingGroupId=json_data.get("ScalingGroupId"),
            ScalingRuleName=json_data.get("ScalingRuleName"),
            ScalingRuleType=json_data.get("ScalingRuleType"),
            TargetValue=json_data.get("TargetValue"),
            StepAdjustment=deserialize_list(json_data.get("StepAdjustment"), StepAdjustmentDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class StepAdjustmentDefinition(BaseModel):
    MetricIntervalLowerBound: Optional[str]
    MetricIntervalUpperBound: Optional[str]
    ScalingAdjustment: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StepAdjustmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepAdjustmentDefinition"]:
        if not json_data:
            return None
        return cls(
            MetricIntervalLowerBound=json_data.get("MetricIntervalLowerBound"),
            MetricIntervalUpperBound=json_data.get("MetricIntervalUpperBound"),
            ScalingAdjustment=json_data.get("ScalingAdjustment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepAdjustmentDefinition = StepAdjustmentDefinition


