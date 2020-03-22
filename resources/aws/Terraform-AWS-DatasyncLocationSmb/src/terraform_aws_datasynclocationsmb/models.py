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
    AgentArns: Optional[Sequence[str]]
    Arn: Optional[str]
    Domain: Optional[str]
    Id: Optional[str]
    Password: Optional[str]
    ServerHostname: Optional[str]
    Subdirectory: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Uri: Optional[str]
    User: Optional[str]
    MountOptions: Optional[Sequence["_MountOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AgentArns=json_data.get("AgentArns"),
            Arn=json_data.get("Arn"),
            Domain=json_data.get("Domain"),
            Id=json_data.get("Id"),
            Password=json_data.get("Password"),
            ServerHostname=json_data.get("ServerHostname"),
            Subdirectory=json_data.get("Subdirectory"),
            Tags=json_data.get("Tags"),
            Uri=json_data.get("Uri"),
            User=json_data.get("User"),
            MountOptions=json_data.get("MountOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class MountOptions:
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MountOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MountOptions"]:
        if not json_data:
            return None
        return cls(
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MountOptions = MountOptions


