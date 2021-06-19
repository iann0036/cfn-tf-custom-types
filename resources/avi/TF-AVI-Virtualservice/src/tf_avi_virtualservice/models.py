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
    ActiveStandbySeTag: Optional[str]
    AdvertiseDownVs: Optional[bool]
    AllowInvalidClientCert: Optional[bool]
    AnalyticsProfileRef: Optional[str]
    ApicContractGraph: Optional[str]
    ApplicationProfileRef: Optional[str]
    BgpPeerLabels: Optional[Sequence[str]]
    BulkSyncKvcache: Optional[bool]
    CloseClientConnOnConfigUpdate: Optional[bool]
    CloudConfigCksum: Optional[str]
    CloudRef: Optional[str]
    CloudType: Optional[str]
    CreatedBy: Optional[str]
    DelayFairness: Optional[bool]
    Description: Optional[str]
    EastWestPlacement: Optional[bool]
    EnableAutogw: Optional[bool]
    EnableRhi: Optional[bool]
    EnableRhiSnat: Optional[bool]
    Enabled: Optional[bool]
    ErrorPageProfileRef: Optional[str]
    FlowDist: Optional[str]
    FlowLabelType: Optional[str]
    Fqdn: Optional[str]
    HostNameXlate: Optional[str]
    IcapRequestProfileRefs: Optional[Sequence[str]]
    Id: Optional[str]
    IgnPoolNetReach: Optional[bool]
    LimitDoser: Optional[bool]
    MaxCpsPerClient: Optional[float]
    MicroserviceRef: Optional[str]
    MinPoolsUp: Optional[float]
    Name: Optional[str]
    NetworkProfileRef: Optional[str]
    NetworkSecurityPolicyRef: Optional[str]
    NsxSecuritygroup: Optional[Sequence[str]]
    PoolGroupRef: Optional[str]
    PoolRef: Optional[str]
    RemoveListeningPortOnVsDown: Optional[bool]
    ScaleoutEcmp: Optional[bool]
    SeGroupRef: Optional[str]
    SecurityPolicyRef: Optional[str]
    ServerNetworkProfileRef: Optional[str]
    ServiceMetadata: Optional[str]
    SslKeyAndCertificateRefs: Optional[Sequence[str]]
    SslProfileRef: Optional[str]
    SslSessCacheAvgSize: Optional[float]
    SsoPolicyRef: Optional[str]
    TenantRef: Optional[str]
    TestSeDatastoreLevel1Ref: Optional[str]
    TrafficCloneProfileRef: Optional[str]
    TrafficEnabled: Optional[bool]
    Type: Optional[str]
    UseBridgeIpAsVip: Optional[bool]
    UseVipAsSnat: Optional[bool]
    Uuid: Optional[str]
    VhDomainName: Optional[Sequence[str]]
    VhParentVsUuid: Optional[str]
    VhType: Optional[str]
    VrfContextRef: Optional[str]
    VsvipCloudConfigCksum: Optional[str]
    VsvipRef: Optional[str]
    WafPolicyRef: Optional[str]
    Weight: Optional[float]
    AnalyticsPolicy: Optional[Sequence["_AnalyticsPolicyDefinition"]]
    ClientAuth: Optional[Sequence["_ClientAuthDefinition"]]
    ConnectionsRateLimit: Optional[Sequence["_ConnectionsRateLimitDefinition"]]
    ContentRewrite: Optional[Sequence["_ContentRewriteDefinition"]]
    DnsInfo: Optional[Sequence["_DnsInfoDefinition"]]
    DnsPolicies: Optional[Sequence["_DnsPoliciesDefinition"]]
    HttpPolicies: Optional[Sequence["_HttpPoliciesDefinition"]]
    JwtConfig: Optional[Sequence["_JwtConfigDefinition"]]
    L4Policies: Optional[Sequence["_L4PoliciesDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    PerformanceLimits: Optional[Sequence["_PerformanceLimitsDefinition"]]
    RequestsRateLimit: Optional[Sequence["_RequestsRateLimitDefinition"]]
    SamlSpConfig: Optional[Sequence["_SamlSpConfigDefinition"]]
    ServicePoolSelect: Optional[Sequence["_ServicePoolSelectDefinition"]]
    Services: Optional[Sequence["_ServicesDefinition"]]
    SidebandProfile: Optional[Sequence["_SidebandProfileDefinition"]]
    SnatIp: Optional[Sequence["_SnatIpDefinition"]]
    SslProfileSelectors: Optional[Sequence["_SslProfileSelectorsDefinition"]]
    StaticDnsRecords: Optional[Sequence["_StaticDnsRecordsDefinition"]]
    TopologyPolicies: Optional[Sequence["_TopologyPoliciesDefinition"]]
    VhMatches: Optional[Sequence["_VhMatchesDefinition"]]
    Vip: Optional[Sequence["_VipDefinition"]]
    VsDatascripts: Optional[Sequence["_VsDatascriptsDefinition"]]

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
            ActiveStandbySeTag=json_data.get("ActiveStandbySeTag"),
            AdvertiseDownVs=json_data.get("AdvertiseDownVs"),
            AllowInvalidClientCert=json_data.get("AllowInvalidClientCert"),
            AnalyticsProfileRef=json_data.get("AnalyticsProfileRef"),
            ApicContractGraph=json_data.get("ApicContractGraph"),
            ApplicationProfileRef=json_data.get("ApplicationProfileRef"),
            BgpPeerLabels=json_data.get("BgpPeerLabels"),
            BulkSyncKvcache=json_data.get("BulkSyncKvcache"),
            CloseClientConnOnConfigUpdate=json_data.get("CloseClientConnOnConfigUpdate"),
            CloudConfigCksum=json_data.get("CloudConfigCksum"),
            CloudRef=json_data.get("CloudRef"),
            CloudType=json_data.get("CloudType"),
            CreatedBy=json_data.get("CreatedBy"),
            DelayFairness=json_data.get("DelayFairness"),
            Description=json_data.get("Description"),
            EastWestPlacement=json_data.get("EastWestPlacement"),
            EnableAutogw=json_data.get("EnableAutogw"),
            EnableRhi=json_data.get("EnableRhi"),
            EnableRhiSnat=json_data.get("EnableRhiSnat"),
            Enabled=json_data.get("Enabled"),
            ErrorPageProfileRef=json_data.get("ErrorPageProfileRef"),
            FlowDist=json_data.get("FlowDist"),
            FlowLabelType=json_data.get("FlowLabelType"),
            Fqdn=json_data.get("Fqdn"),
            HostNameXlate=json_data.get("HostNameXlate"),
            IcapRequestProfileRefs=json_data.get("IcapRequestProfileRefs"),
            Id=json_data.get("Id"),
            IgnPoolNetReach=json_data.get("IgnPoolNetReach"),
            LimitDoser=json_data.get("LimitDoser"),
            MaxCpsPerClient=json_data.get("MaxCpsPerClient"),
            MicroserviceRef=json_data.get("MicroserviceRef"),
            MinPoolsUp=json_data.get("MinPoolsUp"),
            Name=json_data.get("Name"),
            NetworkProfileRef=json_data.get("NetworkProfileRef"),
            NetworkSecurityPolicyRef=json_data.get("NetworkSecurityPolicyRef"),
            NsxSecuritygroup=json_data.get("NsxSecuritygroup"),
            PoolGroupRef=json_data.get("PoolGroupRef"),
            PoolRef=json_data.get("PoolRef"),
            RemoveListeningPortOnVsDown=json_data.get("RemoveListeningPortOnVsDown"),
            ScaleoutEcmp=json_data.get("ScaleoutEcmp"),
            SeGroupRef=json_data.get("SeGroupRef"),
            SecurityPolicyRef=json_data.get("SecurityPolicyRef"),
            ServerNetworkProfileRef=json_data.get("ServerNetworkProfileRef"),
            ServiceMetadata=json_data.get("ServiceMetadata"),
            SslKeyAndCertificateRefs=json_data.get("SslKeyAndCertificateRefs"),
            SslProfileRef=json_data.get("SslProfileRef"),
            SslSessCacheAvgSize=json_data.get("SslSessCacheAvgSize"),
            SsoPolicyRef=json_data.get("SsoPolicyRef"),
            TenantRef=json_data.get("TenantRef"),
            TestSeDatastoreLevel1Ref=json_data.get("TestSeDatastoreLevel1Ref"),
            TrafficCloneProfileRef=json_data.get("TrafficCloneProfileRef"),
            TrafficEnabled=json_data.get("TrafficEnabled"),
            Type=json_data.get("Type"),
            UseBridgeIpAsVip=json_data.get("UseBridgeIpAsVip"),
            UseVipAsSnat=json_data.get("UseVipAsSnat"),
            Uuid=json_data.get("Uuid"),
            VhDomainName=json_data.get("VhDomainName"),
            VhParentVsUuid=json_data.get("VhParentVsUuid"),
            VhType=json_data.get("VhType"),
            VrfContextRef=json_data.get("VrfContextRef"),
            VsvipCloudConfigCksum=json_data.get("VsvipCloudConfigCksum"),
            VsvipRef=json_data.get("VsvipRef"),
            WafPolicyRef=json_data.get("WafPolicyRef"),
            Weight=json_data.get("Weight"),
            AnalyticsPolicy=deserialize_list(json_data.get("AnalyticsPolicy"), AnalyticsPolicyDefinition),
            ClientAuth=deserialize_list(json_data.get("ClientAuth"), ClientAuthDefinition),
            ConnectionsRateLimit=deserialize_list(json_data.get("ConnectionsRateLimit"), ConnectionsRateLimitDefinition),
            ContentRewrite=deserialize_list(json_data.get("ContentRewrite"), ContentRewriteDefinition),
            DnsInfo=deserialize_list(json_data.get("DnsInfo"), DnsInfoDefinition),
            DnsPolicies=deserialize_list(json_data.get("DnsPolicies"), DnsPoliciesDefinition),
            HttpPolicies=deserialize_list(json_data.get("HttpPolicies"), HttpPoliciesDefinition),
            JwtConfig=deserialize_list(json_data.get("JwtConfig"), JwtConfigDefinition),
            L4Policies=deserialize_list(json_data.get("L4Policies"), L4PoliciesDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            PerformanceLimits=deserialize_list(json_data.get("PerformanceLimits"), PerformanceLimitsDefinition),
            RequestsRateLimit=deserialize_list(json_data.get("RequestsRateLimit"), RequestsRateLimitDefinition),
            SamlSpConfig=deserialize_list(json_data.get("SamlSpConfig"), SamlSpConfigDefinition),
            ServicePoolSelect=deserialize_list(json_data.get("ServicePoolSelect"), ServicePoolSelectDefinition),
            Services=deserialize_list(json_data.get("Services"), ServicesDefinition),
            SidebandProfile=deserialize_list(json_data.get("SidebandProfile"), SidebandProfileDefinition),
            SnatIp=deserialize_list(json_data.get("SnatIp"), SnatIpDefinition),
            SslProfileSelectors=deserialize_list(json_data.get("SslProfileSelectors"), SslProfileSelectorsDefinition),
            StaticDnsRecords=deserialize_list(json_data.get("StaticDnsRecords"), StaticDnsRecordsDefinition),
            TopologyPolicies=deserialize_list(json_data.get("TopologyPolicies"), TopologyPoliciesDefinition),
            VhMatches=deserialize_list(json_data.get("VhMatches"), VhMatchesDefinition),
            Vip=deserialize_list(json_data.get("Vip"), VipDefinition),
            VsDatascripts=deserialize_list(json_data.get("VsDatascripts"), VsDatascriptsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnalyticsPolicyDefinition(BaseModel):
    AllHeaders: Optional[bool]
    ClientInsights: Optional[str]
    SignificantLogThrottle: Optional[float]
    UdfLogThrottle: Optional[float]
    ClientInsightsSampling: Optional[Sequence["_ClientInsightsSamplingDefinition"]]
    ClientLogFilters: Optional[Sequence["_ClientLogFiltersDefinition"]]
    FullClientLogs: Optional[Sequence["_FullClientLogsDefinition"]]
    LearningLogPolicy: Optional[Sequence["_LearningLogPolicyDefinition"]]
    MetricsRealtimeUpdate: Optional[Sequence["_MetricsRealtimeUpdateDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AnalyticsPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalyticsPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            AllHeaders=json_data.get("AllHeaders"),
            ClientInsights=json_data.get("ClientInsights"),
            SignificantLogThrottle=json_data.get("SignificantLogThrottle"),
            UdfLogThrottle=json_data.get("UdfLogThrottle"),
            ClientInsightsSampling=deserialize_list(json_data.get("ClientInsightsSampling"), ClientInsightsSamplingDefinition),
            ClientLogFilters=deserialize_list(json_data.get("ClientLogFilters"), ClientLogFiltersDefinition),
            FullClientLogs=deserialize_list(json_data.get("FullClientLogs"), FullClientLogsDefinition),
            LearningLogPolicy=deserialize_list(json_data.get("LearningLogPolicy"), LearningLogPolicyDefinition),
            MetricsRealtimeUpdate=deserialize_list(json_data.get("MetricsRealtimeUpdate"), MetricsRealtimeUpdateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalyticsPolicyDefinition = AnalyticsPolicyDefinition


@dataclass
class ClientInsightsSamplingDefinition(BaseModel):
    ClientIp: Optional[Sequence["_ClientIpDefinition"]]
    SampleUris: Optional[Sequence["_SampleUrisDefinition"]]
    SkipUris: Optional[Sequence["_SkipUrisDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientInsightsSamplingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientInsightsSamplingDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientIp=deserialize_list(json_data.get("ClientIp"), ClientIpDefinition),
            SampleUris=deserialize_list(json_data.get("SampleUris"), SampleUrisDefinition),
            SkipUris=deserialize_list(json_data.get("SkipUris"), SkipUrisDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientInsightsSamplingDefinition = ClientInsightsSamplingDefinition


@dataclass
class ClientIpDefinition(BaseModel):
    GroupRefs: Optional[Sequence[str]]
    MatchCriteria: Optional[str]
    Addrs: Optional[Sequence["_AddrsDefinition"]]
    Prefixes: Optional[Sequence["_PrefixesDefinition"]]
    Ranges: Optional[Sequence["_RangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientIpDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupRefs=json_data.get("GroupRefs"),
            MatchCriteria=json_data.get("MatchCriteria"),
            Addrs=deserialize_list(json_data.get("Addrs"), AddrsDefinition),
            Prefixes=deserialize_list(json_data.get("Prefixes"), PrefixesDefinition),
            Ranges=deserialize_list(json_data.get("Ranges"), RangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientIpDefinition = ClientIpDefinition


@dataclass
class AddrsDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddrsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddrsDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddrsDefinition = AddrsDefinition


@dataclass
class PrefixesDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixesDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixesDefinition = PrefixesDefinition


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
class RangesDefinition(BaseModel):
    Begin: Optional[Sequence["_BeginDefinition"]]
    End: Optional[Sequence["_EndDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RangesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangesDefinition"]:
        if not json_data:
            return None
        return cls(
            Begin=deserialize_list(json_data.get("Begin"), BeginDefinition),
            End=deserialize_list(json_data.get("End"), EndDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangesDefinition = RangesDefinition


@dataclass
class BeginDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BeginDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BeginDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BeginDefinition = BeginDefinition


@dataclass
class EndDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndDefinition = EndDefinition


@dataclass
class SampleUrisDefinition(BaseModel):
    MatchCriteria: Optional[str]
    MatchStr: Optional[Sequence[str]]
    StringGroupRefs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SampleUrisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SampleUrisDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            MatchStr=json_data.get("MatchStr"),
            StringGroupRefs=json_data.get("StringGroupRefs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SampleUrisDefinition = SampleUrisDefinition


@dataclass
class SkipUrisDefinition(BaseModel):
    MatchCriteria: Optional[str]
    MatchStr: Optional[Sequence[str]]
    StringGroupRefs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SkipUrisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SkipUrisDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            MatchStr=json_data.get("MatchStr"),
            StringGroupRefs=json_data.get("StringGroupRefs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SkipUrisDefinition = SkipUrisDefinition


@dataclass
class ClientLogFiltersDefinition(BaseModel):
    AllHeaders: Optional[bool]
    Duration: Optional[float]
    Enabled: Optional[bool]
    Index: Optional[float]
    Name: Optional[str]
    ClientIp: Optional[Sequence["_ClientIpDefinition"]]
    Uri: Optional[Sequence["_UriDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientLogFiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientLogFiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            AllHeaders=json_data.get("AllHeaders"),
            Duration=json_data.get("Duration"),
            Enabled=json_data.get("Enabled"),
            Index=json_data.get("Index"),
            Name=json_data.get("Name"),
            ClientIp=deserialize_list(json_data.get("ClientIp"), ClientIpDefinition),
            Uri=deserialize_list(json_data.get("Uri"), UriDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientLogFiltersDefinition = ClientLogFiltersDefinition


@dataclass
class UriDefinition(BaseModel):
    MatchCriteria: Optional[str]
    MatchStr: Optional[Sequence[str]]
    StringGroupRefs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_UriDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UriDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            MatchStr=json_data.get("MatchStr"),
            StringGroupRefs=json_data.get("StringGroupRefs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UriDefinition = UriDefinition


@dataclass
class FullClientLogsDefinition(BaseModel):
    Duration: Optional[float]
    Enabled: Optional[bool]
    Throttle: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FullClientLogsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FullClientLogsDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            Enabled=json_data.get("Enabled"),
            Throttle=json_data.get("Throttle"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FullClientLogsDefinition = FullClientLogsDefinition


@dataclass
class LearningLogPolicyDefinition(BaseModel):
    Enabled: Optional[bool]
    Host: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LearningLogPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LearningLogPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Host=json_data.get("Host"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LearningLogPolicyDefinition = LearningLogPolicyDefinition


@dataclass
class MetricsRealtimeUpdateDefinition(BaseModel):
    Duration: Optional[float]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_MetricsRealtimeUpdateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricsRealtimeUpdateDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricsRealtimeUpdateDefinition = MetricsRealtimeUpdateDefinition


@dataclass
class ClientAuthDefinition(BaseModel):
    AuthProfileRef: Optional[str]
    Realm: Optional[str]
    Type: Optional[str]
    RequestUriPath: Optional[Sequence["_RequestUriPathDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientAuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientAuthDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthProfileRef=json_data.get("AuthProfileRef"),
            Realm=json_data.get("Realm"),
            Type=json_data.get("Type"),
            RequestUriPath=deserialize_list(json_data.get("RequestUriPath"), RequestUriPathDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientAuthDefinition = ClientAuthDefinition


@dataclass
class RequestUriPathDefinition(BaseModel):
    MatchCriteria: Optional[str]
    MatchStr: Optional[Sequence[str]]
    StringGroupRefs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RequestUriPathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestUriPathDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            MatchStr=json_data.get("MatchStr"),
            StringGroupRefs=json_data.get("StringGroupRefs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestUriPathDefinition = RequestUriPathDefinition


@dataclass
class ConnectionsRateLimitDefinition(BaseModel):
    ExplicitTracking: Optional[bool]
    FineGrain: Optional[bool]
    HttpCookie: Optional[str]
    HttpHeader: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    RateLimiter: Optional[Sequence["_RateLimiterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionsRateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionsRateLimitDefinition"]:
        if not json_data:
            return None
        return cls(
            ExplicitTracking=json_data.get("ExplicitTracking"),
            FineGrain=json_data.get("FineGrain"),
            HttpCookie=json_data.get("HttpCookie"),
            HttpHeader=json_data.get("HttpHeader"),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            RateLimiter=deserialize_list(json_data.get("RateLimiter"), RateLimiterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionsRateLimitDefinition = ConnectionsRateLimitDefinition


@dataclass
class ActionDefinition(BaseModel):
    StatusCode: Optional[str]
    Type: Optional[str]
    File: Optional[Sequence["_FileDefinition"]]
    Redirect: Optional[Sequence["_RedirectDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            StatusCode=json_data.get("StatusCode"),
            Type=json_data.get("Type"),
            File=deserialize_list(json_data.get("File"), FileDefinition),
            Redirect=deserialize_list(json_data.get("Redirect"), RedirectDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class FileDefinition(BaseModel):
    ContentType: Optional[str]
    FileContent: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentType=json_data.get("ContentType"),
            FileContent=json_data.get("FileContent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileDefinition = FileDefinition


@dataclass
class RedirectDefinition(BaseModel):
    KeepQuery: Optional[bool]
    Port: Optional[float]
    Protocol: Optional[str]
    StatusCode: Optional[str]
    Host: Optional[Sequence["_HostDefinition"]]
    Path: Optional[Sequence["_PathDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectDefinition"]:
        if not json_data:
            return None
        return cls(
            KeepQuery=json_data.get("KeepQuery"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            StatusCode=json_data.get("StatusCode"),
            Host=deserialize_list(json_data.get("Host"), HostDefinition),
            Path=deserialize_list(json_data.get("Path"), PathDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedirectDefinition = RedirectDefinition


@dataclass
class HostDefinition(BaseModel):
    Type: Optional[str]
    Tokens: Optional[Sequence["_TokensDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HostDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Tokens=deserialize_list(json_data.get("Tokens"), TokensDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostDefinition = HostDefinition


@dataclass
class TokensDefinition(BaseModel):
    EndIndex: Optional[float]
    StartIndex: Optional[float]
    StrValue: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TokensDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TokensDefinition"]:
        if not json_data:
            return None
        return cls(
            EndIndex=json_data.get("EndIndex"),
            StartIndex=json_data.get("StartIndex"),
            StrValue=json_data.get("StrValue"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TokensDefinition = TokensDefinition


@dataclass
class PathDefinition(BaseModel):
    Type: Optional[str]
    Tokens: Optional[Sequence["_TokensDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Tokens=deserialize_list(json_data.get("Tokens"), TokensDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathDefinition = PathDefinition


@dataclass
class RateLimiterDefinition(BaseModel):
    BurstSz: Optional[float]
    Count: Optional[float]
    Name: Optional[str]
    Period: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimiterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimiterDefinition"]:
        if not json_data:
            return None
        return cls(
            BurstSz=json_data.get("BurstSz"),
            Count=json_data.get("Count"),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimiterDefinition = RateLimiterDefinition


@dataclass
class ContentRewriteDefinition(BaseModel):
    RequestRewriteEnabled: Optional[bool]
    ResponseRewriteEnabled: Optional[bool]
    RewritableContentRef: Optional[str]
    ReqMatchReplacePair: Optional[Sequence["_ReqMatchReplacePairDefinition"]]
    RspMatchReplacePair: Optional[Sequence["_RspMatchReplacePairDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ContentRewriteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContentRewriteDefinition"]:
        if not json_data:
            return None
        return cls(
            RequestRewriteEnabled=json_data.get("RequestRewriteEnabled"),
            ResponseRewriteEnabled=json_data.get("ResponseRewriteEnabled"),
            RewritableContentRef=json_data.get("RewritableContentRef"),
            ReqMatchReplacePair=deserialize_list(json_data.get("ReqMatchReplacePair"), ReqMatchReplacePairDefinition),
            RspMatchReplacePair=deserialize_list(json_data.get("RspMatchReplacePair"), RspMatchReplacePairDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContentRewriteDefinition = ContentRewriteDefinition


@dataclass
class ReqMatchReplacePairDefinition(BaseModel):
    MatchString: Optional[str]
    ReplacementString: Optional[Sequence["_ReplacementStringDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReqMatchReplacePairDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReqMatchReplacePairDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchString=json_data.get("MatchString"),
            ReplacementString=deserialize_list(json_data.get("ReplacementString"), ReplacementStringDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReqMatchReplacePairDefinition = ReqMatchReplacePairDefinition


@dataclass
class ReplacementStringDefinition(BaseModel):
    Type: Optional[str]
    Val: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReplacementStringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplacementStringDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Val=json_data.get("Val"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplacementStringDefinition = ReplacementStringDefinition


@dataclass
class RspMatchReplacePairDefinition(BaseModel):
    MatchString: Optional[str]
    ReplacementString: Optional[Sequence["_ReplacementStringDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RspMatchReplacePairDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RspMatchReplacePairDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchString=json_data.get("MatchString"),
            ReplacementString=deserialize_list(json_data.get("ReplacementString"), ReplacementStringDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RspMatchReplacePairDefinition = RspMatchReplacePairDefinition


@dataclass
class DnsInfoDefinition(BaseModel):
    Algorithm: Optional[str]
    Fqdn: Optional[str]
    NumRecordsInResponse: Optional[float]
    Ttl: Optional[float]
    Type: Optional[str]
    Cname: Optional[Sequence["_CnameDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            Fqdn=json_data.get("Fqdn"),
            NumRecordsInResponse=json_data.get("NumRecordsInResponse"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
            Cname=deserialize_list(json_data.get("Cname"), CnameDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsInfoDefinition = DnsInfoDefinition


@dataclass
class CnameDefinition(BaseModel):
    Cname: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CnameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CnameDefinition"]:
        if not json_data:
            return None
        return cls(
            Cname=json_data.get("Cname"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CnameDefinition = CnameDefinition


@dataclass
class DnsPoliciesDefinition(BaseModel):
    DnsPolicyRef: Optional[str]
    Index: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DnsPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsPolicyRef=json_data.get("DnsPolicyRef"),
            Index=json_data.get("Index"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsPoliciesDefinition = DnsPoliciesDefinition


@dataclass
class HttpPoliciesDefinition(BaseModel):
    HttpPolicySetRef: Optional[str]
    Index: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HttpPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            HttpPolicySetRef=json_data.get("HttpPolicySetRef"),
            Index=json_data.get("Index"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpPoliciesDefinition = HttpPoliciesDefinition


@dataclass
class JwtConfigDefinition(BaseModel):
    Audience: Optional[str]
    JwtLocation: Optional[str]
    JwtName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JwtConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JwtConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Audience=json_data.get("Audience"),
            JwtLocation=json_data.get("JwtLocation"),
            JwtName=json_data.get("JwtName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JwtConfigDefinition = JwtConfigDefinition


@dataclass
class L4PoliciesDefinition(BaseModel):
    Index: Optional[float]
    L4PolicySetRef: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_L4PoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_L4PoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            L4PolicySetRef=json_data.get("L4PolicySetRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_L4PoliciesDefinition = L4PoliciesDefinition


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


@dataclass
class PerformanceLimitsDefinition(BaseModel):
    MaxConcurrentConnections: Optional[float]
    MaxThroughput: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PerformanceLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PerformanceLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxConcurrentConnections=json_data.get("MaxConcurrentConnections"),
            MaxThroughput=json_data.get("MaxThroughput"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PerformanceLimitsDefinition = PerformanceLimitsDefinition


@dataclass
class RequestsRateLimitDefinition(BaseModel):
    ExplicitTracking: Optional[bool]
    FineGrain: Optional[bool]
    HttpCookie: Optional[str]
    HttpHeader: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    RateLimiter: Optional[Sequence["_RateLimiterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RequestsRateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestsRateLimitDefinition"]:
        if not json_data:
            return None
        return cls(
            ExplicitTracking=json_data.get("ExplicitTracking"),
            FineGrain=json_data.get("FineGrain"),
            HttpCookie=json_data.get("HttpCookie"),
            HttpHeader=json_data.get("HttpHeader"),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            RateLimiter=deserialize_list(json_data.get("RateLimiter"), RateLimiterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestsRateLimitDefinition = RequestsRateLimitDefinition


@dataclass
class SamlSpConfigDefinition(BaseModel):
    CookieName: Optional[str]
    CookieTimeout: Optional[float]
    EntityId: Optional[str]
    SigningSslKeyAndCertificateRef: Optional[str]
    SingleSignonUrl: Optional[str]
    UseIdpSessionTimeout: Optional[bool]
    Key: Optional[Sequence["_KeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SamlSpConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SamlSpConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CookieName=json_data.get("CookieName"),
            CookieTimeout=json_data.get("CookieTimeout"),
            EntityId=json_data.get("EntityId"),
            SigningSslKeyAndCertificateRef=json_data.get("SigningSslKeyAndCertificateRef"),
            SingleSignonUrl=json_data.get("SingleSignonUrl"),
            UseIdpSessionTimeout=json_data.get("UseIdpSessionTimeout"),
            Key=deserialize_list(json_data.get("Key"), KeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SamlSpConfigDefinition = SamlSpConfigDefinition


@dataclass
class KeyDefinition(BaseModel):
    AesKey: Optional[str]
    HmacKey: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyDefinition"]:
        if not json_data:
            return None
        return cls(
            AesKey=json_data.get("AesKey"),
            HmacKey=json_data.get("HmacKey"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyDefinition = KeyDefinition


@dataclass
class ServicePoolSelectDefinition(BaseModel):
    ServicePoolGroupRef: Optional[str]
    ServicePoolRef: Optional[str]
    ServicePort: Optional[float]
    ServicePortRangeEnd: Optional[float]
    ServiceProtocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServicePoolSelectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicePoolSelectDefinition"]:
        if not json_data:
            return None
        return cls(
            ServicePoolGroupRef=json_data.get("ServicePoolGroupRef"),
            ServicePoolRef=json_data.get("ServicePoolRef"),
            ServicePort=json_data.get("ServicePort"),
            ServicePortRangeEnd=json_data.get("ServicePortRangeEnd"),
            ServiceProtocol=json_data.get("ServiceProtocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicePoolSelectDefinition = ServicePoolSelectDefinition


@dataclass
class ServicesDefinition(BaseModel):
    EnableHttp2: Optional[bool]
    EnableSsl: Optional[bool]
    OverrideApplicationProfileRef: Optional[str]
    OverrideNetworkProfileRef: Optional[str]
    Port: Optional[float]
    PortRangeEnd: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicesDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableHttp2=json_data.get("EnableHttp2"),
            EnableSsl=json_data.get("EnableSsl"),
            OverrideApplicationProfileRef=json_data.get("OverrideApplicationProfileRef"),
            OverrideNetworkProfileRef=json_data.get("OverrideNetworkProfileRef"),
            Port=json_data.get("Port"),
            PortRangeEnd=json_data.get("PortRangeEnd"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicesDefinition = ServicesDefinition


@dataclass
class SidebandProfileDefinition(BaseModel):
    SidebandMaxRequestBodySize: Optional[float]
    Ip: Optional[Sequence["_IpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SidebandProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SidebandProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            SidebandMaxRequestBodySize=json_data.get("SidebandMaxRequestBodySize"),
            Ip=deserialize_list(json_data.get("Ip"), IpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SidebandProfileDefinition = SidebandProfileDefinition


@dataclass
class IpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpDefinition = IpDefinition


@dataclass
class SnatIpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnatIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnatIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnatIpDefinition = SnatIpDefinition


@dataclass
class SslProfileSelectorsDefinition(BaseModel):
    SslProfileRef: Optional[str]
    ClientIpList: Optional[Sequence["_ClientIpListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SslProfileSelectorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslProfileSelectorsDefinition"]:
        if not json_data:
            return None
        return cls(
            SslProfileRef=json_data.get("SslProfileRef"),
            ClientIpList=deserialize_list(json_data.get("ClientIpList"), ClientIpListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslProfileSelectorsDefinition = SslProfileSelectorsDefinition


@dataclass
class ClientIpListDefinition(BaseModel):
    GroupRefs: Optional[Sequence[str]]
    MatchCriteria: Optional[str]
    Addrs: Optional[Sequence["_AddrsDefinition"]]
    Prefixes: Optional[Sequence["_PrefixesDefinition"]]
    Ranges: Optional[Sequence["_RangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientIpListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientIpListDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupRefs=json_data.get("GroupRefs"),
            MatchCriteria=json_data.get("MatchCriteria"),
            Addrs=deserialize_list(json_data.get("Addrs"), AddrsDefinition),
            Prefixes=deserialize_list(json_data.get("Prefixes"), PrefixesDefinition),
            Ranges=deserialize_list(json_data.get("Ranges"), RangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientIpListDefinition = ClientIpListDefinition


@dataclass
class StaticDnsRecordsDefinition(BaseModel):
    Algorithm: Optional[str]
    Delegated: Optional[bool]
    Description: Optional[str]
    Fqdn: Optional[Sequence[str]]
    Metadata: Optional[str]
    NumRecordsInResponse: Optional[float]
    Ttl: Optional[float]
    Type: Optional[str]
    WildcardMatch: Optional[bool]
    Cname: Optional[Sequence["_CnameDefinition"]]
    Ip6Address: Optional[Sequence["_Ip6AddressDefinition"]]
    IpAddress: Optional[Sequence["_IpAddressDefinition"]]
    MxRecords: Optional[Sequence["_MxRecordsDefinition"]]
    Ns: Optional[Sequence["_NsDefinition"]]
    ServiceLocator: Optional[Sequence["_ServiceLocatorDefinition"]]
    TxtRecords: Optional[Sequence["_TxtRecordsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StaticDnsRecordsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticDnsRecordsDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            Delegated=json_data.get("Delegated"),
            Description=json_data.get("Description"),
            Fqdn=json_data.get("Fqdn"),
            Metadata=json_data.get("Metadata"),
            NumRecordsInResponse=json_data.get("NumRecordsInResponse"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
            WildcardMatch=json_data.get("WildcardMatch"),
            Cname=deserialize_list(json_data.get("Cname"), CnameDefinition),
            Ip6Address=deserialize_list(json_data.get("Ip6Address"), Ip6AddressDefinition),
            IpAddress=deserialize_list(json_data.get("IpAddress"), IpAddressDefinition),
            MxRecords=deserialize_list(json_data.get("MxRecords"), MxRecordsDefinition),
            Ns=deserialize_list(json_data.get("Ns"), NsDefinition),
            ServiceLocator=deserialize_list(json_data.get("ServiceLocator"), ServiceLocatorDefinition),
            TxtRecords=deserialize_list(json_data.get("TxtRecords"), TxtRecordsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticDnsRecordsDefinition = StaticDnsRecordsDefinition


@dataclass
class Ip6AddressDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ip6AddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ip6AddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ip6AddressDefinition = Ip6AddressDefinition


@dataclass
class IpAddressDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddressDefinition = IpAddressDefinition


@dataclass
class MxRecordsDefinition(BaseModel):
    Host: Optional[str]
    Priority: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MxRecordsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MxRecordsDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MxRecordsDefinition = MxRecordsDefinition


@dataclass
class NsDefinition(BaseModel):
    Nsname: Optional[str]
    Ip6Address: Optional[Sequence["_Ip6AddressDefinition"]]
    IpAddress: Optional[Sequence["_IpAddressDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NsDefinition"]:
        if not json_data:
            return None
        return cls(
            Nsname=json_data.get("Nsname"),
            Ip6Address=deserialize_list(json_data.get("Ip6Address"), Ip6AddressDefinition),
            IpAddress=deserialize_list(json_data.get("IpAddress"), IpAddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NsDefinition = NsDefinition


@dataclass
class ServiceLocatorDefinition(BaseModel):
    Port: Optional[float]
    Priority: Optional[float]
    Target: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceLocatorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceLocatorDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Priority=json_data.get("Priority"),
            Target=json_data.get("Target"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceLocatorDefinition = ServiceLocatorDefinition


@dataclass
class TxtRecordsDefinition(BaseModel):
    TextStr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TxtRecordsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TxtRecordsDefinition"]:
        if not json_data:
            return None
        return cls(
            TextStr=json_data.get("TextStr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TxtRecordsDefinition = TxtRecordsDefinition


@dataclass
class TopologyPoliciesDefinition(BaseModel):
    DnsPolicyRef: Optional[str]
    Index: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TopologyPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopologyPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsPolicyRef=json_data.get("DnsPolicyRef"),
            Index=json_data.get("Index"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopologyPoliciesDefinition = TopologyPoliciesDefinition


@dataclass
class VhMatchesDefinition(BaseModel):
    Host: Optional[str]
    Path: Optional[Sequence["_PathDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VhMatchesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VhMatchesDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Path=deserialize_list(json_data.get("Path"), PathDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VhMatchesDefinition = VhMatchesDefinition


@dataclass
class VipDefinition(BaseModel):
    AutoAllocateFloatingIp: Optional[bool]
    AutoAllocateIp: Optional[bool]
    AutoAllocateIpType: Optional[str]
    AvailabilityZone: Optional[str]
    AviAllocatedFip: Optional[bool]
    AviAllocatedVip: Optional[bool]
    Enabled: Optional[bool]
    FloatingSubnet6Uuid: Optional[str]
    FloatingSubnetUuid: Optional[str]
    NetworkRef: Optional[str]
    PortUuid: Optional[str]
    PrefixLength: Optional[float]
    Subnet6Uuid: Optional[str]
    SubnetUuid: Optional[str]
    VipId: Optional[str]
    DiscoveredNetworks: Optional[Sequence["_DiscoveredNetworksDefinition"]]
    FloatingIp: Optional[Sequence["_FloatingIpDefinition"]]
    FloatingIp6: Optional[Sequence["_FloatingIp6Definition"]]
    Ip6Address: Optional[Sequence["_Ip6AddressDefinition"]]
    IpAddress: Optional[Sequence["_IpAddressDefinition"]]
    IpamNetworkSubnet: Optional[Sequence["_IpamNetworkSubnetDefinition"]]
    PlacementNetworks: Optional[Sequence["_PlacementNetworksDefinition"]]
    Subnet: Optional[Sequence["_SubnetDefinition"]]
    Subnet6: Optional[Sequence["_Subnet6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VipDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VipDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoAllocateFloatingIp=json_data.get("AutoAllocateFloatingIp"),
            AutoAllocateIp=json_data.get("AutoAllocateIp"),
            AutoAllocateIpType=json_data.get("AutoAllocateIpType"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            AviAllocatedFip=json_data.get("AviAllocatedFip"),
            AviAllocatedVip=json_data.get("AviAllocatedVip"),
            Enabled=json_data.get("Enabled"),
            FloatingSubnet6Uuid=json_data.get("FloatingSubnet6Uuid"),
            FloatingSubnetUuid=json_data.get("FloatingSubnetUuid"),
            NetworkRef=json_data.get("NetworkRef"),
            PortUuid=json_data.get("PortUuid"),
            PrefixLength=json_data.get("PrefixLength"),
            Subnet6Uuid=json_data.get("Subnet6Uuid"),
            SubnetUuid=json_data.get("SubnetUuid"),
            VipId=json_data.get("VipId"),
            DiscoveredNetworks=deserialize_list(json_data.get("DiscoveredNetworks"), DiscoveredNetworksDefinition),
            FloatingIp=deserialize_list(json_data.get("FloatingIp"), FloatingIpDefinition),
            FloatingIp6=deserialize_list(json_data.get("FloatingIp6"), FloatingIp6Definition),
            Ip6Address=deserialize_list(json_data.get("Ip6Address"), Ip6AddressDefinition),
            IpAddress=deserialize_list(json_data.get("IpAddress"), IpAddressDefinition),
            IpamNetworkSubnet=deserialize_list(json_data.get("IpamNetworkSubnet"), IpamNetworkSubnetDefinition),
            PlacementNetworks=deserialize_list(json_data.get("PlacementNetworks"), PlacementNetworksDefinition),
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
            Subnet6=deserialize_list(json_data.get("Subnet6"), Subnet6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VipDefinition = VipDefinition


@dataclass
class DiscoveredNetworksDefinition(BaseModel):
    NetworkRef: Optional[str]
    Subnet: Optional[Sequence["_SubnetDefinition"]]
    Subnet6: Optional[Sequence["_Subnet6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DiscoveredNetworksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiscoveredNetworksDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkRef=json_data.get("NetworkRef"),
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
            Subnet6=deserialize_list(json_data.get("Subnet6"), Subnet6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiscoveredNetworksDefinition = DiscoveredNetworksDefinition


@dataclass
class SubnetDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetDefinition = SubnetDefinition


@dataclass
class Subnet6Definition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Subnet6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subnet6Definition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subnet6Definition = Subnet6Definition


@dataclass
class FloatingIpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FloatingIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FloatingIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FloatingIpDefinition = FloatingIpDefinition


@dataclass
class FloatingIp6Definition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FloatingIp6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FloatingIp6Definition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FloatingIp6Definition = FloatingIp6Definition


@dataclass
class IpamNetworkSubnetDefinition(BaseModel):
    NetworkRef: Optional[str]
    Subnet6Uuid: Optional[str]
    SubnetUuid: Optional[str]
    Subnet: Optional[Sequence["_SubnetDefinition"]]
    Subnet6: Optional[Sequence["_Subnet6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpamNetworkSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpamNetworkSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkRef=json_data.get("NetworkRef"),
            Subnet6Uuid=json_data.get("Subnet6Uuid"),
            SubnetUuid=json_data.get("SubnetUuid"),
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
            Subnet6=deserialize_list(json_data.get("Subnet6"), Subnet6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpamNetworkSubnetDefinition = IpamNetworkSubnetDefinition


@dataclass
class PlacementNetworksDefinition(BaseModel):
    NetworkRef: Optional[str]
    Subnet: Optional[Sequence["_SubnetDefinition"]]
    Subnet6: Optional[Sequence["_Subnet6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementNetworksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementNetworksDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkRef=json_data.get("NetworkRef"),
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
            Subnet6=deserialize_list(json_data.get("Subnet6"), Subnet6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementNetworksDefinition = PlacementNetworksDefinition


@dataclass
class VsDatascriptsDefinition(BaseModel):
    Index: Optional[float]
    VsDatascriptSetRef: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VsDatascriptsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VsDatascriptsDefinition"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            VsDatascriptSetRef=json_data.get("VsDatascriptSetRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VsDatascriptsDefinition = VsDatascriptsDefinition


