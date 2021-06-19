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
    ContentTypesToCompress: Optional[Sequence[str]]
    HostName: Optional[str]
    Id: Optional[str]
    IsCompressionEnabled: Optional[bool]
    IsHttpAllowed: Optional[bool]
    IsHttpsAllowed: Optional[bool]
    Location: Optional[str]
    Name: Optional[str]
    OptimizationType: Optional[str]
    OriginHostHeader: Optional[str]
    OriginPath: Optional[str]
    ProbePath: Optional[str]
    ProfileName: Optional[str]
    QuerystringCachingBehaviour: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    DeliveryRule: Optional[Sequence["_DeliveryRuleDefinition"]]
    GeoFilter: Optional[Sequence["_GeoFilterDefinition"]]
    GlobalDeliveryRule: Optional[Sequence["_GlobalDeliveryRuleDefinition"]]
    Origin: Optional[Sequence["_OriginDefinition"]]
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
            ContentTypesToCompress=json_data.get("ContentTypesToCompress"),
            HostName=json_data.get("HostName"),
            Id=json_data.get("Id"),
            IsCompressionEnabled=json_data.get("IsCompressionEnabled"),
            IsHttpAllowed=json_data.get("IsHttpAllowed"),
            IsHttpsAllowed=json_data.get("IsHttpsAllowed"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            OptimizationType=json_data.get("OptimizationType"),
            OriginHostHeader=json_data.get("OriginHostHeader"),
            OriginPath=json_data.get("OriginPath"),
            ProbePath=json_data.get("ProbePath"),
            ProfileName=json_data.get("ProfileName"),
            QuerystringCachingBehaviour=json_data.get("QuerystringCachingBehaviour"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            DeliveryRule=deserialize_list(json_data.get("DeliveryRule"), DeliveryRuleDefinition),
            GeoFilter=deserialize_list(json_data.get("GeoFilter"), GeoFilterDefinition),
            GlobalDeliveryRule=deserialize_list(json_data.get("GlobalDeliveryRule"), GlobalDeliveryRuleDefinition),
            Origin=deserialize_list(json_data.get("Origin"), OriginDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class DeliveryRuleDefinition(BaseModel):
    Name: Optional[str]
    Order: Optional[float]
    CacheExpirationAction: Optional[Sequence["_CacheExpirationActionDefinition"]]
    CacheKeyQueryStringAction: Optional[Sequence["_CacheKeyQueryStringActionDefinition"]]
    CookiesCondition: Optional[Sequence["_CookiesConditionDefinition"]]
    DeviceCondition: Optional[Sequence["_DeviceConditionDefinition"]]
    HttpVersionCondition: Optional[Sequence["_HttpVersionConditionDefinition"]]
    ModifyRequestHeaderAction: Optional[Sequence["_ModifyRequestHeaderActionDefinition"]]
    ModifyResponseHeaderAction: Optional[Sequence["_ModifyResponseHeaderActionDefinition"]]
    PostArgCondition: Optional[Sequence["_PostArgConditionDefinition"]]
    QueryStringCondition: Optional[Sequence["_QueryStringConditionDefinition"]]
    RemoteAddressCondition: Optional[Sequence["_RemoteAddressConditionDefinition"]]
    RequestBodyCondition: Optional[Sequence["_RequestBodyConditionDefinition"]]
    RequestHeaderCondition: Optional[Sequence["_RequestHeaderConditionDefinition"]]
    RequestMethodCondition: Optional[Sequence["_RequestMethodConditionDefinition"]]
    RequestSchemeCondition: Optional[Sequence["_RequestSchemeConditionDefinition"]]
    RequestUriCondition: Optional[Sequence["_RequestUriConditionDefinition"]]
    UrlFileExtensionCondition: Optional[Sequence["_UrlFileExtensionConditionDefinition"]]
    UrlFileNameCondition: Optional[Sequence["_UrlFileNameConditionDefinition"]]
    UrlPathCondition: Optional[Sequence["_UrlPathConditionDefinition"]]
    UrlRedirectAction: Optional[Sequence["_UrlRedirectActionDefinition"]]
    UrlRewriteAction: Optional[Sequence["_UrlRewriteActionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DeliveryRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeliveryRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Order=json_data.get("Order"),
            CacheExpirationAction=deserialize_list(json_data.get("CacheExpirationAction"), CacheExpirationActionDefinition),
            CacheKeyQueryStringAction=deserialize_list(json_data.get("CacheKeyQueryStringAction"), CacheKeyQueryStringActionDefinition),
            CookiesCondition=deserialize_list(json_data.get("CookiesCondition"), CookiesConditionDefinition),
            DeviceCondition=deserialize_list(json_data.get("DeviceCondition"), DeviceConditionDefinition),
            HttpVersionCondition=deserialize_list(json_data.get("HttpVersionCondition"), HttpVersionConditionDefinition),
            ModifyRequestHeaderAction=deserialize_list(json_data.get("ModifyRequestHeaderAction"), ModifyRequestHeaderActionDefinition),
            ModifyResponseHeaderAction=deserialize_list(json_data.get("ModifyResponseHeaderAction"), ModifyResponseHeaderActionDefinition),
            PostArgCondition=deserialize_list(json_data.get("PostArgCondition"), PostArgConditionDefinition),
            QueryStringCondition=deserialize_list(json_data.get("QueryStringCondition"), QueryStringConditionDefinition),
            RemoteAddressCondition=deserialize_list(json_data.get("RemoteAddressCondition"), RemoteAddressConditionDefinition),
            RequestBodyCondition=deserialize_list(json_data.get("RequestBodyCondition"), RequestBodyConditionDefinition),
            RequestHeaderCondition=deserialize_list(json_data.get("RequestHeaderCondition"), RequestHeaderConditionDefinition),
            RequestMethodCondition=deserialize_list(json_data.get("RequestMethodCondition"), RequestMethodConditionDefinition),
            RequestSchemeCondition=deserialize_list(json_data.get("RequestSchemeCondition"), RequestSchemeConditionDefinition),
            RequestUriCondition=deserialize_list(json_data.get("RequestUriCondition"), RequestUriConditionDefinition),
            UrlFileExtensionCondition=deserialize_list(json_data.get("UrlFileExtensionCondition"), UrlFileExtensionConditionDefinition),
            UrlFileNameCondition=deserialize_list(json_data.get("UrlFileNameCondition"), UrlFileNameConditionDefinition),
            UrlPathCondition=deserialize_list(json_data.get("UrlPathCondition"), UrlPathConditionDefinition),
            UrlRedirectAction=deserialize_list(json_data.get("UrlRedirectAction"), UrlRedirectActionDefinition),
            UrlRewriteAction=deserialize_list(json_data.get("UrlRewriteAction"), UrlRewriteActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeliveryRuleDefinition = DeliveryRuleDefinition


@dataclass
class CacheExpirationActionDefinition(BaseModel):
    Behavior: Optional[str]
    Duration: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CacheExpirationActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheExpirationActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Behavior=json_data.get("Behavior"),
            Duration=json_data.get("Duration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheExpirationActionDefinition = CacheExpirationActionDefinition


@dataclass
class CacheKeyQueryStringActionDefinition(BaseModel):
    Behavior: Optional[str]
    Parameters: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CacheKeyQueryStringActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheKeyQueryStringActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Behavior=json_data.get("Behavior"),
            Parameters=json_data.get("Parameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheKeyQueryStringActionDefinition = CacheKeyQueryStringActionDefinition


@dataclass
class CookiesConditionDefinition(BaseModel):
    MatchValues: Optional[Sequence[str]]
    NegateCondition: Optional[bool]
    Operator: Optional[str]
    Selector: Optional[str]
    Transforms: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CookiesConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookiesConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            NegateCondition=json_data.get("NegateCondition"),
            Operator=json_data.get("Operator"),
            Selector=json_data.get("Selector"),
            Transforms=json_data.get("Transforms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CookiesConditionDefinition = CookiesConditionDefinition


@dataclass
class DeviceConditionDefinition(BaseModel):
    MatchValues: Optional[Sequence[str]]
    NegateCondition: Optional[bool]
    Operator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            NegateCondition=json_data.get("NegateCondition"),
            Operator=json_data.get("Operator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceConditionDefinition = DeviceConditionDefinition


@dataclass
class HttpVersionConditionDefinition(BaseModel):
    MatchValues: Optional[Sequence[str]]
    NegateCondition: Optional[bool]
    Operator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpVersionConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpVersionConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            NegateCondition=json_data.get("NegateCondition"),
            Operator=json_data.get("Operator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpVersionConditionDefinition = HttpVersionConditionDefinition


@dataclass
class ModifyRequestHeaderActionDefinition(BaseModel):
    Action: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ModifyRequestHeaderActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModifyRequestHeaderActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModifyRequestHeaderActionDefinition = ModifyRequestHeaderActionDefinition


@dataclass
class ModifyResponseHeaderActionDefinition(BaseModel):
    Action: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ModifyResponseHeaderActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModifyResponseHeaderActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModifyResponseHeaderActionDefinition = ModifyResponseHeaderActionDefinition


@dataclass
class PostArgConditionDefinition(BaseModel):
    MatchValues: Optional[Sequence[str]]
    NegateCondition: Optional[bool]
    Operator: Optional[str]
    Selector: Optional[str]
    Transforms: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PostArgConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PostArgConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            NegateCondition=json_data.get("NegateCondition"),
            Operator=json_data.get("Operator"),
            Selector=json_data.get("Selector"),
            Transforms=json_data.get("Transforms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PostArgConditionDefinition = PostArgConditionDefinition


@dataclass
class QueryStringConditionDefinition(BaseModel):
    MatchValues: Optional[Sequence[str]]
    NegateCondition: Optional[bool]
    Operator: Optional[str]
    Transforms: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryStringConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryStringConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            NegateCondition=json_data.get("NegateCondition"),
            Operator=json_data.get("Operator"),
            Transforms=json_data.get("Transforms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryStringConditionDefinition = QueryStringConditionDefinition


@dataclass
class RemoteAddressConditionDefinition(BaseModel):
    MatchValues: Optional[Sequence[str]]
    NegateCondition: Optional[bool]
    Operator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RemoteAddressConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoteAddressConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            NegateCondition=json_data.get("NegateCondition"),
            Operator=json_data.get("Operator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoteAddressConditionDefinition = RemoteAddressConditionDefinition


@dataclass
class RequestBodyConditionDefinition(BaseModel):
    MatchValues: Optional[Sequence[str]]
    NegateCondition: Optional[bool]
    Operator: Optional[str]
    Transforms: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RequestBodyConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestBodyConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            NegateCondition=json_data.get("NegateCondition"),
            Operator=json_data.get("Operator"),
            Transforms=json_data.get("Transforms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestBodyConditionDefinition = RequestBodyConditionDefinition


@dataclass
class RequestHeaderConditionDefinition(BaseModel):
    MatchValues: Optional[Sequence[str]]
    NegateCondition: Optional[bool]
    Operator: Optional[str]
    Selector: Optional[str]
    Transforms: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RequestHeaderConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestHeaderConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            NegateCondition=json_data.get("NegateCondition"),
            Operator=json_data.get("Operator"),
            Selector=json_data.get("Selector"),
            Transforms=json_data.get("Transforms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestHeaderConditionDefinition = RequestHeaderConditionDefinition


@dataclass
class RequestMethodConditionDefinition(BaseModel):
    MatchValues: Optional[Sequence[str]]
    NegateCondition: Optional[bool]
    Operator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestMethodConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestMethodConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            NegateCondition=json_data.get("NegateCondition"),
            Operator=json_data.get("Operator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestMethodConditionDefinition = RequestMethodConditionDefinition


@dataclass
class RequestSchemeConditionDefinition(BaseModel):
    MatchValues: Optional[Sequence[str]]
    NegateCondition: Optional[bool]
    Operator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestSchemeConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestSchemeConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            NegateCondition=json_data.get("NegateCondition"),
            Operator=json_data.get("Operator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestSchemeConditionDefinition = RequestSchemeConditionDefinition


@dataclass
class RequestUriConditionDefinition(BaseModel):
    MatchValues: Optional[Sequence[str]]
    NegateCondition: Optional[bool]
    Operator: Optional[str]
    Transforms: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RequestUriConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestUriConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            NegateCondition=json_data.get("NegateCondition"),
            Operator=json_data.get("Operator"),
            Transforms=json_data.get("Transforms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestUriConditionDefinition = RequestUriConditionDefinition


@dataclass
class UrlFileExtensionConditionDefinition(BaseModel):
    MatchValues: Optional[Sequence[str]]
    NegateCondition: Optional[bool]
    Operator: Optional[str]
    Transforms: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_UrlFileExtensionConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlFileExtensionConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            NegateCondition=json_data.get("NegateCondition"),
            Operator=json_data.get("Operator"),
            Transforms=json_data.get("Transforms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlFileExtensionConditionDefinition = UrlFileExtensionConditionDefinition


@dataclass
class UrlFileNameConditionDefinition(BaseModel):
    MatchValues: Optional[Sequence[str]]
    NegateCondition: Optional[bool]
    Operator: Optional[str]
    Transforms: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_UrlFileNameConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlFileNameConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            NegateCondition=json_data.get("NegateCondition"),
            Operator=json_data.get("Operator"),
            Transforms=json_data.get("Transforms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlFileNameConditionDefinition = UrlFileNameConditionDefinition


@dataclass
class UrlPathConditionDefinition(BaseModel):
    MatchValues: Optional[Sequence[str]]
    NegateCondition: Optional[bool]
    Operator: Optional[str]
    Transforms: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_UrlPathConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlPathConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            NegateCondition=json_data.get("NegateCondition"),
            Operator=json_data.get("Operator"),
            Transforms=json_data.get("Transforms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlPathConditionDefinition = UrlPathConditionDefinition


@dataclass
class UrlRedirectActionDefinition(BaseModel):
    Fragment: Optional[str]
    Hostname: Optional[str]
    Path: Optional[str]
    Protocol: Optional[str]
    QueryString: Optional[str]
    RedirectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UrlRedirectActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlRedirectActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Fragment=json_data.get("Fragment"),
            Hostname=json_data.get("Hostname"),
            Path=json_data.get("Path"),
            Protocol=json_data.get("Protocol"),
            QueryString=json_data.get("QueryString"),
            RedirectType=json_data.get("RedirectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlRedirectActionDefinition = UrlRedirectActionDefinition


@dataclass
class UrlRewriteActionDefinition(BaseModel):
    Destination: Optional[str]
    PreserveUnmatchedPath: Optional[bool]
    SourcePattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UrlRewriteActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlRewriteActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
            PreserveUnmatchedPath=json_data.get("PreserveUnmatchedPath"),
            SourcePattern=json_data.get("SourcePattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlRewriteActionDefinition = UrlRewriteActionDefinition


@dataclass
class GeoFilterDefinition(BaseModel):
    Action: Optional[str]
    CountryCodes: Optional[Sequence[str]]
    RelativePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeoFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            CountryCodes=json_data.get("CountryCodes"),
            RelativePath=json_data.get("RelativePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoFilterDefinition = GeoFilterDefinition


@dataclass
class GlobalDeliveryRuleDefinition(BaseModel):
    CacheExpirationAction: Optional[Sequence["_CacheExpirationActionDefinition"]]
    CacheKeyQueryStringAction: Optional[Sequence["_CacheKeyQueryStringActionDefinition"]]
    ModifyRequestHeaderAction: Optional[Sequence["_ModifyRequestHeaderActionDefinition"]]
    ModifyResponseHeaderAction: Optional[Sequence["_ModifyResponseHeaderActionDefinition"]]
    UrlRedirectAction: Optional[Sequence["_UrlRedirectActionDefinition"]]
    UrlRewriteAction: Optional[Sequence["_UrlRewriteActionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalDeliveryRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalDeliveryRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            CacheExpirationAction=deserialize_list(json_data.get("CacheExpirationAction"), CacheExpirationActionDefinition),
            CacheKeyQueryStringAction=deserialize_list(json_data.get("CacheKeyQueryStringAction"), CacheKeyQueryStringActionDefinition),
            ModifyRequestHeaderAction=deserialize_list(json_data.get("ModifyRequestHeaderAction"), ModifyRequestHeaderActionDefinition),
            ModifyResponseHeaderAction=deserialize_list(json_data.get("ModifyResponseHeaderAction"), ModifyResponseHeaderActionDefinition),
            UrlRedirectAction=deserialize_list(json_data.get("UrlRedirectAction"), UrlRedirectActionDefinition),
            UrlRewriteAction=deserialize_list(json_data.get("UrlRewriteAction"), UrlRewriteActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalDeliveryRuleDefinition = GlobalDeliveryRuleDefinition


@dataclass
class OriginDefinition(BaseModel):
    HostName: Optional[str]
    HttpPort: Optional[float]
    HttpsPort: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OriginDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginDefinition"]:
        if not json_data:
            return None
        return cls(
            HostName=json_data.get("HostName"),
            HttpPort=json_data.get("HttpPort"),
            HttpsPort=json_data.get("HttpsPort"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginDefinition = OriginDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


