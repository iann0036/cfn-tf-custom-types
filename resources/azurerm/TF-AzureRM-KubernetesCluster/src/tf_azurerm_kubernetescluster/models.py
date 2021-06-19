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
    ApiServerAuthorizedIpRanges: Optional[Sequence[str]]
    AutomaticChannelUpgrade: Optional[str]
    DiskEncryptionSetId: Optional[str]
    DnsPrefix: Optional[str]
    DnsPrefixPrivateCluster: Optional[str]
    EnablePodSecurityPolicy: Optional[bool]
    Fqdn: Optional[str]
    Id: Optional[str]
    KubeAdminConfig: Optional[Sequence["_KubeAdminConfigDefinition"]]
    KubeAdminConfigRaw: Optional[str]
    KubeConfig: Optional[Sequence["_KubeConfigDefinition"]]
    KubeConfigRaw: Optional[str]
    KubernetesVersion: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    NodeResourceGroup: Optional[str]
    PrivateClusterEnabled: Optional[bool]
    PrivateDnsZoneId: Optional[str]
    PrivateFqdn: Optional[str]
    PrivateLinkEnabled: Optional[bool]
    ResourceGroupName: Optional[str]
    SkuTier: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    AddonProfile: Optional[Sequence["_AddonProfileDefinition"]]
    AutoScalerProfile: Optional[Sequence["_AutoScalerProfileDefinition"]]
    DefaultNodePool: Optional[Sequence["_DefaultNodePoolDefinition"]]
    Identity: Optional[Sequence["_IdentityDefinition"]]
    KubeletIdentity: Optional[Sequence["_KubeletIdentityDefinition"]]
    LinuxProfile: Optional[Sequence["_LinuxProfileDefinition"]]
    NetworkProfile: Optional[Sequence["_NetworkProfileDefinition"]]
    RoleBasedAccessControl: Optional[Sequence["_RoleBasedAccessControlDefinition"]]
    ServicePrincipal: Optional[Sequence["_ServicePrincipalDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    WindowsProfile: Optional[Sequence["_WindowsProfileDefinition"]]

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
            ApiServerAuthorizedIpRanges=json_data.get("ApiServerAuthorizedIpRanges"),
            AutomaticChannelUpgrade=json_data.get("AutomaticChannelUpgrade"),
            DiskEncryptionSetId=json_data.get("DiskEncryptionSetId"),
            DnsPrefix=json_data.get("DnsPrefix"),
            DnsPrefixPrivateCluster=json_data.get("DnsPrefixPrivateCluster"),
            EnablePodSecurityPolicy=json_data.get("EnablePodSecurityPolicy"),
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            KubeAdminConfig=deserialize_list(json_data.get("KubeAdminConfig"), KubeAdminConfigDefinition),
            KubeAdminConfigRaw=json_data.get("KubeAdminConfigRaw"),
            KubeConfig=deserialize_list(json_data.get("KubeConfig"), KubeConfigDefinition),
            KubeConfigRaw=json_data.get("KubeConfigRaw"),
            KubernetesVersion=json_data.get("KubernetesVersion"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NodeResourceGroup=json_data.get("NodeResourceGroup"),
            PrivateClusterEnabled=json_data.get("PrivateClusterEnabled"),
            PrivateDnsZoneId=json_data.get("PrivateDnsZoneId"),
            PrivateFqdn=json_data.get("PrivateFqdn"),
            PrivateLinkEnabled=json_data.get("PrivateLinkEnabled"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SkuTier=json_data.get("SkuTier"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            AddonProfile=deserialize_list(json_data.get("AddonProfile"), AddonProfileDefinition),
            AutoScalerProfile=deserialize_list(json_data.get("AutoScalerProfile"), AutoScalerProfileDefinition),
            DefaultNodePool=deserialize_list(json_data.get("DefaultNodePool"), DefaultNodePoolDefinition),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            KubeletIdentity=deserialize_list(json_data.get("KubeletIdentity"), KubeletIdentityDefinition),
            LinuxProfile=deserialize_list(json_data.get("LinuxProfile"), LinuxProfileDefinition),
            NetworkProfile=deserialize_list(json_data.get("NetworkProfile"), NetworkProfileDefinition),
            RoleBasedAccessControl=deserialize_list(json_data.get("RoleBasedAccessControl"), RoleBasedAccessControlDefinition),
            ServicePrincipal=deserialize_list(json_data.get("ServicePrincipal"), ServicePrincipalDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            WindowsProfile=deserialize_list(json_data.get("WindowsProfile"), WindowsProfileDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class KubeAdminConfigDefinition(BaseModel):
    ClientCertificate: Optional[str]
    ClientKey: Optional[str]
    ClusterCaCertificate: Optional[str]
    Host: Optional[str]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubeAdminConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeAdminConfigDefinition"]:
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
_KubeAdminConfigDefinition = KubeAdminConfigDefinition


@dataclass
class KubeConfigDefinition(BaseModel):
    ClientCertificate: Optional[str]
    ClientKey: Optional[str]
    ClusterCaCertificate: Optional[str]
    Host: Optional[str]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubeConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeConfigDefinition"]:
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
_KubeConfigDefinition = KubeConfigDefinition


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
class AddonProfileDefinition(BaseModel):
    AciConnectorLinux: Optional[Sequence["_AciConnectorLinuxDefinition"]]
    AzurePolicy: Optional[Sequence["_AzurePolicyDefinition"]]
    HttpApplicationRouting: Optional[Sequence["_HttpApplicationRoutingDefinition"]]
    IngressApplicationGateway: Optional[Sequence["_IngressApplicationGatewayDefinition"]]
    KubeDashboard: Optional[Sequence["_KubeDashboardDefinition"]]
    OmsAgent: Optional[Sequence["_OmsAgentDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AddonProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddonProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            AciConnectorLinux=deserialize_list(json_data.get("AciConnectorLinux"), AciConnectorLinuxDefinition),
            AzurePolicy=deserialize_list(json_data.get("AzurePolicy"), AzurePolicyDefinition),
            HttpApplicationRouting=deserialize_list(json_data.get("HttpApplicationRouting"), HttpApplicationRoutingDefinition),
            IngressApplicationGateway=deserialize_list(json_data.get("IngressApplicationGateway"), IngressApplicationGatewayDefinition),
            KubeDashboard=deserialize_list(json_data.get("KubeDashboard"), KubeDashboardDefinition),
            OmsAgent=deserialize_list(json_data.get("OmsAgent"), OmsAgentDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddonProfileDefinition = AddonProfileDefinition


@dataclass
class AciConnectorLinuxDefinition(BaseModel):
    Enabled: Optional[bool]
    SubnetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AciConnectorLinuxDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AciConnectorLinuxDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            SubnetName=json_data.get("SubnetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AciConnectorLinuxDefinition = AciConnectorLinuxDefinition


@dataclass
class AzurePolicyDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AzurePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzurePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzurePolicyDefinition = AzurePolicyDefinition


@dataclass
class HttpApplicationRoutingDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_HttpApplicationRoutingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpApplicationRoutingDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpApplicationRoutingDefinition = HttpApplicationRoutingDefinition


@dataclass
class IngressApplicationGatewayDefinition(BaseModel):
    Enabled: Optional[bool]
    GatewayId: Optional[str]
    GatewayName: Optional[str]
    SubnetCidr: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IngressApplicationGatewayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressApplicationGatewayDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            GatewayId=json_data.get("GatewayId"),
            GatewayName=json_data.get("GatewayName"),
            SubnetCidr=json_data.get("SubnetCidr"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressApplicationGatewayDefinition = IngressApplicationGatewayDefinition


@dataclass
class KubeDashboardDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_KubeDashboardDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeDashboardDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeDashboardDefinition = KubeDashboardDefinition


@dataclass
class OmsAgentDefinition(BaseModel):
    Enabled: Optional[bool]
    LogAnalyticsWorkspaceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OmsAgentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OmsAgentDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            LogAnalyticsWorkspaceId=json_data.get("LogAnalyticsWorkspaceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OmsAgentDefinition = OmsAgentDefinition


@dataclass
class AutoScalerProfileDefinition(BaseModel):
    BalanceSimilarNodeGroups: Optional[bool]
    EmptyBulkDeleteMax: Optional[str]
    Expander: Optional[str]
    MaxGracefulTerminationSec: Optional[str]
    MaxNodeProvisioningTime: Optional[str]
    MaxUnreadyNodes: Optional[float]
    MaxUnreadyPercentage: Optional[float]
    NewPodScaleUpDelay: Optional[str]
    ScaleDownDelayAfterAdd: Optional[str]
    ScaleDownDelayAfterDelete: Optional[str]
    ScaleDownDelayAfterFailure: Optional[str]
    ScaleDownUnneeded: Optional[str]
    ScaleDownUnready: Optional[str]
    ScaleDownUtilizationThreshold: Optional[str]
    ScanInterval: Optional[str]
    SkipNodesWithLocalStorage: Optional[bool]
    SkipNodesWithSystemPods: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScalerProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScalerProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            BalanceSimilarNodeGroups=json_data.get("BalanceSimilarNodeGroups"),
            EmptyBulkDeleteMax=json_data.get("EmptyBulkDeleteMax"),
            Expander=json_data.get("Expander"),
            MaxGracefulTerminationSec=json_data.get("MaxGracefulTerminationSec"),
            MaxNodeProvisioningTime=json_data.get("MaxNodeProvisioningTime"),
            MaxUnreadyNodes=json_data.get("MaxUnreadyNodes"),
            MaxUnreadyPercentage=json_data.get("MaxUnreadyPercentage"),
            NewPodScaleUpDelay=json_data.get("NewPodScaleUpDelay"),
            ScaleDownDelayAfterAdd=json_data.get("ScaleDownDelayAfterAdd"),
            ScaleDownDelayAfterDelete=json_data.get("ScaleDownDelayAfterDelete"),
            ScaleDownDelayAfterFailure=json_data.get("ScaleDownDelayAfterFailure"),
            ScaleDownUnneeded=json_data.get("ScaleDownUnneeded"),
            ScaleDownUnready=json_data.get("ScaleDownUnready"),
            ScaleDownUtilizationThreshold=json_data.get("ScaleDownUtilizationThreshold"),
            ScanInterval=json_data.get("ScanInterval"),
            SkipNodesWithLocalStorage=json_data.get("SkipNodesWithLocalStorage"),
            SkipNodesWithSystemPods=json_data.get("SkipNodesWithSystemPods"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScalerProfileDefinition = AutoScalerProfileDefinition


@dataclass
class DefaultNodePoolDefinition(BaseModel):
    AvailabilityZones: Optional[Sequence[str]]
    EnableAutoScaling: Optional[bool]
    EnableHostEncryption: Optional[bool]
    EnableNodePublicIp: Optional[bool]
    MaxCount: Optional[float]
    MaxPods: Optional[float]
    MinCount: Optional[float]
    Name: Optional[str]
    NodeCount: Optional[float]
    NodeLabels: Optional[Sequence["_NodeLabelsDefinition"]]
    NodePublicIpPrefixId: Optional[str]
    NodeTaints: Optional[Sequence[str]]
    OnlyCriticalAddonsEnabled: Optional[bool]
    OrchestratorVersion: Optional[str]
    OsDiskSizeGb: Optional[float]
    OsDiskType: Optional[str]
    ProximityPlacementGroupId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition2"]]
    Type: Optional[str]
    VmSize: Optional[str]
    VnetSubnetId: Optional[str]
    KubeletConfig: Optional[Sequence["_KubeletConfigDefinition"]]
    LinuxOsConfig: Optional[Sequence["_LinuxOsConfigDefinition"]]
    UpgradeSettings: Optional[Sequence["_UpgradeSettingsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultNodePoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultNodePoolDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZones=json_data.get("AvailabilityZones"),
            EnableAutoScaling=json_data.get("EnableAutoScaling"),
            EnableHostEncryption=json_data.get("EnableHostEncryption"),
            EnableNodePublicIp=json_data.get("EnableNodePublicIp"),
            MaxCount=json_data.get("MaxCount"),
            MaxPods=json_data.get("MaxPods"),
            MinCount=json_data.get("MinCount"),
            Name=json_data.get("Name"),
            NodeCount=json_data.get("NodeCount"),
            NodeLabels=deserialize_list(json_data.get("NodeLabels"), NodeLabelsDefinition),
            NodePublicIpPrefixId=json_data.get("NodePublicIpPrefixId"),
            NodeTaints=json_data.get("NodeTaints"),
            OnlyCriticalAddonsEnabled=json_data.get("OnlyCriticalAddonsEnabled"),
            OrchestratorVersion=json_data.get("OrchestratorVersion"),
            OsDiskSizeGb=json_data.get("OsDiskSizeGb"),
            OsDiskType=json_data.get("OsDiskType"),
            ProximityPlacementGroupId=json_data.get("ProximityPlacementGroupId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition2),
            Type=json_data.get("Type"),
            VmSize=json_data.get("VmSize"),
            VnetSubnetId=json_data.get("VnetSubnetId"),
            KubeletConfig=deserialize_list(json_data.get("KubeletConfig"), KubeletConfigDefinition),
            LinuxOsConfig=deserialize_list(json_data.get("LinuxOsConfig"), LinuxOsConfigDefinition),
            UpgradeSettings=deserialize_list(json_data.get("UpgradeSettings"), UpgradeSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultNodePoolDefinition = DefaultNodePoolDefinition


@dataclass
class NodeLabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeLabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeLabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeLabelsDefinition = NodeLabelsDefinition


@dataclass
class TagsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition2 = TagsDefinition2


@dataclass
class KubeletConfigDefinition(BaseModel):
    AllowedUnsafeSysctls: Optional[Sequence[str]]
    ContainerLogMaxLine: Optional[float]
    ContainerLogMaxSizeMb: Optional[float]
    CpuCfsQuotaEnabled: Optional[bool]
    CpuCfsQuotaPeriod: Optional[str]
    CpuManagerPolicy: Optional[str]
    ImageGcHighThreshold: Optional[float]
    ImageGcLowThreshold: Optional[float]
    PodMaxPid: Optional[float]
    TopologyManagerPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubeletConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeletConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedUnsafeSysctls=json_data.get("AllowedUnsafeSysctls"),
            ContainerLogMaxLine=json_data.get("ContainerLogMaxLine"),
            ContainerLogMaxSizeMb=json_data.get("ContainerLogMaxSizeMb"),
            CpuCfsQuotaEnabled=json_data.get("CpuCfsQuotaEnabled"),
            CpuCfsQuotaPeriod=json_data.get("CpuCfsQuotaPeriod"),
            CpuManagerPolicy=json_data.get("CpuManagerPolicy"),
            ImageGcHighThreshold=json_data.get("ImageGcHighThreshold"),
            ImageGcLowThreshold=json_data.get("ImageGcLowThreshold"),
            PodMaxPid=json_data.get("PodMaxPid"),
            TopologyManagerPolicy=json_data.get("TopologyManagerPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeletConfigDefinition = KubeletConfigDefinition


@dataclass
class LinuxOsConfigDefinition(BaseModel):
    SwapFileSizeMb: Optional[float]
    TransparentHugePageDefrag: Optional[str]
    TransparentHugePageEnabled: Optional[str]
    SysctlConfig: Optional[Sequence["_SysctlConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LinuxOsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinuxOsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            SwapFileSizeMb=json_data.get("SwapFileSizeMb"),
            TransparentHugePageDefrag=json_data.get("TransparentHugePageDefrag"),
            TransparentHugePageEnabled=json_data.get("TransparentHugePageEnabled"),
            SysctlConfig=deserialize_list(json_data.get("SysctlConfig"), SysctlConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinuxOsConfigDefinition = LinuxOsConfigDefinition


@dataclass
class SysctlConfigDefinition(BaseModel):
    FsAioMaxNr: Optional[float]
    FsFileMax: Optional[float]
    FsInotifyMaxUserWatches: Optional[float]
    FsNrOpen: Optional[float]
    KernelThreadsMax: Optional[float]
    NetCoreNetdevMaxBacklog: Optional[float]
    NetCoreOptmemMax: Optional[float]
    NetCoreRmemDefault: Optional[float]
    NetCoreRmemMax: Optional[float]
    NetCoreSomaxconn: Optional[float]
    NetCoreWmemDefault: Optional[float]
    NetCoreWmemMax: Optional[float]
    NetIpv4IpLocalPortRangeMax: Optional[float]
    NetIpv4IpLocalPortRangeMin: Optional[float]
    NetIpv4NeighDefaultGcThresh1: Optional[float]
    NetIpv4NeighDefaultGcThresh2: Optional[float]
    NetIpv4NeighDefaultGcThresh3: Optional[float]
    NetIpv4TcpFinTimeout: Optional[float]
    NetIpv4TcpKeepaliveIntvl: Optional[float]
    NetIpv4TcpKeepaliveProbes: Optional[float]
    NetIpv4TcpKeepaliveTime: Optional[float]
    NetIpv4TcpMaxSynBacklog: Optional[float]
    NetIpv4TcpMaxTwBuckets: Optional[float]
    NetIpv4TcpTwReuse: Optional[bool]
    NetNetfilterNfConntrackBuckets: Optional[float]
    NetNetfilterNfConntrackMax: Optional[float]
    VmMaxMapCount: Optional[float]
    VmSwappiness: Optional[float]
    VmVfsCachePressure: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SysctlConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SysctlConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            FsAioMaxNr=json_data.get("FsAioMaxNr"),
            FsFileMax=json_data.get("FsFileMax"),
            FsInotifyMaxUserWatches=json_data.get("FsInotifyMaxUserWatches"),
            FsNrOpen=json_data.get("FsNrOpen"),
            KernelThreadsMax=json_data.get("KernelThreadsMax"),
            NetCoreNetdevMaxBacklog=json_data.get("NetCoreNetdevMaxBacklog"),
            NetCoreOptmemMax=json_data.get("NetCoreOptmemMax"),
            NetCoreRmemDefault=json_data.get("NetCoreRmemDefault"),
            NetCoreRmemMax=json_data.get("NetCoreRmemMax"),
            NetCoreSomaxconn=json_data.get("NetCoreSomaxconn"),
            NetCoreWmemDefault=json_data.get("NetCoreWmemDefault"),
            NetCoreWmemMax=json_data.get("NetCoreWmemMax"),
            NetIpv4IpLocalPortRangeMax=json_data.get("NetIpv4IpLocalPortRangeMax"),
            NetIpv4IpLocalPortRangeMin=json_data.get("NetIpv4IpLocalPortRangeMin"),
            NetIpv4NeighDefaultGcThresh1=json_data.get("NetIpv4NeighDefaultGcThresh1"),
            NetIpv4NeighDefaultGcThresh2=json_data.get("NetIpv4NeighDefaultGcThresh2"),
            NetIpv4NeighDefaultGcThresh3=json_data.get("NetIpv4NeighDefaultGcThresh3"),
            NetIpv4TcpFinTimeout=json_data.get("NetIpv4TcpFinTimeout"),
            NetIpv4TcpKeepaliveIntvl=json_data.get("NetIpv4TcpKeepaliveIntvl"),
            NetIpv4TcpKeepaliveProbes=json_data.get("NetIpv4TcpKeepaliveProbes"),
            NetIpv4TcpKeepaliveTime=json_data.get("NetIpv4TcpKeepaliveTime"),
            NetIpv4TcpMaxSynBacklog=json_data.get("NetIpv4TcpMaxSynBacklog"),
            NetIpv4TcpMaxTwBuckets=json_data.get("NetIpv4TcpMaxTwBuckets"),
            NetIpv4TcpTwReuse=json_data.get("NetIpv4TcpTwReuse"),
            NetNetfilterNfConntrackBuckets=json_data.get("NetNetfilterNfConntrackBuckets"),
            NetNetfilterNfConntrackMax=json_data.get("NetNetfilterNfConntrackMax"),
            VmMaxMapCount=json_data.get("VmMaxMapCount"),
            VmSwappiness=json_data.get("VmSwappiness"),
            VmVfsCachePressure=json_data.get("VmVfsCachePressure"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SysctlConfigDefinition = SysctlConfigDefinition


@dataclass
class UpgradeSettingsDefinition(BaseModel):
    MaxSurge: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UpgradeSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpgradeSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxSurge=json_data.get("MaxSurge"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpgradeSettingsDefinition = UpgradeSettingsDefinition


@dataclass
class IdentityDefinition(BaseModel):
    Type: Optional[str]
    UserAssignedIdentityId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            UserAssignedIdentityId=json_data.get("UserAssignedIdentityId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityDefinition = IdentityDefinition


@dataclass
class KubeletIdentityDefinition(BaseModel):
    ClientId: Optional[str]
    ObjectId: Optional[str]
    UserAssignedIdentityId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubeletIdentityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeletIdentityDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            ObjectId=json_data.get("ObjectId"),
            UserAssignedIdentityId=json_data.get("UserAssignedIdentityId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeletIdentityDefinition = KubeletIdentityDefinition


@dataclass
class LinuxProfileDefinition(BaseModel):
    AdminUsername: Optional[str]
    SshKey: Optional[Sequence["_SshKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LinuxProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinuxProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminUsername=json_data.get("AdminUsername"),
            SshKey=deserialize_list(json_data.get("SshKey"), SshKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinuxProfileDefinition = LinuxProfileDefinition


@dataclass
class SshKeyDefinition(BaseModel):
    KeyData: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SshKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SshKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyData=json_data.get("KeyData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SshKeyDefinition = SshKeyDefinition


@dataclass
class NetworkProfileDefinition(BaseModel):
    DnsServiceIp: Optional[str]
    DockerBridgeCidr: Optional[str]
    LoadBalancerSku: Optional[str]
    NetworkMode: Optional[str]
    NetworkPlugin: Optional[str]
    NetworkPolicy: Optional[str]
    OutboundType: Optional[str]
    PodCidr: Optional[str]
    ServiceCidr: Optional[str]
    LoadBalancerProfile: Optional[Sequence["_LoadBalancerProfileDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsServiceIp=json_data.get("DnsServiceIp"),
            DockerBridgeCidr=json_data.get("DockerBridgeCidr"),
            LoadBalancerSku=json_data.get("LoadBalancerSku"),
            NetworkMode=json_data.get("NetworkMode"),
            NetworkPlugin=json_data.get("NetworkPlugin"),
            NetworkPolicy=json_data.get("NetworkPolicy"),
            OutboundType=json_data.get("OutboundType"),
            PodCidr=json_data.get("PodCidr"),
            ServiceCidr=json_data.get("ServiceCidr"),
            LoadBalancerProfile=deserialize_list(json_data.get("LoadBalancerProfile"), LoadBalancerProfileDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkProfileDefinition = NetworkProfileDefinition


@dataclass
class LoadBalancerProfileDefinition(BaseModel):
    IdleTimeoutInMinutes: Optional[float]
    ManagedOutboundIpCount: Optional[float]
    OutboundIpAddressIds: Optional[Sequence[str]]
    OutboundIpPrefixIds: Optional[Sequence[str]]
    OutboundPortsAllocated: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancerProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancerProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            IdleTimeoutInMinutes=json_data.get("IdleTimeoutInMinutes"),
            ManagedOutboundIpCount=json_data.get("ManagedOutboundIpCount"),
            OutboundIpAddressIds=json_data.get("OutboundIpAddressIds"),
            OutboundIpPrefixIds=json_data.get("OutboundIpPrefixIds"),
            OutboundPortsAllocated=json_data.get("OutboundPortsAllocated"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancerProfileDefinition = LoadBalancerProfileDefinition


@dataclass
class RoleBasedAccessControlDefinition(BaseModel):
    Enabled: Optional[bool]
    AzureActiveDirectory: Optional[Sequence["_AzureActiveDirectoryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RoleBasedAccessControlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoleBasedAccessControlDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            AzureActiveDirectory=deserialize_list(json_data.get("AzureActiveDirectory"), AzureActiveDirectoryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoleBasedAccessControlDefinition = RoleBasedAccessControlDefinition


@dataclass
class AzureActiveDirectoryDefinition(BaseModel):
    AdminGroupObjectIds: Optional[Sequence[str]]
    AzureRbacEnabled: Optional[bool]
    ClientAppId: Optional[str]
    Managed: Optional[bool]
    ServerAppId: Optional[str]
    ServerAppSecret: Optional[str]
    TenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureActiveDirectoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureActiveDirectoryDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminGroupObjectIds=json_data.get("AdminGroupObjectIds"),
            AzureRbacEnabled=json_data.get("AzureRbacEnabled"),
            ClientAppId=json_data.get("ClientAppId"),
            Managed=json_data.get("Managed"),
            ServerAppId=json_data.get("ServerAppId"),
            ServerAppSecret=json_data.get("ServerAppSecret"),
            TenantId=json_data.get("TenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureActiveDirectoryDefinition = AzureActiveDirectoryDefinition


@dataclass
class ServicePrincipalDefinition(BaseModel):
    ClientId: Optional[str]
    ClientSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServicePrincipalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicePrincipalDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicePrincipalDefinition = ServicePrincipalDefinition


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


@dataclass
class WindowsProfileDefinition(BaseModel):
    AdminPassword: Optional[str]
    AdminUsername: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WindowsProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WindowsProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminPassword=json_data.get("AdminPassword"),
            AdminUsername=json_data.get("AdminUsername"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WindowsProfileDefinition = WindowsProfileDefinition


