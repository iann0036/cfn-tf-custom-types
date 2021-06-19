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
    Arn: Optional[str]
    CacheClusterEnabled: Optional[bool]
    CacheClusterSize: Optional[str]
    ClientCertificateId: Optional[str]
    DeploymentId: Optional[str]
    Description: Optional[str]
    DocumentationVersion: Optional[str]
    ExecutionArn: Optional[str]
    Id: Optional[str]
    InvokeUrl: Optional[str]
    RestApiId: Optional[str]
    StageName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Variables: Optional[Sequence["_VariablesDefinition"]]
    XrayTracingEnabled: Optional[bool]
    AccessLogSettings: Optional[Sequence["_AccessLogSettingsDefinition"]]

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
            Arn=json_data.get("Arn"),
            CacheClusterEnabled=json_data.get("CacheClusterEnabled"),
            CacheClusterSize=json_data.get("CacheClusterSize"),
            ClientCertificateId=json_data.get("ClientCertificateId"),
            DeploymentId=json_data.get("DeploymentId"),
            Description=json_data.get("Description"),
            DocumentationVersion=json_data.get("DocumentationVersion"),
            ExecutionArn=json_data.get("ExecutionArn"),
            Id=json_data.get("Id"),
            InvokeUrl=json_data.get("InvokeUrl"),
            RestApiId=json_data.get("RestApiId"),
            StageName=json_data.get("StageName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Variables=deserialize_list(json_data.get("Variables"), VariablesDefinition),
            XrayTracingEnabled=json_data.get("XrayTracingEnabled"),
            AccessLogSettings=deserialize_list(json_data.get("AccessLogSettings"), AccessLogSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class VariablesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VariablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VariablesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VariablesDefinition = VariablesDefinition


@dataclass
class AccessLogSettingsDefinition(BaseModel):
    DestinationArn: Optional[str]
    Format: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLogSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLogSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationArn=json_data.get("DestinationArn"),
            Format=json_data.get("Format"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLogSettingsDefinition = AccessLogSettingsDefinition


