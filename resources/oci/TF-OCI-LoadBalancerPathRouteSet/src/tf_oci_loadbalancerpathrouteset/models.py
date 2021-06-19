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
    LoadBalancerId: Optional[str]
    Name: Optional[str]
    State: Optional[str]
    PathRoutes: Optional[Sequence["_PathRoutesDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            LoadBalancerId=json_data.get("LoadBalancerId"),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            PathRoutes=deserialize_list(json_data.get("PathRoutes"), PathRoutesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PathRoutesDefinition(BaseModel):
    BackendSetName: Optional[str]
    Path: Optional[str]
    PathMatchType: Optional[Sequence["_PathMatchTypeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PathRoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathRoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            BackendSetName=json_data.get("BackendSetName"),
            Path=json_data.get("Path"),
            PathMatchType=deserialize_list(json_data.get("PathMatchType"), PathMatchTypeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathRoutesDefinition = PathRoutesDefinition


@dataclass
class PathMatchTypeDefinition(BaseModel):
    MatchType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PathMatchTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathMatchTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchType=json_data.get("MatchType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathMatchTypeDefinition = PathMatchTypeDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


