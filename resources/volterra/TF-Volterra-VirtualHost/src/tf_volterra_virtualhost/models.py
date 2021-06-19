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
    AddLocation: Optional[bool]
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    AppendServerName: Optional[str]
    CustomErrors: Optional[Sequence["_CustomErrorsDefinition"]]
    DefaultHeader: Optional[bool]
    Description: Optional[str]
    Disable: Optional[bool]
    DisableDefaultErrorPages: Optional[bool]
    DisableDnsResolve: Optional[bool]
    Domains: Optional[Sequence[str]]
    Id: Optional[str]
    IdleTimeout: Optional[float]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    MaxRequestHeaderSize: Optional[float]
    Name: Optional[str]
    Namespace: Optional[str]
    NoAuthentication: Optional[bool]
    NoChallenge: Optional[bool]
    PassThrough: Optional[bool]
    Proxy: Optional[str]
    RequestHeadersToRemove: Optional[Sequence[str]]
    ResponseHeadersToRemove: Optional[Sequence[str]]
    ServerName: Optional[str]
    AdvertisePolicies: Optional[Sequence["_AdvertisePoliciesDefinition"]]
    Authentication: Optional[Sequence["_AuthenticationDefinition"]]
    BufferPolicy: Optional[Sequence["_BufferPolicyDefinition"]]
    CaptchaChallenge: Optional[Sequence["_CaptchaChallengeDefinition"]]
    CompressionParams: Optional[Sequence["_CompressionParamsDefinition"]]
    CorsPolicy: Optional[Sequence["_CorsPolicyDefinition"]]
    DynamicReverseProxy: Optional[Sequence["_DynamicReverseProxyDefinition"]]
    JsChallenge: Optional[Sequence["_JsChallengeDefinition"]]
    RateLimiter: Optional[Sequence["_RateLimiterDefinition"]]
    RateLimiterAllowedPrefixes: Optional[Sequence["_RateLimiterAllowedPrefixesDefinition"]]
    RequestHeadersToAdd: Optional[Sequence["_RequestHeadersToAddDefinition"]]
    ResponseHeadersToAdd: Optional[Sequence["_ResponseHeadersToAddDefinition"]]
    RetryPolicy: Optional[Sequence["_RetryPolicyDefinition"]]
    Routes: Optional[Sequence["_RoutesDefinition"]]
    TemporaryUserBlocking: Optional[Sequence["_TemporaryUserBlockingDefinition"]]
    TlsParameters: Optional[Sequence["_TlsParametersDefinition"]]
    UserIdentification: Optional[Sequence["_UserIdentificationDefinition"]]
    WafType: Optional[Sequence["_WafTypeDefinition"]]

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
            AddLocation=json_data.get("AddLocation"),
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            AppendServerName=json_data.get("AppendServerName"),
            CustomErrors=deserialize_list(json_data.get("CustomErrors"), CustomErrorsDefinition),
            DefaultHeader=json_data.get("DefaultHeader"),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            DisableDefaultErrorPages=json_data.get("DisableDefaultErrorPages"),
            DisableDnsResolve=json_data.get("DisableDnsResolve"),
            Domains=json_data.get("Domains"),
            Id=json_data.get("Id"),
            IdleTimeout=json_data.get("IdleTimeout"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            MaxRequestHeaderSize=json_data.get("MaxRequestHeaderSize"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            NoAuthentication=json_data.get("NoAuthentication"),
            NoChallenge=json_data.get("NoChallenge"),
            PassThrough=json_data.get("PassThrough"),
            Proxy=json_data.get("Proxy"),
            RequestHeadersToRemove=json_data.get("RequestHeadersToRemove"),
            ResponseHeadersToRemove=json_data.get("ResponseHeadersToRemove"),
            ServerName=json_data.get("ServerName"),
            AdvertisePolicies=deserialize_list(json_data.get("AdvertisePolicies"), AdvertisePoliciesDefinition),
            Authentication=deserialize_list(json_data.get("Authentication"), AuthenticationDefinition),
            BufferPolicy=deserialize_list(json_data.get("BufferPolicy"), BufferPolicyDefinition),
            CaptchaChallenge=deserialize_list(json_data.get("CaptchaChallenge"), CaptchaChallengeDefinition),
            CompressionParams=deserialize_list(json_data.get("CompressionParams"), CompressionParamsDefinition),
            CorsPolicy=deserialize_list(json_data.get("CorsPolicy"), CorsPolicyDefinition),
            DynamicReverseProxy=deserialize_list(json_data.get("DynamicReverseProxy"), DynamicReverseProxyDefinition),
            JsChallenge=deserialize_list(json_data.get("JsChallenge"), JsChallengeDefinition),
            RateLimiter=deserialize_list(json_data.get("RateLimiter"), RateLimiterDefinition),
            RateLimiterAllowedPrefixes=deserialize_list(json_data.get("RateLimiterAllowedPrefixes"), RateLimiterAllowedPrefixesDefinition),
            RequestHeadersToAdd=deserialize_list(json_data.get("RequestHeadersToAdd"), RequestHeadersToAddDefinition),
            ResponseHeadersToAdd=deserialize_list(json_data.get("ResponseHeadersToAdd"), ResponseHeadersToAddDefinition),
            RetryPolicy=deserialize_list(json_data.get("RetryPolicy"), RetryPolicyDefinition),
            Routes=deserialize_list(json_data.get("Routes"), RoutesDefinition),
            TemporaryUserBlocking=deserialize_list(json_data.get("TemporaryUserBlocking"), TemporaryUserBlockingDefinition),
            TlsParameters=deserialize_list(json_data.get("TlsParameters"), TlsParametersDefinition),
            UserIdentification=deserialize_list(json_data.get("UserIdentification"), UserIdentificationDefinition),
            WafType=deserialize_list(json_data.get("WafType"), WafTypeDefinition),
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
class CustomErrorsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomErrorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomErrorsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomErrorsDefinition = CustomErrorsDefinition


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
class AdvertisePoliciesDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdvertisePoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvertisePoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvertisePoliciesDefinition = AdvertisePoliciesDefinition


@dataclass
class AuthenticationDefinition(BaseModel):
    RedirectDynamic: Optional[bool]
    RedirectUrl: Optional[str]
    UseAuthObjectConfig: Optional[bool]
    AuthConfig: Optional[Sequence["_AuthConfigDefinition"]]
    CookieParams: Optional[Sequence["_CookieParamsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationDefinition"]:
        if not json_data:
            return None
        return cls(
            RedirectDynamic=json_data.get("RedirectDynamic"),
            RedirectUrl=json_data.get("RedirectUrl"),
            UseAuthObjectConfig=json_data.get("UseAuthObjectConfig"),
            AuthConfig=deserialize_list(json_data.get("AuthConfig"), AuthConfigDefinition),
            CookieParams=deserialize_list(json_data.get("CookieParams"), CookieParamsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationDefinition = AuthenticationDefinition


@dataclass
class AuthConfigDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthConfigDefinition = AuthConfigDefinition


@dataclass
class CookieParamsDefinition(BaseModel):
    CookieExpiry: Optional[float]
    CookieRefreshInterval: Optional[float]
    SessionExpiry: Optional[float]
    AuthHmac: Optional[Sequence["_AuthHmacDefinition"]]
    KmsKeyHmac: Optional[Sequence["_KmsKeyHmacDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CookieParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookieParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            CookieExpiry=json_data.get("CookieExpiry"),
            CookieRefreshInterval=json_data.get("CookieRefreshInterval"),
            SessionExpiry=json_data.get("SessionExpiry"),
            AuthHmac=deserialize_list(json_data.get("AuthHmac"), AuthHmacDefinition),
            KmsKeyHmac=deserialize_list(json_data.get("KmsKeyHmac"), KmsKeyHmacDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CookieParamsDefinition = CookieParamsDefinition


@dataclass
class AuthHmacDefinition(BaseModel):
    PrimKeyExpiry: Optional[str]
    SecKeyExpiry: Optional[str]
    PrimKey: Optional[Sequence["_PrimKeyDefinition"]]
    SecKey: Optional[Sequence["_SecKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthHmacDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthHmacDefinition"]:
        if not json_data:
            return None
        return cls(
            PrimKeyExpiry=json_data.get("PrimKeyExpiry"),
            SecKeyExpiry=json_data.get("SecKeyExpiry"),
            PrimKey=deserialize_list(json_data.get("PrimKey"), PrimKeyDefinition),
            SecKey=deserialize_list(json_data.get("SecKey"), SecKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthHmacDefinition = AuthHmacDefinition


@dataclass
class PrimKeyDefinition(BaseModel):
    SecretEncodingType: Optional[str]
    BlindfoldSecretInfo: Optional[Sequence["_BlindfoldSecretInfoDefinition"]]
    BlindfoldSecretInfoInternal: Optional[Sequence["_BlindfoldSecretInfoInternalDefinition"]]
    ClearSecretInfo: Optional[Sequence["_ClearSecretInfoDefinition"]]
    VaultSecretInfo: Optional[Sequence["_VaultSecretInfoDefinition"]]
    WingmanSecretInfo: Optional[Sequence["_WingmanSecretInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrimKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrimKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            SecretEncodingType=json_data.get("SecretEncodingType"),
            BlindfoldSecretInfo=deserialize_list(json_data.get("BlindfoldSecretInfo"), BlindfoldSecretInfoDefinition),
            BlindfoldSecretInfoInternal=deserialize_list(json_data.get("BlindfoldSecretInfoInternal"), BlindfoldSecretInfoInternalDefinition),
            ClearSecretInfo=deserialize_list(json_data.get("ClearSecretInfo"), ClearSecretInfoDefinition),
            VaultSecretInfo=deserialize_list(json_data.get("VaultSecretInfo"), VaultSecretInfoDefinition),
            WingmanSecretInfo=deserialize_list(json_data.get("WingmanSecretInfo"), WingmanSecretInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrimKeyDefinition = PrimKeyDefinition


@dataclass
class BlindfoldSecretInfoDefinition(BaseModel):
    DecryptionProvider: Optional[str]
    Location: Optional[str]
    StoreProvider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlindfoldSecretInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlindfoldSecretInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            DecryptionProvider=json_data.get("DecryptionProvider"),
            Location=json_data.get("Location"),
            StoreProvider=json_data.get("StoreProvider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlindfoldSecretInfoDefinition = BlindfoldSecretInfoDefinition


@dataclass
class BlindfoldSecretInfoInternalDefinition(BaseModel):
    DecryptionProvider: Optional[str]
    Location: Optional[str]
    StoreProvider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlindfoldSecretInfoInternalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlindfoldSecretInfoInternalDefinition"]:
        if not json_data:
            return None
        return cls(
            DecryptionProvider=json_data.get("DecryptionProvider"),
            Location=json_data.get("Location"),
            StoreProvider=json_data.get("StoreProvider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlindfoldSecretInfoInternalDefinition = BlindfoldSecretInfoInternalDefinition


@dataclass
class ClearSecretInfoDefinition(BaseModel):
    Provider: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClearSecretInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClearSecretInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Provider=json_data.get("Provider"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClearSecretInfoDefinition = ClearSecretInfoDefinition


@dataclass
class VaultSecretInfoDefinition(BaseModel):
    Key: Optional[str]
    Location: Optional[str]
    Provider: Optional[str]
    SecretEncoding: Optional[str]
    Version: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VaultSecretInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VaultSecretInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Location=json_data.get("Location"),
            Provider=json_data.get("Provider"),
            SecretEncoding=json_data.get("SecretEncoding"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VaultSecretInfoDefinition = VaultSecretInfoDefinition


@dataclass
class WingmanSecretInfoDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WingmanSecretInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WingmanSecretInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WingmanSecretInfoDefinition = WingmanSecretInfoDefinition


@dataclass
class SecKeyDefinition(BaseModel):
    SecretEncodingType: Optional[str]
    BlindfoldSecretInfo: Optional[Sequence["_BlindfoldSecretInfoDefinition"]]
    BlindfoldSecretInfoInternal: Optional[Sequence["_BlindfoldSecretInfoInternalDefinition"]]
    ClearSecretInfo: Optional[Sequence["_ClearSecretInfoDefinition"]]
    VaultSecretInfo: Optional[Sequence["_VaultSecretInfoDefinition"]]
    WingmanSecretInfo: Optional[Sequence["_WingmanSecretInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            SecretEncodingType=json_data.get("SecretEncodingType"),
            BlindfoldSecretInfo=deserialize_list(json_data.get("BlindfoldSecretInfo"), BlindfoldSecretInfoDefinition),
            BlindfoldSecretInfoInternal=deserialize_list(json_data.get("BlindfoldSecretInfoInternal"), BlindfoldSecretInfoInternalDefinition),
            ClearSecretInfo=deserialize_list(json_data.get("ClearSecretInfo"), ClearSecretInfoDefinition),
            VaultSecretInfo=deserialize_list(json_data.get("VaultSecretInfo"), VaultSecretInfoDefinition),
            WingmanSecretInfo=deserialize_list(json_data.get("WingmanSecretInfo"), WingmanSecretInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecKeyDefinition = SecKeyDefinition


@dataclass
class KmsKeyHmacDefinition(BaseModel):
    AuthHmacKms: Optional[Sequence["_AuthHmacKmsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_KmsKeyHmacDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KmsKeyHmacDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthHmacKms=deserialize_list(json_data.get("AuthHmacKms"), AuthHmacKmsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_KmsKeyHmacDefinition = KmsKeyHmacDefinition


@dataclass
class AuthHmacKmsDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthHmacKmsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthHmacKmsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthHmacKmsDefinition = AuthHmacKmsDefinition


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
class CaptchaChallengeDefinition(BaseModel):
    CookieExpiry: Optional[float]
    CustomPage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CaptchaChallengeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaptchaChallengeDefinition"]:
        if not json_data:
            return None
        return cls(
            CookieExpiry=json_data.get("CookieExpiry"),
            CustomPage=json_data.get("CustomPage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaptchaChallengeDefinition = CaptchaChallengeDefinition


@dataclass
class CompressionParamsDefinition(BaseModel):
    ContentLength: Optional[float]
    ContentType: Optional[Sequence[str]]
    DisableOnEtagHeader: Optional[bool]
    RemoveAcceptEncodingHeader: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CompressionParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CompressionParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentLength=json_data.get("ContentLength"),
            ContentType=json_data.get("ContentType"),
            DisableOnEtagHeader=json_data.get("DisableOnEtagHeader"),
            RemoveAcceptEncodingHeader=json_data.get("RemoveAcceptEncodingHeader"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CompressionParamsDefinition = CompressionParamsDefinition


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
class DynamicReverseProxyDefinition(BaseModel):
    ConnectionTimeout: Optional[float]
    ResolutionNetworkType: Optional[str]
    ResolveEndpointDynamically: Optional[bool]
    ResolutionNetwork: Optional[Sequence["_ResolutionNetworkDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicReverseProxyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicReverseProxyDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionTimeout=json_data.get("ConnectionTimeout"),
            ResolutionNetworkType=json_data.get("ResolutionNetworkType"),
            ResolveEndpointDynamically=json_data.get("ResolveEndpointDynamically"),
            ResolutionNetwork=deserialize_list(json_data.get("ResolutionNetwork"), ResolutionNetworkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicReverseProxyDefinition = DynamicReverseProxyDefinition


@dataclass
class ResolutionNetworkDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResolutionNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResolutionNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResolutionNetworkDefinition = ResolutionNetworkDefinition


@dataclass
class JsChallengeDefinition(BaseModel):
    CookieExpiry: Optional[float]
    CustomPage: Optional[str]
    JsScriptDelay: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_JsChallengeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsChallengeDefinition"]:
        if not json_data:
            return None
        return cls(
            CookieExpiry=json_data.get("CookieExpiry"),
            CustomPage=json_data.get("CustomPage"),
            JsScriptDelay=json_data.get("JsScriptDelay"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsChallengeDefinition = JsChallengeDefinition


@dataclass
class RateLimiterDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimiterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimiterDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimiterDefinition = RateLimiterDefinition


@dataclass
class RateLimiterAllowedPrefixesDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimiterAllowedPrefixesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimiterAllowedPrefixesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimiterAllowedPrefixesDefinition = RateLimiterAllowedPrefixesDefinition


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
class RoutesDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutesDefinition = RoutesDefinition


@dataclass
class TemporaryUserBlockingDefinition(BaseModel):
    CustomPage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TemporaryUserBlockingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemporaryUserBlockingDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomPage=json_data.get("CustomPage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemporaryUserBlockingDefinition = TemporaryUserBlockingDefinition


@dataclass
class TlsParametersDefinition(BaseModel):
    RequireClientCertificate: Optional[bool]
    CommonParams: Optional[Sequence["_CommonParamsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TlsParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            RequireClientCertificate=json_data.get("RequireClientCertificate"),
            CommonParams=deserialize_list(json_data.get("CommonParams"), CommonParamsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsParametersDefinition = TlsParametersDefinition


@dataclass
class CommonParamsDefinition(BaseModel):
    CipherSuites: Optional[Sequence[str]]
    MaximumProtocolVersion: Optional[str]
    MinimumProtocolVersion: Optional[str]
    TrustedCaUrl: Optional[str]
    TlsCertificates: Optional[Sequence["_TlsCertificatesDefinition"]]
    ValidationParams: Optional[Sequence["_ValidationParamsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CommonParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CommonParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            CipherSuites=json_data.get("CipherSuites"),
            MaximumProtocolVersion=json_data.get("MaximumProtocolVersion"),
            MinimumProtocolVersion=json_data.get("MinimumProtocolVersion"),
            TrustedCaUrl=json_data.get("TrustedCaUrl"),
            TlsCertificates=deserialize_list(json_data.get("TlsCertificates"), TlsCertificatesDefinition),
            ValidationParams=deserialize_list(json_data.get("ValidationParams"), ValidationParamsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CommonParamsDefinition = CommonParamsDefinition


@dataclass
class TlsCertificatesDefinition(BaseModel):
    CertificateUrl: Optional[str]
    Description: Optional[str]
    PrivateKey: Optional[Sequence["_PrivateKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TlsCertificatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsCertificatesDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateUrl=json_data.get("CertificateUrl"),
            Description=json_data.get("Description"),
            PrivateKey=deserialize_list(json_data.get("PrivateKey"), PrivateKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsCertificatesDefinition = TlsCertificatesDefinition


@dataclass
class PrivateKeyDefinition(BaseModel):
    SecretEncodingType: Optional[str]
    BlindfoldSecretInfo: Optional[Sequence["_BlindfoldSecretInfoDefinition"]]
    BlindfoldSecretInfoInternal: Optional[Sequence["_BlindfoldSecretInfoInternalDefinition"]]
    ClearSecretInfo: Optional[Sequence["_ClearSecretInfoDefinition"]]
    VaultSecretInfo: Optional[Sequence["_VaultSecretInfoDefinition"]]
    WingmanSecretInfo: Optional[Sequence["_WingmanSecretInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            SecretEncodingType=json_data.get("SecretEncodingType"),
            BlindfoldSecretInfo=deserialize_list(json_data.get("BlindfoldSecretInfo"), BlindfoldSecretInfoDefinition),
            BlindfoldSecretInfoInternal=deserialize_list(json_data.get("BlindfoldSecretInfoInternal"), BlindfoldSecretInfoInternalDefinition),
            ClearSecretInfo=deserialize_list(json_data.get("ClearSecretInfo"), ClearSecretInfoDefinition),
            VaultSecretInfo=deserialize_list(json_data.get("VaultSecretInfo"), VaultSecretInfoDefinition),
            WingmanSecretInfo=deserialize_list(json_data.get("WingmanSecretInfo"), WingmanSecretInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateKeyDefinition = PrivateKeyDefinition


@dataclass
class ValidationParamsDefinition(BaseModel):
    SkipHostnameVerification: Optional[bool]
    TrustedCaUrl: Optional[str]
    UseVolterraTrustedCaUrl: Optional[bool]
    VerifySubjectAltNames: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ValidationParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValidationParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            SkipHostnameVerification=json_data.get("SkipHostnameVerification"),
            TrustedCaUrl=json_data.get("TrustedCaUrl"),
            UseVolterraTrustedCaUrl=json_data.get("UseVolterraTrustedCaUrl"),
            VerifySubjectAltNames=json_data.get("VerifySubjectAltNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValidationParamsDefinition = ValidationParamsDefinition


@dataclass
class UserIdentificationDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserIdentificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserIdentificationDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserIdentificationDefinition = UserIdentificationDefinition


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


