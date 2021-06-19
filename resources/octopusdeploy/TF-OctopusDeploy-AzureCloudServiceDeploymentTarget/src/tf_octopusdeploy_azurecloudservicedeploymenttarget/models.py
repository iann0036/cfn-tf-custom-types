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
    AccountId: Optional[str]
    CloudServiceName: Optional[str]
    DefaultWorkerPoolId: Optional[str]
    Environments: Optional[Sequence[str]]
    HasLatestCalamari: Optional[bool]
    HealthStatus: Optional[str]
    Id: Optional[str]
    IsDisabled: Optional[bool]
    IsInProcess: Optional[bool]
    MachinePolicyId: Optional[str]
    Name: Optional[str]
    OperatingSystem: Optional[str]
    Roles: Optional[Sequence[str]]
    ShellName: Optional[str]
    ShellVersion: Optional[str]
    Slot: Optional[str]
    SpaceId: Optional[str]
    Status: Optional[str]
    StatusSummary: Optional[str]
    StorageAccountName: Optional[str]
    SwapIfPossible: Optional[bool]
    TenantTags: Optional[Sequence[str]]
    TenantedDeploymentParticipation: Optional[str]
    Tenants: Optional[Sequence[str]]
    Thumbprint: Optional[str]
    Uri: Optional[str]
    UseCurrentInstanceCount: Optional[bool]
    Endpoint: Optional[Sequence["_EndpointDefinition"]]

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
            AccountId=json_data.get("AccountId"),
            CloudServiceName=json_data.get("CloudServiceName"),
            DefaultWorkerPoolId=json_data.get("DefaultWorkerPoolId"),
            Environments=json_data.get("Environments"),
            HasLatestCalamari=json_data.get("HasLatestCalamari"),
            HealthStatus=json_data.get("HealthStatus"),
            Id=json_data.get("Id"),
            IsDisabled=json_data.get("IsDisabled"),
            IsInProcess=json_data.get("IsInProcess"),
            MachinePolicyId=json_data.get("MachinePolicyId"),
            Name=json_data.get("Name"),
            OperatingSystem=json_data.get("OperatingSystem"),
            Roles=json_data.get("Roles"),
            ShellName=json_data.get("ShellName"),
            ShellVersion=json_data.get("ShellVersion"),
            Slot=json_data.get("Slot"),
            SpaceId=json_data.get("SpaceId"),
            Status=json_data.get("Status"),
            StatusSummary=json_data.get("StatusSummary"),
            StorageAccountName=json_data.get("StorageAccountName"),
            SwapIfPossible=json_data.get("SwapIfPossible"),
            TenantTags=json_data.get("TenantTags"),
            TenantedDeploymentParticipation=json_data.get("TenantedDeploymentParticipation"),
            Tenants=json_data.get("Tenants"),
            Thumbprint=json_data.get("Thumbprint"),
            Uri=json_data.get("Uri"),
            UseCurrentInstanceCount=json_data.get("UseCurrentInstanceCount"),
            Endpoint=deserialize_list(json_data.get("Endpoint"), EndpointDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EndpointDefinition(BaseModel):
    AadClientCredentialSecret: Optional[str]
    AadCredentialType: Optional[str]
    AadUserCredentialUsername: Optional[str]
    AccountId: Optional[str]
    ApplicationsDirectory: Optional[str]
    CertificateSignatureAlgorithm: Optional[str]
    CertificateStoreLocation: Optional[str]
    CertificateStoreName: Optional[str]
    ClientCertificateVariable: Optional[str]
    CloudServiceName: Optional[str]
    ClusterCertificate: Optional[str]
    ClusterUrl: Optional[str]
    CommunicationStyle: Optional[str]
    ConnectionEndpoint: Optional[str]
    DefaultWorkerPoolId: Optional[str]
    DotNetCorePlatform: Optional[str]
    Fingerprint: Optional[str]
    Host: Optional[str]
    Id: Optional[str]
    Namespace: Optional[str]
    Port: Optional[float]
    ProxyId: Optional[str]
    ResourceGroupName: Optional[str]
    RunningInContainer: Optional[bool]
    SecurityMode: Optional[str]
    ServerCertificateThumbprint: Optional[str]
    SkipTlsVerification: Optional[bool]
    Slot: Optional[str]
    StorageAccountName: Optional[str]
    SwapIfPossible: Optional[bool]
    Thumbprint: Optional[str]
    Uri: Optional[str]
    UseCurrentInstanceCount: Optional[bool]
    WebAppName: Optional[str]
    WebAppSlotName: Optional[str]
    WorkingDirectory: Optional[str]
    Authentication: Optional[Sequence["_AuthenticationDefinition"]]
    Container: Optional[Sequence["_ContainerDefinition"]]
    Destination: Optional[Sequence["_DestinationDefinition"]]
    TentacleVersionDetails: Optional[Sequence["_TentacleVersionDetailsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointDefinition"]:
        if not json_data:
            return None
        return cls(
            AadClientCredentialSecret=json_data.get("AadClientCredentialSecret"),
            AadCredentialType=json_data.get("AadCredentialType"),
            AadUserCredentialUsername=json_data.get("AadUserCredentialUsername"),
            AccountId=json_data.get("AccountId"),
            ApplicationsDirectory=json_data.get("ApplicationsDirectory"),
            CertificateSignatureAlgorithm=json_data.get("CertificateSignatureAlgorithm"),
            CertificateStoreLocation=json_data.get("CertificateStoreLocation"),
            CertificateStoreName=json_data.get("CertificateStoreName"),
            ClientCertificateVariable=json_data.get("ClientCertificateVariable"),
            CloudServiceName=json_data.get("CloudServiceName"),
            ClusterCertificate=json_data.get("ClusterCertificate"),
            ClusterUrl=json_data.get("ClusterUrl"),
            CommunicationStyle=json_data.get("CommunicationStyle"),
            ConnectionEndpoint=json_data.get("ConnectionEndpoint"),
            DefaultWorkerPoolId=json_data.get("DefaultWorkerPoolId"),
            DotNetCorePlatform=json_data.get("DotNetCorePlatform"),
            Fingerprint=json_data.get("Fingerprint"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            Namespace=json_data.get("Namespace"),
            Port=json_data.get("Port"),
            ProxyId=json_data.get("ProxyId"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RunningInContainer=json_data.get("RunningInContainer"),
            SecurityMode=json_data.get("SecurityMode"),
            ServerCertificateThumbprint=json_data.get("ServerCertificateThumbprint"),
            SkipTlsVerification=json_data.get("SkipTlsVerification"),
            Slot=json_data.get("Slot"),
            StorageAccountName=json_data.get("StorageAccountName"),
            SwapIfPossible=json_data.get("SwapIfPossible"),
            Thumbprint=json_data.get("Thumbprint"),
            Uri=json_data.get("Uri"),
            UseCurrentInstanceCount=json_data.get("UseCurrentInstanceCount"),
            WebAppName=json_data.get("WebAppName"),
            WebAppSlotName=json_data.get("WebAppSlotName"),
            WorkingDirectory=json_data.get("WorkingDirectory"),
            Authentication=deserialize_list(json_data.get("Authentication"), AuthenticationDefinition),
            Container=deserialize_list(json_data.get("Container"), ContainerDefinition),
            Destination=deserialize_list(json_data.get("Destination"), DestinationDefinition),
            TentacleVersionDetails=deserialize_list(json_data.get("TentacleVersionDetails"), TentacleVersionDetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointDefinition = EndpointDefinition


@dataclass
class AuthenticationDefinition(BaseModel):
    AccountId: Optional[str]
    AdminLogin: Optional[str]
    AssumeRole: Optional[bool]
    AssumeRoleExternalId: Optional[str]
    AssumeRoleSessionDuration: Optional[float]
    AssumedRoleArn: Optional[str]
    AssumedRoleSession: Optional[str]
    AuthenticationType: Optional[str]
    ClientCertificate: Optional[str]
    ClusterName: Optional[str]
    ClusterResourceGroup: Optional[str]
    UseInstanceRole: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            AdminLogin=json_data.get("AdminLogin"),
            AssumeRole=json_data.get("AssumeRole"),
            AssumeRoleExternalId=json_data.get("AssumeRoleExternalId"),
            AssumeRoleSessionDuration=json_data.get("AssumeRoleSessionDuration"),
            AssumedRoleArn=json_data.get("AssumedRoleArn"),
            AssumedRoleSession=json_data.get("AssumedRoleSession"),
            AuthenticationType=json_data.get("AuthenticationType"),
            ClientCertificate=json_data.get("ClientCertificate"),
            ClusterName=json_data.get("ClusterName"),
            ClusterResourceGroup=json_data.get("ClusterResourceGroup"),
            UseInstanceRole=json_data.get("UseInstanceRole"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationDefinition = AuthenticationDefinition


@dataclass
class ContainerDefinition(BaseModel):
    FeedId: Optional[str]
    Image: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerDefinition"]:
        if not json_data:
            return None
        return cls(
            FeedId=json_data.get("FeedId"),
            Image=json_data.get("Image"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerDefinition = ContainerDefinition


@dataclass
class DestinationDefinition(BaseModel):
    DestinationType: Optional[str]
    DropFolderPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationType=json_data.get("DestinationType"),
            DropFolderPath=json_data.get("DropFolderPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationDefinition = DestinationDefinition


@dataclass
class TentacleVersionDetailsDefinition(BaseModel):
    UpgradeLocked: Optional[bool]
    UpgradeRequired: Optional[bool]
    UpgradeSuggested: Optional[bool]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TentacleVersionDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TentacleVersionDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            UpgradeLocked=json_data.get("UpgradeLocked"),
            UpgradeRequired=json_data.get("UpgradeRequired"),
            UpgradeSuggested=json_data.get("UpgradeSuggested"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TentacleVersionDetailsDefinition = TentacleVersionDetailsDefinition


