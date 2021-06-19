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
    Atomic: Optional[bool]
    Chart: Optional[str]
    CleanupOnFail: Optional[bool]
    CreateNamespace: Optional[bool]
    DependencyUpdate: Optional[bool]
    Description: Optional[str]
    Devel: Optional[bool]
    DisableCrdHooks: Optional[bool]
    DisableOpenapiValidation: Optional[bool]
    DisableWebhooks: Optional[bool]
    ForceUpdate: Optional[bool]
    Id: Optional[str]
    Keyring: Optional[str]
    Lint: Optional[bool]
    Manifest: Optional[str]
    MaxHistory: Optional[float]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    RecreatePods: Optional[bool]
    RenderSubchartNotes: Optional[bool]
    Replace: Optional[bool]
    Repository: Optional[str]
    RepositoryCaFile: Optional[str]
    RepositoryCertFile: Optional[str]
    RepositoryKeyFile: Optional[str]
    RepositoryPassword: Optional[str]
    RepositoryUsername: Optional[str]
    ResetValues: Optional[bool]
    ReuseValues: Optional[bool]
    SkipCrds: Optional[bool]
    Status: Optional[str]
    Timeout: Optional[float]
    Values: Optional[Sequence[str]]
    Verify: Optional[bool]
    Version: Optional[str]
    Wait: Optional[bool]
    WaitForJobs: Optional[bool]
    Postrender: Optional[Sequence["_PostrenderDefinition"]]
    Set: Optional[Sequence["_SetDefinition"]]
    SetSensitive: Optional[Sequence["_SetSensitiveDefinition"]]

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
            Atomic=json_data.get("Atomic"),
            Chart=json_data.get("Chart"),
            CleanupOnFail=json_data.get("CleanupOnFail"),
            CreateNamespace=json_data.get("CreateNamespace"),
            DependencyUpdate=json_data.get("DependencyUpdate"),
            Description=json_data.get("Description"),
            Devel=json_data.get("Devel"),
            DisableCrdHooks=json_data.get("DisableCrdHooks"),
            DisableOpenapiValidation=json_data.get("DisableOpenapiValidation"),
            DisableWebhooks=json_data.get("DisableWebhooks"),
            ForceUpdate=json_data.get("ForceUpdate"),
            Id=json_data.get("Id"),
            Keyring=json_data.get("Keyring"),
            Lint=json_data.get("Lint"),
            Manifest=json_data.get("Manifest"),
            MaxHistory=json_data.get("MaxHistory"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            RecreatePods=json_data.get("RecreatePods"),
            RenderSubchartNotes=json_data.get("RenderSubchartNotes"),
            Replace=json_data.get("Replace"),
            Repository=json_data.get("Repository"),
            RepositoryCaFile=json_data.get("RepositoryCaFile"),
            RepositoryCertFile=json_data.get("RepositoryCertFile"),
            RepositoryKeyFile=json_data.get("RepositoryKeyFile"),
            RepositoryPassword=json_data.get("RepositoryPassword"),
            RepositoryUsername=json_data.get("RepositoryUsername"),
            ResetValues=json_data.get("ResetValues"),
            ReuseValues=json_data.get("ReuseValues"),
            SkipCrds=json_data.get("SkipCrds"),
            Status=json_data.get("Status"),
            Timeout=json_data.get("Timeout"),
            Values=json_data.get("Values"),
            Verify=json_data.get("Verify"),
            Version=json_data.get("Version"),
            Wait=json_data.get("Wait"),
            WaitForJobs=json_data.get("WaitForJobs"),
            Postrender=deserialize_list(json_data.get("Postrender"), PostrenderDefinition),
            Set=deserialize_list(json_data.get("Set"), SetDefinition),
            SetSensitive=deserialize_list(json_data.get("SetSensitive"), SetSensitiveDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    AppVersion: Optional[str]
    Chart: Optional[str]
    Name: Optional[str]
    Namespace: Optional[str]
    Revision: Optional[float]
    Values: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            AppVersion=json_data.get("AppVersion"),
            Chart=json_data.get("Chart"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Revision=json_data.get("Revision"),
            Values=json_data.get("Values"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class PostrenderDefinition(BaseModel):
    BinaryPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PostrenderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PostrenderDefinition"]:
        if not json_data:
            return None
        return cls(
            BinaryPath=json_data.get("BinaryPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PostrenderDefinition = PostrenderDefinition


@dataclass
class SetDefinition(BaseModel):
    Name: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetDefinition = SetDefinition


@dataclass
class SetSensitiveDefinition(BaseModel):
    Name: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SetSensitiveDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetSensitiveDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetSensitiveDefinition = SetSensitiveDefinition


