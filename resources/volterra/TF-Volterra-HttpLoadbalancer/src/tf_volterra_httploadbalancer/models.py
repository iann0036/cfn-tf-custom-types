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
    AdvertiseOnPublicDefaultVip: Optional[bool]
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Description: Optional[str]
    Disable: Optional[bool]
    DisableRateLimit: Optional[bool]
    DisableWaf: Optional[bool]
    DoNotAdvertise: Optional[bool]
    Domains: Optional[Sequence[str]]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    LeastActive: Optional[bool]
    Name: Optional[str]
    Namespace: Optional[str]
    NoChallenge: Optional[bool]
    NoServicePolicies: Optional[bool]
    Random: Optional[bool]
    RoundRobin: Optional[bool]
    ServicePoliciesFromNamespace: Optional[bool]
    SourceIpStickiness: Optional[bool]
    ActiveServicePolicies: Optional[Sequence["_ActiveServicePoliciesDefinition"]]
    AdvertiseCustom: Optional[Sequence["_AdvertiseCustomDefinition"]]
    AdvertiseOnPublic: Optional[Sequence["_AdvertiseOnPublicDefinition"]]
    BlockedClients: Optional[Sequence["_BlockedClientsDefinition"]]
    CaptchaChallenge: Optional[Sequence["_CaptchaChallengeDefinition"]]
    CookieStickiness: Optional[Sequence["_CookieStickinessDefinition"]]
    CorsPolicy: Optional[Sequence["_CorsPolicyDefinition"]]
    DefaultRoutePools: Optional[Sequence["_DefaultRoutePoolsDefinition"]]
    Http: Optional[Sequence["_HttpDefinition"]]
    Https: Optional[Sequence["_HttpsDefinition"]]
    HttpsAutoCert: Optional[Sequence["_HttpsAutoCertDefinition"]]
    JsChallenge: Optional[Sequence["_JsChallengeDefinition"]]
    MaliciousUserMitigation: Optional[Sequence["_MaliciousUserMitigationDefinition"]]
    MoreOption: Optional[Sequence["_MoreOptionDefinition"]]
    PolicyBasedChallenge: Optional[Sequence["_PolicyBasedChallengeDefinition"]]
    RateLimit: Optional[Sequence["_RateLimitDefinition"]]
    RingHash: Optional[Sequence["_RingHashDefinition"]]
    Routes: Optional[Sequence["_RoutesDefinition"]]
    TrustedClients: Optional[Sequence["_TrustedClientsDefinition"]]
    UserIdentification: Optional[Sequence["_UserIdentificationDefinition"]]
    Waf: Optional[Sequence["_WafDefinition"]]
    WafExclusionRules: Optional[Sequence["_WafExclusionRulesDefinition"]]
    WafRule: Optional[Sequence["_WafRuleDefinition"]]

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
            AdvertiseOnPublicDefaultVip=json_data.get("AdvertiseOnPublicDefaultVip"),
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            DisableRateLimit=json_data.get("DisableRateLimit"),
            DisableWaf=json_data.get("DisableWaf"),
            DoNotAdvertise=json_data.get("DoNotAdvertise"),
            Domains=json_data.get("Domains"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            LeastActive=json_data.get("LeastActive"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            NoChallenge=json_data.get("NoChallenge"),
            NoServicePolicies=json_data.get("NoServicePolicies"),
            Random=json_data.get("Random"),
            RoundRobin=json_data.get("RoundRobin"),
            ServicePoliciesFromNamespace=json_data.get("ServicePoliciesFromNamespace"),
            SourceIpStickiness=json_data.get("SourceIpStickiness"),
            ActiveServicePolicies=deserialize_list(json_data.get("ActiveServicePolicies"), ActiveServicePoliciesDefinition),
            AdvertiseCustom=deserialize_list(json_data.get("AdvertiseCustom"), AdvertiseCustomDefinition),
            AdvertiseOnPublic=deserialize_list(json_data.get("AdvertiseOnPublic"), AdvertiseOnPublicDefinition),
            BlockedClients=deserialize_list(json_data.get("BlockedClients"), BlockedClientsDefinition),
            CaptchaChallenge=deserialize_list(json_data.get("CaptchaChallenge"), CaptchaChallengeDefinition),
            CookieStickiness=deserialize_list(json_data.get("CookieStickiness"), CookieStickinessDefinition),
            CorsPolicy=deserialize_list(json_data.get("CorsPolicy"), CorsPolicyDefinition),
            DefaultRoutePools=deserialize_list(json_data.get("DefaultRoutePools"), DefaultRoutePoolsDefinition),
            Http=deserialize_list(json_data.get("Http"), HttpDefinition),
            Https=deserialize_list(json_data.get("Https"), HttpsDefinition),
            HttpsAutoCert=deserialize_list(json_data.get("HttpsAutoCert"), HttpsAutoCertDefinition),
            JsChallenge=deserialize_list(json_data.get("JsChallenge"), JsChallengeDefinition),
            MaliciousUserMitigation=deserialize_list(json_data.get("MaliciousUserMitigation"), MaliciousUserMitigationDefinition),
            MoreOption=deserialize_list(json_data.get("MoreOption"), MoreOptionDefinition),
            PolicyBasedChallenge=deserialize_list(json_data.get("PolicyBasedChallenge"), PolicyBasedChallengeDefinition),
            RateLimit=deserialize_list(json_data.get("RateLimit"), RateLimitDefinition),
            RingHash=deserialize_list(json_data.get("RingHash"), RingHashDefinition),
            Routes=deserialize_list(json_data.get("Routes"), RoutesDefinition),
            TrustedClients=deserialize_list(json_data.get("TrustedClients"), TrustedClientsDefinition),
            UserIdentification=deserialize_list(json_data.get("UserIdentification"), UserIdentificationDefinition),
            Waf=deserialize_list(json_data.get("Waf"), WafDefinition),
            WafExclusionRules=deserialize_list(json_data.get("WafExclusionRules"), WafExclusionRulesDefinition),
            WafRule=deserialize_list(json_data.get("WafRule"), WafRuleDefinition),
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
class ActiveServicePoliciesDefinition(BaseModel):
    Policies: Optional[Sequence["_PoliciesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActiveServicePoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActiveServicePoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Policies=deserialize_list(json_data.get("Policies"), PoliciesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActiveServicePoliciesDefinition = ActiveServicePoliciesDefinition


@dataclass
class PoliciesDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PoliciesDefinition = PoliciesDefinition


@dataclass
class AdvertiseCustomDefinition(BaseModel):
    AdvertiseWhere: Optional[Sequence["_AdvertiseWhereDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdvertiseCustomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvertiseCustomDefinition"]:
        if not json_data:
            return None
        return cls(
            AdvertiseWhere=deserialize_list(json_data.get("AdvertiseWhere"), AdvertiseWhereDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvertiseCustomDefinition = AdvertiseCustomDefinition


@dataclass
class AdvertiseWhereDefinition(BaseModel):
    Port: Optional[float]
    UseDefaultPort: Optional[bool]
    Site: Optional[Sequence["_SiteDefinition"]]
    VirtualNetwork: Optional[Sequence["_VirtualNetworkDefinition"]]
    VirtualSite: Optional[Sequence["_VirtualSiteDefinition"]]
    Vk8sService: Optional[Sequence["_Vk8sServiceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdvertiseWhereDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvertiseWhereDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            UseDefaultPort=json_data.get("UseDefaultPort"),
            Site=deserialize_list(json_data.get("Site"), SiteDefinition),
            VirtualNetwork=deserialize_list(json_data.get("VirtualNetwork"), VirtualNetworkDefinition),
            VirtualSite=deserialize_list(json_data.get("VirtualSite"), VirtualSiteDefinition),
            Vk8sService=deserialize_list(json_data.get("Vk8sService"), Vk8sServiceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvertiseWhereDefinition = AdvertiseWhereDefinition


@dataclass
class SiteDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SiteDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SiteDefinition = SiteDefinition


@dataclass
class VirtualNetworkDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNetworkDefinition = VirtualNetworkDefinition


@dataclass
class VirtualSiteDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualSiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualSiteDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualSiteDefinition = VirtualSiteDefinition


@dataclass
class Vk8sServiceDefinition(BaseModel):
    Site: Optional[Sequence["_SiteDefinition"]]
    VirtualSite: Optional[Sequence["_VirtualSiteDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Vk8sServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Vk8sServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            Site=deserialize_list(json_data.get("Site"), SiteDefinition),
            VirtualSite=deserialize_list(json_data.get("VirtualSite"), VirtualSiteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Vk8sServiceDefinition = Vk8sServiceDefinition


@dataclass
class AdvertiseOnPublicDefinition(BaseModel):
    PublicIp: Optional[Sequence["_PublicIpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdvertiseOnPublicDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvertiseOnPublicDefinition"]:
        if not json_data:
            return None
        return cls(
            PublicIp=deserialize_list(json_data.get("PublicIp"), PublicIpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvertiseOnPublicDefinition = AdvertiseOnPublicDefinition


@dataclass
class PublicIpDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicIpDefinition = PublicIpDefinition


@dataclass
class BlockedClientsDefinition(BaseModel):
    AsNumber: Optional[float]
    ExpirationTimestamp: Optional[str]
    IpPrefix: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BlockedClientsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockedClientsDefinition"]:
        if not json_data:
            return None
        return cls(
            AsNumber=json_data.get("AsNumber"),
            ExpirationTimestamp=json_data.get("ExpirationTimestamp"),
            IpPrefix=json_data.get("IpPrefix"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockedClientsDefinition = BlockedClientsDefinition


@dataclass
class MetadataDefinition(BaseModel):
    Description: Optional[str]
    Disable: Optional[bool]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


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
class CookieStickinessDefinition(BaseModel):
    Name: Optional[str]
    Path: Optional[str]
    Ttl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CookieStickinessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookieStickinessDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CookieStickinessDefinition = CookieStickinessDefinition


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
class DefaultRoutePoolsDefinition(BaseModel):
    EndpointSubsets: Optional[Sequence["_EndpointSubsetsDefinition"]]
    Weight: Optional[float]
    Cluster: Optional[Sequence["_ClusterDefinition"]]
    Pool: Optional[Sequence["_PoolDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultRoutePoolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultRoutePoolsDefinition"]:
        if not json_data:
            return None
        return cls(
            EndpointSubsets=deserialize_list(json_data.get("EndpointSubsets"), EndpointSubsetsDefinition),
            Weight=json_data.get("Weight"),
            Cluster=deserialize_list(json_data.get("Cluster"), ClusterDefinition),
            Pool=deserialize_list(json_data.get("Pool"), PoolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultRoutePoolsDefinition = DefaultRoutePoolsDefinition


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
class PoolDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PoolDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PoolDefinition = PoolDefinition


@dataclass
class HttpDefinition(BaseModel):
    DnsVolterraManaged: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_HttpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsVolterraManaged=json_data.get("DnsVolterraManaged"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpDefinition = HttpDefinition


@dataclass
class HttpsDefinition(BaseModel):
    AddHsts: Optional[bool]
    AppendServerName: Optional[str]
    DefaultHeader: Optional[bool]
    HttpRedirect: Optional[bool]
    PassThrough: Optional[bool]
    ServerName: Optional[str]
    TlsParameters: Optional[Sequence["_TlsParametersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpsDefinition"]:
        if not json_data:
            return None
        return cls(
            AddHsts=json_data.get("AddHsts"),
            AppendServerName=json_data.get("AppendServerName"),
            DefaultHeader=json_data.get("DefaultHeader"),
            HttpRedirect=json_data.get("HttpRedirect"),
            PassThrough=json_data.get("PassThrough"),
            ServerName=json_data.get("ServerName"),
            TlsParameters=deserialize_list(json_data.get("TlsParameters"), TlsParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpsDefinition = HttpsDefinition


@dataclass
class TlsParametersDefinition(BaseModel):
    NoMtls: Optional[bool]
    TlsCertificates: Optional[Sequence["_TlsCertificatesDefinition"]]
    TlsConfig: Optional[Sequence["_TlsConfigDefinition"]]
    UseMtls: Optional[Sequence["_UseMtlsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TlsParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            NoMtls=json_data.get("NoMtls"),
            TlsCertificates=deserialize_list(json_data.get("TlsCertificates"), TlsCertificatesDefinition),
            TlsConfig=deserialize_list(json_data.get("TlsConfig"), TlsConfigDefinition),
            UseMtls=deserialize_list(json_data.get("UseMtls"), UseMtlsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsParametersDefinition = TlsParametersDefinition


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
class TlsConfigDefinition(BaseModel):
    DefaultSecurity: Optional[bool]
    LowSecurity: Optional[bool]
    MediumSecurity: Optional[bool]
    CustomSecurity: Optional[Sequence["_CustomSecurityDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TlsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultSecurity=json_data.get("DefaultSecurity"),
            LowSecurity=json_data.get("LowSecurity"),
            MediumSecurity=json_data.get("MediumSecurity"),
            CustomSecurity=deserialize_list(json_data.get("CustomSecurity"), CustomSecurityDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsConfigDefinition = TlsConfigDefinition


@dataclass
class CustomSecurityDefinition(BaseModel):
    CipherSuites: Optional[Sequence[str]]
    MaxVersion: Optional[str]
    MinVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomSecurityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomSecurityDefinition"]:
        if not json_data:
            return None
        return cls(
            CipherSuites=json_data.get("CipherSuites"),
            MaxVersion=json_data.get("MaxVersion"),
            MinVersion=json_data.get("MinVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomSecurityDefinition = CustomSecurityDefinition


@dataclass
class UseMtlsDefinition(BaseModel):
    TrustedCaUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UseMtlsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UseMtlsDefinition"]:
        if not json_data:
            return None
        return cls(
            TrustedCaUrl=json_data.get("TrustedCaUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UseMtlsDefinition = UseMtlsDefinition


@dataclass
class HttpsAutoCertDefinition(BaseModel):
    AddHsts: Optional[bool]
    AppendServerName: Optional[str]
    DefaultHeader: Optional[bool]
    HttpRedirect: Optional[bool]
    NoMtls: Optional[bool]
    PassThrough: Optional[bool]
    ServerName: Optional[str]
    TlsConfig: Optional[Sequence["_TlsConfigDefinition"]]
    UseMtls: Optional[Sequence["_UseMtlsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpsAutoCertDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpsAutoCertDefinition"]:
        if not json_data:
            return None
        return cls(
            AddHsts=json_data.get("AddHsts"),
            AppendServerName=json_data.get("AppendServerName"),
            DefaultHeader=json_data.get("DefaultHeader"),
            HttpRedirect=json_data.get("HttpRedirect"),
            NoMtls=json_data.get("NoMtls"),
            PassThrough=json_data.get("PassThrough"),
            ServerName=json_data.get("ServerName"),
            TlsConfig=deserialize_list(json_data.get("TlsConfig"), TlsConfigDefinition),
            UseMtls=deserialize_list(json_data.get("UseMtls"), UseMtlsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpsAutoCertDefinition = HttpsAutoCertDefinition


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
class MaliciousUserMitigationDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaliciousUserMitigationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaliciousUserMitigationDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaliciousUserMitigationDefinition = MaliciousUserMitigationDefinition


@dataclass
class MoreOptionDefinition(BaseModel):
    CustomErrors: Optional[Sequence["_CustomErrorsDefinition"]]
    DisableDefaultErrorPages: Optional[bool]
    IdleTimeout: Optional[float]
    MaxRequestHeaderSize: Optional[float]
    RequestHeadersToRemove: Optional[Sequence[str]]
    ResponseHeadersToRemove: Optional[Sequence[str]]
    BufferPolicy: Optional[Sequence["_BufferPolicyDefinition"]]
    CompressionParams: Optional[Sequence["_CompressionParamsDefinition"]]
    JavascriptInfo: Optional[Sequence["_JavascriptInfoDefinition"]]
    Jwt: Optional[Sequence["_JwtDefinition"]]
    RequestHeadersToAdd: Optional[Sequence["_RequestHeadersToAddDefinition"]]
    ResponseHeadersToAdd: Optional[Sequence["_ResponseHeadersToAddDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MoreOptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MoreOptionDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomErrors=deserialize_list(json_data.get("CustomErrors"), CustomErrorsDefinition),
            DisableDefaultErrorPages=json_data.get("DisableDefaultErrorPages"),
            IdleTimeout=json_data.get("IdleTimeout"),
            MaxRequestHeaderSize=json_data.get("MaxRequestHeaderSize"),
            RequestHeadersToRemove=json_data.get("RequestHeadersToRemove"),
            ResponseHeadersToRemove=json_data.get("ResponseHeadersToRemove"),
            BufferPolicy=deserialize_list(json_data.get("BufferPolicy"), BufferPolicyDefinition),
            CompressionParams=deserialize_list(json_data.get("CompressionParams"), CompressionParamsDefinition),
            JavascriptInfo=deserialize_list(json_data.get("JavascriptInfo"), JavascriptInfoDefinition),
            Jwt=deserialize_list(json_data.get("Jwt"), JwtDefinition),
            RequestHeadersToAdd=deserialize_list(json_data.get("RequestHeadersToAdd"), RequestHeadersToAddDefinition),
            ResponseHeadersToAdd=deserialize_list(json_data.get("ResponseHeadersToAdd"), ResponseHeadersToAddDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MoreOptionDefinition = MoreOptionDefinition


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
class JavascriptInfoDefinition(BaseModel):
    CachePrefix: Optional[str]
    CustomScriptUrl: Optional[str]
    ScriptConfig: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JavascriptInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JavascriptInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            CachePrefix=json_data.get("CachePrefix"),
            CustomScriptUrl=json_data.get("CustomScriptUrl"),
            ScriptConfig=json_data.get("ScriptConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JavascriptInfoDefinition = JavascriptInfoDefinition


@dataclass
class JwtDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JwtDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JwtDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JwtDefinition = JwtDefinition


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
class PolicyBasedChallengeDefinition(BaseModel):
    AlwaysEnableCaptchaChallenge: Optional[bool]
    AlwaysEnableJsChallenge: Optional[bool]
    DefaultCaptchaChallengeParameters: Optional[bool]
    DefaultJsChallengeParameters: Optional[bool]
    DefaultMitigationSettings: Optional[bool]
    DefaultTemporaryBlockingParameters: Optional[bool]
    NoChallenge: Optional[bool]
    CaptchaChallengeParameters: Optional[Sequence["_CaptchaChallengeParametersDefinition"]]
    JsChallengeParameters: Optional[Sequence["_JsChallengeParametersDefinition"]]
    MaliciousUserMitigation: Optional[Sequence["_MaliciousUserMitigationDefinition"]]
    RuleList: Optional[Sequence["_RuleListDefinition"]]
    TemporaryUserBlocking: Optional[Sequence["_TemporaryUserBlockingDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyBasedChallengeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyBasedChallengeDefinition"]:
        if not json_data:
            return None
        return cls(
            AlwaysEnableCaptchaChallenge=json_data.get("AlwaysEnableCaptchaChallenge"),
            AlwaysEnableJsChallenge=json_data.get("AlwaysEnableJsChallenge"),
            DefaultCaptchaChallengeParameters=json_data.get("DefaultCaptchaChallengeParameters"),
            DefaultJsChallengeParameters=json_data.get("DefaultJsChallengeParameters"),
            DefaultMitigationSettings=json_data.get("DefaultMitigationSettings"),
            DefaultTemporaryBlockingParameters=json_data.get("DefaultTemporaryBlockingParameters"),
            NoChallenge=json_data.get("NoChallenge"),
            CaptchaChallengeParameters=deserialize_list(json_data.get("CaptchaChallengeParameters"), CaptchaChallengeParametersDefinition),
            JsChallengeParameters=deserialize_list(json_data.get("JsChallengeParameters"), JsChallengeParametersDefinition),
            MaliciousUserMitigation=deserialize_list(json_data.get("MaliciousUserMitigation"), MaliciousUserMitigationDefinition),
            RuleList=deserialize_list(json_data.get("RuleList"), RuleListDefinition),
            TemporaryUserBlocking=deserialize_list(json_data.get("TemporaryUserBlocking"), TemporaryUserBlockingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyBasedChallengeDefinition = PolicyBasedChallengeDefinition


@dataclass
class CaptchaChallengeParametersDefinition(BaseModel):
    CookieExpiry: Optional[float]
    CustomPage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CaptchaChallengeParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaptchaChallengeParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            CookieExpiry=json_data.get("CookieExpiry"),
            CustomPage=json_data.get("CustomPage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaptchaChallengeParametersDefinition = CaptchaChallengeParametersDefinition


@dataclass
class JsChallengeParametersDefinition(BaseModel):
    CookieExpiry: Optional[float]
    CustomPage: Optional[str]
    JsScriptDelay: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_JsChallengeParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsChallengeParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            CookieExpiry=json_data.get("CookieExpiry"),
            CustomPage=json_data.get("CustomPage"),
            JsScriptDelay=json_data.get("JsScriptDelay"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsChallengeParametersDefinition = JsChallengeParametersDefinition


@dataclass
class RuleListDefinition(BaseModel):
    Rules: Optional[Sequence["_RulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleListDefinition"]:
        if not json_data:
            return None
        return cls(
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleListDefinition = RuleListDefinition


@dataclass
class RulesDefinition(BaseModel):
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Spec: Optional[Sequence["_SpecDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Spec=deserialize_list(json_data.get("Spec"), SpecDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class SpecDefinition(BaseModel):
    AnyAsn: Optional[bool]
    AnyClient: Optional[bool]
    AnyIp: Optional[bool]
    ClientName: Optional[str]
    DisableChallenge: Optional[bool]
    EnableCaptchaChallenge: Optional[bool]
    EnableJavascriptChallenge: Optional[bool]
    ExpirationTimestamp: Optional[str]
    ArgMatchers: Optional[Sequence["_ArgMatchersDefinition"]]
    AsnList: Optional[Sequence["_AsnListDefinition"]]
    AsnMatcher: Optional[Sequence["_AsnMatcherDefinition"]]
    BodyMatcher: Optional[Sequence["_BodyMatcherDefinition"]]
    ClientNameMatcher: Optional[Sequence["_ClientNameMatcherDefinition"]]
    ClientSelector: Optional[Sequence["_ClientSelectorDefinition"]]
    CookieMatchers: Optional[Sequence["_CookieMatchersDefinition"]]
    DomainMatcher: Optional[Sequence["_DomainMatcherDefinition"]]
    Headers: Optional[Sequence["_HeadersDefinition"]]
    HttpMethod: Optional[Sequence["_HttpMethodDefinition"]]
    IpMatcher: Optional[Sequence["_IpMatcherDefinition"]]
    IpPrefixList: Optional[Sequence["_IpPrefixListDefinition"]]
    Path: Optional[Sequence["_PathDefinition"]]
    QueryParams: Optional[Sequence["_QueryParamsDefinition"]]
    TlsFingerprintMatcher: Optional[Sequence["_TlsFingerprintMatcherDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecDefinition"]:
        if not json_data:
            return None
        return cls(
            AnyAsn=json_data.get("AnyAsn"),
            AnyClient=json_data.get("AnyClient"),
            AnyIp=json_data.get("AnyIp"),
            ClientName=json_data.get("ClientName"),
            DisableChallenge=json_data.get("DisableChallenge"),
            EnableCaptchaChallenge=json_data.get("EnableCaptchaChallenge"),
            EnableJavascriptChallenge=json_data.get("EnableJavascriptChallenge"),
            ExpirationTimestamp=json_data.get("ExpirationTimestamp"),
            ArgMatchers=deserialize_list(json_data.get("ArgMatchers"), ArgMatchersDefinition),
            AsnList=deserialize_list(json_data.get("AsnList"), AsnListDefinition),
            AsnMatcher=deserialize_list(json_data.get("AsnMatcher"), AsnMatcherDefinition),
            BodyMatcher=deserialize_list(json_data.get("BodyMatcher"), BodyMatcherDefinition),
            ClientNameMatcher=deserialize_list(json_data.get("ClientNameMatcher"), ClientNameMatcherDefinition),
            ClientSelector=deserialize_list(json_data.get("ClientSelector"), ClientSelectorDefinition),
            CookieMatchers=deserialize_list(json_data.get("CookieMatchers"), CookieMatchersDefinition),
            DomainMatcher=deserialize_list(json_data.get("DomainMatcher"), DomainMatcherDefinition),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
            HttpMethod=deserialize_list(json_data.get("HttpMethod"), HttpMethodDefinition),
            IpMatcher=deserialize_list(json_data.get("IpMatcher"), IpMatcherDefinition),
            IpPrefixList=deserialize_list(json_data.get("IpPrefixList"), IpPrefixListDefinition),
            Path=deserialize_list(json_data.get("Path"), PathDefinition),
            QueryParams=deserialize_list(json_data.get("QueryParams"), QueryParamsDefinition),
            TlsFingerprintMatcher=deserialize_list(json_data.get("TlsFingerprintMatcher"), TlsFingerprintMatcherDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecDefinition = SpecDefinition


@dataclass
class ArgMatchersDefinition(BaseModel):
    CheckNotPresent: Optional[bool]
    CheckPresent: Optional[bool]
    InvertMatcher: Optional[bool]
    Name: Optional[str]
    Presence: Optional[bool]
    Item: Optional[Sequence["_ItemDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ArgMatchersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArgMatchersDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckNotPresent=json_data.get("CheckNotPresent"),
            CheckPresent=json_data.get("CheckPresent"),
            InvertMatcher=json_data.get("InvertMatcher"),
            Name=json_data.get("Name"),
            Presence=json_data.get("Presence"),
            Item=deserialize_list(json_data.get("Item"), ItemDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArgMatchersDefinition = ArgMatchersDefinition


@dataclass
class ItemDefinition(BaseModel):
    ExactValues: Optional[Sequence[str]]
    RegexValues: Optional[Sequence[str]]
    Transformers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ItemDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ItemDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactValues=json_data.get("ExactValues"),
            RegexValues=json_data.get("RegexValues"),
            Transformers=json_data.get("Transformers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ItemDefinition = ItemDefinition


@dataclass
class AsnListDefinition(BaseModel):
    AsNumbers: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_AsnListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AsnListDefinition"]:
        if not json_data:
            return None
        return cls(
            AsNumbers=json_data.get("AsNumbers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AsnListDefinition = AsnListDefinition


@dataclass
class AsnMatcherDefinition(BaseModel):
    AsnSets: Optional[Sequence["_AsnSetsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AsnMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AsnMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            AsnSets=deserialize_list(json_data.get("AsnSets"), AsnSetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AsnMatcherDefinition = AsnMatcherDefinition


@dataclass
class AsnSetsDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AsnSetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AsnSetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AsnSetsDefinition = AsnSetsDefinition


@dataclass
class BodyMatcherDefinition(BaseModel):
    ExactValues: Optional[Sequence[str]]
    RegexValues: Optional[Sequence[str]]
    Transformers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_BodyMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BodyMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactValues=json_data.get("ExactValues"),
            RegexValues=json_data.get("RegexValues"),
            Transformers=json_data.get("Transformers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BodyMatcherDefinition = BodyMatcherDefinition


@dataclass
class ClientNameMatcherDefinition(BaseModel):
    ExactValues: Optional[Sequence[str]]
    RegexValues: Optional[Sequence[str]]
    Transformers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientNameMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientNameMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactValues=json_data.get("ExactValues"),
            RegexValues=json_data.get("RegexValues"),
            Transformers=json_data.get("Transformers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientNameMatcherDefinition = ClientNameMatcherDefinition


@dataclass
class ClientSelectorDefinition(BaseModel):
    Expressions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Expressions=json_data.get("Expressions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientSelectorDefinition = ClientSelectorDefinition


@dataclass
class CookieMatchersDefinition(BaseModel):
    CheckNotPresent: Optional[bool]
    CheckPresent: Optional[bool]
    InvertMatcher: Optional[bool]
    Name: Optional[str]
    Presence: Optional[bool]
    Item: Optional[Sequence["_ItemDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CookieMatchersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookieMatchersDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckNotPresent=json_data.get("CheckNotPresent"),
            CheckPresent=json_data.get("CheckPresent"),
            InvertMatcher=json_data.get("InvertMatcher"),
            Name=json_data.get("Name"),
            Presence=json_data.get("Presence"),
            Item=deserialize_list(json_data.get("Item"), ItemDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CookieMatchersDefinition = CookieMatchersDefinition


@dataclass
class DomainMatcherDefinition(BaseModel):
    ExactValues: Optional[Sequence[str]]
    RegexValues: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DomainMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactValues=json_data.get("ExactValues"),
            RegexValues=json_data.get("RegexValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainMatcherDefinition = DomainMatcherDefinition


@dataclass
class HeadersDefinition(BaseModel):
    CheckNotPresent: Optional[bool]
    CheckPresent: Optional[bool]
    InvertMatcher: Optional[bool]
    Name: Optional[str]
    Presence: Optional[bool]
    Item: Optional[Sequence["_ItemDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckNotPresent=json_data.get("CheckNotPresent"),
            CheckPresent=json_data.get("CheckPresent"),
            InvertMatcher=json_data.get("InvertMatcher"),
            Name=json_data.get("Name"),
            Presence=json_data.get("Presence"),
            Item=deserialize_list(json_data.get("Item"), ItemDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


@dataclass
class HttpMethodDefinition(BaseModel):
    InvertMatcher: Optional[bool]
    Methods: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpMethodDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpMethodDefinition"]:
        if not json_data:
            return None
        return cls(
            InvertMatcher=json_data.get("InvertMatcher"),
            Methods=json_data.get("Methods"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpMethodDefinition = HttpMethodDefinition


@dataclass
class IpMatcherDefinition(BaseModel):
    InvertMatcher: Optional[bool]
    PrefixSets: Optional[Sequence["_PrefixSetsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            InvertMatcher=json_data.get("InvertMatcher"),
            PrefixSets=deserialize_list(json_data.get("PrefixSets"), PrefixSetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpMatcherDefinition = IpMatcherDefinition


@dataclass
class PrefixSetsDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixSetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixSetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixSetsDefinition = PrefixSetsDefinition


@dataclass
class IpPrefixListDefinition(BaseModel):
    InvertMatch: Optional[bool]
    IpPrefixes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IpPrefixListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpPrefixListDefinition"]:
        if not json_data:
            return None
        return cls(
            InvertMatch=json_data.get("InvertMatch"),
            IpPrefixes=json_data.get("IpPrefixes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpPrefixListDefinition = IpPrefixListDefinition


@dataclass
class PathDefinition(BaseModel):
    ExactValues: Optional[Sequence[str]]
    PrefixValues: Optional[Sequence[str]]
    RegexValues: Optional[Sequence[str]]
    Transformers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactValues=json_data.get("ExactValues"),
            PrefixValues=json_data.get("PrefixValues"),
            RegexValues=json_data.get("RegexValues"),
            Transformers=json_data.get("Transformers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathDefinition = PathDefinition


@dataclass
class QueryParamsDefinition(BaseModel):
    CheckNotPresent: Optional[bool]
    CheckPresent: Optional[bool]
    InvertMatcher: Optional[bool]
    Key: Optional[str]
    Presence: Optional[bool]
    Item: Optional[Sequence["_ItemDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckNotPresent=json_data.get("CheckNotPresent"),
            CheckPresent=json_data.get("CheckPresent"),
            InvertMatcher=json_data.get("InvertMatcher"),
            Key=json_data.get("Key"),
            Presence=json_data.get("Presence"),
            Item=deserialize_list(json_data.get("Item"), ItemDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryParamsDefinition = QueryParamsDefinition


@dataclass
class TlsFingerprintMatcherDefinition(BaseModel):
    Classes: Optional[Sequence[str]]
    ExactValues: Optional[Sequence[str]]
    ExcludedValues: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TlsFingerprintMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsFingerprintMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            Classes=json_data.get("Classes"),
            ExactValues=json_data.get("ExactValues"),
            ExcludedValues=json_data.get("ExcludedValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsFingerprintMatcherDefinition = TlsFingerprintMatcherDefinition


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
class RateLimitDefinition(BaseModel):
    NoIpAllowedList: Optional[bool]
    NoPolicies: Optional[bool]
    CustomIpAllowedList: Optional[Sequence["_CustomIpAllowedListDefinition"]]
    IpAllowedList: Optional[Sequence["_IpAllowedListDefinition"]]
    Policies: Optional[Sequence["_PoliciesDefinition"]]
    RateLimiter: Optional[Sequence["_RateLimiterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimitDefinition"]:
        if not json_data:
            return None
        return cls(
            NoIpAllowedList=json_data.get("NoIpAllowedList"),
            NoPolicies=json_data.get("NoPolicies"),
            CustomIpAllowedList=deserialize_list(json_data.get("CustomIpAllowedList"), CustomIpAllowedListDefinition),
            IpAllowedList=deserialize_list(json_data.get("IpAllowedList"), IpAllowedListDefinition),
            Policies=deserialize_list(json_data.get("Policies"), PoliciesDefinition),
            RateLimiter=deserialize_list(json_data.get("RateLimiter"), RateLimiterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimitDefinition = RateLimitDefinition


@dataclass
class CustomIpAllowedListDefinition(BaseModel):
    RateLimiterAllowedPrefixes: Optional[Sequence["_RateLimiterAllowedPrefixesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomIpAllowedListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomIpAllowedListDefinition"]:
        if not json_data:
            return None
        return cls(
            RateLimiterAllowedPrefixes=deserialize_list(json_data.get("RateLimiterAllowedPrefixes"), RateLimiterAllowedPrefixesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomIpAllowedListDefinition = CustomIpAllowedListDefinition


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
class IpAllowedListDefinition(BaseModel):
    Prefixes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IpAllowedListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAllowedListDefinition"]:
        if not json_data:
            return None
        return cls(
            Prefixes=json_data.get("Prefixes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAllowedListDefinition = IpAllowedListDefinition


@dataclass
class RateLimiterDefinition(BaseModel):
    TotalNumber: Optional[float]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimiterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimiterDefinition"]:
        if not json_data:
            return None
        return cls(
            TotalNumber=json_data.get("TotalNumber"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimiterDefinition = RateLimiterDefinition


@dataclass
class RingHashDefinition(BaseModel):
    HashPolicy: Optional[Sequence["_HashPolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RingHashDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RingHashDefinition"]:
        if not json_data:
            return None
        return cls(
            HashPolicy=deserialize_list(json_data.get("HashPolicy"), HashPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RingHashDefinition = RingHashDefinition


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
class RoutesDefinition(BaseModel):
    CustomRouteObject: Optional[Sequence["_CustomRouteObjectDefinition"]]
    DirectResponseRoute: Optional[Sequence["_DirectResponseRouteDefinition"]]
    RedirectRoute: Optional[Sequence["_RedirectRouteDefinition"]]
    SimpleRoute: Optional[Sequence["_SimpleRouteDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomRouteObject=deserialize_list(json_data.get("CustomRouteObject"), CustomRouteObjectDefinition),
            DirectResponseRoute=deserialize_list(json_data.get("DirectResponseRoute"), DirectResponseRouteDefinition),
            RedirectRoute=deserialize_list(json_data.get("RedirectRoute"), RedirectRouteDefinition),
            SimpleRoute=deserialize_list(json_data.get("SimpleRoute"), SimpleRouteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutesDefinition = RoutesDefinition


@dataclass
class CustomRouteObjectDefinition(BaseModel):
    RouteRef: Optional[Sequence["_RouteRefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomRouteObjectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomRouteObjectDefinition"]:
        if not json_data:
            return None
        return cls(
            RouteRef=deserialize_list(json_data.get("RouteRef"), RouteRefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomRouteObjectDefinition = CustomRouteObjectDefinition


@dataclass
class RouteRefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RouteRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteRefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteRefDefinition = RouteRefDefinition


@dataclass
class DirectResponseRouteDefinition(BaseModel):
    HttpMethod: Optional[str]
    Path: Optional[Sequence["_PathDefinition"]]
    RouteDirectResponse: Optional[Sequence["_RouteDirectResponseDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DirectResponseRouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DirectResponseRouteDefinition"]:
        if not json_data:
            return None
        return cls(
            HttpMethod=json_data.get("HttpMethod"),
            Path=deserialize_list(json_data.get("Path"), PathDefinition),
            RouteDirectResponse=deserialize_list(json_data.get("RouteDirectResponse"), RouteDirectResponseDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DirectResponseRouteDefinition = DirectResponseRouteDefinition


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
class RedirectRouteDefinition(BaseModel):
    HttpMethod: Optional[str]
    Path: Optional[Sequence["_PathDefinition"]]
    RouteRedirect: Optional[Sequence["_RouteRedirectDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectRouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectRouteDefinition"]:
        if not json_data:
            return None
        return cls(
            HttpMethod=json_data.get("HttpMethod"),
            Path=deserialize_list(json_data.get("Path"), PathDefinition),
            RouteRedirect=deserialize_list(json_data.get("RouteRedirect"), RouteRedirectDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedirectRouteDefinition = RedirectRouteDefinition


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
class SimpleRouteDefinition(BaseModel):
    AutoHostRewrite: Optional[bool]
    DisableHostRewrite: Optional[bool]
    HostRewrite: Optional[str]
    HttpMethod: Optional[str]
    AdvancedOptions: Optional[Sequence["_AdvancedOptionsDefinition"]]
    OriginPools: Optional[Sequence["_OriginPoolsDefinition"]]
    Path: Optional[Sequence["_PathDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SimpleRouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SimpleRouteDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoHostRewrite=json_data.get("AutoHostRewrite"),
            DisableHostRewrite=json_data.get("DisableHostRewrite"),
            HostRewrite=json_data.get("HostRewrite"),
            HttpMethod=json_data.get("HttpMethod"),
            AdvancedOptions=deserialize_list(json_data.get("AdvancedOptions"), AdvancedOptionsDefinition),
            OriginPools=deserialize_list(json_data.get("OriginPools"), OriginPoolsDefinition),
            Path=deserialize_list(json_data.get("Path"), PathDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SimpleRouteDefinition = SimpleRouteDefinition


@dataclass
class AdvancedOptionsDefinition(BaseModel):
    CommonBuffering: Optional[bool]
    CommonHashPolicy: Optional[bool]
    DefaultRetryPolicy: Optional[bool]
    DisableLocationAdd: Optional[bool]
    DisableMirroring: Optional[bool]
    DisablePrefixRewrite: Optional[bool]
    DisableSpdy: Optional[bool]
    DisableWaf: Optional[bool]
    DisableWebSocketConfig: Optional[bool]
    DoNotRetractCluster: Optional[bool]
    EnableSpdy: Optional[bool]
    EndpointSubsets: Optional[Sequence["_EndpointSubsetsDefinition2"]]
    PrefixRewrite: Optional[str]
    Priority: Optional[str]
    RequestHeadersToRemove: Optional[Sequence[str]]
    ResponseHeadersToRemove: Optional[Sequence[str]]
    RetractCluster: Optional[bool]
    Timeout: Optional[float]
    BufferPolicy: Optional[Sequence["_BufferPolicyDefinition"]]
    CorsPolicy: Optional[Sequence["_CorsPolicyDefinition"]]
    MirrorPolicy: Optional[Sequence["_MirrorPolicyDefinition"]]
    RequestHeadersToAdd: Optional[Sequence["_RequestHeadersToAddDefinition"]]
    ResponseHeadersToAdd: Optional[Sequence["_ResponseHeadersToAddDefinition"]]
    RetryPolicy: Optional[Sequence["_RetryPolicyDefinition"]]
    SpecificHashPolicy: Optional[Sequence["_SpecificHashPolicyDefinition"]]
    Waf: Optional[Sequence["_WafDefinition"]]
    WafRule: Optional[Sequence["_WafRuleDefinition"]]
    WebSocketConfig: Optional[Sequence["_WebSocketConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            CommonBuffering=json_data.get("CommonBuffering"),
            CommonHashPolicy=json_data.get("CommonHashPolicy"),
            DefaultRetryPolicy=json_data.get("DefaultRetryPolicy"),
            DisableLocationAdd=json_data.get("DisableLocationAdd"),
            DisableMirroring=json_data.get("DisableMirroring"),
            DisablePrefixRewrite=json_data.get("DisablePrefixRewrite"),
            DisableSpdy=json_data.get("DisableSpdy"),
            DisableWaf=json_data.get("DisableWaf"),
            DisableWebSocketConfig=json_data.get("DisableWebSocketConfig"),
            DoNotRetractCluster=json_data.get("DoNotRetractCluster"),
            EnableSpdy=json_data.get("EnableSpdy"),
            EndpointSubsets=deserialize_list(json_data.get("EndpointSubsets"), EndpointSubsetsDefinition2),
            PrefixRewrite=json_data.get("PrefixRewrite"),
            Priority=json_data.get("Priority"),
            RequestHeadersToRemove=json_data.get("RequestHeadersToRemove"),
            ResponseHeadersToRemove=json_data.get("ResponseHeadersToRemove"),
            RetractCluster=json_data.get("RetractCluster"),
            Timeout=json_data.get("Timeout"),
            BufferPolicy=deserialize_list(json_data.get("BufferPolicy"), BufferPolicyDefinition),
            CorsPolicy=deserialize_list(json_data.get("CorsPolicy"), CorsPolicyDefinition),
            MirrorPolicy=deserialize_list(json_data.get("MirrorPolicy"), MirrorPolicyDefinition),
            RequestHeadersToAdd=deserialize_list(json_data.get("RequestHeadersToAdd"), RequestHeadersToAddDefinition),
            ResponseHeadersToAdd=deserialize_list(json_data.get("ResponseHeadersToAdd"), ResponseHeadersToAddDefinition),
            RetryPolicy=deserialize_list(json_data.get("RetryPolicy"), RetryPolicyDefinition),
            SpecificHashPolicy=deserialize_list(json_data.get("SpecificHashPolicy"), SpecificHashPolicyDefinition),
            Waf=deserialize_list(json_data.get("Waf"), WafDefinition),
            WafRule=deserialize_list(json_data.get("WafRule"), WafRuleDefinition),
            WebSocketConfig=deserialize_list(json_data.get("WebSocketConfig"), WebSocketConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedOptionsDefinition = AdvancedOptionsDefinition


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
class MirrorPolicyDefinition(BaseModel):
    OriginPool: Optional[Sequence["_OriginPoolDefinition"]]
    Percent: Optional[Sequence["_PercentDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MirrorPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MirrorPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            OriginPool=deserialize_list(json_data.get("OriginPool"), OriginPoolDefinition),
            Percent=deserialize_list(json_data.get("Percent"), PercentDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MirrorPolicyDefinition = MirrorPolicyDefinition


@dataclass
class OriginPoolDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OriginPoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginPoolDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginPoolDefinition = OriginPoolDefinition


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
class SpecificHashPolicyDefinition(BaseModel):
    HashPolicy: Optional[Sequence["_HashPolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecificHashPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecificHashPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            HashPolicy=deserialize_list(json_data.get("HashPolicy"), HashPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecificHashPolicyDefinition = SpecificHashPolicyDefinition


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
class WafRuleDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WafRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WafRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WafRuleDefinition = WafRuleDefinition


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
class OriginPoolsDefinition(BaseModel):
    EndpointSubsets: Optional[Sequence["_EndpointSubsetsDefinition3"]]
    Weight: Optional[float]
    Cluster: Optional[Sequence["_ClusterDefinition"]]
    Pool: Optional[Sequence["_PoolDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OriginPoolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginPoolsDefinition"]:
        if not json_data:
            return None
        return cls(
            EndpointSubsets=deserialize_list(json_data.get("EndpointSubsets"), EndpointSubsetsDefinition3),
            Weight=json_data.get("Weight"),
            Cluster=deserialize_list(json_data.get("Cluster"), ClusterDefinition),
            Pool=deserialize_list(json_data.get("Pool"), PoolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginPoolsDefinition = OriginPoolsDefinition


@dataclass
class EndpointSubsetsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointSubsetsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointSubsetsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointSubsetsDefinition3 = EndpointSubsetsDefinition3


@dataclass
class TrustedClientsDefinition(BaseModel):
    AsNumber: Optional[float]
    ExpirationTimestamp: Optional[str]
    IpPrefix: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TrustedClientsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrustedClientsDefinition"]:
        if not json_data:
            return None
        return cls(
            AsNumber=json_data.get("AsNumber"),
            ExpirationTimestamp=json_data.get("ExpirationTimestamp"),
            IpPrefix=json_data.get("IpPrefix"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrustedClientsDefinition = TrustedClientsDefinition


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
class WafExclusionRulesDefinition(BaseModel):
    AnyDomain: Optional[bool]
    DomainRegex: Optional[str]
    ExcludeRuleIds: Optional[Sequence[str]]
    ExpirationTimestamp: Optional[str]
    Methods: Optional[Sequence[str]]
    PathRegex: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WafExclusionRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WafExclusionRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            AnyDomain=json_data.get("AnyDomain"),
            DomainRegex=json_data.get("DomainRegex"),
            ExcludeRuleIds=json_data.get("ExcludeRuleIds"),
            ExpirationTimestamp=json_data.get("ExpirationTimestamp"),
            Methods=json_data.get("Methods"),
            PathRegex=json_data.get("PathRegex"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WafExclusionRulesDefinition = WafExclusionRulesDefinition


