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
    ComputePlatform: Optional[str]
    DeploymentConfigId: Optional[str]
    DeploymentConfigName: Optional[str]
    Id: Optional[str]
    MinimumHealthyHosts: Optional[Sequence["_MinimumHealthyHosts"]]
    TrafficRoutingConfig: Optional[Sequence["_TrafficRoutingConfig"]]
    TimeBasedCanary: Optional[Sequence["_TimeBasedCanary"]]
    TimeBasedLinear: Optional[Sequence["_TimeBasedLinear"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ComputePlatform=json_data.get("ComputePlatform"),
            DeploymentConfigId=json_data.get("DeploymentConfigId"),
            DeploymentConfigName=json_data.get("DeploymentConfigName"),
            Id=json_data.get("Id"),
            MinimumHealthyHosts=json_data.get("MinimumHealthyHosts"),
            TrafficRoutingConfig=json_data.get("TrafficRoutingConfig"),
            TimeBasedCanary=json_data.get("TimeBasedCanary"),
            TimeBasedLinear=json_data.get("TimeBasedLinear"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MinimumHealthyHosts:
    Type: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MinimumHealthyHosts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MinimumHealthyHosts"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MinimumHealthyHosts = MinimumHealthyHosts


@dataclass
class TrafficRoutingConfig:
    Type: Optional[str]
    TimeBasedCanary: Optional[Sequence["_TimeBasedCanary"]]
    TimeBasedLinear: Optional[Sequence["_TimeBasedLinear"]]

    @classmethod
    def _deserialize(
        cls: Type["_TrafficRoutingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrafficRoutingConfig"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            TimeBasedCanary=json_data.get("TimeBasedCanary"),
            TimeBasedLinear=json_data.get("TimeBasedLinear"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrafficRoutingConfig = TrafficRoutingConfig


@dataclass
class TimeBasedCanary:
    Interval: Optional[float]
    Percentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TimeBasedCanary"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeBasedCanary"]:
        if not json_data:
            return None
        return cls(
            Interval=json_data.get("Interval"),
            Percentage=json_data.get("Percentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeBasedCanary = TimeBasedCanary


@dataclass
class TimeBasedLinear:
    Interval: Optional[float]
    Percentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TimeBasedLinear"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeBasedLinear"]:
        if not json_data:
            return None
        return cls(
            Interval=json_data.get("Interval"),
            Percentage=json_data.get("Percentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeBasedLinear = TimeBasedLinear


