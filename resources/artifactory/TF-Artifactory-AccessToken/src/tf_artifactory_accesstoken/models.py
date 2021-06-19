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
    AccessToken: Optional[str]
    Audience: Optional[str]
    EndDate: Optional[str]
    EndDateRelative: Optional[str]
    Groups: Optional[Sequence[str]]
    Id: Optional[str]
    RefreshToken: Optional[str]
    Refreshable: Optional[bool]
    Username: Optional[str]
    AdminToken: Optional[Sequence["_AdminTokenDefinition"]]

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
            AccessToken=json_data.get("AccessToken"),
            Audience=json_data.get("Audience"),
            EndDate=json_data.get("EndDate"),
            EndDateRelative=json_data.get("EndDateRelative"),
            Groups=json_data.get("Groups"),
            Id=json_data.get("Id"),
            RefreshToken=json_data.get("RefreshToken"),
            Refreshable=json_data.get("Refreshable"),
            Username=json_data.get("Username"),
            AdminToken=deserialize_list(json_data.get("AdminToken"), AdminTokenDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdminTokenDefinition(BaseModel):
    InstanceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdminTokenDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdminTokenDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceId=json_data.get("InstanceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdminTokenDefinition = AdminTokenDefinition


