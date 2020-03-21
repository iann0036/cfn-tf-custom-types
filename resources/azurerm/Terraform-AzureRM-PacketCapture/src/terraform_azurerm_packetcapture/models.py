# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    MaximumBytesPerPacket: Optional[float]
    MaximumBytesPerSession: Optional[float]
    MaximumCaptureDuration: Optional[float]
    Name: Optional[str]
    NetworkWatcherName: Optional[str]
    ResourceGroupName: Optional[str]
    TargetResourceId: Optional[str]
    Filter: Optional[Sequence["_Filter"]]
    StorageLocation: Optional[Sequence["_StorageLocation"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            MaximumBytesPerPacket=json_data.get("MaximumBytesPerPacket"),
            MaximumBytesPerSession=json_data.get("MaximumBytesPerSession"),
            MaximumCaptureDuration=json_data.get("MaximumCaptureDuration"),
            Name=json_data.get("Name"),
            NetworkWatcherName=json_data.get("NetworkWatcherName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            TargetResourceId=json_data.get("TargetResourceId"),
            Filter=json_data.get("Filter"),
            StorageLocation=json_data.get("StorageLocation"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Filter:
    LocalIpAddress: Optional[str]
    LocalPort: Optional[str]
    Protocol: Optional[str]
    RemoteIpAddress: Optional[str]
    RemotePort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
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
_Filter = Filter


@dataclass
class StorageLocation:
    FilePath: Optional[str]
    StorageAccountId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageLocation"]:
        if not json_data:
            return None
        return cls(
            FilePath=json_data.get("FilePath"),
            StorageAccountId=json_data.get("StorageAccountId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageLocation = StorageLocation


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


