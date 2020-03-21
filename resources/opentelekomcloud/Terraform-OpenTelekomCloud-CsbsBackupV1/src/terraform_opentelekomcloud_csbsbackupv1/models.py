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
    BackupName: Optional[str]
    BackupRecordId: Optional[str]
    Description: Optional[str]
    Region: Optional[str]
    ResourceId: Optional[str]
    ResourceType: Optional[str]
    Status: Optional[str]
    VmMetadata: Optional[Sequence["_VmMetadata"]]
    VolumeBackups: Optional[Sequence["_VolumeBackups"]]
    Tags: Optional[Sequence["_Tags"]]
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
            BackupName=json_data.get("BackupName"),
            BackupRecordId=json_data.get("BackupRecordId"),
            Description=json_data.get("Description"),
            Region=json_data.get("Region"),
            ResourceId=json_data.get("ResourceId"),
            ResourceType=json_data.get("ResourceType"),
            Status=json_data.get("Status"),
            VmMetadata=json_data.get("VmMetadata"),
            VolumeBackups=json_data.get("VolumeBackups"),
            Tags=json_data.get("Tags"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class VmMetadata:
    CloudServiceType: Optional[str]
    Disk: Optional[float]
    Eip: Optional[str]
    ImageType: Optional[str]
    Name: Optional[str]
    PrivateIp: Optional[str]
    Ram: Optional[float]
    Vcpus: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VmMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VmMetadata"]:
        if not json_data:
            return None
        return cls(
            CloudServiceType=json_data.get("CloudServiceType"),
            Disk=json_data.get("Disk"),
            Eip=json_data.get("Eip"),
            ImageType=json_data.get("ImageType"),
            Name=json_data.get("Name"),
            PrivateIp=json_data.get("PrivateIp"),
            Ram=json_data.get("Ram"),
            Vcpus=json_data.get("Vcpus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VmMetadata = VmMetadata


@dataclass
class VolumeBackups:
    AverageSpeed: Optional[float]
    Bootable: Optional[bool]
    Id: Optional[str]
    ImageType: Optional[str]
    Incremental: Optional[bool]
    Name: Optional[str]
    Size: Optional[float]
    SnapshotId: Optional[str]
    SourceVolumeId: Optional[str]
    SourceVolumeName: Optional[str]
    SourceVolumeSize: Optional[float]
    SpaceSavingRatio: Optional[float]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeBackups"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeBackups"]:
        if not json_data:
            return None
        return cls(
            AverageSpeed=json_data.get("AverageSpeed"),
            Bootable=json_data.get("Bootable"),
            Id=json_data.get("Id"),
            ImageType=json_data.get("ImageType"),
            Incremental=json_data.get("Incremental"),
            Name=json_data.get("Name"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
            SourceVolumeId=json_data.get("SourceVolumeId"),
            SourceVolumeName=json_data.get("SourceVolumeName"),
            SourceVolumeSize=json_data.get("SourceVolumeSize"),
            SpaceSavingRatio=json_data.get("SpaceSavingRatio"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeBackups = VolumeBackups


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


