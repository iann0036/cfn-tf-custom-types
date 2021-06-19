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
    AdditionalParameters: Optional[Sequence["_AdditionalParametersDefinition11"]]
    AdditionalProperties: Optional[str]
    Ancestors: Optional[Sequence["_AncestorsDefinition"]]
    Answers: Optional[Sequence["_AnswersDefinition2"]]
    ClassId: Optional[str]
    ConfigurationFile: Optional[Sequence["_ConfigurationFileDefinition"]]
    CreateTime: Optional[str]
    Description: Optional[str]
    DomainGroupMoid: Optional[str]
    ErrorMsg: Optional[str]
    Id: Optional[str]
    Image: Optional[Sequence["_ImageDefinition"]]
    InstallMethod: Optional[str]
    InstallTarget: Optional[Sequence["_InstallTargetDefinition"]]
    ModTime: Optional[str]
    Moid: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    OperState: Optional[str]
    OperatingSystemParameters: Optional[Sequence["_OperatingSystemParametersDefinition"]]
    Organization: Optional[Sequence["_OrganizationDefinition"]]
    OsduImage: Optional[Sequence["_OsduImageDefinition"]]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    Server: Optional[Sequence["_ServerDefinition"]]
    SharedScope: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VersionContext: Optional[Sequence["_VersionContextDefinition3"]]
    WaitForCompletion: Optional[bool]
    WorkflowInfo: Optional[Sequence["_WorkflowInfoDefinition"]]

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
            AdditionalParameters=deserialize_list(json_data.get("AdditionalParameters"), AdditionalParametersDefinition11),
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Ancestors=deserialize_list(json_data.get("Ancestors"), AncestorsDefinition),
            Answers=deserialize_list(json_data.get("Answers"), AnswersDefinition2),
            ClassId=json_data.get("ClassId"),
            ConfigurationFile=deserialize_list(json_data.get("ConfigurationFile"), ConfigurationFileDefinition),
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            ErrorMsg=json_data.get("ErrorMsg"),
            Id=json_data.get("Id"),
            Image=deserialize_list(json_data.get("Image"), ImageDefinition),
            InstallMethod=json_data.get("InstallMethod"),
            InstallTarget=deserialize_list(json_data.get("InstallTarget"), InstallTargetDefinition),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            OperState=json_data.get("OperState"),
            OperatingSystemParameters=deserialize_list(json_data.get("OperatingSystemParameters"), OperatingSystemParametersDefinition),
            Organization=deserialize_list(json_data.get("Organization"), OrganizationDefinition),
            OsduImage=deserialize_list(json_data.get("OsduImage"), OsduImageDefinition),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            Server=deserialize_list(json_data.get("Server"), ServerDefinition),
            SharedScope=json_data.get("SharedScope"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VersionContext=deserialize_list(json_data.get("VersionContext"), VersionContextDefinition3),
            WaitForCompletion=json_data.get("WaitForCompletion"),
            WorkflowInfo=deserialize_list(json_data.get("WorkflowInfo"), WorkflowInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdditionalParametersDefinition11(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    IsValueSet: Optional[bool]
    ObjectType: Optional[str]
    Type: Optional[Sequence["_AdditionalParametersDefinition9"]]
    Value: Optional[Sequence["_AdditionalParametersDefinition10"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalParametersDefinition11"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalParametersDefinition11"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            IsValueSet=json_data.get("IsValueSet"),
            ObjectType=json_data.get("ObjectType"),
            Type=deserialize_list(json_data.get("Type"), AdditionalParametersDefinition9),
            Value=deserialize_list(json_data.get("Value"), AdditionalParametersDefinition10),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalParametersDefinition11 = AdditionalParametersDefinition11


@dataclass
class AdditionalParametersDefinition9(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Default: Optional[Sequence["_AdditionalParametersDefinition2"]]
    Description: Optional[str]
    DisplayMeta: Optional[Sequence["_AdditionalParametersDefinition3"]]
    InputParameters: Optional[Sequence["_AdditionalParametersDefinition4"]]
    Label: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Properties: Optional[Sequence["_AdditionalParametersDefinition8"]]
    Required: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalParametersDefinition9"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalParametersDefinition9"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Default=deserialize_list(json_data.get("Default"), AdditionalParametersDefinition2),
            Description=json_data.get("Description"),
            DisplayMeta=deserialize_list(json_data.get("DisplayMeta"), AdditionalParametersDefinition3),
            InputParameters=deserialize_list(json_data.get("InputParameters"), AdditionalParametersDefinition4),
            Label=json_data.get("Label"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Properties=deserialize_list(json_data.get("Properties"), AdditionalParametersDefinition8),
            Required=json_data.get("Required"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalParametersDefinition9 = AdditionalParametersDefinition9


@dataclass
class AdditionalParametersDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    IsValueSet: Optional[bool]
    ObjectType: Optional[str]
    Override: Optional[bool]
    Value: Optional[Sequence["_AdditionalParametersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalParametersDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalParametersDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            IsValueSet=json_data.get("IsValueSet"),
            ObjectType=json_data.get("ObjectType"),
            Override=json_data.get("Override"),
            Value=deserialize_list(json_data.get("Value"), AdditionalParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalParametersDefinition2 = AdditionalParametersDefinition2


@dataclass
class AdditionalParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalParametersDefinition = AdditionalParametersDefinition


@dataclass
class AdditionalParametersDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InventorySelector: Optional[bool]
    ObjectType: Optional[str]
    WidgetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalParametersDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalParametersDefinition3"]:
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
_AdditionalParametersDefinition3 = AdditionalParametersDefinition3


@dataclass
class AdditionalParametersDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalParametersDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalParametersDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalParametersDefinition4 = AdditionalParametersDefinition4


@dataclass
class AdditionalParametersDefinition8(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Constraints: Optional[Sequence["_AdditionalParametersDefinition6"]]
    InventorySelector: Optional[Sequence["_AdditionalParametersDefinition7"]]
    ObjectType: Optional[str]
    Secure: Optional[bool]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalParametersDefinition8"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalParametersDefinition8"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Constraints=deserialize_list(json_data.get("Constraints"), AdditionalParametersDefinition6),
            InventorySelector=deserialize_list(json_data.get("InventorySelector"), AdditionalParametersDefinition7),
            ObjectType=json_data.get("ObjectType"),
            Secure=json_data.get("Secure"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalParametersDefinition8 = AdditionalParametersDefinition8


@dataclass
class AdditionalParametersDefinition6(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    EnumList: Optional[Sequence["_AdditionalParametersDefinition5"]]
    Max: Optional[float]
    Min: Optional[float]
    ObjectType: Optional[str]
    Regex: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalParametersDefinition6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalParametersDefinition6"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            EnumList=deserialize_list(json_data.get("EnumList"), AdditionalParametersDefinition5),
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
            ObjectType=json_data.get("ObjectType"),
            Regex=json_data.get("Regex"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalParametersDefinition6 = AdditionalParametersDefinition6


@dataclass
class AdditionalParametersDefinition5(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Label: Optional[str]
    ObjectType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalParametersDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalParametersDefinition5"]:
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
_AdditionalParametersDefinition5 = AdditionalParametersDefinition5


@dataclass
class AdditionalParametersDefinition7(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    DisplayAttributes: Optional[Sequence[str]]
    ObjectType: Optional[str]
    Selector: Optional[str]
    ValueAttribute: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalParametersDefinition7"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalParametersDefinition7"]:
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
_AdditionalParametersDefinition7 = AdditionalParametersDefinition7


@dataclass
class AdditionalParametersDefinition10(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalParametersDefinition10"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalParametersDefinition10"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalParametersDefinition10 = AdditionalParametersDefinition10


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
class AnswersDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    AnswerFile: Optional[str]
    ClassId: Optional[str]
    Hostname: Optional[str]
    IpConfigType: Optional[str]
    IpConfiguration: Optional[Sequence["_AnswersDefinition"]]
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
        cls: Type["_AnswersDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnswersDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            AnswerFile=json_data.get("AnswerFile"),
            ClassId=json_data.get("ClassId"),
            Hostname=json_data.get("Hostname"),
            IpConfigType=json_data.get("IpConfigType"),
            IpConfiguration=deserialize_list(json_data.get("IpConfiguration"), AnswersDefinition),
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
_AnswersDefinition2 = AnswersDefinition2


@dataclass
class AnswersDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnswersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnswersDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnswersDefinition = AnswersDefinition


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
class ImageDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageDefinition"]:
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
_ImageDefinition = ImageDefinition


@dataclass
class InstallTargetDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstallTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstallTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstallTargetDefinition = InstallTargetDefinition


@dataclass
class OperatingSystemParametersDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OperatingSystemParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OperatingSystemParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OperatingSystemParametersDefinition = OperatingSystemParametersDefinition


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
class OsduImageDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OsduImageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsduImageDefinition"]:
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
_OsduImageDefinition = OsduImageDefinition


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
class ServerDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerDefinition"]:
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
_ServerDefinition = ServerDefinition


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


@dataclass
class WorkflowInfoDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkflowInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkflowInfoDefinition"]:
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
_WorkflowInfoDefinition = WorkflowInfoDefinition


