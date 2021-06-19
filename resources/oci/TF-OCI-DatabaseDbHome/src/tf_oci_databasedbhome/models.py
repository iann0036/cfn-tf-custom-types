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
    CompartmentId: Optional[str]
    DatabaseSoftwareImageId: Optional[str]
    DbHomeLocation: Optional[str]
    DbSystemId: Optional[str]
    DbVersion: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    IsDesupportedVersion: Optional[bool]
    KmsKeyId: Optional[str]
    KmsKeyVersionId: Optional[str]
    LastPatchHistoryEntryId: Optional[str]
    LifecycleDetails: Optional[str]
    Source: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    VmClusterId: Optional[str]
    Database: Optional[Sequence["_DatabaseDefinition"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            DatabaseSoftwareImageId=json_data.get("DatabaseSoftwareImageId"),
            DbHomeLocation=json_data.get("DbHomeLocation"),
            DbSystemId=json_data.get("DbSystemId"),
            DbVersion=json_data.get("DbVersion"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            IsDesupportedVersion=json_data.get("IsDesupportedVersion"),
            KmsKeyId=json_data.get("KmsKeyId"),
            KmsKeyVersionId=json_data.get("KmsKeyVersionId"),
            LastPatchHistoryEntryId=json_data.get("LastPatchHistoryEntryId"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Source=json_data.get("Source"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            VmClusterId=json_data.get("VmClusterId"),
            Database=deserialize_list(json_data.get("Database"), DatabaseDefinition),
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
class DatabaseDefinition(BaseModel):
    AdminPassword: Optional[str]
    BackupId: Optional[str]
    BackupTdePassword: Optional[str]
    CharacterSet: Optional[str]
    DatabaseId: Optional[str]
    DatabaseSoftwareImageId: Optional[str]
    DbName: Optional[str]
    DbWorkload: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition2"]]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition2"]]
    NcharacterSet: Optional[str]
    PdbName: Optional[str]
    TdeWalletPassword: Optional[str]
    TimeStampForPointInTimeRecovery: Optional[str]
    DbBackupConfig: Optional[Sequence["_DbBackupConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminPassword=json_data.get("AdminPassword"),
            BackupId=json_data.get("BackupId"),
            BackupTdePassword=json_data.get("BackupTdePassword"),
            CharacterSet=json_data.get("CharacterSet"),
            DatabaseId=json_data.get("DatabaseId"),
            DatabaseSoftwareImageId=json_data.get("DatabaseSoftwareImageId"),
            DbName=json_data.get("DbName"),
            DbWorkload=json_data.get("DbWorkload"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition2),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition2),
            NcharacterSet=json_data.get("NcharacterSet"),
            PdbName=json_data.get("PdbName"),
            TdeWalletPassword=json_data.get("TdeWalletPassword"),
            TimeStampForPointInTimeRecovery=json_data.get("TimeStampForPointInTimeRecovery"),
            DbBackupConfig=deserialize_list(json_data.get("DbBackupConfig"), DbBackupConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseDefinition = DatabaseDefinition


@dataclass
class DefinedTagsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition2 = DefinedTagsDefinition2


@dataclass
class FreeformTagsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition2 = FreeformTagsDefinition2


@dataclass
class DbBackupConfigDefinition(BaseModel):
    AutoBackupEnabled: Optional[bool]
    AutoBackupWindow: Optional[str]
    RecoveryWindowInDays: Optional[float]
    BackupDestinationDetails: Optional[Sequence["_BackupDestinationDetailsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DbBackupConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbBackupConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoBackupEnabled=json_data.get("AutoBackupEnabled"),
            AutoBackupWindow=json_data.get("AutoBackupWindow"),
            RecoveryWindowInDays=json_data.get("RecoveryWindowInDays"),
            BackupDestinationDetails=deserialize_list(json_data.get("BackupDestinationDetails"), BackupDestinationDetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbBackupConfigDefinition = DbBackupConfigDefinition


@dataclass
class BackupDestinationDetailsDefinition(BaseModel):
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupDestinationDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupDestinationDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupDestinationDetailsDefinition = BackupDestinationDetailsDefinition


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


