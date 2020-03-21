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
    AffinityCookieTtlSec: Optional[float]
    ConnectionDrainingTimeoutSec: Optional[float]
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    EnableCdn: Optional[bool]
    Fingerprint: Optional[str]
    HealthChecks: Optional[Sequence[str]]
    LoadBalancingScheme: Optional[str]
    Name: Optional[str]
    PortName: Optional[str]
    Project: Optional[str]
    Protocol: Optional[str]
    SecurityPolicy: Optional[str]
    SelfLink: Optional[str]
    SessionAffinity: Optional[str]
    TimeoutSec: Optional[float]
    Backend: Optional[Sequence["_Backend"]]
    CdnPolicy: Optional[Sequence["_CdnPolicy"]]
    Iap: Optional[Sequence["_Iap"]]
    Timeouts: Optional["_Timeouts"]
    CacheKeyPolicy: Optional[Sequence["_CacheKeyPolicy"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AffinityCookieTtlSec=json_data.get("AffinityCookieTtlSec"),
            ConnectionDrainingTimeoutSec=json_data.get("ConnectionDrainingTimeoutSec"),
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            EnableCdn=json_data.get("EnableCdn"),
            Fingerprint=json_data.get("Fingerprint"),
            HealthChecks=json_data.get("HealthChecks"),
            LoadBalancingScheme=json_data.get("LoadBalancingScheme"),
            Name=json_data.get("Name"),
            PortName=json_data.get("PortName"),
            Project=json_data.get("Project"),
            Protocol=json_data.get("Protocol"),
            SecurityPolicy=json_data.get("SecurityPolicy"),
            SelfLink=json_data.get("SelfLink"),
            SessionAffinity=json_data.get("SessionAffinity"),
            TimeoutSec=json_data.get("TimeoutSec"),
            Backend=json_data.get("Backend"),
            CdnPolicy=json_data.get("CdnPolicy"),
            Iap=json_data.get("Iap"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            CacheKeyPolicy=json_data.get("CacheKeyPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Backend:
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
        cls: Type["_Backend"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Backend"]:
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
_Backend = Backend


@dataclass
class CdnPolicy:
    SignedUrlCacheMaxAgeSec: Optional[float]
    CacheKeyPolicy: Optional[Sequence["_CacheKeyPolicy"]]

    @classmethod
    def _deserialize(
        cls: Type["_CdnPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CdnPolicy"]:
        if not json_data:
            return None
        return cls(
            SignedUrlCacheMaxAgeSec=json_data.get("SignedUrlCacheMaxAgeSec"),
            CacheKeyPolicy=json_data.get("CacheKeyPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CdnPolicy = CdnPolicy


@dataclass
class CacheKeyPolicy:
    IncludeHost: Optional[bool]
    IncludeProtocol: Optional[bool]
    IncludeQueryString: Optional[bool]
    QueryStringBlacklist: Optional[Sequence[str]]
    QueryStringWhitelist: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CacheKeyPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheKeyPolicy"]:
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
_CacheKeyPolicy = CacheKeyPolicy


@dataclass
class Iap:
    Oauth2ClientId: Optional[str]
    Oauth2ClientSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Iap"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Iap"]:
        if not json_data:
            return None
        return cls(
            Oauth2ClientId=json_data.get("Oauth2ClientId"),
            Oauth2ClientSecret=json_data.get("Oauth2ClientSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Iap = Iap


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


