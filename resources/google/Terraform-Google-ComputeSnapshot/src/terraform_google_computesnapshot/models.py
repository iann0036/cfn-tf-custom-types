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
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    DiskSizeGb: Optional[float]
    Id: Optional[str]
    LabelFingerprint: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    Licenses: Optional[Sequence[str]]
    Name: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    SnapshotId: Optional[float]
    SourceDisk: Optional[str]
    SourceDiskLink: Optional[str]
    StorageBytes: Optional[float]
    Zone: Optional[str]
    SnapshotEncryptionKey: Optional[Sequence["_SnapshotEncryptionKey"]]
    SourceDiskEncryptionKey: Optional[Sequence["_SourceDiskEncryptionKey"]]
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
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            DiskSizeGb=json_data.get("DiskSizeGb"),
            Id=json_data.get("Id"),
            LabelFingerprint=json_data.get("LabelFingerprint"),
            Labels=json_data.get("Labels"),
            Licenses=json_data.get("Licenses"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            SnapshotId=json_data.get("SnapshotId"),
            SourceDisk=json_data.get("SourceDisk"),
            SourceDiskLink=json_data.get("SourceDiskLink"),
            StorageBytes=json_data.get("StorageBytes"),
            Zone=json_data.get("Zone"),
            SnapshotEncryptionKey=json_data.get("SnapshotEncryptionKey"),
            SourceDiskEncryptionKey=json_data.get("SourceDiskEncryptionKey"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class SnapshotEncryptionKey:
    RawKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotEncryptionKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotEncryptionKey"]:
        if not json_data:
            return None
        return cls(
            RawKey=json_data.get("RawKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotEncryptionKey = SnapshotEncryptionKey


@dataclass
class SourceDiskEncryptionKey:
    RawKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDiskEncryptionKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDiskEncryptionKey"]:
        if not json_data:
            return None
        return cls(
            RawKey=json_data.get("RawKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDiskEncryptionKey = SourceDiskEncryptionKey


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


