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
    AvailabilityDomain: Optional[str]
    BringYourOwnLicense: Optional[bool]
    CloudStorageContainer: Optional[str]
    ComputeSiteName: Optional[str]
    DbaasMonitorUrl: Optional[str]
    Description: Optional[str]
    DesiredState: Optional[str]
    Edition: Optional[str]
    EmUrl: Optional[str]
    GlassfishUrl: Optional[str]
    HighPerformanceStorage: Optional[bool]
    Id: Optional[str]
    IdentityDomain: Optional[str]
    IpNetwork: Optional[str]
    IpReservations: Optional[Sequence[str]]
    Level: Optional[str]
    Name: Optional[str]
    NotificationEmail: Optional[str]
    Region: Optional[str]
    Shape: Optional[str]
    SshPublicKey: Optional[str]
    Status: Optional[str]
    Subnet: Optional[str]
    SubscriptionType: Optional[str]
    Uri: Optional[str]
    Version: Optional[str]
    Backups: Optional[Sequence["_BackupsDefinition"]]
    DatabaseConfiguration: Optional[Sequence["_DatabaseConfigurationDefinition"]]
    DefaultAccessRules: Optional[Sequence["_DefaultAccessRulesDefinition"]]
    HybridDisasterRecovery: Optional[Sequence["_HybridDisasterRecoveryDefinition"]]
    InstantiateFromBackup: Optional[Sequence["_InstantiateFromBackupDefinition"]]
    Standby: Optional[Sequence["_StandbyDefinition"]]
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
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            BringYourOwnLicense=json_data.get("BringYourOwnLicense"),
            CloudStorageContainer=json_data.get("CloudStorageContainer"),
            ComputeSiteName=json_data.get("ComputeSiteName"),
            DbaasMonitorUrl=json_data.get("DbaasMonitorUrl"),
            Description=json_data.get("Description"),
            DesiredState=json_data.get("DesiredState"),
            Edition=json_data.get("Edition"),
            EmUrl=json_data.get("EmUrl"),
            GlassfishUrl=json_data.get("GlassfishUrl"),
            HighPerformanceStorage=json_data.get("HighPerformanceStorage"),
            Id=json_data.get("Id"),
            IdentityDomain=json_data.get("IdentityDomain"),
            IpNetwork=json_data.get("IpNetwork"),
            IpReservations=json_data.get("IpReservations"),
            Level=json_data.get("Level"),
            Name=json_data.get("Name"),
            NotificationEmail=json_data.get("NotificationEmail"),
            Region=json_data.get("Region"),
            Shape=json_data.get("Shape"),
            SshPublicKey=json_data.get("SshPublicKey"),
            Status=json_data.get("Status"),
            Subnet=json_data.get("Subnet"),
            SubscriptionType=json_data.get("SubscriptionType"),
            Uri=json_data.get("Uri"),
            Version=json_data.get("Version"),
            Backups=deserialize_list(json_data.get("Backups"), BackupsDefinition),
            DatabaseConfiguration=deserialize_list(json_data.get("DatabaseConfiguration"), DatabaseConfigurationDefinition),
            DefaultAccessRules=deserialize_list(json_data.get("DefaultAccessRules"), DefaultAccessRulesDefinition),
            HybridDisasterRecovery=deserialize_list(json_data.get("HybridDisasterRecovery"), HybridDisasterRecoveryDefinition),
            InstantiateFromBackup=deserialize_list(json_data.get("InstantiateFromBackup"), InstantiateFromBackupDefinition),
            Standby=deserialize_list(json_data.get("Standby"), StandbyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackupsDefinition(BaseModel):
    CloudStorageContainer: Optional[str]
    CloudStoragePassword: Optional[str]
    CloudStorageUsername: Optional[str]
    CreateIfMissing: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_BackupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupsDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudStorageContainer=json_data.get("CloudStorageContainer"),
            CloudStoragePassword=json_data.get("CloudStoragePassword"),
            CloudStorageUsername=json_data.get("CloudStorageUsername"),
            CreateIfMissing=json_data.get("CreateIfMissing"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupsDefinition = BackupsDefinition


@dataclass
class DatabaseConfigurationDefinition(BaseModel):
    AdminPassword: Optional[str]
    BackupDestination: Optional[str]
    BackupStorageVolumeSize: Optional[float]
    CharacterSet: Optional[str]
    DataStorageVolumeSize: Optional[float]
    DbDemo: Optional[str]
    DisasterRecovery: Optional[bool]
    FailoverDatabase: Optional[bool]
    GoldenGate: Optional[bool]
    IsRac: Optional[bool]
    NationalCharacterSet: Optional[str]
    PdbName: Optional[str]
    Sid: Optional[str]
    SnapshotName: Optional[str]
    SourceServiceName: Optional[str]
    Timezone: Optional[str]
    Type: Optional[str]
    UsableStorage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminPassword=json_data.get("AdminPassword"),
            BackupDestination=json_data.get("BackupDestination"),
            BackupStorageVolumeSize=json_data.get("BackupStorageVolumeSize"),
            CharacterSet=json_data.get("CharacterSet"),
            DataStorageVolumeSize=json_data.get("DataStorageVolumeSize"),
            DbDemo=json_data.get("DbDemo"),
            DisasterRecovery=json_data.get("DisasterRecovery"),
            FailoverDatabase=json_data.get("FailoverDatabase"),
            GoldenGate=json_data.get("GoldenGate"),
            IsRac=json_data.get("IsRac"),
            NationalCharacterSet=json_data.get("NationalCharacterSet"),
            PdbName=json_data.get("PdbName"),
            Sid=json_data.get("Sid"),
            SnapshotName=json_data.get("SnapshotName"),
            SourceServiceName=json_data.get("SourceServiceName"),
            Timezone=json_data.get("Timezone"),
            Type=json_data.get("Type"),
            UsableStorage=json_data.get("UsableStorage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseConfigurationDefinition = DatabaseConfigurationDefinition


@dataclass
class DefaultAccessRulesDefinition(BaseModel):
    EnableDbConsole: Optional[bool]
    EnableDbExpress: Optional[bool]
    EnableDbListener: Optional[bool]
    EnableEmConsole: Optional[bool]
    EnableHttp: Optional[bool]
    EnableHttpSsl: Optional[bool]
    EnableRacDbListener: Optional[bool]
    EnableRacOns: Optional[bool]
    EnableScanListener: Optional[bool]
    EnableSsh: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultAccessRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultAccessRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableDbConsole=json_data.get("EnableDbConsole"),
            EnableDbExpress=json_data.get("EnableDbExpress"),
            EnableDbListener=json_data.get("EnableDbListener"),
            EnableEmConsole=json_data.get("EnableEmConsole"),
            EnableHttp=json_data.get("EnableHttp"),
            EnableHttpSsl=json_data.get("EnableHttpSsl"),
            EnableRacDbListener=json_data.get("EnableRacDbListener"),
            EnableRacOns=json_data.get("EnableRacOns"),
            EnableScanListener=json_data.get("EnableScanListener"),
            EnableSsh=json_data.get("EnableSsh"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultAccessRulesDefinition = DefaultAccessRulesDefinition


@dataclass
class HybridDisasterRecoveryDefinition(BaseModel):
    CloudStorageContainer: Optional[str]
    CloudStoragePassword: Optional[str]
    CloudStorageUsername: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HybridDisasterRecoveryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HybridDisasterRecoveryDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudStorageContainer=json_data.get("CloudStorageContainer"),
            CloudStoragePassword=json_data.get("CloudStoragePassword"),
            CloudStorageUsername=json_data.get("CloudStorageUsername"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HybridDisasterRecoveryDefinition = HybridDisasterRecoveryDefinition


@dataclass
class InstantiateFromBackupDefinition(BaseModel):
    CloudStorageContainer: Optional[str]
    CloudStoragePassword: Optional[str]
    CloudStorageUsername: Optional[str]
    DatabaseId: Optional[str]
    DecryptionKey: Optional[str]
    OnPremise: Optional[bool]
    ServiceId: Optional[str]
    WalletFileContent: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstantiateFromBackupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstantiateFromBackupDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudStorageContainer=json_data.get("CloudStorageContainer"),
            CloudStoragePassword=json_data.get("CloudStoragePassword"),
            CloudStorageUsername=json_data.get("CloudStorageUsername"),
            DatabaseId=json_data.get("DatabaseId"),
            DecryptionKey=json_data.get("DecryptionKey"),
            OnPremise=json_data.get("OnPremise"),
            ServiceId=json_data.get("ServiceId"),
            WalletFileContent=json_data.get("WalletFileContent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstantiateFromBackupDefinition = InstantiateFromBackupDefinition


@dataclass
class StandbyDefinition(BaseModel):
    AvailabilityDomain: Optional[str]
    Subnet: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StandbyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StandbyDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            Subnet=json_data.get("Subnet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StandbyDefinition = StandbyDefinition


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


