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
    Batch: Optional[Sequence["_BatchDefinition3"]]
    ClassId: Optional[str]
    Constraints: Optional[Sequence["_ConstraintsDefinition2"]]
    CreateTime: Optional[str]
    Description: Optional[str]
    DomainGroupMoid: Optional[str]
    ErrorResponseHandler: Optional[Sequence["_ErrorResponseHandlerDefinition"]]
    Id: Optional[str]
    ModTime: Optional[str]
    Moid: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Outcomes: Optional[Sequence["_OutcomesDefinition"]]
    Output: Optional[Sequence["_OutputDefinition"]]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    RetryFromFailedApi: Optional[bool]
    SharedScope: Optional[str]
    SkipOnCondition: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TaskDefinition: Optional[Sequence["_TaskDefinitionDefinition"]]
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
            Batch=deserialize_list(json_data.get("Batch"), BatchDefinition3),
            ClassId=json_data.get("ClassId"),
            Constraints=deserialize_list(json_data.get("Constraints"), ConstraintsDefinition2),
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            ErrorResponseHandler=deserialize_list(json_data.get("ErrorResponseHandler"), ErrorResponseHandlerDefinition),
            Id=json_data.get("Id"),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Outcomes=deserialize_list(json_data.get("Outcomes"), OutcomesDefinition),
            Output=deserialize_list(json_data.get("Output"), OutputDefinition),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            RetryFromFailedApi=json_data.get("RetryFromFailedApi"),
            SharedScope=json_data.get("SharedScope"),
            SkipOnCondition=json_data.get("SkipOnCondition"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TaskDefinition=deserialize_list(json_data.get("TaskDefinition"), TaskDefinitionDefinition),
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
class BatchDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    AssetTargetMoid: Optional[str]
    Body: Optional[str]
    ClassId: Optional[str]
    ContentType: Optional[str]
    Description: Optional[str]
    ErrorContentType: Optional[str]
    Label: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Outcomes: Optional[Sequence["_BatchDefinition"]]
    ResponseSpec: Optional[Sequence["_BatchDefinition2"]]
    SkipOnCondition: Optional[str]
    StartDelay: Optional[float]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BatchDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BatchDefinition3"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            AssetTargetMoid=json_data.get("AssetTargetMoid"),
            Body=json_data.get("Body"),
            ClassId=json_data.get("ClassId"),
            ContentType=json_data.get("ContentType"),
            Description=json_data.get("Description"),
            ErrorContentType=json_data.get("ErrorContentType"),
            Label=json_data.get("Label"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Outcomes=deserialize_list(json_data.get("Outcomes"), BatchDefinition),
            ResponseSpec=deserialize_list(json_data.get("ResponseSpec"), BatchDefinition2),
            SkipOnCondition=json_data.get("SkipOnCondition"),
            StartDelay=json_data.get("StartDelay"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BatchDefinition3 = BatchDefinition3


@dataclass
class BatchDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BatchDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BatchDefinition = BatchDefinition


@dataclass
class BatchDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BatchDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BatchDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BatchDefinition2 = BatchDefinition2


@dataclass
class ConstraintsDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ObjectType: Optional[str]
    TargetDataType: Optional[Sequence["_ConstraintsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConstraintsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConstraintsDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ObjectType=json_data.get("ObjectType"),
            TargetDataType=deserialize_list(json_data.get("TargetDataType"), ConstraintsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConstraintsDefinition2 = ConstraintsDefinition2


@dataclass
class ConstraintsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConstraintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConstraintsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConstraintsDefinition = ConstraintsDefinition


@dataclass
class ErrorResponseHandlerDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ErrorResponseHandlerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ErrorResponseHandlerDefinition"]:
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
_ErrorResponseHandlerDefinition = ErrorResponseHandlerDefinition


@dataclass
class OutcomesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutcomesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutcomesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutcomesDefinition = OutcomesDefinition


@dataclass
class OutputDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputDefinition = OutputDefinition


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
class TaskDefinitionDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaskDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskDefinitionDefinition"]:
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
_TaskDefinitionDefinition = TaskDefinitionDefinition


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


