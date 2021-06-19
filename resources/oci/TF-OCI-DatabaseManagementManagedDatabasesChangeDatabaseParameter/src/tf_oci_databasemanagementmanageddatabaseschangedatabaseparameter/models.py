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
    Id: Optional[str]
    ManagedDatabaseId: Optional[str]
    Scope: Optional[str]
    Credentials: Optional[Sequence["_CredentialsDefinition"]]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
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
            Id=json_data.get("Id"),
            ManagedDatabaseId=json_data.get("ManagedDatabaseId"),
            Scope=json_data.get("Scope"),
            Credentials=deserialize_list(json_data.get("Credentials"), CredentialsDefinition),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CredentialsDefinition(BaseModel):
    Password: Optional[str]
    Role: Optional[str]
    UserName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CredentialsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CredentialsDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Role=json_data.get("Role"),
            UserName=json_data.get("UserName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CredentialsDefinition = CredentialsDefinition


@dataclass
class ParametersDefinition(BaseModel):
    Name: Optional[str]
    UpdateComment: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            UpdateComment=json_data.get("UpdateComment"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


