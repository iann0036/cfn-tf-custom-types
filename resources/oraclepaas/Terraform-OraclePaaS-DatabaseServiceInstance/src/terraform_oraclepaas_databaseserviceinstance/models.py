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
    Backups: Optional[Sequence["_Backups"]]
    DatabaseConfiguration: Optional[Sequence["_DatabaseConfiguration"]]
    DefaultAccessRules: Optional[Sequence["_DefaultAccessRules"]]
    HybridDisasterRecovery: Optional[Sequence["_HybridDisasterRecovery"]]
    InstantiateFromBackup: Optional[Sequence["_InstantiateFromBackup"]]
    Standby: Optional[Sequence["_Standby"]]
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
            Backups=json_data.get("Backups"),
            DatabaseConfiguration=json_data.get("DatabaseConfiguration"),
            DefaultAccessRules=json_data.get("DefaultAccessRules"),
            HybridDisasterRecovery=json_data.get("HybridDisasterRecovery"),
            InstantiateFromBackup=json_data.get("InstantiateFromBackup"),
            Standby=json_data.get("Standby"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Backups:
    CloudStorageContainer: Optional[str]
    CloudStoragePassword: Optional[str]
    CloudStorageUsername: Optional[str]
    CreateIfMissing: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Backups"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Backups"]:
        if not json_data:
            return None
        return cls(
            CloudStorageContainer=json_data.get("CloudStorageContainer"),
            CloudStoragePassword=json_data.get("CloudStoragePassword"),
            CloudStorageUsername=json_data.get("CloudStorageUsername"),
            CreateIfMissing=json_data.get("CreateIfMissing"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Backups = Backups


@dataclass
class DatabaseConfiguration:
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
        cls: Type["_DatabaseConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseConfiguration"]:
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
_DatabaseConfiguration = DatabaseConfiguration


@dataclass
class DefaultAccessRules:
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
        cls: Type["_DefaultAccessRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultAccessRules"]:
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
_DefaultAccessRules = DefaultAccessRules


@dataclass
class HybridDisasterRecovery:
    CloudStorageContainer: Optional[str]
    CloudStoragePassword: Optional[str]
    CloudStorageUsername: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HybridDisasterRecovery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HybridDisasterRecovery"]:
        if not json_data:
            return None
        return cls(
            CloudStorageContainer=json_data.get("CloudStorageContainer"),
            CloudStoragePassword=json_data.get("CloudStoragePassword"),
            CloudStorageUsername=json_data.get("CloudStorageUsername"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HybridDisasterRecovery = HybridDisasterRecovery


@dataclass
class InstantiateFromBackup:
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
        cls: Type["_InstantiateFromBackup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstantiateFromBackup"]:
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
_InstantiateFromBackup = InstantiateFromBackup


@dataclass
class Standby:
    AvailabilityDomain: Optional[str]
    Subnet: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Standby"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Standby"]:
        if not json_data:
            return None
        return cls(
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            Subnet=json_data.get("Subnet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Standby = Standby


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


