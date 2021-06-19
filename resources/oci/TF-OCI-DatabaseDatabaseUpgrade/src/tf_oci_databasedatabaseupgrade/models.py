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
    Action: Optional[str]
    CharacterSet: Optional[str]
    CompartmentId: Optional[str]
    ConnectionStrings: Optional[Sequence["_ConnectionStringsDefinition2"]]
    DatabaseId: Optional[str]
    DatabaseSoftwareImageId: Optional[str]
    DbBackupConfig: Optional[Sequence["_DbBackupConfigDefinition2"]]
    DbHomeId: Optional[str]
    DbName: Optional[str]
    DbSystemId: Optional[str]
    DbUniqueName: Optional[str]
    DbWorkload: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    LastBackupTimestamp: Optional[str]
    LifecycleDetails: Optional[str]
    NcharacterSet: Optional[str]
    PdbName: Optional[str]
    SourceDatabasePointInTimeRecoveryTimestamp: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    VmClusterId: Optional[str]
    DatabaseUpgradeSourceDetails: Optional[Sequence["_DatabaseUpgradeSourceDetailsDefinition"]]
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
            Action=json_data.get("Action"),
            CharacterSet=json_data.get("CharacterSet"),
            CompartmentId=json_data.get("CompartmentId"),
            ConnectionStrings=deserialize_list(json_data.get("ConnectionStrings"), ConnectionStringsDefinition2),
            DatabaseId=json_data.get("DatabaseId"),
            DatabaseSoftwareImageId=json_data.get("DatabaseSoftwareImageId"),
            DbBackupConfig=deserialize_list(json_data.get("DbBackupConfig"), DbBackupConfigDefinition2),
            DbHomeId=json_data.get("DbHomeId"),
            DbName=json_data.get("DbName"),
            DbSystemId=json_data.get("DbSystemId"),
            DbUniqueName=json_data.get("DbUniqueName"),
            DbWorkload=json_data.get("DbWorkload"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            LastBackupTimestamp=json_data.get("LastBackupTimestamp"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            NcharacterSet=json_data.get("NcharacterSet"),
            PdbName=json_data.get("PdbName"),
            SourceDatabasePointInTimeRecoveryTimestamp=json_data.get("SourceDatabasePointInTimeRecoveryTimestamp"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            VmClusterId=json_data.get("VmClusterId"),
            DatabaseUpgradeSourceDetails=deserialize_list(json_data.get("DatabaseUpgradeSourceDetails"), DatabaseUpgradeSourceDetailsDefinition),
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
    Id: Optional[str]
    InternetProxy: Optional[str]
    Type: Optional[str]
    VpcPassword: Optional[str]
    VpcUser: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DbBackupConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbBackupConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            InternetProxy=json_data.get("InternetProxy"),
            Type=json_data.get("Type"),
            VpcPassword=json_data.get("VpcPassword"),
            VpcUser=json_data.get("VpcUser"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbBackupConfigDefinition = DbBackupConfigDefinition


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
class DatabaseUpgradeSourceDetailsDefinition(BaseModel):
    DatabaseSoftwareImageId: Optional[str]
    DbVersion: Optional[str]
    Options: Optional[str]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseUpgradeSourceDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseUpgradeSourceDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            DatabaseSoftwareImageId=json_data.get("DatabaseSoftwareImageId"),
            DbVersion=json_data.get("DbVersion"),
            Options=json_data.get("Options"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseUpgradeSourceDetailsDefinition = DatabaseUpgradeSourceDetailsDefinition


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


