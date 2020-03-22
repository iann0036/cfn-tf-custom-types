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
    EnableHttp2: Optional[bool]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Zones: Optional[Sequence[str]]
    AuthenticationCertificate: Optional[Sequence["_AuthenticationCertificate"]]
    AutoscaleConfiguration: Optional[Sequence["_AutoscaleConfiguration"]]
    BackendAddressPool: Optional[Sequence["_BackendAddressPool"]]
    BackendHttpSettings: Optional[Sequence["_BackendHttpSettings"]]
    CustomErrorConfiguration: Optional[Sequence["_CustomErrorConfiguration"]]
    FrontendIpConfiguration: Optional[Sequence["_FrontendIpConfiguration"]]
    FrontendPort: Optional[Sequence["_FrontendPort"]]
    GatewayIpConfiguration: Optional[Sequence["_GatewayIpConfiguration"]]
    HttpListener: Optional[Sequence["_HttpListener"]]
    Identity: Optional[Sequence["_Identity"]]
    Probe: Optional[Sequence["_Probe"]]
    RedirectConfiguration: Optional[Sequence["_RedirectConfiguration"]]
    RequestRoutingRule: Optional[Sequence["_RequestRoutingRule"]]
    RewriteRuleSet: Optional[Sequence["_RewriteRuleSet"]]
    Sku: Optional[Sequence["_Sku"]]
    SslCertificate: Optional[Sequence["_SslCertificate"]]
    SslPolicy: Optional[Sequence["_SslPolicy"]]
    Timeouts: Optional["_Timeouts"]
    TrustedRootCertificate: Optional[Sequence["_TrustedRootCertificate"]]
    UrlPathMap: Optional[Sequence["_UrlPathMap"]]
    WafConfiguration: Optional[Sequence["_WafConfiguration"]]
    ConnectionDraining: Optional[Sequence["_ConnectionDraining"]]
    Match: Optional[Sequence["_Match"]]
    RewriteRule: Optional[Sequence["_RewriteRule"]]
    PathRule: Optional[Sequence["_PathRule"]]
    DisabledRuleGroup: Optional[Sequence["_DisabledRuleGroup"]]
    Exclusion: Optional[Sequence["_Exclusion"]]
    Condition: Optional[Sequence["_Condition"]]
    RequestHeaderConfiguration: Optional[Sequence["_RequestHeaderConfiguration"]]
    ResponseHeaderConfiguration: Optional[Sequence["_ResponseHeaderConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EnableHttp2=json_data.get("EnableHttp2"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=json_data.get("Tags"),
            Zones=json_data.get("Zones"),
            AuthenticationCertificate=json_data.get("AuthenticationCertificate"),
            AutoscaleConfiguration=json_data.get("AutoscaleConfiguration"),
            BackendAddressPool=json_data.get("BackendAddressPool"),
            BackendHttpSettings=json_data.get("BackendHttpSettings"),
            CustomErrorConfiguration=json_data.get("CustomErrorConfiguration"),
            FrontendIpConfiguration=json_data.get("FrontendIpConfiguration"),
            FrontendPort=json_data.get("FrontendPort"),
            GatewayIpConfiguration=json_data.get("GatewayIpConfiguration"),
            HttpListener=json_data.get("HttpListener"),
            Identity=json_data.get("Identity"),
            Probe=json_data.get("Probe"),
            RedirectConfiguration=json_data.get("RedirectConfiguration"),
            RequestRoutingRule=json_data.get("RequestRoutingRule"),
            RewriteRuleSet=json_data.get("RewriteRuleSet"),
            Sku=json_data.get("Sku"),
            SslCertificate=json_data.get("SslCertificate"),
            SslPolicy=json_data.get("SslPolicy"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            TrustedRootCertificate=json_data.get("TrustedRootCertificate"),
            UrlPathMap=json_data.get("UrlPathMap"),
            WafConfiguration=json_data.get("WafConfiguration"),
            ConnectionDraining=json_data.get("ConnectionDraining"),
            Match=json_data.get("Match"),
            RewriteRule=json_data.get("RewriteRule"),
            PathRule=json_data.get("PathRule"),
            DisabledRuleGroup=json_data.get("DisabledRuleGroup"),
            Exclusion=json_data.get("Exclusion"),
            Condition=json_data.get("Condition"),
            RequestHeaderConfiguration=json_data.get("RequestHeaderConfiguration"),
            ResponseHeaderConfiguration=json_data.get("ResponseHeaderConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class AuthenticationCertificate:
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationCertificate"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationCertificate = AuthenticationCertificate


@dataclass
class AutoscaleConfiguration:
    MaxCapacity: Optional[float]
    MinCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleConfiguration"]:
        if not json_data:
            return None
        return cls(
            MaxCapacity=json_data.get("MaxCapacity"),
            MinCapacity=json_data.get("MinCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleConfiguration = AutoscaleConfiguration


@dataclass
class BackendAddressPool:
    Fqdns: Optional[Sequence[str]]
    IpAddresses: Optional[Sequence[str]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackendAddressPool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendAddressPool"]:
        if not json_data:
            return None
        return cls(
            Fqdns=json_data.get("Fqdns"),
            IpAddresses=json_data.get("IpAddresses"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendAddressPool = BackendAddressPool


@dataclass
class BackendHttpSettings:
    AffinityCookieName: Optional[str]
    CookieBasedAffinity: Optional[str]
    HostName: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    PickHostNameFromBackendAddress: Optional[bool]
    Port: Optional[float]
    ProbeName: Optional[str]
    Protocol: Optional[str]
    RequestTimeout: Optional[float]
    TrustedRootCertificateNames: Optional[Sequence[str]]
    AuthenticationCertificate: Optional[Sequence["_AuthenticationCertificate"]]
    ConnectionDraining: Optional[Sequence["_ConnectionDraining"]]

    @classmethod
    def _deserialize(
        cls: Type["_BackendHttpSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendHttpSettings"]:
        if not json_data:
            return None
        return cls(
            AffinityCookieName=json_data.get("AffinityCookieName"),
            CookieBasedAffinity=json_data.get("CookieBasedAffinity"),
            HostName=json_data.get("HostName"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            PickHostNameFromBackendAddress=json_data.get("PickHostNameFromBackendAddress"),
            Port=json_data.get("Port"),
            ProbeName=json_data.get("ProbeName"),
            Protocol=json_data.get("Protocol"),
            RequestTimeout=json_data.get("RequestTimeout"),
            TrustedRootCertificateNames=json_data.get("TrustedRootCertificateNames"),
            AuthenticationCertificate=json_data.get("AuthenticationCertificate"),
            ConnectionDraining=json_data.get("ConnectionDraining"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendHttpSettings = BackendHttpSettings


@dataclass
class ConnectionDraining:
    DrainTimeoutSec: Optional[float]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionDraining"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionDraining"]:
        if not json_data:
            return None
        return cls(
            DrainTimeoutSec=json_data.get("DrainTimeoutSec"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionDraining = ConnectionDraining


@dataclass
class CustomErrorConfiguration:
    CustomErrorPageUrl: Optional[str]
    StatusCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomErrorConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomErrorConfiguration"]:
        if not json_data:
            return None
        return cls(
            CustomErrorPageUrl=json_data.get("CustomErrorPageUrl"),
            StatusCode=json_data.get("StatusCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomErrorConfiguration = CustomErrorConfiguration


@dataclass
class FrontendIpConfiguration:
    Name: Optional[str]
    PrivateIpAddress: Optional[str]
    PrivateIpAddressAllocation: Optional[str]
    PublicIpAddressId: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FrontendIpConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrontendIpConfiguration"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            PrivateIpAddressAllocation=json_data.get("PrivateIpAddressAllocation"),
            PublicIpAddressId=json_data.get("PublicIpAddressId"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrontendIpConfiguration = FrontendIpConfiguration


@dataclass
class FrontendPort:
    Name: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FrontendPort"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrontendPort"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrontendPort = FrontendPort


@dataclass
class GatewayIpConfiguration:
    Name: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayIpConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayIpConfiguration"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayIpConfiguration = GatewayIpConfiguration


@dataclass
class HttpListener:
    FrontendIpConfigurationName: Optional[str]
    FrontendPortName: Optional[str]
    HostName: Optional[str]
    Name: Optional[str]
    Protocol: Optional[str]
    RequireSni: Optional[bool]
    SslCertificateName: Optional[str]
    CustomErrorConfiguration: Optional[Sequence["_CustomErrorConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpListener"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpListener"]:
        if not json_data:
            return None
        return cls(
            FrontendIpConfigurationName=json_data.get("FrontendIpConfigurationName"),
            FrontendPortName=json_data.get("FrontendPortName"),
            HostName=json_data.get("HostName"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            RequireSni=json_data.get("RequireSni"),
            SslCertificateName=json_data.get("SslCertificateName"),
            CustomErrorConfiguration=json_data.get("CustomErrorConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpListener = HttpListener


@dataclass
class Identity:
    IdentityIds: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Identity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Identity"]:
        if not json_data:
            return None
        return cls(
            IdentityIds=json_data.get("IdentityIds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Identity = Identity


@dataclass
class Probe:
    Host: Optional[str]
    Interval: Optional[float]
    MinimumServers: Optional[float]
    Name: Optional[str]
    Path: Optional[str]
    PickHostNameFromBackendHttpSettings: Optional[bool]
    Protocol: Optional[str]
    Timeout: Optional[float]
    UnhealthyThreshold: Optional[float]
    Match: Optional[Sequence["_Match"]]

    @classmethod
    def _deserialize(
        cls: Type["_Probe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Probe"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Interval=json_data.get("Interval"),
            MinimumServers=json_data.get("MinimumServers"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            PickHostNameFromBackendHttpSettings=json_data.get("PickHostNameFromBackendHttpSettings"),
            Protocol=json_data.get("Protocol"),
            Timeout=json_data.get("Timeout"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
            Match=json_data.get("Match"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Probe = Probe


@dataclass
class Match:
    Body: Optional[str]
    StatusCode: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Match"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Match"]:
        if not json_data:
            return None
        return cls(
            Body=json_data.get("Body"),
            StatusCode=json_data.get("StatusCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Match = Match


@dataclass
class RedirectConfiguration:
    IncludePath: Optional[bool]
    IncludeQueryString: Optional[bool]
    Name: Optional[str]
    RedirectType: Optional[str]
    TargetListenerName: Optional[str]
    TargetUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectConfiguration"]:
        if not json_data:
            return None
        return cls(
            IncludePath=json_data.get("IncludePath"),
            IncludeQueryString=json_data.get("IncludeQueryString"),
            Name=json_data.get("Name"),
            RedirectType=json_data.get("RedirectType"),
            TargetListenerName=json_data.get("TargetListenerName"),
            TargetUrl=json_data.get("TargetUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedirectConfiguration = RedirectConfiguration


@dataclass
class RequestRoutingRule:
    BackendAddressPoolName: Optional[str]
    BackendHttpSettingsName: Optional[str]
    HttpListenerName: Optional[str]
    Name: Optional[str]
    RedirectConfigurationName: Optional[str]
    RewriteRuleSetName: Optional[str]
    RuleType: Optional[str]
    UrlPathMapName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestRoutingRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestRoutingRule"]:
        if not json_data:
            return None
        return cls(
            BackendAddressPoolName=json_data.get("BackendAddressPoolName"),
            BackendHttpSettingsName=json_data.get("BackendHttpSettingsName"),
            HttpListenerName=json_data.get("HttpListenerName"),
            Name=json_data.get("Name"),
            RedirectConfigurationName=json_data.get("RedirectConfigurationName"),
            RewriteRuleSetName=json_data.get("RewriteRuleSetName"),
            RuleType=json_data.get("RuleType"),
            UrlPathMapName=json_data.get("UrlPathMapName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestRoutingRule = RequestRoutingRule


@dataclass
class RewriteRuleSet:
    Name: Optional[str]
    RewriteRule: Optional[Sequence["_RewriteRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_RewriteRuleSet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RewriteRuleSet"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            RewriteRule=json_data.get("RewriteRule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RewriteRuleSet = RewriteRuleSet


@dataclass
class RewriteRule:
    Name: Optional[str]
    RuleSequence: Optional[float]
    Condition: Optional[Sequence["_Condition"]]
    RequestHeaderConfiguration: Optional[Sequence["_RequestHeaderConfiguration"]]
    ResponseHeaderConfiguration: Optional[Sequence["_ResponseHeaderConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_RewriteRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RewriteRule"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            RuleSequence=json_data.get("RuleSequence"),
            Condition=json_data.get("Condition"),
            RequestHeaderConfiguration=json_data.get("RequestHeaderConfiguration"),
            ResponseHeaderConfiguration=json_data.get("ResponseHeaderConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RewriteRule = RewriteRule


@dataclass
class Condition:
    IgnoreCase: Optional[bool]
    Negate: Optional[bool]
    Pattern: Optional[str]
    Variable: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Condition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Condition"]:
        if not json_data:
            return None
        return cls(
            IgnoreCase=json_data.get("IgnoreCase"),
            Negate=json_data.get("Negate"),
            Pattern=json_data.get("Pattern"),
            Variable=json_data.get("Variable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Condition = Condition


@dataclass
class RequestHeaderConfiguration:
    HeaderName: Optional[str]
    HeaderValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestHeaderConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestHeaderConfiguration"]:
        if not json_data:
            return None
        return cls(
            HeaderName=json_data.get("HeaderName"),
            HeaderValue=json_data.get("HeaderValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestHeaderConfiguration = RequestHeaderConfiguration


@dataclass
class ResponseHeaderConfiguration:
    HeaderName: Optional[str]
    HeaderValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseHeaderConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseHeaderConfiguration"]:
        if not json_data:
            return None
        return cls(
            HeaderName=json_data.get("HeaderName"),
            HeaderValue=json_data.get("HeaderValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseHeaderConfiguration = ResponseHeaderConfiguration


@dataclass
class Sku:
    Capacity: Optional[float]
    Name: Optional[str]
    Tier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Sku"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sku"]:
        if not json_data:
            return None
        return cls(
            Capacity=json_data.get("Capacity"),
            Name=json_data.get("Name"),
            Tier=json_data.get("Tier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sku = Sku


@dataclass
class SslCertificate:
    Data: Optional[str]
    KeyVaultSecretId: Optional[str]
    Name: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslCertificate"]:
        if not json_data:
            return None
        return cls(
            Data=json_data.get("Data"),
            KeyVaultSecretId=json_data.get("KeyVaultSecretId"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslCertificate = SslCertificate


@dataclass
class SslPolicy:
    CipherSuites: Optional[Sequence[str]]
    DisabledProtocols: Optional[Sequence[str]]
    MinProtocolVersion: Optional[str]
    PolicyName: Optional[str]
    PolicyType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslPolicy"]:
        if not json_data:
            return None
        return cls(
            CipherSuites=json_data.get("CipherSuites"),
            DisabledProtocols=json_data.get("DisabledProtocols"),
            MinProtocolVersion=json_data.get("MinProtocolVersion"),
            PolicyName=json_data.get("PolicyName"),
            PolicyType=json_data.get("PolicyType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslPolicy = SslPolicy


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
class TrustedRootCertificate:
    Data: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrustedRootCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrustedRootCertificate"]:
        if not json_data:
            return None
        return cls(
            Data=json_data.get("Data"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrustedRootCertificate = TrustedRootCertificate


@dataclass
class UrlPathMap:
    DefaultBackendAddressPoolName: Optional[str]
    DefaultBackendHttpSettingsName: Optional[str]
    DefaultRedirectConfigurationName: Optional[str]
    DefaultRewriteRuleSetName: Optional[str]
    Name: Optional[str]
    PathRule: Optional[Sequence["_PathRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_UrlPathMap"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlPathMap"]:
        if not json_data:
            return None
        return cls(
            DefaultBackendAddressPoolName=json_data.get("DefaultBackendAddressPoolName"),
            DefaultBackendHttpSettingsName=json_data.get("DefaultBackendHttpSettingsName"),
            DefaultRedirectConfigurationName=json_data.get("DefaultRedirectConfigurationName"),
            DefaultRewriteRuleSetName=json_data.get("DefaultRewriteRuleSetName"),
            Name=json_data.get("Name"),
            PathRule=json_data.get("PathRule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlPathMap = UrlPathMap


@dataclass
class PathRule:
    BackendAddressPoolName: Optional[str]
    BackendHttpSettingsName: Optional[str]
    Name: Optional[str]
    Paths: Optional[Sequence[str]]
    RedirectConfigurationName: Optional[str]
    RewriteRuleSetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PathRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathRule"]:
        if not json_data:
            return None
        return cls(
            BackendAddressPoolName=json_data.get("BackendAddressPoolName"),
            BackendHttpSettingsName=json_data.get("BackendHttpSettingsName"),
            Name=json_data.get("Name"),
            Paths=json_data.get("Paths"),
            RedirectConfigurationName=json_data.get("RedirectConfigurationName"),
            RewriteRuleSetName=json_data.get("RewriteRuleSetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathRule = PathRule


@dataclass
class WafConfiguration:
    Enabled: Optional[bool]
    FileUploadLimitMb: Optional[float]
    FirewallMode: Optional[str]
    MaxRequestBodySizeKb: Optional[float]
    RequestBodyCheck: Optional[bool]
    RuleSetType: Optional[str]
    RuleSetVersion: Optional[str]
    DisabledRuleGroup: Optional[Sequence["_DisabledRuleGroup"]]
    Exclusion: Optional[Sequence["_Exclusion"]]

    @classmethod
    def _deserialize(
        cls: Type["_WafConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WafConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            FileUploadLimitMb=json_data.get("FileUploadLimitMb"),
            FirewallMode=json_data.get("FirewallMode"),
            MaxRequestBodySizeKb=json_data.get("MaxRequestBodySizeKb"),
            RequestBodyCheck=json_data.get("RequestBodyCheck"),
            RuleSetType=json_data.get("RuleSetType"),
            RuleSetVersion=json_data.get("RuleSetVersion"),
            DisabledRuleGroup=json_data.get("DisabledRuleGroup"),
            Exclusion=json_data.get("Exclusion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WafConfiguration = WafConfiguration


@dataclass
class DisabledRuleGroup:
    RuleGroupName: Optional[str]
    Rules: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_DisabledRuleGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DisabledRuleGroup"]:
        if not json_data:
            return None
        return cls(
            RuleGroupName=json_data.get("RuleGroupName"),
            Rules=json_data.get("Rules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DisabledRuleGroup = DisabledRuleGroup


@dataclass
class Exclusion:
    MatchVariable: Optional[str]
    Selector: Optional[str]
    SelectorMatchOperator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Exclusion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Exclusion"]:
        if not json_data:
            return None
        return cls(
            MatchVariable=json_data.get("MatchVariable"),
            Selector=json_data.get("Selector"),
            SelectorMatchOperator=json_data.get("SelectorMatchOperator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Exclusion = Exclusion


