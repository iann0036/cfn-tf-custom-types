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
    Location: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    AppEngineRoutingOverride: Optional[Sequence["_AppEngineRoutingOverrideDefinition"]]
    RateLimits: Optional[Sequence["_RateLimitsDefinition"]]
    RetryConfig: Optional[Sequence["_RetryConfigDefinition"]]
    StackdriverLoggingConfig: Optional[Sequence["_StackdriverLoggingConfigDefinition"]]
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
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            AppEngineRoutingOverride=deserialize_list(json_data.get("AppEngineRoutingOverride"), AppEngineRoutingOverrideDefinition),
            RateLimits=deserialize_list(json_data.get("RateLimits"), RateLimitsDefinition),
            RetryConfig=deserialize_list(json_data.get("RetryConfig"), RetryConfigDefinition),
            StackdriverLoggingConfig=deserialize_list(json_data.get("StackdriverLoggingConfig"), StackdriverLoggingConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppEngineRoutingOverrideDefinition(BaseModel):
    Instance: Optional[str]
    Service: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppEngineRoutingOverrideDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppEngineRoutingOverrideDefinition"]:
        if not json_data:
            return None
        return cls(
            Instance=json_data.get("Instance"),
            Service=json_data.get("Service"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppEngineRoutingOverrideDefinition = AppEngineRoutingOverrideDefinition


@dataclass
class RateLimitsDefinition(BaseModel):
    MaxConcurrentDispatches: Optional[float]
    MaxDispatchesPerSecond: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxConcurrentDispatches=json_data.get("MaxConcurrentDispatches"),
            MaxDispatchesPerSecond=json_data.get("MaxDispatchesPerSecond"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimitsDefinition = RateLimitsDefinition


@dataclass
class RetryConfigDefinition(BaseModel):
    MaxAttempts: Optional[float]
    MaxBackoff: Optional[str]
    MaxDoublings: Optional[float]
    MaxRetryDuration: Optional[str]
    MinBackoff: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RetryConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxAttempts=json_data.get("MaxAttempts"),
            MaxBackoff=json_data.get("MaxBackoff"),
            MaxDoublings=json_data.get("MaxDoublings"),
            MaxRetryDuration=json_data.get("MaxRetryDuration"),
            MinBackoff=json_data.get("MinBackoff"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryConfigDefinition = RetryConfigDefinition


@dataclass
class StackdriverLoggingConfigDefinition(BaseModel):
    SamplingRatio: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StackdriverLoggingConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StackdriverLoggingConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            SamplingRatio=json_data.get("SamplingRatio"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StackdriverLoggingConfigDefinition = StackdriverLoggingConfigDefinition


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


