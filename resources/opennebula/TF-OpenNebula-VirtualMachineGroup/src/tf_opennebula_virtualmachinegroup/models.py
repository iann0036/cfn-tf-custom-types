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
    Gid: Optional[float]
    Gname: Optional[str]
    Group: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Permissions: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Uid: Optional[float]
    Uname: Optional[str]
    Role: Optional[Sequence["_RoleDefinition"]]

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
            Gid=json_data.get("Gid"),
            Gname=json_data.get("Gname"),
            Group=json_data.get("Group"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Permissions=json_data.get("Permissions"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Uid=json_data.get("Uid"),
            Uname=json_data.get("Uname"),
            Role=deserialize_list(json_data.get("Role"), RoleDefinition),
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


@dataclass
class RoleDefinition(BaseModel):
    HostAffined: Optional[Sequence[float]]
    HostAntiAffined: Optional[Sequence[float]]
    Name: Optional[str]
    Policy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RoleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoleDefinition"]:
        if not json_data:
            return None
        return cls(
            HostAffined=json_data.get("HostAffined"),
            HostAntiAffined=json_data.get("HostAntiAffined"),
            Name=json_data.get("Name"),
            Policy=json_data.get("Policy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoleDefinition = RoleDefinition


