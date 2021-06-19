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
    AutoSync: Optional[str]
    Description: Optional[str]
    FullLoadOnSync: Optional[str]
    Id: Optional[str]
    IncrementalConfig: Optional[float]
    Name: Optional[str]
    NetworkFailover: Optional[str]
    Partition: Optional[str]
    SaveOnAutoSync: Optional[str]
    Type: Optional[str]
    Device: Optional[Sequence["_DeviceDefinition"]]

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
            AutoSync=json_data.get("AutoSync"),
            Description=json_data.get("Description"),
            FullLoadOnSync=json_data.get("FullLoadOnSync"),
            Id=json_data.get("Id"),
            IncrementalConfig=json_data.get("IncrementalConfig"),
            Name=json_data.get("Name"),
            NetworkFailover=json_data.get("NetworkFailover"),
            Partition=json_data.get("Partition"),
            SaveOnAutoSync=json_data.get("SaveOnAutoSync"),
            Type=json_data.get("Type"),
            Device=deserialize_list(json_data.get("Device"), DeviceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DeviceDefinition(BaseModel):
    Name: Optional[str]
    SetSyncLeader: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            SetSyncLeader=json_data.get("SetSyncLeader"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceDefinition = DeviceDefinition


