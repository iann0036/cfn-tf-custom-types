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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    DefaultRevisionId: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Members: Optional[Sequence["_MembersDefinition"]]
    TemplateRevisions: Optional[Sequence["_TemplateRevisionsDefinition"]]
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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            DefaultRevisionId=json_data.get("DefaultRevisionId"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Members=deserialize_list(json_data.get("Members"), MembersDefinition),
            TemplateRevisions=deserialize_list(json_data.get("TemplateRevisions"), TemplateRevisionsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class MembersDefinition(BaseModel):
    AccessType: Optional[str]
    GroupPrincipalId: Optional[str]
    UserPrincipalId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MembersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MembersDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessType=json_data.get("AccessType"),
            GroupPrincipalId=json_data.get("GroupPrincipalId"),
            UserPrincipalId=json_data.get("UserPrincipalId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MembersDefinition = MembersDefinition


@dataclass
class TemplateRevisionsDefinition(BaseModel):
    Annotations: Optional[Sequence["_AnnotationsDefinition2"]]
    Default: Optional[bool]
    Enabled: Optional[bool]
    Labels: Optional[Sequence["_LabelsDefinition2"]]
    Name: Optional[str]
    ClusterConfig: Optional[Sequence["_ClusterConfigDefinition"]]
    Questions: Optional[Sequence["_QuestionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateRevisionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateRevisionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition2),
            Default=json_data.get("Default"),
            Enabled=json_data.get("Enabled"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition2),
            Name=json_data.get("Name"),
            ClusterConfig=deserialize_list(json_data.get("ClusterConfig"), ClusterConfigDefinition),
            Questions=deserialize_list(json_data.get("Questions"), QuestionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateRevisionsDefinition = TemplateRevisionsDefinition


@dataclass
class AnnotationsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition2 = AnnotationsDefinition2


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
class ClusterConfigDefinition(BaseModel):
    DefaultClusterRoleForProjectMembers: Optional[str]
    DefaultPodSecurityPolicyTemplateId: Optional[str]
    DesiredAgentImage: Optional[str]
    DesiredAuthImage: Optional[str]
    DockerRootDir: Optional[str]
    EnableClusterAlerting: Optional[bool]
    EnableClusterMonitoring: Optional[bool]
    EnableNetworkPolicy: Optional[bool]
    WindowsPreferedCluster: Optional[bool]
    ClusterAuthEndpoint: Optional[Sequence["_ClusterAuthEndpointDefinition"]]
    RkeConfig: Optional[Sequence["_RkeConfigDefinition"]]
    ScheduledClusterScan: Optional[Sequence["_ScheduledClusterScanDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultClusterRoleForProjectMembers=json_data.get("DefaultClusterRoleForProjectMembers"),
            DefaultPodSecurityPolicyTemplateId=json_data.get("DefaultPodSecurityPolicyTemplateId"),
            DesiredAgentImage=json_data.get("DesiredAgentImage"),
            DesiredAuthImage=json_data.get("DesiredAuthImage"),
            DockerRootDir=json_data.get("DockerRootDir"),
            EnableClusterAlerting=json_data.get("EnableClusterAlerting"),
            EnableClusterMonitoring=json_data.get("EnableClusterMonitoring"),
            EnableNetworkPolicy=json_data.get("EnableNetworkPolicy"),
            WindowsPreferedCluster=json_data.get("WindowsPreferedCluster"),
            ClusterAuthEndpoint=deserialize_list(json_data.get("ClusterAuthEndpoint"), ClusterAuthEndpointDefinition),
            RkeConfig=deserialize_list(json_data.get("RkeConfig"), RkeConfigDefinition),
            ScheduledClusterScan=deserialize_list(json_data.get("ScheduledClusterScan"), ScheduledClusterScanDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterConfigDefinition = ClusterConfigDefinition


@dataclass
class ClusterAuthEndpointDefinition(BaseModel):
    CaCerts: Optional[str]
    Enabled: Optional[bool]
    Fqdn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterAuthEndpointDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterAuthEndpointDefinition"]:
        if not json_data:
            return None
        return cls(
            CaCerts=json_data.get("CaCerts"),
            Enabled=json_data.get("Enabled"),
            Fqdn=json_data.get("Fqdn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterAuthEndpointDefinition = ClusterAuthEndpointDefinition


@dataclass
class RkeConfigDefinition(BaseModel):
    AddonJobTimeout: Optional[float]
    Addons: Optional[str]
    AddonsInclude: Optional[Sequence[str]]
    IgnoreDockerVersion: Optional[bool]
    KubernetesVersion: Optional[str]
    PrefixPath: Optional[str]
    SshAgentAuth: Optional[bool]
    SshCertPath: Optional[str]
    SshKeyPath: Optional[str]
    WinPrefixPath: Optional[str]
    Authentication: Optional[Sequence["_AuthenticationDefinition"]]
    Authorization: Optional[Sequence["_AuthorizationDefinition"]]
    BastionHost: Optional[Sequence["_BastionHostDefinition"]]
    CloudProvider: Optional[Sequence["_CloudProviderDefinition"]]
    Dns: Optional[Sequence["_DnsDefinition"]]
    Ingress: Optional[Sequence["_IngressDefinition"]]
    Monitoring: Optional[Sequence["_MonitoringDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
    Nodes: Optional[Sequence["_NodesDefinition"]]
    PrivateRegistries: Optional[Sequence["_PrivateRegistriesDefinition"]]
    Services: Optional[Sequence["_ServicesDefinition"]]
    UpgradeStrategy: Optional[Sequence["_UpgradeStrategyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RkeConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RkeConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AddonJobTimeout=json_data.get("AddonJobTimeout"),
            Addons=json_data.get("Addons"),
            AddonsInclude=json_data.get("AddonsInclude"),
            IgnoreDockerVersion=json_data.get("IgnoreDockerVersion"),
            KubernetesVersion=json_data.get("KubernetesVersion"),
            PrefixPath=json_data.get("PrefixPath"),
            SshAgentAuth=json_data.get("SshAgentAuth"),
            SshCertPath=json_data.get("SshCertPath"),
            SshKeyPath=json_data.get("SshKeyPath"),
            WinPrefixPath=json_data.get("WinPrefixPath"),
            Authentication=deserialize_list(json_data.get("Authentication"), AuthenticationDefinition),
            Authorization=deserialize_list(json_data.get("Authorization"), AuthorizationDefinition),
            BastionHost=deserialize_list(json_data.get("BastionHost"), BastionHostDefinition),
            CloudProvider=deserialize_list(json_data.get("CloudProvider"), CloudProviderDefinition),
            Dns=deserialize_list(json_data.get("Dns"), DnsDefinition),
            Ingress=deserialize_list(json_data.get("Ingress"), IngressDefinition),
            Monitoring=deserialize_list(json_data.get("Monitoring"), MonitoringDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            Nodes=deserialize_list(json_data.get("Nodes"), NodesDefinition),
            PrivateRegistries=deserialize_list(json_data.get("PrivateRegistries"), PrivateRegistriesDefinition),
            Services=deserialize_list(json_data.get("Services"), ServicesDefinition),
            UpgradeStrategy=deserialize_list(json_data.get("UpgradeStrategy"), UpgradeStrategyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RkeConfigDefinition = RkeConfigDefinition


@dataclass
class AuthenticationDefinition(BaseModel):
    Sans: Optional[Sequence[str]]
    Strategy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationDefinition"]:
        if not json_data:
            return None
        return cls(
            Sans=json_data.get("Sans"),
            Strategy=json_data.get("Strategy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationDefinition = AuthenticationDefinition


@dataclass
class AuthorizationDefinition(BaseModel):
    Mode: Optional[str]
    Options: Optional[Sequence["_OptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthorizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthorizationDefinition"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            Options=deserialize_list(json_data.get("Options"), OptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthorizationDefinition = AuthorizationDefinition


@dataclass
class OptionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionsDefinition = OptionsDefinition


@dataclass
class BastionHostDefinition(BaseModel):
    Address: Optional[str]
    Port: Optional[str]
    SshAgentAuth: Optional[bool]
    SshKey: Optional[str]
    SshKeyPath: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BastionHostDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BastionHostDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Port=json_data.get("Port"),
            SshAgentAuth=json_data.get("SshAgentAuth"),
            SshKey=json_data.get("SshKey"),
            SshKeyPath=json_data.get("SshKeyPath"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BastionHostDefinition = BastionHostDefinition


@dataclass
class CloudProviderDefinition(BaseModel):
    CustomCloudProvider: Optional[str]
    Name: Optional[str]
    AwsCloudProvider: Optional[Sequence["_AwsCloudProviderDefinition"]]
    AzureCloudProvider: Optional[Sequence["_AzureCloudProviderDefinition"]]
    OpenstackCloudProvider: Optional[Sequence["_OpenstackCloudProviderDefinition"]]
    VsphereCloudProvider: Optional[Sequence["_VsphereCloudProviderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CloudProviderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudProviderDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomCloudProvider=json_data.get("CustomCloudProvider"),
            Name=json_data.get("Name"),
            AwsCloudProvider=deserialize_list(json_data.get("AwsCloudProvider"), AwsCloudProviderDefinition),
            AzureCloudProvider=deserialize_list(json_data.get("AzureCloudProvider"), AzureCloudProviderDefinition),
            OpenstackCloudProvider=deserialize_list(json_data.get("OpenstackCloudProvider"), OpenstackCloudProviderDefinition),
            VsphereCloudProvider=deserialize_list(json_data.get("VsphereCloudProvider"), VsphereCloudProviderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudProviderDefinition = CloudProviderDefinition


@dataclass
class AwsCloudProviderDefinition(BaseModel):
    Global: Optional[Sequence["_GlobalDefinition"]]
    ServiceOverride: Optional[Sequence["_ServiceOverrideDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudProviderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudProviderDefinition"]:
        if not json_data:
            return None
        return cls(
            Global=deserialize_list(json_data.get("Global"), GlobalDefinition),
            ServiceOverride=deserialize_list(json_data.get("ServiceOverride"), ServiceOverrideDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudProviderDefinition = AwsCloudProviderDefinition


@dataclass
class GlobalDefinition(BaseModel):
    Datacenters: Optional[str]
    InsecureFlag: Optional[bool]
    Password: Optional[str]
    Port: Optional[str]
    SoapRoundtripCount: Optional[float]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalDefinition"]:
        if not json_data:
            return None
        return cls(
            Datacenters=json_data.get("Datacenters"),
            InsecureFlag=json_data.get("InsecureFlag"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SoapRoundtripCount=json_data.get("SoapRoundtripCount"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalDefinition = GlobalDefinition


@dataclass
class ServiceOverrideDefinition(BaseModel):
    Region: Optional[str]
    Service: Optional[str]
    SigningMethod: Optional[str]
    SigningName: Optional[str]
    SigningRegion: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceOverrideDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceOverrideDefinition"]:
        if not json_data:
            return None
        return cls(
            Region=json_data.get("Region"),
            Service=json_data.get("Service"),
            SigningMethod=json_data.get("SigningMethod"),
            SigningName=json_data.get("SigningName"),
            SigningRegion=json_data.get("SigningRegion"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceOverrideDefinition = ServiceOverrideDefinition


@dataclass
class AzureCloudProviderDefinition(BaseModel):
    AadClientCertPassword: Optional[str]
    AadClientCertPath: Optional[str]
    AadClientId: Optional[str]
    AadClientSecret: Optional[str]
    Cloud: Optional[str]
    CloudProviderBackoff: Optional[bool]
    CloudProviderBackoffDuration: Optional[float]
    CloudProviderBackoffExponent: Optional[float]
    CloudProviderBackoffJitter: Optional[float]
    CloudProviderBackoffRetries: Optional[float]
    CloudProviderRateLimit: Optional[bool]
    CloudProviderRateLimitBucket: Optional[float]
    CloudProviderRateLimitQps: Optional[float]
    LoadBalancerSku: Optional[str]
    Location: Optional[str]
    MaximumLoadBalancerRuleCount: Optional[float]
    PrimaryAvailabilitySetName: Optional[str]
    PrimaryScaleSetName: Optional[str]
    ResourceGroup: Optional[str]
    RouteTableName: Optional[str]
    SecurityGroupName: Optional[str]
    SubnetName: Optional[str]
    SubscriptionId: Optional[str]
    TenantId: Optional[str]
    UseInstanceMetadata: Optional[bool]
    UseManagedIdentityExtension: Optional[bool]
    VmType: Optional[str]
    VnetName: Optional[str]
    VnetResourceGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureCloudProviderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureCloudProviderDefinition"]:
        if not json_data:
            return None
        return cls(
            AadClientCertPassword=json_data.get("AadClientCertPassword"),
            AadClientCertPath=json_data.get("AadClientCertPath"),
            AadClientId=json_data.get("AadClientId"),
            AadClientSecret=json_data.get("AadClientSecret"),
            Cloud=json_data.get("Cloud"),
            CloudProviderBackoff=json_data.get("CloudProviderBackoff"),
            CloudProviderBackoffDuration=json_data.get("CloudProviderBackoffDuration"),
            CloudProviderBackoffExponent=json_data.get("CloudProviderBackoffExponent"),
            CloudProviderBackoffJitter=json_data.get("CloudProviderBackoffJitter"),
            CloudProviderBackoffRetries=json_data.get("CloudProviderBackoffRetries"),
            CloudProviderRateLimit=json_data.get("CloudProviderRateLimit"),
            CloudProviderRateLimitBucket=json_data.get("CloudProviderRateLimitBucket"),
            CloudProviderRateLimitQps=json_data.get("CloudProviderRateLimitQps"),
            LoadBalancerSku=json_data.get("LoadBalancerSku"),
            Location=json_data.get("Location"),
            MaximumLoadBalancerRuleCount=json_data.get("MaximumLoadBalancerRuleCount"),
            PrimaryAvailabilitySetName=json_data.get("PrimaryAvailabilitySetName"),
            PrimaryScaleSetName=json_data.get("PrimaryScaleSetName"),
            ResourceGroup=json_data.get("ResourceGroup"),
            RouteTableName=json_data.get("RouteTableName"),
            SecurityGroupName=json_data.get("SecurityGroupName"),
            SubnetName=json_data.get("SubnetName"),
            SubscriptionId=json_data.get("SubscriptionId"),
            TenantId=json_data.get("TenantId"),
            UseInstanceMetadata=json_data.get("UseInstanceMetadata"),
            UseManagedIdentityExtension=json_data.get("UseManagedIdentityExtension"),
            VmType=json_data.get("VmType"),
            VnetName=json_data.get("VnetName"),
            VnetResourceGroup=json_data.get("VnetResourceGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureCloudProviderDefinition = AzureCloudProviderDefinition


@dataclass
class OpenstackCloudProviderDefinition(BaseModel):
    BlockStorage: Optional[Sequence["_BlockStorageDefinition"]]
    Global: Optional[Sequence["_GlobalDefinition"]]
    LoadBalancer: Optional[Sequence["_LoadBalancerDefinition"]]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Route: Optional[Sequence["_RouteDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OpenstackCloudProviderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenstackCloudProviderDefinition"]:
        if not json_data:
            return None
        return cls(
            BlockStorage=deserialize_list(json_data.get("BlockStorage"), BlockStorageDefinition),
            Global=deserialize_list(json_data.get("Global"), GlobalDefinition),
            LoadBalancer=deserialize_list(json_data.get("LoadBalancer"), LoadBalancerDefinition),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Route=deserialize_list(json_data.get("Route"), RouteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenstackCloudProviderDefinition = OpenstackCloudProviderDefinition


@dataclass
class BlockStorageDefinition(BaseModel):
    BsVersion: Optional[str]
    IgnoreVolumeAz: Optional[bool]
    TrustDevicePath: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_BlockStorageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockStorageDefinition"]:
        if not json_data:
            return None
        return cls(
            BsVersion=json_data.get("BsVersion"),
            IgnoreVolumeAz=json_data.get("IgnoreVolumeAz"),
            TrustDevicePath=json_data.get("TrustDevicePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockStorageDefinition = BlockStorageDefinition


@dataclass
class LoadBalancerDefinition(BaseModel):
    CreateMonitor: Optional[bool]
    FloatingNetworkId: Optional[str]
    LbMethod: Optional[str]
    LbProvider: Optional[str]
    LbVersion: Optional[str]
    ManageSecurityGroups: Optional[bool]
    MonitorDelay: Optional[str]
    MonitorMaxRetries: Optional[float]
    MonitorTimeout: Optional[str]
    SubnetId: Optional[str]
    UseOctavia: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancerDefinition"]:
        if not json_data:
            return None
        return cls(
            CreateMonitor=json_data.get("CreateMonitor"),
            FloatingNetworkId=json_data.get("FloatingNetworkId"),
            LbMethod=json_data.get("LbMethod"),
            LbProvider=json_data.get("LbProvider"),
            LbVersion=json_data.get("LbVersion"),
            ManageSecurityGroups=json_data.get("ManageSecurityGroups"),
            MonitorDelay=json_data.get("MonitorDelay"),
            MonitorMaxRetries=json_data.get("MonitorMaxRetries"),
            MonitorTimeout=json_data.get("MonitorTimeout"),
            SubnetId=json_data.get("SubnetId"),
            UseOctavia=json_data.get("UseOctavia"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancerDefinition = LoadBalancerDefinition


@dataclass
class MetadataDefinition(BaseModel):
    RequestTimeout: Optional[float]
    SearchOrder: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            RequestTimeout=json_data.get("RequestTimeout"),
            SearchOrder=json_data.get("SearchOrder"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class RouteDefinition(BaseModel):
    RouterId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteDefinition"]:
        if not json_data:
            return None
        return cls(
            RouterId=json_data.get("RouterId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteDefinition = RouteDefinition


@dataclass
class VsphereCloudProviderDefinition(BaseModel):
    Disk: Optional[Sequence["_DiskDefinition"]]
    Global: Optional[Sequence["_GlobalDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
    VirtualCenter: Optional[Sequence["_VirtualCenterDefinition"]]
    Workspace: Optional[Sequence["_WorkspaceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VsphereCloudProviderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VsphereCloudProviderDefinition"]:
        if not json_data:
            return None
        return cls(
            Disk=deserialize_list(json_data.get("Disk"), DiskDefinition),
            Global=deserialize_list(json_data.get("Global"), GlobalDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            VirtualCenter=deserialize_list(json_data.get("VirtualCenter"), VirtualCenterDefinition),
            Workspace=deserialize_list(json_data.get("Workspace"), WorkspaceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VsphereCloudProviderDefinition = VsphereCloudProviderDefinition


@dataclass
class DiskDefinition(BaseModel):
    ScsiControllerType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskDefinition"]:
        if not json_data:
            return None
        return cls(
            ScsiControllerType=json_data.get("ScsiControllerType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskDefinition = DiskDefinition


@dataclass
class NetworkDefinition(BaseModel):
    PublicNetwork: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            PublicNetwork=json_data.get("PublicNetwork"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class VirtualCenterDefinition(BaseModel):
    Datacenters: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[str]
    SoapRoundtripCount: Optional[float]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualCenterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualCenterDefinition"]:
        if not json_data:
            return None
        return cls(
            Datacenters=json_data.get("Datacenters"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SoapRoundtripCount=json_data.get("SoapRoundtripCount"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualCenterDefinition = VirtualCenterDefinition


@dataclass
class WorkspaceDefinition(BaseModel):
    Datacenter: Optional[str]
    DefaultDatastore: Optional[str]
    Folder: Optional[str]
    ResourcepoolPath: Optional[str]
    Server: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkspaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkspaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Datacenter=json_data.get("Datacenter"),
            DefaultDatastore=json_data.get("DefaultDatastore"),
            Folder=json_data.get("Folder"),
            ResourcepoolPath=json_data.get("ResourcepoolPath"),
            Server=json_data.get("Server"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkspaceDefinition = WorkspaceDefinition


@dataclass
class DnsDefinition(BaseModel):
    NodeSelector: Optional[Sequence["_NodeSelectorDefinition"]]
    Provider: Optional[str]
    ReverseCidrs: Optional[Sequence[str]]
    UpstreamNameservers: Optional[Sequence[str]]
    LinearAutoscalerParams: Optional[Sequence["_LinearAutoscalerParamsDefinition"]]
    Nodelocal: Optional[Sequence["_NodelocalDefinition"]]
    UpdateStrategy: Optional[Sequence["_UpdateStrategyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsDefinition"]:
        if not json_data:
            return None
        return cls(
            NodeSelector=deserialize_list(json_data.get("NodeSelector"), NodeSelectorDefinition),
            Provider=json_data.get("Provider"),
            ReverseCidrs=json_data.get("ReverseCidrs"),
            UpstreamNameservers=json_data.get("UpstreamNameservers"),
            LinearAutoscalerParams=deserialize_list(json_data.get("LinearAutoscalerParams"), LinearAutoscalerParamsDefinition),
            Nodelocal=deserialize_list(json_data.get("Nodelocal"), NodelocalDefinition),
            UpdateStrategy=deserialize_list(json_data.get("UpdateStrategy"), UpdateStrategyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsDefinition = DnsDefinition


@dataclass
class NodeSelectorDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeSelectorDefinition = NodeSelectorDefinition


@dataclass
class LinearAutoscalerParamsDefinition(BaseModel):
    CoresPerReplica: Optional[float]
    Max: Optional[float]
    Min: Optional[float]
    NodesPerReplica: Optional[float]
    PreventSinglePointFailure: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_LinearAutoscalerParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinearAutoscalerParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            CoresPerReplica=json_data.get("CoresPerReplica"),
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
            NodesPerReplica=json_data.get("NodesPerReplica"),
            PreventSinglePointFailure=json_data.get("PreventSinglePointFailure"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinearAutoscalerParamsDefinition = LinearAutoscalerParamsDefinition


@dataclass
class NodelocalDefinition(BaseModel):
    IpAddress: Optional[str]
    NodeSelector: Optional[Sequence["_NodeSelectorDefinition4"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodelocalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodelocalDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            NodeSelector=deserialize_list(json_data.get("NodeSelector"), NodeSelectorDefinition4),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodelocalDefinition = NodelocalDefinition


@dataclass
class NodeSelectorDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeSelectorDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeSelectorDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeSelectorDefinition4 = NodeSelectorDefinition4


@dataclass
class UpdateStrategyDefinition(BaseModel):
    Strategy: Optional[str]
    RollingUpdate: Optional[Sequence["_RollingUpdateDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UpdateStrategyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpdateStrategyDefinition"]:
        if not json_data:
            return None
        return cls(
            Strategy=json_data.get("Strategy"),
            RollingUpdate=deserialize_list(json_data.get("RollingUpdate"), RollingUpdateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpdateStrategyDefinition = UpdateStrategyDefinition


@dataclass
class RollingUpdateDefinition(BaseModel):
    MaxSurge: Optional[float]
    MaxUnavailable: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RollingUpdateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RollingUpdateDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxSurge=json_data.get("MaxSurge"),
            MaxUnavailable=json_data.get("MaxUnavailable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RollingUpdateDefinition = RollingUpdateDefinition


@dataclass
class IngressDefinition(BaseModel):
    DefaultBackend: Optional[bool]
    DnsPolicy: Optional[str]
    ExtraArgs: Optional[Sequence["_ExtraArgsDefinition"]]
    HttpPort: Optional[float]
    HttpsPort: Optional[float]
    NetworkMode: Optional[str]
    NodeSelector: Optional[Sequence["_NodeSelectorDefinition2"]]
    Options: Optional[Sequence["_OptionsDefinition2"]]
    Provider: Optional[str]
    UpdateStrategy: Optional[Sequence["_UpdateStrategyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IngressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultBackend=json_data.get("DefaultBackend"),
            DnsPolicy=json_data.get("DnsPolicy"),
            ExtraArgs=deserialize_list(json_data.get("ExtraArgs"), ExtraArgsDefinition),
            HttpPort=json_data.get("HttpPort"),
            HttpsPort=json_data.get("HttpsPort"),
            NetworkMode=json_data.get("NetworkMode"),
            NodeSelector=deserialize_list(json_data.get("NodeSelector"), NodeSelectorDefinition2),
            Options=deserialize_list(json_data.get("Options"), OptionsDefinition2),
            Provider=json_data.get("Provider"),
            UpdateStrategy=deserialize_list(json_data.get("UpdateStrategy"), UpdateStrategyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressDefinition = IngressDefinition


@dataclass
class ExtraArgsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraArgsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraArgsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraArgsDefinition = ExtraArgsDefinition


@dataclass
class NodeSelectorDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeSelectorDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeSelectorDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeSelectorDefinition2 = NodeSelectorDefinition2


@dataclass
class OptionsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OptionsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionsDefinition2 = OptionsDefinition2


@dataclass
class MonitoringDefinition(BaseModel):
    NodeSelector: Optional[Sequence["_NodeSelectorDefinition3"]]
    Options: Optional[Sequence["_OptionsDefinition3"]]
    Provider: Optional[str]
    Replicas: Optional[float]
    UpdateStrategy: Optional[Sequence["_UpdateStrategyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MonitoringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitoringDefinition"]:
        if not json_data:
            return None
        return cls(
            NodeSelector=deserialize_list(json_data.get("NodeSelector"), NodeSelectorDefinition3),
            Options=deserialize_list(json_data.get("Options"), OptionsDefinition3),
            Provider=json_data.get("Provider"),
            Replicas=json_data.get("Replicas"),
            UpdateStrategy=deserialize_list(json_data.get("UpdateStrategy"), UpdateStrategyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitoringDefinition = MonitoringDefinition


@dataclass
class NodeSelectorDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeSelectorDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeSelectorDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeSelectorDefinition3 = NodeSelectorDefinition3


@dataclass
class OptionsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OptionsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionsDefinition3 = OptionsDefinition3


@dataclass
class NodesDefinition(BaseModel):
    Address: Optional[str]
    DockerSocket: Optional[str]
    HostnameOverride: Optional[str]
    InternalAddress: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition3"]]
    NodeId: Optional[str]
    Port: Optional[str]
    Role: Optional[Sequence[str]]
    SshAgentAuth: Optional[bool]
    SshKey: Optional[str]
    SshKeyPath: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodesDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            DockerSocket=json_data.get("DockerSocket"),
            HostnameOverride=json_data.get("HostnameOverride"),
            InternalAddress=json_data.get("InternalAddress"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition3),
            NodeId=json_data.get("NodeId"),
            Port=json_data.get("Port"),
            Role=json_data.get("Role"),
            SshAgentAuth=json_data.get("SshAgentAuth"),
            SshKey=json_data.get("SshKey"),
            SshKeyPath=json_data.get("SshKeyPath"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodesDefinition = NodesDefinition


@dataclass
class LabelsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition3 = LabelsDefinition3


@dataclass
class PrivateRegistriesDefinition(BaseModel):
    IsDefault: Optional[bool]
    Password: Optional[str]
    Url: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateRegistriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateRegistriesDefinition"]:
        if not json_data:
            return None
        return cls(
            IsDefault=json_data.get("IsDefault"),
            Password=json_data.get("Password"),
            Url=json_data.get("Url"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateRegistriesDefinition = PrivateRegistriesDefinition


@dataclass
class ServicesDefinition(BaseModel):
    Etcd: Optional[Sequence["_EtcdDefinition"]]
    KubeApi: Optional[Sequence["_KubeApiDefinition"]]
    KubeController: Optional[Sequence["_KubeControllerDefinition"]]
    Kubelet: Optional[Sequence["_KubeletDefinition"]]
    Kubeproxy: Optional[Sequence["_KubeproxyDefinition"]]
    Scheduler: Optional[Sequence["_SchedulerDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicesDefinition"]:
        if not json_data:
            return None
        return cls(
            Etcd=deserialize_list(json_data.get("Etcd"), EtcdDefinition),
            KubeApi=deserialize_list(json_data.get("KubeApi"), KubeApiDefinition),
            KubeController=deserialize_list(json_data.get("KubeController"), KubeControllerDefinition),
            Kubelet=deserialize_list(json_data.get("Kubelet"), KubeletDefinition),
            Kubeproxy=deserialize_list(json_data.get("Kubeproxy"), KubeproxyDefinition),
            Scheduler=deserialize_list(json_data.get("Scheduler"), SchedulerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicesDefinition = ServicesDefinition


@dataclass
class EtcdDefinition(BaseModel):
    CaCert: Optional[str]
    Cert: Optional[str]
    Creation: Optional[str]
    ExternalUrls: Optional[Sequence[str]]
    ExtraArgs: Optional[Sequence["_ExtraArgsDefinition2"]]
    ExtraBinds: Optional[Sequence[str]]
    ExtraEnv: Optional[Sequence[str]]
    Gid: Optional[float]
    Image: Optional[str]
    Key: Optional[str]
    Path: Optional[str]
    Retention: Optional[str]
    Snapshot: Optional[bool]
    Uid: Optional[float]
    BackupConfig: Optional[Sequence["_BackupConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EtcdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EtcdDefinition"]:
        if not json_data:
            return None
        return cls(
            CaCert=json_data.get("CaCert"),
            Cert=json_data.get("Cert"),
            Creation=json_data.get("Creation"),
            ExternalUrls=json_data.get("ExternalUrls"),
            ExtraArgs=deserialize_list(json_data.get("ExtraArgs"), ExtraArgsDefinition2),
            ExtraBinds=json_data.get("ExtraBinds"),
            ExtraEnv=json_data.get("ExtraEnv"),
            Gid=json_data.get("Gid"),
            Image=json_data.get("Image"),
            Key=json_data.get("Key"),
            Path=json_data.get("Path"),
            Retention=json_data.get("Retention"),
            Snapshot=json_data.get("Snapshot"),
            Uid=json_data.get("Uid"),
            BackupConfig=deserialize_list(json_data.get("BackupConfig"), BackupConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EtcdDefinition = EtcdDefinition


@dataclass
class ExtraArgsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraArgsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraArgsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraArgsDefinition2 = ExtraArgsDefinition2


@dataclass
class BackupConfigDefinition(BaseModel):
    Enabled: Optional[bool]
    IntervalHours: Optional[float]
    Retention: Optional[float]
    SafeTimestamp: Optional[bool]
    Timeout: Optional[float]
    S3BackupConfig: Optional[Sequence["_S3BackupConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BackupConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            IntervalHours=json_data.get("IntervalHours"),
            Retention=json_data.get("Retention"),
            SafeTimestamp=json_data.get("SafeTimestamp"),
            Timeout=json_data.get("Timeout"),
            S3BackupConfig=deserialize_list(json_data.get("S3BackupConfig"), S3BackupConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupConfigDefinition = BackupConfigDefinition


@dataclass
class S3BackupConfigDefinition(BaseModel):
    AccessKey: Optional[str]
    BucketName: Optional[str]
    CustomCa: Optional[str]
    Endpoint: Optional[str]
    Folder: Optional[str]
    Region: Optional[str]
    SecretKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3BackupConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3BackupConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            BucketName=json_data.get("BucketName"),
            CustomCa=json_data.get("CustomCa"),
            Endpoint=json_data.get("Endpoint"),
            Folder=json_data.get("Folder"),
            Region=json_data.get("Region"),
            SecretKey=json_data.get("SecretKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3BackupConfigDefinition = S3BackupConfigDefinition


@dataclass
class KubeApiDefinition(BaseModel):
    AdmissionConfiguration: Optional[Sequence["_AdmissionConfigurationDefinition"]]
    AlwaysPullImages: Optional[bool]
    ExtraArgs: Optional[Sequence["_ExtraArgsDefinition3"]]
    ExtraBinds: Optional[Sequence[str]]
    ExtraEnv: Optional[Sequence[str]]
    Image: Optional[str]
    PodSecurityPolicy: Optional[bool]
    ServiceClusterIpRange: Optional[str]
    ServiceNodePortRange: Optional[str]
    AuditLog: Optional[Sequence["_AuditLogDefinition"]]
    EventRateLimit: Optional[Sequence["_EventRateLimitDefinition"]]
    SecretsEncryptionConfig: Optional[Sequence["_SecretsEncryptionConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_KubeApiDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeApiDefinition"]:
        if not json_data:
            return None
        return cls(
            AdmissionConfiguration=deserialize_list(json_data.get("AdmissionConfiguration"), AdmissionConfigurationDefinition),
            AlwaysPullImages=json_data.get("AlwaysPullImages"),
            ExtraArgs=deserialize_list(json_data.get("ExtraArgs"), ExtraArgsDefinition3),
            ExtraBinds=json_data.get("ExtraBinds"),
            ExtraEnv=json_data.get("ExtraEnv"),
            Image=json_data.get("Image"),
            PodSecurityPolicy=json_data.get("PodSecurityPolicy"),
            ServiceClusterIpRange=json_data.get("ServiceClusterIpRange"),
            ServiceNodePortRange=json_data.get("ServiceNodePortRange"),
            AuditLog=deserialize_list(json_data.get("AuditLog"), AuditLogDefinition),
            EventRateLimit=deserialize_list(json_data.get("EventRateLimit"), EventRateLimitDefinition),
            SecretsEncryptionConfig=deserialize_list(json_data.get("SecretsEncryptionConfig"), SecretsEncryptionConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeApiDefinition = KubeApiDefinition


@dataclass
class AdmissionConfigurationDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdmissionConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdmissionConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdmissionConfigurationDefinition = AdmissionConfigurationDefinition


@dataclass
class ExtraArgsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraArgsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraArgsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraArgsDefinition3 = ExtraArgsDefinition3


@dataclass
class AuditLogDefinition(BaseModel):
    Enabled: Optional[bool]
    Configuration: Optional[Sequence["_ConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AuditLogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuditLogDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Configuration=deserialize_list(json_data.get("Configuration"), ConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuditLogDefinition = AuditLogDefinition


@dataclass
class ConfigurationDefinition(BaseModel):
    Format: Optional[str]
    MaxAge: Optional[float]
    MaxBackup: Optional[float]
    MaxSize: Optional[float]
    Path: Optional[str]
    Policy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Format=json_data.get("Format"),
            MaxAge=json_data.get("MaxAge"),
            MaxBackup=json_data.get("MaxBackup"),
            MaxSize=json_data.get("MaxSize"),
            Path=json_data.get("Path"),
            Policy=json_data.get("Policy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationDefinition = ConfigurationDefinition


@dataclass
class EventRateLimitDefinition(BaseModel):
    Configuration: Optional[str]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EventRateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventRateLimitDefinition"]:
        if not json_data:
            return None
        return cls(
            Configuration=json_data.get("Configuration"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventRateLimitDefinition = EventRateLimitDefinition


@dataclass
class SecretsEncryptionConfigDefinition(BaseModel):
    CustomConfig: Optional[str]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SecretsEncryptionConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretsEncryptionConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomConfig=json_data.get("CustomConfig"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretsEncryptionConfigDefinition = SecretsEncryptionConfigDefinition


@dataclass
class KubeControllerDefinition(BaseModel):
    ClusterCidr: Optional[str]
    ExtraArgs: Optional[Sequence["_ExtraArgsDefinition4"]]
    ExtraBinds: Optional[Sequence[str]]
    ExtraEnv: Optional[Sequence[str]]
    Image: Optional[str]
    ServiceClusterIpRange: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubeControllerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeControllerDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterCidr=json_data.get("ClusterCidr"),
            ExtraArgs=deserialize_list(json_data.get("ExtraArgs"), ExtraArgsDefinition4),
            ExtraBinds=json_data.get("ExtraBinds"),
            ExtraEnv=json_data.get("ExtraEnv"),
            Image=json_data.get("Image"),
            ServiceClusterIpRange=json_data.get("ServiceClusterIpRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeControllerDefinition = KubeControllerDefinition


@dataclass
class ExtraArgsDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraArgsDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraArgsDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraArgsDefinition4 = ExtraArgsDefinition4


@dataclass
class KubeletDefinition(BaseModel):
    ClusterDnsServer: Optional[str]
    ClusterDomain: Optional[str]
    ExtraArgs: Optional[Sequence["_ExtraArgsDefinition5"]]
    ExtraBinds: Optional[Sequence[str]]
    ExtraEnv: Optional[Sequence[str]]
    FailSwapOn: Optional[bool]
    GenerateServingCertificate: Optional[bool]
    Image: Optional[str]
    InfraContainerImage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubeletDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeletDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterDnsServer=json_data.get("ClusterDnsServer"),
            ClusterDomain=json_data.get("ClusterDomain"),
            ExtraArgs=deserialize_list(json_data.get("ExtraArgs"), ExtraArgsDefinition5),
            ExtraBinds=json_data.get("ExtraBinds"),
            ExtraEnv=json_data.get("ExtraEnv"),
            FailSwapOn=json_data.get("FailSwapOn"),
            GenerateServingCertificate=json_data.get("GenerateServingCertificate"),
            Image=json_data.get("Image"),
            InfraContainerImage=json_data.get("InfraContainerImage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeletDefinition = KubeletDefinition


@dataclass
class ExtraArgsDefinition5(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraArgsDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraArgsDefinition5"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraArgsDefinition5 = ExtraArgsDefinition5


@dataclass
class KubeproxyDefinition(BaseModel):
    ExtraArgs: Optional[Sequence["_ExtraArgsDefinition6"]]
    ExtraBinds: Optional[Sequence[str]]
    ExtraEnv: Optional[Sequence[str]]
    Image: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubeproxyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeproxyDefinition"]:
        if not json_data:
            return None
        return cls(
            ExtraArgs=deserialize_list(json_data.get("ExtraArgs"), ExtraArgsDefinition6),
            ExtraBinds=json_data.get("ExtraBinds"),
            ExtraEnv=json_data.get("ExtraEnv"),
            Image=json_data.get("Image"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeproxyDefinition = KubeproxyDefinition


@dataclass
class ExtraArgsDefinition6(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraArgsDefinition6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraArgsDefinition6"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraArgsDefinition6 = ExtraArgsDefinition6


@dataclass
class SchedulerDefinition(BaseModel):
    ExtraArgs: Optional[Sequence["_ExtraArgsDefinition7"]]
    ExtraBinds: Optional[Sequence[str]]
    ExtraEnv: Optional[Sequence[str]]
    Image: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchedulerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchedulerDefinition"]:
        if not json_data:
            return None
        return cls(
            ExtraArgs=deserialize_list(json_data.get("ExtraArgs"), ExtraArgsDefinition7),
            ExtraBinds=json_data.get("ExtraBinds"),
            ExtraEnv=json_data.get("ExtraEnv"),
            Image=json_data.get("Image"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchedulerDefinition = SchedulerDefinition


@dataclass
class ExtraArgsDefinition7(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraArgsDefinition7"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraArgsDefinition7"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraArgsDefinition7 = ExtraArgsDefinition7


@dataclass
class UpgradeStrategyDefinition(BaseModel):
    Drain: Optional[bool]
    MaxUnavailableControlplane: Optional[str]
    MaxUnavailableWorker: Optional[str]
    DrainInput: Optional[Sequence["_DrainInputDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UpgradeStrategyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpgradeStrategyDefinition"]:
        if not json_data:
            return None
        return cls(
            Drain=json_data.get("Drain"),
            MaxUnavailableControlplane=json_data.get("MaxUnavailableControlplane"),
            MaxUnavailableWorker=json_data.get("MaxUnavailableWorker"),
            DrainInput=deserialize_list(json_data.get("DrainInput"), DrainInputDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpgradeStrategyDefinition = UpgradeStrategyDefinition


@dataclass
class DrainInputDefinition(BaseModel):
    DeleteLocalData: Optional[bool]
    Force: Optional[bool]
    GracePeriod: Optional[float]
    IgnoreDaemonSets: Optional[bool]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DrainInputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DrainInputDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteLocalData=json_data.get("DeleteLocalData"),
            Force=json_data.get("Force"),
            GracePeriod=json_data.get("GracePeriod"),
            IgnoreDaemonSets=json_data.get("IgnoreDaemonSets"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DrainInputDefinition = DrainInputDefinition


@dataclass
class ScheduledClusterScanDefinition(BaseModel):
    Enabled: Optional[bool]
    ScanConfig: Optional[Sequence["_ScanConfigDefinition"]]
    ScheduleConfig: Optional[Sequence["_ScheduleConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduledClusterScanDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledClusterScanDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            ScanConfig=deserialize_list(json_data.get("ScanConfig"), ScanConfigDefinition),
            ScheduleConfig=deserialize_list(json_data.get("ScheduleConfig"), ScheduleConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledClusterScanDefinition = ScheduledClusterScanDefinition


@dataclass
class ScanConfigDefinition(BaseModel):
    CisScanConfig: Optional[Sequence["_CisScanConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScanConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScanConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CisScanConfig=deserialize_list(json_data.get("CisScanConfig"), CisScanConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScanConfigDefinition = ScanConfigDefinition


@dataclass
class CisScanConfigDefinition(BaseModel):
    DebugMaster: Optional[bool]
    DebugWorker: Optional[bool]
    OverrideBenchmarkVersion: Optional[str]
    OverrideSkip: Optional[Sequence[str]]
    Profile: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CisScanConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CisScanConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DebugMaster=json_data.get("DebugMaster"),
            DebugWorker=json_data.get("DebugWorker"),
            OverrideBenchmarkVersion=json_data.get("OverrideBenchmarkVersion"),
            OverrideSkip=json_data.get("OverrideSkip"),
            Profile=json_data.get("Profile"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CisScanConfigDefinition = CisScanConfigDefinition


@dataclass
class ScheduleConfigDefinition(BaseModel):
    CronSchedule: Optional[str]
    Retention: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CronSchedule=json_data.get("CronSchedule"),
            Retention=json_data.get("Retention"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleConfigDefinition = ScheduleConfigDefinition


@dataclass
class QuestionsDefinition(BaseModel):
    Default: Optional[str]
    Required: Optional[bool]
    Type: Optional[str]
    Variable: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QuestionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QuestionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
            Required=json_data.get("Required"),
            Type=json_data.get("Type"),
            Variable=json_data.get("Variable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QuestionsDefinition = QuestionsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


