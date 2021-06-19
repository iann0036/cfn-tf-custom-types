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
    Priority: Optional[float]
    Status: Optional[str]
    Target: Optional[str]
    ZoneId: Optional[str]
    Actions: Optional[Sequence["_ActionsDefinition"]]

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
            Priority=json_data.get("Priority"),
            Status=json_data.get("Status"),
            Target=json_data.get("Target"),
            ZoneId=json_data.get("ZoneId"),
            Actions=deserialize_list(json_data.get("Actions"), ActionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ActionsDefinition(BaseModel):
    AlwaysOnline: Optional[str]
    AlwaysUseHttps: Optional[bool]
    AutomaticHttpsRewrites: Optional[str]
    BrowserCacheTtl: Optional[str]
    BrowserCheck: Optional[str]
    BypassCacheOnCookie: Optional[str]
    CacheByDeviceType: Optional[str]
    CacheDeceptionArmor: Optional[str]
    CacheLevel: Optional[str]
    CacheOnCookie: Optional[str]
    DisableApps: Optional[bool]
    DisablePerformance: Optional[bool]
    DisableRailgun: Optional[bool]
    DisableSecurity: Optional[bool]
    EdgeCacheTtl: Optional[float]
    EmailObfuscation: Optional[str]
    ExplicitCacheControl: Optional[str]
    HostHeaderOverride: Optional[str]
    IpGeolocation: Optional[str]
    Mirage: Optional[str]
    OpportunisticEncryption: Optional[str]
    OriginErrorPagePassThru: Optional[str]
    Polish: Optional[str]
    ResolveOverride: Optional[str]
    RespectStrongEtag: Optional[str]
    ResponseBuffering: Optional[str]
    RocketLoader: Optional[str]
    SecurityLevel: Optional[str]
    ServerSideExclude: Optional[str]
    SortQueryStringForCache: Optional[str]
    Ssl: Optional[str]
    TrueClientIpHeader: Optional[str]
    Waf: Optional[str]
    CacheKeyFields: Optional[Sequence["_CacheKeyFieldsDefinition"]]
    CacheTtlByStatus: Optional[Sequence["_CacheTtlByStatusDefinition"]]
    ForwardingUrl: Optional[Sequence["_ForwardingUrlDefinition"]]
    Minify: Optional[Sequence["_MinifyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionsDefinition"]:
        if not json_data:
            return None
        return cls(
            AlwaysOnline=json_data.get("AlwaysOnline"),
            AlwaysUseHttps=json_data.get("AlwaysUseHttps"),
            AutomaticHttpsRewrites=json_data.get("AutomaticHttpsRewrites"),
            BrowserCacheTtl=json_data.get("BrowserCacheTtl"),
            BrowserCheck=json_data.get("BrowserCheck"),
            BypassCacheOnCookie=json_data.get("BypassCacheOnCookie"),
            CacheByDeviceType=json_data.get("CacheByDeviceType"),
            CacheDeceptionArmor=json_data.get("CacheDeceptionArmor"),
            CacheLevel=json_data.get("CacheLevel"),
            CacheOnCookie=json_data.get("CacheOnCookie"),
            DisableApps=json_data.get("DisableApps"),
            DisablePerformance=json_data.get("DisablePerformance"),
            DisableRailgun=json_data.get("DisableRailgun"),
            DisableSecurity=json_data.get("DisableSecurity"),
            EdgeCacheTtl=json_data.get("EdgeCacheTtl"),
            EmailObfuscation=json_data.get("EmailObfuscation"),
            ExplicitCacheControl=json_data.get("ExplicitCacheControl"),
            HostHeaderOverride=json_data.get("HostHeaderOverride"),
            IpGeolocation=json_data.get("IpGeolocation"),
            Mirage=json_data.get("Mirage"),
            OpportunisticEncryption=json_data.get("OpportunisticEncryption"),
            OriginErrorPagePassThru=json_data.get("OriginErrorPagePassThru"),
            Polish=json_data.get("Polish"),
            ResolveOverride=json_data.get("ResolveOverride"),
            RespectStrongEtag=json_data.get("RespectStrongEtag"),
            ResponseBuffering=json_data.get("ResponseBuffering"),
            RocketLoader=json_data.get("RocketLoader"),
            SecurityLevel=json_data.get("SecurityLevel"),
            ServerSideExclude=json_data.get("ServerSideExclude"),
            SortQueryStringForCache=json_data.get("SortQueryStringForCache"),
            Ssl=json_data.get("Ssl"),
            TrueClientIpHeader=json_data.get("TrueClientIpHeader"),
            Waf=json_data.get("Waf"),
            CacheKeyFields=deserialize_list(json_data.get("CacheKeyFields"), CacheKeyFieldsDefinition),
            CacheTtlByStatus=deserialize_list(json_data.get("CacheTtlByStatus"), CacheTtlByStatusDefinition),
            ForwardingUrl=deserialize_list(json_data.get("ForwardingUrl"), ForwardingUrlDefinition),
            Minify=deserialize_list(json_data.get("Minify"), MinifyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionsDefinition = ActionsDefinition


@dataclass
class CacheKeyFieldsDefinition(BaseModel):
    Cookie: Optional[Sequence["_CookieDefinition"]]
    Header: Optional[Sequence["_HeaderDefinition"]]
    Host: Optional[Sequence["_HostDefinition"]]
    QueryString: Optional[Sequence["_QueryStringDefinition"]]
    User: Optional[Sequence["_UserDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CacheKeyFieldsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheKeyFieldsDefinition"]:
        if not json_data:
            return None
        return cls(
            Cookie=deserialize_list(json_data.get("Cookie"), CookieDefinition),
            Header=deserialize_list(json_data.get("Header"), HeaderDefinition),
            Host=deserialize_list(json_data.get("Host"), HostDefinition),
            QueryString=deserialize_list(json_data.get("QueryString"), QueryStringDefinition),
            User=deserialize_list(json_data.get("User"), UserDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheKeyFieldsDefinition = CacheKeyFieldsDefinition


@dataclass
class CookieDefinition(BaseModel):
    CheckPresence: Optional[Sequence[str]]
    Include: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CookieDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookieDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckPresence=json_data.get("CheckPresence"),
            Include=json_data.get("Include"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CookieDefinition = CookieDefinition


@dataclass
class HeaderDefinition(BaseModel):
    CheckPresence: Optional[Sequence[str]]
    Exclude: Optional[Sequence[str]]
    Include: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckPresence=json_data.get("CheckPresence"),
            Exclude=json_data.get("Exclude"),
            Include=json_data.get("Include"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderDefinition = HeaderDefinition


@dataclass
class HostDefinition(BaseModel):
    Resolved: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_HostDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostDefinition"]:
        if not json_data:
            return None
        return cls(
            Resolved=json_data.get("Resolved"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostDefinition = HostDefinition


@dataclass
class QueryStringDefinition(BaseModel):
    Exclude: Optional[Sequence[str]]
    Ignore: Optional[bool]
    Include: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryStringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryStringDefinition"]:
        if not json_data:
            return None
        return cls(
            Exclude=json_data.get("Exclude"),
            Ignore=json_data.get("Ignore"),
            Include=json_data.get("Include"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryStringDefinition = QueryStringDefinition


@dataclass
class UserDefinition(BaseModel):
    DeviceType: Optional[bool]
    Geo: Optional[bool]
    Lang: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_UserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserDefinition"]:
        if not json_data:
            return None
        return cls(
            DeviceType=json_data.get("DeviceType"),
            Geo=json_data.get("Geo"),
            Lang=json_data.get("Lang"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserDefinition = UserDefinition


@dataclass
class CacheTtlByStatusDefinition(BaseModel):
    Codes: Optional[str]
    Ttl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CacheTtlByStatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheTtlByStatusDefinition"]:
        if not json_data:
            return None
        return cls(
            Codes=json_data.get("Codes"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheTtlByStatusDefinition = CacheTtlByStatusDefinition


@dataclass
class ForwardingUrlDefinition(BaseModel):
    StatusCode: Optional[float]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardingUrlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardingUrlDefinition"]:
        if not json_data:
            return None
        return cls(
            StatusCode=json_data.get("StatusCode"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardingUrlDefinition = ForwardingUrlDefinition


@dataclass
class MinifyDefinition(BaseModel):
    Css: Optional[str]
    Html: Optional[str]
    Js: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MinifyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MinifyDefinition"]:
        if not json_data:
            return None
        return cls(
            Css=json_data.get("Css"),
            Html=json_data.get("Html"),
            Js=json_data.get("Js"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MinifyDefinition = MinifyDefinition


