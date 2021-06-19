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
    CreationTime: Optional[float]
    DatasetId: Optional[str]
    DefinitionBody: Optional[str]
    Description: Optional[str]
    DeterminismLevel: Optional[str]
    Id: Optional[str]
    ImportedLibraries: Optional[Sequence[str]]
    Language: Optional[str]
    LastModifiedTime: Optional[float]
    Project: Optional[str]
    ReturnType: Optional[str]
    RoutineId: Optional[str]
    RoutineType: Optional[str]
    Arguments: Optional[Sequence["_ArgumentsDefinition"]]
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
            CreationTime=json_data.get("CreationTime"),
            DatasetId=json_data.get("DatasetId"),
            DefinitionBody=json_data.get("DefinitionBody"),
            Description=json_data.get("Description"),
            DeterminismLevel=json_data.get("DeterminismLevel"),
            Id=json_data.get("Id"),
            ImportedLibraries=json_data.get("ImportedLibraries"),
            Language=json_data.get("Language"),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            Project=json_data.get("Project"),
            ReturnType=json_data.get("ReturnType"),
            RoutineId=json_data.get("RoutineId"),
            RoutineType=json_data.get("RoutineType"),
            Arguments=deserialize_list(json_data.get("Arguments"), ArgumentsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ArgumentsDefinition(BaseModel):
    ArgumentKind: Optional[str]
    DataType: Optional[str]
    Mode: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ArgumentsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArgumentsDefinition"]:
        if not json_data:
            return None
        return cls(
            ArgumentKind=json_data.get("ArgumentKind"),
            DataType=json_data.get("DataType"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArgumentsDefinition = ArgumentsDefinition


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


