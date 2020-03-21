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
    Id: Optional[str]
    MessageRetention: Optional[float]
    Name: Optional[str]
    NamespaceName: Optional[str]
    PartitionCount: Optional[float]
    PartitionIds: Optional[Sequence[str]]
    ResourceGroupName: Optional[str]
    CaptureDescription: Optional[Sequence["_CaptureDescription"]]
    Timeouts: Optional["_Timeouts"]
    Destination: Optional[Sequence["_Destination"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            MessageRetention=json_data.get("MessageRetention"),
            Name=json_data.get("Name"),
            NamespaceName=json_data.get("NamespaceName"),
            PartitionCount=json_data.get("PartitionCount"),
            PartitionIds=json_data.get("PartitionIds"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            CaptureDescription=json_data.get("CaptureDescription"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Destination=json_data.get("Destination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CaptureDescription:
    Enabled: Optional[bool]
    Encoding: Optional[str]
    IntervalInSeconds: Optional[float]
    SizeLimitInBytes: Optional[float]
    SkipEmptyArchives: Optional[bool]
    Destination: Optional[Sequence["_Destination"]]

    @classmethod
    def _deserialize(
        cls: Type["_CaptureDescription"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaptureDescription"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Encoding=json_data.get("Encoding"),
            IntervalInSeconds=json_data.get("IntervalInSeconds"),
            SizeLimitInBytes=json_data.get("SizeLimitInBytes"),
            SkipEmptyArchives=json_data.get("SkipEmptyArchives"),
            Destination=json_data.get("Destination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaptureDescription = CaptureDescription


@dataclass
class Destination:
    ArchiveNameFormat: Optional[str]
    BlobContainerName: Optional[str]
    Name: Optional[str]
    StorageAccountId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Destination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Destination"]:
        if not json_data:
            return None
        return cls(
            ArchiveNameFormat=json_data.get("ArchiveNameFormat"),
            BlobContainerName=json_data.get("BlobContainerName"),
            Name=json_data.get("Name"),
            StorageAccountId=json_data.get("StorageAccountId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Destination = Destination


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


