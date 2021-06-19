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
    Access: Optional[str]
    Id: Optional[str]
    TeamId: Optional[str]
    WorkspaceId: Optional[str]
    Permissions: Optional[Sequence["_PermissionsDefinition"]]

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
            Access=json_data.get("Access"),
            Id=json_data.get("Id"),
            TeamId=json_data.get("TeamId"),
            WorkspaceId=json_data.get("WorkspaceId"),
            Permissions=deserialize_list(json_data.get("Permissions"), PermissionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PermissionsDefinition(BaseModel):
    Runs: Optional[str]
    SentinelMocks: Optional[str]
    StateVersions: Optional[str]
    Variables: Optional[str]
    WorkspaceLocking: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PermissionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PermissionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Runs=json_data.get("Runs"),
            SentinelMocks=json_data.get("SentinelMocks"),
            StateVersions=json_data.get("StateVersions"),
            Variables=json_data.get("Variables"),
            WorkspaceLocking=json_data.get("WorkspaceLocking"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PermissionsDefinition = PermissionsDefinition


