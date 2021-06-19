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
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    ProcessGroups: Optional[Sequence[str]]
    QueueEntryPoint: Optional[bool]
    QueueEntryPointType: Optional[str]
    Technology: Optional[str]
    Unknowns: Optional[str]
    Rule: Optional[Sequence["_RuleDefinition"]]

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
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ProcessGroups=json_data.get("ProcessGroups"),
            QueueEntryPoint=json_data.get("QueueEntryPoint"),
            QueueEntryPointType=json_data.get("QueueEntryPointType"),
            Technology=json_data.get("Technology"),
            Unknowns=json_data.get("Unknowns"),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RuleDefinition(BaseModel):
    Annotations: Optional[Sequence[str]]
    Enabled: Optional[bool]
    Unknowns: Optional[str]
    Class: Optional[Sequence["_ClassDefinition"]]
    File: Optional[Sequence["_FileDefinition"]]
    Method: Optional[Sequence["_MethodDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Annotations=json_data.get("Annotations"),
            Enabled=json_data.get("Enabled"),
            Unknowns=json_data.get("Unknowns"),
            Class=deserialize_list(json_data.get("Class"), ClassDefinition),
            File=deserialize_list(json_data.get("File"), FileDefinition),
            Method=deserialize_list(json_data.get("Method"), MethodDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class ClassDefinition(BaseModel):
    Match: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClassDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClassDefinition"]:
        if not json_data:
            return None
        return cls(
            Match=json_data.get("Match"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClassDefinition = ClassDefinition


@dataclass
class FileDefinition(BaseModel):
    Match: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileDefinition"]:
        if not json_data:
            return None
        return cls(
            Match=json_data.get("Match"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileDefinition = FileDefinition


@dataclass
class MethodDefinition(BaseModel):
    Arguments: Optional[Sequence[str]]
    Name: Optional[str]
    Returns: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MethodDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MethodDefinition"]:
        if not json_data:
            return None
        return cls(
            Arguments=json_data.get("Arguments"),
            Name=json_data.get("Name"),
            Returns=json_data.get("Returns"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MethodDefinition = MethodDefinition


