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
    Id: Optional[str]
    Name: Optional[str]
    ScalingPlanVersion: Optional[float]
    ApplicationSource: Optional[Sequence["_ApplicationSourceDefinition"]]
    ScalingInstruction: Optional[Sequence["_ScalingInstructionDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ScalingPlanVersion=json_data.get("ScalingPlanVersion"),
            ApplicationSource=deserialize_list(json_data.get("ApplicationSource"), ApplicationSourceDefinition),
            ScalingInstruction=deserialize_list(json_data.get("ScalingInstruction"), ScalingInstructionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ApplicationSourceDefinition(BaseModel):
    CloudformationStackArn: Optional[str]
    TagFilter: Optional[Sequence["_TagFilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudformationStackArn=json_data.get("CloudformationStackArn"),
            TagFilter=deserialize_list(json_data.get("TagFilter"), TagFilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationSourceDefinition = ApplicationSourceDefinition


@dataclass
class TagFilterDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TagFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagFilterDefinition = TagFilterDefinition


@dataclass
class ScalingInstructionDefinition(BaseModel):
    DisableDynamicScaling: Optional[bool]
    MaxCapacity: Optional[float]
    MinCapacity: Optional[float]
    PredictiveScalingMaxCapacityBehavior: Optional[str]
    PredictiveScalingMaxCapacityBuffer: Optional[float]
    PredictiveScalingMode: Optional[str]
    ResourceId: Optional[str]
    ScalableDimension: Optional[str]
    ScalingPolicyUpdateBehavior: Optional[str]
    ScheduledActionBufferTime: Optional[float]
    ServiceNamespace: Optional[str]
    CustomizedLoadMetricSpecification: Optional[Sequence["_CustomizedLoadMetricSpecificationDefinition"]]
    PredefinedLoadMetricSpecification: Optional[Sequence["_PredefinedLoadMetricSpecificationDefinition"]]
    TargetTrackingConfiguration: Optional[Sequence["_TargetTrackingConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingInstructionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingInstructionDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableDynamicScaling=json_data.get("DisableDynamicScaling"),
            MaxCapacity=json_data.get("MaxCapacity"),
            MinCapacity=json_data.get("MinCapacity"),
            PredictiveScalingMaxCapacityBehavior=json_data.get("PredictiveScalingMaxCapacityBehavior"),
            PredictiveScalingMaxCapacityBuffer=json_data.get("PredictiveScalingMaxCapacityBuffer"),
            PredictiveScalingMode=json_data.get("PredictiveScalingMode"),
            ResourceId=json_data.get("ResourceId"),
            ScalableDimension=json_data.get("ScalableDimension"),
            ScalingPolicyUpdateBehavior=json_data.get("ScalingPolicyUpdateBehavior"),
            ScheduledActionBufferTime=json_data.get("ScheduledActionBufferTime"),
            ServiceNamespace=json_data.get("ServiceNamespace"),
            CustomizedLoadMetricSpecification=deserialize_list(json_data.get("CustomizedLoadMetricSpecification"), CustomizedLoadMetricSpecificationDefinition),
            PredefinedLoadMetricSpecification=deserialize_list(json_data.get("PredefinedLoadMetricSpecification"), PredefinedLoadMetricSpecificationDefinition),
            TargetTrackingConfiguration=deserialize_list(json_data.get("TargetTrackingConfiguration"), TargetTrackingConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingInstructionDefinition = ScalingInstructionDefinition


@dataclass
class CustomizedLoadMetricSpecificationDefinition(BaseModel):
    Dimensions: Optional[Sequence["_DimensionsDefinition"]]
    MetricName: Optional[str]
    Namespace: Optional[str]
    Statistic: Optional[str]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomizedLoadMetricSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomizedLoadMetricSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition),
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            Statistic=json_data.get("Statistic"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomizedLoadMetricSpecificationDefinition = CustomizedLoadMetricSpecificationDefinition


@dataclass
class DimensionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionsDefinition = DimensionsDefinition


@dataclass
class PredefinedLoadMetricSpecificationDefinition(BaseModel):
    PredefinedLoadMetricType: Optional[str]
    ResourceLabel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredefinedLoadMetricSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredefinedLoadMetricSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            PredefinedLoadMetricType=json_data.get("PredefinedLoadMetricType"),
            ResourceLabel=json_data.get("ResourceLabel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredefinedLoadMetricSpecificationDefinition = PredefinedLoadMetricSpecificationDefinition


@dataclass
class TargetTrackingConfigurationDefinition(BaseModel):
    DisableScaleIn: Optional[bool]
    EstimatedInstanceWarmup: Optional[float]
    ScaleInCooldown: Optional[float]
    ScaleOutCooldown: Optional[float]
    TargetValue: Optional[float]
    CustomizedScalingMetricSpecification: Optional[Sequence["_CustomizedScalingMetricSpecificationDefinition"]]
    PredefinedScalingMetricSpecification: Optional[Sequence["_PredefinedScalingMetricSpecificationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetTrackingConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetTrackingConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableScaleIn=json_data.get("DisableScaleIn"),
            EstimatedInstanceWarmup=json_data.get("EstimatedInstanceWarmup"),
            ScaleInCooldown=json_data.get("ScaleInCooldown"),
            ScaleOutCooldown=json_data.get("ScaleOutCooldown"),
            TargetValue=json_data.get("TargetValue"),
            CustomizedScalingMetricSpecification=deserialize_list(json_data.get("CustomizedScalingMetricSpecification"), CustomizedScalingMetricSpecificationDefinition),
            PredefinedScalingMetricSpecification=deserialize_list(json_data.get("PredefinedScalingMetricSpecification"), PredefinedScalingMetricSpecificationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetTrackingConfigurationDefinition = TargetTrackingConfigurationDefinition


@dataclass
class CustomizedScalingMetricSpecificationDefinition(BaseModel):
    Dimensions: Optional[Sequence["_DimensionsDefinition2"]]
    MetricName: Optional[str]
    Namespace: Optional[str]
    Statistic: Optional[str]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomizedScalingMetricSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomizedScalingMetricSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition2),
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            Statistic=json_data.get("Statistic"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomizedScalingMetricSpecificationDefinition = CustomizedScalingMetricSpecificationDefinition


@dataclass
class DimensionsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionsDefinition2 = DimensionsDefinition2


@dataclass
class PredefinedScalingMetricSpecificationDefinition(BaseModel):
    PredefinedScalingMetricType: Optional[str]
    ResourceLabel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredefinedScalingMetricSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredefinedScalingMetricSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            PredefinedScalingMetricType=json_data.get("PredefinedScalingMetricType"),
            ResourceLabel=json_data.get("ResourceLabel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredefinedScalingMetricSpecificationDefinition = PredefinedScalingMetricSpecificationDefinition


