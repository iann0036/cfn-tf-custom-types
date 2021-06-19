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
    AssignPublicIp: Optional[bool]
    AvailabilityDomain: Optional[str]
    BackupDestination: Optional[str]
    BringYourOwnLicense: Optional[bool]
    Description: Optional[str]
    DesiredState: Optional[str]
    Edition: Optional[str]
    EnableAdminConsole: Optional[bool]
    ForceDelete: Optional[bool]
    Id: Optional[str]
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
    Backups: Optional[Sequence["_BackupsDefinition"]]
    LoadBalancer: Optional[Sequence["_LoadBalancerDefinition"]]
    OracleTrafficDirector: Optional[Sequence["_OracleTrafficDirectorDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    WeblogicServer: Optional[Sequence["_WeblogicServerDefinition"]]

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
            AssignPublicIp=json_data.get("AssignPublicIp"),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            BackupDestination=json_data.get("BackupDestination"),
            BringYourOwnLicense=json_data.get("BringYourOwnLicense"),
            Description=json_data.get("Description"),
            DesiredState=json_data.get("DesiredState"),
            Edition=json_data.get("Edition"),
            EnableAdminConsole=json_data.get("EnableAdminConsole"),
            ForceDelete=json_data.get("ForceDelete"),
            Id=json_data.get("Id"),
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
            Backups=deserialize_list(json_data.get("Backups"), BackupsDefinition),
            LoadBalancer=deserialize_list(json_data.get("LoadBalancer"), LoadBalancerDefinition),
            OracleTrafficDirector=deserialize_list(json_data.get("OracleTrafficDirector"), OracleTrafficDirectorDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            WeblogicServer=deserialize_list(json_data.get("WeblogicServer"), WeblogicServerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackupsDefinition(BaseModel):
    AutoGenerate: Optional[bool]
    CloudStorageContainer: Optional[str]
    CloudStoragePassword: Optional[str]
    CloudStorageUsername: Optional[str]
    UseOauthForStorage: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_BackupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupsDefinition"]:
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
_BackupsDefinition = BackupsDefinition


@dataclass
class LoadBalancerDefinition(BaseModel):
    LoadBalancingPolicy: Optional[str]
    Subnets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancerDefinition"]:
        if not json_data:
            return None
        return cls(
            LoadBalancingPolicy=json_data.get("LoadBalancingPolicy"),
            Subnets=json_data.get("Subnets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancerDefinition = LoadBalancerDefinition


@dataclass
class OracleTrafficDirectorDefinition(BaseModel):
    HighAvailability: Optional[bool]
    IpReservations: Optional[Sequence[str]]
    LoadBalancingPolicy: Optional[str]
    Shape: Optional[str]
    Admin: Optional[Sequence["_AdminDefinition"]]
    Listener: Optional[Sequence["_ListenerDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OracleTrafficDirectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OracleTrafficDirectorDefinition"]:
        if not json_data:
            return None
        return cls(
            HighAvailability=json_data.get("HighAvailability"),
            IpReservations=json_data.get("IpReservations"),
            LoadBalancingPolicy=json_data.get("LoadBalancingPolicy"),
            Shape=json_data.get("Shape"),
            Admin=deserialize_list(json_data.get("Admin"), AdminDefinition),
            Listener=deserialize_list(json_data.get("Listener"), ListenerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OracleTrafficDirectorDefinition = OracleTrafficDirectorDefinition


@dataclass
class AdminDefinition(BaseModel):
    Password: Optional[str]
    Port: Optional[float]
    SecuredPort: Optional[float]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdminDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdminDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecuredPort=json_data.get("SecuredPort"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdminDefinition = AdminDefinition


@dataclass
class ListenerDefinition(BaseModel):
    Port: Optional[float]
    PrivilegedPort: Optional[float]
    PrivilegedSecuredPort: Optional[float]
    SecuredPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ListenerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListenerDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            PrivilegedPort=json_data.get("PrivilegedPort"),
            PrivilegedSecuredPort=json_data.get("PrivilegedSecuredPort"),
            SecuredPort=json_data.get("SecuredPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListenerDefinition = ListenerDefinition


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


@dataclass
class WeblogicServerDefinition(BaseModel):
    BackupVolumeSize: Optional[str]
    ClusterName: Optional[str]
    ConnectString: Optional[str]
    IpReservations: Optional[Sequence[str]]
    MiddlewareVolumeSize: Optional[str]
    Shape: Optional[str]
    UpperStackProductName: Optional[str]
    Admin: Optional[Sequence["_AdminDefinition"]]
    ApplicationDatabase: Optional[Sequence["_ApplicationDatabaseDefinition"]]
    Cluster: Optional[Sequence["_ClusterDefinition"]]
    Database: Optional[Sequence["_DatabaseDefinition"]]
    Domain: Optional[Sequence["_DomainDefinition"]]
    ManagedServers: Optional[Sequence["_ManagedServersDefinition"]]
    NodeManager: Optional[Sequence["_NodeManagerDefinition"]]
    Ports: Optional[Sequence["_PortsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WeblogicServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeblogicServerDefinition"]:
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
            Admin=deserialize_list(json_data.get("Admin"), AdminDefinition),
            ApplicationDatabase=deserialize_list(json_data.get("ApplicationDatabase"), ApplicationDatabaseDefinition),
            Cluster=deserialize_list(json_data.get("Cluster"), ClusterDefinition),
            Database=deserialize_list(json_data.get("Database"), DatabaseDefinition),
            Domain=deserialize_list(json_data.get("Domain"), DomainDefinition),
            ManagedServers=deserialize_list(json_data.get("ManagedServers"), ManagedServersDefinition),
            NodeManager=deserialize_list(json_data.get("NodeManager"), NodeManagerDefinition),
            Ports=deserialize_list(json_data.get("Ports"), PortsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeblogicServerDefinition = WeblogicServerDefinition


@dataclass
class ApplicationDatabaseDefinition(BaseModel):
    Name: Optional[str]
    Password: Optional[str]
    PdbName: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationDatabaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationDatabaseDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            PdbName=json_data.get("PdbName"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationDatabaseDefinition = ApplicationDatabaseDefinition


@dataclass
class ClusterDefinition(BaseModel):
    Name: Optional[str]
    PathPrefixes: Optional[Sequence[str]]
    ServerCount: Optional[float]
    ServersPerNode: Optional[float]
    Shape: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterDefinition"]:
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
_ClusterDefinition = ClusterDefinition


@dataclass
class DatabaseDefinition(BaseModel):
    Name: Optional[str]
    Password: Optional[str]
    PdbName: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            PdbName=json_data.get("PdbName"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseDefinition = DatabaseDefinition


@dataclass
class DomainDefinition(BaseModel):
    Mode: Optional[str]
    Name: Optional[str]
    PartitionCount: Optional[float]
    VolumeSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainDefinition"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            PartitionCount=json_data.get("PartitionCount"),
            VolumeSize=json_data.get("VolumeSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainDefinition = DomainDefinition


@dataclass
class ManagedServersDefinition(BaseModel):
    InitialHeapSize: Optional[float]
    InitialPermanentGeneration: Optional[float]
    JvmArgs: Optional[str]
    MaxHeapSize: Optional[float]
    MaxPermanentGeneration: Optional[float]
    OverwriteJvmArgs: Optional[bool]
    ServerCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedServersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedServersDefinition"]:
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
_ManagedServersDefinition = ManagedServersDefinition


@dataclass
class NodeManagerDefinition(BaseModel):
    Password: Optional[str]
    Port: Optional[float]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeManagerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeManagerDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeManagerDefinition = NodeManagerDefinition


@dataclass
class PortsDefinition(BaseModel):
    ContentPort: Optional[float]
    DeploymentChannelPort: Optional[float]
    PrivilegedContentPort: Optional[float]
    PrivilegedSecuredContentPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortsDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentPort=json_data.get("ContentPort"),
            DeploymentChannelPort=json_data.get("DeploymentChannelPort"),
            PrivilegedContentPort=json_data.get("PrivilegedContentPort"),
            PrivilegedSecuredContentPort=json_data.get("PrivilegedSecuredContentPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortsDefinition = PortsDefinition


