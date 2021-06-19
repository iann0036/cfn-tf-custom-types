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
    AccountStatus: Optional[str]
    Domain: Optional[str]
    Email: Optional[str]
    FirstName: Optional[str]
    Id: Optional[str]
    LastName: Optional[str]
    Phone: Optional[str]
    UserPassword: Optional[str]
    Username: Optional[str]
    Roles: Optional[Sequence["_RolesDefinition"]]

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
            AccountStatus=json_data.get("AccountStatus"),
            Domain=json_data.get("Domain"),
            Email=json_data.get("Email"),
            FirstName=json_data.get("FirstName"),
            Id=json_data.get("Id"),
            LastName=json_data.get("LastName"),
            Phone=json_data.get("Phone"),
            UserPassword=json_data.get("UserPassword"),
            Username=json_data.get("Username"),
            Roles=deserialize_list(json_data.get("Roles"), RolesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RolesDefinition(BaseModel):
    AccessType: Optional[str]
    Roleid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RolesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RolesDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessType=json_data.get("AccessType"),
            Roleid=json_data.get("Roleid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RolesDefinition = RolesDefinition


