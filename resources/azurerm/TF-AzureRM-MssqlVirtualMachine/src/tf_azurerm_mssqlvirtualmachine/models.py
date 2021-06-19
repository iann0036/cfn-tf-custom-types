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
    Id: Optional[str]
    RServicesEnabled: Optional[bool]
    SqlConnectivityPort: Optional[float]
    SqlConnectivityType: Optional[str]
    SqlConnectivityUpdatePassword: Optional[str]
    SqlConnectivityUpdateUsername: Optional[str]
    SqlLicenseType: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VirtualMachineId: Optional[str]
    AutoBackup: Optional[Sequence["_AutoBackupDefinition"]]
    AutoPatching: Optional[Sequence["_AutoPatchingDefinition"]]
    KeyVaultCredential: Optional[Sequence["_KeyVaultCredentialDefinition"]]
    StorageConfiguration: Optional[Sequence["_StorageConfigurationDefinition"]]
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
            Id=json_data.get("Id"),
            RServicesEnabled=json_data.get("RServicesEnabled"),
            SqlConnectivityPort=json_data.get("SqlConnectivityPort"),
            SqlConnectivityType=json_data.get("SqlConnectivityType"),
            SqlConnectivityUpdatePassword=json_data.get("SqlConnectivityUpdatePassword"),
            SqlConnectivityUpdateUsername=json_data.get("SqlConnectivityUpdateUsername"),
            SqlLicenseType=json_data.get("SqlLicenseType"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VirtualMachineId=json_data.get("VirtualMachineId"),
            AutoBackup=deserialize_list(json_data.get("AutoBackup"), AutoBackupDefinition),
            AutoPatching=deserialize_list(json_data.get("AutoPatching"), AutoPatchingDefinition),
            KeyVaultCredential=deserialize_list(json_data.get("KeyVaultCredential"), KeyVaultCredentialDefinition),
            StorageConfiguration=deserialize_list(json_data.get("StorageConfiguration"), StorageConfigurationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class AutoBackupDefinition(BaseModel):
    EncryptionEnabled: Optional[bool]
    EncryptionPassword: Optional[str]
    RetentionPeriodInDays: Optional[float]
    StorageAccountAccessKey: Optional[str]
    StorageBlobEndpoint: Optional[str]
    SystemDatabasesBackupEnabled: Optional[bool]
    ManualSchedule: Optional[Sequence["_ManualScheduleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoBackupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoBackupDefinition"]:
        if not json_data:
            return None
        return cls(
            EncryptionEnabled=json_data.get("EncryptionEnabled"),
            EncryptionPassword=json_data.get("EncryptionPassword"),
            RetentionPeriodInDays=json_data.get("RetentionPeriodInDays"),
            StorageAccountAccessKey=json_data.get("StorageAccountAccessKey"),
            StorageBlobEndpoint=json_data.get("StorageBlobEndpoint"),
            SystemDatabasesBackupEnabled=json_data.get("SystemDatabasesBackupEnabled"),
            ManualSchedule=deserialize_list(json_data.get("ManualSchedule"), ManualScheduleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoBackupDefinition = AutoBackupDefinition


@dataclass
class ManualScheduleDefinition(BaseModel):
    FullBackupFrequency: Optional[str]
    FullBackupStartHour: Optional[float]
    FullBackupWindowInHours: Optional[float]
    LogBackupFrequencyInMinutes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ManualScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManualScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            FullBackupFrequency=json_data.get("FullBackupFrequency"),
            FullBackupStartHour=json_data.get("FullBackupStartHour"),
            FullBackupWindowInHours=json_data.get("FullBackupWindowInHours"),
            LogBackupFrequencyInMinutes=json_data.get("LogBackupFrequencyInMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManualScheduleDefinition = ManualScheduleDefinition


@dataclass
class AutoPatchingDefinition(BaseModel):
    DayOfWeek: Optional[str]
    MaintenanceWindowDurationInMinutes: Optional[float]
    MaintenanceWindowStartingHour: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoPatchingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoPatchingDefinition"]:
        if not json_data:
            return None
        return cls(
            DayOfWeek=json_data.get("DayOfWeek"),
            MaintenanceWindowDurationInMinutes=json_data.get("MaintenanceWindowDurationInMinutes"),
            MaintenanceWindowStartingHour=json_data.get("MaintenanceWindowStartingHour"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoPatchingDefinition = AutoPatchingDefinition


@dataclass
class KeyVaultCredentialDefinition(BaseModel):
    KeyVaultUrl: Optional[str]
    Name: Optional[str]
    ServicePrincipalName: Optional[str]
    ServicePrincipalSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyVaultCredentialDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyVaultCredentialDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyVaultUrl=json_data.get("KeyVaultUrl"),
            Name=json_data.get("Name"),
            ServicePrincipalName=json_data.get("ServicePrincipalName"),
            ServicePrincipalSecret=json_data.get("ServicePrincipalSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyVaultCredentialDefinition = KeyVaultCredentialDefinition


@dataclass
class StorageConfigurationDefinition(BaseModel):
    DiskType: Optional[str]
    StorageWorkloadType: Optional[str]
    DataSettings: Optional[Sequence["_DataSettingsDefinition"]]
    LogSettings: Optional[Sequence["_LogSettingsDefinition"]]
    TempDbSettings: Optional[Sequence["_TempDbSettingsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StorageConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskType=json_data.get("DiskType"),
            StorageWorkloadType=json_data.get("StorageWorkloadType"),
            DataSettings=deserialize_list(json_data.get("DataSettings"), DataSettingsDefinition),
            LogSettings=deserialize_list(json_data.get("LogSettings"), LogSettingsDefinition),
            TempDbSettings=deserialize_list(json_data.get("TempDbSettings"), TempDbSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageConfigurationDefinition = StorageConfigurationDefinition


@dataclass
class DataSettingsDefinition(BaseModel):
    DefaultFilePath: Optional[str]
    Luns: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_DataSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultFilePath=json_data.get("DefaultFilePath"),
            Luns=json_data.get("Luns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSettingsDefinition = DataSettingsDefinition


@dataclass
class LogSettingsDefinition(BaseModel):
    DefaultFilePath: Optional[str]
    Luns: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_LogSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultFilePath=json_data.get("DefaultFilePath"),
            Luns=json_data.get("Luns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogSettingsDefinition = LogSettingsDefinition


@dataclass
class TempDbSettingsDefinition(BaseModel):
    DefaultFilePath: Optional[str]
    Luns: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_TempDbSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TempDbSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultFilePath=json_data.get("DefaultFilePath"),
            Luns=json_data.get("Luns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TempDbSettingsDefinition = TempDbSettingsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


