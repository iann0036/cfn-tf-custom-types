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
    EdgeSshEndpoint: Optional[str]
    HttpsEndpoint: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Rstudio: Optional[bool]
    SshEndpoint: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Tier: Optional[str]
    TlsMinVersion: Optional[str]
    Gateway: Optional[Sequence["_GatewayDefinition"]]
    Roles: Optional[Sequence["_RolesDefinition"]]
    StorageAccount: Optional[Sequence["_StorageAccountDefinition"]]
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
            EdgeSshEndpoint=json_data.get("EdgeSshEndpoint"),
            HttpsEndpoint=json_data.get("HttpsEndpoint"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Rstudio=json_data.get("Rstudio"),
            SshEndpoint=json_data.get("SshEndpoint"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Tier=json_data.get("Tier"),
            TlsMinVersion=json_data.get("TlsMinVersion"),
            Gateway=deserialize_list(json_data.get("Gateway"), GatewayDefinition),
            Roles=deserialize_list(json_data.get("Roles"), RolesDefinition),
            StorageAccount=deserialize_list(json_data.get("StorageAccount"), StorageAccountDefinition),
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
    Password: Optional[str]
    SshKeys: Optional[Sequence[str]]
    SubnetId: Optional[str]
    Username: Optional[str]
    VirtualNetworkId: Optional[str]
    VmSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EdgeNodeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EdgeNodeDefinition"]:
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
_EdgeNodeDefinition = EdgeNodeDefinition


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
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerNodeDefinition = WorkerNodeDefinition


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

