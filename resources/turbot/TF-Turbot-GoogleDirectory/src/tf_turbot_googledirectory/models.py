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
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    Description: Optional[str]
    DirectoryType: Optional[str]
    GroupIdTemplate: Optional[str]
    HostedName: Optional[str]
    Id: Optional[str]
    KeyFingerprint: Optional[str]
    LoginNameTemplate: Optional[str]
    Parent: Optional[str]
    ParentAkas: Optional[Sequence[str]]
    PgpKey: Optional[str]
    PoolId: Optional[str]
    ProfileIdTemplate: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Title: Optional[str]

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
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            Description=json_data.get("Description"),
            DirectoryType=json_data.get("DirectoryType"),
            GroupIdTemplate=json_data.get("GroupIdTemplate"),
            HostedName=json_data.get("HostedName"),
            Id=json_data.get("Id"),
            KeyFingerprint=json_data.get("KeyFingerprint"),
            LoginNameTemplate=json_data.get("LoginNameTemplate"),
            Parent=json_data.get("Parent"),
            ParentAkas=json_data.get("ParentAkas"),
            PgpKey=json_data.get("PgpKey"),
            PoolId=json_data.get("PoolId"),
            ProfileIdTemplate=json_data.get("ProfileIdTemplate"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Title=json_data.get("Title"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


