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
    AccountId: Optional[str]
    Id: Optional[str]
    KeyVaultId: Optional[str]
    Name: Optional[str]
    OrgId: Optional[str]
    Password: Optional[str]
    ProviderName: Optional[str]
    Admin: Optional[Sequence["_AdminDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AccountId=json_data.get("AccountId"),
            Id=json_data.get("Id"),
            KeyVaultId=json_data.get("KeyVaultId"),
            Name=json_data.get("Name"),
            OrgId=json_data.get("OrgId"),
            Password=json_data.get("Password"),
            ProviderName=json_data.get("ProviderName"),
            Admin=deserialize_list(json_data.get("Admin"), AdminDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdminDefinition(BaseModel):
    EmailAddress: Optional[str]
    FirstName: Optional[str]
    LastName: Optional[str]
    Phone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdminDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdminDefinition"]:
        if not json_data:
            return None
        return cls(
            EmailAddress=json_data.get("EmailAddress"),
            FirstName=json_data.get("FirstName"),
            LastName=json_data.get("LastName"),
            Phone=json_data.get("Phone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdminDefinition = AdminDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


