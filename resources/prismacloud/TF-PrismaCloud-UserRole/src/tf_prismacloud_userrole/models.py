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
    AccountGroupIds: Optional[Sequence[str]]
    AccountGroups: Optional[Sequence["_AccountGroupsDefinition"]]
    AssociatedUsers: Optional[Sequence[str]]
    Description: Optional[str]
    Id: Optional[str]
    LastModifiedBy: Optional[str]
    LastModifiedTs: Optional[float]
    Name: Optional[str]
    RestrictDismissalAccess: Optional[bool]
    RoleId: Optional[str]
    RoleType: Optional[str]

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
            AccountGroupIds=json_data.get("AccountGroupIds"),
            AccountGroups=deserialize_list(json_data.get("AccountGroups"), AccountGroupsDefinition),
            AssociatedUsers=json_data.get("AssociatedUsers"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            LastModifiedBy=json_data.get("LastModifiedBy"),
            LastModifiedTs=json_data.get("LastModifiedTs"),
            Name=json_data.get("Name"),
            RestrictDismissalAccess=json_data.get("RestrictDismissalAccess"),
            RoleId=json_data.get("RoleId"),
            RoleType=json_data.get("RoleType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccountGroupsDefinition(BaseModel):
    GroupId: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccountGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupId=json_data.get("GroupId"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountGroupsDefinition = AccountGroupsDefinition


