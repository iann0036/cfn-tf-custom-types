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
    AffinityCookieTtlSec: Optional[float]
    ConnectionDrainingTimeoutSec: Optional[float]
    CreationTimestamp: Optional[str]
    CustomRequestHeaders: Optional[Sequence[str]]
    CustomResponseHeaders: Optional[Sequence[str]]
    Description: Optional[str]
    EnableCdn: Optional[bool]
    Fingerprint: Optional[str]
    HealthChecks: Optional[Sequence[str]]
    Id: Optional[str]
    LoadBalancingScheme: Optional[str]
    LocalityLbPolicy: Optional[str]
    Name: Optional[str]
    PortName: Optional[str]
    Project: Optional[str]
    Protocol: Optional[str]
    SecurityPolicy: Optional[str]
    SelfLink: Optional[str]
    SessionAffinity: Optional[str]
    TimeoutSec: Optional[float]
    Backend: Optional[Sequence["_BackendDefinition"]]
    CdnPolicy: Optional[Sequence["_CdnPolicyDefinition"]]
    CircuitBreakers: Optional[Sequence["_CircuitBreakersDefinition"]]
    ConsistentHash: Optional[Sequence["_ConsistentHashDefinition"]]
    Iap: Optional[Sequence["_IapDefinition"]]
    LogConfig: Optional[Sequence["_LogConfigDefinition"]]
    OutlierDetection: Optional[Sequence["_OutlierDetectionDefinition"]]
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
            AffinityCookieTtlSec=json_data.get("AffinityCookieTtlSec"),
            ConnectionDrainingTimeoutSec=json_data.get("ConnectionDrainingTimeoutSec"),
            CreationTimestamp=json_data.get("CreationTimestamp"),
            CustomRequestHeaders=json_data.get("CustomRequestHeaders"),
            CustomResponseHeaders=json_data.get("CustomResponseHeaders"),
            Description=json_data.get("Description"),
            EnableCdn=json_data.get("EnableCdn"),
            Fingerprint=json_data.get("Fingerprint"),
            HealthChecks=json_data.get("HealthChecks"),
            Id=json_data.get("Id"),
            LoadBalancingScheme=json_data.get("LoadBalancingScheme"),
            LocalityLbPolicy=json_data.get("LocalityLbPolicy"),
            Name=json_data.get("Name"),
            PortName=json_data.get("PortName"),
            Project=json_data.get("Project"),
            Protocol=json_data.get("Protocol"),
            SecurityPolicy=json_data.get("SecurityPolicy"),
            SelfLink=json_data.get("SelfLink"),
            SessionAffinity=json_data.get("SessionAffinity"),
            TimeoutSec=json_data.get("TimeoutSec"),
            Backend=deserialize_list(json_data.get("Backend"), BackendDefinition),
            CdnPolicy=deserialize_list(json_data.get("CdnPolicy"), CdnPolicyDefinition),
            CircuitBreakers=deserialize_list(json_data.get("CircuitBreakers"), CircuitBreakersDefinition),
            ConsistentHash=deserialize_list(json_data.get("ConsistentHash"), ConsistentHashDefinition),
            Iap=deserialize_list(json_data.get("Iap"), IapDefinition),
            LogConfig=deserialize_list(json_data.get("LogConfig"), LogConfigDefinition),
            OutlierDetection=deserialize_list(json_data.get("OutlierDetection"), OutlierDetectionDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackendDefinition(BaseModel):
    BalancingMode: Optional[str]
    CapacityScaler: Optional[float]
    Description: Optional[str]
    Group: Optional[str]
    MaxConnections: Optional[float]
    MaxConnectionsPerEndpoint: Optional[float]
    MaxConnectionsPerInstance: Optional[float]
    MaxRate: Optional[float]
    MaxRatePerEndpoint: Optional[float]
    MaxRatePerInstance: Optional[float]
    MaxUtilization: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BackendDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendDefinition"]:
        if not json_data:
            return None
        return cls(
            BalancingMode=json_data.get("BalancingMode"),
            CapacityScaler=json_data.get("CapacityScaler"),
            Description=json_data.get("Description"),
            Group=json_data.get("Group"),
            MaxConnections=json_data.get("MaxConnections"),
            MaxConnectionsPerEndpoint=json_data.get("MaxConnectionsPerEndpoint"),
            MaxConnectionsPerInstance=json_data.get("MaxConnectionsPerInstance"),
            MaxRate=json_data.get("MaxRate"),
            MaxRatePerEndpoint=json_data.get("MaxRatePerEndpoint"),
            MaxRatePerInstance=json_data.get("MaxRatePerInstance"),
            MaxUtilization=json_data.get("MaxUtilization"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendDefinition = BackendDefinition


@dataclass
class CdnPolicyDefinition(BaseModel):
    CacheMode: Optional[str]
    ClientTtl: Optional[float]
    DefaultTtl: Optional[float]
    MaxTtl: Optional[float]
    NegativeCaching: Optional[bool]
    ServeWhileStale: Optional[float]
    SignedUrlCacheMaxAgeSec: Optional[float]
    CacheKeyPolicy: Optional[Sequence["_CacheKeyPolicyDefinition"]]
    NegativeCachingPolicy: Optional[Sequence["_NegativeCachingPolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CdnPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CdnPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            CacheMode=json_data.get("CacheMode"),
            ClientTtl=json_data.get("ClientTtl"),
            DefaultTtl=json_data.get("DefaultTtl"),
            MaxTtl=json_data.get("MaxTtl"),
            NegativeCaching=json_data.get("NegativeCaching"),
            ServeWhileStale=json_data.get("ServeWhileStale"),
            SignedUrlCacheMaxAgeSec=json_data.get("SignedUrlCacheMaxAgeSec"),
            CacheKeyPolicy=deserialize_list(json_data.get("CacheKeyPolicy"), CacheKeyPolicyDefinition),
            NegativeCachingPolicy=deserialize_list(json_data.get("NegativeCachingPolicy"), NegativeCachingPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CdnPolicyDefinition = CdnPolicyDefinition


@dataclass
class CacheKeyPolicyDefinition(BaseModel):
    IncludeHost: Optional[bool]
    IncludeProtocol: Optional[bool]
    IncludeQueryString: Optional[bool]
    QueryStringBlacklist: Optional[Sequence[str]]
    QueryStringWhitelist: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CacheKeyPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheKeyPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            IncludeHost=json_data.get("IncludeHost"),
            IncludeProtocol=json_data.get("IncludeProtocol"),
            IncludeQueryString=json_data.get("IncludeQueryString"),
            QueryStringBlacklist=json_data.get("QueryStringBlacklist"),
            QueryStringWhitelist=json_data.get("QueryStringWhitelist"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheKeyPolicyDefinition = CacheKeyPolicyDefinition


@dataclass
class NegativeCachingPolicyDefinition(BaseModel):
    Code: Optional[float]
    Ttl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NegativeCachingPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NegativeCachingPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NegativeCachingPolicyDefinition = NegativeCachingPolicyDefinition


@dataclass
class CircuitBreakersDefinition(BaseModel):
    MaxConnections: Optional[float]
    MaxPendingRequests: Optional[float]
    MaxRequests: Optional[float]
    MaxRequestsPerConnection: Optional[float]
    MaxRetries: Optional[float]
    ConnectTimeout: Optional[Sequence["_ConnectTimeoutDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CircuitBreakersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CircuitBreakersDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxConnections=json_data.get("MaxConnections"),
            MaxPendingRequests=json_data.get("MaxPendingRequests"),
            MaxRequests=json_data.get("MaxRequests"),
            MaxRequestsPerConnection=json_data.get("MaxRequestsPerConnection"),
            MaxRetries=json_data.get("MaxRetries"),
            ConnectTimeout=deserialize_list(json_data.get("ConnectTimeout"), ConnectTimeoutDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CircuitBreakersDefinition = CircuitBreakersDefinition


@dataclass
class ConnectTimeoutDefinition(BaseModel):
    Nanos: Optional[float]
    Seconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectTimeoutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectTimeoutDefinition"]:
        if not json_data:
            return None
        return cls(
            Nanos=json_data.get("Nanos"),
            Seconds=json_data.get("Seconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectTimeoutDefinition = ConnectTimeoutDefinition


@dataclass
class ConsistentHashDefinition(BaseModel):
    HttpHeaderName: Optional[str]
    MinimumRingSize: Optional[float]
    HttpCookie: Optional[Sequence["_HttpCookieDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConsistentHashDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConsistentHashDefinition"]:
        if not json_data:
            return None
        return cls(
            HttpHeaderName=json_data.get("HttpHeaderName"),
            MinimumRingSize=json_data.get("MinimumRingSize"),
            HttpCookie=deserialize_list(json_data.get("HttpCookie"), HttpCookieDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConsistentHashDefinition = ConsistentHashDefinition


@dataclass
class HttpCookieDefinition(BaseModel):
    Name: Optional[str]
    Path: Optional[str]
    Ttl: Optional[Sequence["_TtlDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpCookieDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpCookieDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Ttl=deserialize_list(json_data.get("Ttl"), TtlDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpCookieDefinition = HttpCookieDefinition


@dataclass
class TtlDefinition(BaseModel):
    Nanos: Optional[float]
    Seconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TtlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TtlDefinition"]:
        if not json_data:
            return None
        return cls(
            Nanos=json_data.get("Nanos"),
            Seconds=json_data.get("Seconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TtlDefinition = TtlDefinition


@dataclass
class IapDefinition(BaseModel):
    Oauth2ClientId: Optional[str]
    Oauth2ClientSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IapDefinition"]:
        if not json_data:
            return None
        return cls(
            Oauth2ClientId=json_data.get("Oauth2ClientId"),
            Oauth2ClientSecret=json_data.get("Oauth2ClientSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IapDefinition = IapDefinition


@dataclass
class LogConfigDefinition(BaseModel):
    Enable: Optional[bool]
    SampleRate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            SampleRate=json_data.get("SampleRate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfigDefinition = LogConfigDefinition


@dataclass
class OutlierDetectionDefinition(BaseModel):
    ConsecutiveErrors: Optional[float]
    ConsecutiveGatewayFailure: Optional[float]
    EnforcingConsecutiveErrors: Optional[float]
    EnforcingConsecutiveGatewayFailure: Optional[float]
    EnforcingSuccessRate: Optional[float]
    MaxEjectionPercent: Optional[float]
    SuccessRateMinimumHosts: Optional[float]
    SuccessRateRequestVolume: Optional[float]
    SuccessRateStdevFactor: Optional[float]
    BaseEjectionTime: Optional[Sequence["_BaseEjectionTimeDefinition"]]
    Interval: Optional[Sequence["_IntervalDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutlierDetectionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutlierDetectionDefinition"]:
        if not json_data:
            return None
        return cls(
            ConsecutiveErrors=json_data.get("ConsecutiveErrors"),
            ConsecutiveGatewayFailure=json_data.get("ConsecutiveGatewayFailure"),
            EnforcingConsecutiveErrors=json_data.get("EnforcingConsecutiveErrors"),
            EnforcingConsecutiveGatewayFailure=json_data.get("EnforcingConsecutiveGatewayFailure"),
            EnforcingSuccessRate=json_data.get("EnforcingSuccessRate"),
            MaxEjectionPercent=json_data.get("MaxEjectionPercent"),
            SuccessRateMinimumHosts=json_data.get("SuccessRateMinimumHosts"),
            SuccessRateRequestVolume=json_data.get("SuccessRateRequestVolume"),
            SuccessRateStdevFactor=json_data.get("SuccessRateStdevFactor"),
            BaseEjectionTime=deserialize_list(json_data.get("BaseEjectionTime"), BaseEjectionTimeDefinition),
            Interval=deserialize_list(json_data.get("Interval"), IntervalDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutlierDetectionDefinition = OutlierDetectionDefinition


@dataclass
class BaseEjectionTimeDefinition(BaseModel):
    Nanos: Optional[float]
    Seconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BaseEjectionTimeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BaseEjectionTimeDefinition"]:
        if not json_data:
            return None
        return cls(
            Nanos=json_data.get("Nanos"),
            Seconds=json_data.get("Seconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BaseEjectionTimeDefinition = BaseEjectionTimeDefinition


@dataclass
class IntervalDefinition(BaseModel):
    Nanos: Optional[float]
    Seconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IntervalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntervalDefinition"]:
        if not json_data:
            return None
        return cls(
            Nanos=json_data.get("Nanos"),
            Seconds=json_data.get("Seconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntervalDefinition = IntervalDefinition


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


