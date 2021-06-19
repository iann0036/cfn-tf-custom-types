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
    Arn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PolicyType: Optional[str]
    ResourceId: Optional[str]
    ScalableDimension: Optional[str]
    ServiceNamespace: Optional[str]
    StepScalingPolicyConfiguration: Optional[Sequence["_StepScalingPolicyConfigurationDefinition"]]
    TargetTrackingScalingPolicyConfiguration: Optional[Sequence["_TargetTrackingScalingPolicyConfigurationDefinition"]]

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
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PolicyType=json_data.get("PolicyType"),
            ResourceId=json_data.get("ResourceId"),
            ScalableDimension=json_data.get("ScalableDimension"),
            ServiceNamespace=json_data.get("ServiceNamespace"),
            StepScalingPolicyConfiguration=deserialize_list(json_data.get("StepScalingPolicyConfiguration"), StepScalingPolicyConfigurationDefinition),
            TargetTrackingScalingPolicyConfiguration=deserialize_list(json_data.get("TargetTrackingScalingPolicyConfiguration"), TargetTrackingScalingPolicyConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class StepScalingPolicyConfigurationDefinition(BaseModel):
    AdjustmentType: Optional[str]
    Cooldown: Optional[float]
    MetricAggregationType: Optional[str]
    MinAdjustmentMagnitude: Optional[float]
    StepAdjustment: Optional[Sequence["_StepAdjustmentDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StepScalingPolicyConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepScalingPolicyConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AdjustmentType=json_data.get("AdjustmentType"),
            Cooldown=json_data.get("Cooldown"),
            MetricAggregationType=json_data.get("MetricAggregationType"),
            MinAdjustmentMagnitude=json_data.get("MinAdjustmentMagnitude"),
            StepAdjustment=deserialize_list(json_data.get("StepAdjustment"), StepAdjustmentDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepScalingPolicyConfigurationDefinition = StepScalingPolicyConfigurationDefinition


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
class TargetTrackingScalingPolicyConfigurationDefinition(BaseModel):
    DisableScaleIn: Optional[bool]
    ScaleInCooldown: Optional[float]
    ScaleOutCooldown: Optional[float]
    TargetValue: Optional[float]
    CustomizedMetricSpecification: Optional[Sequence["_CustomizedMetricSpecificationDefinition"]]
    PredefinedMetricSpecification: Optional[Sequence["_PredefinedMetricSpecificationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetTrackingScalingPolicyConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetTrackingScalingPolicyConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableScaleIn=json_data.get("DisableScaleIn"),
            ScaleInCooldown=json_data.get("ScaleInCooldown"),
            ScaleOutCooldown=json_data.get("ScaleOutCooldown"),
            TargetValue=json_data.get("TargetValue"),
            CustomizedMetricSpecification=deserialize_list(json_data.get("CustomizedMetricSpecification"), CustomizedMetricSpecificationDefinition),
            PredefinedMetricSpecification=deserialize_list(json_data.get("PredefinedMetricSpecification"), PredefinedMetricSpecificationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetTrackingScalingPolicyConfigurationDefinition = TargetTrackingScalingPolicyConfigurationDefinition


@dataclass
class CustomizedMetricSpecificationDefinition(BaseModel):
    MetricName: Optional[str]
    Namespace: Optional[str]
    Statistic: Optional[str]
    Unit: Optional[str]
    Dimensions: Optional[Sequence["_DimensionsDefinition"]]

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
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomizedMetricSpecificationDefinition = CustomizedMetricSpecificationDefinition


@dataclass
class DimensionsDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionsDefinition = DimensionsDefinition


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


