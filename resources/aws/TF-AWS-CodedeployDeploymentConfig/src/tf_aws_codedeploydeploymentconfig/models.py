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
    ComputePlatform: Optional[str]
    DeploymentConfigId: Optional[str]
    DeploymentConfigName: Optional[str]
    Id: Optional[str]
    MinimumHealthyHosts: Optional[Sequence["_MinimumHealthyHostsDefinition"]]
    TrafficRoutingConfig: Optional[Sequence["_TrafficRoutingConfigDefinition"]]

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
            ComputePlatform=json_data.get("ComputePlatform"),
            DeploymentConfigId=json_data.get("DeploymentConfigId"),
            DeploymentConfigName=json_data.get("DeploymentConfigName"),
            Id=json_data.get("Id"),
            MinimumHealthyHosts=deserialize_list(json_data.get("MinimumHealthyHosts"), MinimumHealthyHostsDefinition),
            TrafficRoutingConfig=deserialize_list(json_data.get("TrafficRoutingConfig"), TrafficRoutingConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MinimumHealthyHostsDefinition(BaseModel):
    Type: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MinimumHealthyHostsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MinimumHealthyHostsDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MinimumHealthyHostsDefinition = MinimumHealthyHostsDefinition


@dataclass
class TrafficRoutingConfigDefinition(BaseModel):
    Type: Optional[str]
    TimeBasedCanary: Optional[Sequence["_TimeBasedCanaryDefinition"]]
    TimeBasedLinear: Optional[Sequence["_TimeBasedLinearDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TrafficRoutingConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrafficRoutingConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            TimeBasedCanary=deserialize_list(json_data.get("TimeBasedCanary"), TimeBasedCanaryDefinition),
            TimeBasedLinear=deserialize_list(json_data.get("TimeBasedLinear"), TimeBasedLinearDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrafficRoutingConfigDefinition = TrafficRoutingConfigDefinition


@dataclass
class TimeBasedCanaryDefinition(BaseModel):
    Interval: Optional[float]
    Percentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TimeBasedCanaryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeBasedCanaryDefinition"]:
        if not json_data:
            return None
        return cls(
            Interval=json_data.get("Interval"),
            Percentage=json_data.get("Percentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeBasedCanaryDefinition = TimeBasedCanaryDefinition


@dataclass
class TimeBasedLinearDefinition(BaseModel):
    Interval: Optional[float]
    Percentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TimeBasedLinearDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeBasedLinearDefinition"]:
        if not json_data:
            return None
        return cls(
            Interval=json_data.get("Interval"),
            Percentage=json_data.get("Percentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeBasedLinearDefinition = TimeBasedLinearDefinition


