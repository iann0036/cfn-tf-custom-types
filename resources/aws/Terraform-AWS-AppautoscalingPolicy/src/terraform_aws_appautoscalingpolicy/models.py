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
    Arn: Optional[str]
    Cooldown: Optional[float]
    MetricAggregationType: Optional[str]
    MinAdjustmentMagnitude: Optional[float]
    Name: Optional[str]
    PolicyType: Optional[str]
    ResourceId: Optional[str]
    ScalableDimension: Optional[str]
    ServiceNamespace: Optional[str]
    StepAdjustment: Optional[Sequence["_StepAdjustment"]]
    StepScalingPolicyConfiguration: Optional[Sequence["_StepScalingPolicyConfiguration"]]
    TargetTrackingScalingPolicyConfiguration: Optional[Sequence["_TargetTrackingScalingPolicyConfiguration"]]
    CustomizedMetricSpecification: Optional[Sequence["_CustomizedMetricSpecification"]]
    PredefinedMetricSpecification: Optional[Sequence["_PredefinedMetricSpecification"]]
    Dimensions: Optional[Sequence["_Dimensions"]]

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
            Arn=json_data.get("Arn"),
            Cooldown=json_data.get("Cooldown"),
            MetricAggregationType=json_data.get("MetricAggregationType"),
            MinAdjustmentMagnitude=json_data.get("MinAdjustmentMagnitude"),
            Name=json_data.get("Name"),
            PolicyType=json_data.get("PolicyType"),
            ResourceId=json_data.get("ResourceId"),
            ScalableDimension=json_data.get("ScalableDimension"),
            ServiceNamespace=json_data.get("ServiceNamespace"),
            StepAdjustment=json_data.get("StepAdjustment"),
            StepScalingPolicyConfiguration=json_data.get("StepScalingPolicyConfiguration"),
            TargetTrackingScalingPolicyConfiguration=json_data.get("TargetTrackingScalingPolicyConfiguration"),
            CustomizedMetricSpecification=json_data.get("CustomizedMetricSpecification"),
            PredefinedMetricSpecification=json_data.get("PredefinedMetricSpecification"),
            Dimensions=json_data.get("Dimensions"),
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


@dataclass
class StepScalingPolicyConfiguration:
    AdjustmentType: Optional[str]
    Cooldown: Optional[float]
    MetricAggregationType: Optional[str]
    MinAdjustmentMagnitude: Optional[float]
    StepAdjustment: Optional[Sequence["_StepAdjustment"]]

    @classmethod
    def _deserialize(
        cls: Type["_StepScalingPolicyConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepScalingPolicyConfiguration"]:
        if not json_data:
            return None
        return cls(
            AdjustmentType=json_data.get("AdjustmentType"),
            Cooldown=json_data.get("Cooldown"),
            MetricAggregationType=json_data.get("MetricAggregationType"),
            MinAdjustmentMagnitude=json_data.get("MinAdjustmentMagnitude"),
            StepAdjustment=json_data.get("StepAdjustment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepScalingPolicyConfiguration = StepScalingPolicyConfiguration


@dataclass
class TargetTrackingScalingPolicyConfiguration:
    DisableScaleIn: Optional[bool]
    ScaleInCooldown: Optional[float]
    ScaleOutCooldown: Optional[float]
    TargetValue: Optional[float]
    CustomizedMetricSpecification: Optional[Sequence["_CustomizedMetricSpecification"]]
    PredefinedMetricSpecification: Optional[Sequence["_PredefinedMetricSpecification"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetTrackingScalingPolicyConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetTrackingScalingPolicyConfiguration"]:
        if not json_data:
            return None
        return cls(
            DisableScaleIn=json_data.get("DisableScaleIn"),
            ScaleInCooldown=json_data.get("ScaleInCooldown"),
            ScaleOutCooldown=json_data.get("ScaleOutCooldown"),
            TargetValue=json_data.get("TargetValue"),
            CustomizedMetricSpecification=json_data.get("CustomizedMetricSpecification"),
            PredefinedMetricSpecification=json_data.get("PredefinedMetricSpecification"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetTrackingScalingPolicyConfiguration = TargetTrackingScalingPolicyConfiguration


@dataclass
class CustomizedMetricSpecification:
    MetricName: Optional[str]
    Namespace: Optional[str]
    Statistic: Optional[str]
    Unit: Optional[str]
    Dimensions: Optional[Sequence["_Dimensions"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomizedMetricSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomizedMetricSpecification"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            Statistic=json_data.get("Statistic"),
            Unit=json_data.get("Unit"),
            Dimensions=json_data.get("Dimensions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomizedMetricSpecification = CustomizedMetricSpecification


@dataclass
class Dimensions:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dimensions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dimensions"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dimensions = Dimensions


@dataclass
class PredefinedMetricSpecification:
    PredefinedMetricType: Optional[str]
    ResourceLabel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredefinedMetricSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredefinedMetricSpecification"]:
        if not json_data:
            return None
        return cls(
            PredefinedMetricType=json_data.get("PredefinedMetricType"),
            ResourceLabel=json_data.get("ResourceLabel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredefinedMetricSpecification = PredefinedMetricSpecification


