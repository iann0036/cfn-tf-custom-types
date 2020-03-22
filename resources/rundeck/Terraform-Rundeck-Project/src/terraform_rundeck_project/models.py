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
    DefaultNodeExecutorPlugin: Optional[str]
    DefaultNodeFileCopierPlugin: Optional[str]
    Description: Optional[str]
    ExtraConfig: Optional[Sequence["_ExtraConfig"]]
    Id: Optional[str]
    Name: Optional[str]
    SshAuthenticationType: Optional[str]
    SshKeyFilePath: Optional[str]
    SshKeyStoragePath: Optional[str]
    UiUrl: Optional[str]
    ResourceModelSource: Optional[Sequence["_ResourceModelSource"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DefaultNodeExecutorPlugin=json_data.get("DefaultNodeExecutorPlugin"),
            DefaultNodeFileCopierPlugin=json_data.get("DefaultNodeFileCopierPlugin"),
            Description=json_data.get("Description"),
            ExtraConfig=json_data.get("ExtraConfig"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SshAuthenticationType=json_data.get("SshAuthenticationType"),
            SshKeyFilePath=json_data.get("SshKeyFilePath"),
            SshKeyStoragePath=json_data.get("SshKeyStoragePath"),
            UiUrl=json_data.get("UiUrl"),
            ResourceModelSource=json_data.get("ResourceModelSource"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExtraConfig:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraConfig"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraConfig = ExtraConfig


@dataclass
class ResourceModelSource:
    Config: Optional[Sequence["_Config"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModelSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModelSource"]:
        if not json_data:
            return None
        return cls(
            Config=json_data.get("Config"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModelSource = ResourceModelSource


@dataclass
class Config:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Config"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Config = Config


