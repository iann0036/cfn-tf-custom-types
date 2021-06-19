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
    EdgeIds: Optional[Sequence[str]]
    EdgeSelectorType: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Privileged: Optional[bool]
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
            Description=json_data.get("Description"),
            EdgeIds=json_data.get("EdgeIds"),
            EdgeSelectorType=json_data.get("EdgeSelectorType"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Privileged=json_data.get("Privileged"),
            User=deserialize_list(json_data.get("User"), UserDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class UserDefinition(BaseModel):
    Role: Optional[str]
    UserId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserDefinition"]:
        if not json_data:
            return None
        return cls(
            Role=json_data.get("Role"),
            UserId=json_data.get("UserId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserDefinition = UserDefinition


