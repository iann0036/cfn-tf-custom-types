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
    AddonJobTimeout: Optional[float]
    Addons: Optional[str]
    AddonsInclude: Optional[Sequence[str]]
    ApiServerUrl: Optional[str]
    CaCrt: Optional[str]
    CertDir: Optional[str]
    Certificates: Optional[Sequence["_CertificatesDefinition"]]
    ClientCert: Optional[str]
    ClientKey: Optional[str]
    ClusterCidr: Optional[str]
    ClusterDnsServer: Optional[str]
    ClusterDomain: Optional[str]
    ClusterName: Optional[str]
    ClusterYaml: Optional[str]
    ControlPlaneHosts: Optional[Sequence["_ControlPlaneHostsDefinition"]]
    CustomCerts: Optional[bool]
    DelayOnCreation: Optional[float]
    Dind: Optional[bool]
    DindDnsServer: Optional[str]
    DindStorageDriver: Optional[str]
    DisablePortCheck: Optional[bool]
    EtcdHosts: Optional[Sequence["_EtcdHostsDefinition"]]
    Id: Optional[str]
    IgnoreDockerVersion: Optional[bool]
    InactiveHosts: Optional[Sequence["_InactiveHostsDefinition"]]
    InternalKubeConfigYaml: Optional[str]
    KubeAdminUser: Optional[str]
    KubeConfigYaml: Optional[str]
    KubernetesVersion: Optional[str]
    NodesConf: Optional[Sequence[str]]
    PrefixPath: Optional[str]
    RkeClusterYaml: Optional[str]
    RkeState: Optional[str]
    RunningSystemImages: Optional[Sequence["_RunningSystemImagesDefinition"]]
    SshAgentAuth: Optional[bool]
    SshCertPath: Optional[str]
    SshKeyPath: Optional[str]
    UpdateOnly: Optional[bool]
    WorkerHosts: Optional[Sequence["_WorkerHostsDefinition"]]
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
    Restore: Optional[Sequence["_RestoreDefinition"]]
    RotateCertificates: Optional[Sequence["_RotateCertificatesDefinition"]]
    Services: Optional[Sequence["_ServicesDefinition"]]
    ServicesEtcd: Optional[Sequence["_ServicesEtcdDefinition"]]
    ServicesKubeApi: Optional[Sequence["_ServicesKubeApiDefinition"]]
    ServicesKubeController: Optional[Sequence["_ServicesKubeControllerDefinition"]]
    ServicesKubelet: Optional[Sequence["_ServicesKubeletDefinition"]]
    ServicesKubeproxy: Optional[Sequence["_ServicesKubeproxyDefinition"]]
    ServicesScheduler: Optional[Sequence["_ServicesSchedulerDefinition"]]
    SystemImages: Optional[Sequence["_SystemImagesDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    UpgradeStrategy: Optional[Sequence["_UpgradeStrategyDefinition"]]

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
            AddonJobTimeout=json_data.get("AddonJobTimeout"),
            Addons=json_data.get("Addons"),
            AddonsInclude=json_data.get("AddonsInclude"),
            ApiServerUrl=json_data.get("ApiServerUrl"),
            CaCrt=json_data.get("CaCrt"),
            CertDir=json_data.get("CertDir"),
            Certificates=deserialize_list(json_data.get("Certificates"), CertificatesDefinition),
            ClientCert=json_data.get("ClientCert"),
            ClientKey=json_data.get("ClientKey"),
            ClusterCidr=json_data.get("ClusterCidr"),
            ClusterDnsServer=json_data.get("ClusterDnsServer"),
            ClusterDomain=json_data.get("ClusterDomain"),
            ClusterName=json_data.get("ClusterName"),
            ClusterYaml=json_data.get("ClusterYaml"),
            ControlPlaneHosts=deserialize_list(json_data.get("ControlPlaneHosts"), ControlPlaneHostsDefinition),
            CustomCerts=json_data.get("CustomCerts"),
            DelayOnCreation=json_data.get("DelayOnCreation"),
            Dind=json_data.get("Dind"),
            DindDnsServer=json_data.get("DindDnsServer"),
            DindStorageDriver=json_data.get("DindStorageDriver"),
            DisablePortCheck=json_data.get("DisablePortCheck"),
            EtcdHosts=deserialize_list(json_data.get("EtcdHosts"), EtcdHostsDefinition),
            Id=json_data.get("Id"),
            IgnoreDockerVersion=json_data.get("IgnoreDockerVersion"),
            InactiveHosts=deserialize_list(json_data.get("InactiveHosts"), InactiveHostsDefinition),
            InternalKubeConfigYaml=json_data.get("InternalKubeConfigYaml"),
            KubeAdminUser=json_data.get("KubeAdminUser"),
            KubeConfigYaml=json_data.get("KubeConfigYaml"),
            KubernetesVersion=json_data.get("KubernetesVersion"),
            NodesConf=json_data.get("NodesConf"),
            PrefixPath=json_data.get("PrefixPath"),
            RkeClusterYaml=json_data.get("RkeClusterYaml"),
            RkeState=json_data.get("RkeState"),
            RunningSystemImages=deserialize_list(json_data.get("RunningSystemImages"), RunningSystemImagesDefinition),
            SshAgentAuth=json_data.get("SshAgentAuth"),
            SshCertPath=json_data.get("SshCertPath"),
            SshKeyPath=json_data.get("SshKeyPath"),
            UpdateOnly=json_data.get("UpdateOnly"),
            WorkerHosts=deserialize_list(json_data.get("WorkerHosts"), WorkerHostsDefinition),
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
            Restore=deserialize_list(json_data.get("Restore"), RestoreDefinition),
            RotateCertificates=deserialize_list(json_data.get("RotateCertificates"), RotateCertificatesDefinition),
            Services=deserialize_list(json_data.get("Services"), ServicesDefinition),
            ServicesEtcd=deserialize_list(json_data.get("ServicesEtcd"), ServicesEtcdDefinition),
            ServicesKubeApi=deserialize_list(json_data.get("ServicesKubeApi"), ServicesKubeApiDefinition),
            ServicesKubeController=deserialize_list(json_data.get("ServicesKubeController"), ServicesKubeControllerDefinition),
            ServicesKubelet=deserialize_list(json_data.get("ServicesKubelet"), ServicesKubeletDefinition),
            ServicesKubeproxy=deserialize_list(json_data.get("ServicesKubeproxy"), ServicesKubeproxyDefinition),
            ServicesScheduler=deserialize_list(json_data.get("ServicesScheduler"), ServicesSchedulerDefinition),
            SystemImages=deserialize_list(json_data.get("SystemImages"), SystemImagesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            UpgradeStrategy=deserialize_list(json_data.get("UpgradeStrategy"), UpgradeStrategyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CertificatesDefinition(BaseModel):
    Certificate: Optional[str]
    CommonName: Optional[str]
    Config: Optional[str]
    ConfigEnvName: Optional[str]
    ConfigPath: Optional[str]
    EnvName: Optional[str]
    Id: Optional[str]
    Key: Optional[str]
    KeyEnvName: Optional[str]
    KeyPath: Optional[str]
    Name: Optional[str]
    OuName: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificatesDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            CommonName=json_data.get("CommonName"),
            Config=json_data.get("Config"),
            ConfigEnvName=json_data.get("ConfigEnvName"),
            ConfigPath=json_data.get("ConfigPath"),
            EnvName=json_data.get("EnvName"),
            Id=json_data.get("Id"),
            Key=json_data.get("Key"),
            KeyEnvName=json_data.get("KeyEnvName"),
            KeyPath=json_data.get("KeyPath"),
            Name=json_data.get("Name"),
            OuName=json_data.get("OuName"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificatesDefinition = CertificatesDefinition


@dataclass
class ControlPlaneHostsDefinition(BaseModel):
    Address: Optional[str]
    NodeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ControlPlaneHostsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ControlPlaneHostsDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            NodeName=json_data.get("NodeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ControlPlaneHostsDefinition = ControlPlaneHostsDefinition


@dataclass
class EtcdHostsDefinition(BaseModel):
    Address: Optional[str]
    NodeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EtcdHostsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EtcdHostsDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            NodeName=json_data.get("NodeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EtcdHostsDefinition = EtcdHostsDefinition


@dataclass
class InactiveHostsDefinition(BaseModel):
    Address: Optional[str]
    NodeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InactiveHostsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InactiveHostsDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            NodeName=json_data.get("NodeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InactiveHostsDefinition = InactiveHostsDefinition


@dataclass
class RunningSystemImagesDefinition(BaseModel):
    AciCniDeployContainer: Optional[str]
    AciControllerContainer: Optional[str]
    AciHostContainer: Optional[str]
    AciMcastContainer: Optional[str]
    AciOpflexContainer: Optional[str]
    AciOvsContainer: Optional[str]
    Alpine: Optional[str]
    CalicoCni: Optional[str]
    CalicoControllers: Optional[str]
    CalicoCtl: Optional[str]
    CalicoFlexVol: Optional[str]
    CalicoNode: Optional[str]
    CanalCni: Optional[str]
    CanalFlannel: Optional[str]
    CanalFlexVol: Optional[str]
    CanalNode: Optional[str]
    CertDownloader: Optional[str]
    Coredns: Optional[str]
    CorednsAutoscaler: Optional[str]
    Dnsmasq: Optional[str]
    Etcd: Optional[str]
    Flannel: Optional[str]
    FlannelCni: Optional[str]
    Ingress: Optional[str]
    IngressBackend: Optional[str]
    KubeDns: Optional[str]
    KubeDnsAutoscaler: Optional[str]
    KubeDnsSidecar: Optional[str]
    Kubernetes: Optional[str]
    KubernetesServicesSidecar: Optional[str]
    MetricsServer: Optional[str]
    NginxProxy: Optional[str]
    Nodelocal: Optional[str]
    PodInfraContainer: Optional[str]
    WeaveCni: Optional[str]
    WeaveNode: Optional[str]
    WindowsPodInfraContainer: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RunningSystemImagesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunningSystemImagesDefinition"]:
        if not json_data:
            return None
        return cls(
            AciCniDeployContainer=json_data.get("AciCniDeployContainer"),
            AciControllerContainer=json_data.get("AciControllerContainer"),
            AciHostContainer=json_data.get("AciHostContainer"),
            AciMcastContainer=json_data.get("AciMcastContainer"),
            AciOpflexContainer=json_data.get("AciOpflexContainer"),
            AciOvsContainer=json_data.get("AciOvsContainer"),
            Alpine=json_data.get("Alpine"),
            CalicoCni=json_data.get("CalicoCni"),
            CalicoControllers=json_data.get("CalicoControllers"),
            CalicoCtl=json_data.get("CalicoCtl"),
            CalicoFlexVol=json_data.get("CalicoFlexVol"),
            CalicoNode=json_data.get("CalicoNode"),
            CanalCni=json_data.get("CanalCni"),
            CanalFlannel=json_data.get("CanalFlannel"),
            CanalFlexVol=json_data.get("CanalFlexVol"),
            CanalNode=json_data.get("CanalNode"),
            CertDownloader=json_data.get("CertDownloader"),
            Coredns=json_data.get("Coredns"),
            CorednsAutoscaler=json_data.get("CorednsAutoscaler"),
            Dnsmasq=json_data.get("Dnsmasq"),
            Etcd=json_data.get("Etcd"),
            Flannel=json_data.get("Flannel"),
            FlannelCni=json_data.get("FlannelCni"),
            Ingress=json_data.get("Ingress"),
            IngressBackend=json_data.get("IngressBackend"),
            KubeDns=json_data.get("KubeDns"),
            KubeDnsAutoscaler=json_data.get("KubeDnsAutoscaler"),
            KubeDnsSidecar=json_data.get("KubeDnsSidecar"),
            Kubernetes=json_data.get("Kubernetes"),
            KubernetesServicesSidecar=json_data.get("KubernetesServicesSidecar"),
            MetricsServer=json_data.get("MetricsServer"),
            NginxProxy=json_data.get("NginxProxy"),
            Nodelocal=json_data.get("Nodelocal"),
            PodInfraContainer=json_data.get("PodInfraContainer"),
            WeaveCni=json_data.get("WeaveCni"),
            WeaveNode=json_data.get("WeaveNode"),
            WindowsPodInfraContainer=json_data.get("WindowsPodInfraContainer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunningSystemImagesDefinition = RunningSystemImagesDefinition


@dataclass
class WorkerHostsDefinition(BaseModel):
    Address: Optional[str]
    NodeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerHostsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerHostsDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            NodeName=json_data.get("NodeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerHostsDefinition = WorkerHostsDefinition


@dataclass
class AuthenticationDefinition(BaseModel):
    Sans: Optional[Sequence[str]]
    Strategy: Optional[str]
    Webhook: Optional[Sequence["_WebhookDefinition"]]

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
            Webhook=deserialize_list(json_data.get("Webhook"), WebhookDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationDefinition = AuthenticationDefinition


@dataclass
class WebhookDefinition(BaseModel):
    CacheTimeout: Optional[str]
    ConfigFile: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebhookDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebhookDefinition"]:
        if not json_data:
            return None
        return cls(
            CacheTimeout=json_data.get("CacheTimeout"),
            ConfigFile=json_data.get("ConfigFile"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebhookDefinition = WebhookDefinition


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
    SshCert: Optional[str]
    SshCertPath: Optional[str]
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
            SshCert=json_data.get("SshCert"),
            SshCertPath=json_data.get("SshCertPath"),
            SshKey=json_data.get("SshKey"),
            SshKeyPath=json_data.get("SshKeyPath"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BastionHostDefinition = BastionHostDefinition


@dataclass
class CloudProviderDefinition(BaseModel):
    CustomCloudConfig: Optional[str]
    CustomCloudProvider: Optional[str]
    Name: Optional[str]
    AwsCloudConfig: Optional[Sequence["_AwsCloudConfigDefinition"]]
    AwsCloudProvider: Optional[Sequence["_AwsCloudProviderDefinition"]]
    AzureCloudConfig: Optional[Sequence["_AzureCloudConfigDefinition"]]
    AzureCloudProvider: Optional[Sequence["_AzureCloudProviderDefinition"]]
    OpenstackCloudConfig: Optional[Sequence["_OpenstackCloudConfigDefinition"]]
    OpenstackCloudProvider: Optional[Sequence["_OpenstackCloudProviderDefinition"]]
    VsphereCloudConfig: Optional[Sequence["_VsphereCloudConfigDefinition"]]
    VsphereCloudProvider: Optional[Sequence["_VsphereCloudProviderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CloudProviderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudProviderDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomCloudConfig=json_data.get("CustomCloudConfig"),
            CustomCloudProvider=json_data.get("CustomCloudProvider"),
            Name=json_data.get("Name"),
            AwsCloudConfig=deserialize_list(json_data.get("AwsCloudConfig"), AwsCloudConfigDefinition),
            AwsCloudProvider=deserialize_list(json_data.get("AwsCloudProvider"), AwsCloudProviderDefinition),
            AzureCloudConfig=deserialize_list(json_data.get("AzureCloudConfig"), AzureCloudConfigDefinition),
            AzureCloudProvider=deserialize_list(json_data.get("AzureCloudProvider"), AzureCloudProviderDefinition),
            OpenstackCloudConfig=deserialize_list(json_data.get("OpenstackCloudConfig"), OpenstackCloudConfigDefinition),
            OpenstackCloudProvider=deserialize_list(json_data.get("OpenstackCloudProvider"), OpenstackCloudProviderDefinition),
            VsphereCloudConfig=deserialize_list(json_data.get("VsphereCloudConfig"), VsphereCloudConfigDefinition),
            VsphereCloudProvider=deserialize_list(json_data.get("VsphereCloudProvider"), VsphereCloudProviderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudProviderDefinition = CloudProviderDefinition


@dataclass
class AwsCloudConfigDefinition(BaseModel):
    Global: Optional[Sequence["_GlobalDefinition"]]
    ServiceOverride: Optional[Sequence["_ServiceOverrideDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Global=deserialize_list(json_data.get("Global"), GlobalDefinition),
            ServiceOverride=deserialize_list(json_data.get("ServiceOverride"), ServiceOverrideDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudConfigDefinition = AwsCloudConfigDefinition


@dataclass
class GlobalDefinition(BaseModel):
    Datacenter: Optional[str]
    Datacenters: Optional[str]
    Datastore: Optional[str]
    InsecureFlag: Optional[bool]
    Password: Optional[str]
    Port: Optional[str]
    SoapRoundtripCount: Optional[float]
    User: Optional[str]
    VmName: Optional[str]
    VmUuid: Optional[str]
    WorkingDir: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalDefinition"]:
        if not json_data:
            return None
        return cls(
            Datacenter=json_data.get("Datacenter"),
            Datacenters=json_data.get("Datacenters"),
            Datastore=json_data.get("Datastore"),
            InsecureFlag=json_data.get("InsecureFlag"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SoapRoundtripCount=json_data.get("SoapRoundtripCount"),
            User=json_data.get("User"),
            VmName=json_data.get("VmName"),
            VmUuid=json_data.get("VmUuid"),
            WorkingDir=json_data.get("WorkingDir"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalDefinition = GlobalDefinition


@dataclass
class ServiceOverrideDefinition(BaseModel):
    Key: Optional[str]
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
            Key=json_data.get("Key"),
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
class AzureCloudConfigDefinition(BaseModel):
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
        cls: Type["_AzureCloudConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureCloudConfigDefinition"]:
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
_AzureCloudConfigDefinition = AzureCloudConfigDefinition


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
class OpenstackCloudConfigDefinition(BaseModel):
    BlockStorage: Optional[Sequence["_BlockStorageDefinition"]]
    Global: Optional[Sequence["_GlobalDefinition"]]
    LoadBalancer: Optional[Sequence["_LoadBalancerDefinition"]]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Route: Optional[Sequence["_RouteDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OpenstackCloudConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenstackCloudConfigDefinition"]:
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
_OpenstackCloudConfigDefinition = OpenstackCloudConfigDefinition


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
class VsphereCloudConfigDefinition(BaseModel):
    Disk: Optional[Sequence["_DiskDefinition"]]
    Global: Optional[Sequence["_GlobalDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
    VirtualCenter: Optional[Sequence["_VirtualCenterDefinition"]]
    Workspace: Optional[Sequence["_WorkspaceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VsphereCloudConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VsphereCloudConfigDefinition"]:
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
_VsphereCloudConfigDefinition = VsphereCloudConfigDefinition


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
class DnsDefinition(BaseModel):
    NodeSelector: Optional[Sequence["_NodeSelectorDefinition"]]
    Provider: Optional[str]
    ReverseCidrs: Optional[Sequence[str]]
    UpstreamNameservers: Optional[Sequence[str]]
    Nodelocal: Optional[Sequence["_NodelocalDefinition"]]

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
            Nodelocal=deserialize_list(json_data.get("Nodelocal"), NodelocalDefinition),
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
class IngressDefinition(BaseModel):
    DnsPolicy: Optional[str]
    ExtraArgs: Optional[Sequence["_ExtraArgsDefinition"]]
    NodeSelector: Optional[Sequence["_NodeSelectorDefinition2"]]
    Options: Optional[Sequence["_OptionsDefinition2"]]
    Provider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IngressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsPolicy=json_data.get("DnsPolicy"),
            ExtraArgs=deserialize_list(json_data.get("ExtraArgs"), ExtraArgsDefinition),
            NodeSelector=deserialize_list(json_data.get("NodeSelector"), NodeSelectorDefinition2),
            Options=deserialize_list(json_data.get("Options"), OptionsDefinition2),
            Provider=json_data.get("Provider"),
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
    Labels: Optional[Sequence["_LabelsDefinition"]]
    NodeName: Optional[str]
    Port: Optional[str]
    Role: Optional[Sequence[str]]
    Roles: Optional[str]
    SshAgentAuth: Optional[bool]
    SshCert: Optional[str]
    SshCertPath: Optional[str]
    SshKey: Optional[str]
    SshKeyPath: Optional[str]
    User: Optional[str]
    Taints: Optional[Sequence["_TaintsDefinition"]]

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
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            NodeName=json_data.get("NodeName"),
            Port=json_data.get("Port"),
            Role=json_data.get("Role"),
            Roles=json_data.get("Roles"),
            SshAgentAuth=json_data.get("SshAgentAuth"),
            SshCert=json_data.get("SshCert"),
            SshCertPath=json_data.get("SshCertPath"),
            SshKey=json_data.get("SshKey"),
            SshKeyPath=json_data.get("SshKeyPath"),
            User=json_data.get("User"),
            Taints=deserialize_list(json_data.get("Taints"), TaintsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodesDefinition = NodesDefinition


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
class TaintsDefinition(BaseModel):
    Effect: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaintsDefinition"]:
        if not json_data:
            return None
        return cls(
            Effect=json_data.get("Effect"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaintsDefinition = TaintsDefinition


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
class RestoreDefinition(BaseModel):
    Restore: Optional[bool]
    SnapshotName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RestoreDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestoreDefinition"]:
        if not json_data:
            return None
        return cls(
            Restore=json_data.get("Restore"),
            SnapshotName=json_data.get("SnapshotName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestoreDefinition = RestoreDefinition


@dataclass
class RotateCertificatesDefinition(BaseModel):
    CaCertificates: Optional[bool]
    Services: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RotateCertificatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RotateCertificatesDefinition"]:
        if not json_data:
            return None
        return cls(
            CaCertificates=json_data.get("CaCertificates"),
            Services=json_data.get("Services"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RotateCertificatesDefinition = RotateCertificatesDefinition


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
    ExtraArgs: Optional[Sequence["_ExtraArgsDefinition8"]]
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
            ExtraArgs=deserialize_list(json_data.get("ExtraArgs"), ExtraArgsDefinition8),
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
class ExtraArgsDefinition8(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraArgsDefinition8"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraArgsDefinition8"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraArgsDefinition8 = ExtraArgsDefinition8


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
    AlwaysPullImages: Optional[bool]
    ExtraArgs: Optional[Sequence["_ExtraArgsDefinition9"]]
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
            AlwaysPullImages=json_data.get("AlwaysPullImages"),
            ExtraArgs=deserialize_list(json_data.get("ExtraArgs"), ExtraArgsDefinition9),
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
class ExtraArgsDefinition9(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraArgsDefinition9"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraArgsDefinition9"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraArgsDefinition9 = ExtraArgsDefinition9


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
    ExtraArgs: Optional[Sequence["_ExtraArgsDefinition10"]]
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
            ExtraArgs=deserialize_list(json_data.get("ExtraArgs"), ExtraArgsDefinition10),
            ExtraBinds=json_data.get("ExtraBinds"),
            ExtraEnv=json_data.get("ExtraEnv"),
            Image=json_data.get("Image"),
            ServiceClusterIpRange=json_data.get("ServiceClusterIpRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeControllerDefinition = KubeControllerDefinition


@dataclass
class ExtraArgsDefinition10(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraArgsDefinition10"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraArgsDefinition10"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraArgsDefinition10 = ExtraArgsDefinition10


@dataclass
class KubeletDefinition(BaseModel):
    ClusterDnsServer: Optional[str]
    ClusterDomain: Optional[str]
    ExtraArgs: Optional[Sequence["_ExtraArgsDefinition11"]]
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
            ExtraArgs=deserialize_list(json_data.get("ExtraArgs"), ExtraArgsDefinition11),
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
class ExtraArgsDefinition11(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraArgsDefinition11"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraArgsDefinition11"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraArgsDefinition11 = ExtraArgsDefinition11


@dataclass
class KubeproxyDefinition(BaseModel):
    ExtraArgs: Optional[Sequence["_ExtraArgsDefinition12"]]
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
            ExtraArgs=deserialize_list(json_data.get("ExtraArgs"), ExtraArgsDefinition12),
            ExtraBinds=json_data.get("ExtraBinds"),
            ExtraEnv=json_data.get("ExtraEnv"),
            Image=json_data.get("Image"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeproxyDefinition = KubeproxyDefinition


@dataclass
class ExtraArgsDefinition12(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraArgsDefinition12"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraArgsDefinition12"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraArgsDefinition12 = ExtraArgsDefinition12


@dataclass
class SchedulerDefinition(BaseModel):
    ExtraArgs: Optional[Sequence["_ExtraArgsDefinition13"]]
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
            ExtraArgs=deserialize_list(json_data.get("ExtraArgs"), ExtraArgsDefinition13),
            ExtraBinds=json_data.get("ExtraBinds"),
            ExtraEnv=json_data.get("ExtraEnv"),
            Image=json_data.get("Image"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchedulerDefinition = SchedulerDefinition


@dataclass
class ExtraArgsDefinition13(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraArgsDefinition13"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraArgsDefinition13"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraArgsDefinition13 = ExtraArgsDefinition13


@dataclass
class ServicesEtcdDefinition(BaseModel):
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
        cls: Type["_ServicesEtcdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicesEtcdDefinition"]:
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
_ServicesEtcdDefinition = ServicesEtcdDefinition


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
class ServicesKubeApiDefinition(BaseModel):
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
        cls: Type["_ServicesKubeApiDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicesKubeApiDefinition"]:
        if not json_data:
            return None
        return cls(
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
_ServicesKubeApiDefinition = ServicesKubeApiDefinition


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
class ServicesKubeControllerDefinition(BaseModel):
    ClusterCidr: Optional[str]
    ExtraArgs: Optional[Sequence["_ExtraArgsDefinition4"]]
    ExtraBinds: Optional[Sequence[str]]
    ExtraEnv: Optional[Sequence[str]]
    Image: Optional[str]
    ServiceClusterIpRange: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServicesKubeControllerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicesKubeControllerDefinition"]:
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
_ServicesKubeControllerDefinition = ServicesKubeControllerDefinition


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
class ServicesKubeletDefinition(BaseModel):
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
        cls: Type["_ServicesKubeletDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicesKubeletDefinition"]:
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
_ServicesKubeletDefinition = ServicesKubeletDefinition


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
class ServicesKubeproxyDefinition(BaseModel):
    ExtraArgs: Optional[Sequence["_ExtraArgsDefinition6"]]
    ExtraBinds: Optional[Sequence[str]]
    ExtraEnv: Optional[Sequence[str]]
    Image: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServicesKubeproxyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicesKubeproxyDefinition"]:
        if not json_data:
            return None
        return cls(
            ExtraArgs=deserialize_list(json_data.get("ExtraArgs"), ExtraArgsDefinition6),
            ExtraBinds=json_data.get("ExtraBinds"),
            ExtraEnv=json_data.get("ExtraEnv"),
            Image=json_data.get("Image"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicesKubeproxyDefinition = ServicesKubeproxyDefinition


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
class ServicesSchedulerDefinition(BaseModel):
    ExtraArgs: Optional[Sequence["_ExtraArgsDefinition7"]]
    ExtraBinds: Optional[Sequence[str]]
    ExtraEnv: Optional[Sequence[str]]
    Image: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServicesSchedulerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicesSchedulerDefinition"]:
        if not json_data:
            return None
        return cls(
            ExtraArgs=deserialize_list(json_data.get("ExtraArgs"), ExtraArgsDefinition7),
            ExtraBinds=json_data.get("ExtraBinds"),
            ExtraEnv=json_data.get("ExtraEnv"),
            Image=json_data.get("Image"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicesSchedulerDefinition = ServicesSchedulerDefinition


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
class SystemImagesDefinition(BaseModel):
    AciCniDeployContainer: Optional[str]
    AciControllerContainer: Optional[str]
    AciHostContainer: Optional[str]
    AciMcastContainer: Optional[str]
    AciOpflexContainer: Optional[str]
    AciOvsContainer: Optional[str]
    Alpine: Optional[str]
    CalicoCni: Optional[str]
    CalicoControllers: Optional[str]
    CalicoCtl: Optional[str]
    CalicoFlexVol: Optional[str]
    CalicoNode: Optional[str]
    CanalCni: Optional[str]
    CanalFlannel: Optional[str]
    CanalFlexVol: Optional[str]
    CanalNode: Optional[str]
    CertDownloader: Optional[str]
    Coredns: Optional[str]
    CorednsAutoscaler: Optional[str]
    Dnsmasq: Optional[str]
    Etcd: Optional[str]
    Flannel: Optional[str]
    FlannelCni: Optional[str]
    Ingress: Optional[str]
    IngressBackend: Optional[str]
    KubeDns: Optional[str]
    KubeDnsAutoscaler: Optional[str]
    KubeDnsSidecar: Optional[str]
    Kubernetes: Optional[str]
    KubernetesServicesSidecar: Optional[str]
    MetricsServer: Optional[str]
    NginxProxy: Optional[str]
    Nodelocal: Optional[str]
    PodInfraContainer: Optional[str]
    WeaveCni: Optional[str]
    WeaveNode: Optional[str]
    WindowsPodInfraContainer: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemImagesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemImagesDefinition"]:
        if not json_data:
            return None
        return cls(
            AciCniDeployContainer=json_data.get("AciCniDeployContainer"),
            AciControllerContainer=json_data.get("AciControllerContainer"),
            AciHostContainer=json_data.get("AciHostContainer"),
            AciMcastContainer=json_data.get("AciMcastContainer"),
            AciOpflexContainer=json_data.get("AciOpflexContainer"),
            AciOvsContainer=json_data.get("AciOvsContainer"),
            Alpine=json_data.get("Alpine"),
            CalicoCni=json_data.get("CalicoCni"),
            CalicoControllers=json_data.get("CalicoControllers"),
            CalicoCtl=json_data.get("CalicoCtl"),
            CalicoFlexVol=json_data.get("CalicoFlexVol"),
            CalicoNode=json_data.get("CalicoNode"),
            CanalCni=json_data.get("CanalCni"),
            CanalFlannel=json_data.get("CanalFlannel"),
            CanalFlexVol=json_data.get("CanalFlexVol"),
            CanalNode=json_data.get("CanalNode"),
            CertDownloader=json_data.get("CertDownloader"),
            Coredns=json_data.get("Coredns"),
            CorednsAutoscaler=json_data.get("CorednsAutoscaler"),
            Dnsmasq=json_data.get("Dnsmasq"),
            Etcd=json_data.get("Etcd"),
            Flannel=json_data.get("Flannel"),
            FlannelCni=json_data.get("FlannelCni"),
            Ingress=json_data.get("Ingress"),
            IngressBackend=json_data.get("IngressBackend"),
            KubeDns=json_data.get("KubeDns"),
            KubeDnsAutoscaler=json_data.get("KubeDnsAutoscaler"),
            KubeDnsSidecar=json_data.get("KubeDnsSidecar"),
            Kubernetes=json_data.get("Kubernetes"),
            KubernetesServicesSidecar=json_data.get("KubernetesServicesSidecar"),
            MetricsServer=json_data.get("MetricsServer"),
            NginxProxy=json_data.get("NginxProxy"),
            Nodelocal=json_data.get("Nodelocal"),
            PodInfraContainer=json_data.get("PodInfraContainer"),
            WeaveCni=json_data.get("WeaveCni"),
            WeaveNode=json_data.get("WeaveNode"),
            WindowsPodInfraContainer=json_data.get("WindowsPodInfraContainer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemImagesDefinition = SystemImagesDefinition


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


