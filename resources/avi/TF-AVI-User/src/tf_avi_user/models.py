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
    DefaultTenantRef: Optional[str]
    Email: Optional[str]
    FullName: Optional[str]
    Id: Optional[str]
    IsSuperuser: Optional[bool]
    Local: Optional[bool]
    Name: Optional[str]
    Password: Optional[str]
    UserProfileRef: Optional[str]
    Username: Optional[str]
    Uuid: Optional[str]
    Access: Optional[Sequence["_AccessDefinition"]]

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
            DefaultTenantRef=json_data.get("DefaultTenantRef"),
            Email=json_data.get("Email"),
            FullName=json_data.get("FullName"),
            Id=json_data.get("Id"),
            IsSuperuser=json_data.get("IsSuperuser"),
            Local=json_data.get("Local"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            UserProfileRef=json_data.get("UserProfileRef"),
            Username=json_data.get("Username"),
            Uuid=json_data.get("Uuid"),
            Access=deserialize_list(json_data.get("Access"), AccessDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccessDefinition(BaseModel):
    AllTenants: Optional[bool]
    RoleRef: Optional[str]
    TenantRef: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessDefinition"]:
        if not json_data:
            return None
        return cls(
            AllTenants=json_data.get("AllTenants"),
            RoleRef=json_data.get("RoleRef"),
            TenantRef=json_data.get("TenantRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessDefinition = AccessDefinition


