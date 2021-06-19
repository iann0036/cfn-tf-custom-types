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
    AwsIamPath: Optional[str]
    AwsManagedPolicy: Optional[bool]
    Description: Optional[str]
    Id: Optional[str]
    LastUpdated: Optional[str]
    Name: Optional[str]
    PathSuffix: Optional[str]
    Policy: Optional[str]
    SystemManagedPolicy: Optional[bool]
    OwnerUserGroups: Optional[Sequence["_OwnerUserGroupsDefinition"]]
    OwnerUsers: Optional[Sequence["_OwnerUsersDefinition"]]

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
            AwsIamPath=json_data.get("AwsIamPath"),
            AwsManagedPolicy=json_data.get("AwsManagedPolicy"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            LastUpdated=json_data.get("LastUpdated"),
            Name=json_data.get("Name"),
            PathSuffix=json_data.get("PathSuffix"),
            Policy=json_data.get("Policy"),
            SystemManagedPolicy=json_data.get("SystemManagedPolicy"),
            OwnerUserGroups=deserialize_list(json_data.get("OwnerUserGroups"), OwnerUserGroupsDefinition),
            OwnerUsers=deserialize_list(json_data.get("OwnerUsers"), OwnerUsersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OwnerUserGroupsDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OwnerUserGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnerUserGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnerUserGroupsDefinition = OwnerUserGroupsDefinition


@dataclass
class OwnerUsersDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OwnerUsersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnerUsersDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnerUsersDefinition = OwnerUsersDefinition


