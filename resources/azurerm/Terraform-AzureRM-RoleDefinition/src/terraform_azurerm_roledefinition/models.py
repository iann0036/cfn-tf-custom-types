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
    AssignableScopes: Optional[Sequence[str]]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    RoleDefinitionId: Optional[str]
    Scope: Optional[str]
    Permissions: Optional[Sequence["_Permissions"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AssignableScopes=json_data.get("AssignableScopes"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RoleDefinitionId=json_data.get("RoleDefinitionId"),
            Scope=json_data.get("Scope"),
            Permissions=json_data.get("Permissions"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Permissions:
    Actions: Optional[Sequence[str]]
    DataActions: Optional[Sequence[str]]
    NotActions: Optional[Sequence[str]]
    NotDataActions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Permissions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Permissions"]:
        if not json_data:
            return None
        return cls(
            Actions=json_data.get("Actions"),
            DataActions=json_data.get("DataActions"),
            NotActions=json_data.get("NotActions"),
            NotDataActions=json_data.get("NotDataActions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Permissions = Permissions


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


