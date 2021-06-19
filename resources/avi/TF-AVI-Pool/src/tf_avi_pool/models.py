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
    AnalyticsProfileRef: Optional[str]
    ApicEpgName: Optional[str]
    ApplicationPersistenceProfileRef: Optional[str]
    AutoscaleLaunchConfigRef: Optional[str]
    AutoscaleNetworks: Optional[Sequence[str]]
    AutoscalePolicyRef: Optional[str]
    CapacityEstimation: Optional[bool]
    CapacityEstimationTtfbThresh: Optional[float]
    CloudConfigCksum: Optional[str]
    CloudRef: Optional[str]
    ConnectionRampDuration: Optional[float]
    CreatedBy: Optional[str]
    DefaultServerPort: Optional[float]
    DeleteServerOnDnsRefresh: Optional[bool]
    Description: Optional[str]
    DomainName: Optional[Sequence[str]]
    EastWest: Optional[bool]
    EnableHttp2: Optional[bool]
    Enabled: Optional[bool]
    ExternalAutoscaleGroups: Optional[Sequence[str]]
    FewestTasksFeedbackDelay: Optional[float]
    GracefulDisableTimeout: Optional[float]
    HealthMonitorRefs: Optional[Sequence[str]]
    HostCheckEnabled: Optional[bool]
    Id: Optional[str]
    IgnoreServerPort: Optional[bool]
    IgnoreServers: Optional[bool]
    InlineHealthMonitor: Optional[bool]
    IpaddrgroupRef: Optional[str]
    LbAlgorithm: Optional[str]
    LbAlgorithmConsistentHashHdr: Optional[str]
    LbAlgorithmCoreNonaffinity: Optional[float]
    LbAlgorithmHash: Optional[str]
    LookupServerByName: Optional[bool]
    MaxConcurrentConnectionsPerServer: Optional[float]
    MinHealthMonitorsUp: Optional[float]
    MinServersUp: Optional[float]
    Name: Optional[str]
    NsxSecuritygroup: Optional[Sequence[str]]
    PkiProfileRef: Optional[str]
    RequestQueueDepth: Optional[float]
    RequestQueueEnabled: Optional[bool]
    ResolvePoolByDns: Optional[bool]
    RewriteHostHeaderToServerName: Optional[bool]
    RewriteHostHeaderToSni: Optional[bool]
    RoutingPool: Optional[bool]
    ServerName: Optional[str]
    ServerTimeout: Optional[float]
    ServiceMetadata: Optional[str]
    SniEnabled: Optional[bool]
    SslKeyAndCertificateRef: Optional[str]
    SslProfileRef: Optional[str]
    TenantRef: Optional[str]
    Tier1Lr: Optional[str]
    UseServicePort: Optional[bool]
    Uuid: Optional[str]
    VrfRef: Optional[str]
    AnalyticsPolicy: Optional[Sequence["_AnalyticsPolicyDefinition"]]
    ConnPoolProperties: Optional[Sequence["_ConnPoolPropertiesDefinition"]]
    FailAction: Optional[Sequence["_FailActionDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    MaxConnRatePerServer: Optional[Sequence["_MaxConnRatePerServerDefinition"]]
    Networks: Optional[Sequence["_NetworksDefinition"]]
    PlacementNetworks: Optional[Sequence["_PlacementNetworksDefinition"]]
    ServerReselect: Optional[Sequence["_ServerReselectDefinition"]]
    Servers: Optional[Sequence["_ServersDefinition"]]

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
            AnalyticsProfileRef=json_data.get("AnalyticsProfileRef"),
            ApicEpgName=json_data.get("ApicEpgName"),
            ApplicationPersistenceProfileRef=json_data.get("ApplicationPersistenceProfileRef"),
            AutoscaleLaunchConfigRef=json_data.get("AutoscaleLaunchConfigRef"),
            AutoscaleNetworks=json_data.get("AutoscaleNetworks"),
            AutoscalePolicyRef=json_data.get("AutoscalePolicyRef"),
            CapacityEstimation=json_data.get("CapacityEstimation"),
            CapacityEstimationTtfbThresh=json_data.get("CapacityEstimationTtfbThresh"),
            CloudConfigCksum=json_data.get("CloudConfigCksum"),
            CloudRef=json_data.get("CloudRef"),
            ConnectionRampDuration=json_data.get("ConnectionRampDuration"),
            CreatedBy=json_data.get("CreatedBy"),
            DefaultServerPort=json_data.get("DefaultServerPort"),
            DeleteServerOnDnsRefresh=json_data.get("DeleteServerOnDnsRefresh"),
            Description=json_data.get("Description"),
            DomainName=json_data.get("DomainName"),
            EastWest=json_data.get("EastWest"),
            EnableHttp2=json_data.get("EnableHttp2"),
            Enabled=json_data.get("Enabled"),
            ExternalAutoscaleGroups=json_data.get("ExternalAutoscaleGroups"),
            FewestTasksFeedbackDelay=json_data.get("FewestTasksFeedbackDelay"),
            GracefulDisableTimeout=json_data.get("GracefulDisableTimeout"),
            HealthMonitorRefs=json_data.get("HealthMonitorRefs"),
            HostCheckEnabled=json_data.get("HostCheckEnabled"),
            Id=json_data.get("Id"),
            IgnoreServerPort=json_data.get("IgnoreServerPort"),
            IgnoreServers=json_data.get("IgnoreServers"),
            InlineHealthMonitor=json_data.get("InlineHealthMonitor"),
            IpaddrgroupRef=json_data.get("IpaddrgroupRef"),
            LbAlgorithm=json_data.get("LbAlgorithm"),
            LbAlgorithmConsistentHashHdr=json_data.get("LbAlgorithmConsistentHashHdr"),
            LbAlgorithmCoreNonaffinity=json_data.get("LbAlgorithmCoreNonaffinity"),
            LbAlgorithmHash=json_data.get("LbAlgorithmHash"),
            LookupServerByName=json_data.get("LookupServerByName"),
            MaxConcurrentConnectionsPerServer=json_data.get("MaxConcurrentConnectionsPerServer"),
            MinHealthMonitorsUp=json_data.get("MinHealthMonitorsUp"),
            MinServersUp=json_data.get("MinServersUp"),
            Name=json_data.get("Name"),
            NsxSecuritygroup=json_data.get("NsxSecuritygroup"),
            PkiProfileRef=json_data.get("PkiProfileRef"),
            RequestQueueDepth=json_data.get("RequestQueueDepth"),
            RequestQueueEnabled=json_data.get("RequestQueueEnabled"),
            ResolvePoolByDns=json_data.get("ResolvePoolByDns"),
            RewriteHostHeaderToServerName=json_data.get("RewriteHostHeaderToServerName"),
            RewriteHostHeaderToSni=json_data.get("RewriteHostHeaderToSni"),
            RoutingPool=json_data.get("RoutingPool"),
            ServerName=json_data.get("ServerName"),
            ServerTimeout=json_data.get("ServerTimeout"),
            ServiceMetadata=json_data.get("ServiceMetadata"),
            SniEnabled=json_data.get("SniEnabled"),
            SslKeyAndCertificateRef=json_data.get("SslKeyAndCertificateRef"),
            SslProfileRef=json_data.get("SslProfileRef"),
            TenantRef=json_data.get("TenantRef"),
            Tier1Lr=json_data.get("Tier1Lr"),
            UseServicePort=json_data.get("UseServicePort"),
            Uuid=json_data.get("Uuid"),
            VrfRef=json_data.get("VrfRef"),
            AnalyticsPolicy=deserialize_list(json_data.get("AnalyticsPolicy"), AnalyticsPolicyDefinition),
            ConnPoolProperties=deserialize_list(json_data.get("ConnPoolProperties"), ConnPoolPropertiesDefinition),
            FailAction=deserialize_list(json_data.get("FailAction"), FailActionDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            MaxConnRatePerServer=deserialize_list(json_data.get("MaxConnRatePerServer"), MaxConnRatePerServerDefinition),
            Networks=deserialize_list(json_data.get("Networks"), NetworksDefinition),
            PlacementNetworks=deserialize_list(json_data.get("PlacementNetworks"), PlacementNetworksDefinition),
            ServerReselect=deserialize_list(json_data.get("ServerReselect"), ServerReselectDefinition),
            Servers=deserialize_list(json_data.get("Servers"), ServersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnalyticsPolicyDefinition(BaseModel):
    EnableRealtimeMetrics: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AnalyticsPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalyticsPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableRealtimeMetrics=json_data.get("EnableRealtimeMetrics"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalyticsPolicyDefinition = AnalyticsPolicyDefinition


@dataclass
class ConnPoolPropertiesDefinition(BaseModel):
    UpstreamConnpoolConnIdleTmo: Optional[float]
    UpstreamConnpoolConnLifeTmo: Optional[float]
    UpstreamConnpoolConnMaxReuse: Optional[float]
    UpstreamConnpoolServerMaxCache: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConnPoolPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnPoolPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            UpstreamConnpoolConnIdleTmo=json_data.get("UpstreamConnpoolConnIdleTmo"),
            UpstreamConnpoolConnLifeTmo=json_data.get("UpstreamConnpoolConnLifeTmo"),
            UpstreamConnpoolConnMaxReuse=json_data.get("UpstreamConnpoolConnMaxReuse"),
            UpstreamConnpoolServerMaxCache=json_data.get("UpstreamConnpoolServerMaxCache"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnPoolPropertiesDefinition = ConnPoolPropertiesDefinition


@dataclass
class FailActionDefinition(BaseModel):
    Type: Optional[str]
    LocalRsp: Optional[Sequence["_LocalRspDefinition"]]
    Redirect: Optional[Sequence["_RedirectDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FailActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            LocalRsp=deserialize_list(json_data.get("LocalRsp"), LocalRspDefinition),
            Redirect=deserialize_list(json_data.get("Redirect"), RedirectDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailActionDefinition = FailActionDefinition


@dataclass
class LocalRspDefinition(BaseModel):
    StatusCode: Optional[str]
    File: Optional[Sequence["_FileDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LocalRspDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalRspDefinition"]:
        if not json_data:
            return None
        return cls(
            StatusCode=json_data.get("StatusCode"),
            File=deserialize_list(json_data.get("File"), FileDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalRspDefinition = LocalRspDefinition


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
class MaxConnRatePerServerDefinition(BaseModel):
    ExplicitTracking: Optional[bool]
    FineGrain: Optional[bool]
    HttpCookie: Optional[str]
    HttpHeader: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    RateLimiter: Optional[Sequence["_RateLimiterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MaxConnRatePerServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaxConnRatePerServerDefinition"]:
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
_MaxConnRatePerServerDefinition = MaxConnRatePerServerDefinition


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
class NetworksDefinition(BaseModel):
    NetworkRef: Optional[str]
    ServerFilter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworksDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkRef=json_data.get("NetworkRef"),
            ServerFilter=json_data.get("ServerFilter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworksDefinition = NetworksDefinition


@dataclass
class PlacementNetworksDefinition(BaseModel):
    NetworkRef: Optional[str]
    Subnet: Optional[Sequence["_SubnetDefinition"]]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementNetworksDefinition = PlacementNetworksDefinition


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
class ServerReselectDefinition(BaseModel):
    Enabled: Optional[bool]
    NumRetries: Optional[float]
    RetryNonidempotent: Optional[bool]
    RetryTimeout: Optional[float]
    SvrRespCode: Optional[Sequence["_SvrRespCodeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServerReselectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerReselectDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            NumRetries=json_data.get("NumRetries"),
            RetryNonidempotent=json_data.get("RetryNonidempotent"),
            RetryTimeout=json_data.get("RetryTimeout"),
            SvrRespCode=deserialize_list(json_data.get("SvrRespCode"), SvrRespCodeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerReselectDefinition = ServerReselectDefinition


@dataclass
class SvrRespCodeDefinition(BaseModel):
    Codes: Optional[Sequence[float]]
    RespCodeBlock: Optional[Sequence[str]]
    Ranges: Optional[Sequence["_RangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SvrRespCodeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SvrRespCodeDefinition"]:
        if not json_data:
            return None
        return cls(
            Codes=json_data.get("Codes"),
            RespCodeBlock=json_data.get("RespCodeBlock"),
            Ranges=deserialize_list(json_data.get("Ranges"), RangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SvrRespCodeDefinition = SvrRespCodeDefinition


@dataclass
class RangesDefinition(BaseModel):
    Begin: Optional[float]
    End: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RangesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangesDefinition"]:
        if not json_data:
            return None
        return cls(
            Begin=json_data.get("Begin"),
            End=json_data.get("End"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangesDefinition = RangesDefinition


@dataclass
class ServersDefinition(BaseModel):
    AutoscalingGroupName: Optional[str]
    AvailabilityZone: Optional[str]
    Description: Optional[str]
    Enabled: Optional[bool]
    ExternalOrchestrationId: Optional[str]
    ExternalUuid: Optional[str]
    Hostname: Optional[str]
    MacAddress: Optional[str]
    NwRef: Optional[str]
    Port: Optional[float]
    PrstHdrVal: Optional[str]
    Ratio: Optional[float]
    ResolveServerByDns: Optional[bool]
    RewriteHostHeader: Optional[bool]
    ServerNode: Optional[str]
    Static: Optional[bool]
    VerifyNetwork: Optional[bool]
    VmRef: Optional[str]
    DiscoveredNetworks: Optional[Sequence["_DiscoveredNetworksDefinition"]]
    Ip: Optional[Sequence["_IpDefinition"]]
    Location: Optional[Sequence["_LocationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServersDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoscalingGroupName=json_data.get("AutoscalingGroupName"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            ExternalOrchestrationId=json_data.get("ExternalOrchestrationId"),
            ExternalUuid=json_data.get("ExternalUuid"),
            Hostname=json_data.get("Hostname"),
            MacAddress=json_data.get("MacAddress"),
            NwRef=json_data.get("NwRef"),
            Port=json_data.get("Port"),
            PrstHdrVal=json_data.get("PrstHdrVal"),
            Ratio=json_data.get("Ratio"),
            ResolveServerByDns=json_data.get("ResolveServerByDns"),
            RewriteHostHeader=json_data.get("RewriteHostHeader"),
            ServerNode=json_data.get("ServerNode"),
            Static=json_data.get("Static"),
            VerifyNetwork=json_data.get("VerifyNetwork"),
            VmRef=json_data.get("VmRef"),
            DiscoveredNetworks=deserialize_list(json_data.get("DiscoveredNetworks"), DiscoveredNetworksDefinition),
            Ip=deserialize_list(json_data.get("Ip"), IpDefinition),
            Location=deserialize_list(json_data.get("Location"), LocationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServersDefinition = ServersDefinition


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
class LocationDefinition(BaseModel):
    Latitude: Optional[float]
    Longitude: Optional[float]
    Name: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocationDefinition"]:
        if not json_data:
            return None
        return cls(
            Latitude=json_data.get("Latitude"),
            Longitude=json_data.get("Longitude"),
            Name=json_data.get("Name"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocationDefinition = LocationDefinition


