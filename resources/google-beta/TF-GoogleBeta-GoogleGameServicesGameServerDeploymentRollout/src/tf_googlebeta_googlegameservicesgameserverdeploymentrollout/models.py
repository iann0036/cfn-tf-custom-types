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
    DefaultGameServerConfig: Optional[str]
    DeploymentId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    GameServerConfigOverrides: Optional[Sequence["_GameServerConfigOverridesDefinition"]]
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
            DefaultGameServerConfig=json_data.get("DefaultGameServerConfig"),
            DeploymentId=json_data.get("DeploymentId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            GameServerConfigOverrides=deserialize_list(json_data.get("GameServerConfigOverrides"), GameServerConfigOverridesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GameServerConfigOverridesDefinition(BaseModel):
    ConfigVersion: Optional[str]
    RealmsSelector: Optional[Sequence["_RealmsSelectorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GameServerConfigOverridesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GameServerConfigOverridesDefinition"]:
        if not json_data:
            return None
        return cls(
            ConfigVersion=json_data.get("ConfigVersion"),
            RealmsSelector=deserialize_list(json_data.get("RealmsSelector"), RealmsSelectorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GameServerConfigOverridesDefinition = GameServerConfigOverridesDefinition


@dataclass
class RealmsSelectorDefinition(BaseModel):
    Realms: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RealmsSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RealmsSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Realms=json_data.get("Realms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RealmsSelectorDefinition = RealmsSelectorDefinition


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


