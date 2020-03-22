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
    CompartmentId: Optional[str]
    DbHomeLocation: Optional[str]
    DbSystemId: Optional[str]
    DbVersion: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    LastPatchHistoryEntryId: Optional[str]
    LifecycleDetails: Optional[str]
    Source: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    VmClusterId: Optional[str]
    Database: Optional[Sequence["_Database"]]
    Timeouts: Optional["_Timeouts"]
    DbBackupConfig: Optional[Sequence["_DbBackupConfig"]]
    BackupDestinationDetails: Optional[Sequence["_BackupDestinationDetails"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CompartmentId=json_data.get("CompartmentId"),
            DbHomeLocation=json_data.get("DbHomeLocation"),
            DbSystemId=json_data.get("DbSystemId"),
            DbVersion=json_data.get("DbVersion"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            LastPatchHistoryEntryId=json_data.get("LastPatchHistoryEntryId"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Source=json_data.get("Source"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            VmClusterId=json_data.get("VmClusterId"),
            Database=json_data.get("Database"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            DbBackupConfig=json_data.get("DbBackupConfig"),
            BackupDestinationDetails=json_data.get("BackupDestinationDetails"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Database:
    AdminPassword: Optional[str]
    BackupId: Optional[str]
    BackupTdePassword: Optional[str]
    CharacterSet: Optional[str]
    DbName: Optional[str]
    DbWorkload: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    NcharacterSet: Optional[str]
    PdbName: Optional[str]
    DbBackupConfig: Optional[Sequence["_DbBackupConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_Database"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Database"]:
        if not json_data:
            return None
        return cls(
            AdminPassword=json_data.get("AdminPassword"),
            BackupId=json_data.get("BackupId"),
            BackupTdePassword=json_data.get("BackupTdePassword"),
            CharacterSet=json_data.get("CharacterSet"),
            DbName=json_data.get("DbName"),
            DbWorkload=json_data.get("DbWorkload"),
            DefinedTags=json_data.get("DefinedTags"),
            FreeformTags=json_data.get("FreeformTags"),
            NcharacterSet=json_data.get("NcharacterSet"),
            PdbName=json_data.get("PdbName"),
            DbBackupConfig=json_data.get("DbBackupConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Database = Database


@dataclass
class DefinedTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class DbBackupConfig:
    AutoBackupEnabled: Optional[bool]
    AutoBackupWindow: Optional[str]
    RecoveryWindowInDays: Optional[float]
    BackupDestinationDetails: Optional[Sequence["_BackupDestinationDetails"]]

    @classmethod
    def _deserialize(
        cls: Type["_DbBackupConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbBackupConfig"]:
        if not json_data:
            return None
        return cls(
            AutoBackupEnabled=json_data.get("AutoBackupEnabled"),
            AutoBackupWindow=json_data.get("AutoBackupWindow"),
            RecoveryWindowInDays=json_data.get("RecoveryWindowInDays"),
            BackupDestinationDetails=json_data.get("BackupDestinationDetails"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbBackupConfig = DbBackupConfig


@dataclass
class BackupDestinationDetails:
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupDestinationDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupDestinationDetails"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupDestinationDetails = BackupDestinationDetails


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


