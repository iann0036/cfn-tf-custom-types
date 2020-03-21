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
    AssignPublicIp: Optional[bool]
    AvailabilityDomain: Optional[str]
    BackupDestination: Optional[str]
    BringYourOwnLicense: Optional[bool]
    Description: Optional[str]
    DesiredState: Optional[str]
    Edition: Optional[str]
    EnableAdminConsole: Optional[bool]
    ForceDelete: Optional[bool]
    IpNetwork: Optional[str]
    Level: Optional[str]
    MeteringFrequency: Optional[str]
    Name: Optional[str]
    NotificationEmail: Optional[str]
    Region: Optional[str]
    ServiceVersion: Optional[str]
    SnapshotName: Optional[str]
    SourceServiceName: Optional[str]
    SshPublicKey: Optional[str]
    Status: Optional[str]
    Subnet: Optional[str]
    UseIdentityService: Optional[bool]
    Backups: Optional[Sequence["_Backups"]]
    LoadBalancer: Optional[Sequence["_LoadBalancer"]]
    OracleTrafficDirector: Optional[Sequence["_OracleTrafficDirector"]]
    Timeouts: Optional["_Timeouts"]
    WeblogicServer: Optional[Sequence["_WeblogicServer"]]
    Admin: Optional[Sequence["_Admin"]]
    Listener: Optional[Sequence["_Listener"]]
    ApplicationDatabase: Optional[Sequence["_ApplicationDatabase"]]
    Cluster: Optional[Sequence["_Cluster"]]
    Database: Optional[Sequence["_Database"]]
    Domain: Optional[Sequence["_Domain"]]
    ManagedServers: Optional[Sequence["_ManagedServers"]]
    NodeManager: Optional[Sequence["_NodeManager"]]
    Ports: Optional[Sequence["_Ports"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AssignPublicIp=json_data.get("AssignPublicIp"),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            BackupDestination=json_data.get("BackupDestination"),
            BringYourOwnLicense=json_data.get("BringYourOwnLicense"),
            Description=json_data.get("Description"),
            DesiredState=json_data.get("DesiredState"),
            Edition=json_data.get("Edition"),
            EnableAdminConsole=json_data.get("EnableAdminConsole"),
            ForceDelete=json_data.get("ForceDelete"),
            IpNetwork=json_data.get("IpNetwork"),
            Level=json_data.get("Level"),
            MeteringFrequency=json_data.get("MeteringFrequency"),
            Name=json_data.get("Name"),
            NotificationEmail=json_data.get("NotificationEmail"),
            Region=json_data.get("Region"),
            ServiceVersion=json_data.get("ServiceVersion"),
            SnapshotName=json_data.get("SnapshotName"),
            SourceServiceName=json_data.get("SourceServiceName"),
            SshPublicKey=json_data.get("SshPublicKey"),
            Status=json_data.get("Status"),
            Subnet=json_data.get("Subnet"),
            UseIdentityService=json_data.get("UseIdentityService"),
            Backups=json_data.get("Backups"),
            LoadBalancer=json_data.get("LoadBalancer"),
            OracleTrafficDirector=json_data.get("OracleTrafficDirector"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            WeblogicServer=json_data.get("WeblogicServer"),
            Admin=json_data.get("Admin"),
            Listener=json_data.get("Listener"),
            ApplicationDatabase=json_data.get("ApplicationDatabase"),
            Cluster=json_data.get("Cluster"),
            Database=json_data.get("Database"),
            Domain=json_data.get("Domain"),
            ManagedServers=json_data.get("ManagedServers"),
            NodeManager=json_data.get("NodeManager"),
            Ports=json_data.get("Ports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Backups:
    AutoGenerate: Optional[bool]
    CloudStorageContainer: Optional[str]
    CloudStoragePassword: Optional[str]
    CloudStorageUsername: Optional[str]
    UseOauthForStorage: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Backups"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Backups"]:
        if not json_data:
            return None
        return cls(
            AutoGenerate=json_data.get("AutoGenerate"),
            CloudStorageContainer=json_data.get("CloudStorageContainer"),
            CloudStoragePassword=json_data.get("CloudStoragePassword"),
            CloudStorageUsername=json_data.get("CloudStorageUsername"),
            UseOauthForStorage=json_data.get("UseOauthForStorage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Backups = Backups


@dataclass
class LoadBalancer:
    LoadBalancingPolicy: Optional[str]
    Subnets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancer"]:
        if not json_data:
            return None
        return cls(
            LoadBalancingPolicy=json_data.get("LoadBalancingPolicy"),
            Subnets=json_data.get("Subnets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancer = LoadBalancer


@dataclass
class OracleTrafficDirector:
    HighAvailability: Optional[bool]
    IpReservations: Optional[Sequence[str]]
    LoadBalancingPolicy: Optional[str]
    Shape: Optional[str]
    Admin: Optional[Sequence["_Admin"]]
    Listener: Optional[Sequence["_Listener"]]

    @classmethod
    def _deserialize(
        cls: Type["_OracleTrafficDirector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OracleTrafficDirector"]:
        if not json_data:
            return None
        return cls(
            HighAvailability=json_data.get("HighAvailability"),
            IpReservations=json_data.get("IpReservations"),
            LoadBalancingPolicy=json_data.get("LoadBalancingPolicy"),
            Shape=json_data.get("Shape"),
            Admin=json_data.get("Admin"),
            Listener=json_data.get("Listener"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OracleTrafficDirector = OracleTrafficDirector


@dataclass
class Admin:
    Password: Optional[str]
    Port: Optional[float]
    SecuredPort: Optional[float]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Admin"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Admin"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecuredPort=json_data.get("SecuredPort"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Admin = Admin


@dataclass
class Listener:
    Port: Optional[float]
    PrivilegedPort: Optional[float]
    PrivilegedSecuredPort: Optional[float]
    SecuredPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Listener"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Listener"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            PrivilegedPort=json_data.get("PrivilegedPort"),
            PrivilegedSecuredPort=json_data.get("PrivilegedSecuredPort"),
            SecuredPort=json_data.get("SecuredPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Listener = Listener


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


@dataclass
class WeblogicServer:
    BackupVolumeSize: Optional[str]
    ClusterName: Optional[str]
    ConnectString: Optional[str]
    IpReservations: Optional[Sequence[str]]
    MiddlewareVolumeSize: Optional[str]
    Shape: Optional[str]
    UpperStackProductName: Optional[str]
    Admin: Optional[Sequence["_Admin"]]
    ApplicationDatabase: Optional[Sequence["_ApplicationDatabase"]]
    Cluster: Optional[Sequence["_Cluster"]]
    Database: Optional[Sequence["_Database"]]
    Domain: Optional[Sequence["_Domain"]]
    ManagedServers: Optional[Sequence["_ManagedServers"]]
    NodeManager: Optional[Sequence["_NodeManager"]]
    Ports: Optional[Sequence["_Ports"]]

    @classmethod
    def _deserialize(
        cls: Type["_WeblogicServer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeblogicServer"]:
        if not json_data:
            return None
        return cls(
            BackupVolumeSize=json_data.get("BackupVolumeSize"),
            ClusterName=json_data.get("ClusterName"),
            ConnectString=json_data.get("ConnectString"),
            IpReservations=json_data.get("IpReservations"),
            MiddlewareVolumeSize=json_data.get("MiddlewareVolumeSize"),
            Shape=json_data.get("Shape"),
            UpperStackProductName=json_data.get("UpperStackProductName"),
            Admin=json_data.get("Admin"),
            ApplicationDatabase=json_data.get("ApplicationDatabase"),
            Cluster=json_data.get("Cluster"),
            Database=json_data.get("Database"),
            Domain=json_data.get("Domain"),
            ManagedServers=json_data.get("ManagedServers"),
            NodeManager=json_data.get("NodeManager"),
            Ports=json_data.get("Ports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeblogicServer = WeblogicServer


@dataclass
class ApplicationDatabase:
    Name: Optional[str]
    Password: Optional[str]
    PdbName: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationDatabase"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationDatabase"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            PdbName=json_data.get("PdbName"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationDatabase = ApplicationDatabase


@dataclass
class Cluster:
    Name: Optional[str]
    PathPrefixes: Optional[Sequence[str]]
    ServerCount: Optional[float]
    ServersPerNode: Optional[float]
    Shape: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Cluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cluster"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PathPrefixes=json_data.get("PathPrefixes"),
            ServerCount=json_data.get("ServerCount"),
            ServersPerNode=json_data.get("ServersPerNode"),
            Shape=json_data.get("Shape"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cluster = Cluster


@dataclass
class Database:
    Name: Optional[str]
    Password: Optional[str]
    PdbName: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Database"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Database"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            PdbName=json_data.get("PdbName"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Database = Database


@dataclass
class Domain:
    Mode: Optional[str]
    Name: Optional[str]
    PartitionCount: Optional[float]
    VolumeSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Domain"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Domain"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            PartitionCount=json_data.get("PartitionCount"),
            VolumeSize=json_data.get("VolumeSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Domain = Domain


@dataclass
class ManagedServers:
    InitialHeapSize: Optional[float]
    InitialPermanentGeneration: Optional[float]
    JvmArgs: Optional[str]
    MaxHeapSize: Optional[float]
    MaxPermanentGeneration: Optional[float]
    OverwriteJvmArgs: Optional[bool]
    ServerCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedServers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedServers"]:
        if not json_data:
            return None
        return cls(
            InitialHeapSize=json_data.get("InitialHeapSize"),
            InitialPermanentGeneration=json_data.get("InitialPermanentGeneration"),
            JvmArgs=json_data.get("JvmArgs"),
            MaxHeapSize=json_data.get("MaxHeapSize"),
            MaxPermanentGeneration=json_data.get("MaxPermanentGeneration"),
            OverwriteJvmArgs=json_data.get("OverwriteJvmArgs"),
            ServerCount=json_data.get("ServerCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedServers = ManagedServers


@dataclass
class NodeManager:
    Password: Optional[str]
    Port: Optional[float]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeManager"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeManager"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeManager = NodeManager


@dataclass
class Ports:
    ContentPort: Optional[float]
    DeploymentChannelPort: Optional[float]
    PrivilegedContentPort: Optional[float]
    PrivilegedSecuredContentPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Ports"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ports"]:
        if not json_data:
            return None
        return cls(
            ContentPort=json_data.get("ContentPort"),
            DeploymentChannelPort=json_data.get("DeploymentChannelPort"),
            PrivilegedContentPort=json_data.get("PrivilegedContentPort"),
            PrivilegedSecuredContentPort=json_data.get("PrivilegedSecuredContentPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ports = Ports


