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
    DisplayName: Optional[str]
    Id: Optional[str]
    NsxId: Optional[str]
    Path: Optional[str]
    Revision: Optional[float]
    AppId: Optional[Sequence["_AppIdDefinition"]]
    DomainName: Optional[Sequence["_DomainNameDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]
    UrlCategory: Optional[Sequence["_UrlCategoryDefinition"]]

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
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            NsxId=json_data.get("NsxId"),
            Path=json_data.get("Path"),
            Revision=json_data.get("Revision"),
            AppId=deserialize_list(json_data.get("AppId"), AppIdDefinition),
            DomainName=deserialize_list(json_data.get("DomainName"), DomainNameDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
            UrlCategory=deserialize_list(json_data.get("UrlCategory"), UrlCategoryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppIdDefinition(BaseModel):
    Description: Optional[str]
    Value: Optional[Sequence[str]]
    SubAttribute: Optional[Sequence["_SubAttributeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AppIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Value=json_data.get("Value"),
            SubAttribute=deserialize_list(json_data.get("SubAttribute"), SubAttributeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppIdDefinition = AppIdDefinition


@dataclass
class SubAttributeDefinition(BaseModel):
    CifsSmbVersion: Optional[Sequence[str]]
    TlsCipherSuite: Optional[Sequence[str]]
    TlsVersion: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SubAttributeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubAttributeDefinition"]:
        if not json_data:
            return None
        return cls(
            CifsSmbVersion=json_data.get("CifsSmbVersion"),
            TlsCipherSuite=json_data.get("TlsCipherSuite"),
            TlsVersion=json_data.get("TlsVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubAttributeDefinition = SubAttributeDefinition


@dataclass
class DomainNameDefinition(BaseModel):
    Description: Optional[str]
    Value: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DomainNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainNameDefinition = DomainNameDefinition


@dataclass
class TagDefinition(BaseModel):
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


@dataclass
class UrlCategoryDefinition(BaseModel):
    Description: Optional[str]
    Value: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_UrlCategoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlCategoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlCategoryDefinition = UrlCategoryDefinition


