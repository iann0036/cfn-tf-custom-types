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
    Distributions: Optional[Sequence["_DistributionsDefinition"]]
    DomainGroupMoid: Optional[str]
    FileContent: Optional[str]
    Id: Optional[str]
    Internal: Optional[bool]
    ModTime: Optional[str]
    Moid: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    Placeholders: Optional[Sequence["_PlaceholdersDefinition11"]]
    SharedScope: Optional[str]
    Supported: Optional[bool]
    Tags: Optional[Sequence["_TagsDefinition"]]
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
            Distributions=deserialize_list(json_data.get("Distributions"), DistributionsDefinition),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            FileContent=json_data.get("FileContent"),
            Id=json_data.get("Id"),
            Internal=json_data.get("Internal"),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            Placeholders=deserialize_list(json_data.get("Placeholders"), PlaceholdersDefinition11),
            SharedScope=json_data.get("SharedScope"),
            Supported=json_data.get("Supported"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
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
class DistributionsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DistributionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DistributionsDefinition"]:
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
_DistributionsDefinition = DistributionsDefinition


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
class PlaceholdersDefinition11(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    IsValueSet: Optional[bool]
    ObjectType: Optional[str]
    Type: Optional[Sequence["_PlaceholdersDefinition9"]]
    Value: Optional[Sequence["_PlaceholdersDefinition10"]]

    @classmethod
    def _deserialize(
        cls: Type["_PlaceholdersDefinition11"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlaceholdersDefinition11"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            IsValueSet=json_data.get("IsValueSet"),
            ObjectType=json_data.get("ObjectType"),
            Type=deserialize_list(json_data.get("Type"), PlaceholdersDefinition9),
            Value=deserialize_list(json_data.get("Value"), PlaceholdersDefinition10),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlaceholdersDefinition11 = PlaceholdersDefinition11


@dataclass
class PlaceholdersDefinition9(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Default: Optional[Sequence["_PlaceholdersDefinition2"]]
    Description: Optional[str]
    DisplayMeta: Optional[Sequence["_PlaceholdersDefinition3"]]
    InputParameters: Optional[Sequence["_PlaceholdersDefinition4"]]
    Label: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Properties: Optional[Sequence["_PlaceholdersDefinition8"]]
    Required: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PlaceholdersDefinition9"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlaceholdersDefinition9"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Default=deserialize_list(json_data.get("Default"), PlaceholdersDefinition2),
            Description=json_data.get("Description"),
            DisplayMeta=deserialize_list(json_data.get("DisplayMeta"), PlaceholdersDefinition3),
            InputParameters=deserialize_list(json_data.get("InputParameters"), PlaceholdersDefinition4),
            Label=json_data.get("Label"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Properties=deserialize_list(json_data.get("Properties"), PlaceholdersDefinition8),
            Required=json_data.get("Required"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlaceholdersDefinition9 = PlaceholdersDefinition9


@dataclass
class PlaceholdersDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    IsValueSet: Optional[bool]
    ObjectType: Optional[str]
    Override: Optional[bool]
    Value: Optional[Sequence["_PlaceholdersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PlaceholdersDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlaceholdersDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            IsValueSet=json_data.get("IsValueSet"),
            ObjectType=json_data.get("ObjectType"),
            Override=json_data.get("Override"),
            Value=deserialize_list(json_data.get("Value"), PlaceholdersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlaceholdersDefinition2 = PlaceholdersDefinition2


@dataclass
class PlaceholdersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlaceholdersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlaceholdersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlaceholdersDefinition = PlaceholdersDefinition


@dataclass
class PlaceholdersDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InventorySelector: Optional[bool]
    ObjectType: Optional[str]
    WidgetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlaceholdersDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlaceholdersDefinition3"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            InventorySelector=json_data.get("InventorySelector"),
            ObjectType=json_data.get("ObjectType"),
            WidgetType=json_data.get("WidgetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlaceholdersDefinition3 = PlaceholdersDefinition3


@dataclass
class PlaceholdersDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlaceholdersDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlaceholdersDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlaceholdersDefinition4 = PlaceholdersDefinition4


@dataclass
class PlaceholdersDefinition8(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Constraints: Optional[Sequence["_PlaceholdersDefinition6"]]
    InventorySelector: Optional[Sequence["_PlaceholdersDefinition7"]]
    ObjectType: Optional[str]
    Secure: Optional[bool]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlaceholdersDefinition8"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlaceholdersDefinition8"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Constraints=deserialize_list(json_data.get("Constraints"), PlaceholdersDefinition6),
            InventorySelector=deserialize_list(json_data.get("InventorySelector"), PlaceholdersDefinition7),
            ObjectType=json_data.get("ObjectType"),
            Secure=json_data.get("Secure"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlaceholdersDefinition8 = PlaceholdersDefinition8


@dataclass
class PlaceholdersDefinition6(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    EnumList: Optional[Sequence["_PlaceholdersDefinition5"]]
    Max: Optional[float]
    Min: Optional[float]
    ObjectType: Optional[str]
    Regex: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlaceholdersDefinition6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlaceholdersDefinition6"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            EnumList=deserialize_list(json_data.get("EnumList"), PlaceholdersDefinition5),
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
            ObjectType=json_data.get("ObjectType"),
            Regex=json_data.get("Regex"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlaceholdersDefinition6 = PlaceholdersDefinition6


@dataclass
class PlaceholdersDefinition5(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Label: Optional[str]
    ObjectType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlaceholdersDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlaceholdersDefinition5"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Label=json_data.get("Label"),
            ObjectType=json_data.get("ObjectType"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlaceholdersDefinition5 = PlaceholdersDefinition5


@dataclass
class PlaceholdersDefinition7(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    DisplayAttributes: Optional[Sequence[str]]
    ObjectType: Optional[str]
    Selector: Optional[str]
    ValueAttribute: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlaceholdersDefinition7"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlaceholdersDefinition7"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            DisplayAttributes=json_data.get("DisplayAttributes"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
            ValueAttribute=json_data.get("ValueAttribute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlaceholdersDefinition7 = PlaceholdersDefinition7


@dataclass
class PlaceholdersDefinition10(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlaceholdersDefinition10"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlaceholdersDefinition10"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlaceholdersDefinition10 = PlaceholdersDefinition10


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


