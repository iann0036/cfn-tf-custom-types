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
    MessageRetention: Optional[float]
    Name: Optional[str]
    NamespaceName: Optional[str]
    PartitionCount: Optional[float]
    PartitionIds: Optional[Sequence[str]]
    ResourceGroupName: Optional[str]
    Status: Optional[str]
    CaptureDescription: Optional[Sequence["_CaptureDescriptionDefinition"]]
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
            MessageRetention=json_data.get("MessageRetention"),
            Name=json_data.get("Name"),
            NamespaceName=json_data.get("NamespaceName"),
            PartitionCount=json_data.get("PartitionCount"),
            PartitionIds=json_data.get("PartitionIds"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Status=json_data.get("Status"),
            CaptureDescription=deserialize_list(json_data.get("CaptureDescription"), CaptureDescriptionDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CaptureDescriptionDefinition(BaseModel):
    Enabled: Optional[bool]
    Encoding: Optional[str]
    IntervalInSeconds: Optional[float]
    SizeLimitInBytes: Optional[float]
    SkipEmptyArchives: Optional[bool]
    Destination: Optional[Sequence["_DestinationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CaptureDescriptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaptureDescriptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Encoding=json_data.get("Encoding"),
            IntervalInSeconds=json_data.get("IntervalInSeconds"),
            SizeLimitInBytes=json_data.get("SizeLimitInBytes"),
            SkipEmptyArchives=json_data.get("SkipEmptyArchives"),
            Destination=deserialize_list(json_data.get("Destination"), DestinationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaptureDescriptionDefinition = CaptureDescriptionDefinition


@dataclass
class DestinationDefinition(BaseModel):
    ArchiveNameFormat: Optional[str]
    BlobContainerName: Optional[str]
    Name: Optional[str]
    StorageAccountId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveNameFormat=json_data.get("ArchiveNameFormat"),
            BlobContainerName=json_data.get("BlobContainerName"),
            Name=json_data.get("Name"),
            StorageAccountId=json_data.get("StorageAccountId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationDefinition = DestinationDefinition


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


