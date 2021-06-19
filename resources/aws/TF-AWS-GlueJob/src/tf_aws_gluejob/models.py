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
    Connections: Optional[Sequence[str]]
    DefaultArguments: Optional[Sequence["_DefaultArgumentsDefinition"]]
    Description: Optional[str]
    GlueVersion: Optional[str]
    Id: Optional[str]
    MaxCapacity: Optional[float]
    MaxRetries: Optional[float]
    Name: Optional[str]
    NonOverridableArguments: Optional[Sequence["_NonOverridableArgumentsDefinition"]]
    NumberOfWorkers: Optional[float]
    RoleArn: Optional[str]
    SecurityConfiguration: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Timeout: Optional[float]
    WorkerType: Optional[str]
    Command: Optional[Sequence["_CommandDefinition"]]
    ExecutionProperty: Optional[Sequence["_ExecutionPropertyDefinition"]]
    NotificationProperty: Optional[Sequence["_NotificationPropertyDefinition"]]

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
            Connections=json_data.get("Connections"),
            DefaultArguments=deserialize_list(json_data.get("DefaultArguments"), DefaultArgumentsDefinition),
            Description=json_data.get("Description"),
            GlueVersion=json_data.get("GlueVersion"),
            Id=json_data.get("Id"),
            MaxCapacity=json_data.get("MaxCapacity"),
            MaxRetries=json_data.get("MaxRetries"),
            Name=json_data.get("Name"),
            NonOverridableArguments=deserialize_list(json_data.get("NonOverridableArguments"), NonOverridableArgumentsDefinition),
            NumberOfWorkers=json_data.get("NumberOfWorkers"),
            RoleArn=json_data.get("RoleArn"),
            SecurityConfiguration=json_data.get("SecurityConfiguration"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Timeout=json_data.get("Timeout"),
            WorkerType=json_data.get("WorkerType"),
            Command=deserialize_list(json_data.get("Command"), CommandDefinition),
            ExecutionProperty=deserialize_list(json_data.get("ExecutionProperty"), ExecutionPropertyDefinition),
            NotificationProperty=deserialize_list(json_data.get("NotificationProperty"), NotificationPropertyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefaultArgumentsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultArgumentsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultArgumentsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultArgumentsDefinition = DefaultArgumentsDefinition


@dataclass
class NonOverridableArgumentsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NonOverridableArgumentsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NonOverridableArgumentsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NonOverridableArgumentsDefinition = NonOverridableArgumentsDefinition


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
class CommandDefinition(BaseModel):
    Name: Optional[str]
    PythonVersion: Optional[str]
    ScriptLocation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CommandDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CommandDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PythonVersion=json_data.get("PythonVersion"),
            ScriptLocation=json_data.get("ScriptLocation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CommandDefinition = CommandDefinition


@dataclass
class ExecutionPropertyDefinition(BaseModel):
    MaxConcurrentRuns: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ExecutionPropertyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExecutionPropertyDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxConcurrentRuns=json_data.get("MaxConcurrentRuns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExecutionPropertyDefinition = ExecutionPropertyDefinition


@dataclass
class NotificationPropertyDefinition(BaseModel):
    NotifyDelayAfter: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationPropertyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationPropertyDefinition"]:
        if not json_data:
            return None
        return cls(
            NotifyDelayAfter=json_data.get("NotifyDelayAfter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationPropertyDefinition = NotificationPropertyDefinition


