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
    AccountName: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    MaxTasksPerNode: Optional[float]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    NodeAgentSkuId: Optional[str]
    ResourceGroupName: Optional[str]
    StopPendingResizeOperation: Optional[bool]
    VmSize: Optional[str]
    AutoScale: Optional[Sequence["_AutoScale"]]
    Certificate: Optional[Sequence["_Certificate"]]
    ContainerConfiguration: Optional[Sequence["_ContainerConfiguration"]]
    FixedScale: Optional[Sequence["_FixedScale"]]
    NetworkConfiguration: Optional[Sequence["_NetworkConfiguration"]]
    StartTask: Optional[Sequence["_StartTask"]]
    StorageImageReference: Optional[Sequence["_StorageImageReference"]]
    Timeouts: Optional["_Timeouts"]
    EndpointConfiguration: Optional[Sequence["_EndpointConfiguration"]]
    ResourceFile: Optional[Sequence["_ResourceFile"]]
    UserIdentity: Optional[Sequence["_UserIdentity"]]
    NetworkSecurityGroupRules: Optional[Sequence["_NetworkSecurityGroupRules"]]
    AutoUser: Optional[Sequence["_AutoUser"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccountName=json_data.get("AccountName"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            MaxTasksPerNode=json_data.get("MaxTasksPerNode"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            NodeAgentSkuId=json_data.get("NodeAgentSkuId"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            StopPendingResizeOperation=json_data.get("StopPendingResizeOperation"),
            VmSize=json_data.get("VmSize"),
            AutoScale=json_data.get("AutoScale"),
            Certificate=json_data.get("Certificate"),
            ContainerConfiguration=json_data.get("ContainerConfiguration"),
            FixedScale=json_data.get("FixedScale"),
            NetworkConfiguration=json_data.get("NetworkConfiguration"),
            StartTask=json_data.get("StartTask"),
            StorageImageReference=json_data.get("StorageImageReference"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            EndpointConfiguration=json_data.get("EndpointConfiguration"),
            ResourceFile=json_data.get("ResourceFile"),
            UserIdentity=json_data.get("UserIdentity"),
            NetworkSecurityGroupRules=json_data.get("NetworkSecurityGroupRules"),
            AutoUser=json_data.get("AutoUser"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Metadata:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class AutoScale:
    EvaluationInterval: Optional[str]
    Formula: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScale"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScale"]:
        if not json_data:
            return None
        return cls(
            EvaluationInterval=json_data.get("EvaluationInterval"),
            Formula=json_data.get("Formula"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScale = AutoScale


@dataclass
class Certificate:
    Id: Optional[str]
    StoreLocation: Optional[str]
    StoreName: Optional[str]
    Visibility: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Certificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Certificate"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            StoreLocation=json_data.get("StoreLocation"),
            StoreName=json_data.get("StoreName"),
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Certificate = Certificate


@dataclass
class ContainerConfiguration:
    ContainerRegistries: Optional[Sequence["_ContainerRegistries"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerConfiguration"]:
        if not json_data:
            return None
        return cls(
            ContainerRegistries=json_data.get("ContainerRegistries"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerConfiguration = ContainerConfiguration


@dataclass
class ContainerRegistries:
    Password: Optional[str]
    RegistryServer: Optional[str]
    UserName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerRegistries"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerRegistries"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            RegistryServer=json_data.get("RegistryServer"),
            UserName=json_data.get("UserName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerRegistries = ContainerRegistries


@dataclass
class FixedScale:
    ResizeTimeout: Optional[str]
    TargetDedicatedNodes: Optional[float]
    TargetLowPriorityNodes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FixedScale"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FixedScale"]:
        if not json_data:
            return None
        return cls(
            ResizeTimeout=json_data.get("ResizeTimeout"),
            TargetDedicatedNodes=json_data.get("TargetDedicatedNodes"),
            TargetLowPriorityNodes=json_data.get("TargetLowPriorityNodes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FixedScale = FixedScale


@dataclass
class NetworkConfiguration:
    PublicIps: Optional[Sequence[str]]
    SubnetId: Optional[str]
    EndpointConfiguration: Optional[Sequence["_EndpointConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfiguration"]:
        if not json_data:
            return None
        return cls(
            PublicIps=json_data.get("PublicIps"),
            SubnetId=json_data.get("SubnetId"),
            EndpointConfiguration=json_data.get("EndpointConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfiguration = NetworkConfiguration


@dataclass
class EndpointConfiguration:
    BackendPort: Optional[float]
    FrontendPortRange: Optional[str]
    Name: Optional[str]
    Protocol: Optional[str]
    NetworkSecurityGroupRules: Optional[Sequence["_NetworkSecurityGroupRules"]]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointConfiguration"]:
        if not json_data:
            return None
        return cls(
            BackendPort=json_data.get("BackendPort"),
            FrontendPortRange=json_data.get("FrontendPortRange"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            NetworkSecurityGroupRules=json_data.get("NetworkSecurityGroupRules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointConfiguration = EndpointConfiguration


@dataclass
class NetworkSecurityGroupRules:
    Access: Optional[str]
    Priority: Optional[float]
    SourceAddressPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkSecurityGroupRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkSecurityGroupRules"]:
        if not json_data:
            return None
        return cls(
            Access=json_data.get("Access"),
            Priority=json_data.get("Priority"),
            SourceAddressPrefix=json_data.get("SourceAddressPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkSecurityGroupRules = NetworkSecurityGroupRules


@dataclass
class StartTask:
    CommandLine: Optional[str]
    Environment: Optional[Sequence["_Environment"]]
    MaxTaskRetryCount: Optional[float]
    WaitForSuccess: Optional[bool]
    ResourceFile: Optional[Sequence["_ResourceFile"]]
    UserIdentity: Optional[Sequence["_UserIdentity"]]

    @classmethod
    def _deserialize(
        cls: Type["_StartTask"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StartTask"]:
        if not json_data:
            return None
        return cls(
            CommandLine=json_data.get("CommandLine"),
            Environment=json_data.get("Environment"),
            MaxTaskRetryCount=json_data.get("MaxTaskRetryCount"),
            WaitForSuccess=json_data.get("WaitForSuccess"),
            ResourceFile=json_data.get("ResourceFile"),
            UserIdentity=json_data.get("UserIdentity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StartTask = StartTask


@dataclass
class Environment:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Environment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Environment"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Environment = Environment


@dataclass
class ResourceFile:
    AutoStorageContainerName: Optional[str]
    BlobPrefix: Optional[str]
    FileMode: Optional[str]
    FilePath: Optional[str]
    HttpUrl: Optional[str]
    StorageContainerUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceFile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceFile"]:
        if not json_data:
            return None
        return cls(
            AutoStorageContainerName=json_data.get("AutoStorageContainerName"),
            BlobPrefix=json_data.get("BlobPrefix"),
            FileMode=json_data.get("FileMode"),
            FilePath=json_data.get("FilePath"),
            HttpUrl=json_data.get("HttpUrl"),
            StorageContainerUrl=json_data.get("StorageContainerUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceFile = ResourceFile


@dataclass
class UserIdentity:
    UserName: Optional[str]
    AutoUser: Optional[Sequence["_AutoUser"]]

    @classmethod
    def _deserialize(
        cls: Type["_UserIdentity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserIdentity"]:
        if not json_data:
            return None
        return cls(
            UserName=json_data.get("UserName"),
            AutoUser=json_data.get("AutoUser"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserIdentity = UserIdentity


@dataclass
class AutoUser:
    ElevationLevel: Optional[str]
    Scope: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoUser"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoUser"]:
        if not json_data:
            return None
        return cls(
            ElevationLevel=json_data.get("ElevationLevel"),
            Scope=json_data.get("Scope"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoUser = AutoUser


@dataclass
class StorageImageReference:
    Id: Optional[str]
    Offer: Optional[str]
    Publisher: Optional[str]
    Sku: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageImageReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageImageReference"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Offer=json_data.get("Offer"),
            Publisher=json_data.get("Publisher"),
            Sku=json_data.get("Sku"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageImageReference = StorageImageReference


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


