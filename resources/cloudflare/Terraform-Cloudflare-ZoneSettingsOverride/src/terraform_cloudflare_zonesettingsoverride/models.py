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
    InitialSettings: Optional[Sequence["_InitialSettings"]]
    InitialSettingsReadAt: Optional[str]
    ReadonlySettings: Optional[Sequence[str]]
    ZoneId: Optional[str]
    ZoneStatus: Optional[str]
    ZoneType: Optional[str]
    Settings: Optional[Sequence["_Settings"]]
    Minify: Optional[Sequence["_Minify2"]]
    MobileRedirect: Optional[Sequence["_MobileRedirect2"]]
    SecurityHeader: Optional[Sequence["_SecurityHeader2"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            InitialSettings=json_data.get("InitialSettings"),
            InitialSettingsReadAt=json_data.get("InitialSettingsReadAt"),
            ReadonlySettings=json_data.get("ReadonlySettings"),
            ZoneId=json_data.get("ZoneId"),
            ZoneStatus=json_data.get("ZoneStatus"),
            ZoneType=json_data.get("ZoneType"),
            Settings=json_data.get("Settings"),
            Minify=json_data.get("Minify"),
            MobileRedirect=json_data.get("MobileRedirect"),
            SecurityHeader=json_data.get("SecurityHeader"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InitialSettings:
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
    EdgeCacheTtl: Optional[float]
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
    Minify: Optional[Sequence["_Minify"]]
    Mirage: Optional[str]
    MobileRedirect: Optional[Sequence["_MobileRedirect"]]
    OpportunisticEncryption: Optional[str]
    OpportunisticOnion: Optional[str]
    OriginErrorPagePassThru: Optional[str]
    Polish: Optional[str]
    PrefetchPreload: Optional[str]
    PrivacyPass: Optional[str]
    PseudoIpv4: Optional[str]
    ResponseBuffering: Optional[str]
    RocketLoader: Optional[str]
    SecurityHeader: Optional[Sequence["_SecurityHeader"]]
    SecurityLevel: Optional[str]
    ServerSideExclude: Optional[str]
    SortQueryStringForCache: Optional[str]
    Ssl: Optional[str]
    Tls12Only: Optional[str]
    Tls13: Optional[str]
    TlsClientAuth: Optional[str]
    TrueClientIpHeader: Optional[str]
    Waf: Optional[str]
    Webp: Optional[str]
    Websockets: Optional[str]
    ZeroRtt: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InitialSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitialSettings"]:
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
            EdgeCacheTtl=json_data.get("EdgeCacheTtl"),
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
            Minify=json_data.get("Minify"),
            Mirage=json_data.get("Mirage"),
            MobileRedirect=json_data.get("MobileRedirect"),
            OpportunisticEncryption=json_data.get("OpportunisticEncryption"),
            OpportunisticOnion=json_data.get("OpportunisticOnion"),
            OriginErrorPagePassThru=json_data.get("OriginErrorPagePassThru"),
            Polish=json_data.get("Polish"),
            PrefetchPreload=json_data.get("PrefetchPreload"),
            PrivacyPass=json_data.get("PrivacyPass"),
            PseudoIpv4=json_data.get("PseudoIpv4"),
            ResponseBuffering=json_data.get("ResponseBuffering"),
            RocketLoader=json_data.get("RocketLoader"),
            SecurityHeader=json_data.get("SecurityHeader"),
            SecurityLevel=json_data.get("SecurityLevel"),
            ServerSideExclude=json_data.get("ServerSideExclude"),
            SortQueryStringForCache=json_data.get("SortQueryStringForCache"),
            Ssl=json_data.get("Ssl"),
            Tls12Only=json_data.get("Tls12Only"),
            Tls13=json_data.get("Tls13"),
            TlsClientAuth=json_data.get("TlsClientAuth"),
            TrueClientIpHeader=json_data.get("TrueClientIpHeader"),
            Waf=json_data.get("Waf"),
            Webp=json_data.get("Webp"),
            Websockets=json_data.get("Websockets"),
            ZeroRtt=json_data.get("ZeroRtt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitialSettings = InitialSettings


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


@dataclass
class MobileRedirect:
    MobileSubdomain: Optional[str]
    Status: Optional[str]
    StripUri: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_MobileRedirect"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MobileRedirect"]:
        if not json_data:
            return None
        return cls(
            MobileSubdomain=json_data.get("MobileSubdomain"),
            Status=json_data.get("Status"),
            StripUri=json_data.get("StripUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MobileRedirect = MobileRedirect


@dataclass
class SecurityHeader:
    Enabled: Optional[bool]
    IncludeSubdomains: Optional[bool]
    MaxAge: Optional[float]
    Nosniff: Optional[bool]
    Preload: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityHeader"]:
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
_SecurityHeader = SecurityHeader


@dataclass
class Settings:
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
    EdgeCacheTtl: Optional[float]
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
    Waf: Optional[str]
    Webp: Optional[str]
    Websockets: Optional[str]
    ZeroRtt: Optional[str]
    Minify: Optional[Sequence["_Minify2"]]
    MobileRedirect: Optional[Sequence["_MobileRedirect2"]]
    SecurityHeader: Optional[Sequence["_SecurityHeader2"]]

    @classmethod
    def _deserialize(
        cls: Type["_Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Settings"]:
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
            EdgeCacheTtl=json_data.get("EdgeCacheTtl"),
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
            Waf=json_data.get("Waf"),
            Webp=json_data.get("Webp"),
            Websockets=json_data.get("Websockets"),
            ZeroRtt=json_data.get("ZeroRtt"),
            Minify=json_data.get("Minify"),
            MobileRedirect=json_data.get("MobileRedirect"),
            SecurityHeader=json_data.get("SecurityHeader"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Settings = Settings


@dataclass
class Minify2:
    Css: Optional[str]
    Html: Optional[str]
    Js: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Minify2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Minify2"]:
        if not json_data:
            return None
        return cls(
            Css=json_data.get("Css"),
            Html=json_data.get("Html"),
            Js=json_data.get("Js"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Minify2 = Minify2


@dataclass
class MobileRedirect2:
    MobileSubdomain: Optional[str]
    Status: Optional[str]
    StripUri: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_MobileRedirect2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MobileRedirect2"]:
        if not json_data:
            return None
        return cls(
            MobileSubdomain=json_data.get("MobileSubdomain"),
            Status=json_data.get("Status"),
            StripUri=json_data.get("StripUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MobileRedirect2 = MobileRedirect2


@dataclass
class SecurityHeader2:
    Enabled: Optional[bool]
    IncludeSubdomains: Optional[bool]
    MaxAge: Optional[float]
    Nosniff: Optional[bool]
    Preload: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityHeader2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityHeader2"]:
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
_SecurityHeader2 = SecurityHeader2


