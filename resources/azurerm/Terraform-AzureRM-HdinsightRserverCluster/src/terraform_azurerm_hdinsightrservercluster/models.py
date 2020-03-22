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
    ClusterVersion: Optional[str]
    EdgeSshEndpoint: Optional[str]
    HttpsEndpoint: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Rstudio: Optional[bool]
    SshEndpoint: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Tier: Optional[str]
    Gateway: Optional[Sequence["_Gateway"]]
    Roles: Optional[Sequence["_Roles"]]
    StorageAccount: Optional[Sequence["_StorageAccount"]]
    Timeouts: Optional["_Timeouts"]
    EdgeNode: Optional[Sequence["_EdgeNode"]]
    HeadNode: Optional[Sequence["_HeadNode"]]
    WorkerNode: Optional[Sequence["_WorkerNode"]]
    ZookeeperNode: Optional[Sequence["_ZookeeperNode"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            Tags=json_data.get("Tags"),
            Tier=json_data.get("Tier"),
            Gateway=json_data.get("Gateway"),
            Roles=json_data.get("Roles"),
            StorageAccount=json_data.get("StorageAccount"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            EdgeNode=json_data.get("EdgeNode"),
            HeadNode=json_data.get("HeadNode"),
            WorkerNode=json_data.get("WorkerNode"),
            ZookeeperNode=json_data.get("ZookeeperNode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Gateway:
    Enabled: Optional[bool]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Gateway"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Gateway"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Gateway = Gateway


@dataclass
class Roles:
    EdgeNode: Optional[Sequence["_EdgeNode"]]
    HeadNode: Optional[Sequence["_HeadNode"]]
    WorkerNode: Optional[Sequence["_WorkerNode"]]
    ZookeeperNode: Optional[Sequence["_ZookeeperNode"]]

    @classmethod
    def _deserialize(
        cls: Type["_Roles"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Roles"]:
        if not json_data:
            return None
        return cls(
            EdgeNode=json_data.get("EdgeNode"),
            HeadNode=json_data.get("HeadNode"),
            WorkerNode=json_data.get("WorkerNode"),
            ZookeeperNode=json_data.get("ZookeeperNode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Roles = Roles


@dataclass
class EdgeNode:
    Password: Optional[str]
    SshKeys: Optional[Sequence[str]]
    SubnetId: Optional[str]
    Username: Optional[str]
    VirtualNetworkId: Optional[str]
    VmSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EdgeNode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EdgeNode"]:
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
_EdgeNode = EdgeNode


@dataclass
class HeadNode:
    Password: Optional[str]
    SshKeys: Optional[Sequence[str]]
    SubnetId: Optional[str]
    Username: Optional[str]
    VirtualNetworkId: Optional[str]
    VmSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadNode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadNode"]:
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
_HeadNode = HeadNode


@dataclass
class WorkerNode:
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
        cls: Type["_WorkerNode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerNode"]:
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
_WorkerNode = WorkerNode


@dataclass
class ZookeeperNode:
    Password: Optional[str]
    SshKeys: Optional[Sequence[str]]
    SubnetId: Optional[str]
    Username: Optional[str]
    VirtualNetworkId: Optional[str]
    VmSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZookeeperNode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZookeeperNode"]:
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
_ZookeeperNode = ZookeeperNode


@dataclass
class StorageAccount:
    IsDefault: Optional[bool]
    StorageAccountKey: Optional[str]
    StorageContainerId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageAccount"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageAccount"]:
        if not json_data:
            return None
        return cls(
            IsDefault=json_data.get("IsDefault"),
            StorageAccountKey=json_data.get("StorageAccountKey"),
            StorageContainerId=json_data.get("StorageContainerId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageAccount = StorageAccount


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


