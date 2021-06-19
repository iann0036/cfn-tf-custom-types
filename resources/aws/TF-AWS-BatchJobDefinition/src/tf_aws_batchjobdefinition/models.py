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
    ContainerProperties: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
    PlatformCapabilities: Optional[Sequence[str]]
    PropagateTags: Optional[bool]
    Revision: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Type: Optional[str]
    RetryStrategy: Optional[Sequence["_RetryStrategyDefinition"]]
    Timeout: Optional[Sequence["_TimeoutDefinition"]]

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
            ContainerProperties=json_data.get("ContainerProperties"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            PlatformCapabilities=json_data.get("PlatformCapabilities"),
            PropagateTags=json_data.get("PropagateTags"),
            Revision=json_data.get("Revision"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Type=json_data.get("Type"),
            RetryStrategy=deserialize_list(json_data.get("RetryStrategy"), RetryStrategyDefinition),
            Timeout=deserialize_list(json_data.get("Timeout"), TimeoutDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class RetryStrategyDefinition(BaseModel):
    Attempts: Optional[float]
    EvaluateOnExit: Optional[Sequence["_EvaluateOnExitDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RetryStrategyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryStrategyDefinition"]:
        if not json_data:
            return None
        return cls(
            Attempts=json_data.get("Attempts"),
            EvaluateOnExit=deserialize_list(json_data.get("EvaluateOnExit"), EvaluateOnExitDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryStrategyDefinition = RetryStrategyDefinition


@dataclass
class EvaluateOnExitDefinition(BaseModel):
    Action: Optional[str]
    OnExitCode: Optional[str]
    OnReason: Optional[str]
    OnStatusReason: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EvaluateOnExitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EvaluateOnExitDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            OnExitCode=json_data.get("OnExitCode"),
            OnReason=json_data.get("OnReason"),
            OnStatusReason=json_data.get("OnStatusReason"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EvaluateOnExitDefinition = EvaluateOnExitDefinition


@dataclass
class TimeoutDefinition(BaseModel):
    AttemptDurationSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutDefinition"]:
        if not json_data:
            return None
        return cls(
            AttemptDurationSeconds=json_data.get("AttemptDurationSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutDefinition = TimeoutDefinition


