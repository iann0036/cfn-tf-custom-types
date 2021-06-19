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
    ClusterIpv4Cidr: Optional[str]
    DatapathProvider: Optional[str]
    DefaultMaxPodsPerNode: Optional[float]
    Description: Optional[str]
    EnableAutopilot: Optional[bool]
    EnableBinaryAuthorization: Optional[bool]
    EnableIntranodeVisibility: Optional[bool]
    EnableKubernetesAlpha: Optional[bool]
    EnableL4IlbSubsetting: Optional[bool]
    EnableLegacyAbac: Optional[bool]
    EnableShieldedNodes: Optional[bool]
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
    NetworkingMode: Optional[str]
    NodeLocations: Optional[Sequence[str]]
    NodeVersion: Optional[str]
    Operation: Optional[str]
    PrivateIpv6GoogleAccess: Optional[str]
    Project: Optional[str]
    RemoveDefaultNodePool: Optional[bool]
    ResourceLabels: Optional[Sequence["_ResourceLabelsDefinition"]]
    SelfLink: Optional[str]
    ServicesIpv4Cidr: Optional[str]
    Subnetwork: Optional[str]
    TpuIpv4CidrBlock: Optional[str]
    AddonsConfig: Optional[Sequence["_AddonsConfigDefinition"]]
    AuthenticatorGroupsConfig: Optional[Sequence["_AuthenticatorGroupsConfigDefinition"]]
    ClusterAutoscaling: Optional[Sequence["_ClusterAutoscalingDefinition"]]
    ClusterTelemetry: Optional[Sequence["_ClusterTelemetryDefinition"]]
    ConfidentialNodes: Optional[Sequence["_ConfidentialNodesDefinition"]]
    DatabaseEncryption: Optional[Sequence["_DatabaseEncryptionDefinition"]]
    DefaultSnatStatus: Optional[Sequence["_DefaultSnatStatusDefinition"]]
    IpAllocationPolicy: Optional[Sequence["_IpAllocationPolicyDefinition"]]
    MaintenancePolicy: Optional[Sequence["_MaintenancePolicyDefinition"]]
    MasterAuth: Optional[Sequence["_MasterAuthDefinition"]]
    MasterAuthorizedNetworksConfig: Optional[Sequence["_MasterAuthorizedNetworksConfigDefinition"]]
    NetworkPolicy: Optional[Sequence["_NetworkPolicyDefinition"]]
    NodeConfig: Optional[Sequence["_NodeConfigDefinition"]]
    NodePool: Optional[Sequence["_NodePoolDefinition"]]
    NotificationConfig: Optional[Sequence["_NotificationConfigDefinition"]]
    PodSecurityPolicyConfig: Optional[Sequence["_PodSecurityPolicyConfigDefinition"]]
    PrivateClusterConfig: Optional[Sequence["_PrivateClusterConfigDefinition"]]
    ReleaseChannel: Optional[Sequence["_ReleaseChannelDefinition"]]
    ResourceUsageExportConfig: Optional[Sequence["_ResourceUsageExportConfigDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    VerticalPodAutoscaling: Optional[Sequence["_VerticalPodAutoscalingDefinition"]]
    WorkloadIdentityConfig: Optional[Sequence["_WorkloadIdentityConfigDefinition"]]

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
            ClusterIpv4Cidr=json_data.get("ClusterIpv4Cidr"),
            DatapathProvider=json_data.get("DatapathProvider"),
            DefaultMaxPodsPerNode=json_data.get("DefaultMaxPodsPerNode"),
            Description=json_data.get("Description"),
            EnableAutopilot=json_data.get("EnableAutopilot"),
            EnableBinaryAuthorization=json_data.get("EnableBinaryAuthorization"),
            EnableIntranodeVisibility=json_data.get("EnableIntranodeVisibility"),
            EnableKubernetesAlpha=json_data.get("EnableKubernetesAlpha"),
            EnableL4IlbSubsetting=json_data.get("EnableL4IlbSubsetting"),
            EnableLegacyAbac=json_data.get("EnableLegacyAbac"),
            EnableShieldedNodes=json_data.get("EnableShieldedNodes"),
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
            NetworkingMode=json_data.get("NetworkingMode"),
            NodeLocations=json_data.get("NodeLocations"),
            NodeVersion=json_data.get("NodeVersion"),
            Operation=json_data.get("Operation"),
            PrivateIpv6GoogleAccess=json_data.get("PrivateIpv6GoogleAccess"),
            Project=json_data.get("Project"),
            RemoveDefaultNodePool=json_data.get("RemoveDefaultNodePool"),
            ResourceLabels=deserialize_list(json_data.get("ResourceLabels"), ResourceLabelsDefinition),
            SelfLink=json_data.get("SelfLink"),
            ServicesIpv4Cidr=json_data.get("ServicesIpv4Cidr"),
            Subnetwork=json_data.get("Subnetwork"),
            TpuIpv4CidrBlock=json_data.get("TpuIpv4CidrBlock"),
            AddonsConfig=deserialize_list(json_data.get("AddonsConfig"), AddonsConfigDefinition),
            AuthenticatorGroupsConfig=deserialize_list(json_data.get("AuthenticatorGroupsConfig"), AuthenticatorGroupsConfigDefinition),
            ClusterAutoscaling=deserialize_list(json_data.get("ClusterAutoscaling"), ClusterAutoscalingDefinition),
            ClusterTelemetry=deserialize_list(json_data.get("ClusterTelemetry"), ClusterTelemetryDefinition),
            ConfidentialNodes=deserialize_list(json_data.get("ConfidentialNodes"), ConfidentialNodesDefinition),
            DatabaseEncryption=deserialize_list(json_data.get("DatabaseEncryption"), DatabaseEncryptionDefinition),
            DefaultSnatStatus=deserialize_list(json_data.get("DefaultSnatStatus"), DefaultSnatStatusDefinition),
            IpAllocationPolicy=deserialize_list(json_data.get("IpAllocationPolicy"), IpAllocationPolicyDefinition),
            MaintenancePolicy=deserialize_list(json_data.get("MaintenancePolicy"), MaintenancePolicyDefinition),
            MasterAuth=deserialize_list(json_data.get("MasterAuth"), MasterAuthDefinition),
            MasterAuthorizedNetworksConfig=deserialize_list(json_data.get("MasterAuthorizedNetworksConfig"), MasterAuthorizedNetworksConfigDefinition),
            NetworkPolicy=deserialize_list(json_data.get("NetworkPolicy"), NetworkPolicyDefinition),
            NodeConfig=deserialize_list(json_data.get("NodeConfig"), NodeConfigDefinition),
            NodePool=deserialize_list(json_data.get("NodePool"), NodePoolDefinition),
            NotificationConfig=deserialize_list(json_data.get("NotificationConfig"), NotificationConfigDefinition),
            PodSecurityPolicyConfig=deserialize_list(json_data.get("PodSecurityPolicyConfig"), PodSecurityPolicyConfigDefinition),
            PrivateClusterConfig=deserialize_list(json_data.get("PrivateClusterConfig"), PrivateClusterConfigDefinition),
            ReleaseChannel=deserialize_list(json_data.get("ReleaseChannel"), ReleaseChannelDefinition),
            ResourceUsageExportConfig=deserialize_list(json_data.get("ResourceUsageExportConfig"), ResourceUsageExportConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VerticalPodAutoscaling=deserialize_list(json_data.get("VerticalPodAutoscaling"), VerticalPodAutoscalingDefinition),
            WorkloadIdentityConfig=deserialize_list(json_data.get("WorkloadIdentityConfig"), WorkloadIdentityConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ResourceLabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceLabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceLabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceLabelsDefinition = ResourceLabelsDefinition


@dataclass
class AddonsConfigDefinition(BaseModel):
    CloudrunConfig: Optional[Sequence["_CloudrunConfigDefinition"]]
    ConfigConnectorConfig: Optional[Sequence["_ConfigConnectorConfigDefinition"]]
    DnsCacheConfig: Optional[Sequence["_DnsCacheConfigDefinition"]]
    GcePersistentDiskCsiDriverConfig: Optional[Sequence["_GcePersistentDiskCsiDriverConfigDefinition"]]
    HorizontalPodAutoscaling: Optional[Sequence["_HorizontalPodAutoscalingDefinition"]]
    HttpLoadBalancing: Optional[Sequence["_HttpLoadBalancingDefinition"]]
    IstioConfig: Optional[Sequence["_IstioConfigDefinition"]]
    KalmConfig: Optional[Sequence["_KalmConfigDefinition"]]
    NetworkPolicyConfig: Optional[Sequence["_NetworkPolicyConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AddonsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddonsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudrunConfig=deserialize_list(json_data.get("CloudrunConfig"), CloudrunConfigDefinition),
            ConfigConnectorConfig=deserialize_list(json_data.get("ConfigConnectorConfig"), ConfigConnectorConfigDefinition),
            DnsCacheConfig=deserialize_list(json_data.get("DnsCacheConfig"), DnsCacheConfigDefinition),
            GcePersistentDiskCsiDriverConfig=deserialize_list(json_data.get("GcePersistentDiskCsiDriverConfig"), GcePersistentDiskCsiDriverConfigDefinition),
            HorizontalPodAutoscaling=deserialize_list(json_data.get("HorizontalPodAutoscaling"), HorizontalPodAutoscalingDefinition),
            HttpLoadBalancing=deserialize_list(json_data.get("HttpLoadBalancing"), HttpLoadBalancingDefinition),
            IstioConfig=deserialize_list(json_data.get("IstioConfig"), IstioConfigDefinition),
            KalmConfig=deserialize_list(json_data.get("KalmConfig"), KalmConfigDefinition),
            NetworkPolicyConfig=deserialize_list(json_data.get("NetworkPolicyConfig"), NetworkPolicyConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddonsConfigDefinition = AddonsConfigDefinition


@dataclass
class CloudrunConfigDefinition(BaseModel):
    Disabled: Optional[bool]
    LoadBalancerType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudrunConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudrunConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Disabled=json_data.get("Disabled"),
            LoadBalancerType=json_data.get("LoadBalancerType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudrunConfigDefinition = CloudrunConfigDefinition


@dataclass
class ConfigConnectorConfigDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigConnectorConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigConnectorConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigConnectorConfigDefinition = ConfigConnectorConfigDefinition


@dataclass
class DnsCacheConfigDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DnsCacheConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsCacheConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsCacheConfigDefinition = DnsCacheConfigDefinition


@dataclass
class GcePersistentDiskCsiDriverConfigDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GcePersistentDiskCsiDriverConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcePersistentDiskCsiDriverConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcePersistentDiskCsiDriverConfigDefinition = GcePersistentDiskCsiDriverConfigDefinition


@dataclass
class HorizontalPodAutoscalingDefinition(BaseModel):
    Disabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_HorizontalPodAutoscalingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HorizontalPodAutoscalingDefinition"]:
        if not json_data:
            return None
        return cls(
            Disabled=json_data.get("Disabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HorizontalPodAutoscalingDefinition = HorizontalPodAutoscalingDefinition


@dataclass
class HttpLoadBalancingDefinition(BaseModel):
    Disabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_HttpLoadBalancingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpLoadBalancingDefinition"]:
        if not json_data:
            return None
        return cls(
            Disabled=json_data.get("Disabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpLoadBalancingDefinition = HttpLoadBalancingDefinition


@dataclass
class IstioConfigDefinition(BaseModel):
    Auth: Optional[str]
    Disabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_IstioConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IstioConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Auth=json_data.get("Auth"),
            Disabled=json_data.get("Disabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IstioConfigDefinition = IstioConfigDefinition


@dataclass
class KalmConfigDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_KalmConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KalmConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KalmConfigDefinition = KalmConfigDefinition


@dataclass
class NetworkPolicyConfigDefinition(BaseModel):
    Disabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkPolicyConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkPolicyConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Disabled=json_data.get("Disabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkPolicyConfigDefinition = NetworkPolicyConfigDefinition


@dataclass
class AuthenticatorGroupsConfigDefinition(BaseModel):
    SecurityGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticatorGroupsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticatorGroupsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            SecurityGroup=json_data.get("SecurityGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticatorGroupsConfigDefinition = AuthenticatorGroupsConfigDefinition


@dataclass
class ClusterAutoscalingDefinition(BaseModel):
    AutoscalingProfile: Optional[str]
    Enabled: Optional[bool]
    AutoProvisioningDefaults: Optional[Sequence["_AutoProvisioningDefaultsDefinition"]]
    ResourceLimits: Optional[Sequence["_ResourceLimitsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterAutoscalingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterAutoscalingDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoscalingProfile=json_data.get("AutoscalingProfile"),
            Enabled=json_data.get("Enabled"),
            AutoProvisioningDefaults=deserialize_list(json_data.get("AutoProvisioningDefaults"), AutoProvisioningDefaultsDefinition),
            ResourceLimits=deserialize_list(json_data.get("ResourceLimits"), ResourceLimitsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterAutoscalingDefinition = ClusterAutoscalingDefinition


@dataclass
class AutoProvisioningDefaultsDefinition(BaseModel):
    MinCpuPlatform: Optional[str]
    OauthScopes: Optional[Sequence[str]]
    ServiceAccount: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoProvisioningDefaultsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoProvisioningDefaultsDefinition"]:
        if not json_data:
            return None
        return cls(
            MinCpuPlatform=json_data.get("MinCpuPlatform"),
            OauthScopes=json_data.get("OauthScopes"),
            ServiceAccount=json_data.get("ServiceAccount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoProvisioningDefaultsDefinition = AutoProvisioningDefaultsDefinition


@dataclass
class ResourceLimitsDefinition(BaseModel):
    Maximum: Optional[float]
    Minimum: Optional[float]
    ResourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            Maximum=json_data.get("Maximum"),
            Minimum=json_data.get("Minimum"),
            ResourceType=json_data.get("ResourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceLimitsDefinition = ResourceLimitsDefinition


@dataclass
class ClusterTelemetryDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterTelemetryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterTelemetryDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterTelemetryDefinition = ClusterTelemetryDefinition


@dataclass
class ConfidentialNodesDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConfidentialNodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfidentialNodesDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfidentialNodesDefinition = ConfidentialNodesDefinition


@dataclass
class DatabaseEncryptionDefinition(BaseModel):
    KeyName: Optional[str]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseEncryptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseEncryptionDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyName=json_data.get("KeyName"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseEncryptionDefinition = DatabaseEncryptionDefinition


@dataclass
class DefaultSnatStatusDefinition(BaseModel):
    Disabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultSnatStatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultSnatStatusDefinition"]:
        if not json_data:
            return None
        return cls(
            Disabled=json_data.get("Disabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultSnatStatusDefinition = DefaultSnatStatusDefinition


@dataclass
class IpAllocationPolicyDefinition(BaseModel):
    ClusterIpv4CidrBlock: Optional[str]
    ClusterSecondaryRangeName: Optional[str]
    ServicesIpv4CidrBlock: Optional[str]
    ServicesSecondaryRangeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAllocationPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAllocationPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterIpv4CidrBlock=json_data.get("ClusterIpv4CidrBlock"),
            ClusterSecondaryRangeName=json_data.get("ClusterSecondaryRangeName"),
            ServicesIpv4CidrBlock=json_data.get("ServicesIpv4CidrBlock"),
            ServicesSecondaryRangeName=json_data.get("ServicesSecondaryRangeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAllocationPolicyDefinition = IpAllocationPolicyDefinition


@dataclass
class MaintenancePolicyDefinition(BaseModel):
    DailyMaintenanceWindow: Optional[Sequence["_DailyMaintenanceWindowDefinition"]]
    MaintenanceExclusion: Optional[Sequence["_MaintenanceExclusionDefinition"]]
    RecurringWindow: Optional[Sequence["_RecurringWindowDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenancePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenancePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            DailyMaintenanceWindow=deserialize_list(json_data.get("DailyMaintenanceWindow"), DailyMaintenanceWindowDefinition),
            MaintenanceExclusion=deserialize_list(json_data.get("MaintenanceExclusion"), MaintenanceExclusionDefinition),
            RecurringWindow=deserialize_list(json_data.get("RecurringWindow"), RecurringWindowDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenancePolicyDefinition = MaintenancePolicyDefinition


@dataclass
class DailyMaintenanceWindowDefinition(BaseModel):
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DailyMaintenanceWindowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DailyMaintenanceWindowDefinition"]:
        if not json_data:
            return None
        return cls(
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DailyMaintenanceWindowDefinition = DailyMaintenanceWindowDefinition


@dataclass
class MaintenanceExclusionDefinition(BaseModel):
    EndTime: Optional[str]
    ExclusionName: Optional[str]
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceExclusionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceExclusionDefinition"]:
        if not json_data:
            return None
        return cls(
            EndTime=json_data.get("EndTime"),
            ExclusionName=json_data.get("ExclusionName"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceExclusionDefinition = MaintenanceExclusionDefinition


@dataclass
class RecurringWindowDefinition(BaseModel):
    EndTime: Optional[str]
    Recurrence: Optional[str]
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecurringWindowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecurringWindowDefinition"]:
        if not json_data:
            return None
        return cls(
            EndTime=json_data.get("EndTime"),
            Recurrence=json_data.get("Recurrence"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecurringWindowDefinition = RecurringWindowDefinition


@dataclass
class MasterAuthDefinition(BaseModel):
    Password: Optional[str]
    Username: Optional[str]
    ClientCertificateConfig: Optional[Sequence["_ClientCertificateConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MasterAuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterAuthDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
            ClientCertificateConfig=deserialize_list(json_data.get("ClientCertificateConfig"), ClientCertificateConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterAuthDefinition = MasterAuthDefinition


@dataclass
class ClientCertificateConfigDefinition(BaseModel):
    IssueClientCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ClientCertificateConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientCertificateConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            IssueClientCertificate=json_data.get("IssueClientCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientCertificateConfigDefinition = ClientCertificateConfigDefinition


@dataclass
class MasterAuthorizedNetworksConfigDefinition(BaseModel):
    CidrBlocks: Optional[Sequence["_CidrBlocksDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MasterAuthorizedNetworksConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterAuthorizedNetworksConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CidrBlocks=deserialize_list(json_data.get("CidrBlocks"), CidrBlocksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterAuthorizedNetworksConfigDefinition = MasterAuthorizedNetworksConfigDefinition


@dataclass
class CidrBlocksDefinition(BaseModel):
    CidrBlock: Optional[str]
    DisplayName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CidrBlocksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CidrBlocksDefinition"]:
        if not json_data:
            return None
        return cls(
            CidrBlock=json_data.get("CidrBlock"),
            DisplayName=json_data.get("DisplayName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CidrBlocksDefinition = CidrBlocksDefinition


@dataclass
class NetworkPolicyDefinition(BaseModel):
    Enabled: Optional[bool]
    Provider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Provider=json_data.get("Provider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkPolicyDefinition = NetworkPolicyDefinition


@dataclass
class NodeConfigDefinition(BaseModel):
    BootDiskKmsKey: Optional[str]
    DiskSizeGb: Optional[float]
    DiskType: Optional[str]
    GuestAccelerator: Optional[Sequence["_GuestAcceleratorDefinition2"]]
    ImageType: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition2"]]
    LocalSsdCount: Optional[float]
    MachineType: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition2"]]
    MinCpuPlatform: Optional[str]
    OauthScopes: Optional[Sequence[str]]
    Preemptible: Optional[bool]
    ServiceAccount: Optional[str]
    Tags: Optional[Sequence[str]]
    Taint: Optional[Sequence["_TaintDefinition2"]]
    EphemeralStorageConfig: Optional[Sequence["_EphemeralStorageConfigDefinition"]]
    KubeletConfig: Optional[Sequence["_KubeletConfigDefinition"]]
    LinuxNodeConfig: Optional[Sequence["_LinuxNodeConfigDefinition"]]
    SandboxConfig: Optional[Sequence["_SandboxConfigDefinition"]]
    ShieldedInstanceConfig: Optional[Sequence["_ShieldedInstanceConfigDefinition"]]
    WorkloadMetadataConfig: Optional[Sequence["_WorkloadMetadataConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BootDiskKmsKey=json_data.get("BootDiskKmsKey"),
            DiskSizeGb=json_data.get("DiskSizeGb"),
            DiskType=json_data.get("DiskType"),
            GuestAccelerator=deserialize_list(json_data.get("GuestAccelerator"), GuestAcceleratorDefinition2),
            ImageType=json_data.get("ImageType"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition2),
            LocalSsdCount=json_data.get("LocalSsdCount"),
            MachineType=json_data.get("MachineType"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition2),
            MinCpuPlatform=json_data.get("MinCpuPlatform"),
            OauthScopes=json_data.get("OauthScopes"),
            Preemptible=json_data.get("Preemptible"),
            ServiceAccount=json_data.get("ServiceAccount"),
            Tags=json_data.get("Tags"),
            Taint=deserialize_list(json_data.get("Taint"), TaintDefinition2),
            EphemeralStorageConfig=deserialize_list(json_data.get("EphemeralStorageConfig"), EphemeralStorageConfigDefinition),
            KubeletConfig=deserialize_list(json_data.get("KubeletConfig"), KubeletConfigDefinition),
            LinuxNodeConfig=deserialize_list(json_data.get("LinuxNodeConfig"), LinuxNodeConfigDefinition),
            SandboxConfig=deserialize_list(json_data.get("SandboxConfig"), SandboxConfigDefinition),
            ShieldedInstanceConfig=deserialize_list(json_data.get("ShieldedInstanceConfig"), ShieldedInstanceConfigDefinition),
            WorkloadMetadataConfig=deserialize_list(json_data.get("WorkloadMetadataConfig"), WorkloadMetadataConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeConfigDefinition = NodeConfigDefinition


@dataclass
class GuestAcceleratorDefinition2(BaseModel):
    Count: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestAcceleratorDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestAcceleratorDefinition2"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestAcceleratorDefinition2 = GuestAcceleratorDefinition2


@dataclass
class LabelsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition2 = LabelsDefinition2


@dataclass
class MetadataDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition2 = MetadataDefinition2


@dataclass
class TaintDefinition2(BaseModel):
    Effect: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaintDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaintDefinition2"]:
        if not json_data:
            return None
        return cls(
            Effect=json_data.get("Effect"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaintDefinition2 = TaintDefinition2


@dataclass
class EphemeralStorageConfigDefinition(BaseModel):
    LocalSsdCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EphemeralStorageConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EphemeralStorageConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            LocalSsdCount=json_data.get("LocalSsdCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EphemeralStorageConfigDefinition = EphemeralStorageConfigDefinition


@dataclass
class KubeletConfigDefinition(BaseModel):
    CpuCfsQuota: Optional[bool]
    CpuCfsQuotaPeriod: Optional[str]
    CpuManagerPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubeletConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeletConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CpuCfsQuota=json_data.get("CpuCfsQuota"),
            CpuCfsQuotaPeriod=json_data.get("CpuCfsQuotaPeriod"),
            CpuManagerPolicy=json_data.get("CpuManagerPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeletConfigDefinition = KubeletConfigDefinition


@dataclass
class LinuxNodeConfigDefinition(BaseModel):
    Sysctls: Optional[Sequence["_SysctlsDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_LinuxNodeConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinuxNodeConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Sysctls=deserialize_list(json_data.get("Sysctls"), SysctlsDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinuxNodeConfigDefinition = LinuxNodeConfigDefinition


@dataclass
class SysctlsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SysctlsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SysctlsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SysctlsDefinition2 = SysctlsDefinition2


@dataclass
class SandboxConfigDefinition(BaseModel):
    SandboxType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SandboxConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SandboxConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            SandboxType=json_data.get("SandboxType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SandboxConfigDefinition = SandboxConfigDefinition


@dataclass
class ShieldedInstanceConfigDefinition(BaseModel):
    EnableIntegrityMonitoring: Optional[bool]
    EnableSecureBoot: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ShieldedInstanceConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShieldedInstanceConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableIntegrityMonitoring=json_data.get("EnableIntegrityMonitoring"),
            EnableSecureBoot=json_data.get("EnableSecureBoot"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShieldedInstanceConfigDefinition = ShieldedInstanceConfigDefinition


@dataclass
class WorkloadMetadataConfigDefinition(BaseModel):
    NodeMetadata: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkloadMetadataConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkloadMetadataConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            NodeMetadata=json_data.get("NodeMetadata"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkloadMetadataConfigDefinition = WorkloadMetadataConfigDefinition


@dataclass
class NodePoolDefinition(BaseModel):
    InitialNodeCount: Optional[float]
    MaxPodsPerNode: Optional[float]
    Name: Optional[str]
    NamePrefix: Optional[str]
    NodeCount: Optional[float]
    NodeLocations: Optional[Sequence[str]]
    Version: Optional[str]
    Autoscaling: Optional[Sequence["_AutoscalingDefinition"]]
    Management: Optional[Sequence["_ManagementDefinition"]]
    NodeConfig: Optional[Sequence["_NodeConfigDefinition"]]
    UpgradeSettings: Optional[Sequence["_UpgradeSettingsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodePoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodePoolDefinition"]:
        if not json_data:
            return None
        return cls(
            InitialNodeCount=json_data.get("InitialNodeCount"),
            MaxPodsPerNode=json_data.get("MaxPodsPerNode"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            NodeCount=json_data.get("NodeCount"),
            NodeLocations=json_data.get("NodeLocations"),
            Version=json_data.get("Version"),
            Autoscaling=deserialize_list(json_data.get("Autoscaling"), AutoscalingDefinition),
            Management=deserialize_list(json_data.get("Management"), ManagementDefinition),
            NodeConfig=deserialize_list(json_data.get("NodeConfig"), NodeConfigDefinition),
            UpgradeSettings=deserialize_list(json_data.get("UpgradeSettings"), UpgradeSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodePoolDefinition = NodePoolDefinition


@dataclass
class AutoscalingDefinition(BaseModel):
    MaxNodeCount: Optional[float]
    MinNodeCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscalingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscalingDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxNodeCount=json_data.get("MaxNodeCount"),
            MinNodeCount=json_data.get("MinNodeCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscalingDefinition = AutoscalingDefinition


@dataclass
class ManagementDefinition(BaseModel):
    AutoRepair: Optional[bool]
    AutoUpgrade: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ManagementDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagementDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoRepair=json_data.get("AutoRepair"),
            AutoUpgrade=json_data.get("AutoUpgrade"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagementDefinition = ManagementDefinition


@dataclass
class UpgradeSettingsDefinition(BaseModel):
    MaxSurge: Optional[float]
    MaxUnavailable: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_UpgradeSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpgradeSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxSurge=json_data.get("MaxSurge"),
            MaxUnavailable=json_data.get("MaxUnavailable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpgradeSettingsDefinition = UpgradeSettingsDefinition


@dataclass
class NotificationConfigDefinition(BaseModel):
    Pubsub: Optional[Sequence["_PubsubDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Pubsub=deserialize_list(json_data.get("Pubsub"), PubsubDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationConfigDefinition = NotificationConfigDefinition


@dataclass
class PubsubDefinition(BaseModel):
    Enabled: Optional[bool]
    Topic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PubsubDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PubsubDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Topic=json_data.get("Topic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PubsubDefinition = PubsubDefinition


@dataclass
class PodSecurityPolicyConfigDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PodSecurityPolicyConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PodSecurityPolicyConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PodSecurityPolicyConfigDefinition = PodSecurityPolicyConfigDefinition


@dataclass
class PrivateClusterConfigDefinition(BaseModel):
    EnablePrivateEndpoint: Optional[bool]
    EnablePrivateNodes: Optional[bool]
    MasterIpv4CidrBlock: Optional[str]
    MasterGlobalAccessConfig: Optional[Sequence["_MasterGlobalAccessConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateClusterConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateClusterConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            EnablePrivateEndpoint=json_data.get("EnablePrivateEndpoint"),
            EnablePrivateNodes=json_data.get("EnablePrivateNodes"),
            MasterIpv4CidrBlock=json_data.get("MasterIpv4CidrBlock"),
            MasterGlobalAccessConfig=deserialize_list(json_data.get("MasterGlobalAccessConfig"), MasterGlobalAccessConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateClusterConfigDefinition = PrivateClusterConfigDefinition


@dataclass
class MasterGlobalAccessConfigDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_MasterGlobalAccessConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterGlobalAccessConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterGlobalAccessConfigDefinition = MasterGlobalAccessConfigDefinition


@dataclass
class ReleaseChannelDefinition(BaseModel):
    Channel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReleaseChannelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReleaseChannelDefinition"]:
        if not json_data:
            return None
        return cls(
            Channel=json_data.get("Channel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReleaseChannelDefinition = ReleaseChannelDefinition


@dataclass
class ResourceUsageExportConfigDefinition(BaseModel):
    EnableNetworkEgressMetering: Optional[bool]
    EnableResourceConsumptionMetering: Optional[bool]
    BigqueryDestination: Optional[Sequence["_BigqueryDestinationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceUsageExportConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceUsageExportConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableNetworkEgressMetering=json_data.get("EnableNetworkEgressMetering"),
            EnableResourceConsumptionMetering=json_data.get("EnableResourceConsumptionMetering"),
            BigqueryDestination=deserialize_list(json_data.get("BigqueryDestination"), BigqueryDestinationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceUsageExportConfigDefinition = ResourceUsageExportConfigDefinition


@dataclass
class BigqueryDestinationDefinition(BaseModel):
    DatasetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BigqueryDestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BigqueryDestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            DatasetId=json_data.get("DatasetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BigqueryDestinationDefinition = BigqueryDestinationDefinition


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
class VerticalPodAutoscalingDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_VerticalPodAutoscalingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VerticalPodAutoscalingDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VerticalPodAutoscalingDefinition = VerticalPodAutoscalingDefinition


@dataclass
class WorkloadIdentityConfigDefinition(BaseModel):
    IdentityNamespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkloadIdentityConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkloadIdentityConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            IdentityNamespace=json_data.get("IdentityNamespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkloadIdentityConfigDefinition = WorkloadIdentityConfigDefinition


