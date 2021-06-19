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
    AutoTunedVpusPerGb: Optional[str]
    AvailabilityDomain: Optional[str]
    BackupPolicyId: Optional[str]
    BlockVolumeReplicasDeletion: Optional[bool]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    IsAutoTuneEnabled: Optional[bool]
    IsHydrated: Optional[bool]
    KmsKeyId: Optional[str]
    SizeInGbs: Optional[str]
    SizeInMbs: Optional[str]
    State: Optional[str]
    SystemTags: Optional[Sequence["_SystemTagsDefinition"]]
    TimeCreated: Optional[str]
    VolumeBackupId: Optional[str]
    VolumeGroupId: Optional[str]
    VpusPerGb: Optional[str]
    BlockVolumeReplicas: Optional[Sequence["_BlockVolumeReplicasDefinition"]]
    SourceDetails: Optional[Sequence["_SourceDetailsDefinition"]]
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
            AutoTunedVpusPerGb=json_data.get("AutoTunedVpusPerGb"),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            BackupPolicyId=json_data.get("BackupPolicyId"),
            BlockVolumeReplicasDeletion=json_data.get("BlockVolumeReplicasDeletion"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            IsAutoTuneEnabled=json_data.get("IsAutoTuneEnabled"),
            IsHydrated=json_data.get("IsHydrated"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SizeInGbs=json_data.get("SizeInGbs"),
            SizeInMbs=json_data.get("SizeInMbs"),
            State=json_data.get("State"),
            SystemTags=deserialize_list(json_data.get("SystemTags"), SystemTagsDefinition),
            TimeCreated=json_data.get("TimeCreated"),
            VolumeBackupId=json_data.get("VolumeBackupId"),
            VolumeGroupId=json_data.get("VolumeGroupId"),
            VpusPerGb=json_data.get("VpusPerGb"),
            BlockVolumeReplicas=deserialize_list(json_data.get("BlockVolumeReplicas"), BlockVolumeReplicasDefinition),
            SourceDetails=deserialize_list(json_data.get("SourceDetails"), SourceDetailsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class SystemTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemTagsDefinition = SystemTagsDefinition


@dataclass
class BlockVolumeReplicasDefinition(BaseModel):
    AvailabilityDomain: Optional[str]
    DisplayName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlockVolumeReplicasDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockVolumeReplicasDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            DisplayName=json_data.get("DisplayName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockVolumeReplicasDefinition = BlockVolumeReplicasDefinition


@dataclass
class SourceDetailsDefinition(BaseModel):
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDetailsDefinition = SourceDetailsDefinition


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


