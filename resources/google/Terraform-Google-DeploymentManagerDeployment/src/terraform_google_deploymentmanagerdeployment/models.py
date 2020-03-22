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
    CreatePolicy: Optional[str]
    DeletePolicy: Optional[str]
    DeploymentId: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Manifest: Optional[str]
    Name: Optional[str]
    Preview: Optional[bool]
    Project: Optional[str]
    SelfLink: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    Target: Optional[Sequence["_Target"]]
    Timeouts: Optional["_Timeouts"]
    Config: Optional[Sequence["_Config"]]
    Imports: Optional[Sequence["_Imports"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreatePolicy=json_data.get("CreatePolicy"),
            DeletePolicy=json_data.get("DeletePolicy"),
            DeploymentId=json_data.get("DeploymentId"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Manifest=json_data.get("Manifest"),
            Name=json_data.get("Name"),
            Preview=json_data.get("Preview"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            Labels=json_data.get("Labels"),
            Target=json_data.get("Target"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Config=json_data.get("Config"),
            Imports=json_data.get("Imports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class Target:
    Config: Optional[Sequence["_Config"]]
    Imports: Optional[Sequence["_Imports"]]

    @classmethod
    def _deserialize(
        cls: Type["_Target"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Target"]:
        if not json_data:
            return None
        return cls(
            Config=json_data.get("Config"),
            Imports=json_data.get("Imports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Target = Target


@dataclass
class Config:
    Content: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Config"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Config = Config


@dataclass
class Imports:
    Content: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Imports"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Imports"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Imports = Imports


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


