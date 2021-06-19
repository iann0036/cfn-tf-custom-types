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
    ClusterVersion: Optional[str]
    HttpsEndpoint: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    SshEndpoint: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Tier: Optional[str]
    TlsMinVersion: Optional[str]
    ComponentVersion: Optional[Sequence["_ComponentVersionDefinition"]]
    Gateway: Optional[Sequence["_GatewayDefinition"]]
    Metastores: Optional[Sequence["_MetastoresDefinition"]]
    Monitor: Optional[Sequence["_MonitorDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
    Roles: Optional[Sequence["_RolesDefinition"]]
    StorageAccount: Optional[Sequence["_StorageAccountDefinition"]]
    StorageAccountGen2: Optional[Sequence["_StorageAccountGen2Definition"]]
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
            ClusterVersion=json_data.get("ClusterVersion"),
            HttpsEndpoint=json_data.get("HttpsEndpoint"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SshEndpoint=json_data.get("SshEndpoint"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Tier=json_data.get("Tier"),
            TlsMinVersion=json_data.get("TlsMinVersion"),
            ComponentVersion=deserialize_list(json_data.get("ComponentVersion"), ComponentVersionDefinition),
            Gateway=deserialize_list(json_data.get("Gateway"), GatewayDefinition),
            Metastores=deserialize_list(json_data.get("Metastores"), MetastoresDefinition),
            Monitor=deserialize_list(json_data.get("Monitor"), MonitorDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            Roles=deserialize_list(json_data.get("Roles"), RolesDefinition),
            StorageAccount=deserialize_list(json_data.get("StorageAccount"), StorageAccountDefinition),
            StorageAccountGen2=deserialize_list(json_data.get("StorageAccountGen2"), StorageAccountGen2Definition),
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
class ComponentVersionDefinition(BaseModel):
    Hadoop: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentVersionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentVersionDefinition"]:
        if not json_data:
            return None
        return cls(
            Hadoop=json_data.get("Hadoop"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentVersionDefinition = ComponentVersionDefinition


@dataclass
class GatewayDefinition(BaseModel):
    Enabled: Optional[bool]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayDefinition = GatewayDefinition


@dataclass
class MetastoresDefinition(BaseModel):
    Ambari: Optional[Sequence["_AmbariDefinition"]]
    Hive: Optional[Sequence["_HiveDefinition"]]
    Oozie: Optional[Sequence["_OozieDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetastoresDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetastoresDefinition"]:
        if not json_data:
            return None
        return cls(
            Ambari=deserialize_list(json_data.get("Ambari"), AmbariDefinition),
            Hive=deserialize_list(json_data.get("Hive"), HiveDefinition),
            Oozie=deserialize_list(json_data.get("Oozie"), OozieDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetastoresDefinition = MetastoresDefinition


@dataclass
class AmbariDefinition(BaseModel):
    DatabaseName: Optional[str]
    Password: Optional[str]
    Server: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AmbariDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmbariDefinition"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            Password=json_data.get("Password"),
            Server=json_data.get("Server"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmbariDefinition = AmbariDefinition


@dataclass
class HiveDefinition(BaseModel):
    DatabaseName: Optional[str]
    Password: Optional[str]
    Server: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HiveDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HiveDefinition"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            Password=json_data.get("Password"),
            Server=json_data.get("Server"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HiveDefinition = HiveDefinition


@dataclass
class OozieDefinition(BaseModel):
    DatabaseName: Optional[str]
    Password: Optional[str]
    Server: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OozieDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OozieDefinition"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            Password=json_data.get("Password"),
            Server=json_data.get("Server"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OozieDefinition = OozieDefinition


@dataclass
class MonitorDefinition(BaseModel):
    LogAnalyticsWorkspaceId: Optional[str]
    PrimaryKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            LogAnalyticsWorkspaceId=json_data.get("LogAnalyticsWorkspaceId"),
            PrimaryKey=json_data.get("PrimaryKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitorDefinition = MonitorDefinition


@dataclass
class NetworkDefinition(BaseModel):
    ConnectionDirection: Optional[str]
    PrivateLinkEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionDirection=json_data.get("ConnectionDirection"),
            PrivateLinkEnabled=json_data.get("PrivateLinkEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class RolesDefinition(BaseModel):
    EdgeNode: Optional[Sequence["_EdgeNodeDefinition"]]
    HeadNode: Optional[Sequence["_HeadNodeDefinition"]]
    WorkerNode: Optional[Sequence["_WorkerNodeDefinition"]]
    ZookeeperNode: Optional[Sequence["_ZookeeperNodeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RolesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RolesDefinition"]:
        if not json_data:
            return None
        return cls(
            EdgeNode=deserialize_list(json_data.get("EdgeNode"), EdgeNodeDefinition),
            HeadNode=deserialize_list(json_data.get("HeadNode"), HeadNodeDefinition),
            WorkerNode=deserialize_list(json_data.get("WorkerNode"), WorkerNodeDefinition),
            ZookeeperNode=deserialize_list(json_data.get("ZookeeperNode"), ZookeeperNodeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RolesDefinition = RolesDefinition


@dataclass
class EdgeNodeDefinition(BaseModel):
    TargetInstanceCount: Optional[float]
    VmSize: Optional[str]
    InstallScriptAction: Optional[Sequence["_InstallScriptActionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EdgeNodeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EdgeNodeDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetInstanceCount=json_data.get("TargetInstanceCount"),
            VmSize=json_data.get("VmSize"),
            InstallScriptAction=deserialize_list(json_data.get("InstallScriptAction"), InstallScriptActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EdgeNodeDefinition = EdgeNodeDefinition


@dataclass
class InstallScriptActionDefinition(BaseModel):
    Name: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstallScriptActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstallScriptActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstallScriptActionDefinition = InstallScriptActionDefinition


@dataclass
class HeadNodeDefinition(BaseModel):
    Password: Optional[str]
    SshKeys: Optional[Sequence[str]]
    SubnetId: Optional[str]
    Username: Optional[str]
    VirtualNetworkId: Optional[str]
    VmSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadNodeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadNodeDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            SshKeys=json_data.get("SshKeys"),
            SubnetId=json_data.get("SubnetId"),
            Username=json_data.get("Username"),
            VirtualNetworkId=json_data.get("VirtualNetworkId"),
            VmSize=json_data.get("VmSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadNodeDefinition = HeadNodeDefinition


@dataclass
class WorkerNodeDefinition(BaseModel):
    MinInstanceCount: Optional[float]
    Password: Optional[str]
    SshKeys: Optional[Sequence[str]]
    SubnetId: Optional[str]
    TargetInstanceCount: Optional[float]
    Username: Optional[str]
    VirtualNetworkId: Optional[str]
    VmSize: Optional[str]
    Autoscale: Optional[Sequence["_AutoscaleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerNodeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerNodeDefinition"]:
        if not json_data:
            return None
        return cls(
            MinInstanceCount=json_data.get("MinInstanceCount"),
            Password=json_data.get("Password"),
            SshKeys=json_data.get("SshKeys"),
            SubnetId=json_data.get("SubnetId"),
            TargetInstanceCount=json_data.get("TargetInstanceCount"),
            Username=json_data.get("Username"),
            VirtualNetworkId=json_data.get("VirtualNetworkId"),
            VmSize=json_data.get("VmSize"),
            Autoscale=deserialize_list(json_data.get("Autoscale"), AutoscaleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerNodeDefinition = WorkerNodeDefinition


@dataclass
class AutoscaleDefinition(BaseModel):
    Capacity: Optional[Sequence["_CapacityDefinition"]]
    Recurrence: Optional[Sequence["_RecurrenceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleDefinition"]:
        if not json_data:
            return None
        return cls(
            Capacity=deserialize_list(json_data.get("Capacity"), CapacityDefinition),
            Recurrence=deserialize_list(json_data.get("Recurrence"), RecurrenceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleDefinition = AutoscaleDefinition


@dataclass
class CapacityDefinition(BaseModel):
    MaxInstanceCount: Optional[float]
    MinInstanceCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxInstanceCount=json_data.get("MaxInstanceCount"),
            MinInstanceCount=json_data.get("MinInstanceCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityDefinition = CapacityDefinition


@dataclass
class RecurrenceDefinition(BaseModel):
    Timezone: Optional[str]
    Schedule: Optional[Sequence["_ScheduleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RecurrenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecurrenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Timezone=json_data.get("Timezone"),
            Schedule=deserialize_list(json_data.get("Schedule"), ScheduleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecurrenceDefinition = RecurrenceDefinition


@dataclass
class ScheduleDefinition(BaseModel):
    Days: Optional[Sequence[str]]
    TargetInstanceCount: Optional[float]
    Time: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
            TargetInstanceCount=json_data.get("TargetInstanceCount"),
            Time=json_data.get("Time"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleDefinition = ScheduleDefinition


@dataclass
class ZookeeperNodeDefinition(BaseModel):
    Password: Optional[str]
    SshKeys: Optional[Sequence[str]]
    SubnetId: Optional[str]
    Username: Optional[str]
    VirtualNetworkId: Optional[str]
    VmSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZookeeperNodeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZookeeperNodeDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            SshKeys=json_data.get("SshKeys"),
            SubnetId=json_data.get("SubnetId"),
            Username=json_data.get("Username"),
            VirtualNetworkId=json_data.get("VirtualNetworkId"),
            VmSize=json_data.get("VmSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZookeeperNodeDefinition = ZookeeperNodeDefinition


@dataclass
class StorageAccountDefinition(BaseModel):
    IsDefault: Optional[bool]
    StorageAccountKey: Optional[str]
    StorageContainerId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageAccountDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageAccountDefinition"]:
        if not json_data:
            return None
        return cls(
            IsDefault=json_data.get("IsDefault"),
            StorageAccountKey=json_data.get("StorageAccountKey"),
            StorageContainerId=json_data.get("StorageContainerId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageAccountDefinition = StorageAccountDefinition


@dataclass
class StorageAccountGen2Definition(BaseModel):
    FilesystemId: Optional[str]
    IsDefault: Optional[bool]
    ManagedIdentityResourceId: Optional[str]
    StorageResourceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageAccountGen2Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageAccountGen2Definition"]:
        if not json_data:
            return None
        return cls(
            FilesystemId=json_data.get("FilesystemId"),
            IsDefault=json_data.get("IsDefault"),
            ManagedIdentityResourceId=json_data.get("ManagedIdentityResourceId"),
            StorageResourceId=json_data.get("StorageResourceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageAccountGen2Definition = StorageAccountGen2Definition


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


