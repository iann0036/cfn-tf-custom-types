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
    LoadBalancer: Optional[str]
    Name: Optional[str]
    State: Optional[bool]
    Type: Optional[str]
    Uri: Optional[str]
    ApplicationCookieStickinessPolicy: Optional[Sequence["_ApplicationCookieStickinessPolicy"]]
    CloudgatePolicy: Optional[Sequence["_CloudgatePolicy"]]
    LoadBalancerCookieStickinessPolicy: Optional[Sequence["_LoadBalancerCookieStickinessPolicy"]]
    LoadBalancingMechanismPolicy: Optional[Sequence["_LoadBalancingMechanismPolicy"]]
    RateLimitingRequestPolicy: Optional[Sequence["_RateLimitingRequestPolicy"]]
    RedirectPolicy: Optional[Sequence["_RedirectPolicy"]]
    ResourceAccessControlPolicy: Optional[Sequence["_ResourceAccessControlPolicy"]]
    SetRequestHeaderPolicy: Optional[Sequence["_SetRequestHeaderPolicy"]]
    SslNegotiationPolicy: Optional[Sequence["_SslNegotiationPolicy"]]
    TrustedCertificatePolicy: Optional[Sequence["_TrustedCertificatePolicy"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            LoadBalancer=json_data.get("LoadBalancer"),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            Type=json_data.get("Type"),
            Uri=json_data.get("Uri"),
            ApplicationCookieStickinessPolicy=json_data.get("ApplicationCookieStickinessPolicy"),
            CloudgatePolicy=json_data.get("CloudgatePolicy"),
            LoadBalancerCookieStickinessPolicy=json_data.get("LoadBalancerCookieStickinessPolicy"),
            LoadBalancingMechanismPolicy=json_data.get("LoadBalancingMechanismPolicy"),
            RateLimitingRequestPolicy=json_data.get("RateLimitingRequestPolicy"),
            RedirectPolicy=json_data.get("RedirectPolicy"),
            ResourceAccessControlPolicy=json_data.get("ResourceAccessControlPolicy"),
            SetRequestHeaderPolicy=json_data.get("SetRequestHeaderPolicy"),
            SslNegotiationPolicy=json_data.get("SslNegotiationPolicy"),
            TrustedCertificatePolicy=json_data.get("TrustedCertificatePolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ApplicationCookieStickinessPolicy:
    CookieName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationCookieStickinessPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationCookieStickinessPolicy"]:
        if not json_data:
            return None
        return cls(
            CookieName=json_data.get("CookieName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationCookieStickinessPolicy = ApplicationCookieStickinessPolicy


@dataclass
class CloudgatePolicy:
    CloudgateApplication: Optional[str]
    CloudgatePolicyName: Optional[str]
    IdentityServiceInstanceGuid: Optional[str]
    VirtualHostnameForPolicyAttribution: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudgatePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudgatePolicy"]:
        if not json_data:
            return None
        return cls(
            CloudgateApplication=json_data.get("CloudgateApplication"),
            CloudgatePolicyName=json_data.get("CloudgatePolicyName"),
            IdentityServiceInstanceGuid=json_data.get("IdentityServiceInstanceGuid"),
            VirtualHostnameForPolicyAttribution=json_data.get("VirtualHostnameForPolicyAttribution"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudgatePolicy = CloudgatePolicy


@dataclass
class LoadBalancerCookieStickinessPolicy:
    CookieExpirationPeriod: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancerCookieStickinessPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancerCookieStickinessPolicy"]:
        if not json_data:
            return None
        return cls(
            CookieExpirationPeriod=json_data.get("CookieExpirationPeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancerCookieStickinessPolicy = LoadBalancerCookieStickinessPolicy


@dataclass
class LoadBalancingMechanismPolicy:
    LoadBalancingMechanism: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancingMechanismPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancingMechanismPolicy"]:
        if not json_data:
            return None
        return cls(
            LoadBalancingMechanism=json_data.get("LoadBalancingMechanism"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancingMechanismPolicy = LoadBalancingMechanismPolicy


@dataclass
class RateLimitingRequestPolicy:
    BurstSize: Optional[float]
    DelayExcessiveRequests: Optional[bool]
    HttpErrorCode: Optional[float]
    LoggingLevel: Optional[str]
    RateLimitingCriteria: Optional[str]
    RequestsPerSecond: Optional[float]
    Zone: Optional[str]
    ZoneMemorySize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimitingRequestPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimitingRequestPolicy"]:
        if not json_data:
            return None
        return cls(
            BurstSize=json_data.get("BurstSize"),
            DelayExcessiveRequests=json_data.get("DelayExcessiveRequests"),
            HttpErrorCode=json_data.get("HttpErrorCode"),
            LoggingLevel=json_data.get("LoggingLevel"),
            RateLimitingCriteria=json_data.get("RateLimitingCriteria"),
            RequestsPerSecond=json_data.get("RequestsPerSecond"),
            Zone=json_data.get("Zone"),
            ZoneMemorySize=json_data.get("ZoneMemorySize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimitingRequestPolicy = RateLimitingRequestPolicy


@dataclass
class RedirectPolicy:
    RedirectUri: Optional[str]
    ResponseCode: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectPolicy"]:
        if not json_data:
            return None
        return cls(
            RedirectUri=json_data.get("RedirectUri"),
            ResponseCode=json_data.get("ResponseCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedirectPolicy = RedirectPolicy


@dataclass
class ResourceAccessControlPolicy:
    DeniedClients: Optional[Sequence[str]]
    Disposition: Optional[str]
    PermittedClients: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAccessControlPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAccessControlPolicy"]:
        if not json_data:
            return None
        return cls(
            DeniedClients=json_data.get("DeniedClients"),
            Disposition=json_data.get("Disposition"),
            PermittedClients=json_data.get("PermittedClients"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAccessControlPolicy = ResourceAccessControlPolicy


@dataclass
class SetRequestHeaderPolicy:
    ActionWhenHeaderExists: Optional[str]
    ActionWhenHeaderValueIs: Optional[Sequence[str]]
    ActionWhenHeaderValueIsNot: Optional[Sequence[str]]
    HeaderName: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SetRequestHeaderPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetRequestHeaderPolicy"]:
        if not json_data:
            return None
        return cls(
            ActionWhenHeaderExists=json_data.get("ActionWhenHeaderExists"),
            ActionWhenHeaderValueIs=json_data.get("ActionWhenHeaderValueIs"),
            ActionWhenHeaderValueIsNot=json_data.get("ActionWhenHeaderValueIsNot"),
            HeaderName=json_data.get("HeaderName"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetRequestHeaderPolicy = SetRequestHeaderPolicy


@dataclass
class SslNegotiationPolicy:
    Port: Optional[float]
    ServerOrderPreference: Optional[str]
    SslCiphers: Optional[Sequence[str]]
    SslProtocol: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SslNegotiationPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslNegotiationPolicy"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            ServerOrderPreference=json_data.get("ServerOrderPreference"),
            SslCiphers=json_data.get("SslCiphers"),
            SslProtocol=json_data.get("SslProtocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslNegotiationPolicy = SslNegotiationPolicy


@dataclass
class TrustedCertificatePolicy:
    TrustedCertificate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrustedCertificatePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrustedCertificatePolicy"]:
        if not json_data:
            return None
        return cls(
            TrustedCertificate=json_data.get("TrustedCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrustedCertificatePolicy = TrustedCertificatePolicy


