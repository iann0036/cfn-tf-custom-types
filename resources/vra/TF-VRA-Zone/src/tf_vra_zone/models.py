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
    CloudAccountId: Optional[str]
    CreatedAt: Optional[str]
    CustomProperties: Optional[Sequence["_CustomPropertiesDefinition"]]
    Description: Optional[str]
    ExternalRegionId: Optional[str]
    Folder: Optional[str]
    Id: Optional[str]
    Links: Optional[Sequence["_LinksDefinition"]]
    Name: Optional[str]
    OrgId: Optional[str]
    Owner: Optional[str]
    PlacementPolicy: Optional[str]
    RegionId: Optional[str]
    UpdatedAt: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsToMatch: Optional[Sequence["_TagsToMatchDefinition"]]

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
            CloudAccountId=json_data.get("CloudAccountId"),
            CreatedAt=json_data.get("CreatedAt"),
            CustomProperties=deserialize_list(json_data.get("CustomProperties"), CustomPropertiesDefinition),
            Description=json_data.get("Description"),
            ExternalRegionId=json_data.get("ExternalRegionId"),
            Folder=json_data.get("Folder"),
            Id=json_data.get("Id"),
            Links=deserialize_list(json_data.get("Links"), LinksDefinition),
            Name=json_data.get("Name"),
            OrgId=json_data.get("OrgId"),
            Owner=json_data.get("Owner"),
            PlacementPolicy=json_data.get("PlacementPolicy"),
            RegionId=json_data.get("RegionId"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsToMatch=deserialize_list(json_data.get("TagsToMatch"), TagsToMatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomPropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomPropertiesDefinition = CustomPropertiesDefinition


@dataclass
class LinksDefinition(BaseModel):
    Href: Optional[str]
    Hrefs: Optional[Sequence[str]]
    Rel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LinksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinksDefinition"]:
        if not json_data:
            return None
        return cls(
            Href=json_data.get("Href"),
            Hrefs=json_data.get("Hrefs"),
            Rel=json_data.get("Rel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinksDefinition = LinksDefinition


@dataclass
class TagsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsToMatchDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsToMatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsToMatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsToMatchDefinition = TagsToMatchDefinition


