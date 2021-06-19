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
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    SelfLink: Optional[str]
    Target: Optional[str]
    AutoscalingPolicy: Optional[Sequence["_AutoscalingPolicyDefinition"]]
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
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            SelfLink=json_data.get("SelfLink"),
            Target=json_data.get("Target"),
            AutoscalingPolicy=deserialize_list(json_data.get("AutoscalingPolicy"), AutoscalingPolicyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutoscalingPolicyDefinition(BaseModel):
    CooldownPeriod: Optional[float]
    MaxReplicas: Optional[float]
    MinReplicas: Optional[float]
    Mode: Optional[str]
    CpuUtilization: Optional[Sequence["_CpuUtilizationDefinition"]]
    LoadBalancingUtilization: Optional[Sequence["_LoadBalancingUtilizationDefinition"]]
    Metric: Optional[Sequence["_MetricDefinition"]]
    ScaleInControl: Optional[Sequence["_ScaleInControlDefinition"]]
    ScalingSchedules: Optional[Sequence["_ScalingSchedulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscalingPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscalingPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            CooldownPeriod=json_data.get("CooldownPeriod"),
            MaxReplicas=json_data.get("MaxReplicas"),
            MinReplicas=json_data.get("MinReplicas"),
            Mode=json_data.get("Mode"),
            CpuUtilization=deserialize_list(json_data.get("CpuUtilization"), CpuUtilizationDefinition),
            LoadBalancingUtilization=deserialize_list(json_data.get("LoadBalancingUtilization"), LoadBalancingUtilizationDefinition),
            Metric=deserialize_list(json_data.get("Metric"), MetricDefinition),
            ScaleInControl=deserialize_list(json_data.get("ScaleInControl"), ScaleInControlDefinition),
            ScalingSchedules=deserialize_list(json_data.get("ScalingSchedules"), ScalingSchedulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscalingPolicyDefinition = AutoscalingPolicyDefinition


@dataclass
class CpuUtilizationDefinition(BaseModel):
    PredictiveMethod: Optional[str]
    Target: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CpuUtilizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CpuUtilizationDefinition"]:
        if not json_data:
            return None
        return cls(
            PredictiveMethod=json_data.get("PredictiveMethod"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CpuUtilizationDefinition = CpuUtilizationDefinition


@dataclass
class LoadBalancingUtilizationDefinition(BaseModel):
    Target: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancingUtilizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancingUtilizationDefinition"]:
        if not json_data:
            return None
        return cls(
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancingUtilizationDefinition = LoadBalancingUtilizationDefinition


@dataclass
class MetricDefinition(BaseModel):
    Name: Optional[str]
    Target: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Target=json_data.get("Target"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDefinition = MetricDefinition


@dataclass
class ScaleInControlDefinition(BaseModel):
    TimeWindowSec: Optional[float]
    MaxScaledInReplicas: Optional[Sequence["_MaxScaledInReplicasDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScaleInControlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScaleInControlDefinition"]:
        if not json_data:
            return None
        return cls(
            TimeWindowSec=json_data.get("TimeWindowSec"),
            MaxScaledInReplicas=deserialize_list(json_data.get("MaxScaledInReplicas"), MaxScaledInReplicasDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScaleInControlDefinition = ScaleInControlDefinition


@dataclass
class MaxScaledInReplicasDefinition(BaseModel):
    Fixed: Optional[float]
    Percent: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MaxScaledInReplicasDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaxScaledInReplicasDefinition"]:
        if not json_data:
            return None
        return cls(
            Fixed=json_data.get("Fixed"),
            Percent=json_data.get("Percent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaxScaledInReplicasDefinition = MaxScaledInReplicasDefinition


@dataclass
class ScalingSchedulesDefinition(BaseModel):
    Description: Optional[str]
    Disabled: Optional[bool]
    DurationSec: Optional[float]
    MinRequiredReplicas: Optional[float]
    Name: Optional[str]
    Schedule: Optional[str]
    TimeZone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingSchedulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingSchedulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Disabled=json_data.get("Disabled"),
            DurationSec=json_data.get("DurationSec"),
            MinRequiredReplicas=json_data.get("MinRequiredReplicas"),
            Name=json_data.get("Name"),
            Schedule=json_data.get("Schedule"),
            TimeZone=json_data.get("TimeZone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingSchedulesDefinition = ScalingSchedulesDefinition


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


