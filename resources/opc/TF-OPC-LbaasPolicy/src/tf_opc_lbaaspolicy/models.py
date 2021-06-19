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
    Id: Optional[str]
    LoadBalancer: Optional[str]
    Name: Optional[str]
    State: Optional[bool]
    Type: Optional[str]
    Uri: Optional[str]
    ApplicationCookieStickinessPolicy: Optional[Sequence["_ApplicationCookieStickinessPolicyDefinition"]]
    CloudgatePolicy: Optional[Sequence["_CloudgatePolicyDefinition"]]
    LoadBalancerCookieStickinessPolicy: Optional[Sequence["_LoadBalancerCookieStickinessPolicyDefinition"]]
    LoadBalancingMechanismPolicy: Optional[Sequence["_LoadBalancingMechanismPolicyDefinition"]]
    RateLimitingRequestPolicy: Optional[Sequence["_RateLimitingRequestPolicyDefinition"]]
    RedirectPolicy: Optional[Sequence["_RedirectPolicyDefinition"]]
    ResourceAccessControlPolicy: Optional[Sequence["_ResourceAccessControlPolicyDefinition"]]
    SetRequestHeaderPolicy: Optional[Sequence["_SetRequestHeaderPolicyDefinition"]]
    SslNegotiationPolicy: Optional[Sequence["_SslNegotiationPolicyDefinition"]]
    TrustedCertificatePolicy: Optional[Sequence["_TrustedCertificatePolicyDefinition"]]

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
            Id=json_data.get("Id"),
            LoadBalancer=json_data.get("LoadBalancer"),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            Type=json_data.get("Type"),
            Uri=json_data.get("Uri"),
            ApplicationCookieStickinessPolicy=deserialize_list(json_data.get("ApplicationCookieStickinessPolicy"), ApplicationCookieStickinessPolicyDefinition),
            CloudgatePolicy=deserialize_list(json_data.get("CloudgatePolicy"), CloudgatePolicyDefinition),
            LoadBalancerCookieStickinessPolicy=deserialize_list(json_data.get("LoadBalancerCookieStickinessPolicy"), LoadBalancerCookieStickinessPolicyDefinition),
            LoadBalancingMechanismPolicy=deserialize_list(json_data.get("LoadBalancingMechanismPolicy"), LoadBalancingMechanismPolicyDefinition),
            RateLimitingRequestPolicy=deserialize_list(json_data.get("RateLimitingRequestPolicy"), RateLimitingRequestPolicyDefinition),
            RedirectPolicy=deserialize_list(json_data.get("RedirectPolicy"), RedirectPolicyDefinition),
            ResourceAccessControlPolicy=deserialize_list(json_data.get("ResourceAccessControlPolicy"), ResourceAccessControlPolicyDefinition),
            SetRequestHeaderPolicy=deserialize_list(json_data.get("SetRequestHeaderPolicy"), SetRequestHeaderPolicyDefinition),
            SslNegotiationPolicy=deserialize_list(json_data.get("SslNegotiationPolicy"), SslNegotiationPolicyDefinition),
            TrustedCertificatePolicy=deserialize_list(json_data.get("TrustedCertificatePolicy"), TrustedCertificatePolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ApplicationCookieStickinessPolicyDefinition(BaseModel):
    CookieName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationCookieStickinessPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationCookieStickinessPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            CookieName=json_data.get("CookieName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationCookieStickinessPolicyDefinition = ApplicationCookieStickinessPolicyDefinition


@dataclass
class CloudgatePolicyDefinition(BaseModel):
    CloudgateApplication: Optional[str]
    CloudgatePolicyName: Optional[str]
    IdentityServiceInstanceGuid: Optional[str]
    VirtualHostnameForPolicyAttribution: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudgatePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudgatePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudgateApplication=json_data.get("CloudgateApplication"),
            CloudgatePolicyName=json_data.get("CloudgatePolicyName"),
            IdentityServiceInstanceGuid=json_data.get("IdentityServiceInstanceGuid"),
            VirtualHostnameForPolicyAttribution=json_data.get("VirtualHostnameForPolicyAttribution"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudgatePolicyDefinition = CloudgatePolicyDefinition


@dataclass
class LoadBalancerCookieStickinessPolicyDefinition(BaseModel):
    CookieExpirationPeriod: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancerCookieStickinessPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancerCookieStickinessPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            CookieExpirationPeriod=json_data.get("CookieExpirationPeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancerCookieStickinessPolicyDefinition = LoadBalancerCookieStickinessPolicyDefinition


@dataclass
class LoadBalancingMechanismPolicyDefinition(BaseModel):
    LoadBalancingMechanism: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancingMechanismPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancingMechanismPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            LoadBalancingMechanism=json_data.get("LoadBalancingMechanism"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancingMechanismPolicyDefinition = LoadBalancingMechanismPolicyDefinition


@dataclass
class RateLimitingRequestPolicyDefinition(BaseModel):
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
        cls: Type["_RateLimitingRequestPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimitingRequestPolicyDefinition"]:
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
_RateLimitingRequestPolicyDefinition = RateLimitingRequestPolicyDefinition


@dataclass
class RedirectPolicyDefinition(BaseModel):
    RedirectUri: Optional[str]
    ResponseCode: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            RedirectUri=json_data.get("RedirectUri"),
            ResponseCode=json_data.get("ResponseCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedirectPolicyDefinition = RedirectPolicyDefinition


@dataclass
class ResourceAccessControlPolicyDefinition(BaseModel):
    DeniedClients: Optional[Sequence[str]]
    Disposition: Optional[str]
    PermittedClients: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAccessControlPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAccessControlPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            DeniedClients=json_data.get("DeniedClients"),
            Disposition=json_data.get("Disposition"),
            PermittedClients=json_data.get("PermittedClients"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAccessControlPolicyDefinition = ResourceAccessControlPolicyDefinition


@dataclass
class SetRequestHeaderPolicyDefinition(BaseModel):
    ActionWhenHeaderExists: Optional[str]
    ActionWhenHeaderValueIs: Optional[Sequence[str]]
    ActionWhenHeaderValueIsNot: Optional[Sequence[str]]
    HeaderName: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SetRequestHeaderPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetRequestHeaderPolicyDefinition"]:
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
_SetRequestHeaderPolicyDefinition = SetRequestHeaderPolicyDefinition


@dataclass
class SslNegotiationPolicyDefinition(BaseModel):
    Port: Optional[float]
    ServerOrderPreference: Optional[str]
    SslCiphers: Optional[Sequence[str]]
    SslProtocol: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SslNegotiationPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslNegotiationPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            ServerOrderPreference=json_data.get("ServerOrderPreference"),
            SslCiphers=json_data.get("SslCiphers"),
            SslProtocol=json_data.get("SslProtocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslNegotiationPolicyDefinition = SslNegotiationPolicyDefinition


@dataclass
class TrustedCertificatePolicyDefinition(BaseModel):
    TrustedCertificate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrustedCertificatePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrustedCertificatePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            TrustedCertificate=json_data.get("TrustedCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrustedCertificatePolicyDefinition = TrustedCertificatePolicyDefinition


