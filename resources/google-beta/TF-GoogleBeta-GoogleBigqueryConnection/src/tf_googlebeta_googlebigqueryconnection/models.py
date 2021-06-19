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
    ConnectionId: Optional[str]
    Description: Optional[str]
    FriendlyName: Optional[str]
    HasCredential: Optional[bool]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    CloudSql: Optional[Sequence["_CloudSqlDefinition"]]
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
            ConnectionId=json_data.get("ConnectionId"),
            Description=json_data.get("Description"),
            FriendlyName=json_data.get("FriendlyName"),
            HasCredential=json_data.get("HasCredential"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            CloudSql=deserialize_list(json_data.get("CloudSql"), CloudSqlDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CloudSqlDefinition(BaseModel):
    Database: Optional[str]
    InstanceId: Optional[str]
    Type: Optional[str]
    Credential: Optional[Sequence["_CredentialDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CloudSqlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudSqlDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            InstanceId=json_data.get("InstanceId"),
            Type=json_data.get("Type"),
            Credential=deserialize_list(json_data.get("Credential"), CredentialDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudSqlDefinition = CloudSqlDefinition


@dataclass
class CredentialDefinition(BaseModel):
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CredentialDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CredentialDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CredentialDefinition = CredentialDefinition


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


