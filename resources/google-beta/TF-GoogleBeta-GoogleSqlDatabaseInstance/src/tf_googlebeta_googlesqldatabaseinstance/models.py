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
    ConnectionName: Optional[str]
    DatabaseVersion: Optional[str]
    DeletionProtection: Optional[bool]
    EncryptionKeyName: Optional[str]
    FirstIpAddress: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[Sequence["_IpAddressDefinition"]]
    MasterInstanceName: Optional[str]
    Name: Optional[str]
    PrivateIpAddress: Optional[str]
    Project: Optional[str]
    PublicIpAddress: Optional[str]
    Region: Optional[str]
    RootPassword: Optional[str]
    SelfLink: Optional[str]
    ServerCaCert: Optional[Sequence["_ServerCaCertDefinition"]]
    ServiceAccountEmailAddress: Optional[str]
    Clone: Optional[Sequence["_CloneDefinition"]]
    ReplicaConfiguration: Optional[Sequence["_ReplicaConfigurationDefinition"]]
    RestoreBackupContext: Optional[Sequence["_RestoreBackupContextDefinition"]]
    Settings: Optional[Sequence["_SettingsDefinition"]]
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
            ConnectionName=json_data.get("ConnectionName"),
            DatabaseVersion=json_data.get("DatabaseVersion"),
            DeletionProtection=json_data.get("DeletionProtection"),
            EncryptionKeyName=json_data.get("EncryptionKeyName"),
            FirstIpAddress=json_data.get("FirstIpAddress"),
            Id=json_data.get("Id"),
            IpAddress=deserialize_list(json_data.get("IpAddress"), IpAddressDefinition),
            MasterInstanceName=json_data.get("MasterInstanceName"),
            Name=json_data.get("Name"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            Project=json_data.get("Project"),
            PublicIpAddress=json_data.get("PublicIpAddress"),
            Region=json_data.get("Region"),
            RootPassword=json_data.get("RootPassword"),
            SelfLink=json_data.get("SelfLink"),
            ServerCaCert=deserialize_list(json_data.get("ServerCaCert"), ServerCaCertDefinition),
            ServiceAccountEmailAddress=json_data.get("ServiceAccountEmailAddress"),
            Clone=deserialize_list(json_data.get("Clone"), CloneDefinition),
            ReplicaConfiguration=deserialize_list(json_data.get("ReplicaConfiguration"), ReplicaConfigurationDefinition),
            RestoreBackupContext=deserialize_list(json_data.get("RestoreBackupContext"), RestoreBackupContextDefinition),
            Settings=deserialize_list(json_data.get("Settings"), SettingsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IpAddressDefinition(BaseModel):
    IpAddress: Optional[str]
    TimeToRetire: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            TimeToRetire=json_data.get("TimeToRetire"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddressDefinition = IpAddressDefinition


@dataclass
class ServerCaCertDefinition(BaseModel):
    Cert: Optional[str]
    CommonName: Optional[str]
    CreateTime: Optional[str]
    ExpirationTime: Optional[str]
    Sha1Fingerprint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerCaCertDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerCaCertDefinition"]:
        if not json_data:
            return None
        return cls(
            Cert=json_data.get("Cert"),
            CommonName=json_data.get("CommonName"),
            CreateTime=json_data.get("CreateTime"),
            ExpirationTime=json_data.get("ExpirationTime"),
            Sha1Fingerprint=json_data.get("Sha1Fingerprint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerCaCertDefinition = ServerCaCertDefinition


@dataclass
class CloneDefinition(BaseModel):
    PointInTime: Optional[str]
    SourceInstanceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloneDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloneDefinition"]:
        if not json_data:
            return None
        return cls(
            PointInTime=json_data.get("PointInTime"),
            SourceInstanceName=json_data.get("SourceInstanceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloneDefinition = CloneDefinition


@dataclass
class ReplicaConfigurationDefinition(BaseModel):
    CaCertificate: Optional[str]
    ClientCertificate: Optional[str]
    ClientKey: Optional[str]
    ConnectRetryInterval: Optional[float]
    DumpFilePath: Optional[str]
    FailoverTarget: Optional[bool]
    MasterHeartbeatPeriod: Optional[float]
    Password: Optional[str]
    SslCipher: Optional[str]
    Username: Optional[str]
    VerifyServerCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicaConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicaConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            CaCertificate=json_data.get("CaCertificate"),
            ClientCertificate=json_data.get("ClientCertificate"),
            ClientKey=json_data.get("ClientKey"),
            ConnectRetryInterval=json_data.get("ConnectRetryInterval"),
            DumpFilePath=json_data.get("DumpFilePath"),
            FailoverTarget=json_data.get("FailoverTarget"),
            MasterHeartbeatPeriod=json_data.get("MasterHeartbeatPeriod"),
            Password=json_data.get("Password"),
            SslCipher=json_data.get("SslCipher"),
            Username=json_data.get("Username"),
            VerifyServerCertificate=json_data.get("VerifyServerCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicaConfigurationDefinition = ReplicaConfigurationDefinition


@dataclass
class RestoreBackupContextDefinition(BaseModel):
    BackupRunId: Optional[float]
    InstanceId: Optional[str]
    Project: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RestoreBackupContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestoreBackupContextDefinition"]:
        if not json_data:
            return None
        return cls(
            BackupRunId=json_data.get("BackupRunId"),
            InstanceId=json_data.get("InstanceId"),
            Project=json_data.get("Project"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestoreBackupContextDefinition = RestoreBackupContextDefinition


@dataclass
class SettingsDefinition(BaseModel):
    ActivationPolicy: Optional[str]
    AuthorizedGaeApplications: Optional[Sequence[str]]
    AvailabilityType: Optional[str]
    CrashSafeReplication: Optional[bool]
    DiskAutoresize: Optional[bool]
    DiskAutoresizeLimit: Optional[float]
    DiskSize: Optional[float]
    DiskType: Optional[str]
    PricingPlan: Optional[str]
    ReplicationType: Optional[str]
    Tier: Optional[str]
    UserLabels: Optional[Sequence["_UserLabelsDefinition"]]
    BackupConfiguration: Optional[Sequence["_BackupConfigurationDefinition"]]
    DatabaseFlags: Optional[Sequence["_DatabaseFlagsDefinition"]]
    InsightsConfig: Optional[Sequence["_InsightsConfigDefinition"]]
    IpConfiguration: Optional[Sequence["_IpConfigurationDefinition"]]
    LocationPreference: Optional[Sequence["_LocationPreferenceDefinition"]]
    MaintenanceWindow: Optional[Sequence["_MaintenanceWindowDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            ActivationPolicy=json_data.get("ActivationPolicy"),
            AuthorizedGaeApplications=json_data.get("AuthorizedGaeApplications"),
            AvailabilityType=json_data.get("AvailabilityType"),
            CrashSafeReplication=json_data.get("CrashSafeReplication"),
            DiskAutoresize=json_data.get("DiskAutoresize"),
            DiskAutoresizeLimit=json_data.get("DiskAutoresizeLimit"),
            DiskSize=json_data.get("DiskSize"),
            DiskType=json_data.get("DiskType"),
            PricingPlan=json_data.get("PricingPlan"),
            ReplicationType=json_data.get("ReplicationType"),
            Tier=json_data.get("Tier"),
            UserLabels=deserialize_list(json_data.get("UserLabels"), UserLabelsDefinition),
            BackupConfiguration=deserialize_list(json_data.get("BackupConfiguration"), BackupConfigurationDefinition),
            DatabaseFlags=deserialize_list(json_data.get("DatabaseFlags"), DatabaseFlagsDefinition),
            InsightsConfig=deserialize_list(json_data.get("InsightsConfig"), InsightsConfigDefinition),
            IpConfiguration=deserialize_list(json_data.get("IpConfiguration"), IpConfigurationDefinition),
            LocationPreference=deserialize_list(json_data.get("LocationPreference"), LocationPreferenceDefinition),
            MaintenanceWindow=deserialize_list(json_data.get("MaintenanceWindow"), MaintenanceWindowDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SettingsDefinition = SettingsDefinition


@dataclass
class UserLabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserLabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserLabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserLabelsDefinition = UserLabelsDefinition


@dataclass
class BackupConfigurationDefinition(BaseModel):
    BinaryLogEnabled: Optional[bool]
    Enabled: Optional[bool]
    Location: Optional[str]
    PointInTimeRecoveryEnabled: Optional[bool]
    StartTime: Optional[str]
    TransactionLogRetentionDays: Optional[float]
    BackupRetentionSettings: Optional[Sequence["_BackupRetentionSettingsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BackupConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            BinaryLogEnabled=json_data.get("BinaryLogEnabled"),
            Enabled=json_data.get("Enabled"),
            Location=json_data.get("Location"),
            PointInTimeRecoveryEnabled=json_data.get("PointInTimeRecoveryEnabled"),
            StartTime=json_data.get("StartTime"),
            TransactionLogRetentionDays=json_data.get("TransactionLogRetentionDays"),
            BackupRetentionSettings=deserialize_list(json_data.get("BackupRetentionSettings"), BackupRetentionSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupConfigurationDefinition = BackupConfigurationDefinition


@dataclass
class BackupRetentionSettingsDefinition(BaseModel):
    RetainedBackups: Optional[float]
    RetentionUnit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupRetentionSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupRetentionSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            RetainedBackups=json_data.get("RetainedBackups"),
            RetentionUnit=json_data.get("RetentionUnit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupRetentionSettingsDefinition = BackupRetentionSettingsDefinition


@dataclass
class DatabaseFlagsDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseFlagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseFlagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseFlagsDefinition = DatabaseFlagsDefinition


@dataclass
class InsightsConfigDefinition(BaseModel):
    QueryInsightsEnabled: Optional[bool]
    QueryStringLength: Optional[float]
    RecordApplicationTags: Optional[bool]
    RecordClientAddress: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_InsightsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InsightsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            QueryInsightsEnabled=json_data.get("QueryInsightsEnabled"),
            QueryStringLength=json_data.get("QueryStringLength"),
            RecordApplicationTags=json_data.get("RecordApplicationTags"),
            RecordClientAddress=json_data.get("RecordClientAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InsightsConfigDefinition = InsightsConfigDefinition


@dataclass
class IpConfigurationDefinition(BaseModel):
    Ipv4Enabled: Optional[bool]
    PrivateNetwork: Optional[str]
    RequireSsl: Optional[bool]
    AuthorizedNetworks: Optional[Sequence["_AuthorizedNetworksDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4Enabled=json_data.get("Ipv4Enabled"),
            PrivateNetwork=json_data.get("PrivateNetwork"),
            RequireSsl=json_data.get("RequireSsl"),
            AuthorizedNetworks=deserialize_list(json_data.get("AuthorizedNetworks"), AuthorizedNetworksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpConfigurationDefinition = IpConfigurationDefinition


@dataclass
class AuthorizedNetworksDefinition(BaseModel):
    ExpirationTime: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthorizedNetworksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthorizedNetworksDefinition"]:
        if not json_data:
            return None
        return cls(
            ExpirationTime=json_data.get("ExpirationTime"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthorizedNetworksDefinition = AuthorizedNetworksDefinition


@dataclass
class LocationPreferenceDefinition(BaseModel):
    FollowGaeApplication: Optional[str]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocationPreferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocationPreferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            FollowGaeApplication=json_data.get("FollowGaeApplication"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocationPreferenceDefinition = LocationPreferenceDefinition


@dataclass
class MaintenanceWindowDefinition(BaseModel):
    Day: Optional[float]
    Hour: Optional[float]
    UpdateTrack: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowDefinition"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            Hour=json_data.get("Hour"),
            UpdateTrack=json_data.get("UpdateTrack"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowDefinition = MaintenanceWindowDefinition


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


