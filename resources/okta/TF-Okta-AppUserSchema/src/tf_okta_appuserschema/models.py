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
    AppId: Optional[str]
    ArrayEnum: Optional[Sequence[str]]
    ArrayType: Optional[str]
    Description: Optional[str]
    Enum: Optional[Sequence[str]]
    ExternalName: Optional[str]
    ExternalNamespace: Optional[str]
    Id: Optional[str]
    Index: Optional[str]
    Master: Optional[str]
    MaxLength: Optional[float]
    MinLength: Optional[float]
    Pattern: Optional[str]
    Permissions: Optional[str]
    Required: Optional[bool]
    Scope: Optional[str]
    Title: Optional[str]
    Type: Optional[str]
    Union: Optional[bool]
    Unique: Optional[str]
    UserType: Optional[str]
    ArrayOneOf: Optional[Sequence["_ArrayOneOfDefinition"]]
    OneOf: Optional[Sequence["_OneOfDefinition"]]

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
            AppId=json_data.get("AppId"),
            ArrayEnum=json_data.get("ArrayEnum"),
            ArrayType=json_data.get("ArrayType"),
            Description=json_data.get("Description"),
            Enum=json_data.get("Enum"),
            ExternalName=json_data.get("ExternalName"),
            ExternalNamespace=json_data.get("ExternalNamespace"),
            Id=json_data.get("Id"),
            Index=json_data.get("Index"),
            Master=json_data.get("Master"),
            MaxLength=json_data.get("MaxLength"),
            MinLength=json_data.get("MinLength"),
            Pattern=json_data.get("Pattern"),
            Permissions=json_data.get("Permissions"),
            Required=json_data.get("Required"),
            Scope=json_data.get("Scope"),
            Title=json_data.get("Title"),
            Type=json_data.get("Type"),
            Union=json_data.get("Union"),
            Unique=json_data.get("Unique"),
            UserType=json_data.get("UserType"),
            ArrayOneOf=deserialize_list(json_data.get("ArrayOneOf"), ArrayOneOfDefinition),
            OneOf=deserialize_list(json_data.get("OneOf"), OneOfDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ArrayOneOfDefinition(BaseModel):
    Const: Optional[str]
    Title: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ArrayOneOfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArrayOneOfDefinition"]:
        if not json_data:
            return None
        return cls(
            Const=json_data.get("Const"),
            Title=json_data.get("Title"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArrayOneOfDefinition = ArrayOneOfDefinition


@dataclass
class OneOfDefinition(BaseModel):
    Const: Optional[str]
    Title: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OneOfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OneOfDefinition"]:
        if not json_data:
            return None
        return cls(
            Const=json_data.get("Const"),
            Title=json_data.get("Title"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OneOfDefinition = OneOfDefinition


