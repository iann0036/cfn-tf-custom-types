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
    DefaultVersion: Optional[bool]
    Description: Optional[str]
    DomainGroupMoid: Optional[str]
    Id: Optional[str]
    ImplementedTasks: Optional[Sequence["_ImplementedTasksDefinition"]]
    InterfaceTask: Optional[Sequence["_InterfaceTaskDefinition"]]
    InternalProperties: Optional[Sequence["_InternalPropertiesDefinition3"]]
    Label: Optional[str]
    LicenseEntitlement: Optional[str]
    ModTime: Optional[str]
    Moid: Optional[str]
    Name: Optional[str]
    NrVersion: Optional[float]
    ObjectType: Optional[str]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    Properties: Optional[Sequence["_PropertiesDefinition11"]]
    RollbackTasks: Optional[Sequence["_RollbackTasksDefinition2"]]
    SecurePropAccess: Optional[bool]
    SharedScope: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TaskMetadata: Optional[Sequence["_TaskMetadataDefinition"]]
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
            DefaultVersion=json_data.get("DefaultVersion"),
            Description=json_data.get("Description"),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            Id=json_data.get("Id"),
            ImplementedTasks=deserialize_list(json_data.get("ImplementedTasks"), ImplementedTasksDefinition),
            InterfaceTask=deserialize_list(json_data.get("InterfaceTask"), InterfaceTaskDefinition),
            InternalProperties=deserialize_list(json_data.get("InternalProperties"), InternalPropertiesDefinition3),
            Label=json_data.get("Label"),
            LicenseEntitlement=json_data.get("LicenseEntitlement"),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            NrVersion=json_data.get("NrVersion"),
            ObjectType=json_data.get("ObjectType"),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition11),
            RollbackTasks=deserialize_list(json_data.get("RollbackTasks"), RollbackTasksDefinition2),
            SecurePropAccess=json_data.get("SecurePropAccess"),
            SharedScope=json_data.get("SharedScope"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TaskMetadata=deserialize_list(json_data.get("TaskMetadata"), TaskMetadataDefinition),
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
class ImplementedTasksDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImplementedTasksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImplementedTasksDefinition"]:
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
_ImplementedTasksDefinition = ImplementedTasksDefinition


@dataclass
class InterfaceTaskDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterfaceTaskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfaceTaskDefinition"]:
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
_InterfaceTaskDefinition = InterfaceTaskDefinition


@dataclass
class InternalPropertiesDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    BaseTaskType: Optional[str]
    ClassId: Optional[str]
    Constraints: Optional[Sequence["_InternalPropertiesDefinition2"]]
    Internal: Optional[bool]
    ObjectType: Optional[str]
    Owner: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternalPropertiesDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternalPropertiesDefinition3"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            BaseTaskType=json_data.get("BaseTaskType"),
            ClassId=json_data.get("ClassId"),
            Constraints=deserialize_list(json_data.get("Constraints"), InternalPropertiesDefinition2),
            Internal=json_data.get("Internal"),
            ObjectType=json_data.get("ObjectType"),
            Owner=json_data.get("Owner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternalPropertiesDefinition3 = InternalPropertiesDefinition3


@dataclass
class InternalPropertiesDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ObjectType: Optional[str]
    TargetDataType: Optional[Sequence["_InternalPropertiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InternalPropertiesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternalPropertiesDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ObjectType=json_data.get("ObjectType"),
            TargetDataType=deserialize_list(json_data.get("TargetDataType"), InternalPropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternalPropertiesDefinition2 = InternalPropertiesDefinition2


@dataclass
class InternalPropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternalPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternalPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternalPropertiesDefinition = InternalPropertiesDefinition


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
class PropertiesDefinition11(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ExternalMeta: Optional[bool]
    InputDefinition: Optional[Sequence["_PropertiesDefinition5"]]
    ObjectType: Optional[str]
    OutputDefinition: Optional[Sequence["_PropertiesDefinition10"]]
    RetryCount: Optional[float]
    RetryDelay: Optional[float]
    RetryPolicy: Optional[str]
    SupportStatus: Optional[str]
    Timeout: Optional[float]
    TimeoutPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition11"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition11"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ExternalMeta=json_data.get("ExternalMeta"),
            InputDefinition=deserialize_list(json_data.get("InputDefinition"), PropertiesDefinition5),
            ObjectType=json_data.get("ObjectType"),
            OutputDefinition=deserialize_list(json_data.get("OutputDefinition"), PropertiesDefinition10),
            RetryCount=json_data.get("RetryCount"),
            RetryDelay=json_data.get("RetryDelay"),
            RetryPolicy=json_data.get("RetryPolicy"),
            SupportStatus=json_data.get("SupportStatus"),
            Timeout=json_data.get("Timeout"),
            TimeoutPolicy=json_data.get("TimeoutPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition11 = PropertiesDefinition11


@dataclass
class PropertiesDefinition5(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Default: Optional[Sequence["_PropertiesDefinition2"]]
    Description: Optional[str]
    DisplayMeta: Optional[Sequence["_PropertiesDefinition3"]]
    InputParameters: Optional[Sequence["_PropertiesDefinition4"]]
    Label: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Required: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition5"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Default=deserialize_list(json_data.get("Default"), PropertiesDefinition2),
            Description=json_data.get("Description"),
            DisplayMeta=deserialize_list(json_data.get("DisplayMeta"), PropertiesDefinition3),
            InputParameters=deserialize_list(json_data.get("InputParameters"), PropertiesDefinition4),
            Label=json_data.get("Label"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Required=json_data.get("Required"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition5 = PropertiesDefinition5


@dataclass
class PropertiesDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    IsValueSet: Optional[bool]
    ObjectType: Optional[str]
    Override: Optional[bool]
    Value: Optional[Sequence["_PropertiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            IsValueSet=json_data.get("IsValueSet"),
            ObjectType=json_data.get("ObjectType"),
            Override=json_data.get("Override"),
            Value=deserialize_list(json_data.get("Value"), PropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition2 = PropertiesDefinition2


@dataclass
class PropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition = PropertiesDefinition


@dataclass
class PropertiesDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InventorySelector: Optional[bool]
    ObjectType: Optional[str]
    WidgetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition3"]:
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
_PropertiesDefinition3 = PropertiesDefinition3


@dataclass
class PropertiesDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition4 = PropertiesDefinition4


@dataclass
class PropertiesDefinition10(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Default: Optional[Sequence["_PropertiesDefinition7"]]
    Description: Optional[str]
    DisplayMeta: Optional[Sequence["_PropertiesDefinition8"]]
    InputParameters: Optional[Sequence["_PropertiesDefinition9"]]
    Label: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Required: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition10"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition10"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Default=deserialize_list(json_data.get("Default"), PropertiesDefinition7),
            Description=json_data.get("Description"),
            DisplayMeta=deserialize_list(json_data.get("DisplayMeta"), PropertiesDefinition8),
            InputParameters=deserialize_list(json_data.get("InputParameters"), PropertiesDefinition9),
            Label=json_data.get("Label"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Required=json_data.get("Required"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition10 = PropertiesDefinition10


@dataclass
class PropertiesDefinition7(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    IsValueSet: Optional[bool]
    ObjectType: Optional[str]
    Override: Optional[bool]
    Value: Optional[Sequence["_PropertiesDefinition6"]]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition7"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition7"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            IsValueSet=json_data.get("IsValueSet"),
            ObjectType=json_data.get("ObjectType"),
            Override=json_data.get("Override"),
            Value=deserialize_list(json_data.get("Value"), PropertiesDefinition6),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition7 = PropertiesDefinition7


@dataclass
class PropertiesDefinition6(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition6"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition6 = PropertiesDefinition6


@dataclass
class PropertiesDefinition8(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InventorySelector: Optional[bool]
    ObjectType: Optional[str]
    WidgetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition8"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition8"]:
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
_PropertiesDefinition8 = PropertiesDefinition8


@dataclass
class PropertiesDefinition9(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition9"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition9"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition9 = PropertiesDefinition9


@dataclass
class RollbackTasksDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    CatalogMoid: Optional[str]
    ClassId: Optional[str]
    Description: Optional[str]
    InputParameters: Optional[Sequence["_RollbackTasksDefinition"]]
    Name: Optional[str]
    NrVersion: Optional[float]
    ObjectType: Optional[str]
    TaskMoid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RollbackTasksDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RollbackTasksDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            CatalogMoid=json_data.get("CatalogMoid"),
            ClassId=json_data.get("ClassId"),
            Description=json_data.get("Description"),
            InputParameters=deserialize_list(json_data.get("InputParameters"), RollbackTasksDefinition),
            Name=json_data.get("Name"),
            NrVersion=json_data.get("NrVersion"),
            ObjectType=json_data.get("ObjectType"),
            TaskMoid=json_data.get("TaskMoid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RollbackTasksDefinition2 = RollbackTasksDefinition2


@dataclass
class RollbackTasksDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RollbackTasksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RollbackTasksDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RollbackTasksDefinition = RollbackTasksDefinition


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
class TaskMetadataDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaskMetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskMetadataDefinition"]:
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
_TaskMetadataDefinition = TaskMetadataDefinition


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


