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
    ProjectId: Optional[str]
    RoleName: Optional[str]
    Actions: Optional[Sequence["_ActionsDefinition"]]
    InheritedRoles: Optional[Sequence["_InheritedRolesDefinition"]]

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
            ProjectId=json_data.get("ProjectId"),
            RoleName=json_data.get("RoleName"),
            Actions=deserialize_list(json_data.get("Actions"), ActionsDefinition),
            InheritedRoles=deserialize_list(json_data.get("InheritedRoles"), InheritedRolesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ActionsDefinition(BaseModel):
    Action: Optional[str]
    Resources: Optional[Sequence["_ResourcesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Resources=deserialize_list(json_data.get("Resources"), ResourcesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionsDefinition = ActionsDefinition


@dataclass
class ResourcesDefinition(BaseModel):
    Cluster: Optional[bool]
    CollectionName: Optional[str]
    DatabaseName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            Cluster=json_data.get("Cluster"),
            CollectionName=json_data.get("CollectionName"),
            DatabaseName=json_data.get("DatabaseName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcesDefinition = ResourcesDefinition


@dataclass
class InheritedRolesDefinition(BaseModel):
    DatabaseName: Optional[str]
    RoleName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InheritedRolesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InheritedRolesDefinition"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            RoleName=json_data.get("RoleName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InheritedRolesDefinition = InheritedRolesDefinition


