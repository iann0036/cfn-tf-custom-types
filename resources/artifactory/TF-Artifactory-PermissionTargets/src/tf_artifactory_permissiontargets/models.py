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
    ExcludesPattern: Optional[str]
    Id: Optional[str]
    IncludesPattern: Optional[str]
    Name: Optional[str]
    Repositories: Optional[Sequence[str]]
    Build: Optional[Sequence["_BuildDefinition"]]
    Groups: Optional[Sequence["_GroupsDefinition"]]
    Repo: Optional[Sequence["_RepoDefinition"]]
    Users: Optional[Sequence["_UsersDefinition"]]

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
            ExcludesPattern=json_data.get("ExcludesPattern"),
            Id=json_data.get("Id"),
            IncludesPattern=json_data.get("IncludesPattern"),
            Name=json_data.get("Name"),
            Repositories=json_data.get("Repositories"),
            Build=deserialize_list(json_data.get("Build"), BuildDefinition),
            Groups=deserialize_list(json_data.get("Groups"), GroupsDefinition),
            Repo=deserialize_list(json_data.get("Repo"), RepoDefinition),
            Users=deserialize_list(json_data.get("Users"), UsersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BuildDefinition(BaseModel):
    ExcludesPattern: Optional[Sequence[str]]
    IncludesPattern: Optional[Sequence[str]]
    Repositories: Optional[Sequence[str]]
    Actions: Optional[Sequence["_ActionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BuildDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BuildDefinition"]:
        if not json_data:
            return None
        return cls(
            ExcludesPattern=json_data.get("ExcludesPattern"),
            IncludesPattern=json_data.get("IncludesPattern"),
            Repositories=json_data.get("Repositories"),
            Actions=deserialize_list(json_data.get("Actions"), ActionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BuildDefinition = BuildDefinition


@dataclass
class ActionsDefinition(BaseModel):
    Groups: Optional[Sequence["_GroupsDefinition"]]
    Users: Optional[Sequence["_UsersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Groups=deserialize_list(json_data.get("Groups"), GroupsDefinition),
            Users=deserialize_list(json_data.get("Users"), UsersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionsDefinition = ActionsDefinition


@dataclass
class GroupsDefinition(BaseModel):
    Name: Optional[str]
    Permissions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_GroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Permissions=json_data.get("Permissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupsDefinition = GroupsDefinition


@dataclass
class UsersDefinition(BaseModel):
    Name: Optional[str]
    Permissions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_UsersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsersDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Permissions=json_data.get("Permissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsersDefinition = UsersDefinition


@dataclass
class RepoDefinition(BaseModel):
    ExcludesPattern: Optional[Sequence[str]]
    IncludesPattern: Optional[Sequence[str]]
    Repositories: Optional[Sequence[str]]
    Actions: Optional[Sequence["_ActionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RepoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RepoDefinition"]:
        if not json_data:
            return None
        return cls(
            ExcludesPattern=json_data.get("ExcludesPattern"),
            IncludesPattern=json_data.get("IncludesPattern"),
            Repositories=json_data.get("Repositories"),
            Actions=deserialize_list(json_data.get("Actions"), ActionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RepoDefinition = RepoDefinition


