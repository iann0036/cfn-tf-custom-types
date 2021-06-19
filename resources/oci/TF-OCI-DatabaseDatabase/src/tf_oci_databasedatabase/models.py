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
    CharacterSet: Optional[str]
    CompartmentId: Optional[str]
    ConnectionStrings: Optional[Sequence["_ConnectionStringsDefinition2"]]
    DatabaseSoftwareImageId: Optional[str]
    DbBackupConfig: Optional[Sequence["_DbBackupConfigDefinition2"]]
    DbHomeId: Optional[str]
    DbName: Optional[str]
    DbSystemId: Optional[str]
    DbUniqueName: Optional[str]
    DbVersion: Optional[str]
    DbWorkload: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    KmsKeyMigration: Optional[bool]
    KmsKeyRotation: Optional[float]
    KmsKeyVersionId: Optional[str]
    LastBackupTimestamp: Optional[str]
    LifecycleDetails: Optional[str]
    NcharacterSet: Optional[str]
    PdbName: Optional[str]
    Source: Optional[str]
    SourceDatabasePointInTimeRecoveryTimestamp: Optional[str]
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
            CharacterSet=json_data.get("CharacterSet"),
            CompartmentId=json_data.get("CompartmentId"),
            ConnectionStrings=deserialize_list(json_data.get("ConnectionStrings"), ConnectionStringsDefinition2),
            DatabaseSoftwareImageId=json_data.get("DatabaseSoftwareImageId"),
            DbBackupConfig=deserialize_list(json_data.get("DbBackupConfig"), DbBackupConfigDefinition2),
            DbHomeId=json_data.get("DbHomeId"),
            DbName=json_data.get("DbName"),
            DbSystemId=json_data.get("DbSystemId"),
            DbUniqueName=json_data.get("DbUniqueName"),
            DbVersion=json_data.get("DbVersion"),
            DbWorkload=json_data.get("DbWorkload"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            KmsKeyMigration=json_data.get("KmsKeyMigration"),
            KmsKeyRotation=json_data.get("KmsKeyRotation"),
            KmsKeyVersionId=json_data.get("KmsKeyVersionId"),
            LastBackupTimestamp=json_data.get("LastBackupTimestamp"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            NcharacterSet=json_data.get("NcharacterSet"),
            PdbName=json_data.get("PdbName"),
            Source=json_data.get("Source"),
            SourceDatabasePointInTimeRecoveryTimestamp=json_data.get("SourceDatabasePointInTimeRecoveryTimestamp"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            VmClusterId=json_data.get("VmClusterId"),
            Database=deserialize_list(json_data.get("Database"), DatabaseDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConnectionStringsDefinition2(BaseModel):
    AllConnectionStrings: Optional[Sequence["_ConnectionStringsDefinition"]]
    CdbDefault: Optional[str]
    CdbIpDefault: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionStringsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionStringsDefinition2"]:
        if not json_data:
            return None
        return cls(
            AllConnectionStrings=deserialize_list(json_data.get("AllConnectionStrings"), ConnectionStringsDefinition),
            CdbDefault=json_data.get("CdbDefault"),
            CdbIpDefault=json_data.get("CdbIpDefault"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionStringsDefinition2 = ConnectionStringsDefinition2


@dataclass
class ConnectionStringsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionStringsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionStringsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionStringsDefinition = ConnectionStringsDefinition


@dataclass
class DbBackupConfigDefinition2(BaseModel):
    AutoBackupEnabled: Optional[bool]
    AutoBackupWindow: Optional[str]
    BackupDestinationDetails: Optional[Sequence["_DbBackupConfigDefinition"]]
    RecoveryWindowInDays: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DbBackupConfigDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbBackupConfigDefinition2"]:
        if not json_data:
            return None
        return cls(
            AutoBackupEnabled=json_data.get("AutoBackupEnabled"),
            AutoBackupWindow=json_data.get("AutoBackupWindow"),
            BackupDestinationDetails=deserialize_list(json_data.get("BackupDestinationDetails"), DbBackupConfigDefinition),
            RecoveryWindowInDays=json_data.get("RecoveryWindowInDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbBackupConfigDefinition2 = DbBackupConfigDefinition2


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
    DatabaseSoftwareImageId: Optional[str]
    DbName: Optional[str]
    DbUniqueName: Optional[str]
    DbWorkload: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition2"]]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition2"]]
    NcharacterSet: Optional[str]
    PdbName: Optional[str]
    TdeWalletPassword: Optional[str]
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
            DatabaseSoftwareImageId=json_data.get("DatabaseSoftwareImageId"),
            DbName=json_data.get("DbName"),
            DbUniqueName=json_data.get("DbUniqueName"),
            DbWorkload=json_data.get("DbWorkload"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition2),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition2),
            NcharacterSet=json_data.get("NcharacterSet"),
            PdbName=json_data.get("PdbName"),
            TdeWalletPassword=json_data.get("TdeWalletPassword"),
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


