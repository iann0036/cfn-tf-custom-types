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
    Id: Optional[str]
    MaximumBytesPerPacket: Optional[float]
    MaximumBytesPerSession: Optional[float]
    MaximumCaptureDuration: Optional[float]
    Name: Optional[str]
    NetworkWatcherName: Optional[str]
    ResourceGroupName: Optional[str]
    TargetResourceId: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]
    StorageLocation: Optional[Sequence["_StorageLocationDefinition"]]
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
            Id=json_data.get("Id"),
            MaximumBytesPerPacket=json_data.get("MaximumBytesPerPacket"),
            MaximumBytesPerSession=json_data.get("MaximumBytesPerSession"),
            MaximumCaptureDuration=json_data.get("MaximumCaptureDuration"),
            Name=json_data.get("Name"),
            NetworkWatcherName=json_data.get("NetworkWatcherName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            TargetResourceId=json_data.get("TargetResourceId"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
            StorageLocation=deserialize_list(json_data.get("StorageLocation"), StorageLocationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FilterDefinition(BaseModel):
    LocalIpAddress: Optional[str]
    LocalPort: Optional[str]
    Protocol: Optional[str]
    RemoteIpAddress: Optional[str]
    RemotePort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            LocalIpAddress=json_data.get("LocalIpAddress"),
            LocalPort=json_data.get("LocalPort"),
            Protocol=json_data.get("Protocol"),
            RemoteIpAddress=json_data.get("RemoteIpAddress"),
            RemotePort=json_data.get("RemotePort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class StorageLocationDefinition(BaseModel):
    FilePath: Optional[str]
    StorageAccountId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageLocationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageLocationDefinition"]:
        if not json_data:
            return None
        return cls(
            FilePath=json_data.get("FilePath"),
            StorageAccountId=json_data.get("StorageAccountId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageLocationDefinition = StorageLocationDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


