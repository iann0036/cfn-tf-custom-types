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
    Priority: Optional[float]
    Status: Optional[str]
    Target: Optional[str]
    ZoneId: Optional[str]
    Actions: Optional[Sequence["_Actions"]]
    ForwardingUrl: Optional[Sequence["_ForwardingUrl"]]
    Minify: Optional[Sequence["_Minify"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Priority=json_data.get("Priority"),
            Status=json_data.get("Status"),
            Target=json_data.get("Target"),
            ZoneId=json_data.get("ZoneId"),
            Actions=json_data.get("Actions"),
            ForwardingUrl=json_data.get("ForwardingUrl"),
            Minify=json_data.get("Minify"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Actions:
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
    ForwardingUrl: Optional[Sequence["_ForwardingUrl"]]
    Minify: Optional[Sequence["_Minify"]]

    @classmethod
    def _deserialize(
        cls: Type["_Actions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Actions"]:
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
            ForwardingUrl=json_data.get("ForwardingUrl"),
            Minify=json_data.get("Minify"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Actions = Actions


@dataclass
class ForwardingUrl:
    StatusCode: Optional[float]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardingUrl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardingUrl"]:
        if not json_data:
            return None
        return cls(
            StatusCode=json_data.get("StatusCode"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardingUrl = ForwardingUrl


@dataclass
class Minify:
    Css: Optional[str]
    Html: Optional[str]
    Js: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Minify"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Minify"]:
        if not json_data:
            return None
        return cls(
            Css=json_data.get("Css"),
            Html=json_data.get("Html"),
            Js=json_data.get("Js"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Minify = Minify


