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
    ClonedFrom: Optional[Sequence["_ClonedFromDefinition"]]
    CreateTime: Optional[str]
    DefaultVersion: Optional[bool]
    Description: Optional[str]
    DomainGroupMoid: Optional[str]
    Id: Optional[str]
    InputDefinition: Optional[Sequence["_InputDefinitionDefinition5"]]
    InputParameterSet: Optional[Sequence["_InputParameterSetDefinition"]]
    Label: Optional[str]
    LicenseEntitlement: Optional[str]
    MaxTaskCount: Optional[float]
    MaxWorkerTaskCount: Optional[float]
    ModTime: Optional[str]
    Moid: Optional[str]
    Name: Optional[str]
    NrVersion: Optional[float]
    ObjectType: Optional[str]
    OutputDefinition: Optional[Sequence["_OutputDefinitionDefinition5"]]
    OutputParameters: Optional[Sequence["_OutputParametersDefinition"]]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    Properties: Optional[Sequence["_PropertiesDefinition"]]
    SharedScope: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Tasks: Optional[Sequence["_TasksDefinition"]]
    UiInputFilters: Optional[Sequence["_UiInputFiltersDefinition"]]
    UiRenderingData: Optional[Sequence["_UiRenderingDataDefinition"]]
    ValidationInformation: Optional[Sequence["_ValidationInformationDefinition2"]]
    VersionContext: Optional[Sequence["_VersionContextDefinition3"]]
    WorkflowMetadata: Optional[Sequence["_WorkflowMetadataDefinition"]]

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
            ClonedFrom=deserialize_list(json_data.get("ClonedFrom"), ClonedFromDefinition),
            CreateTime=json_data.get("CreateTime"),
            DefaultVersion=json_data.get("DefaultVersion"),
            Description=json_data.get("Description"),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            Id=json_data.get("Id"),
            InputDefinition=deserialize_list(json_data.get("InputDefinition"), InputDefinitionDefinition5),
            InputParameterSet=deserialize_list(json_data.get("InputParameterSet"), InputParameterSetDefinition),
            Label=json_data.get("Label"),
            LicenseEntitlement=json_data.get("LicenseEntitlement"),
            MaxTaskCount=json_data.get("MaxTaskCount"),
            MaxWorkerTaskCount=json_data.get("MaxWorkerTaskCount"),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            NrVersion=json_data.get("NrVersion"),
            ObjectType=json_data.get("ObjectType"),
            OutputDefinition=deserialize_list(json_data.get("OutputDefinition"), OutputDefinitionDefinition5),
            OutputParameters=deserialize_list(json_data.get("OutputParameters"), OutputParametersDefinition),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition),
            SharedScope=json_data.get("SharedScope"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Tasks=deserialize_list(json_data.get("Tasks"), TasksDefinition),
            UiInputFilters=deserialize_list(json_data.get("UiInputFilters"), UiInputFiltersDefinition),
            UiRenderingData=deserialize_list(json_data.get("UiRenderingData"), UiRenderingDataDefinition),
            ValidationInformation=deserialize_list(json_data.get("ValidationInformation"), ValidationInformationDefinition2),
            VersionContext=deserialize_list(json_data.get("VersionContext"), VersionContextDefinition3),
            WorkflowMetadata=deserialize_list(json_data.get("WorkflowMetadata"), WorkflowMetadataDefinition),
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
class ClonedFromDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClonedFromDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClonedFromDefinition"]:
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
_ClonedFromDefinition = ClonedFromDefinition


@dataclass
class InputDefinitionDefinition5(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Default: Optional[Sequence["_InputDefinitionDefinition2"]]
    Description: Optional[str]
    DisplayMeta: Optional[Sequence["_InputDefinitionDefinition3"]]
    InputParameters: Optional[Sequence["_InputDefinitionDefinition4"]]
    Label: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Required: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_InputDefinitionDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputDefinitionDefinition5"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Default=deserialize_list(json_data.get("Default"), InputDefinitionDefinition2),
            Description=json_data.get("Description"),
            DisplayMeta=deserialize_list(json_data.get("DisplayMeta"), InputDefinitionDefinition3),
            InputParameters=deserialize_list(json_data.get("InputParameters"), InputDefinitionDefinition4),
            Label=json_data.get("Label"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Required=json_data.get("Required"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputDefinitionDefinition5 = InputDefinitionDefinition5


@dataclass
class InputDefinitionDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    IsValueSet: Optional[bool]
    ObjectType: Optional[str]
    Override: Optional[bool]
    Value: Optional[Sequence["_InputDefinitionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InputDefinitionDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputDefinitionDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            IsValueSet=json_data.get("IsValueSet"),
            ObjectType=json_data.get("ObjectType"),
            Override=json_data.get("Override"),
            Value=deserialize_list(json_data.get("Value"), InputDefinitionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputDefinitionDefinition2 = InputDefinitionDefinition2


@dataclass
class InputDefinitionDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputDefinitionDefinition = InputDefinitionDefinition


@dataclass
class InputDefinitionDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InventorySelector: Optional[bool]
    ObjectType: Optional[str]
    WidgetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputDefinitionDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputDefinitionDefinition3"]:
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
_InputDefinitionDefinition3 = InputDefinitionDefinition3


@dataclass
class InputDefinitionDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputDefinitionDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputDefinitionDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputDefinitionDefinition4 = InputDefinitionDefinition4


@dataclass
class InputParameterSetDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Condition: Optional[str]
    ControlParameter: Optional[str]
    EnableParameters: Optional[Sequence[str]]
    Name: Optional[str]
    ObjectType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputParameterSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputParameterSetDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Condition=json_data.get("Condition"),
            ControlParameter=json_data.get("ControlParameter"),
            EnableParameters=json_data.get("EnableParameters"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputParameterSetDefinition = InputParameterSetDefinition


@dataclass
class OutputDefinitionDefinition5(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Default: Optional[Sequence["_OutputDefinitionDefinition2"]]
    Description: Optional[str]
    DisplayMeta: Optional[Sequence["_OutputDefinitionDefinition3"]]
    InputParameters: Optional[Sequence["_OutputDefinitionDefinition4"]]
    Label: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Required: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_OutputDefinitionDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputDefinitionDefinition5"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Default=deserialize_list(json_data.get("Default"), OutputDefinitionDefinition2),
            Description=json_data.get("Description"),
            DisplayMeta=deserialize_list(json_data.get("DisplayMeta"), OutputDefinitionDefinition3),
            InputParameters=deserialize_list(json_data.get("InputParameters"), OutputDefinitionDefinition4),
            Label=json_data.get("Label"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Required=json_data.get("Required"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputDefinitionDefinition5 = OutputDefinitionDefinition5


@dataclass
class OutputDefinitionDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    IsValueSet: Optional[bool]
    ObjectType: Optional[str]
    Override: Optional[bool]
    Value: Optional[Sequence["_OutputDefinitionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutputDefinitionDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputDefinitionDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            IsValueSet=json_data.get("IsValueSet"),
            ObjectType=json_data.get("ObjectType"),
            Override=json_data.get("Override"),
            Value=deserialize_list(json_data.get("Value"), OutputDefinitionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputDefinitionDefinition2 = OutputDefinitionDefinition2


@dataclass
class OutputDefinitionDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutputDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputDefinitionDefinition = OutputDefinitionDefinition


@dataclass
class OutputDefinitionDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InventorySelector: Optional[bool]
    ObjectType: Optional[str]
    WidgetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutputDefinitionDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputDefinitionDefinition3"]:
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
_OutputDefinitionDefinition3 = OutputDefinitionDefinition3


@dataclass
class OutputDefinitionDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutputDefinitionDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputDefinitionDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputDefinitionDefinition4 = OutputDefinitionDefinition4


@dataclass
class OutputParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutputParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputParametersDefinition = OutputParametersDefinition


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
class PropertiesDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    EnableDebug: Optional[bool]
    ExternalMeta: Optional[bool]
    ObjectType: Optional[str]
    Retryable: Optional[bool]
    SupportStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            EnableDebug=json_data.get("EnableDebug"),
            ExternalMeta=json_data.get("ExternalMeta"),
            ObjectType=json_data.get("ObjectType"),
            Retryable=json_data.get("Retryable"),
            SupportStatus=json_data.get("SupportStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition = PropertiesDefinition


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
class TasksDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Description: Optional[str]
    Label: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TasksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TasksDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Description=json_data.get("Description"),
            Label=json_data.get("Label"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TasksDefinition = TasksDefinition


@dataclass
class UiInputFiltersDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Filters: Optional[Sequence[str]]
    Name: Optional[str]
    ObjectType: Optional[str]
    UserHelpMessage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UiInputFiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UiInputFiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Filters=json_data.get("Filters"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            UserHelpMessage=json_data.get("UserHelpMessage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UiInputFiltersDefinition = UiInputFiltersDefinition


@dataclass
class UiRenderingDataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UiRenderingDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UiRenderingDataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UiRenderingDataDefinition = UiRenderingDataDefinition


@dataclass
class ValidationInformationDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ObjectType: Optional[str]
    State: Optional[str]
    ValidationError: Optional[Sequence["_ValidationInformationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ValidationInformationDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValidationInformationDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ObjectType=json_data.get("ObjectType"),
            State=json_data.get("State"),
            ValidationError=deserialize_list(json_data.get("ValidationError"), ValidationInformationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValidationInformationDefinition2 = ValidationInformationDefinition2


@dataclass
class ValidationInformationDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ErrorLog: Optional[str]
    Field: Optional[str]
    ObjectType: Optional[str]
    TaskName: Optional[str]
    TransitionName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValidationInformationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValidationInformationDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ErrorLog=json_data.get("ErrorLog"),
            Field=json_data.get("Field"),
            ObjectType=json_data.get("ObjectType"),
            TaskName=json_data.get("TaskName"),
            TransitionName=json_data.get("TransitionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValidationInformationDefinition = ValidationInformationDefinition


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
class WorkflowMetadataDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkflowMetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkflowMetadataDefinition"]:
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
_WorkflowMetadataDefinition = WorkflowMetadataDefinition


