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
    ApplicationObjectId: Optional[str]
    Backend: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    MaxTtl: Optional[str]
    Role: Optional[str]
    Ttl: Optional[str]
    AzureGroups: Optional[Sequence["_AzureGroupsDefinition"]]
    AzureRoles: Optional[Sequence["_AzureRolesDefinition"]]

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
            ApplicationObjectId=json_data.get("ApplicationObjectId"),
            Backend=json_data.get("Backend"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            MaxTtl=json_data.get("MaxTtl"),
            Role=json_data.get("Role"),
            Ttl=json_data.get("Ttl"),
            AzureGroups=deserialize_list(json_data.get("AzureGroups"), AzureGroupsDefinition),
            AzureRoles=deserialize_list(json_data.get("AzureRoles"), AzureRolesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AzureGroupsDefinition(BaseModel):
    GroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupName=json_data.get("GroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureGroupsDefinition = AzureGroupsDefinition


@dataclass
class AzureRolesDefinition(BaseModel):
    RoleName: Optional[str]
    Scope: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureRolesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureRolesDefinition"]:
        if not json_data:
            return None
        return cls(
            RoleName=json_data.get("RoleName"),
            Scope=json_data.get("Scope"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureRolesDefinition = AzureRolesDefinition


