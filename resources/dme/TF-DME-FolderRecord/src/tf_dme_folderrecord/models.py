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
    DefaultFolder: Optional[bool]
    Domains: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    Secondaries: Optional[Sequence[str]]
    FolderPermissions: Optional[Sequence["_FolderPermissionsDefinition"]]

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
            DefaultFolder=json_data.get("DefaultFolder"),
            Domains=json_data.get("Domains"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Secondaries=json_data.get("Secondaries"),
            FolderPermissions=deserialize_list(json_data.get("FolderPermissions"), FolderPermissionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FolderPermissionsDefinition(BaseModel):
    GroupId: Optional[float]
    GroupName: Optional[str]
    Permission: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FolderPermissionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FolderPermissionsDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupId=json_data.get("GroupId"),
            GroupName=json_data.get("GroupName"),
            Permission=json_data.get("Permission"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FolderPermissionsDefinition = FolderPermissionsDefinition


