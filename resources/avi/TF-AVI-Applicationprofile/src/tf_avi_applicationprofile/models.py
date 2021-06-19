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
    CloudConfigCksum: Optional[str]
    CreatedBy: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PreserveClientIp: Optional[bool]
    PreserveClientPort: Optional[bool]
    PreserveDestIpPort: Optional[bool]
    TenantRef: Optional[str]
    Type: Optional[str]
    Uuid: Optional[str]
    DnsServiceProfile: Optional[Sequence["_DnsServiceProfileDefinition"]]
    DosRlProfile: Optional[Sequence["_DosRlProfileDefinition"]]
    HttpProfile: Optional[Sequence["_HttpProfileDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    SipServiceProfile: Optional[Sequence["_SipServiceProfileDefinition"]]
    TcpAppProfile: Optional[Sequence["_TcpAppProfileDefinition"]]

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
            CloudConfigCksum=json_data.get("CloudConfigCksum"),
            CreatedBy=json_data.get("CreatedBy"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PreserveClientIp=json_data.get("PreserveClientIp"),
            PreserveClientPort=json_data.get("PreserveClientPort"),
            PreserveDestIpPort=json_data.get("PreserveDestIpPort"),
            TenantRef=json_data.get("TenantRef"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
            DnsServiceProfile=deserialize_list(json_data.get("DnsServiceProfile"), DnsServiceProfileDefinition),
            DosRlProfile=deserialize_list(json_data.get("DosRlProfile"), DosRlProfileDefinition),
            HttpProfile=deserialize_list(json_data.get("HttpProfile"), HttpProfileDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            SipServiceProfile=deserialize_list(json_data.get("SipServiceProfile"), SipServiceProfileDefinition),
            TcpAppProfile=deserialize_list(json_data.get("TcpAppProfile"), TcpAppProfileDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DnsServiceProfileDefinition(BaseModel):
    AaaaEmptyResponse: Optional[bool]
    AdminEmail: Optional[str]
    DnsOverTcpEnabled: Optional[bool]
    DomainNames: Optional[Sequence[str]]
    EcsStrippingEnabled: Optional[bool]
    Edns: Optional[bool]
    EdnsClientSubnetPrefixLen: Optional[float]
    ErrorResponse: Optional[str]
    NameServer: Optional[str]
    NegativeCachingTtl: Optional[float]
    NumDnsIp: Optional[float]
    Ttl: Optional[float]
    DnsZones: Optional[Sequence["_DnsZonesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsServiceProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsServiceProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            AaaaEmptyResponse=json_data.get("AaaaEmptyResponse"),
            AdminEmail=json_data.get("AdminEmail"),
            DnsOverTcpEnabled=json_data.get("DnsOverTcpEnabled"),
            DomainNames=json_data.get("DomainNames"),
            EcsStrippingEnabled=json_data.get("EcsStrippingEnabled"),
            Edns=json_data.get("Edns"),
            EdnsClientSubnetPrefixLen=json_data.get("EdnsClientSubnetPrefixLen"),
            ErrorResponse=json_data.get("ErrorResponse"),
            NameServer=json_data.get("NameServer"),
            NegativeCachingTtl=json_data.get("NegativeCachingTtl"),
            NumDnsIp=json_data.get("NumDnsIp"),
            Ttl=json_data.get("Ttl"),
            DnsZones=deserialize_list(json_data.get("DnsZones"), DnsZonesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsServiceProfileDefinition = DnsServiceProfileDefinition


@dataclass
class DnsZonesDefinition(BaseModel):
    AdminEmail: Optional[str]
    DomainName: Optional[str]
    NameServer: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsZonesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsZonesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminEmail=json_data.get("AdminEmail"),
            DomainName=json_data.get("DomainName"),
            NameServer=json_data.get("NameServer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsZonesDefinition = DnsZonesDefinition


@dataclass
class DosRlProfileDefinition(BaseModel):
    DosProfile: Optional[Sequence["_DosProfileDefinition"]]
    RlProfile: Optional[Sequence["_RlProfileDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DosRlProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DosRlProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            DosProfile=deserialize_list(json_data.get("DosProfile"), DosProfileDefinition),
            RlProfile=deserialize_list(json_data.get("RlProfile"), RlProfileDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DosRlProfileDefinition = DosRlProfileDefinition


@dataclass
class DosProfileDefinition(BaseModel):
    ThreshPeriod: Optional[float]
    ThreshInfo: Optional[Sequence["_ThreshInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DosProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DosProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            ThreshPeriod=json_data.get("ThreshPeriod"),
            ThreshInfo=deserialize_list(json_data.get("ThreshInfo"), ThreshInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DosProfileDefinition = DosProfileDefinition


@dataclass
class ThreshInfoDefinition(BaseModel):
    Attack: Optional[str]
    MaxValue: Optional[float]
    MinValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ThreshInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThreshInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Attack=json_data.get("Attack"),
            MaxValue=json_data.get("MaxValue"),
            MinValue=json_data.get("MinValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThreshInfoDefinition = ThreshInfoDefinition


@dataclass
class RlProfileDefinition(BaseModel):
    ClientIpConnectionsRateLimit: Optional[Sequence["_ClientIpConnectionsRateLimitDefinition"]]
    ClientIpFailedRequestsRateLimit: Optional[Sequence["_ClientIpFailedRequestsRateLimitDefinition"]]
    ClientIpRequestsRateLimit: Optional[Sequence["_ClientIpRequestsRateLimitDefinition"]]
    ClientIpScannersRequestsRateLimit: Optional[Sequence["_ClientIpScannersRequestsRateLimitDefinition"]]
    ClientIpToUriFailedRequestsRateLimit: Optional[Sequence["_ClientIpToUriFailedRequestsRateLimitDefinition"]]
    ClientIpToUriRequestsRateLimit: Optional[Sequence["_ClientIpToUriRequestsRateLimitDefinition"]]
    CustomRequestsRateLimit: Optional[Sequence["_CustomRequestsRateLimitDefinition"]]
    HttpHeaderRateLimits: Optional[Sequence["_HttpHeaderRateLimitsDefinition"]]
    UriFailedRequestsRateLimit: Optional[Sequence["_UriFailedRequestsRateLimitDefinition"]]
    UriRequestsRateLimit: Optional[Sequence["_UriRequestsRateLimitDefinition"]]
    UriScannersRequestsRateLimit: Optional[Sequence["_UriScannersRequestsRateLimitDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RlProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RlProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientIpConnectionsRateLimit=deserialize_list(json_data.get("ClientIpConnectionsRateLimit"), ClientIpConnectionsRateLimitDefinition),
            ClientIpFailedRequestsRateLimit=deserialize_list(json_data.get("ClientIpFailedRequestsRateLimit"), ClientIpFailedRequestsRateLimitDefinition),
            ClientIpRequestsRateLimit=deserialize_list(json_data.get("ClientIpRequestsRateLimit"), ClientIpRequestsRateLimitDefinition),
            ClientIpScannersRequestsRateLimit=deserialize_list(json_data.get("ClientIpScannersRequestsRateLimit"), ClientIpScannersRequestsRateLimitDefinition),
            ClientIpToUriFailedRequestsRateLimit=deserialize_list(json_data.get("ClientIpToUriFailedRequestsRateLimit"), ClientIpToUriFailedRequestsRateLimitDefinition),
            ClientIpToUriRequestsRateLimit=deserialize_list(json_data.get("ClientIpToUriRequestsRateLimit"), ClientIpToUriRequestsRateLimitDefinition),
            CustomRequestsRateLimit=deserialize_list(json_data.get("CustomRequestsRateLimit"), CustomRequestsRateLimitDefinition),
            HttpHeaderRateLimits=deserialize_list(json_data.get("HttpHeaderRateLimits"), HttpHeaderRateLimitsDefinition),
            UriFailedRequestsRateLimit=deserialize_list(json_data.get("UriFailedRequestsRateLimit"), UriFailedRequestsRateLimitDefinition),
            UriRequestsRateLimit=deserialize_list(json_data.get("UriRequestsRateLimit"), UriRequestsRateLimitDefinition),
            UriScannersRequestsRateLimit=deserialize_list(json_data.get("UriScannersRequestsRateLimit"), UriScannersRequestsRateLimitDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RlProfileDefinition = RlProfileDefinition


@dataclass
class ClientIpConnectionsRateLimitDefinition(BaseModel):
    ExplicitTracking: Optional[bool]
    FineGrain: Optional[bool]
    HttpCookie: Optional[str]
    HttpHeader: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    RateLimiter: Optional[Sequence["_RateLimiterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientIpConnectionsRateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientIpConnectionsRateLimitDefinition"]:
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
_ClientIpConnectionsRateLimitDefinition = ClientIpConnectionsRateLimitDefinition


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
class ClientIpFailedRequestsRateLimitDefinition(BaseModel):
    ExplicitTracking: Optional[bool]
    FineGrain: Optional[bool]
    HttpCookie: Optional[str]
    HttpHeader: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    RateLimiter: Optional[Sequence["_RateLimiterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientIpFailedRequestsRateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientIpFailedRequestsRateLimitDefinition"]:
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
_ClientIpFailedRequestsRateLimitDefinition = ClientIpFailedRequestsRateLimitDefinition


@dataclass
class ClientIpRequestsRateLimitDefinition(BaseModel):
    ExplicitTracking: Optional[bool]
    FineGrain: Optional[bool]
    HttpCookie: Optional[str]
    HttpHeader: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    RateLimiter: Optional[Sequence["_RateLimiterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientIpRequestsRateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientIpRequestsRateLimitDefinition"]:
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
_ClientIpRequestsRateLimitDefinition = ClientIpRequestsRateLimitDefinition


@dataclass
class ClientIpScannersRequestsRateLimitDefinition(BaseModel):
    ExplicitTracking: Optional[bool]
    FineGrain: Optional[bool]
    HttpCookie: Optional[str]
    HttpHeader: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    RateLimiter: Optional[Sequence["_RateLimiterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientIpScannersRequestsRateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientIpScannersRequestsRateLimitDefinition"]:
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
_ClientIpScannersRequestsRateLimitDefinition = ClientIpScannersRequestsRateLimitDefinition


@dataclass
class ClientIpToUriFailedRequestsRateLimitDefinition(BaseModel):
    ExplicitTracking: Optional[bool]
    FineGrain: Optional[bool]
    HttpCookie: Optional[str]
    HttpHeader: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    RateLimiter: Optional[Sequence["_RateLimiterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientIpToUriFailedRequestsRateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientIpToUriFailedRequestsRateLimitDefinition"]:
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
_ClientIpToUriFailedRequestsRateLimitDefinition = ClientIpToUriFailedRequestsRateLimitDefinition


@dataclass
class ClientIpToUriRequestsRateLimitDefinition(BaseModel):
    ExplicitTracking: Optional[bool]
    FineGrain: Optional[bool]
    HttpCookie: Optional[str]
    HttpHeader: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    RateLimiter: Optional[Sequence["_RateLimiterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientIpToUriRequestsRateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientIpToUriRequestsRateLimitDefinition"]:
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
_ClientIpToUriRequestsRateLimitDefinition = ClientIpToUriRequestsRateLimitDefinition


@dataclass
class CustomRequestsRateLimitDefinition(BaseModel):
    ExplicitTracking: Optional[bool]
    FineGrain: Optional[bool]
    HttpCookie: Optional[str]
    HttpHeader: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    RateLimiter: Optional[Sequence["_RateLimiterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomRequestsRateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomRequestsRateLimitDefinition"]:
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
_CustomRequestsRateLimitDefinition = CustomRequestsRateLimitDefinition


@dataclass
class HttpHeaderRateLimitsDefinition(BaseModel):
    ExplicitTracking: Optional[bool]
    FineGrain: Optional[bool]
    HttpCookie: Optional[str]
    HttpHeader: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    RateLimiter: Optional[Sequence["_RateLimiterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpHeaderRateLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpHeaderRateLimitsDefinition"]:
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
_HttpHeaderRateLimitsDefinition = HttpHeaderRateLimitsDefinition


@dataclass
class UriFailedRequestsRateLimitDefinition(BaseModel):
    ExplicitTracking: Optional[bool]
    FineGrain: Optional[bool]
    HttpCookie: Optional[str]
    HttpHeader: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    RateLimiter: Optional[Sequence["_RateLimiterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UriFailedRequestsRateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UriFailedRequestsRateLimitDefinition"]:
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
_UriFailedRequestsRateLimitDefinition = UriFailedRequestsRateLimitDefinition


@dataclass
class UriRequestsRateLimitDefinition(BaseModel):
    ExplicitTracking: Optional[bool]
    FineGrain: Optional[bool]
    HttpCookie: Optional[str]
    HttpHeader: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    RateLimiter: Optional[Sequence["_RateLimiterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UriRequestsRateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UriRequestsRateLimitDefinition"]:
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
_UriRequestsRateLimitDefinition = UriRequestsRateLimitDefinition


@dataclass
class UriScannersRequestsRateLimitDefinition(BaseModel):
    ExplicitTracking: Optional[bool]
    FineGrain: Optional[bool]
    HttpCookie: Optional[str]
    HttpHeader: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    RateLimiter: Optional[Sequence["_RateLimiterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UriScannersRequestsRateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UriScannersRequestsRateLimitDefinition"]:
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
_UriScannersRequestsRateLimitDefinition = UriScannersRequestsRateLimitDefinition


@dataclass
class HttpProfileDefinition(BaseModel):
    AllowDotsInHeaderName: Optional[bool]
    ClientBodyTimeout: Optional[float]
    ClientHeaderTimeout: Optional[float]
    ClientMaxBodySize: Optional[float]
    ClientMaxHeaderSize: Optional[float]
    ClientMaxRequestSize: Optional[float]
    ConnectionMultiplexingEnabled: Optional[bool]
    DetectNtlmApp: Optional[bool]
    DisableKeepalivePostsMsie6: Optional[bool]
    DisableSniHostnameCheck: Optional[bool]
    EnableChunkMerge: Optional[bool]
    EnableFireAndForget: Optional[bool]
    EnableRequestBodyBuffering: Optional[bool]
    EnableRequestBodyMetrics: Optional[bool]
    FwdCloseHdrForBoundConnections: Optional[bool]
    HstsEnabled: Optional[bool]
    HstsMaxAge: Optional[float]
    HstsSubdomainsEnabled: Optional[bool]
    HttpToHttps: Optional[bool]
    HttpUpstreamBufferSize: Optional[float]
    HttponlyEnabled: Optional[bool]
    KeepaliveHeader: Optional[bool]
    KeepaliveTimeout: Optional[float]
    MaxBadRpsCip: Optional[float]
    MaxBadRpsCipUri: Optional[float]
    MaxBadRpsUri: Optional[float]
    MaxKeepaliveRequests: Optional[float]
    MaxResponseHeadersSize: Optional[float]
    MaxRpsCip: Optional[float]
    MaxRpsCipUri: Optional[float]
    MaxRpsUnknownCip: Optional[float]
    MaxRpsUnknownUri: Optional[float]
    MaxRpsUri: Optional[float]
    PkiProfileRef: Optional[str]
    PostAcceptTimeout: Optional[float]
    ResetConnHttpOnSslPort: Optional[bool]
    RespondWith100Continue: Optional[bool]
    SecureCookieEnabled: Optional[bool]
    ServerSideRedirectToHttps: Optional[bool]
    SslClientCertificateMode: Optional[str]
    UseAppKeepaliveTimeout: Optional[bool]
    WebsocketsEnabled: Optional[bool]
    XForwardedProtoEnabled: Optional[bool]
    XffAlternateName: Optional[str]
    XffEnabled: Optional[bool]
    CacheConfig: Optional[Sequence["_CacheConfigDefinition"]]
    CompressionProfile: Optional[Sequence["_CompressionProfileDefinition"]]
    Http2Profile: Optional[Sequence["_Http2ProfileDefinition"]]
    SslClientCertificateAction: Optional[Sequence["_SslClientCertificateActionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowDotsInHeaderName=json_data.get("AllowDotsInHeaderName"),
            ClientBodyTimeout=json_data.get("ClientBodyTimeout"),
            ClientHeaderTimeout=json_data.get("ClientHeaderTimeout"),
            ClientMaxBodySize=json_data.get("ClientMaxBodySize"),
            ClientMaxHeaderSize=json_data.get("ClientMaxHeaderSize"),
            ClientMaxRequestSize=json_data.get("ClientMaxRequestSize"),
            ConnectionMultiplexingEnabled=json_data.get("ConnectionMultiplexingEnabled"),
            DetectNtlmApp=json_data.get("DetectNtlmApp"),
            DisableKeepalivePostsMsie6=json_data.get("DisableKeepalivePostsMsie6"),
            DisableSniHostnameCheck=json_data.get("DisableSniHostnameCheck"),
            EnableChunkMerge=json_data.get("EnableChunkMerge"),
            EnableFireAndForget=json_data.get("EnableFireAndForget"),
            EnableRequestBodyBuffering=json_data.get("EnableRequestBodyBuffering"),
            EnableRequestBodyMetrics=json_data.get("EnableRequestBodyMetrics"),
            FwdCloseHdrForBoundConnections=json_data.get("FwdCloseHdrForBoundConnections"),
            HstsEnabled=json_data.get("HstsEnabled"),
            HstsMaxAge=json_data.get("HstsMaxAge"),
            HstsSubdomainsEnabled=json_data.get("HstsSubdomainsEnabled"),
            HttpToHttps=json_data.get("HttpToHttps"),
            HttpUpstreamBufferSize=json_data.get("HttpUpstreamBufferSize"),
            HttponlyEnabled=json_data.get("HttponlyEnabled"),
            KeepaliveHeader=json_data.get("KeepaliveHeader"),
            KeepaliveTimeout=json_data.get("KeepaliveTimeout"),
            MaxBadRpsCip=json_data.get("MaxBadRpsCip"),
            MaxBadRpsCipUri=json_data.get("MaxBadRpsCipUri"),
            MaxBadRpsUri=json_data.get("MaxBadRpsUri"),
            MaxKeepaliveRequests=json_data.get("MaxKeepaliveRequests"),
            MaxResponseHeadersSize=json_data.get("MaxResponseHeadersSize"),
            MaxRpsCip=json_data.get("MaxRpsCip"),
            MaxRpsCipUri=json_data.get("MaxRpsCipUri"),
            MaxRpsUnknownCip=json_data.get("MaxRpsUnknownCip"),
            MaxRpsUnknownUri=json_data.get("MaxRpsUnknownUri"),
            MaxRpsUri=json_data.get("MaxRpsUri"),
            PkiProfileRef=json_data.get("PkiProfileRef"),
            PostAcceptTimeout=json_data.get("PostAcceptTimeout"),
            ResetConnHttpOnSslPort=json_data.get("ResetConnHttpOnSslPort"),
            RespondWith100Continue=json_data.get("RespondWith100Continue"),
            SecureCookieEnabled=json_data.get("SecureCookieEnabled"),
            ServerSideRedirectToHttps=json_data.get("ServerSideRedirectToHttps"),
            SslClientCertificateMode=json_data.get("SslClientCertificateMode"),
            UseAppKeepaliveTimeout=json_data.get("UseAppKeepaliveTimeout"),
            WebsocketsEnabled=json_data.get("WebsocketsEnabled"),
            XForwardedProtoEnabled=json_data.get("XForwardedProtoEnabled"),
            XffAlternateName=json_data.get("XffAlternateName"),
            XffEnabled=json_data.get("XffEnabled"),
            CacheConfig=deserialize_list(json_data.get("CacheConfig"), CacheConfigDefinition),
            CompressionProfile=deserialize_list(json_data.get("CompressionProfile"), CompressionProfileDefinition),
            Http2Profile=deserialize_list(json_data.get("Http2Profile"), Http2ProfileDefinition),
            SslClientCertificateAction=deserialize_list(json_data.get("SslClientCertificateAction"), SslClientCertificateActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpProfileDefinition = HttpProfileDefinition


@dataclass
class CacheConfigDefinition(BaseModel):
    AgeHeader: Optional[bool]
    Aggressive: Optional[bool]
    DateHeader: Optional[bool]
    DefaultExpire: Optional[float]
    Enabled: Optional[bool]
    HeuristicExpire: Optional[bool]
    IgnoreRequestCacheControl: Optional[bool]
    MaxCacheSize: Optional[float]
    MaxObjectSize: Optional[float]
    MimeTypesBlockGroupRefs: Optional[Sequence[str]]
    MimeTypesBlockLists: Optional[Sequence[str]]
    MimeTypesGroupRefs: Optional[Sequence[str]]
    MimeTypesList: Optional[Sequence[str]]
    MinObjectSize: Optional[float]
    QueryCacheable: Optional[bool]
    XcacheHeader: Optional[bool]
    UriNonCacheable: Optional[Sequence["_UriNonCacheableDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CacheConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AgeHeader=json_data.get("AgeHeader"),
            Aggressive=json_data.get("Aggressive"),
            DateHeader=json_data.get("DateHeader"),
            DefaultExpire=json_data.get("DefaultExpire"),
            Enabled=json_data.get("Enabled"),
            HeuristicExpire=json_data.get("HeuristicExpire"),
            IgnoreRequestCacheControl=json_data.get("IgnoreRequestCacheControl"),
            MaxCacheSize=json_data.get("MaxCacheSize"),
            MaxObjectSize=json_data.get("MaxObjectSize"),
            MimeTypesBlockGroupRefs=json_data.get("MimeTypesBlockGroupRefs"),
            MimeTypesBlockLists=json_data.get("MimeTypesBlockLists"),
            MimeTypesGroupRefs=json_data.get("MimeTypesGroupRefs"),
            MimeTypesList=json_data.get("MimeTypesList"),
            MinObjectSize=json_data.get("MinObjectSize"),
            QueryCacheable=json_data.get("QueryCacheable"),
            XcacheHeader=json_data.get("XcacheHeader"),
            UriNonCacheable=deserialize_list(json_data.get("UriNonCacheable"), UriNonCacheableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheConfigDefinition = CacheConfigDefinition


@dataclass
class UriNonCacheableDefinition(BaseModel):
    MatchCase: Optional[str]
    MatchCriteria: Optional[str]
    MatchStr: Optional[Sequence[str]]
    StringGroupRefs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_UriNonCacheableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UriNonCacheableDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCase=json_data.get("MatchCase"),
            MatchCriteria=json_data.get("MatchCriteria"),
            MatchStr=json_data.get("MatchStr"),
            StringGroupRefs=json_data.get("StringGroupRefs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UriNonCacheableDefinition = UriNonCacheableDefinition


@dataclass
class CompressionProfileDefinition(BaseModel):
    CompressibleContentRef: Optional[str]
    Compression: Optional[bool]
    RemoveAcceptEncodingHeader: Optional[bool]
    Type: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CompressionProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CompressionProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            CompressibleContentRef=json_data.get("CompressibleContentRef"),
            Compression=json_data.get("Compression"),
            RemoveAcceptEncodingHeader=json_data.get("RemoveAcceptEncodingHeader"),
            Type=json_data.get("Type"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CompressionProfileDefinition = CompressionProfileDefinition


@dataclass
class FilterDefinition(BaseModel):
    DevicesRef: Optional[str]
    Index: Optional[float]
    IpAddrsRef: Optional[str]
    Level: Optional[str]
    Match: Optional[str]
    Name: Optional[str]
    UserAgent: Optional[Sequence[str]]
    IpAddrPrefixes: Optional[Sequence["_IpAddrPrefixesDefinition"]]
    IpAddrRanges: Optional[Sequence["_IpAddrRangesDefinition"]]
    IpAddrs: Optional[Sequence["_IpAddrsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            DevicesRef=json_data.get("DevicesRef"),
            Index=json_data.get("Index"),
            IpAddrsRef=json_data.get("IpAddrsRef"),
            Level=json_data.get("Level"),
            Match=json_data.get("Match"),
            Name=json_data.get("Name"),
            UserAgent=json_data.get("UserAgent"),
            IpAddrPrefixes=deserialize_list(json_data.get("IpAddrPrefixes"), IpAddrPrefixesDefinition),
            IpAddrRanges=deserialize_list(json_data.get("IpAddrRanges"), IpAddrRangesDefinition),
            IpAddrs=deserialize_list(json_data.get("IpAddrs"), IpAddrsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class IpAddrPrefixesDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddrPrefixesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddrPrefixesDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddrPrefixesDefinition = IpAddrPrefixesDefinition


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
class IpAddrRangesDefinition(BaseModel):
    Begin: Optional[Sequence["_BeginDefinition"]]
    End: Optional[Sequence["_EndDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddrRangesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddrRangesDefinition"]:
        if not json_data:
            return None
        return cls(
            Begin=deserialize_list(json_data.get("Begin"), BeginDefinition),
            End=deserialize_list(json_data.get("End"), EndDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddrRangesDefinition = IpAddrRangesDefinition


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
class IpAddrsDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddrsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddrsDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddrsDefinition = IpAddrsDefinition


@dataclass
class Http2ProfileDefinition(BaseModel):
    Http2InitialWindowSize: Optional[float]
    MaxHttp2ConcurrentStreamsPerConnection: Optional[float]
    MaxHttp2ControlFramesPerConnection: Optional[float]
    MaxHttp2EmptyDataFramesPerConnection: Optional[float]
    MaxHttp2HeaderFieldSize: Optional[float]
    MaxHttp2QueuedFramesToClientPerConnection: Optional[float]
    MaxHttp2RequestsPerConnection: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Http2ProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Http2ProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            Http2InitialWindowSize=json_data.get("Http2InitialWindowSize"),
            MaxHttp2ConcurrentStreamsPerConnection=json_data.get("MaxHttp2ConcurrentStreamsPerConnection"),
            MaxHttp2ControlFramesPerConnection=json_data.get("MaxHttp2ControlFramesPerConnection"),
            MaxHttp2EmptyDataFramesPerConnection=json_data.get("MaxHttp2EmptyDataFramesPerConnection"),
            MaxHttp2HeaderFieldSize=json_data.get("MaxHttp2HeaderFieldSize"),
            MaxHttp2QueuedFramesToClientPerConnection=json_data.get("MaxHttp2QueuedFramesToClientPerConnection"),
            MaxHttp2RequestsPerConnection=json_data.get("MaxHttp2RequestsPerConnection"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Http2ProfileDefinition = Http2ProfileDefinition


@dataclass
class SslClientCertificateActionDefinition(BaseModel):
    CloseConnection: Optional[bool]
    Headers: Optional[Sequence["_HeadersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SslClientCertificateActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslClientCertificateActionDefinition"]:
        if not json_data:
            return None
        return cls(
            CloseConnection=json_data.get("CloseConnection"),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslClientCertificateActionDefinition = SslClientCertificateActionDefinition


@dataclass
class HeadersDefinition(BaseModel):
    RequestHeader: Optional[str]
    RequestHeaderValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            RequestHeader=json_data.get("RequestHeader"),
            RequestHeaderValue=json_data.get("RequestHeaderValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


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
class SipServiceProfileDefinition(BaseModel):
    TransactionTimeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SipServiceProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SipServiceProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            TransactionTimeout=json_data.get("TransactionTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SipServiceProfileDefinition = SipServiceProfileDefinition


@dataclass
class TcpAppProfileDefinition(BaseModel):
    PkiProfileRef: Optional[str]
    ProxyProtocolEnabled: Optional[bool]
    ProxyProtocolVersion: Optional[str]
    SslClientCertificateMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TcpAppProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpAppProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            PkiProfileRef=json_data.get("PkiProfileRef"),
            ProxyProtocolEnabled=json_data.get("ProxyProtocolEnabled"),
            ProxyProtocolVersion=json_data.get("ProxyProtocolVersion"),
            SslClientCertificateMode=json_data.get("SslClientCertificateMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpAppProfileDefinition = TcpAppProfileDefinition


