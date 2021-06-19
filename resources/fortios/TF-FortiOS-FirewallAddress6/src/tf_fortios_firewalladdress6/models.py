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
    CacheTtl: Optional[float]
    Color: Optional[float]
    Comment: Optional[str]
    Country: Optional[str]
    DynamicSortSubtable: Optional[str]
    EndIp: Optional[str]
    EndMac: Optional[str]
    Fqdn: Optional[str]
    Host: Optional[str]
    HostType: Optional[str]
    Id: Optional[str]
    Ip6: Optional[str]
    Name: Optional[str]
    ObjId: Optional[str]
    Sdn: Optional[str]
    StartIp: Optional[str]
    StartMac: Optional[str]
    Template: Optional[str]
    Type: Optional[str]
    Uuid: Optional[str]
    Vdomparam: Optional[str]
    Visibility: Optional[str]
    List: Optional[Sequence["_ListDefinition"]]
    SubnetSegment: Optional[Sequence["_SubnetSegmentDefinition"]]
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
            CacheTtl=json_data.get("CacheTtl"),
            Color=json_data.get("Color"),
            Comment=json_data.get("Comment"),
            Country=json_data.get("Country"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EndIp=json_data.get("EndIp"),
            EndMac=json_data.get("EndMac"),
            Fqdn=json_data.get("Fqdn"),
            Host=json_data.get("Host"),
            HostType=json_data.get("HostType"),
            Id=json_data.get("Id"),
            Ip6=json_data.get("Ip6"),
            Name=json_data.get("Name"),
            ObjId=json_data.get("ObjId"),
            Sdn=json_data.get("Sdn"),
            StartIp=json_data.get("StartIp"),
            StartMac=json_data.get("StartMac"),
            Template=json_data.get("Template"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
            Vdomparam=json_data.get("Vdomparam"),
            Visibility=json_data.get("Visibility"),
            List=deserialize_list(json_data.get("List"), ListDefinition),
            SubnetSegment=deserialize_list(json_data.get("SubnetSegment"), SubnetSegmentDefinition),
            Tagging=deserialize_list(json_data.get("Tagging"), TaggingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ListDefinition(BaseModel):
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListDefinition = ListDefinition


@dataclass
class SubnetSegmentDefinition(BaseModel):
    Name: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetSegmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetSegmentDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetSegmentDefinition = SubnetSegmentDefinition


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


