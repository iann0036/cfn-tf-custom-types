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
    AccessActivityLog: Optional[bool]
    CreateBackupUnit: Optional[bool]
    CreateDatacenter: Optional[bool]
    CreateInternetAccess: Optional[bool]
    CreateK8sCluster: Optional[bool]
    CreatePcc: Optional[bool]
    CreateSnapshot: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    ReserveIp: Optional[bool]
    S3Privilege: Optional[bool]
    UserId: Optional[str]
    Users: Optional[Sequence["_UsersDefinition"]]
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
            AccessActivityLog=json_data.get("AccessActivityLog"),
            CreateBackupUnit=json_data.get("CreateBackupUnit"),
            CreateDatacenter=json_data.get("CreateDatacenter"),
            CreateInternetAccess=json_data.get("CreateInternetAccess"),
            CreateK8sCluster=json_data.get("CreateK8sCluster"),
            CreatePcc=json_data.get("CreatePcc"),
            CreateSnapshot=json_data.get("CreateSnapshot"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ReserveIp=json_data.get("ReserveIp"),
            S3Privilege=json_data.get("S3Privilege"),
            UserId=json_data.get("UserId"),
            Users=deserialize_list(json_data.get("Users"), UsersDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class UsersDefinition(BaseModel):
    Administrator: Optional[bool]
    Email: Optional[str]
    FirstName: Optional[str]
    ForceSecAuth: Optional[bool]
    LastName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UsersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsersDefinition"]:
        if not json_data:
            return None
        return cls(
            Administrator=json_data.get("Administrator"),
            Email=json_data.get("Email"),
            FirstName=json_data.get("FirstName"),
            ForceSecAuth=json_data.get("ForceSecAuth"),
            LastName=json_data.get("LastName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsersDefinition = UsersDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Default: Optional[str]
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
            Default=json_data.get("Default"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


