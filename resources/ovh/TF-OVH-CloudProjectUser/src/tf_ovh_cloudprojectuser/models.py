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
    CreationDate: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    OpenstackRc: Optional[Sequence["_OpenstackRcDefinition"]]
    Password: Optional[str]
    RoleName: Optional[str]
    RoleNames: Optional[Sequence[str]]
    Roles: Optional[Sequence["_RolesDefinition"]]
    ServiceName: Optional[str]
    Status: Optional[str]
    Username: Optional[str]

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
            CreationDate=json_data.get("CreationDate"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            OpenstackRc=deserialize_list(json_data.get("OpenstackRc"), OpenstackRcDefinition),
            Password=json_data.get("Password"),
            RoleName=json_data.get("RoleName"),
            RoleNames=json_data.get("RoleNames"),
            Roles=deserialize_list(json_data.get("Roles"), RolesDefinition),
            ServiceName=json_data.get("ServiceName"),
            Status=json_data.get("Status"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OpenstackRcDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OpenstackRcDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenstackRcDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenstackRcDefinition = OpenstackRcDefinition


@dataclass
class RolesDefinition(BaseModel):
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Permissions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RolesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RolesDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Permissions=json_data.get("Permissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RolesDefinition = RolesDefinition


