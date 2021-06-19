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
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ParseTestId: Optional[str]
    Secure: Optional[bool]
    Tags: Optional[Sequence[str]]
    Value: Optional[str]
    ParseTestOptions: Optional[Sequence["_ParseTestOptionsDefinition"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ParseTestId=json_data.get("ParseTestId"),
            Secure=json_data.get("Secure"),
            Tags=json_data.get("Tags"),
            Value=json_data.get("Value"),
            ParseTestOptions=deserialize_list(json_data.get("ParseTestOptions"), ParseTestOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ParseTestOptionsDefinition(BaseModel):
    Field: Optional[str]
    Type: Optional[str]
    Parser: Optional[Sequence["_ParserDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ParseTestOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParseTestOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Field=json_data.get("Field"),
            Type=json_data.get("Type"),
            Parser=deserialize_list(json_data.get("Parser"), ParserDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParseTestOptionsDefinition = ParseTestOptionsDefinition


@dataclass
class ParserDefinition(BaseModel):
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParserDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParserDefinition = ParserDefinition


