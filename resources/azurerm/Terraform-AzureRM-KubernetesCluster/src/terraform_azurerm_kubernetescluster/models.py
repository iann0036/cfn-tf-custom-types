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
    ApiServerAuthorizedIpRanges: Optional[Sequence[str]]
    DnsPrefix: Optional[str]
    EnablePodSecurityPolicy: Optional[bool]
    Fqdn: Optional[str]
    Id: Optional[str]
    KubeAdminConfig: Optional[Sequence["_KubeAdminConfig"]]
    KubeAdminConfigRaw: Optional[str]
    KubeConfig: Optional[Sequence["_KubeConfig"]]
    KubeConfigRaw: Optional[str]
    KubernetesVersion: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    NodeResourceGroup: Optional[str]
    PrivateFqdn: Optional[str]
    PrivateLinkEnabled: Optional[bool]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    AddonProfile: Optional[Sequence["_AddonProfile"]]
    DefaultNodePool: Optional[Sequence["_DefaultNodePool"]]
    Identity: Optional[Sequence["_Identity"]]
    LinuxProfile: Optional[Sequence["_LinuxProfile"]]
    NetworkProfile: Optional[Sequence["_NetworkProfile"]]
    RoleBasedAccessControl: Optional[Sequence["_RoleBasedAccessControl"]]
    ServicePrincipal: Optional[Sequence["_ServicePrincipal"]]
    Timeouts: Optional["_Timeouts"]
    WindowsProfile: Optional[Sequence["_WindowsProfile"]]
    AciConnectorLinux: Optional[Sequence["_AciConnectorLinux"]]
    AzurePolicy: Optional[Sequence["_AzurePolicy"]]
    HttpApplicationRouting: Optional[Sequence["_HttpApplicationRouting"]]
    KubeDashboard: Optional[Sequence["_KubeDashboard"]]
    OmsAgent: Optional[Sequence["_OmsAgent"]]
    SshKey: Optional[Sequence["_SshKey"]]
    LoadBalancerProfile: Optional[Sequence["_LoadBalancerProfile"]]
    AzureActiveDirectory: Optional[Sequence["_AzureActiveDirectory"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApiServerAuthorizedIpRanges=json_data.get("ApiServerAuthorizedIpRanges"),
            DnsPrefix=json_data.get("DnsPrefix"),
            EnablePodSecurityPolicy=json_data.get("EnablePodSecurityPolicy"),
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            KubeAdminConfig=json_data.get("KubeAdminConfig"),
            KubeAdminConfigRaw=json_data.get("KubeAdminConfigRaw"),
            KubeConfig=json_data.get("KubeConfig"),
            KubeConfigRaw=json_data.get("KubeConfigRaw"),
            KubernetesVersion=json_data.get("KubernetesVersion"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NodeResourceGroup=json_data.get("NodeResourceGroup"),
            PrivateFqdn=json_data.get("PrivateFqdn"),
            PrivateLinkEnabled=json_data.get("PrivateLinkEnabled"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=json_data.get("Tags"),
            AddonProfile=json_data.get("AddonProfile"),
            DefaultNodePool=json_data.get("DefaultNodePool"),
            Identity=json_data.get("Identity"),
            LinuxProfile=json_data.get("LinuxProfile"),
            NetworkProfile=json_data.get("NetworkProfile"),
            RoleBasedAccessControl=json_data.get("RoleBasedAccessControl"),
            ServicePrincipal=json_data.get("ServicePrincipal"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            WindowsProfile=json_data.get("WindowsProfile"),
            AciConnectorLinux=json_data.get("AciConnectorLinux"),
            AzurePolicy=json_data.get("AzurePolicy"),
            HttpApplicationRouting=json_data.get("HttpApplicationRouting"),
            KubeDashboard=json_data.get("KubeDashboard"),
            OmsAgent=json_data.get("OmsAgent"),
            SshKey=json_data.get("SshKey"),
            LoadBalancerProfile=json_data.get("LoadBalancerProfile"),
            AzureActiveDirectory=json_data.get("AzureActiveDirectory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class KubeAdminConfig:
    ClientCertificate: Optional[str]
    ClientKey: Optional[str]
    ClusterCaCertificate: Optional[str]
    Host: Optional[str]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubeAdminConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeAdminConfig"]:
        if not json_data:
            return None
        return cls(
            ClientCertificate=json_data.get("ClientCertificate"),
            ClientKey=json_data.get("ClientKey"),
            ClusterCaCertificate=json_data.get("ClusterCaCertificate"),
            Host=json_data.get("Host"),
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeAdminConfig = KubeAdminConfig


@dataclass
class KubeConfig:
    ClientCertificate: Optional[str]
    ClientKey: Optional[str]
    ClusterCaCertificate: Optional[str]
    Host: Optional[str]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeConfig"]:
        if not json_data:
            return None
        return cls(
            ClientCertificate=json_data.get("ClientCertificate"),
            ClientKey=json_data.get("ClientKey"),
            ClusterCaCertificate=json_data.get("ClusterCaCertificate"),
            Host=json_data.get("Host"),
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeConfig = KubeConfig


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
class AddonProfile:
    AciConnectorLinux: Optional[Sequence["_AciConnectorLinux"]]
    AzurePolicy: Optional[Sequence["_AzurePolicy"]]
    HttpApplicationRouting: Optional[Sequence["_HttpApplicationRouting"]]
    KubeDashboard: Optional[Sequence["_KubeDashboard"]]
    OmsAgent: Optional[Sequence["_OmsAgent"]]

    @classmethod
    def _deserialize(
        cls: Type["_AddonProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddonProfile"]:
        if not json_data:
            return None
        return cls(
            AciConnectorLinux=json_data.get("AciConnectorLinux"),
            AzurePolicy=json_data.get("AzurePolicy"),
            HttpApplicationRouting=json_data.get("HttpApplicationRouting"),
            KubeDashboard=json_data.get("KubeDashboard"),
            OmsAgent=json_data.get("OmsAgent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddonProfile = AddonProfile


@dataclass
class AciConnectorLinux:
    Enabled: Optional[bool]
    SubnetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AciConnectorLinux"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AciConnectorLinux"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            SubnetName=json_data.get("SubnetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AciConnectorLinux = AciConnectorLinux


@dataclass
class AzurePolicy:
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AzurePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzurePolicy"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzurePolicy = AzurePolicy


@dataclass
class HttpApplicationRouting:
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_HttpApplicationRouting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpApplicationRouting"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpApplicationRouting = HttpApplicationRouting


@dataclass
class KubeDashboard:
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_KubeDashboard"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeDashboard"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeDashboard = KubeDashboard


@dataclass
class OmsAgent:
    Enabled: Optional[bool]
    LogAnalyticsWorkspaceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OmsAgent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OmsAgent"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            LogAnalyticsWorkspaceId=json_data.get("LogAnalyticsWorkspaceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OmsAgent = OmsAgent


@dataclass
class DefaultNodePool:
    AvailabilityZones: Optional[Sequence[str]]
    EnableAutoScaling: Optional[bool]
    EnableNodePublicIp: Optional[bool]
    MaxCount: Optional[float]
    MaxPods: Optional[float]
    MinCount: Optional[float]
    Name: Optional[str]
    NodeCount: Optional[float]
    NodeLabels: Optional[Sequence["_NodeLabels"]]
    NodeTaints: Optional[Sequence[str]]
    OsDiskSizeGb: Optional[float]
    Tags: Optional[Sequence["_Tags2"]]
    Type: Optional[str]
    VmSize: Optional[str]
    VnetSubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultNodePool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultNodePool"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZones=json_data.get("AvailabilityZones"),
            EnableAutoScaling=json_data.get("EnableAutoScaling"),
            EnableNodePublicIp=json_data.get("EnableNodePublicIp"),
            MaxCount=json_data.get("MaxCount"),
            MaxPods=json_data.get("MaxPods"),
            MinCount=json_data.get("MinCount"),
            Name=json_data.get("Name"),
            NodeCount=json_data.get("NodeCount"),
            NodeLabels=json_data.get("NodeLabels"),
            NodeTaints=json_data.get("NodeTaints"),
            OsDiskSizeGb=json_data.get("OsDiskSizeGb"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            VmSize=json_data.get("VmSize"),
            VnetSubnetId=json_data.get("VnetSubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultNodePool = DefaultNodePool


@dataclass
class NodeLabels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeLabels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeLabels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeLabels = NodeLabels


@dataclass
class Tags2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags2 = Tags2


@dataclass
class Identity:
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Identity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Identity"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Identity = Identity


@dataclass
class LinuxProfile:
    AdminUsername: Optional[str]
    SshKey: Optional[Sequence["_SshKey"]]

    @classmethod
    def _deserialize(
        cls: Type["_LinuxProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinuxProfile"]:
        if not json_data:
            return None
        return cls(
            AdminUsername=json_data.get("AdminUsername"),
            SshKey=json_data.get("SshKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinuxProfile = LinuxProfile


@dataclass
class SshKey:
    KeyData: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SshKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SshKey"]:
        if not json_data:
            return None
        return cls(
            KeyData=json_data.get("KeyData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SshKey = SshKey


@dataclass
class NetworkProfile:
    DnsServiceIp: Optional[str]
    DockerBridgeCidr: Optional[str]
    LoadBalancerSku: Optional[str]
    NetworkPlugin: Optional[str]
    NetworkPolicy: Optional[str]
    PodCidr: Optional[str]
    ServiceCidr: Optional[str]
    LoadBalancerProfile: Optional[Sequence["_LoadBalancerProfile"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkProfile"]:
        if not json_data:
            return None
        return cls(
            DnsServiceIp=json_data.get("DnsServiceIp"),
            DockerBridgeCidr=json_data.get("DockerBridgeCidr"),
            LoadBalancerSku=json_data.get("LoadBalancerSku"),
            NetworkPlugin=json_data.get("NetworkPlugin"),
            NetworkPolicy=json_data.get("NetworkPolicy"),
            PodCidr=json_data.get("PodCidr"),
            ServiceCidr=json_data.get("ServiceCidr"),
            LoadBalancerProfile=json_data.get("LoadBalancerProfile"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkProfile = NetworkProfile


@dataclass
class LoadBalancerProfile:
    ManagedOutboundIpCount: Optional[float]
    OutboundIpAddressIds: Optional[Sequence[str]]
    OutboundIpPrefixIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancerProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancerProfile"]:
        if not json_data:
            return None
        return cls(
            ManagedOutboundIpCount=json_data.get("ManagedOutboundIpCount"),
            OutboundIpAddressIds=json_data.get("OutboundIpAddressIds"),
            OutboundIpPrefixIds=json_data.get("OutboundIpPrefixIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancerProfile = LoadBalancerProfile


@dataclass
class RoleBasedAccessControl:
    Enabled: Optional[bool]
    AzureActiveDirectory: Optional[Sequence["_AzureActiveDirectory"]]

    @classmethod
    def _deserialize(
        cls: Type["_RoleBasedAccessControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoleBasedAccessControl"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            AzureActiveDirectory=json_data.get("AzureActiveDirectory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoleBasedAccessControl = RoleBasedAccessControl


@dataclass
class AzureActiveDirectory:
    ClientAppId: Optional[str]
    ServerAppId: Optional[str]
    ServerAppSecret: Optional[str]
    TenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureActiveDirectory"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureActiveDirectory"]:
        if not json_data:
            return None
        return cls(
            ClientAppId=json_data.get("ClientAppId"),
            ServerAppId=json_data.get("ServerAppId"),
            ServerAppSecret=json_data.get("ServerAppSecret"),
            TenantId=json_data.get("TenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureActiveDirectory = AzureActiveDirectory


@dataclass
class ServicePrincipal:
    ClientId: Optional[str]
    ClientSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServicePrincipal"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicePrincipal"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicePrincipal = ServicePrincipal


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


@dataclass
class WindowsProfile:
    AdminPassword: Optional[str]
    AdminUsername: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WindowsProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WindowsProfile"]:
        if not json_data:
            return None
        return cls(
            AdminPassword=json_data.get("AdminPassword"),
            AdminUsername=json_data.get("AdminUsername"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WindowsProfile = WindowsProfile


