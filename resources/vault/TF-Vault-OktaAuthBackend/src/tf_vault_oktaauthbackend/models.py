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
    Accessor: Optional[str]
    BaseUrl: Optional[str]
    BypassOktaMfa: Optional[bool]
    Description: Optional[str]
    Group: Optional[Sequence["_GroupDefinition"]]
    Id: Optional[str]
    MaxTtl: Optional[str]
    Organization: Optional[str]
    Path: Optional[str]
    Token: Optional[str]
    Ttl: Optional[str]
    User: Optional[Sequence["_UserDefinition"]]

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
            Accessor=json_data.get("Accessor"),
            BaseUrl=json_data.get("BaseUrl"),
            BypassOktaMfa=json_data.get("BypassOktaMfa"),
            Description=json_data.get("Description"),
            Group=deserialize_list(json_data.get("Group"), GroupDefinition),
            Id=json_data.get("Id"),
            MaxTtl=json_data.get("MaxTtl"),
            Organization=json_data.get("Organization"),
            Path=json_data.get("Path"),
            Token=json_data.get("Token"),
            Ttl=json_data.get("Ttl"),
            User=deserialize_list(json_data.get("User"), UserDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GroupDefinition(BaseModel):
    GroupName: Optional[str]
    Policies: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_GroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupName=json_data.get("GroupName"),
            Policies=json_data.get("Policies"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupDefinition = GroupDefinition


@dataclass
class UserDefinition(BaseModel):
    Groups: Optional[Sequence[str]]
    Policies: Optional[Sequence[str]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserDefinition"]:
        if not json_data:
            return None
        return cls(
            Groups=json_data.get("Groups"),
            Policies=json_data.get("Policies"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserDefinition = UserDefinition


