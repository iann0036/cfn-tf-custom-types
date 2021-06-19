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
    AllowRouting: Optional[str]
    Color: Optional[float]
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    Exclude: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Type: Optional[str]
    Uuid: Optional[str]
    Vdomparam: Optional[str]
    Visibility: Optional[str]
    ExcludeMember: Optional[Sequence["_ExcludeMemberDefinition"]]
    Member: Optional[Sequence["_MemberDefinition"]]
    Tagging: Optional[Sequence["_TaggingDefinition"]]

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
            AllowRouting=json_data.get("AllowRouting"),
            Color=json_data.get("Color"),
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Exclude=json_data.get("Exclude"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
            Vdomparam=json_data.get("Vdomparam"),
            Visibility=json_data.get("Visibility"),
            ExcludeMember=deserialize_list(json_data.get("ExcludeMember"), ExcludeMemberDefinition),
            Member=deserialize_list(json_data.get("Member"), MemberDefinition),
            Tagging=deserialize_list(json_data.get("Tagging"), TaggingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExcludeMemberDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExcludeMemberDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExcludeMemberDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExcludeMemberDefinition = ExcludeMemberDefinition


@dataclass
class MemberDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MemberDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemberDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemberDefinition = MemberDefinition


@dataclass
class TaggingDefinition(BaseModel):
    Category: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TaggingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaggingDefinition"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Name=json_data.get("Name"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaggingDefinition = TaggingDefinition


@dataclass
class TagsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


