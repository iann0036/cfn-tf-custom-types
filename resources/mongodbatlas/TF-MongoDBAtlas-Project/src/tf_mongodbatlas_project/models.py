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
    ClusterCount: Optional[float]
    Created: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OrgId: Optional[str]
    Teams: Optional[Sequence["_TeamsDefinition"]]

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
            ClusterCount=json_data.get("ClusterCount"),
            Created=json_data.get("Created"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OrgId=json_data.get("OrgId"),
            Teams=deserialize_list(json_data.get("Teams"), TeamsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TeamsDefinition(BaseModel):
    RoleNames: Optional[Sequence[str]]
    TeamId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TeamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TeamsDefinition"]:
        if not json_data:
            return None
        return cls(
            RoleNames=json_data.get("RoleNames"),
            TeamId=json_data.get("TeamId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TeamsDefinition = TeamsDefinition


