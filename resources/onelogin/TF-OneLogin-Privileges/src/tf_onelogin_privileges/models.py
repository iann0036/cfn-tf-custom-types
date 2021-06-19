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
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    RoleIds: Optional[Sequence[float]]
    UserIds: Optional[Sequence[float]]
    Privilege: Optional[Sequence["_PrivilegeDefinition"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RoleIds=json_data.get("RoleIds"),
            UserIds=json_data.get("UserIds"),
            Privilege=deserialize_list(json_data.get("Privilege"), PrivilegeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PrivilegeDefinition(BaseModel):
    Version: Optional[str]
    Statement: Optional[Sequence["_StatementDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrivilegeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivilegeDefinition"]:
        if not json_data:
            return None
        return cls(
            Version=json_data.get("Version"),
            Statement=deserialize_list(json_data.get("Statement"), StatementDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivilegeDefinition = PrivilegeDefinition


@dataclass
class StatementDefinition(BaseModel):
    Action: Optional[Sequence[str]]
    Effect: Optional[str]
    Scope: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_StatementDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatementDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Effect=json_data.get("Effect"),
            Scope=json_data.get("Scope"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatementDefinition = StatementDefinition


