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
    Config: Optional[Sequence["_ConfigDefinition"]]
    ConnectorName: Optional[str]
    Id: Optional[str]
    PluginAuthor: Optional[str]
    PluginClass: Optional[str]
    PluginDocUrl: Optional[str]
    PluginTitle: Optional[str]
    PluginType: Optional[str]
    PluginVersion: Optional[str]
    Project: Optional[str]
    ServiceName: Optional[str]
    Task: Optional[Sequence["_TaskDefinition"]]
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
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
            ConnectorName=json_data.get("ConnectorName"),
            Id=json_data.get("Id"),
            PluginAuthor=json_data.get("PluginAuthor"),
            PluginClass=json_data.get("PluginClass"),
            PluginDocUrl=json_data.get("PluginDocUrl"),
            PluginTitle=json_data.get("PluginTitle"),
            PluginType=json_data.get("PluginType"),
            PluginVersion=json_data.get("PluginVersion"),
            Project=json_data.get("Project"),
            ServiceName=json_data.get("ServiceName"),
            Task=deserialize_list(json_data.get("Task"), TaskDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConfigDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


@dataclass
class TaskDefinition(BaseModel):
    Connector: Optional[str]
    Task: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TaskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskDefinition"]:
        if not json_data:
            return None
        return cls(
            Connector=json_data.get("Connector"),
            Task=json_data.get("Task"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskDefinition = TaskDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Read: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Read=json_data.get("Read"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


