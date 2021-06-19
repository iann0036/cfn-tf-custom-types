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
    ClassId: Optional[str]
    ConfigurationFile: Optional[Sequence["_ConfigurationFileDefinition"]]
    CreateTime: Optional[str]
    DomainGroupMoid: Optional[str]
    FileContent: Optional[str]
    GlobalConfig: Optional[Sequence["_GlobalConfigDefinition2"]]
    Id: Optional[str]
    IsFileContentSet: Optional[bool]
    ModTime: Optional[str]
    Moid: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    OperState: Optional[str]
    Organization: Optional[Sequence["_OrganizationDefinition"]]
    OsImage: Optional[Sequence["_OsImageDefinition"]]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    ScuImage: Optional[Sequence["_ScuImageDefinition"]]
    ServerConfigs: Optional[Sequence["_ServerConfigsDefinition15"]]
    Servers: Optional[Sequence["_ServersDefinition"]]
    SharedScope: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    ValidationInfos: Optional[Sequence["_ValidationInfosDefinition"]]
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
            ClassId=json_data.get("ClassId"),
            ConfigurationFile=deserialize_list(json_data.get("ConfigurationFile"), ConfigurationFileDefinition),
            CreateTime=json_data.get("CreateTime"),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            FileContent=json_data.get("FileContent"),
            GlobalConfig=deserialize_list(json_data.get("GlobalConfig"), GlobalConfigDefinition2),
            Id=json_data.get("Id"),
            IsFileContentSet=json_data.get("IsFileContentSet"),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            OperState=json_data.get("OperState"),
            Organization=deserialize_list(json_data.get("Organization"), OrganizationDefinition),
            OsImage=deserialize_list(json_data.get("OsImage"), OsImageDefinition),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            ScuImage=deserialize_list(json_data.get("ScuImage"), ScuImageDefinition),
            ServerConfigs=deserialize_list(json_data.get("ServerConfigs"), ServerConfigsDefinition15),
            Servers=deserialize_list(json_data.get("Servers"), ServersDefinition),
            SharedScope=json_data.get("SharedScope"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            ValidationInfos=deserialize_list(json_data.get("ValidationInfos"), ValidationInfosDefinition),
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
class ConfigurationFileDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationFileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationFileDefinition"]:
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
_ConfigurationFileDefinition = ConfigurationFileDefinition


@dataclass
class GlobalConfigDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ConfigurationFileName: Optional[str]
    ConfigurationSource: Optional[str]
    InstallMethod: Optional[str]
    InstallTargetType: Optional[str]
    ObjectType: Optional[str]
    OperatingSystemParameters: Optional[Sequence["_GlobalConfigDefinition"]]
    OsImageName: Optional[str]
    ScuImageName: Optional[str]
    WindowsEdition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalConfigDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalConfigDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ConfigurationFileName=json_data.get("ConfigurationFileName"),
            ConfigurationSource=json_data.get("ConfigurationSource"),
            InstallMethod=json_data.get("InstallMethod"),
            InstallTargetType=json_data.get("InstallTargetType"),
            ObjectType=json_data.get("ObjectType"),
            OperatingSystemParameters=deserialize_list(json_data.get("OperatingSystemParameters"), GlobalConfigDefinition),
            OsImageName=json_data.get("OsImageName"),
            ScuImageName=json_data.get("ScuImageName"),
            WindowsEdition=json_data.get("WindowsEdition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalConfigDefinition2 = GlobalConfigDefinition2


@dataclass
class GlobalConfigDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalConfigDefinition = GlobalConfigDefinition


@dataclass
class OrganizationDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OrganizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrganizationDefinition"]:
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
_OrganizationDefinition = OrganizationDefinition


@dataclass
class OsImageDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OsImageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsImageDefinition"]:
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
_OsImageDefinition = OsImageDefinition


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
class ScuImageDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScuImageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScuImageDefinition"]:
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
_ScuImageDefinition = ScuImageDefinition


@dataclass
class ServerConfigsDefinition15(BaseModel):
    AdditionalParameters: Optional[Sequence["_ServerConfigsDefinition11"]]
    AdditionalProperties: Optional[str]
    Answers: Optional[Sequence["_ServerConfigsDefinition13"]]
    ClassId: Optional[str]
    ErrorMsgs: Optional[Sequence[str]]
    InstallTarget: Optional[str]
    ObjectType: Optional[str]
    ProcessedInstallTarget: Optional[Sequence["_ServerConfigsDefinition14"]]
    SerialNumber: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerConfigsDefinition15"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerConfigsDefinition15"]:
        if not json_data:
            return None
        return cls(
            AdditionalParameters=deserialize_list(json_data.get("AdditionalParameters"), ServerConfigsDefinition11),
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Answers=deserialize_list(json_data.get("Answers"), ServerConfigsDefinition13),
            ClassId=json_data.get("ClassId"),
            ErrorMsgs=json_data.get("ErrorMsgs"),
            InstallTarget=json_data.get("InstallTarget"),
            ObjectType=json_data.get("ObjectType"),
            ProcessedInstallTarget=deserialize_list(json_data.get("ProcessedInstallTarget"), ServerConfigsDefinition14),
            SerialNumber=json_data.get("SerialNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerConfigsDefinition15 = ServerConfigsDefinition15


@dataclass
class ServerConfigsDefinition11(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    IsValueSet: Optional[bool]
    ObjectType: Optional[str]
    Type: Optional[Sequence["_ServerConfigsDefinition9"]]
    Value: Optional[Sequence["_ServerConfigsDefinition10"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServerConfigsDefinition11"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerConfigsDefinition11"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            IsValueSet=json_data.get("IsValueSet"),
            ObjectType=json_data.get("ObjectType"),
            Type=deserialize_list(json_data.get("Type"), ServerConfigsDefinition9),
            Value=deserialize_list(json_data.get("Value"), ServerConfigsDefinition10),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerConfigsDefinition11 = ServerConfigsDefinition11


@dataclass
class ServerConfigsDefinition9(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Default: Optional[Sequence["_ServerConfigsDefinition2"]]
    Description: Optional[str]
    DisplayMeta: Optional[Sequence["_ServerConfigsDefinition3"]]
    InputParameters: Optional[Sequence["_ServerConfigsDefinition4"]]
    Label: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Properties: Optional[Sequence["_ServerConfigsDefinition8"]]
    Required: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ServerConfigsDefinition9"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerConfigsDefinition9"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Default=deserialize_list(json_data.get("Default"), ServerConfigsDefinition2),
            Description=json_data.get("Description"),
            DisplayMeta=deserialize_list(json_data.get("DisplayMeta"), ServerConfigsDefinition3),
            InputParameters=deserialize_list(json_data.get("InputParameters"), ServerConfigsDefinition4),
            Label=json_data.get("Label"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Properties=deserialize_list(json_data.get("Properties"), ServerConfigsDefinition8),
            Required=json_data.get("Required"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerConfigsDefinition9 = ServerConfigsDefinition9


@dataclass
class ServerConfigsDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    IsValueSet: Optional[bool]
    ObjectType: Optional[str]
    Override: Optional[bool]
    Value: Optional[Sequence["_ServerConfigsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServerConfigsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerConfigsDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            IsValueSet=json_data.get("IsValueSet"),
            ObjectType=json_data.get("ObjectType"),
            Override=json_data.get("Override"),
            Value=deserialize_list(json_data.get("Value"), ServerConfigsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerConfigsDefinition2 = ServerConfigsDefinition2


@dataclass
class ServerConfigsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerConfigsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerConfigsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerConfigsDefinition = ServerConfigsDefinition


@dataclass
class ServerConfigsDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InventorySelector: Optional[bool]
    ObjectType: Optional[str]
    WidgetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerConfigsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerConfigsDefinition3"]:
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
_ServerConfigsDefinition3 = ServerConfigsDefinition3


@dataclass
class ServerConfigsDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerConfigsDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerConfigsDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerConfigsDefinition4 = ServerConfigsDefinition4


@dataclass
class ServerConfigsDefinition8(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Constraints: Optional[Sequence["_ServerConfigsDefinition6"]]
    InventorySelector: Optional[Sequence["_ServerConfigsDefinition7"]]
    ObjectType: Optional[str]
    Secure: Optional[bool]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerConfigsDefinition8"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerConfigsDefinition8"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Constraints=deserialize_list(json_data.get("Constraints"), ServerConfigsDefinition6),
            InventorySelector=deserialize_list(json_data.get("InventorySelector"), ServerConfigsDefinition7),
            ObjectType=json_data.get("ObjectType"),
            Secure=json_data.get("Secure"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerConfigsDefinition8 = ServerConfigsDefinition8


@dataclass
class ServerConfigsDefinition6(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    EnumList: Optional[Sequence["_ServerConfigsDefinition5"]]
    Max: Optional[float]
    Min: Optional[float]
    ObjectType: Optional[str]
    Regex: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerConfigsDefinition6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerConfigsDefinition6"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            EnumList=deserialize_list(json_data.get("EnumList"), ServerConfigsDefinition5),
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
            ObjectType=json_data.get("ObjectType"),
            Regex=json_data.get("Regex"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerConfigsDefinition6 = ServerConfigsDefinition6


@dataclass
class ServerConfigsDefinition5(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Label: Optional[str]
    ObjectType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerConfigsDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerConfigsDefinition5"]:
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
_ServerConfigsDefinition5 = ServerConfigsDefinition5


@dataclass
class ServerConfigsDefinition7(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    DisplayAttributes: Optional[Sequence[str]]
    ObjectType: Optional[str]
    Selector: Optional[str]
    ValueAttribute: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerConfigsDefinition7"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerConfigsDefinition7"]:
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
_ServerConfigsDefinition7 = ServerConfigsDefinition7


@dataclass
class ServerConfigsDefinition10(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerConfigsDefinition10"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerConfigsDefinition10"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerConfigsDefinition10 = ServerConfigsDefinition10


@dataclass
class ServerConfigsDefinition13(BaseModel):
    AdditionalProperties: Optional[str]
    AnswerFile: Optional[str]
    ClassId: Optional[str]
    Hostname: Optional[str]
    IpConfigType: Optional[str]
    IpConfiguration: Optional[Sequence["_ServerConfigsDefinition12"]]
    IsAnswerFileSet: Optional[bool]
    IsRootPasswordCrypted: Optional[bool]
    IsRootPasswordSet: Optional[bool]
    Nameserver: Optional[str]
    NrSource: Optional[str]
    ObjectType: Optional[str]
    ProductKey: Optional[str]
    RootPassword: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerConfigsDefinition13"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerConfigsDefinition13"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            AnswerFile=json_data.get("AnswerFile"),
            ClassId=json_data.get("ClassId"),
            Hostname=json_data.get("Hostname"),
            IpConfigType=json_data.get("IpConfigType"),
            IpConfiguration=deserialize_list(json_data.get("IpConfiguration"), ServerConfigsDefinition12),
            IsAnswerFileSet=json_data.get("IsAnswerFileSet"),
            IsRootPasswordCrypted=json_data.get("IsRootPasswordCrypted"),
            IsRootPasswordSet=json_data.get("IsRootPasswordSet"),
            Nameserver=json_data.get("Nameserver"),
            NrSource=json_data.get("NrSource"),
            ObjectType=json_data.get("ObjectType"),
            ProductKey=json_data.get("ProductKey"),
            RootPassword=json_data.get("RootPassword"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerConfigsDefinition13 = ServerConfigsDefinition13


@dataclass
class ServerConfigsDefinition12(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerConfigsDefinition12"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerConfigsDefinition12"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerConfigsDefinition12 = ServerConfigsDefinition12


@dataclass
class ServerConfigsDefinition14(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerConfigsDefinition14"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerConfigsDefinition14"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerConfigsDefinition14 = ServerConfigsDefinition14


@dataclass
class ServersDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServersDefinition"]:
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
_ServersDefinition = ServersDefinition


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
class ValidationInfosDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ErrorMsg: Optional[str]
    ObjectType: Optional[str]
    Status: Optional[str]
    StepName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValidationInfosDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValidationInfosDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ErrorMsg=json_data.get("ErrorMsg"),
            ObjectType=json_data.get("ObjectType"),
            Status=json_data.get("Status"),
            StepName=json_data.get("StepName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValidationInfosDefinition = ValidationInfosDefinition


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


