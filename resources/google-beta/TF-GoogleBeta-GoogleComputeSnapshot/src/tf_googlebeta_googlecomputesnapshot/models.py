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
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    DiskSizeGb: Optional[float]
    Id: Optional[str]
    LabelFingerprint: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Licenses: Optional[Sequence[str]]
    Name: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    SnapshotId: Optional[float]
    SourceDisk: Optional[str]
    SourceDiskLink: Optional[str]
    StorageBytes: Optional[float]
    StorageLocations: Optional[Sequence[str]]
    Zone: Optional[str]
    SnapshotEncryptionKey: Optional[Sequence["_SnapshotEncryptionKeyDefinition"]]
    SourceDiskEncryptionKey: Optional[Sequence["_SourceDiskEncryptionKeyDefinition"]]
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
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            DiskSizeGb=json_data.get("DiskSizeGb"),
            Id=json_data.get("Id"),
            LabelFingerprint=json_data.get("LabelFingerprint"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Licenses=json_data.get("Licenses"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            SnapshotId=json_data.get("SnapshotId"),
            SourceDisk=json_data.get("SourceDisk"),
            SourceDiskLink=json_data.get("SourceDiskLink"),
            StorageBytes=json_data.get("StorageBytes"),
            StorageLocations=json_data.get("StorageLocations"),
            Zone=json_data.get("Zone"),
            SnapshotEncryptionKey=deserialize_list(json_data.get("SnapshotEncryptionKey"), SnapshotEncryptionKeyDefinition),
            SourceDiskEncryptionKey=deserialize_list(json_data.get("SourceDiskEncryptionKey"), SourceDiskEncryptionKeyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class SnapshotEncryptionKeyDefinition(BaseModel):
    KmsKeySelfLink: Optional[str]
    KmsKeyServiceAccount: Optional[str]
    RawKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotEncryptionKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotEncryptionKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeySelfLink=json_data.get("KmsKeySelfLink"),
            KmsKeyServiceAccount=json_data.get("KmsKeyServiceAccount"),
            RawKey=json_data.get("RawKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotEncryptionKeyDefinition = SnapshotEncryptionKeyDefinition


@dataclass
class SourceDiskEncryptionKeyDefinition(BaseModel):
    KmsKeyServiceAccount: Optional[str]
    RawKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDiskEncryptionKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDiskEncryptionKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeyServiceAccount=json_data.get("KmsKeyServiceAccount"),
            RawKey=json_data.get("RawKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDiskEncryptionKeyDefinition = SourceDiskEncryptionKeyDefinition


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


