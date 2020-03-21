# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Id: Optional[str]
    LoadBalancerId: Optional[str]
    Name: Optional[str]
    State: Optional[str]
    PathRoutes: Optional[Sequence["_PathRoutes"]]
    Timeouts: Optional["_Timeouts"]
    PathMatchType: Optional[Sequence["_PathMatchType"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            PathRoutes=json_data.get("PathRoutes"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            PathMatchType=json_data.get("PathMatchType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PathRoutes:
    BackendSetName: Optional[str]
    Path: Optional[str]
    PathMatchType: Optional[Sequence["_PathMatchType"]]

    @classmethod
    def _deserialize(
        cls: Type["_PathRoutes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathRoutes"]:
        if not json_data:
            return None
        return cls(
            BackendSetName=json_data.get("BackendSetName"),
            Path=json_data.get("Path"),
            PathMatchType=json_data.get("PathMatchType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathRoutes = PathRoutes


@dataclass
class PathMatchType:
    MatchType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PathMatchType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathMatchType"]:
        if not json_data:
            return None
        return cls(
            MatchType=json_data.get("MatchType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathMatchType = PathMatchType


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


