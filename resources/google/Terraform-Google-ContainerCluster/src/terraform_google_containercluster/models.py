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
    AdditionalZones: Optional[Sequence[str]]
    ClusterIpv4Cidr: Optional[str]
    DefaultMaxPodsPerNode: Optional[float]
    Description: Optional[str]
    EnableBinaryAuthorization: Optional[bool]
    EnableIntranodeVisibility: Optional[bool]
    EnableKubernetesAlpha: Optional[bool]
    EnableLegacyAbac: Optional[bool]
    EnableTpu: Optional[bool]
    Endpoint: Optional[str]
    Id: Optional[str]
    InitialNodeCount: Optional[float]
    InstanceGroupUrls: Optional[Sequence[str]]
    LabelFingerprint: Optional[str]
    Location: Optional[str]
    LoggingService: Optional[str]
    MasterVersion: Optional[str]
    MinMasterVersion: Optional[str]
    MonitoringService: Optional[str]
    Name: Optional[str]
    Network: Optional[str]
    NodeLocations: Optional[Sequence[str]]
    NodeVersion: Optional[str]
    Operation: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    RemoveDefaultNodePool: Optional[bool]
    ResourceLabels: Optional[Sequence["_ResourceLabels"]]
    ServicesIpv4Cidr: Optional[str]
    Subnetwork: Optional[str]
    Zone: Optional[str]
    AddonsConfig: Optional[Sequence["_AddonsConfig"]]
    AuthenticatorGroupsConfig: Optional[Sequence["_AuthenticatorGroupsConfig"]]
    ClusterAutoscaling: Optional[Sequence["_ClusterAutoscaling"]]
    IpAllocationPolicy: Optional[Sequence["_IpAllocationPolicy"]]
    MaintenancePolicy: Optional[Sequence["_MaintenancePolicy"]]
    MasterAuth: Optional[Sequence["_MasterAuth"]]
    MasterAuthorizedNetworksConfig: Optional[Sequence["_MasterAuthorizedNetworksConfig"]]
    NetworkPolicy: Optional[Sequence["_NetworkPolicy"]]
    NodeConfig: Optional[Sequence["_NodeConfig"]]
    NodePool: Optional[Sequence["_NodePool"]]
    PodSecurityPolicyConfig: Optional[Sequence["_PodSecurityPolicyConfig"]]
    PrivateClusterConfig: Optional[Sequence["_PrivateClusterConfig"]]
    Timeouts: Optional["_Timeouts"]
    VerticalPodAutoscaling: Optional[Sequence["_VerticalPodAutoscaling"]]
    HorizontalPodAutoscaling: Optional[Sequence["_HorizontalPodAutoscaling"]]
    HttpLoadBalancing: Optional[Sequence["_HttpLoadBalancing"]]
    KubernetesDashboard: Optional[Sequence["_KubernetesDashboard"]]
    NetworkPolicyConfig: Optional[Sequence["_NetworkPolicyConfig"]]
    AutoProvisioningDefaults: Optional[Sequence["_AutoProvisioningDefaults"]]
    ResourceLimits: Optional[Sequence["_ResourceLimits"]]
    DailyMaintenanceWindow: Optional[Sequence["_DailyMaintenanceWindow"]]
    ClientCertificateConfig: Optional[Sequence["_ClientCertificateConfig"]]
    CidrBlocks: Optional[Sequence["_CidrBlocks"]]
    SandboxConfig: Optional[Sequence["_SandboxConfig"]]
    ShieldedInstanceConfig: Optional[Sequence["_ShieldedInstanceConfig"]]
    WorkloadMetadataConfig: Optional[Sequence["_WorkloadMetadataConfig"]]
    Autoscaling: Optional[Sequence["_Autoscaling"]]
    Management: Optional[Sequence["_Management"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdditionalZones=json_data.get("AdditionalZones"),
            ClusterIpv4Cidr=json_data.get("ClusterIpv4Cidr"),
            DefaultMaxPodsPerNode=json_data.get("DefaultMaxPodsPerNode"),
            Description=json_data.get("Description"),
            EnableBinaryAuthorization=json_data.get("EnableBinaryAuthorization"),
            EnableIntranodeVisibility=json_data.get("EnableIntranodeVisibility"),
            EnableKubernetesAlpha=json_data.get("EnableKubernetesAlpha"),
            EnableLegacyAbac=json_data.get("EnableLegacyAbac"),
            EnableTpu=json_data.get("EnableTpu"),
            Endpoint=json_data.get("Endpoint"),
            Id=json_data.get("Id"),
            InitialNodeCount=json_data.get("InitialNodeCount"),
            InstanceGroupUrls=json_data.get("InstanceGroupUrls"),
            LabelFingerprint=json_data.get("LabelFingerprint"),
            Location=json_data.get("Location"),
            LoggingService=json_data.get("LoggingService"),
            MasterVersion=json_data.get("MasterVersion"),
            MinMasterVersion=json_data.get("MinMasterVersion"),
            MonitoringService=json_data.get("MonitoringService"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            NodeLocations=json_data.get("NodeLocations"),
            NodeVersion=json_data.get("NodeVersion"),
            Operation=json_data.get("Operation"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            RemoveDefaultNodePool=json_data.get("RemoveDefaultNodePool"),
            ResourceLabels=json_data.get("ResourceLabels"),
            ServicesIpv4Cidr=json_data.get("ServicesIpv4Cidr"),
            Subnetwork=json_data.get("Subnetwork"),
            Zone=json_data.get("Zone"),
            AddonsConfig=json_data.get("AddonsConfig"),
            AuthenticatorGroupsConfig=json_data.get("AuthenticatorGroupsConfig"),
            ClusterAutoscaling=json_data.get("ClusterAutoscaling"),
            IpAllocationPolicy=json_data.get("IpAllocationPolicy"),
            MaintenancePolicy=json_data.get("MaintenancePolicy"),
            MasterAuth=json_data.get("MasterAuth"),
            MasterAuthorizedNetworksConfig=json_data.get("MasterAuthorizedNetworksConfig"),
            NetworkPolicy=json_data.get("NetworkPolicy"),
            NodeConfig=json_data.get("NodeConfig"),
            NodePool=json_data.get("NodePool"),
            PodSecurityPolicyConfig=json_data.get("PodSecurityPolicyConfig"),
            PrivateClusterConfig=json_data.get("PrivateClusterConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            VerticalPodAutoscaling=json_data.get("VerticalPodAutoscaling"),
            HorizontalPodAutoscaling=json_data.get("HorizontalPodAutoscaling"),
            HttpLoadBalancing=json_data.get("HttpLoadBalancing"),
            KubernetesDashboard=json_data.get("KubernetesDashboard"),
            NetworkPolicyConfig=json_data.get("NetworkPolicyConfig"),
            AutoProvisioningDefaults=json_data.get("AutoProvisioningDefaults"),
            ResourceLimits=json_data.get("ResourceLimits"),
            DailyMaintenanceWindow=json_data.get("DailyMaintenanceWindow"),
            ClientCertificateConfig=json_data.get("ClientCertificateConfig"),
            CidrBlocks=json_data.get("CidrBlocks"),
            SandboxConfig=json_data.get("SandboxConfig"),
            ShieldedInstanceConfig=json_data.get("ShieldedInstanceConfig"),
            WorkloadMetadataConfig=json_data.get("WorkloadMetadataConfig"),
            Autoscaling=json_data.get("Autoscaling"),
            Management=json_data.get("Management"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ResourceLabels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceLabels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceLabels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceLabels = ResourceLabels


@dataclass
class AddonsConfig:
    HorizontalPodAutoscaling: Optional[Sequence["_HorizontalPodAutoscaling"]]
    HttpLoadBalancing: Optional[Sequence["_HttpLoadBalancing"]]
    KubernetesDashboard: Optional[Sequence["_KubernetesDashboard"]]
    NetworkPolicyConfig: Optional[Sequence["_NetworkPolicyConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_AddonsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddonsConfig"]:
        if not json_data:
            return None
        return cls(
            HorizontalPodAutoscaling=json_data.get("HorizontalPodAutoscaling"),
            HttpLoadBalancing=json_data.get("HttpLoadBalancing"),
            KubernetesDashboard=json_data.get("KubernetesDashboard"),
            NetworkPolicyConfig=json_data.get("NetworkPolicyConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddonsConfig = AddonsConfig


@dataclass
class HorizontalPodAutoscaling:
    Disabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_HorizontalPodAutoscaling"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HorizontalPodAutoscaling"]:
        if not json_data:
            return None
        return cls(
            Disabled=json_data.get("Disabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HorizontalPodAutoscaling = HorizontalPodAutoscaling


@dataclass
class HttpLoadBalancing:
    Disabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_HttpLoadBalancing"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpLoadBalancing"]:
        if not json_data:
            return None
        return cls(
            Disabled=json_data.get("Disabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpLoadBalancing = HttpLoadBalancing


@dataclass
class KubernetesDashboard:
    Disabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_KubernetesDashboard"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubernetesDashboard"]:
        if not json_data:
            return None
        return cls(
            Disabled=json_data.get("Disabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubernetesDashboard = KubernetesDashboard


@dataclass
class NetworkPolicyConfig:
    Disabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkPolicyConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkPolicyConfig"]:
        if not json_data:
            return None
        return cls(
            Disabled=json_data.get("Disabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkPolicyConfig = NetworkPolicyConfig


@dataclass
class AuthenticatorGroupsConfig:
    SecurityGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticatorGroupsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticatorGroupsConfig"]:
        if not json_data:
            return None
        return cls(
            SecurityGroup=json_data.get("SecurityGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticatorGroupsConfig = AuthenticatorGroupsConfig


@dataclass
class ClusterAutoscaling:
    Enabled: Optional[bool]
    AutoProvisioningDefaults: Optional[Sequence["_AutoProvisioningDefaults"]]
    ResourceLimits: Optional[Sequence["_ResourceLimits"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterAutoscaling"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterAutoscaling"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            AutoProvisioningDefaults=json_data.get("AutoProvisioningDefaults"),
            ResourceLimits=json_data.get("ResourceLimits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterAutoscaling = ClusterAutoscaling


@dataclass
class AutoProvisioningDefaults:
    OauthScopes: Optional[Sequence[str]]
    ServiceAccount: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoProvisioningDefaults"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoProvisioningDefaults"]:
        if not json_data:
            return None
        return cls(
            OauthScopes=json_data.get("OauthScopes"),
            ServiceAccount=json_data.get("ServiceAccount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoProvisioningDefaults = AutoProvisioningDefaults


@dataclass
class ResourceLimits:
    Maximum: Optional[float]
    Minimum: Optional[float]
    ResourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceLimits"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceLimits"]:
        if not json_data:
            return None
        return cls(
            Maximum=json_data.get("Maximum"),
            Minimum=json_data.get("Minimum"),
            ResourceType=json_data.get("ResourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceLimits = ResourceLimits


@dataclass
class IpAllocationPolicy:
    ClusterIpv4CidrBlock: Optional[str]
    ClusterSecondaryRangeName: Optional[str]
    NodeIpv4CidrBlock: Optional[str]
    ServicesIpv4CidrBlock: Optional[str]
    ServicesSecondaryRangeName: Optional[str]
    SubnetworkName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAllocationPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAllocationPolicy"]:
        if not json_data:
            return None
        return cls(
            ClusterIpv4CidrBlock=json_data.get("ClusterIpv4CidrBlock"),
            ClusterSecondaryRangeName=json_data.get("ClusterSecondaryRangeName"),
            NodeIpv4CidrBlock=json_data.get("NodeIpv4CidrBlock"),
            ServicesIpv4CidrBlock=json_data.get("ServicesIpv4CidrBlock"),
            ServicesSecondaryRangeName=json_data.get("ServicesSecondaryRangeName"),
            SubnetworkName=json_data.get("SubnetworkName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAllocationPolicy = IpAllocationPolicy


@dataclass
class MaintenancePolicy:
    DailyMaintenanceWindow: Optional[Sequence["_DailyMaintenanceWindow"]]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenancePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenancePolicy"]:
        if not json_data:
            return None
        return cls(
            DailyMaintenanceWindow=json_data.get("DailyMaintenanceWindow"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenancePolicy = MaintenancePolicy


@dataclass
class DailyMaintenanceWindow:
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DailyMaintenanceWindow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DailyMaintenanceWindow"]:
        if not json_data:
            return None
        return cls(
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DailyMaintenanceWindow = DailyMaintenanceWindow


@dataclass
class MasterAuth:
    Password: Optional[str]
    Username: Optional[str]
    ClientCertificateConfig: Optional[Sequence["_ClientCertificateConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_MasterAuth"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterAuth"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
            ClientCertificateConfig=json_data.get("ClientCertificateConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterAuth = MasterAuth


@dataclass
class ClientCertificateConfig:
    IssueClientCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ClientCertificateConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientCertificateConfig"]:
        if not json_data:
            return None
        return cls(
            IssueClientCertificate=json_data.get("IssueClientCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientCertificateConfig = ClientCertificateConfig


@dataclass
class MasterAuthorizedNetworksConfig:
    CidrBlocks: Optional[Sequence["_CidrBlocks"]]

    @classmethod
    def _deserialize(
        cls: Type["_MasterAuthorizedNetworksConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterAuthorizedNetworksConfig"]:
        if not json_data:
            return None
        return cls(
            CidrBlocks=json_data.get("CidrBlocks"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterAuthorizedNetworksConfig = MasterAuthorizedNetworksConfig


@dataclass
class CidrBlocks:
    CidrBlock: Optional[str]
    DisplayName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CidrBlocks"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CidrBlocks"]:
        if not json_data:
            return None
        return cls(
            CidrBlock=json_data.get("CidrBlock"),
            DisplayName=json_data.get("DisplayName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CidrBlocks = CidrBlocks


@dataclass
class NetworkPolicy:
    Enabled: Optional[bool]
    Provider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkPolicy"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Provider=json_data.get("Provider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkPolicy = NetworkPolicy


@dataclass
class NodeConfig:
    DiskSizeGb: Optional[float]
    DiskType: Optional[str]
    GuestAccelerator: Optional[Sequence["_GuestAccelerator"]]
    ImageType: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    LocalSsdCount: Optional[float]
    MachineType: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    MinCpuPlatform: Optional[str]
    OauthScopes: Optional[Sequence[str]]
    Preemptible: Optional[bool]
    ServiceAccount: Optional[str]
    Tags: Optional[Sequence[str]]
    Taint: Optional[Sequence["_Taint"]]
    SandboxConfig: Optional[Sequence["_SandboxConfig"]]
    ShieldedInstanceConfig: Optional[Sequence["_ShieldedInstanceConfig"]]
    WorkloadMetadataConfig: Optional[Sequence["_WorkloadMetadataConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeConfig"]:
        if not json_data:
            return None
        return cls(
            DiskSizeGb=json_data.get("DiskSizeGb"),
            DiskType=json_data.get("DiskType"),
            GuestAccelerator=json_data.get("GuestAccelerator"),
            ImageType=json_data.get("ImageType"),
            Labels=json_data.get("Labels"),
            LocalSsdCount=json_data.get("LocalSsdCount"),
            MachineType=json_data.get("MachineType"),
            Metadata=json_data.get("Metadata"),
            MinCpuPlatform=json_data.get("MinCpuPlatform"),
            OauthScopes=json_data.get("OauthScopes"),
            Preemptible=json_data.get("Preemptible"),
            ServiceAccount=json_data.get("ServiceAccount"),
            Tags=json_data.get("Tags"),
            Taint=json_data.get("Taint"),
            SandboxConfig=json_data.get("SandboxConfig"),
            ShieldedInstanceConfig=json_data.get("ShieldedInstanceConfig"),
            WorkloadMetadataConfig=json_data.get("WorkloadMetadataConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeConfig = NodeConfig


@dataclass
class GuestAccelerator:
    Count: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestAccelerator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestAccelerator"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestAccelerator = GuestAccelerator


@dataclass
class Labels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


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
class Taint:
    Effect: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Taint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Taint"]:
        if not json_data:
            return None
        return cls(
            Effect=json_data.get("Effect"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Taint = Taint


@dataclass
class SandboxConfig:
    SandboxType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SandboxConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SandboxConfig"]:
        if not json_data:
            return None
        return cls(
            SandboxType=json_data.get("SandboxType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SandboxConfig = SandboxConfig


@dataclass
class ShieldedInstanceConfig:
    EnableIntegrityMonitoring: Optional[bool]
    EnableSecureBoot: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ShieldedInstanceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShieldedInstanceConfig"]:
        if not json_data:
            return None
        return cls(
            EnableIntegrityMonitoring=json_data.get("EnableIntegrityMonitoring"),
            EnableSecureBoot=json_data.get("EnableSecureBoot"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShieldedInstanceConfig = ShieldedInstanceConfig


@dataclass
class WorkloadMetadataConfig:
    NodeMetadata: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkloadMetadataConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkloadMetadataConfig"]:
        if not json_data:
            return None
        return cls(
            NodeMetadata=json_data.get("NodeMetadata"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkloadMetadataConfig = WorkloadMetadataConfig


@dataclass
class NodePool:
    InitialNodeCount: Optional[float]
    MaxPodsPerNode: Optional[float]
    Name: Optional[str]
    NamePrefix: Optional[str]
    NodeCount: Optional[float]
    Version: Optional[str]
    Autoscaling: Optional[Sequence["_Autoscaling"]]
    Management: Optional[Sequence["_Management"]]
    NodeConfig: Optional[Sequence["_NodeConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodePool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodePool"]:
        if not json_data:
            return None
        return cls(
            InitialNodeCount=json_data.get("InitialNodeCount"),
            MaxPodsPerNode=json_data.get("MaxPodsPerNode"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            NodeCount=json_data.get("NodeCount"),
            Version=json_data.get("Version"),
            Autoscaling=json_data.get("Autoscaling"),
            Management=json_data.get("Management"),
            NodeConfig=json_data.get("NodeConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodePool = NodePool


@dataclass
class Autoscaling:
    MaxNodeCount: Optional[float]
    MinNodeCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Autoscaling"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Autoscaling"]:
        if not json_data:
            return None
        return cls(
            MaxNodeCount=json_data.get("MaxNodeCount"),
            MinNodeCount=json_data.get("MinNodeCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Autoscaling = Autoscaling


@dataclass
class Management:
    AutoRepair: Optional[bool]
    AutoUpgrade: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Management"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Management"]:
        if not json_data:
            return None
        return cls(
            AutoRepair=json_data.get("AutoRepair"),
            AutoUpgrade=json_data.get("AutoUpgrade"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Management = Management


@dataclass
class PodSecurityPolicyConfig:
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PodSecurityPolicyConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PodSecurityPolicyConfig"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PodSecurityPolicyConfig = PodSecurityPolicyConfig


@dataclass
class PrivateClusterConfig:
    EnablePrivateEndpoint: Optional[bool]
    EnablePrivateNodes: Optional[bool]
    MasterIpv4CidrBlock: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateClusterConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateClusterConfig"]:
        if not json_data:
            return None
        return cls(
            EnablePrivateEndpoint=json_data.get("EnablePrivateEndpoint"),
            EnablePrivateNodes=json_data.get("EnablePrivateNodes"),
            MasterIpv4CidrBlock=json_data.get("MasterIpv4CidrBlock"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateClusterConfig = PrivateClusterConfig


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
class VerticalPodAutoscaling:
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_VerticalPodAutoscaling"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VerticalPodAutoscaling"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VerticalPodAutoscaling = VerticalPodAutoscaling


