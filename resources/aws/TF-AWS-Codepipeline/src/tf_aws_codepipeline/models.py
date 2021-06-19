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
    Id: Optional[str]
    Name: Optional[str]
    RoleArn: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    ArtifactStore: Optional[Sequence["_ArtifactStoreDefinition"]]
    Stage: Optional[Sequence["_StageDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RoleArn=json_data.get("RoleArn"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            ArtifactStore=deserialize_list(json_data.get("ArtifactStore"), ArtifactStoreDefinition),
            Stage=deserialize_list(json_data.get("Stage"), StageDefinition),
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
class ArtifactStoreDefinition(BaseModel):
    Location: Optional[str]
    Region: Optional[str]
    Type: Optional[str]
    EncryptionKey: Optional[Sequence["_EncryptionKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ArtifactStoreDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArtifactStoreDefinition"]:
        if not json_data:
            return None
        return cls(
            Location=json_data.get("Location"),
            Region=json_data.get("Region"),
            Type=json_data.get("Type"),
            EncryptionKey=deserialize_list(json_data.get("EncryptionKey"), EncryptionKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArtifactStoreDefinition = ArtifactStoreDefinition


@dataclass
class EncryptionKeyDefinition(BaseModel):
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionKeyDefinition = EncryptionKeyDefinition


@dataclass
class StageDefinition(BaseModel):
    Name: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StageDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StageDefinition = StageDefinition


@dataclass
class ActionDefinition(BaseModel):
    Category: Optional[str]
    Configuration: Optional[Sequence["_ConfigurationDefinition"]]
    InputArtifacts: Optional[Sequence[str]]
    Name: Optional[str]
    Namespace: Optional[str]
    OutputArtifacts: Optional[Sequence[str]]
    Owner: Optional[str]
    Provider: Optional[str]
    Region: Optional[str]
    RoleArn: Optional[str]
    RunOrder: Optional[float]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Configuration=deserialize_list(json_data.get("Configuration"), ConfigurationDefinition),
            InputArtifacts=json_data.get("InputArtifacts"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            OutputArtifacts=json_data.get("OutputArtifacts"),
            Owner=json_data.get("Owner"),
            Provider=json_data.get("Provider"),
            Region=json_data.get("Region"),
            RoleArn=json_data.get("RoleArn"),
            RunOrder=json_data.get("RunOrder"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class ConfigurationDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationDefinition = ConfigurationDefinition


