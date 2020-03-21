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
    LabelFingerprint: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    LastAttachTimestamp: Optional[str]
    LastDetachTimestamp: Optional[str]
    Name: Optional[str]
    PhysicalBlockSizeBytes: Optional[float]
    Project: Optional[str]
    Region: Optional[str]
    ReplicaZones: Optional[Sequence[str]]
    SelfLink: Optional[str]
    Size: Optional[float]
    Snapshot: Optional[str]
    SourceSnapshotId: Optional[str]
    Type: Optional[str]
    Users: Optional[Sequence[str]]
    DiskEncryptionKey: Optional[Sequence["_DiskEncryptionKey"]]
    SourceSnapshotEncryptionKey: Optional[Sequence["_SourceSnapshotEncryptionKey"]]
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
            LabelFingerprint=json_data.get("LabelFingerprint"),
            Labels=json_data.get("Labels"),
            LastAttachTimestamp=json_data.get("LastAttachTimestamp"),
            LastDetachTimestamp=json_data.get("LastDetachTimestamp"),
            Name=json_data.get("Name"),
            PhysicalBlockSizeBytes=json_data.get("PhysicalBlockSizeBytes"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            ReplicaZones=json_data.get("ReplicaZones"),
            SelfLink=json_data.get("SelfLink"),
            Size=json_data.get("Size"),
            Snapshot=json_data.get("Snapshot"),
            SourceSnapshotId=json_data.get("SourceSnapshotId"),
            Type=json_data.get("Type"),
            Users=json_data.get("Users"),
            DiskEncryptionKey=json_data.get("DiskEncryptionKey"),
            SourceSnapshotEncryptionKey=json_data.get("SourceSnapshotEncryptionKey"),
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
class DiskEncryptionKey:
    RawKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskEncryptionKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskEncryptionKey"]:
        if not json_data:
            return None
        return cls(
            RawKey=json_data.get("RawKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskEncryptionKey = DiskEncryptionKey


@dataclass
class SourceSnapshotEncryptionKey:
    RawKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceSnapshotEncryptionKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceSnapshotEncryptionKey"]:
        if not json_data:
            return None
        return cls(
            RawKey=json_data.get("RawKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceSnapshotEncryptionKey = SourceSnapshotEncryptionKey


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


