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
    Bucket: Optional[str]
    Domain: Optional[str]
    Email: Optional[str]
    Entity: Optional[str]
    EntityId: Optional[str]
    Generation: Optional[float]
    Id: Optional[str]
    Object: Optional[str]
    ProjectTeam: Optional[Sequence["_ProjectTeamDefinition"]]
    Role: Optional[str]
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
            Bucket=json_data.get("Bucket"),
            Domain=json_data.get("Domain"),
            Email=json_data.get("Email"),
            Entity=json_data.get("Entity"),
            EntityId=json_data.get("EntityId"),
            Generation=json_data.get("Generation"),
            Id=json_data.get("Id"),
            Object=json_data.get("Object"),
            ProjectTeam=deserialize_list(json_data.get("ProjectTeam"), ProjectTeamDefinition),
            Role=json_data.get("Role"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ProjectTeamDefinition(BaseModel):
    ProjectNumber: Optional[str]
    Team: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectTeamDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectTeamDefinition"]:
        if not json_data:
            return None
        return cls(
            ProjectNumber=json_data.get("ProjectNumber"),
            Team=json_data.get("Team"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectTeamDefinition = ProjectTeamDefinition


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

