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
    Name: Optional[str]
    RoleArn: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    ArtifactStore: Optional[Sequence["_ArtifactStore"]]
    Stage: Optional[Sequence["_Stage"]]
    EncryptionKey: Optional[Sequence["_EncryptionKey"]]
    Action: Optional[Sequence["_Action"]]

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
            Name=json_data.get("Name"),
            RoleArn=json_data.get("RoleArn"),
            Tags=json_data.get("Tags"),
            ArtifactStore=json_data.get("ArtifactStore"),
            Stage=json_data.get("Stage"),
            EncryptionKey=json_data.get("EncryptionKey"),
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class ArtifactStore:
    Location: Optional[str]
    Type: Optional[str]
    EncryptionKey: Optional[Sequence["_EncryptionKey"]]

    @classmethod
    def _deserialize(
        cls: Type["_ArtifactStore"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArtifactStore"]:
        if not json_data:
            return None
        return cls(
            Location=json_data.get("Location"),
            Type=json_data.get("Type"),
            EncryptionKey=json_data.get("EncryptionKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArtifactStore = ArtifactStore


@dataclass
class EncryptionKey:
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionKey"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionKey = EncryptionKey


@dataclass
class Stage:
    Name: Optional[str]
    Action: Optional[Sequence["_Action"]]

    @classmethod
    def _deserialize(
        cls: Type["_Stage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Stage"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Stage = Stage


@dataclass
class Action:
    Category: Optional[str]
    Configuration: Optional[Sequence["_Configuration"]]
    InputArtifacts: Optional[Sequence[str]]
    Name: Optional[str]
    OutputArtifacts: Optional[Sequence[str]]
    Owner: Optional[str]
    Provider: Optional[str]
    RoleArn: Optional[str]
    RunOrder: Optional[float]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Configuration=json_data.get("Configuration"),
            InputArtifacts=json_data.get("InputArtifacts"),
            Name=json_data.get("Name"),
            OutputArtifacts=json_data.get("OutputArtifacts"),
            Owner=json_data.get("Owner"),
            Provider=json_data.get("Provider"),
            RoleArn=json_data.get("RoleArn"),
            RunOrder=json_data.get("RunOrder"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class Configuration:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Configuration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Configuration"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Configuration = Configuration


