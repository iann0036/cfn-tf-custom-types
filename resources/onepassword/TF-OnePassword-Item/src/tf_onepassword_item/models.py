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
    Category: Optional[str]
    Database: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    Password: Optional[str]
    Port: Optional[str]
    Tags: Optional[Sequence[str]]
    Title: Optional[str]
    Type: Optional[str]
    Url: Optional[str]
    Username: Optional[str]
    Uuid: Optional[str]
    Vault: Optional[str]
    PasswordRecipe: Optional[Sequence["_PasswordRecipeDefinition"]]
    Section: Optional[Sequence["_SectionDefinition"]]

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
            Category=json_data.get("Category"),
            Database=json_data.get("Database"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Tags=json_data.get("Tags"),
            Title=json_data.get("Title"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
            Uuid=json_data.get("Uuid"),
            Vault=json_data.get("Vault"),
            PasswordRecipe=deserialize_list(json_data.get("PasswordRecipe"), PasswordRecipeDefinition),
            Section=deserialize_list(json_data.get("Section"), SectionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PasswordRecipeDefinition(BaseModel):
    Digits: Optional[bool]
    Length: Optional[float]
    Letters: Optional[bool]
    Symbols: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PasswordRecipeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PasswordRecipeDefinition"]:
        if not json_data:
            return None
        return cls(
            Digits=json_data.get("Digits"),
            Length=json_data.get("Length"),
            Letters=json_data.get("Letters"),
            Symbols=json_data.get("Symbols"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PasswordRecipeDefinition = PasswordRecipeDefinition


@dataclass
class SectionDefinition(BaseModel):
    Label: Optional[str]
    Field: Optional[Sequence["_FieldDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SectionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SectionDefinition"]:
        if not json_data:
            return None
        return cls(
            Label=json_data.get("Label"),
            Field=deserialize_list(json_data.get("Field"), FieldDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SectionDefinition = SectionDefinition


@dataclass
class FieldDefinition(BaseModel):
    Id: Optional[str]
    Label: Optional[str]
    Purpose: Optional[str]
    Type: Optional[str]
    Value: Optional[str]
    PasswordRecipe: Optional[Sequence["_PasswordRecipeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FieldDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Label=json_data.get("Label"),
            Purpose=json_data.get("Purpose"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
            PasswordRecipe=deserialize_list(json_data.get("PasswordRecipe"), PasswordRecipeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldDefinition = FieldDefinition


