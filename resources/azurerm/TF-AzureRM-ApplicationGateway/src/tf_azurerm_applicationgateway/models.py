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
    EnableHttp2: Optional[bool]
    FirewallPolicyId: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Zones: Optional[Sequence[str]]
    AuthenticationCertificate: Optional[Sequence["_AuthenticationCertificateDefinition"]]
    AutoscaleConfiguration: Optional[Sequence["_AutoscaleConfigurationDefinition"]]
    BackendAddressPool: Optional[Sequence["_BackendAddressPoolDefinition"]]
    BackendHttpSettings: Optional[Sequence["_BackendHttpSettingsDefinition"]]
    CustomErrorConfiguration: Optional[Sequence["_CustomErrorConfigurationDefinition"]]
    FrontendIpConfiguration: Optional[Sequence["_FrontendIpConfigurationDefinition"]]
    FrontendPort: Optional[Sequence["_FrontendPortDefinition"]]
    GatewayIpConfiguration: Optional[Sequence["_GatewayIpConfigurationDefinition"]]
    HttpListener: Optional[Sequence["_HttpListenerDefinition"]]
    Identity: Optional[Sequence["_IdentityDefinition"]]
    Probe: Optional[Sequence["_ProbeDefinition"]]
    RedirectConfiguration: Optional[Sequence["_RedirectConfigurationDefinition"]]
    RequestRoutingRule: Optional[Sequence["_RequestRoutingRuleDefinition"]]
    RewriteRuleSet: Optional[Sequence["_RewriteRuleSetDefinition"]]
    Sku: Optional[Sequence["_SkuDefinition"]]
    SslCertificate: Optional[Sequence["_SslCertificateDefinition"]]
    SslPolicy: Optional[Sequence["_SslPolicyDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    TrustedRootCertificate: Optional[Sequence["_TrustedRootCertificateDefinition"]]
    UrlPathMap: Optional[Sequence["_UrlPathMapDefinition"]]
    WafConfiguration: Optional[Sequence["_WafConfigurationDefinition"]]

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
            EnableHttp2=json_data.get("EnableHttp2"),
            FirewallPolicyId=json_data.get("FirewallPolicyId"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Zones=json_data.get("Zones"),
            AuthenticationCertificate=deserialize_list(json_data.get("AuthenticationCertificate"), AuthenticationCertificateDefinition),
            AutoscaleConfiguration=deserialize_list(json_data.get("AutoscaleConfiguration"), AutoscaleConfigurationDefinition),
            BackendAddressPool=deserialize_list(json_data.get("BackendAddressPool"), BackendAddressPoolDefinition),
            BackendHttpSettings=deserialize_list(json_data.get("BackendHttpSettings"), BackendHttpSettingsDefinition),
            CustomErrorConfiguration=deserialize_list(json_data.get("CustomErrorConfiguration"), CustomErrorConfigurationDefinition),
            FrontendIpConfiguration=deserialize_list(json_data.get("FrontendIpConfiguration"), FrontendIpConfigurationDefinition),
            FrontendPort=deserialize_list(json_data.get("FrontendPort"), FrontendPortDefinition),
            GatewayIpConfiguration=deserialize_list(json_data.get("GatewayIpConfiguration"), GatewayIpConfigurationDefinition),
            HttpListener=deserialize_list(json_data.get("HttpListener"), HttpListenerDefinition),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            Probe=deserialize_list(json_data.get("Probe"), ProbeDefinition),
            RedirectConfiguration=deserialize_list(json_data.get("RedirectConfiguration"), RedirectConfigurationDefinition),
            RequestRoutingRule=deserialize_list(json_data.get("RequestRoutingRule"), RequestRoutingRuleDefinition),
            RewriteRuleSet=deserialize_list(json_data.get("RewriteRuleSet"), RewriteRuleSetDefinition),
            Sku=deserialize_list(json_data.get("Sku"), SkuDefinition),
            SslCertificate=deserialize_list(json_data.get("SslCertificate"), SslCertificateDefinition),
            SslPolicy=deserialize_list(json_data.get("SslPolicy"), SslPolicyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            TrustedRootCertificate=deserialize_list(json_data.get("TrustedRootCertificate"), TrustedRootCertificateDefinition),
            UrlPathMap=deserialize_list(json_data.get("UrlPathMap"), UrlPathMapDefinition),
            WafConfiguration=deserialize_list(json_data.get("WafConfiguration"), WafConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class AuthenticationCertificateDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationCertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationCertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationCertificateDefinition = AuthenticationCertificateDefinition


@dataclass
class AutoscaleConfigurationDefinition(BaseModel):
    MaxCapacity: Optional[float]
    MinCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxCapacity=json_data.get("MaxCapacity"),
            MinCapacity=json_data.get("MinCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleConfigurationDefinition = AutoscaleConfigurationDefinition


@dataclass
class BackendAddressPoolDefinition(BaseModel):
    Fqdns: Optional[Sequence[str]]
    IpAddresses: Optional[Sequence[str]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackendAddressPoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendAddressPoolDefinition"]:
        if not json_data:
            return None
        return cls(
            Fqdns=json_data.get("Fqdns"),
            IpAddresses=json_data.get("IpAddresses"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendAddressPoolDefinition = BackendAddressPoolDefinition


@dataclass
class BackendHttpSettingsDefinition(BaseModel):
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
    AuthenticationCertificate: Optional[Sequence["_AuthenticationCertificateDefinition"]]
    ConnectionDraining: Optional[Sequence["_ConnectionDrainingDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BackendHttpSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendHttpSettingsDefinition"]:
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
            AuthenticationCertificate=deserialize_list(json_data.get("AuthenticationCertificate"), AuthenticationCertificateDefinition),
            ConnectionDraining=deserialize_list(json_data.get("ConnectionDraining"), ConnectionDrainingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendHttpSettingsDefinition = BackendHttpSettingsDefinition


@dataclass
class ConnectionDrainingDefinition(BaseModel):
    DrainTimeoutSec: Optional[float]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionDrainingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionDrainingDefinition"]:
        if not json_data:
            return None
        return cls(
            DrainTimeoutSec=json_data.get("DrainTimeoutSec"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionDrainingDefinition = ConnectionDrainingDefinition


@dataclass
class CustomErrorConfigurationDefinition(BaseModel):
    CustomErrorPageUrl: Optional[str]
    StatusCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomErrorConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomErrorConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomErrorPageUrl=json_data.get("CustomErrorPageUrl"),
            StatusCode=json_data.get("StatusCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomErrorConfigurationDefinition = CustomErrorConfigurationDefinition


@dataclass
class FrontendIpConfigurationDefinition(BaseModel):
    Name: Optional[str]
    PrivateIpAddress: Optional[str]
    PrivateIpAddressAllocation: Optional[str]
    PublicIpAddressId: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FrontendIpConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrontendIpConfigurationDefinition"]:
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
_FrontendIpConfigurationDefinition = FrontendIpConfigurationDefinition


@dataclass
class FrontendPortDefinition(BaseModel):
    Name: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FrontendPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrontendPortDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrontendPortDefinition = FrontendPortDefinition


@dataclass
class GatewayIpConfigurationDefinition(BaseModel):
    Name: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayIpConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayIpConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayIpConfigurationDefinition = GatewayIpConfigurationDefinition


@dataclass
class HttpListenerDefinition(BaseModel):
    FirewallPolicyId: Optional[str]
    FrontendIpConfigurationName: Optional[str]
    FrontendPortName: Optional[str]
    HostName: Optional[str]
    HostNames: Optional[Sequence[str]]
    Name: Optional[str]
    Protocol: Optional[str]
    RequireSni: Optional[bool]
    SslCertificateName: Optional[str]
    CustomErrorConfiguration: Optional[Sequence["_CustomErrorConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpListenerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpListenerDefinition"]:
        if not json_data:
            return None
        return cls(
            FirewallPolicyId=json_data.get("FirewallPolicyId"),
            FrontendIpConfigurationName=json_data.get("FrontendIpConfigurationName"),
            FrontendPortName=json_data.get("FrontendPortName"),
            HostName=json_data.get("HostName"),
            HostNames=json_data.get("HostNames"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            RequireSni=json_data.get("RequireSni"),
            SslCertificateName=json_data.get("SslCertificateName"),
            CustomErrorConfiguration=deserialize_list(json_data.get("CustomErrorConfiguration"), CustomErrorConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpListenerDefinition = HttpListenerDefinition


@dataclass
class IdentityDefinition(BaseModel):
    IdentityIds: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityDefinition"]:
        if not json_data:
            return None
        return cls(
            IdentityIds=json_data.get("IdentityIds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityDefinition = IdentityDefinition


@dataclass
class ProbeDefinition(BaseModel):
    Host: Optional[str]
    Interval: Optional[float]
    MinimumServers: Optional[float]
    Name: Optional[str]
    Path: Optional[str]
    PickHostNameFromBackendHttpSettings: Optional[bool]
    Port: Optional[float]
    Protocol: Optional[str]
    Timeout: Optional[float]
    UnhealthyThreshold: Optional[float]
    Match: Optional[Sequence["_MatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProbeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProbeDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Interval=json_data.get("Interval"),
            MinimumServers=json_data.get("MinimumServers"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            PickHostNameFromBackendHttpSettings=json_data.get("PickHostNameFromBackendHttpSettings"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            Timeout=json_data.get("Timeout"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProbeDefinition = ProbeDefinition


@dataclass
class MatchDefinition(BaseModel):
    Body: Optional[str]
    StatusCode: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Body=json_data.get("Body"),
            StatusCode=json_data.get("StatusCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class RedirectConfigurationDefinition(BaseModel):
    IncludePath: Optional[bool]
    IncludeQueryString: Optional[bool]
    Name: Optional[str]
    RedirectType: Optional[str]
    TargetListenerName: Optional[str]
    TargetUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectConfigurationDefinition"]:
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
_RedirectConfigurationDefinition = RedirectConfigurationDefinition


@dataclass
class RequestRoutingRuleDefinition(BaseModel):
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
        cls: Type["_RequestRoutingRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestRoutingRuleDefinition"]:
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
_RequestRoutingRuleDefinition = RequestRoutingRuleDefinition


@dataclass
class RewriteRuleSetDefinition(BaseModel):
    Name: Optional[str]
    RewriteRule: Optional[Sequence["_RewriteRuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RewriteRuleSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RewriteRuleSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            RewriteRule=deserialize_list(json_data.get("RewriteRule"), RewriteRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RewriteRuleSetDefinition = RewriteRuleSetDefinition


@dataclass
class RewriteRuleDefinition(BaseModel):
    Name: Optional[str]
    RuleSequence: Optional[float]
    Condition: Optional[Sequence["_ConditionDefinition"]]
    RequestHeaderConfiguration: Optional[Sequence["_RequestHeaderConfigurationDefinition"]]
    ResponseHeaderConfiguration: Optional[Sequence["_ResponseHeaderConfigurationDefinition"]]
    Url: Optional[Sequence["_UrlDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RewriteRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RewriteRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            RuleSequence=json_data.get("RuleSequence"),
            Condition=deserialize_list(json_data.get("Condition"), ConditionDefinition),
            RequestHeaderConfiguration=deserialize_list(json_data.get("RequestHeaderConfiguration"), RequestHeaderConfigurationDefinition),
            ResponseHeaderConfiguration=deserialize_list(json_data.get("ResponseHeaderConfiguration"), ResponseHeaderConfigurationDefinition),
            Url=deserialize_list(json_data.get("Url"), UrlDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RewriteRuleDefinition = RewriteRuleDefinition


@dataclass
class ConditionDefinition(BaseModel):
    IgnoreCase: Optional[bool]
    Negate: Optional[bool]
    Pattern: Optional[str]
    Variable: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            IgnoreCase=json_data.get("IgnoreCase"),
            Negate=json_data.get("Negate"),
            Pattern=json_data.get("Pattern"),
            Variable=json_data.get("Variable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionDefinition = ConditionDefinition


@dataclass
class RequestHeaderConfigurationDefinition(BaseModel):
    HeaderName: Optional[str]
    HeaderValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestHeaderConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestHeaderConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            HeaderName=json_data.get("HeaderName"),
            HeaderValue=json_data.get("HeaderValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestHeaderConfigurationDefinition = RequestHeaderConfigurationDefinition


@dataclass
class ResponseHeaderConfigurationDefinition(BaseModel):
    HeaderName: Optional[str]
    HeaderValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseHeaderConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseHeaderConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            HeaderName=json_data.get("HeaderName"),
            HeaderValue=json_data.get("HeaderValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseHeaderConfigurationDefinition = ResponseHeaderConfigurationDefinition


@dataclass
class UrlDefinition(BaseModel):
    Path: Optional[str]
    QueryString: Optional[str]
    Reroute: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_UrlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            QueryString=json_data.get("QueryString"),
            Reroute=json_data.get("Reroute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlDefinition = UrlDefinition


@dataclass
class SkuDefinition(BaseModel):
    Capacity: Optional[float]
    Name: Optional[str]
    Tier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SkuDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SkuDefinition"]:
        if not json_data:
            return None
        return cls(
            Capacity=json_data.get("Capacity"),
            Name=json_data.get("Name"),
            Tier=json_data.get("Tier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SkuDefinition = SkuDefinition


@dataclass
class SslCertificateDefinition(BaseModel):
    Data: Optional[str]
    KeyVaultSecretId: Optional[str]
    Name: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslCertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslCertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            Data=json_data.get("Data"),
            KeyVaultSecretId=json_data.get("KeyVaultSecretId"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslCertificateDefinition = SslCertificateDefinition


@dataclass
class SslPolicyDefinition(BaseModel):
    CipherSuites: Optional[Sequence[str]]
    DisabledProtocols: Optional[Sequence[str]]
    MinProtocolVersion: Optional[str]
    PolicyName: Optional[str]
    PolicyType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslPolicyDefinition"]:
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
_SslPolicyDefinition = SslPolicyDefinition


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
class TrustedRootCertificateDefinition(BaseModel):
    Data: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrustedRootCertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrustedRootCertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            Data=json_data.get("Data"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrustedRootCertificateDefinition = TrustedRootCertificateDefinition


@dataclass
class UrlPathMapDefinition(BaseModel):
    DefaultBackendAddressPoolName: Optional[str]
    DefaultBackendHttpSettingsName: Optional[str]
    DefaultRedirectConfigurationName: Optional[str]
    DefaultRewriteRuleSetName: Optional[str]
    Name: Optional[str]
    PathRule: Optional[Sequence["_PathRuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UrlPathMapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlPathMapDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultBackendAddressPoolName=json_data.get("DefaultBackendAddressPoolName"),
            DefaultBackendHttpSettingsName=json_data.get("DefaultBackendHttpSettingsName"),
            DefaultRedirectConfigurationName=json_data.get("DefaultRedirectConfigurationName"),
            DefaultRewriteRuleSetName=json_data.get("DefaultRewriteRuleSetName"),
            Name=json_data.get("Name"),
            PathRule=deserialize_list(json_data.get("PathRule"), PathRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlPathMapDefinition = UrlPathMapDefinition


@dataclass
class PathRuleDefinition(BaseModel):
    BackendAddressPoolName: Optional[str]
    BackendHttpSettingsName: Optional[str]
    FirewallPolicyId: Optional[str]
    Name: Optional[str]
    Paths: Optional[Sequence[str]]
    RedirectConfigurationName: Optional[str]
    RewriteRuleSetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PathRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            BackendAddressPoolName=json_data.get("BackendAddressPoolName"),
            BackendHttpSettingsName=json_data.get("BackendHttpSettingsName"),
            FirewallPolicyId=json_data.get("FirewallPolicyId"),
            Name=json_data.get("Name"),
            Paths=json_data.get("Paths"),
            RedirectConfigurationName=json_data.get("RedirectConfigurationName"),
            RewriteRuleSetName=json_data.get("RewriteRuleSetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathRuleDefinition = PathRuleDefinition


@dataclass
class WafConfigurationDefinition(BaseModel):
    Enabled: Optional[bool]
    FileUploadLimitMb: Optional[float]
    FirewallMode: Optional[str]
    MaxRequestBodySizeKb: Optional[float]
    RequestBodyCheck: Optional[bool]
    RuleSetType: Optional[str]
    RuleSetVersion: Optional[str]
    DisabledRuleGroup: Optional[Sequence["_DisabledRuleGroupDefinition"]]
    Exclusion: Optional[Sequence["_ExclusionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WafConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WafConfigurationDefinition"]:
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
            DisabledRuleGroup=deserialize_list(json_data.get("DisabledRuleGroup"), DisabledRuleGroupDefinition),
            Exclusion=deserialize_list(json_data.get("Exclusion"), ExclusionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WafConfigurationDefinition = WafConfigurationDefinition


@dataclass
class DisabledRuleGroupDefinition(BaseModel):
    RuleGroupName: Optional[str]
    Rules: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_DisabledRuleGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DisabledRuleGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            RuleGroupName=json_data.get("RuleGroupName"),
            Rules=json_data.get("Rules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DisabledRuleGroupDefinition = DisabledRuleGroupDefinition


@dataclass
class ExclusionDefinition(BaseModel):
    MatchVariable: Optional[str]
    Selector: Optional[str]
    SelectorMatchOperator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExclusionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExclusionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchVariable=json_data.get("MatchVariable"),
            Selector=json_data.get("Selector"),
            SelectorMatchOperator=json_data.get("SelectorMatchOperator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExclusionDefinition = ExclusionDefinition


