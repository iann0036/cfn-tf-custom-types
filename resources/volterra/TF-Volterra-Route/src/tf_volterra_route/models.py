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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Description: Optional[str]
    Disable: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    Routes: Optional[Sequence["_RoutesDefinition"]]

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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Routes=deserialize_list(json_data.get("Routes"), RoutesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class RoutesDefinition(BaseModel):
    DisableCustomScript: Optional[bool]
    DisableLocationAdd: Optional[bool]
    RequestHeadersToRemove: Optional[Sequence[str]]
    ResponseHeadersToRemove: Optional[Sequence[str]]
    Match: Optional[Sequence["_MatchDefinition"]]
    RequestHeadersToAdd: Optional[Sequence["_RequestHeadersToAddDefinition"]]
    ResponseHeadersToAdd: Optional[Sequence["_ResponseHeadersToAddDefinition"]]
    RouteDestination: Optional[Sequence["_RouteDestinationDefinition"]]
    RouteDirectResponse: Optional[Sequence["_RouteDirectResponseDefinition"]]
    RouteRedirect: Optional[Sequence["_RouteRedirectDefinition"]]
    ServicePolicy: Optional[Sequence["_ServicePolicyDefinition"]]
    WafType: Optional[Sequence["_WafTypeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableCustomScript=json_data.get("DisableCustomScript"),
            DisableLocationAdd=json_data.get("DisableLocationAdd"),
            RequestHeadersToRemove=json_data.get("RequestHeadersToRemove"),
            ResponseHeadersToRemove=json_data.get("ResponseHeadersToRemove"),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
            RequestHeadersToAdd=deserialize_list(json_data.get("RequestHeadersToAdd"), RequestHeadersToAddDefinition),
            ResponseHeadersToAdd=deserialize_list(json_data.get("ResponseHeadersToAdd"), ResponseHeadersToAddDefinition),
            RouteDestination=deserialize_list(json_data.get("RouteDestination"), RouteDestinationDefinition),
            RouteDirectResponse=deserialize_list(json_data.get("RouteDirectResponse"), RouteDirectResponseDefinition),
            RouteRedirect=deserialize_list(json_data.get("RouteRedirect"), RouteRedirectDefinition),
            ServicePolicy=deserialize_list(json_data.get("ServicePolicy"), ServicePolicyDefinition),
            WafType=deserialize_list(json_data.get("WafType"), WafTypeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutesDefinition = RoutesDefinition


@dataclass
class MatchDefinition(BaseModel):
    HttpMethod: Optional[str]
    Headers: Optional[Sequence["_HeadersDefinition"]]
    Path: Optional[Sequence["_PathDefinition"]]
    QueryParams: Optional[Sequence["_QueryParamsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            HttpMethod=json_data.get("HttpMethod"),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
            Path=deserialize_list(json_data.get("Path"), PathDefinition),
            QueryParams=deserialize_list(json_data.get("QueryParams"), QueryParamsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class HeadersDefinition(BaseModel):
    Exact: Optional[str]
    InvertMatch: Optional[bool]
    Name: Optional[str]
    Presence: Optional[bool]
    Regex: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            Exact=json_data.get("Exact"),
            InvertMatch=json_data.get("InvertMatch"),
            Name=json_data.get("Name"),
            Presence=json_data.get("Presence"),
            Regex=json_data.get("Regex"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


@dataclass
class PathDefinition(BaseModel):
    Path: Optional[str]
    Prefix: Optional[str]
    Regex: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Prefix=json_data.get("Prefix"),
            Regex=json_data.get("Regex"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathDefinition = PathDefinition


@dataclass
class QueryParamsDefinition(BaseModel):
    Exact: Optional[str]
    Key: Optional[str]
    Regex: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueryParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            Exact=json_data.get("Exact"),
            Key=json_data.get("Key"),
            Regex=json_data.get("Regex"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryParamsDefinition = QueryParamsDefinition


@dataclass
class RequestHeadersToAddDefinition(BaseModel):
    Append: Optional[bool]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestHeadersToAddDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestHeadersToAddDefinition"]:
        if not json_data:
            return None
        return cls(
            Append=json_data.get("Append"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestHeadersToAddDefinition = RequestHeadersToAddDefinition


@dataclass
class ResponseHeadersToAddDefinition(BaseModel):
    Append: Optional[bool]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseHeadersToAddDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseHeadersToAddDefinition"]:
        if not json_data:
            return None
        return cls(
            Append=json_data.get("Append"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseHeadersToAddDefinition = ResponseHeadersToAddDefinition


@dataclass
class RouteDestinationDefinition(BaseModel):
    AutoHostRewrite: Optional[bool]
    DoNotRetractCluster: Optional[bool]
    EndpointSubsets: Optional[Sequence["_EndpointSubsetsDefinition"]]
    HostRewrite: Optional[str]
    PrefixRewrite: Optional[str]
    Priority: Optional[str]
    RetractCluster: Optional[bool]
    Timeout: Optional[float]
    BufferPolicy: Optional[Sequence["_BufferPolicyDefinition"]]
    CorsPolicy: Optional[Sequence["_CorsPolicyDefinition"]]
    Destinations: Optional[Sequence["_DestinationsDefinition"]]
    HashPolicy: Optional[Sequence["_HashPolicyDefinition"]]
    MirrorPolicy: Optional[Sequence["_MirrorPolicyDefinition"]]
    RetryPolicy: Optional[Sequence["_RetryPolicyDefinition"]]
    SpdyConfig: Optional[Sequence["_SpdyConfigDefinition"]]
    WebSocketConfig: Optional[Sequence["_WebSocketConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RouteDestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteDestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoHostRewrite=json_data.get("AutoHostRewrite"),
            DoNotRetractCluster=json_data.get("DoNotRetractCluster"),
            EndpointSubsets=deserialize_list(json_data.get("EndpointSubsets"), EndpointSubsetsDefinition),
            HostRewrite=json_data.get("HostRewrite"),
            PrefixRewrite=json_data.get("PrefixRewrite"),
            Priority=json_data.get("Priority"),
            RetractCluster=json_data.get("RetractCluster"),
            Timeout=json_data.get("Timeout"),
            BufferPolicy=deserialize_list(json_data.get("BufferPolicy"), BufferPolicyDefinition),
            CorsPolicy=deserialize_list(json_data.get("CorsPolicy"), CorsPolicyDefinition),
            Destinations=deserialize_list(json_data.get("Destinations"), DestinationsDefinition),
            HashPolicy=deserialize_list(json_data.get("HashPolicy"), HashPolicyDefinition),
            MirrorPolicy=deserialize_list(json_data.get("MirrorPolicy"), MirrorPolicyDefinition),
            RetryPolicy=deserialize_list(json_data.get("RetryPolicy"), RetryPolicyDefinition),
            SpdyConfig=deserialize_list(json_data.get("SpdyConfig"), SpdyConfigDefinition),
            WebSocketConfig=deserialize_list(json_data.get("WebSocketConfig"), WebSocketConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteDestinationDefinition = RouteDestinationDefinition


@dataclass
class EndpointSubsetsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointSubsetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointSubsetsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointSubsetsDefinition = EndpointSubsetsDefinition


@dataclass
class BufferPolicyDefinition(BaseModel):
    Disabled: Optional[bool]
    MaxRequestBytes: Optional[float]
    MaxRequestTime: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BufferPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BufferPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Disabled=json_data.get("Disabled"),
            MaxRequestBytes=json_data.get("MaxRequestBytes"),
            MaxRequestTime=json_data.get("MaxRequestTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BufferPolicyDefinition = BufferPolicyDefinition


@dataclass
class CorsPolicyDefinition(BaseModel):
    AllowCredentials: Optional[bool]
    AllowHeaders: Optional[str]
    AllowMethods: Optional[str]
    AllowOrigin: Optional[Sequence[str]]
    AllowOriginRegex: Optional[Sequence[str]]
    Disabled: Optional[bool]
    ExposeHeaders: Optional[str]
    MaxAge: Optional[str]
    MaximumAge: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CorsPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowCredentials=json_data.get("AllowCredentials"),
            AllowHeaders=json_data.get("AllowHeaders"),
            AllowMethods=json_data.get("AllowMethods"),
            AllowOrigin=json_data.get("AllowOrigin"),
            AllowOriginRegex=json_data.get("AllowOriginRegex"),
            Disabled=json_data.get("Disabled"),
            ExposeHeaders=json_data.get("ExposeHeaders"),
            MaxAge=json_data.get("MaxAge"),
            MaximumAge=json_data.get("MaximumAge"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsPolicyDefinition = CorsPolicyDefinition


@dataclass
class DestinationsDefinition(BaseModel):
    EndpointSubsets: Optional[Sequence["_EndpointSubsetsDefinition2"]]
    Weight: Optional[float]
    Cluster: Optional[Sequence["_ClusterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationsDefinition"]:
        if not json_data:
            return None
        return cls(
            EndpointSubsets=deserialize_list(json_data.get("EndpointSubsets"), EndpointSubsetsDefinition2),
            Weight=json_data.get("Weight"),
            Cluster=deserialize_list(json_data.get("Cluster"), ClusterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationsDefinition = DestinationsDefinition


@dataclass
class EndpointSubsetsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointSubsetsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointSubsetsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointSubsetsDefinition2 = EndpointSubsetsDefinition2


@dataclass
class ClusterDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterDefinition = ClusterDefinition


@dataclass
class HashPolicyDefinition(BaseModel):
    HeaderName: Optional[str]
    SourceIp: Optional[bool]
    Terminal: Optional[bool]
    Cookie: Optional[Sequence["_CookieDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HashPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HashPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            HeaderName=json_data.get("HeaderName"),
            SourceIp=json_data.get("SourceIp"),
            Terminal=json_data.get("Terminal"),
            Cookie=deserialize_list(json_data.get("Cookie"), CookieDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HashPolicyDefinition = HashPolicyDefinition


@dataclass
class CookieDefinition(BaseModel):
    Name: Optional[str]
    Path: Optional[str]
    Ttl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CookieDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookieDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CookieDefinition = CookieDefinition


@dataclass
class MirrorPolicyDefinition(BaseModel):
    Cluster: Optional[Sequence["_ClusterDefinition"]]
    Percent: Optional[Sequence["_PercentDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MirrorPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MirrorPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Cluster=deserialize_list(json_data.get("Cluster"), ClusterDefinition),
            Percent=deserialize_list(json_data.get("Percent"), PercentDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MirrorPolicyDefinition = MirrorPolicyDefinition


@dataclass
class PercentDefinition(BaseModel):
    Denominator: Optional[str]
    Numerator: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PercentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PercentDefinition"]:
        if not json_data:
            return None
        return cls(
            Denominator=json_data.get("Denominator"),
            Numerator=json_data.get("Numerator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PercentDefinition = PercentDefinition


@dataclass
class RetryPolicyDefinition(BaseModel):
    NumRetries: Optional[float]
    PerTryTimeout: Optional[float]
    RetriableStatusCodes: Optional[Sequence[float]]
    RetryOn: Optional[str]
    BackOff: Optional[Sequence["_BackOffDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RetryPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            NumRetries=json_data.get("NumRetries"),
            PerTryTimeout=json_data.get("PerTryTimeout"),
            RetriableStatusCodes=json_data.get("RetriableStatusCodes"),
            RetryOn=json_data.get("RetryOn"),
            BackOff=deserialize_list(json_data.get("BackOff"), BackOffDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryPolicyDefinition = RetryPolicyDefinition


@dataclass
class BackOffDefinition(BaseModel):
    BaseInterval: Optional[float]
    MaxInterval: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BackOffDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackOffDefinition"]:
        if not json_data:
            return None
        return cls(
            BaseInterval=json_data.get("BaseInterval"),
            MaxInterval=json_data.get("MaxInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackOffDefinition = BackOffDefinition


@dataclass
class SpdyConfigDefinition(BaseModel):
    UseSpdy: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SpdyConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpdyConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            UseSpdy=json_data.get("UseSpdy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpdyConfigDefinition = SpdyConfigDefinition


@dataclass
class WebSocketConfigDefinition(BaseModel):
    IdleTimeout: Optional[float]
    MaxConnectAttempts: Optional[float]
    UseWebsocket: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_WebSocketConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebSocketConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            IdleTimeout=json_data.get("IdleTimeout"),
            MaxConnectAttempts=json_data.get("MaxConnectAttempts"),
            UseWebsocket=json_data.get("UseWebsocket"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebSocketConfigDefinition = WebSocketConfigDefinition


@dataclass
class RouteDirectResponseDefinition(BaseModel):
    ResponseBody: Optional[str]
    ResponseCode: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RouteDirectResponseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteDirectResponseDefinition"]:
        if not json_data:
            return None
        return cls(
            ResponseBody=json_data.get("ResponseBody"),
            ResponseCode=json_data.get("ResponseCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteDirectResponseDefinition = RouteDirectResponseDefinition


@dataclass
class RouteRedirectDefinition(BaseModel):
    AllParams: Optional[bool]
    HostRedirect: Optional[str]
    PathRedirect: Optional[str]
    ProtoRedirect: Optional[str]
    RemoveAllParams: Optional[bool]
    ResponseCode: Optional[float]
    RetainAllParams: Optional[bool]
    StripQueryParams: Optional[Sequence["_StripQueryParamsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RouteRedirectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteRedirectDefinition"]:
        if not json_data:
            return None
        return cls(
            AllParams=json_data.get("AllParams"),
            HostRedirect=json_data.get("HostRedirect"),
            PathRedirect=json_data.get("PathRedirect"),
            ProtoRedirect=json_data.get("ProtoRedirect"),
            RemoveAllParams=json_data.get("RemoveAllParams"),
            ResponseCode=json_data.get("ResponseCode"),
            RetainAllParams=json_data.get("RetainAllParams"),
            StripQueryParams=deserialize_list(json_data.get("StripQueryParams"), StripQueryParamsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteRedirectDefinition = RouteRedirectDefinition


@dataclass
class StripQueryParamsDefinition(BaseModel):
    QueryParams: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_StripQueryParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StripQueryParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            QueryParams=json_data.get("QueryParams"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StripQueryParamsDefinition = StripQueryParamsDefinition


@dataclass
class ServicePolicyDefinition(BaseModel):
    Disable: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ServicePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Disable=json_data.get("Disable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicePolicyDefinition = ServicePolicyDefinition


@dataclass
class WafTypeDefinition(BaseModel):
    Waf: Optional[Sequence["_WafDefinition"]]
    WafRules: Optional[Sequence["_WafRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WafTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WafTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Waf=deserialize_list(json_data.get("Waf"), WafDefinition),
            WafRules=deserialize_list(json_data.get("WafRules"), WafRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WafTypeDefinition = WafTypeDefinition


@dataclass
class WafDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WafDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WafDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WafDefinition = WafDefinition


@dataclass
class WafRulesDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WafRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WafRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WafRulesDefinition = WafRulesDefinition


