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
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    SelfLink: Optional[str]
    Target: Optional[str]
    AutoscalingPolicy: Optional[Sequence["_AutoscalingPolicy"]]
    Timeouts: Optional["_Timeouts"]
    CpuUtilization: Optional[Sequence["_CpuUtilization"]]
    LoadBalancingUtilization: Optional[Sequence["_LoadBalancingUtilization"]]
    Metric: Optional[Sequence["_Metric"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            AutoscalingPolicy=json_data.get("AutoscalingPolicy"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            CpuUtilization=json_data.get("CpuUtilization"),
            LoadBalancingUtilization=json_data.get("LoadBalancingUtilization"),
            Metric=json_data.get("Metric"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutoscalingPolicy:
    CooldownPeriod: Optional[float]
    MaxReplicas: Optional[float]
    MinReplicas: Optional[float]
    CpuUtilization: Optional[Sequence["_CpuUtilization"]]
    LoadBalancingUtilization: Optional[Sequence["_LoadBalancingUtilization"]]
    Metric: Optional[Sequence["_Metric"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscalingPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscalingPolicy"]:
        if not json_data:
            return None
        return cls(
            CooldownPeriod=json_data.get("CooldownPeriod"),
            MaxReplicas=json_data.get("MaxReplicas"),
            MinReplicas=json_data.get("MinReplicas"),
            CpuUtilization=json_data.get("CpuUtilization"),
            LoadBalancingUtilization=json_data.get("LoadBalancingUtilization"),
            Metric=json_data.get("Metric"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscalingPolicy = AutoscalingPolicy


@dataclass
class CpuUtilization:
    Target: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CpuUtilization"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CpuUtilization"]:
        if not json_data:
            return None
        return cls(
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CpuUtilization = CpuUtilization


@dataclass
class LoadBalancingUtilization:
    Target: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancingUtilization"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancingUtilization"]:
        if not json_data:
            return None
        return cls(
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancingUtilization = LoadBalancingUtilization


@dataclass
class Metric:
    Name: Optional[str]
    Target: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metric"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Target=json_data.get("Target"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metric = Metric


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


