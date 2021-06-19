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
    CreateDefaultMaintainer: Optional[bool]
    Description: Optional[str]
    Etag: Optional[str]
    Id: Optional[str]
    LdapDn: Optional[str]
    MembersCount: Optional[float]
    Name: Optional[str]
    NodeId: Optional[str]
    ParentTeamId: Optional[float]
    Privacy: Optional[str]
    Slug: Optional[str]

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
            CreateDefaultMaintainer=json_data.get("CreateDefaultMaintainer"),
            Description=json_data.get("Description"),
            Etag=json_data.get("Etag"),
            Id=json_data.get("Id"),
            LdapDn=json_data.get("LdapDn"),
            MembersCount=json_data.get("MembersCount"),
            Name=json_data.get("Name"),
            NodeId=json_data.get("NodeId"),
            ParentTeamId=json_data.get("ParentTeamId"),
            Privacy=json_data.get("Privacy"),
            Slug=json_data.get("Slug"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


