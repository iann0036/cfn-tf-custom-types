# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Arn: Optional[str]
    Content: Optional[str]
    CreatedDate: Optional[str]
    DefaultVersion: Optional[str]
    Description: Optional[str]
    DocumentFormat: Optional[str]
    DocumentType: Optional[str]
    Hash: Optional[str]
    HashType: Optional[str]
    LatestVersion: Optional[str]
    Name: Optional[str]
    Owner: Optional[str]
    Parameter: Optional[Sequence["_Parameter"]]
    Permissions: Optional[Sequence["_Permissions"]]
    PlatformTypes: Optional[Sequence[str]]
    SchemaVersion: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TargetType: Optional[str]
    AttachmentsSource: Optional[Sequence["_AttachmentsSource"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Content=json_data.get("Content"),
            CreatedDate=json_data.get("CreatedDate"),
            DefaultVersion=json_data.get("DefaultVersion"),
            Description=json_data.get("Description"),
            DocumentFormat=json_data.get("DocumentFormat"),
            DocumentType=json_data.get("DocumentType"),
            Hash=json_data.get("Hash"),
            HashType=json_data.get("HashType"),
            LatestVersion=json_data.get("LatestVersion"),
            Name=json_data.get("Name"),
            Owner=json_data.get("Owner"),
            Parameter=json_data.get("Parameter"),
            Permissions=json_data.get("Permissions"),
            PlatformTypes=json_data.get("PlatformTypes"),
            SchemaVersion=json_data.get("SchemaVersion"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            TargetType=json_data.get("TargetType"),
            AttachmentsSource=json_data.get("AttachmentsSource"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Parameter:
    DefaultValue: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Parameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameter"]:
        if not json_data:
            return None
        return cls(
            DefaultValue=json_data.get("DefaultValue"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameter = Parameter


@dataclass
class Permissions:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Permissions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Permissions"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Permissions = Permissions


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class AttachmentsSource:
    Key: Optional[str]
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AttachmentsSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttachmentsSource"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttachmentsSource = AttachmentsSource


