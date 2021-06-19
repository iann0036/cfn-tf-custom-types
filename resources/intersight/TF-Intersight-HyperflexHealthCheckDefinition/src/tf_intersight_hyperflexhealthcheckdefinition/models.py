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
    Category: Optional[str]
    ClassId: Optional[str]
    CommonCauses: Optional[str]
    Configuration: Optional[str]
    CreateTime: Optional[str]
    DefaultHealthCheckScriptInfo: Optional[Sequence["_DefaultHealthCheckScriptInfoDefinition"]]
    Description: Optional[str]
    DomainGroupMoid: Optional[str]
    HealthCheckScriptInfos: Optional[Sequence["_HealthCheckScriptInfosDefinition"]]
    HealthImpact: Optional[str]
    Id: Optional[str]
    InternalName: Optional[str]
    MinimumHyperFlexVersion: Optional[str]
    ModTime: Optional[str]
    Moid: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    Reference: Optional[str]
    Resolution: Optional[str]
    ScriptExecutionMode: Optional[str]
    ScriptExecutionOnComputeNodes: Optional[bool]
    SharedScope: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TargetExecutionType: Optional[str]
    Timeout: Optional[float]
    UnsupportedHyperFlexVersions: Optional[Sequence[str]]
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
            Category=json_data.get("Category"),
            ClassId=json_data.get("ClassId"),
            CommonCauses=json_data.get("CommonCauses"),
            Configuration=json_data.get("Configuration"),
            CreateTime=json_data.get("CreateTime"),
            DefaultHealthCheckScriptInfo=deserialize_list(json_data.get("DefaultHealthCheckScriptInfo"), DefaultHealthCheckScriptInfoDefinition),
            Description=json_data.get("Description"),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            HealthCheckScriptInfos=deserialize_list(json_data.get("HealthCheckScriptInfos"), HealthCheckScriptInfosDefinition),
            HealthImpact=json_data.get("HealthImpact"),
            Id=json_data.get("Id"),
            InternalName=json_data.get("InternalName"),
            MinimumHyperFlexVersion=json_data.get("MinimumHyperFlexVersion"),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            Reference=json_data.get("Reference"),
            Resolution=json_data.get("Resolution"),
            ScriptExecutionMode=json_data.get("ScriptExecutionMode"),
            ScriptExecutionOnComputeNodes=json_data.get("ScriptExecutionOnComputeNodes"),
            SharedScope=json_data.get("SharedScope"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TargetExecutionType=json_data.get("TargetExecutionType"),
            Timeout=json_data.get("Timeout"),
            UnsupportedHyperFlexVersions=json_data.get("UnsupportedHyperFlexVersions"),
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
class DefaultHealthCheckScriptInfoDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    AggregateScriptName: Optional[str]
    ClassId: Optional[str]
    HyperflexVersion: Optional[str]
    NrVersion: Optional[str]
    ObjectType: Optional[str]
    ScriptExecuteLocation: Optional[str]
    ScriptInput: Optional[str]
    ScriptName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultHealthCheckScriptInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultHealthCheckScriptInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            AggregateScriptName=json_data.get("AggregateScriptName"),
            ClassId=json_data.get("ClassId"),
            HyperflexVersion=json_data.get("HyperflexVersion"),
            NrVersion=json_data.get("NrVersion"),
            ObjectType=json_data.get("ObjectType"),
            ScriptExecuteLocation=json_data.get("ScriptExecuteLocation"),
            ScriptInput=json_data.get("ScriptInput"),
            ScriptName=json_data.get("ScriptName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultHealthCheckScriptInfoDefinition = DefaultHealthCheckScriptInfoDefinition


@dataclass
class HealthCheckScriptInfosDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    AggregateScriptName: Optional[str]
    ClassId: Optional[str]
    HyperflexVersion: Optional[str]
    NrVersion: Optional[str]
    ObjectType: Optional[str]
    ScriptExecuteLocation: Optional[str]
    ScriptInput: Optional[str]
    ScriptName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckScriptInfosDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckScriptInfosDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            AggregateScriptName=json_data.get("AggregateScriptName"),
            ClassId=json_data.get("ClassId"),
            HyperflexVersion=json_data.get("HyperflexVersion"),
            NrVersion=json_data.get("NrVersion"),
            ObjectType=json_data.get("ObjectType"),
            ScriptExecuteLocation=json_data.get("ScriptExecuteLocation"),
            ScriptInput=json_data.get("ScriptInput"),
            ScriptName=json_data.get("ScriptName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckScriptInfosDefinition = HealthCheckScriptInfosDefinition


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


