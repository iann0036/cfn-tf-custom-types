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
    ConnectionName: Optional[str]
    DatabaseVersion: Optional[str]
    FirstIpAddress: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[Sequence["_IpAddress"]]
    MasterInstanceName: Optional[str]
    Name: Optional[str]
    PrivateIpAddress: Optional[str]
    Project: Optional[str]
    PublicIpAddress: Optional[str]
    Region: Optional[str]
    SelfLink: Optional[str]
    ServerCaCert: Optional[Sequence["_ServerCaCert"]]
    ServiceAccountEmailAddress: Optional[str]
    ReplicaConfiguration: Optional[Sequence["_ReplicaConfiguration"]]
    Settings: Optional[Sequence["_Settings"]]
    Timeouts: Optional["_Timeouts"]
    BackupConfiguration: Optional[Sequence["_BackupConfiguration"]]
    DatabaseFlags: Optional[Sequence["_DatabaseFlags"]]
    IpConfiguration: Optional[Sequence["_IpConfiguration"]]
    LocationPreference: Optional[Sequence["_LocationPreference"]]
    MaintenanceWindow: Optional[Sequence["_MaintenanceWindow"]]
    AuthorizedNetworks: Optional[Sequence["_AuthorizedNetworks"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ConnectionName=json_data.get("ConnectionName"),
            DatabaseVersion=json_data.get("DatabaseVersion"),
            FirstIpAddress=json_data.get("FirstIpAddress"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            MasterInstanceName=json_data.get("MasterInstanceName"),
            Name=json_data.get("Name"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            Project=json_data.get("Project"),
            PublicIpAddress=json_data.get("PublicIpAddress"),
            Region=json_data.get("Region"),
            SelfLink=json_data.get("SelfLink"),
            ServerCaCert=json_data.get("ServerCaCert"),
            ServiceAccountEmailAddress=json_data.get("ServiceAccountEmailAddress"),
            ReplicaConfiguration=json_data.get("ReplicaConfiguration"),
            Settings=json_data.get("Settings"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            BackupConfiguration=json_data.get("BackupConfiguration"),
            DatabaseFlags=json_data.get("DatabaseFlags"),
            IpConfiguration=json_data.get("IpConfiguration"),
            LocationPreference=json_data.get("LocationPreference"),
            MaintenanceWindow=json_data.get("MaintenanceWindow"),
            AuthorizedNetworks=json_data.get("AuthorizedNetworks"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IpAddress:
    IpAddress: Optional[str]
    TimeToRetire: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddress"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            TimeToRetire=json_data.get("TimeToRetire"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddress = IpAddress


@dataclass
class ServerCaCert:
    Cert: Optional[str]
    CommonName: Optional[str]
    CreateTime: Optional[str]
    ExpirationTime: Optional[str]
    Sha1Fingerprint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerCaCert"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerCaCert"]:
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
_ServerCaCert = ServerCaCert


@dataclass
class ReplicaConfiguration:
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
        cls: Type["_ReplicaConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicaConfiguration"]:
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
_ReplicaConfiguration = ReplicaConfiguration


@dataclass
class Settings:
    ActivationPolicy: Optional[str]
    AuthorizedGaeApplications: Optional[Sequence[str]]
    AvailabilityType: Optional[str]
    CrashSafeReplication: Optional[bool]
    DiskAutoresize: Optional[bool]
    DiskSize: Optional[float]
    DiskType: Optional[str]
    PricingPlan: Optional[str]
    ReplicationType: Optional[str]
    Tier: Optional[str]
    UserLabels: Optional[Sequence["_UserLabels"]]
    BackupConfiguration: Optional[Sequence["_BackupConfiguration"]]
    DatabaseFlags: Optional[Sequence["_DatabaseFlags"]]
    IpConfiguration: Optional[Sequence["_IpConfiguration"]]
    LocationPreference: Optional[Sequence["_LocationPreference"]]
    MaintenanceWindow: Optional[Sequence["_MaintenanceWindow"]]

    @classmethod
    def _deserialize(
        cls: Type["_Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Settings"]:
        if not json_data:
            return None
        return cls(
            ActivationPolicy=json_data.get("ActivationPolicy"),
            AuthorizedGaeApplications=json_data.get("AuthorizedGaeApplications"),
            AvailabilityType=json_data.get("AvailabilityType"),
            CrashSafeReplication=json_data.get("CrashSafeReplication"),
            DiskAutoresize=json_data.get("DiskAutoresize"),
            DiskSize=json_data.get("DiskSize"),
            DiskType=json_data.get("DiskType"),
            PricingPlan=json_data.get("PricingPlan"),
            ReplicationType=json_data.get("ReplicationType"),
            Tier=json_data.get("Tier"),
            UserLabels=json_data.get("UserLabels"),
            BackupConfiguration=json_data.get("BackupConfiguration"),
            DatabaseFlags=json_data.get("DatabaseFlags"),
            IpConfiguration=json_data.get("IpConfiguration"),
            LocationPreference=json_data.get("LocationPreference"),
            MaintenanceWindow=json_data.get("MaintenanceWindow"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Settings = Settings


@dataclass
class UserLabels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserLabels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserLabels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserLabels = UserLabels


@dataclass
class BackupConfiguration:
    BinaryLogEnabled: Optional[bool]
    Enabled: Optional[bool]
    Location: Optional[str]
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupConfiguration"]:
        if not json_data:
            return None
        return cls(
            BinaryLogEnabled=json_data.get("BinaryLogEnabled"),
            Enabled=json_data.get("Enabled"),
            Location=json_data.get("Location"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupConfiguration = BackupConfiguration


@dataclass
class DatabaseFlags:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseFlags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseFlags"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseFlags = DatabaseFlags


@dataclass
class IpConfiguration:
    Ipv4Enabled: Optional[bool]
    PrivateNetwork: Optional[str]
    RequireSsl: Optional[bool]
    AuthorizedNetworks: Optional[Sequence["_AuthorizedNetworks"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpConfiguration"]:
        if not json_data:
            return None
        return cls(
            Ipv4Enabled=json_data.get("Ipv4Enabled"),
            PrivateNetwork=json_data.get("PrivateNetwork"),
            RequireSsl=json_data.get("RequireSsl"),
            AuthorizedNetworks=json_data.get("AuthorizedNetworks"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpConfiguration = IpConfiguration


@dataclass
class AuthorizedNetworks:
    ExpirationTime: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthorizedNetworks"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthorizedNetworks"]:
        if not json_data:
            return None
        return cls(
            ExpirationTime=json_data.get("ExpirationTime"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthorizedNetworks = AuthorizedNetworks


@dataclass
class LocationPreference:
    FollowGaeApplication: Optional[str]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocationPreference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocationPreference"]:
        if not json_data:
            return None
        return cls(
            FollowGaeApplication=json_data.get("FollowGaeApplication"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocationPreference = LocationPreference


@dataclass
class MaintenanceWindow:
    Day: Optional[float]
    Hour: Optional[float]
    UpdateTrack: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindow"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            Hour=json_data.get("Hour"),
            UpdateTrack=json_data.get("UpdateTrack"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindow = MaintenanceWindow


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


