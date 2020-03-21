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
    Cname: Optional[str]
    EnforceBackendPoolsCertificateNameCheck: Optional[bool]
    FriendlyName: Optional[str]
    LoadBalancerEnabled: Optional[bool]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    BackendPool: Optional[Sequence["_BackendPool"]]
    BackendPoolHealthProbe: Optional[Sequence["_BackendPoolHealthProbe"]]
    BackendPoolLoadBalancing: Optional[Sequence["_BackendPoolLoadBalancing"]]
    FrontendEndpoint: Optional[Sequence["_FrontendEndpoint"]]
    RoutingRule: Optional[Sequence["_RoutingRule"]]
    Timeouts: Optional["_Timeouts"]
    Backend: Optional[Sequence["_Backend"]]
    CustomHttpsConfiguration: Optional[Sequence["_CustomHttpsConfiguration"]]
    ForwardingConfiguration: Optional[Sequence["_ForwardingConfiguration"]]
    RedirectConfiguration: Optional[Sequence["_RedirectConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Cname=json_data.get("Cname"),
            EnforceBackendPoolsCertificateNameCheck=json_data.get("EnforceBackendPoolsCertificateNameCheck"),
            FriendlyName=json_data.get("FriendlyName"),
            LoadBalancerEnabled=json_data.get("LoadBalancerEnabled"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=json_data.get("Tags"),
            BackendPool=json_data.get("BackendPool"),
            BackendPoolHealthProbe=json_data.get("BackendPoolHealthProbe"),
            BackendPoolLoadBalancing=json_data.get("BackendPoolLoadBalancing"),
            FrontendEndpoint=json_data.get("FrontendEndpoint"),
            RoutingRule=json_data.get("RoutingRule"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Backend=json_data.get("Backend"),
            CustomHttpsConfiguration=json_data.get("CustomHttpsConfiguration"),
            ForwardingConfiguration=json_data.get("ForwardingConfiguration"),
            RedirectConfiguration=json_data.get("RedirectConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class BackendPool:
    HealthProbeName: Optional[str]
    LoadBalancingName: Optional[str]
    Name: Optional[str]
    Backend: Optional[Sequence["_Backend"]]

    @classmethod
    def _deserialize(
        cls: Type["_BackendPool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendPool"]:
        if not json_data:
            return None
        return cls(
            HealthProbeName=json_data.get("HealthProbeName"),
            LoadBalancingName=json_data.get("LoadBalancingName"),
            Name=json_data.get("Name"),
            Backend=json_data.get("Backend"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendPool = BackendPool


@dataclass
class Backend:
    Address: Optional[str]
    Enabled: Optional[bool]
    HostHeader: Optional[str]
    HttpPort: Optional[float]
    HttpsPort: Optional[float]
    Priority: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Backend"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Backend"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Enabled=json_data.get("Enabled"),
            HostHeader=json_data.get("HostHeader"),
            HttpPort=json_data.get("HttpPort"),
            HttpsPort=json_data.get("HttpsPort"),
            Priority=json_data.get("Priority"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Backend = Backend


@dataclass
class BackendPoolHealthProbe:
    Enabled: Optional[bool]
    IntervalInSeconds: Optional[float]
    Name: Optional[str]
    Path: Optional[str]
    ProbeMethod: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackendPoolHealthProbe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendPoolHealthProbe"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            IntervalInSeconds=json_data.get("IntervalInSeconds"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            ProbeMethod=json_data.get("ProbeMethod"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendPoolHealthProbe = BackendPoolHealthProbe


@dataclass
class BackendPoolLoadBalancing:
    AdditionalLatencyMilliseconds: Optional[float]
    Name: Optional[str]
    SampleSize: Optional[float]
    SuccessfulSamplesRequired: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BackendPoolLoadBalancing"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendPoolLoadBalancing"]:
        if not json_data:
            return None
        return cls(
            AdditionalLatencyMilliseconds=json_data.get("AdditionalLatencyMilliseconds"),
            Name=json_data.get("Name"),
            SampleSize=json_data.get("SampleSize"),
            SuccessfulSamplesRequired=json_data.get("SuccessfulSamplesRequired"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendPoolLoadBalancing = BackendPoolLoadBalancing


@dataclass
class FrontendEndpoint:
    CustomHttpsProvisioningEnabled: Optional[bool]
    HostName: Optional[str]
    Name: Optional[str]
    SessionAffinityEnabled: Optional[bool]
    SessionAffinityTtlSeconds: Optional[float]
    WebApplicationFirewallPolicyLinkId: Optional[str]
    CustomHttpsConfiguration: Optional[Sequence["_CustomHttpsConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_FrontendEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrontendEndpoint"]:
        if not json_data:
            return None
        return cls(
            CustomHttpsProvisioningEnabled=json_data.get("CustomHttpsProvisioningEnabled"),
            HostName=json_data.get("HostName"),
            Name=json_data.get("Name"),
            SessionAffinityEnabled=json_data.get("SessionAffinityEnabled"),
            SessionAffinityTtlSeconds=json_data.get("SessionAffinityTtlSeconds"),
            WebApplicationFirewallPolicyLinkId=json_data.get("WebApplicationFirewallPolicyLinkId"),
            CustomHttpsConfiguration=json_data.get("CustomHttpsConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrontendEndpoint = FrontendEndpoint


@dataclass
class CustomHttpsConfiguration:
    AzureKeyVaultCertificateSecretName: Optional[str]
    AzureKeyVaultCertificateSecretVersion: Optional[str]
    AzureKeyVaultCertificateVaultId: Optional[str]
    CertificateSource: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomHttpsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomHttpsConfiguration"]:
        if not json_data:
            return None
        return cls(
            AzureKeyVaultCertificateSecretName=json_data.get("AzureKeyVaultCertificateSecretName"),
            AzureKeyVaultCertificateSecretVersion=json_data.get("AzureKeyVaultCertificateSecretVersion"),
            AzureKeyVaultCertificateVaultId=json_data.get("AzureKeyVaultCertificateVaultId"),
            CertificateSource=json_data.get("CertificateSource"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomHttpsConfiguration = CustomHttpsConfiguration


@dataclass
class RoutingRule:
    AcceptedProtocols: Optional[Sequence[str]]
    Enabled: Optional[bool]
    FrontendEndpoints: Optional[Sequence[str]]
    Name: Optional[str]
    PatternsToMatch: Optional[Sequence[str]]
    ForwardingConfiguration: Optional[Sequence["_ForwardingConfiguration"]]
    RedirectConfiguration: Optional[Sequence["_RedirectConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingRule"]:
        if not json_data:
            return None
        return cls(
            AcceptedProtocols=json_data.get("AcceptedProtocols"),
            Enabled=json_data.get("Enabled"),
            FrontendEndpoints=json_data.get("FrontendEndpoints"),
            Name=json_data.get("Name"),
            PatternsToMatch=json_data.get("PatternsToMatch"),
            ForwardingConfiguration=json_data.get("ForwardingConfiguration"),
            RedirectConfiguration=json_data.get("RedirectConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingRule = RoutingRule


@dataclass
class ForwardingConfiguration:
    BackendPoolName: Optional[str]
    CacheEnabled: Optional[bool]
    CacheQueryParameterStripDirective: Optional[str]
    CacheUseDynamicCompression: Optional[bool]
    CustomForwardingPath: Optional[str]
    ForwardingProtocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardingConfiguration"]:
        if not json_data:
            return None
        return cls(
            BackendPoolName=json_data.get("BackendPoolName"),
            CacheEnabled=json_data.get("CacheEnabled"),
            CacheQueryParameterStripDirective=json_data.get("CacheQueryParameterStripDirective"),
            CacheUseDynamicCompression=json_data.get("CacheUseDynamicCompression"),
            CustomForwardingPath=json_data.get("CustomForwardingPath"),
            ForwardingProtocol=json_data.get("ForwardingProtocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardingConfiguration = ForwardingConfiguration


@dataclass
class RedirectConfiguration:
    CustomFragment: Optional[str]
    CustomHost: Optional[str]
    CustomPath: Optional[str]
    CustomQueryString: Optional[str]
    RedirectProtocol: Optional[str]
    RedirectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectConfiguration"]:
        if not json_data:
            return None
        return cls(
            CustomFragment=json_data.get("CustomFragment"),
            CustomHost=json_data.get("CustomHost"),
            CustomPath=json_data.get("CustomPath"),
            CustomQueryString=json_data.get("CustomQueryString"),
            RedirectProtocol=json_data.get("RedirectProtocol"),
            RedirectType=json_data.get("RedirectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedirectConfiguration = RedirectConfiguration


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


