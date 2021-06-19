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
    AccountMoid: Optional[str]
    AdditionalProperties: Optional[str]
    Ancestors: Optional[Sequence["_AncestorsDefinition"]]
    Catalog: Optional[Sequence["_CatalogDefinition"]]
    ClassId: Optional[str]
    CreateTime: Optional[str]
    Description: Optional[str]
    DomainGroupMoid: Optional[str]
    DownloadCount: Optional[float]
    Id: Optional[str]
    ImportAction: Optional[str]
    ImportState: Optional[str]
    ImportedTime: Optional[str]
    LastAccessTime: Optional[str]
    Md5eTag: Optional[str]
    Md5sum: Optional[str]
    ModTime: Optional[str]
    Moid: Optional[str]
    Name: Optional[str]
    NrSource: Optional[Sequence["_NrSourceDefinition"]]
    NrVersion: Optional[str]
    ObjectType: Optional[str]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    ReleaseDate: Optional[str]
    Sha512sum: Optional[str]
    SharedScope: Optional[str]
    Size: Optional[float]
    SoftwareAdvisoryUrl: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Vendor: Optional[str]
    VersionContext: Optional[Sequence["_VersionContextDefinition3"]]

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
            AccountMoid=json_data.get("AccountMoid"),
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Ancestors=deserialize_list(json_data.get("Ancestors"), AncestorsDefinition),
            Catalog=deserialize_list(json_data.get("Catalog"), CatalogDefinition),
            ClassId=json_data.get("ClassId"),
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            DownloadCount=json_data.get("DownloadCount"),
            Id=json_data.get("Id"),
            ImportAction=json_data.get("ImportAction"),
            ImportState=json_data.get("ImportState"),
            ImportedTime=json_data.get("ImportedTime"),
            LastAccessTime=json_data.get("LastAccessTime"),
            Md5eTag=json_data.get("Md5eTag"),
            Md5sum=json_data.get("Md5sum"),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            NrSource=deserialize_list(json_data.get("NrSource"), NrSourceDefinition),
            NrVersion=json_data.get("NrVersion"),
            ObjectType=json_data.get("ObjectType"),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            ReleaseDate=json_data.get("ReleaseDate"),
            Sha512sum=json_data.get("Sha512sum"),
            SharedScope=json_data.get("SharedScope"),
            Size=json_data.get("Size"),
            SoftwareAdvisoryUrl=json_data.get("SoftwareAdvisoryUrl"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Vendor=json_data.get("Vendor"),
            VersionContext=deserialize_list(json_data.get("VersionContext"), VersionContextDefinition3),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AncestorsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AncestorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AncestorsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AncestorsDefinition = AncestorsDefinition


@dataclass
class CatalogDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CatalogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CatalogDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CatalogDefinition = CatalogDefinition


@dataclass
class NrSourceDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NrSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NrSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NrSourceDefinition = NrSourceDefinition


@dataclass
class ParentDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParentDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParentDefinition = ParentDefinition


@dataclass
class PermissionResourcesDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PermissionResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PermissionResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PermissionResourcesDefinition = PermissionResourcesDefinition


@dataclass
class TagsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
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
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class VersionContextDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InterestedMos: Optional[Sequence["_VersionContextDefinition"]]
    NrVersion: Optional[str]
    ObjectType: Optional[str]
    RefMo: Optional[Sequence["_VersionContextDefinition2"]]
    Timestamp: Optional[str]
    VersionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition3"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            InterestedMos=deserialize_list(json_data.get("InterestedMos"), VersionContextDefinition),
            NrVersion=json_data.get("NrVersion"),
            ObjectType=json_data.get("ObjectType"),
            RefMo=deserialize_list(json_data.get("RefMo"), VersionContextDefinition2),
            Timestamp=json_data.get("Timestamp"),
            VersionType=json_data.get("VersionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition3 = VersionContextDefinition3


@dataclass
class VersionContextDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition = VersionContextDefinition


@dataclass
class VersionContextDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition2 = VersionContextDefinition2


