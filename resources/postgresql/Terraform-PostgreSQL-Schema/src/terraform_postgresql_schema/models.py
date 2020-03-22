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
    Database: Optional[str]
    DropCascade: Optional[bool]
    Id: Optional[str]
    IfNotExists: Optional[bool]
    Name: Optional[str]
    Owner: Optional[str]
    Policy: Optional[Sequence["_Policy"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Database=json_data.get("Database"),
            DropCascade=json_data.get("DropCascade"),
            Id=json_data.get("Id"),
            IfNotExists=json_data.get("IfNotExists"),
            Name=json_data.get("Name"),
            Owner=json_data.get("Owner"),
            Policy=json_data.get("Policy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Policy:
    Create: Optional[bool]
    CreateWithGrant: Optional[bool]
    Role: Optional[str]
    Usage: Optional[bool]
    UsageWithGrant: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Policy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Policy"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            CreateWithGrant=json_data.get("CreateWithGrant"),
            Role=json_data.get("Role"),
            Usage=json_data.get("Usage"),
            UsageWithGrant=json_data.get("UsageWithGrant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Policy = Policy


