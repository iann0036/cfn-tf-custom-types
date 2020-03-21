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
    AllocatedCapacity: Optional[float]
    Arn: Optional[str]
    Connections: Optional[Sequence[str]]
    DefaultArguments: Optional[Sequence["_DefaultArguments"]]
    Description: Optional[str]
    GlueVersion: Optional[str]
    Id: Optional[str]
    MaxCapacity: Optional[float]
    MaxRetries: Optional[float]
    Name: Optional[str]
    NumberOfWorkers: Optional[float]
    RoleArn: Optional[str]
    SecurityConfiguration: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Timeout: Optional[float]
    WorkerType: Optional[str]
    Command: Optional[Sequence["_Command"]]
    ExecutionProperty: Optional[Sequence["_ExecutionProperty"]]
    NotificationProperty: Optional[Sequence["_NotificationProperty"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllocatedCapacity=json_data.get("AllocatedCapacity"),
            Arn=json_data.get("Arn"),
            Connections=json_data.get("Connections"),
            DefaultArguments=json_data.get("DefaultArguments"),
            Description=json_data.get("Description"),
            GlueVersion=json_data.get("GlueVersion"),
            Id=json_data.get("Id"),
            MaxCapacity=json_data.get("MaxCapacity"),
            MaxRetries=json_data.get("MaxRetries"),
            Name=json_data.get("Name"),
            NumberOfWorkers=json_data.get("NumberOfWorkers"),
            RoleArn=json_data.get("RoleArn"),
            SecurityConfiguration=json_data.get("SecurityConfiguration"),
            Tags=json_data.get("Tags"),
            Timeout=json_data.get("Timeout"),
            WorkerType=json_data.get("WorkerType"),
            Command=json_data.get("Command"),
            ExecutionProperty=json_data.get("ExecutionProperty"),
            NotificationProperty=json_data.get("NotificationProperty"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefaultArguments:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultArguments"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultArguments"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultArguments = DefaultArguments


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Command:
    Name: Optional[str]
    PythonVersion: Optional[str]
    ScriptLocation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Command"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Command"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PythonVersion=json_data.get("PythonVersion"),
            ScriptLocation=json_data.get("ScriptLocation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Command = Command


@dataclass
class ExecutionProperty:
    MaxConcurrentRuns: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ExecutionProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExecutionProperty"]:
        if not json_data:
            return None
        return cls(
            MaxConcurrentRuns=json_data.get("MaxConcurrentRuns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExecutionProperty = ExecutionProperty


@dataclass
class NotificationProperty:
    NotifyDelayAfter: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationProperty"]:
        if not json_data:
            return None
        return cls(
            NotifyDelayAfter=json_data.get("NotifyDelayAfter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationProperty = NotificationProperty


