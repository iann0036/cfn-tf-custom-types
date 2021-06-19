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
    ApicMode: Optional[bool]
    AutoscalePollingInterval: Optional[float]
    DhcpEnabled: Optional[bool]
    DnsProviderRef: Optional[str]
    DnsResolutionOnSe: Optional[bool]
    EastWestDnsProviderRef: Optional[str]
    EastWestIpamProviderRef: Optional[str]
    EnableVipOnAllInterfaces: Optional[bool]
    EnableVipStaticRoutes: Optional[bool]
    Id: Optional[str]
    Ip6AutocfgEnabled: Optional[bool]
    IpamProviderRef: Optional[str]
    LicenseTier: Optional[str]
    LicenseType: Optional[str]
    Mtu: Optional[float]
    Name: Optional[str]
    ObjNamePrefix: Optional[str]
    PreferStaticRoutes: Optional[bool]
    SeGroupTemplateRef: Optional[str]
    StateBasedDnsRegistration: Optional[bool]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    VmcDeployment: Optional[bool]
    Vtype: Optional[str]
    ApicConfiguration: Optional[Sequence["_ApicConfigurationDefinition"]]
    AwsConfiguration: Optional[Sequence["_AwsConfigurationDefinition"]]
    AzureConfiguration: Optional[Sequence["_AzureConfigurationDefinition"]]
    CloudstackConfiguration: Optional[Sequence["_CloudstackConfigurationDefinition"]]
    CustomTags: Optional[Sequence["_CustomTagsDefinition"]]
    DnsResolvers: Optional[Sequence["_DnsResolversDefinition"]]
    DockerConfiguration: Optional[Sequence["_DockerConfigurationDefinition"]]
    GcpConfiguration: Optional[Sequence["_GcpConfigurationDefinition"]]
    LinuxserverConfiguration: Optional[Sequence["_LinuxserverConfigurationDefinition"]]
    NsxConfiguration: Optional[Sequence["_NsxConfigurationDefinition"]]
    NsxtConfiguration: Optional[Sequence["_NsxtConfigurationDefinition"]]
    OpenstackConfiguration: Optional[Sequence["_OpenstackConfigurationDefinition"]]
    ProxyConfiguration: Optional[Sequence["_ProxyConfigurationDefinition"]]
    RancherConfiguration: Optional[Sequence["_RancherConfigurationDefinition"]]
    VcaConfiguration: Optional[Sequence["_VcaConfigurationDefinition"]]
    VcenterConfiguration: Optional[Sequence["_VcenterConfigurationDefinition"]]

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
            ApicMode=json_data.get("ApicMode"),
            AutoscalePollingInterval=json_data.get("AutoscalePollingInterval"),
            DhcpEnabled=json_data.get("DhcpEnabled"),
            DnsProviderRef=json_data.get("DnsProviderRef"),
            DnsResolutionOnSe=json_data.get("DnsResolutionOnSe"),
            EastWestDnsProviderRef=json_data.get("EastWestDnsProviderRef"),
            EastWestIpamProviderRef=json_data.get("EastWestIpamProviderRef"),
            EnableVipOnAllInterfaces=json_data.get("EnableVipOnAllInterfaces"),
            EnableVipStaticRoutes=json_data.get("EnableVipStaticRoutes"),
            Id=json_data.get("Id"),
            Ip6AutocfgEnabled=json_data.get("Ip6AutocfgEnabled"),
            IpamProviderRef=json_data.get("IpamProviderRef"),
            LicenseTier=json_data.get("LicenseTier"),
            LicenseType=json_data.get("LicenseType"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            ObjNamePrefix=json_data.get("ObjNamePrefix"),
            PreferStaticRoutes=json_data.get("PreferStaticRoutes"),
            SeGroupTemplateRef=json_data.get("SeGroupTemplateRef"),
            StateBasedDnsRegistration=json_data.get("StateBasedDnsRegistration"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            VmcDeployment=json_data.get("VmcDeployment"),
            Vtype=json_data.get("Vtype"),
            ApicConfiguration=deserialize_list(json_data.get("ApicConfiguration"), ApicConfigurationDefinition),
            AwsConfiguration=deserialize_list(json_data.get("AwsConfiguration"), AwsConfigurationDefinition),
            AzureConfiguration=deserialize_list(json_data.get("AzureConfiguration"), AzureConfigurationDefinition),
            CloudstackConfiguration=deserialize_list(json_data.get("CloudstackConfiguration"), CloudstackConfigurationDefinition),
            CustomTags=deserialize_list(json_data.get("CustomTags"), CustomTagsDefinition),
            DnsResolvers=deserialize_list(json_data.get("DnsResolvers"), DnsResolversDefinition),
            DockerConfiguration=deserialize_list(json_data.get("DockerConfiguration"), DockerConfigurationDefinition),
            GcpConfiguration=deserialize_list(json_data.get("GcpConfiguration"), GcpConfigurationDefinition),
            LinuxserverConfiguration=deserialize_list(json_data.get("LinuxserverConfiguration"), LinuxserverConfigurationDefinition),
            NsxConfiguration=deserialize_list(json_data.get("NsxConfiguration"), NsxConfigurationDefinition),
            NsxtConfiguration=deserialize_list(json_data.get("NsxtConfiguration"), NsxtConfigurationDefinition),
            OpenstackConfiguration=deserialize_list(json_data.get("OpenstackConfiguration"), OpenstackConfigurationDefinition),
            ProxyConfiguration=deserialize_list(json_data.get("ProxyConfiguration"), ProxyConfigurationDefinition),
            RancherConfiguration=deserialize_list(json_data.get("RancherConfiguration"), RancherConfigurationDefinition),
            VcaConfiguration=deserialize_list(json_data.get("VcaConfiguration"), VcaConfigurationDefinition),
            VcenterConfiguration=deserialize_list(json_data.get("VcenterConfiguration"), VcenterConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ApicConfigurationDefinition(BaseModel):
    ApicAdminTenant: Optional[str]
    ApicDomain: Optional[str]
    ApicName: Optional[Sequence[str]]
    ApicPassword: Optional[str]
    ApicUsername: Optional[str]
    ContextAware: Optional[str]
    SeTunnelMode: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ApicConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApicConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ApicAdminTenant=json_data.get("ApicAdminTenant"),
            ApicDomain=json_data.get("ApicDomain"),
            ApicName=json_data.get("ApicName"),
            ApicPassword=json_data.get("ApicPassword"),
            ApicUsername=json_data.get("ApicUsername"),
            ContextAware=json_data.get("ContextAware"),
            SeTunnelMode=json_data.get("SeTunnelMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApicConfigurationDefinition = ApicConfigurationDefinition


@dataclass
class AwsConfigurationDefinition(BaseModel):
    AccessKeyId: Optional[str]
    AsgPollInterval: Optional[float]
    FreeElasticips: Optional[bool]
    IamAssumeRole: Optional[str]
    PublishVipToPublicZone: Optional[bool]
    Region: Optional[str]
    Route53Integration: Optional[bool]
    SecretAccessKey: Optional[str]
    Ttl: Optional[float]
    UseIamRoles: Optional[bool]
    UseSnsSqs: Optional[bool]
    Vpc: Optional[str]
    VpcId: Optional[str]
    EbsEncryption: Optional[Sequence["_EbsEncryptionDefinition"]]
    S3Encryption: Optional[Sequence["_S3EncryptionDefinition"]]
    SqsEncryption: Optional[Sequence["_SqsEncryptionDefinition"]]
    Zones: Optional[Sequence["_ZonesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKeyId=json_data.get("AccessKeyId"),
            AsgPollInterval=json_data.get("AsgPollInterval"),
            FreeElasticips=json_data.get("FreeElasticips"),
            IamAssumeRole=json_data.get("IamAssumeRole"),
            PublishVipToPublicZone=json_data.get("PublishVipToPublicZone"),
            Region=json_data.get("Region"),
            Route53Integration=json_data.get("Route53Integration"),
            SecretAccessKey=json_data.get("SecretAccessKey"),
            Ttl=json_data.get("Ttl"),
            UseIamRoles=json_data.get("UseIamRoles"),
            UseSnsSqs=json_data.get("UseSnsSqs"),
            Vpc=json_data.get("Vpc"),
            VpcId=json_data.get("VpcId"),
            EbsEncryption=deserialize_list(json_data.get("EbsEncryption"), EbsEncryptionDefinition),
            S3Encryption=deserialize_list(json_data.get("S3Encryption"), S3EncryptionDefinition),
            SqsEncryption=deserialize_list(json_data.get("SqsEncryption"), SqsEncryptionDefinition),
            Zones=deserialize_list(json_data.get("Zones"), ZonesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConfigurationDefinition = AwsConfigurationDefinition


@dataclass
class EbsEncryptionDefinition(BaseModel):
    MasterKey: Optional[str]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsEncryptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsEncryptionDefinition"]:
        if not json_data:
            return None
        return cls(
            MasterKey=json_data.get("MasterKey"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsEncryptionDefinition = EbsEncryptionDefinition


@dataclass
class S3EncryptionDefinition(BaseModel):
    MasterKey: Optional[str]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3EncryptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3EncryptionDefinition"]:
        if not json_data:
            return None
        return cls(
            MasterKey=json_data.get("MasterKey"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3EncryptionDefinition = S3EncryptionDefinition


@dataclass
class SqsEncryptionDefinition(BaseModel):
    MasterKey: Optional[str]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SqsEncryptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SqsEncryptionDefinition"]:
        if not json_data:
            return None
        return cls(
            MasterKey=json_data.get("MasterKey"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SqsEncryptionDefinition = SqsEncryptionDefinition


@dataclass
class ZonesDefinition(BaseModel):
    AvailabilityZone: Optional[str]
    MgmtNetworkName: Optional[str]
    MgmtNetworkUuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZonesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZonesDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            MgmtNetworkName=json_data.get("MgmtNetworkName"),
            MgmtNetworkUuid=json_data.get("MgmtNetworkUuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZonesDefinition = ZonesDefinition


@dataclass
class AzureConfigurationDefinition(BaseModel):
    AvailabilityZones: Optional[Sequence[str]]
    CloudCredentialsRef: Optional[str]
    DesId: Optional[str]
    Location: Optional[str]
    ResourceGroup: Optional[str]
    SubscriptionId: Optional[str]
    UseAzureDns: Optional[bool]
    UseEnhancedHa: Optional[bool]
    UseManagedDisks: Optional[bool]
    UseStandardAlb: Optional[bool]
    NetworkInfo: Optional[Sequence["_NetworkInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AzureConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZones=json_data.get("AvailabilityZones"),
            CloudCredentialsRef=json_data.get("CloudCredentialsRef"),
            DesId=json_data.get("DesId"),
            Location=json_data.get("Location"),
            ResourceGroup=json_data.get("ResourceGroup"),
            SubscriptionId=json_data.get("SubscriptionId"),
            UseAzureDns=json_data.get("UseAzureDns"),
            UseEnhancedHa=json_data.get("UseEnhancedHa"),
            UseManagedDisks=json_data.get("UseManagedDisks"),
            UseStandardAlb=json_data.get("UseStandardAlb"),
            NetworkInfo=deserialize_list(json_data.get("NetworkInfo"), NetworkInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureConfigurationDefinition = AzureConfigurationDefinition


@dataclass
class NetworkInfoDefinition(BaseModel):
    ManagementNetworkId: Optional[str]
    SeNetworkId: Optional[str]
    VirtualNetworkId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            ManagementNetworkId=json_data.get("ManagementNetworkId"),
            SeNetworkId=json_data.get("SeNetworkId"),
            VirtualNetworkId=json_data.get("VirtualNetworkId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInfoDefinition = NetworkInfoDefinition


@dataclass
class CloudstackConfigurationDefinition(BaseModel):
    AccessKeyId: Optional[str]
    ApiUrl: Optional[str]
    CntrPublicIp: Optional[str]
    Hypervisor: Optional[str]
    MgmtNetworkName: Optional[str]
    MgmtNetworkUuid: Optional[str]
    SecretAccessKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudstackConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudstackConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKeyId=json_data.get("AccessKeyId"),
            ApiUrl=json_data.get("ApiUrl"),
            CntrPublicIp=json_data.get("CntrPublicIp"),
            Hypervisor=json_data.get("Hypervisor"),
            MgmtNetworkName=json_data.get("MgmtNetworkName"),
            MgmtNetworkUuid=json_data.get("MgmtNetworkUuid"),
            SecretAccessKey=json_data.get("SecretAccessKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudstackConfigurationDefinition = CloudstackConfigurationDefinition


@dataclass
class CustomTagsDefinition(BaseModel):
    TagKey: Optional[str]
    TagVal: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            TagKey=json_data.get("TagKey"),
            TagVal=json_data.get("TagVal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomTagsDefinition = CustomTagsDefinition


@dataclass
class DnsResolversDefinition(BaseModel):
    FixedTtl: Optional[float]
    MinTtl: Optional[float]
    ResolverName: Optional[str]
    UseMgmt: Optional[bool]
    NameserverIps: Optional[Sequence["_NameserverIpsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsResolversDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsResolversDefinition"]:
        if not json_data:
            return None
        return cls(
            FixedTtl=json_data.get("FixedTtl"),
            MinTtl=json_data.get("MinTtl"),
            ResolverName=json_data.get("ResolverName"),
            UseMgmt=json_data.get("UseMgmt"),
            NameserverIps=deserialize_list(json_data.get("NameserverIps"), NameserverIpsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsResolversDefinition = DnsResolversDefinition


@dataclass
class NameserverIpsDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NameserverIpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NameserverIpsDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NameserverIpsDefinition = NameserverIpsDefinition


@dataclass
class DockerConfigurationDefinition(BaseModel):
    AppSyncFrequency: Optional[float]
    CaTlsKeyAndCertificateRef: Optional[str]
    ClientTlsKeyAndCertificateRef: Optional[str]
    ContainerPortMatchHttpService: Optional[bool]
    CoredumpDirectory: Optional[str]
    DisableAutoBackendServiceSync: Optional[bool]
    DisableAutoFrontendServiceSync: Optional[bool]
    DisableAutoSeCreation: Optional[bool]
    EnableEventSubscription: Optional[bool]
    FeproxyContainerPortAsService: Optional[bool]
    FeproxyVipsEnableProxyArp: Optional[bool]
    FleetEndpoint: Optional[str]
    HttpContainerPorts: Optional[Sequence[float]]
    SeDeploymentMethod: Optional[str]
    SeSpawnRate: Optional[float]
    SeVolume: Optional[str]
    ServicesAccessibleAllInterfaces: Optional[bool]
    SshUserRef: Optional[str]
    UcpNodes: Optional[Sequence[str]]
    UseContainerIpPort: Optional[bool]
    UseControllerImage: Optional[bool]
    DockerRegistrySe: Optional[Sequence["_DockerRegistrySeDefinition"]]
    EastWestPlacementSubnet: Optional[Sequence["_EastWestPlacementSubnetDefinition"]]
    SeExcludeAttributes: Optional[Sequence["_SeExcludeAttributesDefinition"]]
    SeIncludeAttributes: Optional[Sequence["_SeIncludeAttributesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DockerConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DockerConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AppSyncFrequency=json_data.get("AppSyncFrequency"),
            CaTlsKeyAndCertificateRef=json_data.get("CaTlsKeyAndCertificateRef"),
            ClientTlsKeyAndCertificateRef=json_data.get("ClientTlsKeyAndCertificateRef"),
            ContainerPortMatchHttpService=json_data.get("ContainerPortMatchHttpService"),
            CoredumpDirectory=json_data.get("CoredumpDirectory"),
            DisableAutoBackendServiceSync=json_data.get("DisableAutoBackendServiceSync"),
            DisableAutoFrontendServiceSync=json_data.get("DisableAutoFrontendServiceSync"),
            DisableAutoSeCreation=json_data.get("DisableAutoSeCreation"),
            EnableEventSubscription=json_data.get("EnableEventSubscription"),
            FeproxyContainerPortAsService=json_data.get("FeproxyContainerPortAsService"),
            FeproxyVipsEnableProxyArp=json_data.get("FeproxyVipsEnableProxyArp"),
            FleetEndpoint=json_data.get("FleetEndpoint"),
            HttpContainerPorts=json_data.get("HttpContainerPorts"),
            SeDeploymentMethod=json_data.get("SeDeploymentMethod"),
            SeSpawnRate=json_data.get("SeSpawnRate"),
            SeVolume=json_data.get("SeVolume"),
            ServicesAccessibleAllInterfaces=json_data.get("ServicesAccessibleAllInterfaces"),
            SshUserRef=json_data.get("SshUserRef"),
            UcpNodes=json_data.get("UcpNodes"),
            UseContainerIpPort=json_data.get("UseContainerIpPort"),
            UseControllerImage=json_data.get("UseControllerImage"),
            DockerRegistrySe=deserialize_list(json_data.get("DockerRegistrySe"), DockerRegistrySeDefinition),
            EastWestPlacementSubnet=deserialize_list(json_data.get("EastWestPlacementSubnet"), EastWestPlacementSubnetDefinition),
            SeExcludeAttributes=deserialize_list(json_data.get("SeExcludeAttributes"), SeExcludeAttributesDefinition),
            SeIncludeAttributes=deserialize_list(json_data.get("SeIncludeAttributes"), SeIncludeAttributesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DockerConfigurationDefinition = DockerConfigurationDefinition


@dataclass
class DockerRegistrySeDefinition(BaseModel):
    Password: Optional[str]
    Private: Optional[bool]
    Registry: Optional[str]
    Username: Optional[str]
    OshiftRegistry: Optional[Sequence["_OshiftRegistryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DockerRegistrySeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DockerRegistrySeDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Private=json_data.get("Private"),
            Registry=json_data.get("Registry"),
            Username=json_data.get("Username"),
            OshiftRegistry=deserialize_list(json_data.get("OshiftRegistry"), OshiftRegistryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DockerRegistrySeDefinition = DockerRegistrySeDefinition


@dataclass
class OshiftRegistryDefinition(BaseModel):
    RegistryNamespace: Optional[str]
    RegistryService: Optional[str]
    RegistryVip: Optional[Sequence["_RegistryVipDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OshiftRegistryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OshiftRegistryDefinition"]:
        if not json_data:
            return None
        return cls(
            RegistryNamespace=json_data.get("RegistryNamespace"),
            RegistryService=json_data.get("RegistryService"),
            RegistryVip=deserialize_list(json_data.get("RegistryVip"), RegistryVipDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OshiftRegistryDefinition = OshiftRegistryDefinition


@dataclass
class RegistryVipDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegistryVipDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegistryVipDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegistryVipDefinition = RegistryVipDefinition


@dataclass
class EastWestPlacementSubnetDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EastWestPlacementSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EastWestPlacementSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EastWestPlacementSubnetDefinition = EastWestPlacementSubnetDefinition


@dataclass
class IpAddrDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddrDefinition = IpAddrDefinition


@dataclass
class SeExcludeAttributesDefinition(BaseModel):
    Attribute: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SeExcludeAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeExcludeAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeExcludeAttributesDefinition = SeExcludeAttributesDefinition


@dataclass
class SeIncludeAttributesDefinition(BaseModel):
    Attribute: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SeIncludeAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeIncludeAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeIncludeAttributesDefinition = SeIncludeAttributesDefinition


@dataclass
class GcpConfigurationDefinition(BaseModel):
    CloudCredentialsRef: Optional[str]
    FirewallTargetTags: Optional[Sequence[str]]
    GcsBucketName: Optional[str]
    GcsProjectId: Optional[str]
    RegionName: Optional[str]
    SeProjectId: Optional[str]
    Zones: Optional[Sequence[str]]
    EncryptionKeys: Optional[Sequence["_EncryptionKeysDefinition"]]
    NetworkConfig: Optional[Sequence["_NetworkConfigDefinition"]]
    VipAllocationStrategy: Optional[Sequence["_VipAllocationStrategyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GcpConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcpConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudCredentialsRef=json_data.get("CloudCredentialsRef"),
            FirewallTargetTags=json_data.get("FirewallTargetTags"),
            GcsBucketName=json_data.get("GcsBucketName"),
            GcsProjectId=json_data.get("GcsProjectId"),
            RegionName=json_data.get("RegionName"),
            SeProjectId=json_data.get("SeProjectId"),
            Zones=json_data.get("Zones"),
            EncryptionKeys=deserialize_list(json_data.get("EncryptionKeys"), EncryptionKeysDefinition),
            NetworkConfig=deserialize_list(json_data.get("NetworkConfig"), NetworkConfigDefinition),
            VipAllocationStrategy=deserialize_list(json_data.get("VipAllocationStrategy"), VipAllocationStrategyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcpConfigurationDefinition = GcpConfigurationDefinition


@dataclass
class EncryptionKeysDefinition(BaseModel):
    GcsBucketKmsKeyId: Optional[str]
    GcsObjectsKmsKeyId: Optional[str]
    SeDiskKmsKeyId: Optional[str]
    SeImageKmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionKeysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionKeysDefinition"]:
        if not json_data:
            return None
        return cls(
            GcsBucketKmsKeyId=json_data.get("GcsBucketKmsKeyId"),
            GcsObjectsKmsKeyId=json_data.get("GcsObjectsKmsKeyId"),
            SeDiskKmsKeyId=json_data.get("SeDiskKmsKeyId"),
            SeImageKmsKeyId=json_data.get("SeImageKmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionKeysDefinition = EncryptionKeysDefinition


@dataclass
class NetworkConfigDefinition(BaseModel):
    Config: Optional[str]
    Inband: Optional[Sequence["_InbandDefinition"]]
    OneArm: Optional[Sequence["_OneArmDefinition"]]
    TwoArm: Optional[Sequence["_TwoArmDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Config=json_data.get("Config"),
            Inband=deserialize_list(json_data.get("Inband"), InbandDefinition),
            OneArm=deserialize_list(json_data.get("OneArm"), OneArmDefinition),
            TwoArm=deserialize_list(json_data.get("TwoArm"), TwoArmDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfigDefinition = NetworkConfigDefinition


@dataclass
class InbandDefinition(BaseModel):
    VpcNetworkName: Optional[str]
    VpcProjectId: Optional[str]
    VpcSubnetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InbandDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InbandDefinition"]:
        if not json_data:
            return None
        return cls(
            VpcNetworkName=json_data.get("VpcNetworkName"),
            VpcProjectId=json_data.get("VpcProjectId"),
            VpcSubnetName=json_data.get("VpcSubnetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InbandDefinition = InbandDefinition


@dataclass
class OneArmDefinition(BaseModel):
    DataVpcNetworkName: Optional[str]
    DataVpcProjectId: Optional[str]
    DataVpcSubnetName: Optional[str]
    ManagementVpcNetworkName: Optional[str]
    ManagementVpcProjectId: Optional[str]
    ManagementVpcSubnetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OneArmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OneArmDefinition"]:
        if not json_data:
            return None
        return cls(
            DataVpcNetworkName=json_data.get("DataVpcNetworkName"),
            DataVpcProjectId=json_data.get("DataVpcProjectId"),
            DataVpcSubnetName=json_data.get("DataVpcSubnetName"),
            ManagementVpcNetworkName=json_data.get("ManagementVpcNetworkName"),
            ManagementVpcProjectId=json_data.get("ManagementVpcProjectId"),
            ManagementVpcSubnetName=json_data.get("ManagementVpcSubnetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OneArmDefinition = OneArmDefinition


@dataclass
class TwoArmDefinition(BaseModel):
    BackendDataVpcNetworkName: Optional[str]
    BackendDataVpcProjectId: Optional[str]
    BackendDataVpcSubnetName: Optional[str]
    FrontendDataVpcNetworkName: Optional[str]
    FrontendDataVpcProjectId: Optional[str]
    FrontendDataVpcSubnetName: Optional[str]
    ManagementVpcNetworkName: Optional[str]
    ManagementVpcProjectId: Optional[str]
    ManagementVpcSubnetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TwoArmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TwoArmDefinition"]:
        if not json_data:
            return None
        return cls(
            BackendDataVpcNetworkName=json_data.get("BackendDataVpcNetworkName"),
            BackendDataVpcProjectId=json_data.get("BackendDataVpcProjectId"),
            BackendDataVpcSubnetName=json_data.get("BackendDataVpcSubnetName"),
            FrontendDataVpcNetworkName=json_data.get("FrontendDataVpcNetworkName"),
            FrontendDataVpcProjectId=json_data.get("FrontendDataVpcProjectId"),
            FrontendDataVpcSubnetName=json_data.get("FrontendDataVpcSubnetName"),
            ManagementVpcNetworkName=json_data.get("ManagementVpcNetworkName"),
            ManagementVpcProjectId=json_data.get("ManagementVpcProjectId"),
            ManagementVpcSubnetName=json_data.get("ManagementVpcSubnetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TwoArmDefinition = TwoArmDefinition


@dataclass
class VipAllocationStrategyDefinition(BaseModel):
    Mode: Optional[str]
    Ilb: Optional[Sequence["_IlbDefinition"]]
    Routes: Optional[Sequence["_RoutesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VipAllocationStrategyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VipAllocationStrategyDefinition"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            Ilb=deserialize_list(json_data.get("Ilb"), IlbDefinition),
            Routes=deserialize_list(json_data.get("Routes"), RoutesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VipAllocationStrategyDefinition = VipAllocationStrategyDefinition


@dataclass
class IlbDefinition(BaseModel):
    CloudRouterNames: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IlbDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IlbDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudRouterNames=json_data.get("CloudRouterNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IlbDefinition = IlbDefinition


@dataclass
class RoutesDefinition(BaseModel):
    MatchSeGroupSubnet: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchSeGroupSubnet=json_data.get("MatchSeGroupSubnet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutesDefinition = RoutesDefinition


@dataclass
class LinuxserverConfigurationDefinition(BaseModel):
    SeInbandMgmt: Optional[bool]
    SeLogDiskPath: Optional[str]
    SeLogDiskSizeGb: Optional[float]
    SeSysDiskPath: Optional[str]
    SeSysDiskSizeGb: Optional[float]
    SshUserRef: Optional[str]
    Hosts: Optional[Sequence["_HostsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LinuxserverConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinuxserverConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            SeInbandMgmt=json_data.get("SeInbandMgmt"),
            SeLogDiskPath=json_data.get("SeLogDiskPath"),
            SeLogDiskSizeGb=json_data.get("SeLogDiskSizeGb"),
            SeSysDiskPath=json_data.get("SeSysDiskPath"),
            SeSysDiskSizeGb=json_data.get("SeSysDiskSizeGb"),
            SshUserRef=json_data.get("SshUserRef"),
            Hosts=deserialize_list(json_data.get("Hosts"), HostsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinuxserverConfigurationDefinition = LinuxserverConfigurationDefinition


@dataclass
class HostsDefinition(BaseModel):
    NodeAvailabilityZone: Optional[str]
    SeGroupRef: Optional[str]
    HostAttr: Optional[Sequence["_HostAttrDefinition"]]
    HostIp: Optional[Sequence["_HostIpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HostsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostsDefinition"]:
        if not json_data:
            return None
        return cls(
            NodeAvailabilityZone=json_data.get("NodeAvailabilityZone"),
            SeGroupRef=json_data.get("SeGroupRef"),
            HostAttr=deserialize_list(json_data.get("HostAttr"), HostAttrDefinition),
            HostIp=deserialize_list(json_data.get("HostIp"), HostIpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostsDefinition = HostsDefinition


@dataclass
class HostAttrDefinition(BaseModel):
    AttrKey: Optional[str]
    AttrVal: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostAttrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostAttrDefinition"]:
        if not json_data:
            return None
        return cls(
            AttrKey=json_data.get("AttrKey"),
            AttrVal=json_data.get("AttrVal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostAttrDefinition = HostAttrDefinition


@dataclass
class HostIpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostIpDefinition = HostIpDefinition


@dataclass
class NsxConfigurationDefinition(BaseModel):
    AviNsxPrefix: Optional[str]
    NsxManagerName: Optional[str]
    NsxManagerPassword: Optional[str]
    NsxManagerUsername: Optional[str]
    NsxPollTime: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NsxConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NsxConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AviNsxPrefix=json_data.get("AviNsxPrefix"),
            NsxManagerName=json_data.get("NsxManagerName"),
            NsxManagerPassword=json_data.get("NsxManagerPassword"),
            NsxManagerUsername=json_data.get("NsxManagerUsername"),
            NsxPollTime=json_data.get("NsxPollTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NsxConfigurationDefinition = NsxConfigurationDefinition


@dataclass
class NsxtConfigurationDefinition(BaseModel):
    AutomateDfwRules: Optional[bool]
    DomainId: Optional[str]
    EnforcementpointId: Optional[str]
    NsxtCredentialsRef: Optional[str]
    NsxtUrl: Optional[str]
    SiteId: Optional[str]
    DataNetworkConfig: Optional[Sequence["_DataNetworkConfigDefinition"]]
    ManagementNetworkConfig: Optional[Sequence["_ManagementNetworkConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NsxtConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NsxtConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AutomateDfwRules=json_data.get("AutomateDfwRules"),
            DomainId=json_data.get("DomainId"),
            EnforcementpointId=json_data.get("EnforcementpointId"),
            NsxtCredentialsRef=json_data.get("NsxtCredentialsRef"),
            NsxtUrl=json_data.get("NsxtUrl"),
            SiteId=json_data.get("SiteId"),
            DataNetworkConfig=deserialize_list(json_data.get("DataNetworkConfig"), DataNetworkConfigDefinition),
            ManagementNetworkConfig=deserialize_list(json_data.get("ManagementNetworkConfig"), ManagementNetworkConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NsxtConfigurationDefinition = NsxtConfigurationDefinition


@dataclass
class DataNetworkConfigDefinition(BaseModel):
    TransportZone: Optional[str]
    TzType: Optional[str]
    VlanSegments: Optional[Sequence[str]]
    Tier1SegmentConfig: Optional[Sequence["_Tier1SegmentConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DataNetworkConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataNetworkConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            TransportZone=json_data.get("TransportZone"),
            TzType=json_data.get("TzType"),
            VlanSegments=json_data.get("VlanSegments"),
            Tier1SegmentConfig=deserialize_list(json_data.get("Tier1SegmentConfig"), Tier1SegmentConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataNetworkConfigDefinition = DataNetworkConfigDefinition


@dataclass
class Tier1SegmentConfigDefinition(BaseModel):
    SegmentConfigMode: Optional[str]
    Automatic: Optional[Sequence["_AutomaticDefinition"]]
    Manual: Optional[Sequence["_ManualDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Tier1SegmentConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tier1SegmentConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            SegmentConfigMode=json_data.get("SegmentConfigMode"),
            Automatic=deserialize_list(json_data.get("Automatic"), AutomaticDefinition),
            Manual=deserialize_list(json_data.get("Manual"), ManualDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tier1SegmentConfigDefinition = Tier1SegmentConfigDefinition


@dataclass
class AutomaticDefinition(BaseModel):
    NumSePerSegment: Optional[float]
    Tier1LrIds: Optional[Sequence[str]]
    NsxtSegmentSubnet: Optional[Sequence["_NsxtSegmentSubnetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutomaticDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutomaticDefinition"]:
        if not json_data:
            return None
        return cls(
            NumSePerSegment=json_data.get("NumSePerSegment"),
            Tier1LrIds=json_data.get("Tier1LrIds"),
            NsxtSegmentSubnet=deserialize_list(json_data.get("NsxtSegmentSubnet"), NsxtSegmentSubnetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutomaticDefinition = AutomaticDefinition


@dataclass
class NsxtSegmentSubnetDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NsxtSegmentSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NsxtSegmentSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NsxtSegmentSubnetDefinition = NsxtSegmentSubnetDefinition


@dataclass
class ManualDefinition(BaseModel):
    Tier1Lrs: Optional[Sequence["_Tier1LrsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ManualDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManualDefinition"]:
        if not json_data:
            return None
        return cls(
            Tier1Lrs=deserialize_list(json_data.get("Tier1Lrs"), Tier1LrsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManualDefinition = ManualDefinition


@dataclass
class Tier1LrsDefinition(BaseModel):
    SegmentId: Optional[str]
    Tier1LrId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tier1LrsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tier1LrsDefinition"]:
        if not json_data:
            return None
        return cls(
            SegmentId=json_data.get("SegmentId"),
            Tier1LrId=json_data.get("Tier1LrId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tier1LrsDefinition = Tier1LrsDefinition


@dataclass
class ManagementNetworkConfigDefinition(BaseModel):
    TransportZone: Optional[str]
    TzType: Optional[str]
    VlanSegment: Optional[str]
    OverlaySegment: Optional[Sequence["_OverlaySegmentDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ManagementNetworkConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagementNetworkConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            TransportZone=json_data.get("TransportZone"),
            TzType=json_data.get("TzType"),
            VlanSegment=json_data.get("VlanSegment"),
            OverlaySegment=deserialize_list(json_data.get("OverlaySegment"), OverlaySegmentDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagementNetworkConfigDefinition = ManagementNetworkConfigDefinition


@dataclass
class OverlaySegmentDefinition(BaseModel):
    SegmentId: Optional[str]
    Tier1LrId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OverlaySegmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverlaySegmentDefinition"]:
        if not json_data:
            return None
        return cls(
            SegmentId=json_data.get("SegmentId"),
            Tier1LrId=json_data.get("Tier1LrId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverlaySegmentDefinition = OverlaySegmentDefinition


@dataclass
class OpenstackConfigurationDefinition(BaseModel):
    AdminTenant: Optional[str]
    AdminTenantUuid: Optional[str]
    AllowedAddressPairs: Optional[bool]
    AntiAffinity: Optional[bool]
    AuthUrl: Optional[str]
    ConfigDrive: Optional[bool]
    ContrailDisablePolicy: Optional[bool]
    ContrailEndpoint: Optional[str]
    ContrailPlugin: Optional[bool]
    ExternalNetworks: Optional[bool]
    FreeFloatingips: Optional[bool]
    Hypervisor: Optional[str]
    ImgFormat: Optional[str]
    ImportKeystoneTenants: Optional[bool]
    Insecure: Optional[bool]
    KeystoneHost: Optional[str]
    MapAdminToCloudadmin: Optional[bool]
    MgmtNetworkName: Optional[str]
    MgmtNetworkUuid: Optional[str]
    NameOwner: Optional[bool]
    NeutronRbac: Optional[bool]
    Password: Optional[str]
    Privilege: Optional[str]
    ProvName: Optional[Sequence[str]]
    Region: Optional[str]
    SecurityGroups: Optional[bool]
    TenantSe: Optional[bool]
    UseAdminUrl: Optional[bool]
    UseInternalEndpoints: Optional[bool]
    UseKeystoneAuth: Optional[bool]
    Username: Optional[str]
    CustomSeImageProperties: Optional[Sequence["_CustomSeImagePropertiesDefinition"]]
    HypervisorProperties: Optional[Sequence["_HypervisorPropertiesDefinition"]]
    ProviderVipNetworks: Optional[Sequence["_ProviderVipNetworksDefinition"]]
    RoleMapping: Optional[Sequence["_RoleMappingDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OpenstackConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenstackConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminTenant=json_data.get("AdminTenant"),
            AdminTenantUuid=json_data.get("AdminTenantUuid"),
            AllowedAddressPairs=json_data.get("AllowedAddressPairs"),
            AntiAffinity=json_data.get("AntiAffinity"),
            AuthUrl=json_data.get("AuthUrl"),
            ConfigDrive=json_data.get("ConfigDrive"),
            ContrailDisablePolicy=json_data.get("ContrailDisablePolicy"),
            ContrailEndpoint=json_data.get("ContrailEndpoint"),
            ContrailPlugin=json_data.get("ContrailPlugin"),
            ExternalNetworks=json_data.get("ExternalNetworks"),
            FreeFloatingips=json_data.get("FreeFloatingips"),
            Hypervisor=json_data.get("Hypervisor"),
            ImgFormat=json_data.get("ImgFormat"),
            ImportKeystoneTenants=json_data.get("ImportKeystoneTenants"),
            Insecure=json_data.get("Insecure"),
            KeystoneHost=json_data.get("KeystoneHost"),
            MapAdminToCloudadmin=json_data.get("MapAdminToCloudadmin"),
            MgmtNetworkName=json_data.get("MgmtNetworkName"),
            MgmtNetworkUuid=json_data.get("MgmtNetworkUuid"),
            NameOwner=json_data.get("NameOwner"),
            NeutronRbac=json_data.get("NeutronRbac"),
            Password=json_data.get("Password"),
            Privilege=json_data.get("Privilege"),
            ProvName=json_data.get("ProvName"),
            Region=json_data.get("Region"),
            SecurityGroups=json_data.get("SecurityGroups"),
            TenantSe=json_data.get("TenantSe"),
            UseAdminUrl=json_data.get("UseAdminUrl"),
            UseInternalEndpoints=json_data.get("UseInternalEndpoints"),
            UseKeystoneAuth=json_data.get("UseKeystoneAuth"),
            Username=json_data.get("Username"),
            CustomSeImageProperties=deserialize_list(json_data.get("CustomSeImageProperties"), CustomSeImagePropertiesDefinition),
            HypervisorProperties=deserialize_list(json_data.get("HypervisorProperties"), HypervisorPropertiesDefinition),
            ProviderVipNetworks=deserialize_list(json_data.get("ProviderVipNetworks"), ProviderVipNetworksDefinition),
            RoleMapping=deserialize_list(json_data.get("RoleMapping"), RoleMappingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenstackConfigurationDefinition = OpenstackConfigurationDefinition


@dataclass
class CustomSeImagePropertiesDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomSeImagePropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomSeImagePropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomSeImagePropertiesDefinition = CustomSeImagePropertiesDefinition


@dataclass
class HypervisorPropertiesDefinition(BaseModel):
    Hypervisor: Optional[str]
    ImageProperties: Optional[Sequence["_ImagePropertiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HypervisorPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HypervisorPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Hypervisor=json_data.get("Hypervisor"),
            ImageProperties=deserialize_list(json_data.get("ImageProperties"), ImagePropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HypervisorPropertiesDefinition = HypervisorPropertiesDefinition


@dataclass
class ImagePropertiesDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImagePropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImagePropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImagePropertiesDefinition = ImagePropertiesDefinition


@dataclass
class ProviderVipNetworksDefinition(BaseModel):
    OsNetworkUuid: Optional[str]
    OsTenantUuids: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ProviderVipNetworksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProviderVipNetworksDefinition"]:
        if not json_data:
            return None
        return cls(
            OsNetworkUuid=json_data.get("OsNetworkUuid"),
            OsTenantUuids=json_data.get("OsTenantUuids"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProviderVipNetworksDefinition = ProviderVipNetworksDefinition


@dataclass
class RoleMappingDefinition(BaseModel):
    AviRole: Optional[str]
    OsRole: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RoleMappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoleMappingDefinition"]:
        if not json_data:
            return None
        return cls(
            AviRole=json_data.get("AviRole"),
            OsRole=json_data.get("OsRole"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoleMappingDefinition = RoleMappingDefinition


@dataclass
class ProxyConfigurationDefinition(BaseModel):
    Host: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProxyConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProxyConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProxyConfigurationDefinition = ProxyConfigurationDefinition


@dataclass
class RancherConfigurationDefinition(BaseModel):
    AccessKey: Optional[str]
    AppSyncFrequency: Optional[float]
    ContainerPortMatchHttpService: Optional[bool]
    CoredumpDirectory: Optional[str]
    DisableAutoBackendServiceSync: Optional[bool]
    DisableAutoFrontendServiceSync: Optional[bool]
    DisableAutoSeCreation: Optional[bool]
    EnableEventSubscription: Optional[bool]
    FeproxyContainerPortAsService: Optional[bool]
    FeproxyVipsEnableProxyArp: Optional[bool]
    FleetEndpoint: Optional[str]
    HttpContainerPorts: Optional[Sequence[float]]
    RancherServers: Optional[Sequence[str]]
    SeDeploymentMethod: Optional[str]
    SeSpawnRate: Optional[float]
    SeVolume: Optional[str]
    SecretKey: Optional[str]
    ServicesAccessibleAllInterfaces: Optional[bool]
    SshUserRef: Optional[str]
    UseContainerIpPort: Optional[bool]
    UseControllerImage: Optional[bool]
    DockerRegistrySe: Optional[Sequence["_DockerRegistrySeDefinition"]]
    EastWestPlacementSubnet: Optional[Sequence["_EastWestPlacementSubnetDefinition"]]
    NuageController: Optional[Sequence["_NuageControllerDefinition"]]
    SeExcludeAttributes: Optional[Sequence["_SeExcludeAttributesDefinition"]]
    SeIncludeAttributes: Optional[Sequence["_SeIncludeAttributesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RancherConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RancherConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            AppSyncFrequency=json_data.get("AppSyncFrequency"),
            ContainerPortMatchHttpService=json_data.get("ContainerPortMatchHttpService"),
            CoredumpDirectory=json_data.get("CoredumpDirectory"),
            DisableAutoBackendServiceSync=json_data.get("DisableAutoBackendServiceSync"),
            DisableAutoFrontendServiceSync=json_data.get("DisableAutoFrontendServiceSync"),
            DisableAutoSeCreation=json_data.get("DisableAutoSeCreation"),
            EnableEventSubscription=json_data.get("EnableEventSubscription"),
            FeproxyContainerPortAsService=json_data.get("FeproxyContainerPortAsService"),
            FeproxyVipsEnableProxyArp=json_data.get("FeproxyVipsEnableProxyArp"),
            FleetEndpoint=json_data.get("FleetEndpoint"),
            HttpContainerPorts=json_data.get("HttpContainerPorts"),
            RancherServers=json_data.get("RancherServers"),
            SeDeploymentMethod=json_data.get("SeDeploymentMethod"),
            SeSpawnRate=json_data.get("SeSpawnRate"),
            SeVolume=json_data.get("SeVolume"),
            SecretKey=json_data.get("SecretKey"),
            ServicesAccessibleAllInterfaces=json_data.get("ServicesAccessibleAllInterfaces"),
            SshUserRef=json_data.get("SshUserRef"),
            UseContainerIpPort=json_data.get("UseContainerIpPort"),
            UseControllerImage=json_data.get("UseControllerImage"),
            DockerRegistrySe=deserialize_list(json_data.get("DockerRegistrySe"), DockerRegistrySeDefinition),
            EastWestPlacementSubnet=deserialize_list(json_data.get("EastWestPlacementSubnet"), EastWestPlacementSubnetDefinition),
            NuageController=deserialize_list(json_data.get("NuageController"), NuageControllerDefinition),
            SeExcludeAttributes=deserialize_list(json_data.get("SeExcludeAttributes"), SeExcludeAttributesDefinition),
            SeIncludeAttributes=deserialize_list(json_data.get("SeIncludeAttributes"), SeIncludeAttributesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RancherConfigurationDefinition = RancherConfigurationDefinition


@dataclass
class NuageControllerDefinition(BaseModel):
    NuageOrganization: Optional[str]
    NuagePassword: Optional[str]
    NuagePort: Optional[float]
    NuageUsername: Optional[str]
    NuageVsdHost: Optional[str]
    SeDomain: Optional[str]
    SeEnterprise: Optional[str]
    SeNetwork: Optional[str]
    SePolicyGroup: Optional[str]
    SeUser: Optional[str]
    SeZone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NuageControllerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NuageControllerDefinition"]:
        if not json_data:
            return None
        return cls(
            NuageOrganization=json_data.get("NuageOrganization"),
            NuagePassword=json_data.get("NuagePassword"),
            NuagePort=json_data.get("NuagePort"),
            NuageUsername=json_data.get("NuageUsername"),
            NuageVsdHost=json_data.get("NuageVsdHost"),
            SeDomain=json_data.get("SeDomain"),
            SeEnterprise=json_data.get("SeEnterprise"),
            SeNetwork=json_data.get("SeNetwork"),
            SePolicyGroup=json_data.get("SePolicyGroup"),
            SeUser=json_data.get("SeUser"),
            SeZone=json_data.get("SeZone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NuageControllerDefinition = NuageControllerDefinition


@dataclass
class VcaConfigurationDefinition(BaseModel):
    Privilege: Optional[str]
    VcaHost: Optional[str]
    VcaInstance: Optional[str]
    VcaMgmtNetwork: Optional[str]
    VcaOrgnization: Optional[str]
    VcaPassword: Optional[str]
    VcaUsername: Optional[str]
    VcaVdc: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VcaConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VcaConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Privilege=json_data.get("Privilege"),
            VcaHost=json_data.get("VcaHost"),
            VcaInstance=json_data.get("VcaInstance"),
            VcaMgmtNetwork=json_data.get("VcaMgmtNetwork"),
            VcaOrgnization=json_data.get("VcaOrgnization"),
            VcaPassword=json_data.get("VcaPassword"),
            VcaUsername=json_data.get("VcaUsername"),
            VcaVdc=json_data.get("VcaVdc"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VcaConfigurationDefinition = VcaConfigurationDefinition


@dataclass
class VcenterConfigurationDefinition(BaseModel):
    Datacenter: Optional[str]
    DeactivateVmDiscovery: Optional[bool]
    ManagementNetwork: Optional[str]
    Password: Optional[str]
    Privilege: Optional[str]
    Username: Optional[str]
    VcenterTemplateSeLocation: Optional[str]
    VcenterUrl: Optional[str]
    ManagementIpSubnet: Optional[Sequence["_ManagementIpSubnetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VcenterConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VcenterConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Datacenter=json_data.get("Datacenter"),
            DeactivateVmDiscovery=json_data.get("DeactivateVmDiscovery"),
            ManagementNetwork=json_data.get("ManagementNetwork"),
            Password=json_data.get("Password"),
            Privilege=json_data.get("Privilege"),
            Username=json_data.get("Username"),
            VcenterTemplateSeLocation=json_data.get("VcenterTemplateSeLocation"),
            VcenterUrl=json_data.get("VcenterUrl"),
            ManagementIpSubnet=deserialize_list(json_data.get("ManagementIpSubnet"), ManagementIpSubnetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VcenterConfigurationDefinition = VcenterConfigurationDefinition


@dataclass
class ManagementIpSubnetDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ManagementIpSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagementIpSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagementIpSubnetDefinition = ManagementIpSubnetDefinition


