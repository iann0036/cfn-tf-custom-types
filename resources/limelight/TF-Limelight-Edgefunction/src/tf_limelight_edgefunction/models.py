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
    CanDebug: Optional[bool]
    Description: Optional[str]
    FunctionArchive: Optional[str]
    FunctionSha256: Optional[str]
    Handler: Optional[str]
    Id: Optional[str]
    Memory: Optional[float]
    Name: Optional[str]
    ReservedConcurrency: Optional[float]
    RevisionId: Optional[float]
    Runtime: Optional[str]
    Shortname: Optional[str]
    Timeout: Optional[float]
    EnvironmentVariable: Optional[Sequence["_EnvironmentVariableDefinition"]]

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
            CanDebug=json_data.get("CanDebug"),
            Description=json_data.get("Description"),
            FunctionArchive=json_data.get("FunctionArchive"),
            FunctionSha256=json_data.get("FunctionSha256"),
            Handler=json_data.get("Handler"),
            Id=json_data.get("Id"),
            Memory=json_data.get("Memory"),
            Name=json_data.get("Name"),
            ReservedConcurrency=json_data.get("ReservedConcurrency"),
            RevisionId=json_data.get("RevisionId"),
            Runtime=json_data.get("Runtime"),
            Shortname=json_data.get("Shortname"),
            Timeout=json_data.get("Timeout"),
            EnvironmentVariable=deserialize_list(json_data.get("EnvironmentVariable"), EnvironmentVariableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EnvironmentVariableDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentVariableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentVariableDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentVariableDefinition = EnvironmentVariableDefinition


