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
    Admin: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Grant: Optional[Sequence["_Grant"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Admin=json_data.get("Admin"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Grant=json_data.get("Grant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Grant:
    Database: Optional[str]
    Privilege: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Grant"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Grant"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            Privilege=json_data.get("Privilege"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Grant = Grant


