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
    CaseSensitivity: Optional[str]
    Color: Optional[float]
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    Header: Optional[str]
    HeaderName: Optional[str]
    Host: Optional[str]
    HostRegex: Optional[str]
    Id: Optional[str]
    Method: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Query: Optional[str]
    Referrer: Optional[str]
    Type: Optional[str]
    Ua: Optional[str]
    Uuid: Optional[str]
    Vdomparam: Optional[str]
    Visibility: Optional[str]
    Category: Optional[Sequence["_CategoryDefinition"]]
    HeaderGroup: Optional[Sequence["_HeaderGroupDefinition"]]
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
            CaseSensitivity=json_data.get("CaseSensitivity"),
            Color=json_data.get("Color"),
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Header=json_data.get("Header"),
            HeaderName=json_data.get("HeaderName"),
            Host=json_data.get("Host"),
            HostRegex=json_data.get("HostRegex"),
            Id=json_data.get("Id"),
            Method=json_data.get("Method"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Query=json_data.get("Query"),
            Referrer=json_data.get("Referrer"),
            Type=json_data.get("Type"),
            Ua=json_data.get("Ua"),
            Uuid=json_data.get("Uuid"),
            Vdomparam=json_data.get("Vdomparam"),
            Visibility=json_data.get("Visibility"),
            Category=deserialize_list(json_data.get("Category"), CategoryDefinition),
            HeaderGroup=deserialize_list(json_data.get("HeaderGroup"), HeaderGroupDefinition),
            Tagging=deserialize_list(json_data.get("Tagging"), TaggingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CategoryDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CategoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoryDefinition = CategoryDefinition


@dataclass
class HeaderGroupDefinition(BaseModel):
    CaseSensitivity: Optional[str]
    Header: Optional[str]
    HeaderName: Optional[str]
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitivity=json_data.get("CaseSensitivity"),
            Header=json_data.get("Header"),
            HeaderName=json_data.get("HeaderName"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderGroupDefinition = HeaderGroupDefinition


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


