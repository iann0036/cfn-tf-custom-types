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
    Location: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    AppEngineRoutingOverride: Optional[Sequence["_AppEngineRoutingOverride"]]
    RateLimits: Optional[Sequence["_RateLimits"]]
    RetryConfig: Optional[Sequence["_RetryConfig"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            AppEngineRoutingOverride=json_data.get("AppEngineRoutingOverride"),
            RateLimits=json_data.get("RateLimits"),
            RetryConfig=json_data.get("RetryConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppEngineRoutingOverride:
    Instance: Optional[str]
    Service: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppEngineRoutingOverride"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppEngineRoutingOverride"]:
        if not json_data:
            return None
        return cls(
            Instance=json_data.get("Instance"),
            Service=json_data.get("Service"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppEngineRoutingOverride = AppEngineRoutingOverride


@dataclass
class RateLimits:
    MaxConcurrentDispatches: Optional[float]
    MaxDispatchesPerSecond: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimits"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimits"]:
        if not json_data:
            return None
        return cls(
            MaxConcurrentDispatches=json_data.get("MaxConcurrentDispatches"),
            MaxDispatchesPerSecond=json_data.get("MaxDispatchesPerSecond"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimits = RateLimits


@dataclass
class RetryConfig:
    MaxAttempts: Optional[float]
    MaxBackoff: Optional[str]
    MaxDoublings: Optional[float]
    MaxRetryDuration: Optional[str]
    MinBackoff: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RetryConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryConfig"]:
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
_RetryConfig = RetryConfig


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


