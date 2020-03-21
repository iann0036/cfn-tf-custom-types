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
    CreationTimestamp: Optional[str]
    DefaultService: Optional[str]
    Description: Optional[str]
    Fingerprint: Optional[str]
    Id: Optional[str]
    MapId: Optional[float]
    Name: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    HeaderAction: Optional[Sequence["_HeaderAction"]]
    HostRule: Optional[Sequence["_HostRule"]]
    PathMatcher: Optional[Sequence["_PathMatcher"]]
    Test: Optional[Sequence["_Test"]]
    Timeouts: Optional["_Timeouts"]
    RequestHeadersToAdd: Optional[Sequence["_RequestHeadersToAdd"]]
    ResponseHeadersToAdd: Optional[Sequence["_ResponseHeadersToAdd"]]
    PathRule: Optional[Sequence["_PathRule"]]
    RouteRules: Optional[Sequence["_RouteRules"]]
    RouteAction: Optional[Sequence["_RouteAction"]]
    UrlRedirect: Optional[Sequence["_UrlRedirect"]]
    MatchRules: Optional[Sequence["_MatchRules"]]
    CorsPolicy: Optional[Sequence["_CorsPolicy"]]
    FaultInjectionPolicy: Optional[Sequence["_FaultInjectionPolicy"]]
    RequestMirrorPolicy: Optional[Sequence["_RequestMirrorPolicy"]]
    RetryPolicy: Optional[Sequence["_RetryPolicy"]]
    Timeout: Optional[Sequence["_Timeout"]]
    UrlRewrite: Optional[Sequence["_UrlRewrite"]]
    WeightedBackendServices: Optional[Sequence["_WeightedBackendServices"]]
    HeaderMatches: Optional[Sequence["_HeaderMatches"]]
    MetadataFilters: Optional[Sequence["_MetadataFilters"]]
    QueryParameterMatches: Optional[Sequence["_QueryParameterMatches"]]
    Abort: Optional[Sequence["_Abort"]]
    Delay: Optional[Sequence["_Delay"]]
    PerTryTimeout: Optional[Sequence["_PerTryTimeout"]]
    RangeMatch: Optional[Sequence["_RangeMatch"]]
    FilterLabels: Optional[Sequence["_FilterLabels"]]
    FixedDelay: Optional[Sequence["_FixedDelay"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreationTimestamp=json_data.get("CreationTimestamp"),
            DefaultService=json_data.get("DefaultService"),
            Description=json_data.get("Description"),
            Fingerprint=json_data.get("Fingerprint"),
            Id=json_data.get("Id"),
            MapId=json_data.get("MapId"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            HeaderAction=json_data.get("HeaderAction"),
            HostRule=json_data.get("HostRule"),
            PathMatcher=json_data.get("PathMatcher"),
            Test=json_data.get("Test"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            RequestHeadersToAdd=json_data.get("RequestHeadersToAdd"),
            ResponseHeadersToAdd=json_data.get("ResponseHeadersToAdd"),
            PathRule=json_data.get("PathRule"),
            RouteRules=json_data.get("RouteRules"),
            RouteAction=json_data.get("RouteAction"),
            UrlRedirect=json_data.get("UrlRedirect"),
            MatchRules=json_data.get("MatchRules"),
            CorsPolicy=json_data.get("CorsPolicy"),
            FaultInjectionPolicy=json_data.get("FaultInjectionPolicy"),
            RequestMirrorPolicy=json_data.get("RequestMirrorPolicy"),
            RetryPolicy=json_data.get("RetryPolicy"),
            Timeout=json_data.get("Timeout"),
            UrlRewrite=json_data.get("UrlRewrite"),
            WeightedBackendServices=json_data.get("WeightedBackendServices"),
            HeaderMatches=json_data.get("HeaderMatches"),
            MetadataFilters=json_data.get("MetadataFilters"),
            QueryParameterMatches=json_data.get("QueryParameterMatches"),
            Abort=json_data.get("Abort"),
            Delay=json_data.get("Delay"),
            PerTryTimeout=json_data.get("PerTryTimeout"),
            RangeMatch=json_data.get("RangeMatch"),
            FilterLabels=json_data.get("FilterLabels"),
            FixedDelay=json_data.get("FixedDelay"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HeaderAction:
    RequestHeadersToRemove: Optional[Sequence[str]]
    ResponseHeadersToRemove: Optional[Sequence[str]]
    RequestHeadersToAdd: Optional[Sequence["_RequestHeadersToAdd"]]
    ResponseHeadersToAdd: Optional[Sequence["_ResponseHeadersToAdd"]]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderAction"]:
        if not json_data:
            return None
        return cls(
            RequestHeadersToRemove=json_data.get("RequestHeadersToRemove"),
            ResponseHeadersToRemove=json_data.get("ResponseHeadersToRemove"),
            RequestHeadersToAdd=json_data.get("RequestHeadersToAdd"),
            ResponseHeadersToAdd=json_data.get("ResponseHeadersToAdd"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderAction = HeaderAction


@dataclass
class RequestHeadersToAdd:
    HeaderName: Optional[str]
    HeaderValue: Optional[str]
    Replace: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RequestHeadersToAdd"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestHeadersToAdd"]:
        if not json_data:
            return None
        return cls(
            HeaderName=json_data.get("HeaderName"),
            HeaderValue=json_data.get("HeaderValue"),
            Replace=json_data.get("Replace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestHeadersToAdd = RequestHeadersToAdd


@dataclass
class ResponseHeadersToAdd:
    HeaderName: Optional[str]
    HeaderValue: Optional[str]
    Replace: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseHeadersToAdd"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseHeadersToAdd"]:
        if not json_data:
            return None
        return cls(
            HeaderName=json_data.get("HeaderName"),
            HeaderValue=json_data.get("HeaderValue"),
            Replace=json_data.get("Replace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseHeadersToAdd = ResponseHeadersToAdd


@dataclass
class HostRule:
    Description: Optional[str]
    Hosts: Optional[Sequence[str]]
    PathMatcher: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostRule"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Hosts=json_data.get("Hosts"),
            PathMatcher=json_data.get("PathMatcher"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostRule = HostRule


@dataclass
class PathMatcher:
    DefaultService: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    HeaderAction: Optional[Sequence["_HeaderAction"]]
    PathRule: Optional[Sequence["_PathRule"]]
    RouteRules: Optional[Sequence["_RouteRules"]]

    @classmethod
    def _deserialize(
        cls: Type["_PathMatcher"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathMatcher"]:
        if not json_data:
            return None
        return cls(
            DefaultService=json_data.get("DefaultService"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            HeaderAction=json_data.get("HeaderAction"),
            PathRule=json_data.get("PathRule"),
            RouteRules=json_data.get("RouteRules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathMatcher = PathMatcher


@dataclass
class PathRule:
    Paths: Optional[Sequence[str]]
    Service: Optional[str]
    RouteAction: Optional[Sequence["_RouteAction"]]
    UrlRedirect: Optional[Sequence["_UrlRedirect"]]

    @classmethod
    def _deserialize(
        cls: Type["_PathRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathRule"]:
        if not json_data:
            return None
        return cls(
            Paths=json_data.get("Paths"),
            Service=json_data.get("Service"),
            RouteAction=json_data.get("RouteAction"),
            UrlRedirect=json_data.get("UrlRedirect"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathRule = PathRule


@dataclass
class RouteAction:
    CorsPolicy: Optional[Sequence["_CorsPolicy"]]
    FaultInjectionPolicy: Optional[Sequence["_FaultInjectionPolicy"]]
    RequestMirrorPolicy: Optional[Sequence["_RequestMirrorPolicy"]]
    RetryPolicy: Optional[Sequence["_RetryPolicy"]]
    Timeout: Optional[Sequence["_Timeout"]]
    UrlRewrite: Optional[Sequence["_UrlRewrite"]]
    WeightedBackendServices: Optional[Sequence["_WeightedBackendServices"]]

    @classmethod
    def _deserialize(
        cls: Type["_RouteAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteAction"]:
        if not json_data:
            return None
        return cls(
            CorsPolicy=json_data.get("CorsPolicy"),
            FaultInjectionPolicy=json_data.get("FaultInjectionPolicy"),
            RequestMirrorPolicy=json_data.get("RequestMirrorPolicy"),
            RetryPolicy=json_data.get("RetryPolicy"),
            Timeout=json_data.get("Timeout"),
            UrlRewrite=json_data.get("UrlRewrite"),
            WeightedBackendServices=json_data.get("WeightedBackendServices"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteAction = RouteAction


@dataclass
class CorsPolicy:
    AllowCredentials: Optional[bool]
    AllowHeaders: Optional[Sequence[str]]
    AllowMethods: Optional[Sequence[str]]
    AllowOriginRegexes: Optional[Sequence[str]]
    AllowOrigins: Optional[Sequence[str]]
    Disabled: Optional[bool]
    ExposeHeaders: Optional[Sequence[str]]
    MaxAge: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CorsPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsPolicy"]:
        if not json_data:
            return None
        return cls(
            AllowCredentials=json_data.get("AllowCredentials"),
            AllowHeaders=json_data.get("AllowHeaders"),
            AllowMethods=json_data.get("AllowMethods"),
            AllowOriginRegexes=json_data.get("AllowOriginRegexes"),
            AllowOrigins=json_data.get("AllowOrigins"),
            Disabled=json_data.get("Disabled"),
            ExposeHeaders=json_data.get("ExposeHeaders"),
            MaxAge=json_data.get("MaxAge"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsPolicy = CorsPolicy


@dataclass
class FaultInjectionPolicy:
    Abort: Optional[Sequence["_Abort"]]
    Delay: Optional[Sequence["_Delay"]]

    @classmethod
    def _deserialize(
        cls: Type["_FaultInjectionPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FaultInjectionPolicy"]:
        if not json_data:
            return None
        return cls(
            Abort=json_data.get("Abort"),
            Delay=json_data.get("Delay"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FaultInjectionPolicy = FaultInjectionPolicy


@dataclass
class Abort:
    HttpStatus: Optional[float]
    Percentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Abort"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Abort"]:
        if not json_data:
            return None
        return cls(
            HttpStatus=json_data.get("HttpStatus"),
            Percentage=json_data.get("Percentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Abort = Abort


@dataclass
class Delay:
    Percentage: Optional[float]
    FixedDelay: Optional[Sequence["_FixedDelay"]]

    @classmethod
    def _deserialize(
        cls: Type["_Delay"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Delay"]:
        if not json_data:
            return None
        return cls(
            Percentage=json_data.get("Percentage"),
            FixedDelay=json_data.get("FixedDelay"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Delay = Delay


@dataclass
class FixedDelay:
    Nanos: Optional[float]
    Seconds: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FixedDelay"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FixedDelay"]:
        if not json_data:
            return None
        return cls(
            Nanos=json_data.get("Nanos"),
            Seconds=json_data.get("Seconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FixedDelay = FixedDelay


@dataclass
class RequestMirrorPolicy:
    BackendService: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestMirrorPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestMirrorPolicy"]:
        if not json_data:
            return None
        return cls(
            BackendService=json_data.get("BackendService"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestMirrorPolicy = RequestMirrorPolicy


@dataclass
class RetryPolicy:
    NumRetries: Optional[float]
    RetryConditions: Optional[Sequence[str]]
    PerTryTimeout: Optional[Sequence["_PerTryTimeout"]]

    @classmethod
    def _deserialize(
        cls: Type["_RetryPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryPolicy"]:
        if not json_data:
            return None
        return cls(
            NumRetries=json_data.get("NumRetries"),
            RetryConditions=json_data.get("RetryConditions"),
            PerTryTimeout=json_data.get("PerTryTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryPolicy = RetryPolicy


@dataclass
class PerTryTimeout:
    Nanos: Optional[float]
    Seconds: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PerTryTimeout"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PerTryTimeout"]:
        if not json_data:
            return None
        return cls(
            Nanos=json_data.get("Nanos"),
            Seconds=json_data.get("Seconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PerTryTimeout = PerTryTimeout


@dataclass
class Timeout:
    Nanos: Optional[float]
    Seconds: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeout"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeout"]:
        if not json_data:
            return None
        return cls(
            Nanos=json_data.get("Nanos"),
            Seconds=json_data.get("Seconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeout = Timeout


@dataclass
class UrlRewrite:
    HostRewrite: Optional[str]
    PathPrefixRewrite: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UrlRewrite"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlRewrite"]:
        if not json_data:
            return None
        return cls(
            HostRewrite=json_data.get("HostRewrite"),
            PathPrefixRewrite=json_data.get("PathPrefixRewrite"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlRewrite = UrlRewrite


@dataclass
class WeightedBackendServices:
    BackendService: Optional[str]
    Weight: Optional[float]
    HeaderAction: Optional[Sequence["_HeaderAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_WeightedBackendServices"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeightedBackendServices"]:
        if not json_data:
            return None
        return cls(
            BackendService=json_data.get("BackendService"),
            Weight=json_data.get("Weight"),
            HeaderAction=json_data.get("HeaderAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeightedBackendServices = WeightedBackendServices


@dataclass
class UrlRedirect:
    HostRedirect: Optional[str]
    HttpsRedirect: Optional[bool]
    PathRedirect: Optional[str]
    PrefixRedirect: Optional[str]
    RedirectResponseCode: Optional[str]
    StripQuery: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_UrlRedirect"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlRedirect"]:
        if not json_data:
            return None
        return cls(
            HostRedirect=json_data.get("HostRedirect"),
            HttpsRedirect=json_data.get("HttpsRedirect"),
            PathRedirect=json_data.get("PathRedirect"),
            PrefixRedirect=json_data.get("PrefixRedirect"),
            RedirectResponseCode=json_data.get("RedirectResponseCode"),
            StripQuery=json_data.get("StripQuery"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlRedirect = UrlRedirect


@dataclass
class RouteRules:
    Priority: Optional[float]
    Service: Optional[str]
    HeaderAction: Optional[Sequence["_HeaderAction"]]
    MatchRules: Optional[Sequence["_MatchRules"]]
    RouteAction: Optional[Sequence["_RouteAction"]]
    UrlRedirect: Optional[Sequence["_UrlRedirect"]]

    @classmethod
    def _deserialize(
        cls: Type["_RouteRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteRules"]:
        if not json_data:
            return None
        return cls(
            Priority=json_data.get("Priority"),
            Service=json_data.get("Service"),
            HeaderAction=json_data.get("HeaderAction"),
            MatchRules=json_data.get("MatchRules"),
            RouteAction=json_data.get("RouteAction"),
            UrlRedirect=json_data.get("UrlRedirect"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteRules = RouteRules


@dataclass
class MatchRules:
    FullPathMatch: Optional[str]
    IgnoreCase: Optional[bool]
    PrefixMatch: Optional[str]
    RegexMatch: Optional[str]
    HeaderMatches: Optional[Sequence["_HeaderMatches"]]
    MetadataFilters: Optional[Sequence["_MetadataFilters"]]
    QueryParameterMatches: Optional[Sequence["_QueryParameterMatches"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchRules"]:
        if not json_data:
            return None
        return cls(
            FullPathMatch=json_data.get("FullPathMatch"),
            IgnoreCase=json_data.get("IgnoreCase"),
            PrefixMatch=json_data.get("PrefixMatch"),
            RegexMatch=json_data.get("RegexMatch"),
            HeaderMatches=json_data.get("HeaderMatches"),
            MetadataFilters=json_data.get("MetadataFilters"),
            QueryParameterMatches=json_data.get("QueryParameterMatches"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchRules = MatchRules


@dataclass
class HeaderMatches:
    ExactMatch: Optional[str]
    HeaderName: Optional[str]
    InvertMatch: Optional[bool]
    PrefixMatch: Optional[str]
    PresentMatch: Optional[bool]
    RegexMatch: Optional[str]
    SuffixMatch: Optional[str]
    RangeMatch: Optional[Sequence["_RangeMatch"]]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderMatches"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderMatches"]:
        if not json_data:
            return None
        return cls(
            ExactMatch=json_data.get("ExactMatch"),
            HeaderName=json_data.get("HeaderName"),
            InvertMatch=json_data.get("InvertMatch"),
            PrefixMatch=json_data.get("PrefixMatch"),
            PresentMatch=json_data.get("PresentMatch"),
            RegexMatch=json_data.get("RegexMatch"),
            SuffixMatch=json_data.get("SuffixMatch"),
            RangeMatch=json_data.get("RangeMatch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderMatches = HeaderMatches


@dataclass
class RangeMatch:
    RangeEnd: Optional[float]
    RangeStart: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RangeMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangeMatch"]:
        if not json_data:
            return None
        return cls(
            RangeEnd=json_data.get("RangeEnd"),
            RangeStart=json_data.get("RangeStart"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangeMatch = RangeMatch


@dataclass
class MetadataFilters:
    FilterMatchCriteria: Optional[str]
    FilterLabels: Optional[Sequence["_FilterLabels"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataFilters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataFilters"]:
        if not json_data:
            return None
        return cls(
            FilterMatchCriteria=json_data.get("FilterMatchCriteria"),
            FilterLabels=json_data.get("FilterLabels"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataFilters = MetadataFilters


@dataclass
class FilterLabels:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterLabels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterLabels"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterLabels = FilterLabels


@dataclass
class QueryParameterMatches:
    ExactMatch: Optional[str]
    Name: Optional[str]
    PresentMatch: Optional[bool]
    RegexMatch: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueryParameterMatches"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryParameterMatches"]:
        if not json_data:
            return None
        return cls(
            ExactMatch=json_data.get("ExactMatch"),
            Name=json_data.get("Name"),
            PresentMatch=json_data.get("PresentMatch"),
            RegexMatch=json_data.get("RegexMatch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryParameterMatches = QueryParameterMatches


@dataclass
class Test:
    Description: Optional[str]
    Host: Optional[str]
    Path: Optional[str]
    Service: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Test"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Test"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Host=json_data.get("Host"),
            Path=json_data.get("Path"),
            Service=json_data.get("Service"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Test = Test


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


