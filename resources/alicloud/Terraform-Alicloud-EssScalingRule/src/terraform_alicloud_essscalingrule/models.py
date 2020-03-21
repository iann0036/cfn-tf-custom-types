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
    AdjustmentType: Optional[str]
    AdjustmentValue: Optional[float]
    Ari: Optional[str]
    Cooldown: Optional[float]
    DisableScaleIn: Optional[bool]
    EstimatedInstanceWarmup: Optional[float]
    MetricName: Optional[str]
    ScalingGroupId: Optional[str]
    ScalingRuleName: Optional[str]
    ScalingRuleType: Optional[str]
    TargetValue: Optional[float]
    StepAdjustment: Optional[Sequence["_StepAdjustment"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdjustmentType=json_data.get("AdjustmentType"),
            AdjustmentValue=json_data.get("AdjustmentValue"),
            Ari=json_data.get("Ari"),
            Cooldown=json_data.get("Cooldown"),
            DisableScaleIn=json_data.get("DisableScaleIn"),
            EstimatedInstanceWarmup=json_data.get("EstimatedInstanceWarmup"),
            MetricName=json_data.get("MetricName"),
            ScalingGroupId=json_data.get("ScalingGroupId"),
            ScalingRuleName=json_data.get("ScalingRuleName"),
            ScalingRuleType=json_data.get("ScalingRuleType"),
            TargetValue=json_data.get("TargetValue"),
            StepAdjustment=json_data.get("StepAdjustment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class StepAdjustment:
    MetricIntervalLowerBound: Optional[str]
    MetricIntervalUpperBound: Optional[str]
    ScalingAdjustment: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StepAdjustment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepAdjustment"]:
        if not json_data:
            return None
        return cls(
            MetricIntervalLowerBound=json_data.get("MetricIntervalLowerBound"),
            MetricIntervalUpperBound=json_data.get("MetricIntervalUpperBound"),
            ScalingAdjustment=json_data.get("ScalingAdjustment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepAdjustment = StepAdjustment


