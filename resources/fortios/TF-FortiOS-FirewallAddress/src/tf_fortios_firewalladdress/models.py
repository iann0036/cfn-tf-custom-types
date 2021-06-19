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
    AssociatedInterface: Optional[str]
    CacheTtl: Optional[float]
    ClearpassSpt: Optional[str]
    Color: Optional[float]
    Comment: Optional[str]
    Country: Optional[str]
    DynamicSortSubtable: Optional[str]
    EndIp: Optional[str]
    EndMac: Optional[str]
    EpgName: Optional[str]
    Filter: Optional[str]
    Fqdn: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    Name: Optional[str]
    NodeIpOnly: Optional[str]
    ObjId: Optional[str]
    ObjTag: Optional[str]
    ObjType: Optional[str]
    Organization: Optional[str]
    PolicyGroup: Optional[str]
    Sdn: Optional[str]
    SdnAddrType: Optional[str]
    SdnTag: Optional[str]
    StartIp: Optional[str]
    StartMac: Optional[str]
    SubType: Optional[str]
    Subnet: Optional[str]
    SubnetName: Optional[str]
    Tenant: Optional[str]
    Type: Optional[str]
    Uuid: Optional[str]
    Vdomparam: Optional[str]
    Visibility: Optional[str]
    Wildcard: Optional[str]
    WildcardFqdn: Optional[str]
    FssoGroup: Optional[Sequence["_FssoGroupDefinition"]]
    List: Optional[Sequence["_ListDefinition"]]
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
            AssociatedInterface=json_data.get("AssociatedInterface"),
            CacheTtl=json_data.get("CacheTtl"),
            ClearpassSpt=json_data.get("ClearpassSpt"),
            Color=json_data.get("Color"),
            Comment=json_data.get("Comment"),
            Country=json_data.get("Country"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EndIp=json_data.get("EndIp"),
            EndMac=json_data.get("EndMac"),
            EpgName=json_data.get("EpgName"),
            Filter=json_data.get("Filter"),
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            Name=json_data.get("Name"),
            NodeIpOnly=json_data.get("NodeIpOnly"),
            ObjId=json_data.get("ObjId"),
            ObjTag=json_data.get("ObjTag"),
            ObjType=json_data.get("ObjType"),
            Organization=json_data.get("Organization"),
            PolicyGroup=json_data.get("PolicyGroup"),
            Sdn=json_data.get("Sdn"),
            SdnAddrType=json_data.get("SdnAddrType"),
            SdnTag=json_data.get("SdnTag"),
            StartIp=json_data.get("StartIp"),
            StartMac=json_data.get("StartMac"),
            SubType=json_data.get("SubType"),
            Subnet=json_data.get("Subnet"),
            SubnetName=json_data.get("SubnetName"),
            Tenant=json_data.get("Tenant"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
            Vdomparam=json_data.get("Vdomparam"),
            Visibility=json_data.get("Visibility"),
            Wildcard=json_data.get("Wildcard"),
            WildcardFqdn=json_data.get("WildcardFqdn"),
            FssoGroup=deserialize_list(json_data.get("FssoGroup"), FssoGroupDefinition),
            List=deserialize_list(json_data.get("List"), ListDefinition),
            Tagging=deserialize_list(json_data.get("Tagging"), TaggingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FssoGroupDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FssoGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FssoGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FssoGroupDefinition = FssoGroupDefinition


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


