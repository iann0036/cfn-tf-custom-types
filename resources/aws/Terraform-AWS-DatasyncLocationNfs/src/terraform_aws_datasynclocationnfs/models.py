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
    Id: Optional[str]
    ServerHostname: Optional[str]
    Subdirectory: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Uri: Optional[str]
    OnPremConfig: Optional[Sequence["_OnPremConfig"]]

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
            Id=json_data.get("Id"),
            ServerHostname=json_data.get("ServerHostname"),
            Subdirectory=json_data.get("Subdirectory"),
            Tags=json_data.get("Tags"),
            Uri=json_data.get("Uri"),
            OnPremConfig=json_data.get("OnPremConfig"),
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
class OnPremConfig:
    AgentArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_OnPremConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnPremConfig"]:
        if not json_data:
            return None
        return cls(
            AgentArns=json_data.get("AgentArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnPremConfig = OnPremConfig


