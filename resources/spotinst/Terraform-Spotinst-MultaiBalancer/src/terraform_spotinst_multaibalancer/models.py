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
    DnsCnameAliases: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    Scheme: Optional[str]
    ConnectionTimeouts: Optional[Sequence["_ConnectionTimeouts"]]
    Tags: Optional[Sequence["_Tags"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DnsCnameAliases=json_data.get("DnsCnameAliases"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Scheme=json_data.get("Scheme"),
            ConnectionTimeouts=json_data.get("ConnectionTimeouts"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConnectionTimeouts:
    Draining: Optional[float]
    Idle: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionTimeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionTimeouts"]:
        if not json_data:
            return None
        return cls(
            Draining=json_data.get("Draining"),
            Idle=json_data.get("Idle"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionTimeouts = ConnectionTimeouts


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


