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
    DefaultItem: Optional[bool]
    Description: Optional[str]
    DiskProperties: Optional[Sequence["_DiskPropertiesDefinition"]]
    DiskTargetProperties: Optional[Sequence["_DiskTargetPropertiesDefinition"]]
    ExternalRegionId: Optional[str]
    Id: Optional[str]
    Links: Optional[Sequence["_LinksDefinition"]]
    Name: Optional[str]
    OrgId: Optional[str]
    Owner: Optional[str]
    RegionId: Optional[str]
    SupportsEncryption: Optional[bool]
    UpdatedAt: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]

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
            DefaultItem=json_data.get("DefaultItem"),
            Description=json_data.get("Description"),
            DiskProperties=deserialize_list(json_data.get("DiskProperties"), DiskPropertiesDefinition),
            DiskTargetProperties=deserialize_list(json_data.get("DiskTargetProperties"), DiskTargetPropertiesDefinition),
            ExternalRegionId=json_data.get("ExternalRegionId"),
            Id=json_data.get("Id"),
            Links=deserialize_list(json_data.get("Links"), LinksDefinition),
            Name=json_data.get("Name"),
            OrgId=json_data.get("OrgId"),
            Owner=json_data.get("Owner"),
            RegionId=json_data.get("RegionId"),
            SupportsEncryption=json_data.get("SupportsEncryption"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DiskPropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskPropertiesDefinition = DiskPropertiesDefinition


@dataclass
class DiskTargetPropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskTargetPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskTargetPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskTargetPropertiesDefinition = DiskTargetPropertiesDefinition


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


