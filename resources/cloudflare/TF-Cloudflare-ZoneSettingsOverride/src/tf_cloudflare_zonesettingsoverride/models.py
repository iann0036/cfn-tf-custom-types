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
    InitialSettings: Optional[Sequence["_InitialSettingsDefinition4"]]
    InitialSettingsReadAt: Optional[str]
    ReadonlySettings: Optional[Sequence[str]]
    ZoneId: Optional[str]
    ZoneStatus: Optional[str]
    ZoneType: Optional[str]
    Settings: Optional[Sequence["_SettingsDefinition"]]

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
            InitialSettings=deserialize_list(json_data.get("InitialSettings"), InitialSettingsDefinition4),
            InitialSettingsReadAt=json_data.get("InitialSettingsReadAt"),
            ReadonlySettings=json_data.get("ReadonlySettings"),
            ZoneId=json_data.get("ZoneId"),
            ZoneStatus=json_data.get("ZoneStatus"),
            ZoneType=json_data.get("ZoneType"),
            Settings=deserialize_list(json_data.get("Settings"), SettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InitialSettingsDefinition4(BaseModel):
    AlwaysOnline: Optional[str]
    AlwaysUseHttps: Optional[str]
    AutomaticHttpsRewrites: Optional[str]
    Brotli: Optional[str]
    BrowserCacheTtl: Optional[float]
    BrowserCheck: Optional[str]
    CacheLevel: Optional[str]
    ChallengeTtl: Optional[float]
    CnameFlattening: Optional[str]
    DevelopmentMode: Optional[str]
    EmailObfuscation: Optional[str]
    H2Prioritization: Optional[str]
    HotlinkProtection: Optional[str]
    Http2: Optional[str]
    Http3: Optional[str]
    ImageResizing: Optional[str]
    IpGeolocation: Optional[str]
    Ipv6: Optional[str]
    MaxUpload: Optional[float]
    MinTlsVersion: Optional[str]
    Minify: Optional[Sequence["_InitialSettingsDefinition"]]
    Mirage: Optional[str]
    MobileRedirect: Optional[Sequence["_InitialSettingsDefinition2"]]
    OpportunisticEncryption: Optional[str]
    OpportunisticOnion: Optional[str]
    OriginErrorPagePassThru: Optional[str]
    Polish: Optional[str]
    PrefetchPreload: Optional[str]
    PrivacyPass: Optional[str]
    PseudoIpv4: Optional[str]
    ResponseBuffering: Optional[str]
    RocketLoader: Optional[str]
    SecurityHeader: Optional[Sequence["_InitialSettingsDefinition3"]]
    SecurityLevel: Optional[str]
    ServerSideExclude: Optional[str]
    SortQueryStringForCache: Optional[str]
    Ssl: Optional[str]
    Tls12Only: Optional[str]
    Tls13: Optional[str]
    TlsClientAuth: Optional[str]
    TrueClientIpHeader: Optional[str]
    UniversalSsl: Optional[str]
    Waf: Optional[str]
    Webp: Optional[str]
    Websockets: Optional[str]
    ZeroRtt: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InitialSettingsDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitialSettingsDefinition4"]:
        if not json_data:
            return None
        return cls(
            AlwaysOnline=json_data.get("AlwaysOnline"),
            AlwaysUseHttps=json_data.get("AlwaysUseHttps"),
            AutomaticHttpsRewrites=json_data.get("AutomaticHttpsRewrites"),
            Brotli=json_data.get("Brotli"),
            BrowserCacheTtl=json_data.get("BrowserCacheTtl"),
            BrowserCheck=json_data.get("BrowserCheck"),
            CacheLevel=json_data.get("CacheLevel"),
            ChallengeTtl=json_data.get("ChallengeTtl"),
            CnameFlattening=json_data.get("CnameFlattening"),
            DevelopmentMode=json_data.get("DevelopmentMode"),
            EmailObfuscation=json_data.get("EmailObfuscation"),
            H2Prioritization=json_data.get("H2Prioritization"),
            HotlinkProtection=json_data.get("HotlinkProtection"),
            Http2=json_data.get("Http2"),
            Http3=json_data.get("Http3"),
            ImageResizing=json_data.get("ImageResizing"),
            IpGeolocation=json_data.get("IpGeolocation"),
            Ipv6=json_data.get("Ipv6"),
            MaxUpload=json_data.get("MaxUpload"),
            MinTlsVersion=json_data.get("MinTlsVersion"),
            Minify=deserialize_list(json_data.get("Minify"), InitialSettingsDefinition),
            Mirage=json_data.get("Mirage"),
            MobileRedirect=deserialize_list(json_data.get("MobileRedirect"), InitialSettingsDefinition2),
            OpportunisticEncryption=json_data.get("OpportunisticEncryption"),
            OpportunisticOnion=json_data.get("OpportunisticOnion"),
            OriginErrorPagePassThru=json_data.get("OriginErrorPagePassThru"),
            Polish=json_data.get("Polish"),
            PrefetchPreload=json_data.get("PrefetchPreload"),
            PrivacyPass=json_data.get("PrivacyPass"),
            PseudoIpv4=json_data.get("PseudoIpv4"),
            ResponseBuffering=json_data.get("ResponseBuffering"),
            RocketLoader=json_data.get("RocketLoader"),
            SecurityHeader=deserialize_list(json_data.get("SecurityHeader"), InitialSettingsDefinition3),
            SecurityLevel=json_data.get("SecurityLevel"),
            ServerSideExclude=json_data.get("ServerSideExclude"),
            SortQueryStringForCache=json_data.get("SortQueryStringForCache"),
            Ssl=json_data.get("Ssl"),
            Tls12Only=json_data.get("Tls12Only"),
            Tls13=json_data.get("Tls13"),
            TlsClientAuth=json_data.get("TlsClientAuth"),
            TrueClientIpHeader=json_data.get("TrueClientIpHeader"),
            UniversalSsl=json_data.get("UniversalSsl"),
            Waf=json_data.get("Waf"),
            Webp=json_data.get("Webp"),
            Websockets=json_data.get("Websockets"),
            ZeroRtt=json_data.get("ZeroRtt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitialSettingsDefinition4 = InitialSettingsDefinition4


@dataclass
class InitialSettingsDefinition(BaseModel):
    Css: Optional[str]
    Html: Optional[str]
    Js: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InitialSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitialSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Css=json_data.get("Css"),
            Html=json_data.get("Html"),
            Js=json_data.get("Js"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitialSettingsDefinition = InitialSettingsDefinition


@dataclass
class InitialSettingsDefinition2(BaseModel):
    MobileSubdomain: Optional[str]
    Status: Optional[str]
    StripUri: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_InitialSettingsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitialSettingsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MobileSubdomain=json_data.get("MobileSubdomain"),
            Status=json_data.get("Status"),
            StripUri=json_data.get("StripUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitialSettingsDefinition2 = InitialSettingsDefinition2


@dataclass
class InitialSettingsDefinition3(BaseModel):
    Enabled: Optional[bool]
    IncludeSubdomains: Optional[bool]
    MaxAge: Optional[float]
    Nosniff: Optional[bool]
    Preload: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_InitialSettingsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitialSettingsDefinition3"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            IncludeSubdomains=json_data.get("IncludeSubdomains"),
            MaxAge=json_data.get("MaxAge"),
            Nosniff=json_data.get("Nosniff"),
            Preload=json_data.get("Preload"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitialSettingsDefinition3 = InitialSettingsDefinition3


@dataclass
class SettingsDefinition(BaseModel):
    AlwaysOnline: Optional[str]
    AlwaysUseHttps: Optional[str]
    AutomaticHttpsRewrites: Optional[str]
    Brotli: Optional[str]
    BrowserCacheTtl: Optional[float]
    BrowserCheck: Optional[str]
    CacheLevel: Optional[str]
    ChallengeTtl: Optional[float]
    CnameFlattening: Optional[str]
    DevelopmentMode: Optional[str]
    EmailObfuscation: Optional[str]
    H2Prioritization: Optional[str]
    HotlinkProtection: Optional[str]
    Http2: Optional[str]
    Http3: Optional[str]
    ImageResizing: Optional[str]
    IpGeolocation: Optional[str]
    Ipv6: Optional[str]
    MaxUpload: Optional[float]
    MinTlsVersion: Optional[str]
    Mirage: Optional[str]
    OpportunisticEncryption: Optional[str]
    OpportunisticOnion: Optional[str]
    OriginErrorPagePassThru: Optional[str]
    Polish: Optional[str]
    PrefetchPreload: Optional[str]
    PrivacyPass: Optional[str]
    PseudoIpv4: Optional[str]
    ResponseBuffering: Optional[str]
    RocketLoader: Optional[str]
    SecurityLevel: Optional[str]
    ServerSideExclude: Optional[str]
    SortQueryStringForCache: Optional[str]
    Ssl: Optional[str]
    Tls12Only: Optional[str]
    Tls13: Optional[str]
    TlsClientAuth: Optional[str]
    TrueClientIpHeader: Optional[str]
    UniversalSsl: Optional[str]
    Waf: Optional[str]
    Webp: Optional[str]
    Websockets: Optional[str]
    ZeroRtt: Optional[str]
    Minify: Optional[Sequence["_MinifyDefinition"]]
    MobileRedirect: Optional[Sequence["_MobileRedirectDefinition"]]
    SecurityHeader: Optional[Sequence["_SecurityHeaderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AlwaysOnline=json_data.get("AlwaysOnline"),
            AlwaysUseHttps=json_data.get("AlwaysUseHttps"),
            AutomaticHttpsRewrites=json_data.get("AutomaticHttpsRewrites"),
            Brotli=json_data.get("Brotli"),
            BrowserCacheTtl=json_data.get("BrowserCacheTtl"),
            BrowserCheck=json_data.get("BrowserCheck"),
            CacheLevel=json_data.get("CacheLevel"),
            ChallengeTtl=json_data.get("ChallengeTtl"),
            CnameFlattening=json_data.get("CnameFlattening"),
            DevelopmentMode=json_data.get("DevelopmentMode"),
            EmailObfuscation=json_data.get("EmailObfuscation"),
            H2Prioritization=json_data.get("H2Prioritization"),
            HotlinkProtection=json_data.get("HotlinkProtection"),
            Http2=json_data.get("Http2"),
            Http3=json_data.get("Http3"),
            ImageResizing=json_data.get("ImageResizing"),
            IpGeolocation=json_data.get("IpGeolocation"),
            Ipv6=json_data.get("Ipv6"),
            MaxUpload=json_data.get("MaxUpload"),
            MinTlsVersion=json_data.get("MinTlsVersion"),
            Mirage=json_data.get("Mirage"),
            OpportunisticEncryption=json_data.get("OpportunisticEncryption"),
            OpportunisticOnion=json_data.get("OpportunisticOnion"),
            OriginErrorPagePassThru=json_data.get("OriginErrorPagePassThru"),
            Polish=json_data.get("Polish"),
            PrefetchPreload=json_data.get("PrefetchPreload"),
            PrivacyPass=json_data.get("PrivacyPass"),
            PseudoIpv4=json_data.get("PseudoIpv4"),
            ResponseBuffering=json_data.get("ResponseBuffering"),
            RocketLoader=json_data.get("RocketLoader"),
            SecurityLevel=json_data.get("SecurityLevel"),
            ServerSideExclude=json_data.get("ServerSideExclude"),
            SortQueryStringForCache=json_data.get("SortQueryStringForCache"),
            Ssl=json_data.get("Ssl"),
            Tls12Only=json_data.get("Tls12Only"),
            Tls13=json_data.get("Tls13"),
            TlsClientAuth=json_data.get("TlsClientAuth"),
            TrueClientIpHeader=json_data.get("TrueClientIpHeader"),
            UniversalSsl=json_data.get("UniversalSsl"),
            Waf=json_data.get("Waf"),
            Webp=json_data.get("Webp"),
            Websockets=json_data.get("Websockets"),
            ZeroRtt=json_data.get("ZeroRtt"),
            Minify=deserialize_list(json_data.get("Minify"), MinifyDefinition),
            MobileRedirect=deserialize_list(json_data.get("MobileRedirect"), MobileRedirectDefinition),
            SecurityHeader=deserialize_list(json_data.get("SecurityHeader"), SecurityHeaderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SettingsDefinition = SettingsDefinition


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


@dataclass
class MobileRedirectDefinition(BaseModel):
    MobileSubdomain: Optional[str]
    Status: Optional[str]
    StripUri: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_MobileRedirectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MobileRedirectDefinition"]:
        if not json_data:
            return None
        return cls(
            MobileSubdomain=json_data.get("MobileSubdomain"),
            Status=json_data.get("Status"),
            StripUri=json_data.get("StripUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MobileRedirectDefinition = MobileRedirectDefinition


@dataclass
class SecurityHeaderDefinition(BaseModel):
    Enabled: Optional[bool]
    IncludeSubdomains: Optional[bool]
    MaxAge: Optional[float]
    Nosniff: Optional[bool]
    Preload: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityHeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityHeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            IncludeSubdomains=json_data.get("IncludeSubdomains"),
            MaxAge=json_data.get("MaxAge"),
            Nosniff=json_data.get("Nosniff"),
            Preload=json_data.get("Preload"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityHeaderDefinition = SecurityHeaderDefinition


