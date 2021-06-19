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
    AccountName: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    MaxTasksPerNode: Optional[float]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    NodeAgentSkuId: Optional[str]
    ResourceGroupName: Optional[str]
    StopPendingResizeOperation: Optional[bool]
    VmSize: Optional[str]
    AutoScale: Optional[Sequence["_AutoScaleDefinition"]]
    Certificate: Optional[Sequence["_CertificateDefinition"]]
    ContainerConfiguration: Optional[Sequence["_ContainerConfigurationDefinition"]]
    FixedScale: Optional[Sequence["_FixedScaleDefinition"]]
    NetworkConfiguration: Optional[Sequence["_NetworkConfigurationDefinition"]]
    StartTask: Optional[Sequence["_StartTaskDefinition"]]
    StorageImageReference: Optional[Sequence["_StorageImageReferenceDefinition"]]
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
            AccountName=json_data.get("AccountName"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            MaxTasksPerNode=json_data.get("MaxTasksPerNode"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            NodeAgentSkuId=json_data.get("NodeAgentSkuId"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            StopPendingResizeOperation=json_data.get("StopPendingResizeOperation"),
            VmSize=json_data.get("VmSize"),
            AutoScale=deserialize_list(json_data.get("AutoScale"), AutoScaleDefinition),
            Certificate=deserialize_list(json_data.get("Certificate"), CertificateDefinition),
            ContainerConfiguration=deserialize_list(json_data.get("ContainerConfiguration"), ContainerConfigurationDefinition),
            FixedScale=deserialize_list(json_data.get("FixedScale"), FixedScaleDefinition),
            NetworkConfiguration=deserialize_list(json_data.get("NetworkConfiguration"), NetworkConfigurationDefinition),
            StartTask=deserialize_list(json_data.get("StartTask"), StartTaskDefinition),
            StorageImageReference=deserialize_list(json_data.get("StorageImageReference"), StorageImageReferenceDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class AutoScaleDefinition(BaseModel):
    EvaluationInterval: Optional[str]
    Formula: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScaleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScaleDefinition"]:
        if not json_data:
            return None
        return cls(
            EvaluationInterval=json_data.get("EvaluationInterval"),
            Formula=json_data.get("Formula"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScaleDefinition = AutoScaleDefinition


@dataclass
class CertificateDefinition(BaseModel):
    Id: Optional[str]
    StoreLocation: Optional[str]
    StoreName: Optional[str]
    Visibility: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            StoreLocation=json_data.get("StoreLocation"),
            StoreName=json_data.get("StoreName"),
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDefinition = CertificateDefinition


@dataclass
class ContainerConfigurationDefinition(BaseModel):
    ContainerImageNames: Optional[Sequence[str]]
    ContainerRegistries: Optional[Sequence["_ContainerRegistriesDefinition"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ContainerImageNames=json_data.get("ContainerImageNames"),
            ContainerRegistries=deserialize_list(json_data.get("ContainerRegistries"), ContainerRegistriesDefinition),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerConfigurationDefinition = ContainerConfigurationDefinition


@dataclass
class ContainerRegistriesDefinition(BaseModel):
    Password: Optional[str]
    RegistryServer: Optional[str]
    UserName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerRegistriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerRegistriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            RegistryServer=json_data.get("RegistryServer"),
            UserName=json_data.get("UserName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerRegistriesDefinition = ContainerRegistriesDefinition


@dataclass
class FixedScaleDefinition(BaseModel):
    ResizeTimeout: Optional[str]
    TargetDedicatedNodes: Optional[float]
    TargetLowPriorityNodes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FixedScaleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FixedScaleDefinition"]:
        if not json_data:
            return None
        return cls(
            ResizeTimeout=json_data.get("ResizeTimeout"),
            TargetDedicatedNodes=json_data.get("TargetDedicatedNodes"),
            TargetLowPriorityNodes=json_data.get("TargetLowPriorityNodes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FixedScaleDefinition = FixedScaleDefinition


@dataclass
class NetworkConfigurationDefinition(BaseModel):
    PublicAddressProvisioningType: Optional[str]
    PublicIps: Optional[Sequence[str]]
    SubnetId: Optional[str]
    EndpointConfiguration: Optional[Sequence["_EndpointConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            PublicAddressProvisioningType=json_data.get("PublicAddressProvisioningType"),
            PublicIps=json_data.get("PublicIps"),
            SubnetId=json_data.get("SubnetId"),
            EndpointConfiguration=deserialize_list(json_data.get("EndpointConfiguration"), EndpointConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfigurationDefinition = NetworkConfigurationDefinition


@dataclass
class EndpointConfigurationDefinition(BaseModel):
    BackendPort: Optional[float]
    FrontendPortRange: Optional[str]
    Name: Optional[str]
    Protocol: Optional[str]
    NetworkSecurityGroupRules: Optional[Sequence["_NetworkSecurityGroupRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            BackendPort=json_data.get("BackendPort"),
            FrontendPortRange=json_data.get("FrontendPortRange"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            NetworkSecurityGroupRules=deserialize_list(json_data.get("NetworkSecurityGroupRules"), NetworkSecurityGroupRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointConfigurationDefinition = EndpointConfigurationDefinition


@dataclass
class NetworkSecurityGroupRulesDefinition(BaseModel):
    Access: Optional[str]
    Priority: Optional[float]
    SourceAddressPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkSecurityGroupRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkSecurityGroupRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Access=json_data.get("Access"),
            Priority=json_data.get("Priority"),
            SourceAddressPrefix=json_data.get("SourceAddressPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkSecurityGroupRulesDefinition = NetworkSecurityGroupRulesDefinition


@dataclass
class StartTaskDefinition(BaseModel):
    CommandLine: Optional[str]
    Environment: Optional[Sequence["_EnvironmentDefinition"]]
    MaxTaskRetryCount: Optional[float]
    WaitForSuccess: Optional[bool]
    ResourceFile: Optional[Sequence["_ResourceFileDefinition"]]
    UserIdentity: Optional[Sequence["_UserIdentityDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StartTaskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StartTaskDefinition"]:
        if not json_data:
            return None
        return cls(
            CommandLine=json_data.get("CommandLine"),
            Environment=deserialize_list(json_data.get("Environment"), EnvironmentDefinition),
            MaxTaskRetryCount=json_data.get("MaxTaskRetryCount"),
            WaitForSuccess=json_data.get("WaitForSuccess"),
            ResourceFile=deserialize_list(json_data.get("ResourceFile"), ResourceFileDefinition),
            UserIdentity=deserialize_list(json_data.get("UserIdentity"), UserIdentityDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StartTaskDefinition = StartTaskDefinition


@dataclass
class EnvironmentDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentDefinition = EnvironmentDefinition


@dataclass
class ResourceFileDefinition(BaseModel):
    AutoStorageContainerName: Optional[str]
    BlobPrefix: Optional[str]
    FileMode: Optional[str]
    FilePath: Optional[str]
    HttpUrl: Optional[str]
    StorageContainerUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceFileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceFileDefinition"]:
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
_ResourceFileDefinition = ResourceFileDefinition


@dataclass
class UserIdentityDefinition(BaseModel):
    UserName: Optional[str]
    AutoUser: Optional[Sequence["_AutoUserDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UserIdentityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserIdentityDefinition"]:
        if not json_data:
            return None
        return cls(
            UserName=json_data.get("UserName"),
            AutoUser=deserialize_list(json_data.get("AutoUser"), AutoUserDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserIdentityDefinition = UserIdentityDefinition


@dataclass
class AutoUserDefinition(BaseModel):
    ElevationLevel: Optional[str]
    Scope: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoUserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoUserDefinition"]:
        if not json_data:
            return None
        return cls(
            ElevationLevel=json_data.get("ElevationLevel"),
            Scope=json_data.get("Scope"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoUserDefinition = AutoUserDefinition


@dataclass
class StorageImageReferenceDefinition(BaseModel):
    Id: Optional[str]
    Offer: Optional[str]
    Publisher: Optional[str]
    Sku: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageImageReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageImageReferenceDefinition"]:
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
_StorageImageReferenceDefinition = StorageImageReferenceDefinition


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


