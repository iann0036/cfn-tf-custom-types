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
    Id: Optional[str]
    User: Optional[str]
    Vhost: Optional[str]
    Permissions: Optional[Sequence["_Permissions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            User=json_data.get("User"),
            Vhost=json_data.get("Vhost"),
            Permissions=json_data.get("Permissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Permissions:
    Exchange: Optional[str]
    Read: Optional[str]
    Write: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Permissions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Permissions"]:
        if not json_data:
            return None
        return cls(
            Exchange=json_data.get("Exchange"),
            Read=json_data.get("Read"),
            Write=json_data.get("Write"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Permissions = Permissions


