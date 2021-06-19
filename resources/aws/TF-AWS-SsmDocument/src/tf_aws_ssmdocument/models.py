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
    Content: Optional[str]
    CreatedDate: Optional[str]
    DefaultVersion: Optional[str]
    Description: Optional[str]
    DocumentFormat: Optional[str]
    DocumentType: Optional[str]
    DocumentVersion: Optional[str]
    Hash: Optional[str]
    HashType: Optional[str]
    Id: Optional[str]
    LatestVersion: Optional[str]
    Name: Optional[str]
    Owner: Optional[str]
    Parameter: Optional[Sequence["_ParameterDefinition"]]
    Permissions: Optional[Sequence["_PermissionsDefinition"]]
    PlatformTypes: Optional[Sequence[str]]
    SchemaVersion: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    TargetType: Optional[str]
    VersionName: Optional[str]
    AttachmentsSource: Optional[Sequence["_AttachmentsSourceDefinition"]]

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
            Content=json_data.get("Content"),
            CreatedDate=json_data.get("CreatedDate"),
            DefaultVersion=json_data.get("DefaultVersion"),
            Description=json_data.get("Description"),
            DocumentFormat=json_data.get("DocumentFormat"),
            DocumentType=json_data.get("DocumentType"),
            DocumentVersion=json_data.get("DocumentVersion"),
            Hash=json_data.get("Hash"),
            HashType=json_data.get("HashType"),
            Id=json_data.get("Id"),
            LatestVersion=json_data.get("LatestVersion"),
            Name=json_data.get("Name"),
            Owner=json_data.get("Owner"),
            Parameter=deserialize_list(json_data.get("Parameter"), ParameterDefinition),
            Permissions=deserialize_list(json_data.get("Permissions"), PermissionsDefinition),
            PlatformTypes=json_data.get("PlatformTypes"),
            SchemaVersion=json_data.get("SchemaVersion"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            TargetType=json_data.get("TargetType"),
            VersionName=json_data.get("VersionName"),
            AttachmentsSource=deserialize_list(json_data.get("AttachmentsSource"), AttachmentsSourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ParameterDefinition(BaseModel):
    DefaultValue: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultValue=json_data.get("DefaultValue"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterDefinition = ParameterDefinition


@dataclass
class PermissionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PermissionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PermissionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PermissionsDefinition = PermissionsDefinition


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
class AttachmentsSourceDefinition(BaseModel):
    Key: Optional[str]
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AttachmentsSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttachmentsSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttachmentsSourceDefinition = AttachmentsSourceDefinition


