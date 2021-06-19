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
    Id: Optional[str]
    Image: Optional[str]
    Interface: Optional[str]
    LabelFingerprint: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    LastAttachTimestamp: Optional[str]
    LastDetachTimestamp: Optional[str]
    MultiWriter: Optional[bool]
    Name: Optional[str]
    PhysicalBlockSizeBytes: Optional[float]
    Project: Optional[str]
    ProvisionedIops: Optional[float]
    ResourcePolicies: Optional[Sequence[str]]
    SelfLink: Optional[str]
    Size: Optional[float]
    Snapshot: Optional[str]
    SourceImageId: Optional[str]
    SourceSnapshotId: Optional[str]
    Type: Optional[str]
    Users: Optional[Sequence[str]]
    Zone: Optional[str]
    DiskEncryptionKey: Optional[Sequence["_DiskEncryptionKeyDefinition"]]
    SourceImageEncryptionKey: Optional[Sequence["_SourceImageEncryptionKeyDefinition"]]
    SourceSnapshotEncryptionKey: Optional[Sequence["_SourceSnapshotEncryptionKeyDefinition"]]
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
            Id=json_data.get("Id"),
            Image=json_data.get("Image"),
            Interface=json_data.get("Interface"),
            LabelFingerprint=json_data.get("LabelFingerprint"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            LastAttachTimestamp=json_data.get("LastAttachTimestamp"),
            LastDetachTimestamp=json_data.get("LastDetachTimestamp"),
            MultiWriter=json_data.get("MultiWriter"),
            Name=json_data.get("Name"),
            PhysicalBlockSizeBytes=json_data.get("PhysicalBlockSizeBytes"),
            Project=json_data.get("Project"),
            ProvisionedIops=json_data.get("ProvisionedIops"),
            ResourcePolicies=json_data.get("ResourcePolicies"),
            SelfLink=json_data.get("SelfLink"),
            Size=json_data.get("Size"),
            Snapshot=json_data.get("Snapshot"),
            SourceImageId=json_data.get("SourceImageId"),
            SourceSnapshotId=json_data.get("SourceSnapshotId"),
            Type=json_data.get("Type"),
            Users=json_data.get("Users"),
            Zone=json_data.get("Zone"),
            DiskEncryptionKey=deserialize_list(json_data.get("DiskEncryptionKey"), DiskEncryptionKeyDefinition),
            SourceImageEncryptionKey=deserialize_list(json_data.get("SourceImageEncryptionKey"), SourceImageEncryptionKeyDefinition),
            SourceSnapshotEncryptionKey=deserialize_list(json_data.get("SourceSnapshotEncryptionKey"), SourceSnapshotEncryptionKeyDefinition),
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
class DiskEncryptionKeyDefinition(BaseModel):
    KmsKeySelfLink: Optional[str]
    KmsKeyServiceAccount: Optional[str]
    RawKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskEncryptionKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskEncryptionKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeySelfLink=json_data.get("KmsKeySelfLink"),
            KmsKeyServiceAccount=json_data.get("KmsKeyServiceAccount"),
            RawKey=json_data.get("RawKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskEncryptionKeyDefinition = DiskEncryptionKeyDefinition


@dataclass
class SourceImageEncryptionKeyDefinition(BaseModel):
    KmsKeySelfLink: Optional[str]
    KmsKeyServiceAccount: Optional[str]
    RawKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceImageEncryptionKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceImageEncryptionKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeySelfLink=json_data.get("KmsKeySelfLink"),
            KmsKeyServiceAccount=json_data.get("KmsKeyServiceAccount"),
            RawKey=json_data.get("RawKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceImageEncryptionKeyDefinition = SourceImageEncryptionKeyDefinition


@dataclass
class SourceSnapshotEncryptionKeyDefinition(BaseModel):
    KmsKeySelfLink: Optional[str]
    KmsKeyServiceAccount: Optional[str]
    RawKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceSnapshotEncryptionKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceSnapshotEncryptionKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeySelfLink=json_data.get("KmsKeySelfLink"),
            KmsKeyServiceAccount=json_data.get("KmsKeyServiceAccount"),
            RawKey=json_data.get("RawKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceSnapshotEncryptionKeyDefinition = SourceSnapshotEncryptionKeyDefinition


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


