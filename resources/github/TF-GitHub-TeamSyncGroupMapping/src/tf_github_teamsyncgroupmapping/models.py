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
    Etag: Optional[str]
    Id: Optional[str]
    TeamSlug: Optional[str]
    Group: Optional[Sequence["_GroupDefinition"]]

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
            Etag=json_data.get("Etag"),
            Id=json_data.get("Id"),
            TeamSlug=json_data.get("TeamSlug"),
            Group=deserialize_list(json_data.get("Group"), GroupDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GroupDefinition(BaseModel):
    GroupDescription: Optional[str]
    GroupId: Optional[str]
    GroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupDescription=json_data.get("GroupDescription"),
            GroupId=json_data.get("GroupId"),
            GroupName=json_data.get("GroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupDefinition = GroupDefinition


