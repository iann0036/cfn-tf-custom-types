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
    CreationTimestamp: Optional[str]
    DefaultService: Optional[str]
    Description: Optional[str]
    Fingerprint: Optional[str]
    Id: Optional[str]
    MapId: Optional[float]
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    SelfLink: Optional[str]
    DefaultUrlRedirect: Optional[Sequence["_DefaultUrlRedirectDefinition"]]
    HostRule: Optional[Sequence["_HostRuleDefinition"]]
    PathMatcher: Optional[Sequence["_PathMatcherDefinition"]]
    Test: Optional[Sequence["_TestDefinition"]]
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
            CreationTimestamp=json_data.get("CreationTimestamp"),
            DefaultService=json_data.get("DefaultService"),
            Description=json_data.get("Description"),
            Fingerprint=json_data.get("Fingerprint"),
            Id=json_data.get("Id"),
            MapId=json_data.get("MapId"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            SelfLink=json_data.get("SelfLink"),
            DefaultUrlRedirect=deserialize_list(json_data.get("DefaultUrlRedirect"), DefaultUrlRedirectDefinition),
            HostRule=deserialize_list(json_data.get("HostRule"), HostRuleDefinition),
            PathMatcher=deserialize_list(json_data.get("PathMatcher"), PathMatcherDefinition),
            Test=deserialize_list(json_data.get("Test"), TestDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefaultUrlRedirectDefinition(BaseModel):
    HostRedirect: Optional[str]
    HttpsRedirect: Optional[bool]
    PathRedirect: Optional[str]
    PrefixRedirect: Optional[str]
    RedirectResponseCode: Optional[str]
    StripQuery: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultUrlRedirectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultUrlRedirectDefinition"]:
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
_DefaultUrlRedirectDefinition = DefaultUrlRedirectDefinition


@dataclass
class HostRuleDefinition(BaseModel):
    Description: Optional[str]
    Hosts: Optional[Sequence[str]]
    PathMatcher: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Hosts=json_data.get("Hosts"),
            PathMatcher=json_data.get("PathMatcher"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostRuleDefinition = HostRuleDefinition


@dataclass
class PathMatcherDefinition(BaseModel):
    DefaultService: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    DefaultUrlRedirect: Optional[Sequence["_DefaultUrlRedirectDefinition"]]
    PathRule: Optional[Sequence["_PathRuleDefinition"]]
    RouteRules: Optional[Sequence["_RouteRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PathMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultService=json_data.get("DefaultService"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            DefaultUrlRedirect=deserialize_list(json_data.get("DefaultUrlRedirect"), DefaultUrlRedirectDefinition),
            PathRule=deserialize_list(json_data.get("PathRule"), PathRuleDefinition),
            RouteRules=deserialize_list(json_data.get("RouteRules"), RouteRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathMatcherDefinition = PathMatcherDefinition


@dataclass
class PathRuleDefinition(BaseModel):
    Paths: Optional[Sequence[str]]
    Service: Optional[str]
    RouteAction: Optional[Sequence["_RouteActionDefinition"]]
    UrlRedirect: Optional[Sequence["_UrlRedirectDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PathRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Paths=json_data.get("Paths"),
            Service=json_data.get("Service"),
            RouteAction=deserialize_list(json_data.get("RouteAction"), RouteActionDefinition),
            UrlRedirect=deserialize_list(json_data.get("UrlRedirect"), UrlRedirectDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathRuleDefinition = PathRuleDefinition


@dataclass
class RouteActionDefinition(BaseModel):
    CorsPolicy: Optional[Sequence["_CorsPolicyDefinition"]]
    FaultInjectionPolicy: Optional[Sequence["_FaultInjectionPolicyDefinition"]]
    RequestMirrorPolicy: Optional[Sequence["_RequestMirrorPolicyDefinition"]]
    RetryPolicy: Optional[Sequence["_RetryPolicyDefinition"]]
    Timeout: Optional[Sequence["_TimeoutDefinition"]]
    UrlRewrite: Optional[Sequence["_UrlRewriteDefinition"]]
    WeightedBackendServices: Optional[Sequence["_WeightedBackendServicesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RouteActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteActionDefinition"]:
        if not json_data:
            return None
        return cls(
            CorsPolicy=deserialize_list(json_data.get("CorsPolicy"), CorsPolicyDefinition),
            FaultInjectionPolicy=deserialize_list(json_data.get("FaultInjectionPolicy"), FaultInjectionPolicyDefinition),
            RequestMirrorPolicy=deserialize_list(json_data.get("RequestMirrorPolicy"), RequestMirrorPolicyDefinition),
            RetryPolicy=deserialize_list(json_data.get("RetryPolicy"), RetryPolicyDefinition),
            Timeout=deserialize_list(json_data.get("Timeout"), TimeoutDefinition),
            UrlRewrite=deserialize_list(json_data.get("UrlRewrite"), UrlRewriteDefinition),
            WeightedBackendServices=deserialize_list(json_data.get("WeightedBackendServices"), WeightedBackendServicesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteActionDefinition = RouteActionDefinition


@dataclass
class CorsPolicyDefinition(BaseModel):
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
        cls: Type["_CorsPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsPolicyDefinition"]:
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
_CorsPolicyDefinition = CorsPolicyDefinition


@dataclass
class FaultInjectionPolicyDefinition(BaseModel):
    Abort: Optional[Sequence["_AbortDefinition"]]
    Delay: Optional[Sequence["_DelayDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FaultInjectionPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FaultInjectionPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Abort=deserialize_list(json_data.get("Abort"), AbortDefinition),
            Delay=deserialize_list(json_data.get("Delay"), DelayDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FaultInjectionPolicyDefinition = FaultInjectionPolicyDefinition


@dataclass
class AbortDefinition(BaseModel):
    HttpStatus: Optional[float]
    Percentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AbortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AbortDefinition"]:
        if not json_data:
            return None
        return cls(
            HttpStatus=json_data.get("HttpStatus"),
            Percentage=json_data.get("Percentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AbortDefinition = AbortDefinition


@dataclass
class DelayDefinition(BaseModel):
    Percentage: Optional[float]
    FixedDelay: Optional[Sequence["_FixedDelayDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DelayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DelayDefinition"]:
        if not json_data:
            return None
        return cls(
            Percentage=json_data.get("Percentage"),
            FixedDelay=deserialize_list(json_data.get("FixedDelay"), FixedDelayDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DelayDefinition = DelayDefinition


@dataclass
class FixedDelayDefinition(BaseModel):
    Nanos: Optional[float]
    Seconds: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FixedDelayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FixedDelayDefinition"]:
        if not json_data:
            return None
        return cls(
            Nanos=json_data.get("Nanos"),
            Seconds=json_data.get("Seconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FixedDelayDefinition = FixedDelayDefinition


@dataclass
class RequestMirrorPolicyDefinition(BaseModel):
    BackendService: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestMirrorPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestMirrorPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            BackendService=json_data.get("BackendService"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestMirrorPolicyDefinition = RequestMirrorPolicyDefinition


@dataclass
class RetryPolicyDefinition(BaseModel):
    NumRetries: Optional[float]
    RetryConditions: Optional[Sequence[str]]
    PerTryTimeout: Optional[Sequence["_PerTryTimeoutDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RetryPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            NumRetries=json_data.get("NumRetries"),
            RetryConditions=json_data.get("RetryConditions"),
            PerTryTimeout=deserialize_list(json_data.get("PerTryTimeout"), PerTryTimeoutDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryPolicyDefinition = RetryPolicyDefinition


@dataclass
class PerTryTimeoutDefinition(BaseModel):
    Nanos: Optional[float]
    Seconds: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PerTryTimeoutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PerTryTimeoutDefinition"]:
        if not json_data:
            return None
        return cls(
            Nanos=json_data.get("Nanos"),
            Seconds=json_data.get("Seconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PerTryTimeoutDefinition = PerTryTimeoutDefinition


@dataclass
class TimeoutDefinition(BaseModel):
    Nanos: Optional[float]
    Seconds: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutDefinition"]:
        if not json_data:
            return None
        return cls(
            Nanos=json_data.get("Nanos"),
            Seconds=json_data.get("Seconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutDefinition = TimeoutDefinition


@dataclass
class UrlRewriteDefinition(BaseModel):
    HostRewrite: Optional[str]
    PathPrefixRewrite: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UrlRewriteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlRewriteDefinition"]:
        if not json_data:
            return None
        return cls(
            HostRewrite=json_data.get("HostRewrite"),
            PathPrefixRewrite=json_data.get("PathPrefixRewrite"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlRewriteDefinition = UrlRewriteDefinition


@dataclass
class WeightedBackendServicesDefinition(BaseModel):
    BackendService: Optional[str]
    Weight: Optional[float]
    HeaderAction: Optional[Sequence["_HeaderActionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WeightedBackendServicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeightedBackendServicesDefinition"]:
        if not json_data:
            return None
        return cls(
            BackendService=json_data.get("BackendService"),
            Weight=json_data.get("Weight"),
            HeaderAction=deserialize_list(json_data.get("HeaderAction"), HeaderActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeightedBackendServicesDefinition = WeightedBackendServicesDefinition


@dataclass
class HeaderActionDefinition(BaseModel):
    RequestHeadersToRemove: Optional[Sequence[str]]
    ResponseHeadersToRemove: Optional[Sequence[str]]
    RequestHeadersToAdd: Optional[Sequence["_RequestHeadersToAddDefinition"]]
    ResponseHeadersToAdd: Optional[Sequence["_ResponseHeadersToAddDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderActionDefinition"]:
        if not json_data:
            return None
        return cls(
            RequestHeadersToRemove=json_data.get("RequestHeadersToRemove"),
            ResponseHeadersToRemove=json_data.get("ResponseHeadersToRemove"),
            RequestHeadersToAdd=deserialize_list(json_data.get("RequestHeadersToAdd"), RequestHeadersToAddDefinition),
            ResponseHeadersToAdd=deserialize_list(json_data.get("ResponseHeadersToAdd"), ResponseHeadersToAddDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderActionDefinition = HeaderActionDefinition


@dataclass
class RequestHeadersToAddDefinition(BaseModel):
    HeaderName: Optional[str]
    HeaderValue: Optional[str]
    Replace: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RequestHeadersToAddDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestHeadersToAddDefinition"]:
        if not json_data:
            return None
        return cls(
            HeaderName=json_data.get("HeaderName"),
            HeaderValue=json_data.get("HeaderValue"),
            Replace=json_data.get("Replace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestHeadersToAddDefinition = RequestHeadersToAddDefinition


@dataclass
class ResponseHeadersToAddDefinition(BaseModel):
    HeaderName: Optional[str]
    HeaderValue: Optional[str]
    Replace: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseHeadersToAddDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseHeadersToAddDefinition"]:
        if not json_data:
            return None
        return cls(
            HeaderName=json_data.get("HeaderName"),
            HeaderValue=json_data.get("HeaderValue"),
            Replace=json_data.get("Replace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseHeadersToAddDefinition = ResponseHeadersToAddDefinition


@dataclass
class UrlRedirectDefinition(BaseModel):
    HostRedirect: Optional[str]
    HttpsRedirect: Optional[bool]
    PathRedirect: Optional[str]
    PrefixRedirect: Optional[str]
    RedirectResponseCode: Optional[str]
    StripQuery: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_UrlRedirectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlRedirectDefinition"]:
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
_UrlRedirectDefinition = UrlRedirectDefinition


@dataclass
class RouteRulesDefinition(BaseModel):
    Priority: Optional[float]
    Service: Optional[str]
    HeaderAction: Optional[Sequence["_HeaderActionDefinition"]]
    MatchRules: Optional[Sequence["_MatchRulesDefinition"]]
    RouteAction: Optional[Sequence["_RouteActionDefinition"]]
    UrlRedirect: Optional[Sequence["_UrlRedirectDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RouteRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Priority=json_data.get("Priority"),
            Service=json_data.get("Service"),
            HeaderAction=deserialize_list(json_data.get("HeaderAction"), HeaderActionDefinition),
            MatchRules=deserialize_list(json_data.get("MatchRules"), MatchRulesDefinition),
            RouteAction=deserialize_list(json_data.get("RouteAction"), RouteActionDefinition),
            UrlRedirect=deserialize_list(json_data.get("UrlRedirect"), UrlRedirectDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteRulesDefinition = RouteRulesDefinition


@dataclass
class MatchRulesDefinition(BaseModel):
    FullPathMatch: Optional[str]
    IgnoreCase: Optional[bool]
    PrefixMatch: Optional[str]
    RegexMatch: Optional[str]
    HeaderMatches: Optional[Sequence["_HeaderMatchesDefinition"]]
    MetadataFilters: Optional[Sequence["_MetadataFiltersDefinition"]]
    QueryParameterMatches: Optional[Sequence["_QueryParameterMatchesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            FullPathMatch=json_data.get("FullPathMatch"),
            IgnoreCase=json_data.get("IgnoreCase"),
            PrefixMatch=json_data.get("PrefixMatch"),
            RegexMatch=json_data.get("RegexMatch"),
            HeaderMatches=deserialize_list(json_data.get("HeaderMatches"), HeaderMatchesDefinition),
            MetadataFilters=deserialize_list(json_data.get("MetadataFilters"), MetadataFiltersDefinition),
            QueryParameterMatches=deserialize_list(json_data.get("QueryParameterMatches"), QueryParameterMatchesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchRulesDefinition = MatchRulesDefinition


@dataclass
class HeaderMatchesDefinition(BaseModel):
    ExactMatch: Optional[str]
    HeaderName: Optional[str]
    InvertMatch: Optional[bool]
    PrefixMatch: Optional[str]
    PresentMatch: Optional[bool]
    RegexMatch: Optional[str]
    SuffixMatch: Optional[str]
    RangeMatch: Optional[Sequence["_RangeMatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderMatchesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderMatchesDefinition"]:
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
            RangeMatch=deserialize_list(json_data.get("RangeMatch"), RangeMatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderMatchesDefinition = HeaderMatchesDefinition


@dataclass
class RangeMatchDefinition(BaseModel):
    RangeEnd: Optional[float]
    RangeStart: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RangeMatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangeMatchDefinition"]:
        if not json_data:
            return None
        return cls(
            RangeEnd=json_data.get("RangeEnd"),
            RangeStart=json_data.get("RangeStart"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangeMatchDefinition = RangeMatchDefinition


@dataclass
class MetadataFiltersDefinition(BaseModel):
    FilterMatchCriteria: Optional[str]
    FilterLabels: Optional[Sequence["_FilterLabelsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataFiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataFiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            FilterMatchCriteria=json_data.get("FilterMatchCriteria"),
            FilterLabels=deserialize_list(json_data.get("FilterLabels"), FilterLabelsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataFiltersDefinition = MetadataFiltersDefinition


@dataclass
class FilterLabelsDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterLabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterLabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterLabelsDefinition = FilterLabelsDefinition


@dataclass
class QueryParameterMatchesDefinition(BaseModel):
    ExactMatch: Optional[str]
    Name: Optional[str]
    PresentMatch: Optional[bool]
    RegexMatch: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueryParameterMatchesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryParameterMatchesDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactMatch=json_data.get("ExactMatch"),
            Name=json_data.get("Name"),
            PresentMatch=json_data.get("PresentMatch"),
            RegexMatch=json_data.get("RegexMatch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryParameterMatchesDefinition = QueryParameterMatchesDefinition


@dataclass
class TestDefinition(BaseModel):
    Description: Optional[str]
    Host: Optional[str]
    Path: Optional[str]
    Service: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TestDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TestDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Host=json_data.get("Host"),
            Path=json_data.get("Path"),
            Service=json_data.get("Service"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TestDefinition = TestDefinition


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


