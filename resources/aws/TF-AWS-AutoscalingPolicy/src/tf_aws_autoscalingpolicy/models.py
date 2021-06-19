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
    Arn: Optional[str]
    AutoscalingGroupName: Optional[str]
    Cooldown: Optional[float]
    EstimatedInstanceWarmup: Optional[float]
    Id: Optional[str]
    MetricAggregationType: Optional[str]
    MinAdjustmentMagnitude: Optional[float]
    Name: Optional[str]
    PolicyType: Optional[str]
    ScalingAdjustment: Optional[float]
    PredictiveScalingConfiguration: Optional[Sequence["_PredictiveScalingConfigurationDefinition"]]
    StepAdjustment: Optional[Sequence["_StepAdjustmentDefinition"]]
    TargetTrackingConfiguration: Optional[Sequence["_TargetTrackingConfigurationDefinition"]]

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
            Arn=json_data.get("Arn"),
            AutoscalingGroupName=json_data.get("AutoscalingGroupName"),
            Cooldown=json_data.get("Cooldown"),
            EstimatedInstanceWarmup=json_data.get("EstimatedInstanceWarmup"),
            Id=json_data.get("Id"),
            MetricAggregationType=json_data.get("MetricAggregationType"),
            MinAdjustmentMagnitude=json_data.get("MinAdjustmentMagnitude"),
            Name=json_data.get("Name"),
            PolicyType=json_data.get("PolicyType"),
            ScalingAdjustment=json_data.get("ScalingAdjustment"),
            PredictiveScalingConfiguration=deserialize_list(json_data.get("PredictiveScalingConfiguration"), PredictiveScalingConfigurationDefinition),
            StepAdjustment=deserialize_list(json_data.get("StepAdjustment"), StepAdjustmentDefinition),
            TargetTrackingConfiguration=deserialize_list(json_data.get("TargetTrackingConfiguration"), TargetTrackingConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PredictiveScalingConfigurationDefinition(BaseModel):
    MaxCapacityBreachBehavior: Optional[str]
    MaxCapacityBuffer: Optional[str]
    Mode: Optional[str]
    SchedulingBufferTime: Optional[str]
    MetricSpecification: Optional[Sequence["_MetricSpecificationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PredictiveScalingConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredictiveScalingConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxCapacityBreachBehavior=json_data.get("MaxCapacityBreachBehavior"),
            MaxCapacityBuffer=json_data.get("MaxCapacityBuffer"),
            Mode=json_data.get("Mode"),
            SchedulingBufferTime=json_data.get("SchedulingBufferTime"),
            MetricSpecification=deserialize_list(json_data.get("MetricSpecification"), MetricSpecificationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredictiveScalingConfigurationDefinition = PredictiveScalingConfigurationDefinition


@dataclass
class MetricSpecificationDefinition(BaseModel):
    TargetValue: Optional[float]
    PredefinedLoadMetricSpecification: Optional[Sequence["_PredefinedLoadMetricSpecificationDefinition"]]
    PredefinedMetricPairSpecification: Optional[Sequence["_PredefinedMetricPairSpecificationDefinition"]]
    PredefinedScalingMetricSpecification: Optional[Sequence["_PredefinedScalingMetricSpecificationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetValue=json_data.get("TargetValue"),
            PredefinedLoadMetricSpecification=deserialize_list(json_data.get("PredefinedLoadMetricSpecification"), PredefinedLoadMetricSpecificationDefinition),
            PredefinedMetricPairSpecification=deserialize_list(json_data.get("PredefinedMetricPairSpecification"), PredefinedMetricPairSpecificationDefinition),
            PredefinedScalingMetricSpecification=deserialize_list(json_data.get("PredefinedScalingMetricSpecification"), PredefinedScalingMetricSpecificationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricSpecificationDefinition = MetricSpecificationDefinition


@dataclass
class PredefinedLoadMetricSpecificationDefinition(BaseModel):
    PredefinedMetricType: Optional[str]
    ResourceLabel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredefinedLoadMetricSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredefinedLoadMetricSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            PredefinedMetricType=json_data.get("PredefinedMetricType"),
            ResourceLabel=json_data.get("ResourceLabel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredefinedLoadMetricSpecificationDefinition = PredefinedLoadMetricSpecificationDefinition


@dataclass
class PredefinedMetricPairSpecificationDefinition(BaseModel):
    PredefinedMetricType: Optional[str]
    ResourceLabel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredefinedMetricPairSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredefinedMetricPairSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            PredefinedMetricType=json_data.get("PredefinedMetricType"),
            ResourceLabel=json_data.get("ResourceLabel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredefinedMetricPairSpecificationDefinition = PredefinedMetricPairSpecificationDefinition


@dataclass
class PredefinedScalingMetricSpecificationDefinition(BaseModel):
    PredefinedMetricType: Optional[str]
    ResourceLabel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredefinedScalingMetricSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredefinedScalingMetricSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            PredefinedMetricType=json_data.get("PredefinedMetricType"),
            ResourceLabel=json_data.get("ResourceLabel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredefinedScalingMetricSpecificationDefinition = PredefinedScalingMetricSpecificationDefinition


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


@dataclass
class TargetTrackingConfigurationDefinition(BaseModel):
    DisableScaleIn: Optional[bool]
    TargetValue: Optional[float]
    CustomizedMetricSpecification: Optional[Sequence["_CustomizedMetricSpecificationDefinition"]]
    PredefinedMetricSpecification: Optional[Sequence["_PredefinedMetricSpecificationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetTrackingConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetTrackingConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableScaleIn=json_data.get("DisableScaleIn"),
            TargetValue=json_data.get("TargetValue"),
            CustomizedMetricSpecification=deserialize_list(json_data.get("CustomizedMetricSpecification"), CustomizedMetricSpecificationDefinition),
            PredefinedMetricSpecification=deserialize_list(json_data.get("PredefinedMetricSpecification"), PredefinedMetricSpecificationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetTrackingConfigurationDefinition = TargetTrackingConfigurationDefinition


@dataclass
class CustomizedMetricSpecificationDefinition(BaseModel):
    MetricName: Optional[str]
    Namespace: Optional[str]
    Statistic: Optional[str]
    Unit: Optional[str]
    MetricDimension: Optional[Sequence["_MetricDimensionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomizedMetricSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomizedMetricSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            Statistic=json_data.get("Statistic"),
            Unit=json_data.get("Unit"),
            MetricDimension=deserialize_list(json_data.get("MetricDimension"), MetricDimensionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomizedMetricSpecificationDefinition = CustomizedMetricSpecificationDefinition


@dataclass
class MetricDimensionDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDimensionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDimensionDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDimensionDefinition = MetricDimensionDefinition


@dataclass
class PredefinedMetricSpecificationDefinition(BaseModel):
    PredefinedMetricType: Optional[str]
    ResourceLabel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredefinedMetricSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredefinedMetricSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            PredefinedMetricType=json_data.get("PredefinedMetricType"),
            ResourceLabel=json_data.get("ResourceLabel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredefinedMetricSpecificationDefinition = PredefinedMetricSpecificationDefinition


