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
    AutoscalingGroupName: Optional[str]
    Cooldown: Optional[float]
    EstimatedInstanceWarmup: Optional[float]
    Id: Optional[str]
    MetricAggregationType: Optional[str]
    MinAdjustmentMagnitude: Optional[float]
    MinAdjustmentStep: Optional[float]
    Name: Optional[str]
    PolicyType: Optional[str]
    ScalingAdjustment: Optional[float]
    StepAdjustment: Optional[Sequence["_StepAdjustment"]]
    TargetTrackingConfiguration: Optional[Sequence["_TargetTrackingConfiguration"]]
    CustomizedMetricSpecification: Optional[Sequence["_CustomizedMetricSpecification"]]
    PredefinedMetricSpecification: Optional[Sequence["_PredefinedMetricSpecification"]]
    MetricDimension: Optional[Sequence["_MetricDimension"]]

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
            AutoscalingGroupName=json_data.get("AutoscalingGroupName"),
            Cooldown=json_data.get("Cooldown"),
            EstimatedInstanceWarmup=json_data.get("EstimatedInstanceWarmup"),
            Id=json_data.get("Id"),
            MetricAggregationType=json_data.get("MetricAggregationType"),
            MinAdjustmentMagnitude=json_data.get("MinAdjustmentMagnitude"),
            MinAdjustmentStep=json_data.get("MinAdjustmentStep"),
            Name=json_data.get("Name"),
            PolicyType=json_data.get("PolicyType"),
            ScalingAdjustment=json_data.get("ScalingAdjustment"),
            StepAdjustment=json_data.get("StepAdjustment"),
            TargetTrackingConfiguration=json_data.get("TargetTrackingConfiguration"),
            CustomizedMetricSpecification=json_data.get("CustomizedMetricSpecification"),
            PredefinedMetricSpecification=json_data.get("PredefinedMetricSpecification"),
            MetricDimension=json_data.get("MetricDimension"),
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
class TargetTrackingConfiguration:
    DisableScaleIn: Optional[bool]
    TargetValue: Optional[float]
    CustomizedMetricSpecification: Optional[Sequence["_CustomizedMetricSpecification"]]
    PredefinedMetricSpecification: Optional[Sequence["_PredefinedMetricSpecification"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetTrackingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetTrackingConfiguration"]:
        if not json_data:
            return None
        return cls(
            DisableScaleIn=json_data.get("DisableScaleIn"),
            TargetValue=json_data.get("TargetValue"),
            CustomizedMetricSpecification=json_data.get("CustomizedMetricSpecification"),
            PredefinedMetricSpecification=json_data.get("PredefinedMetricSpecification"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetTrackingConfiguration = TargetTrackingConfiguration


@dataclass
class CustomizedMetricSpecification:
    MetricName: Optional[str]
    Namespace: Optional[str]
    Statistic: Optional[str]
    Unit: Optional[str]
    MetricDimension: Optional[Sequence["_MetricDimension"]]

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
            MetricDimension=json_data.get("MetricDimension"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomizedMetricSpecification = CustomizedMetricSpecification


@dataclass
class MetricDimension:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDimension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDimension"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDimension = MetricDimension


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


