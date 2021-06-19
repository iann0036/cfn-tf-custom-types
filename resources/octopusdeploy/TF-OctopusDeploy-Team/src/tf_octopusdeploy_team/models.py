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
    CanBeDeleted: Optional[bool]
    CanBeRenamed: Optional[bool]
    CanChangeMembers: Optional[bool]
    CanChangeRoles: Optional[bool]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    SpaceId: Optional[str]
    Users: Optional[Sequence[str]]
    ExternalSecurityGroups: Optional[Sequence["_ExternalSecurityGroupsDefinition"]]

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
            CanBeDeleted=json_data.get("CanBeDeleted"),
            CanBeRenamed=json_data.get("CanBeRenamed"),
            CanChangeMembers=json_data.get("CanChangeMembers"),
            CanChangeRoles=json_data.get("CanChangeRoles"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SpaceId=json_data.get("SpaceId"),
            Users=json_data.get("Users"),
            ExternalSecurityGroups=deserialize_list(json_data.get("ExternalSecurityGroups"), ExternalSecurityGroupsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExternalSecurityGroupsDefinition(BaseModel):
    DisplayIdAndName: Optional[bool]
    DisplayName: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalSecurityGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalSecurityGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            DisplayIdAndName=json_data.get("DisplayIdAndName"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalSecurityGroupsDefinition = ExternalSecurityGroupsDefinition


