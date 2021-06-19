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
    DiscoveryConsul: Optional[Sequence["_DiscoveryConsulDefinition"]]
    DiscoveryK8s: Optional[Sequence["_DiscoveryK8sDefinition"]]
    Where: Optional[Sequence["_WhereDefinition"]]

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
            DiscoveryConsul=deserialize_list(json_data.get("DiscoveryConsul"), DiscoveryConsulDefinition),
            DiscoveryK8s=deserialize_list(json_data.get("DiscoveryK8s"), DiscoveryK8sDefinition),
            Where=deserialize_list(json_data.get("Where"), WhereDefinition),
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
class DiscoveryConsulDefinition(BaseModel):
    AccessInfo: Optional[Sequence["_AccessInfoDefinition"]]
    PublishInfo: Optional[Sequence["_PublishInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DiscoveryConsulDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiscoveryConsulDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessInfo=deserialize_list(json_data.get("AccessInfo"), AccessInfoDefinition),
            PublishInfo=deserialize_list(json_data.get("PublishInfo"), PublishInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiscoveryConsulDefinition = DiscoveryConsulDefinition


@dataclass
class AccessInfoDefinition(BaseModel):
    InCluster: Optional[bool]
    Isolated: Optional[bool]
    Reachable: Optional[bool]
    ConnectionInfo: Optional[Sequence["_ConnectionInfoDefinition"]]
    KubeconfigUrl: Optional[Sequence["_KubeconfigUrlDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AccessInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            InCluster=json_data.get("InCluster"),
            Isolated=json_data.get("Isolated"),
            Reachable=json_data.get("Reachable"),
            ConnectionInfo=deserialize_list(json_data.get("ConnectionInfo"), ConnectionInfoDefinition),
            KubeconfigUrl=deserialize_list(json_data.get("KubeconfigUrl"), KubeconfigUrlDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessInfoDefinition = AccessInfoDefinition


@dataclass
class ConnectionInfoDefinition(BaseModel):
    ApiServer: Optional[str]
    TlsInfo: Optional[Sequence["_TlsInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiServer=json_data.get("ApiServer"),
            TlsInfo=deserialize_list(json_data.get("TlsInfo"), TlsInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionInfoDefinition = ConnectionInfoDefinition


@dataclass
class TlsInfoDefinition(BaseModel):
    Certificate: Optional[str]
    ServerName: Optional[str]
    TrustedCaUrl: Optional[str]
    CaCertificateUrl: Optional[Sequence["_CaCertificateUrlDefinition"]]
    CertificateUrl: Optional[Sequence["_CertificateUrlDefinition"]]
    KeyUrl: Optional[Sequence["_KeyUrlDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TlsInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            ServerName=json_data.get("ServerName"),
            TrustedCaUrl=json_data.get("TrustedCaUrl"),
            CaCertificateUrl=deserialize_list(json_data.get("CaCertificateUrl"), CaCertificateUrlDefinition),
            CertificateUrl=deserialize_list(json_data.get("CertificateUrl"), CertificateUrlDefinition),
            KeyUrl=deserialize_list(json_data.get("KeyUrl"), KeyUrlDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsInfoDefinition = TlsInfoDefinition


@dataclass
class CaCertificateUrlDefinition(BaseModel):
    SecretEncodingType: Optional[str]
    BlindfoldSecretInfo: Optional[Sequence["_BlindfoldSecretInfoDefinition"]]
    BlindfoldSecretInfoInternal: Optional[Sequence["_BlindfoldSecretInfoInternalDefinition"]]
    ClearSecretInfo: Optional[Sequence["_ClearSecretInfoDefinition"]]
    VaultSecretInfo: Optional[Sequence["_VaultSecretInfoDefinition"]]
    WingmanSecretInfo: Optional[Sequence["_WingmanSecretInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CaCertificateUrlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaCertificateUrlDefinition"]:
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
_CaCertificateUrlDefinition = CaCertificateUrlDefinition


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
class CertificateUrlDefinition(BaseModel):
    SecretEncodingType: Optional[str]
    BlindfoldSecretInfo: Optional[Sequence["_BlindfoldSecretInfoDefinition"]]
    BlindfoldSecretInfoInternal: Optional[Sequence["_BlindfoldSecretInfoInternalDefinition"]]
    ClearSecretInfo: Optional[Sequence["_ClearSecretInfoDefinition"]]
    VaultSecretInfo: Optional[Sequence["_VaultSecretInfoDefinition"]]
    WingmanSecretInfo: Optional[Sequence["_WingmanSecretInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateUrlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateUrlDefinition"]:
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
_CertificateUrlDefinition = CertificateUrlDefinition


@dataclass
class KeyUrlDefinition(BaseModel):
    SecretEncodingType: Optional[str]
    BlindfoldSecretInfo: Optional[Sequence["_BlindfoldSecretInfoDefinition"]]
    BlindfoldSecretInfoInternal: Optional[Sequence["_BlindfoldSecretInfoInternalDefinition"]]
    ClearSecretInfo: Optional[Sequence["_ClearSecretInfoDefinition"]]
    VaultSecretInfo: Optional[Sequence["_VaultSecretInfoDefinition"]]
    WingmanSecretInfo: Optional[Sequence["_WingmanSecretInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_KeyUrlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyUrlDefinition"]:
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
_KeyUrlDefinition = KeyUrlDefinition


@dataclass
class KubeconfigUrlDefinition(BaseModel):
    SecretEncodingType: Optional[str]
    BlindfoldSecretInfo: Optional[Sequence["_BlindfoldSecretInfoDefinition"]]
    BlindfoldSecretInfoInternal: Optional[Sequence["_BlindfoldSecretInfoInternalDefinition"]]
    ClearSecretInfo: Optional[Sequence["_ClearSecretInfoDefinition"]]
    VaultSecretInfo: Optional[Sequence["_VaultSecretInfoDefinition"]]
    WingmanSecretInfo: Optional[Sequence["_WingmanSecretInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_KubeconfigUrlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeconfigUrlDefinition"]:
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
_KubeconfigUrlDefinition = KubeconfigUrlDefinition


@dataclass
class PublishInfoDefinition(BaseModel):
    Disable: Optional[bool]
    PublishFqdns: Optional[bool]
    DnsDelegation: Optional[Sequence["_DnsDelegationDefinition"]]
    Publish: Optional[Sequence["_PublishDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PublishInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublishInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Disable=json_data.get("Disable"),
            PublishFqdns=json_data.get("PublishFqdns"),
            DnsDelegation=deserialize_list(json_data.get("DnsDelegation"), DnsDelegationDefinition),
            Publish=deserialize_list(json_data.get("Publish"), PublishDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublishInfoDefinition = PublishInfoDefinition


@dataclass
class DnsDelegationDefinition(BaseModel):
    DnsMode: Optional[str]
    Subdomain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsDelegationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsDelegationDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsMode=json_data.get("DnsMode"),
            Subdomain=json_data.get("Subdomain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsDelegationDefinition = DnsDelegationDefinition


@dataclass
class PublishDefinition(BaseModel):
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublishDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublishDefinition"]:
        if not json_data:
            return None
        return cls(
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublishDefinition = PublishDefinition


@dataclass
class DiscoveryK8sDefinition(BaseModel):
    AccessInfo: Optional[Sequence["_AccessInfoDefinition"]]
    PublishInfo: Optional[Sequence["_PublishInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DiscoveryK8sDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiscoveryK8sDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessInfo=deserialize_list(json_data.get("AccessInfo"), AccessInfoDefinition),
            PublishInfo=deserialize_list(json_data.get("PublishInfo"), PublishInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiscoveryK8sDefinition = DiscoveryK8sDefinition


@dataclass
class WhereDefinition(BaseModel):
    Site: Optional[Sequence["_SiteDefinition"]]
    VirtualNetwork: Optional[Sequence["_VirtualNetworkDefinition"]]
    VirtualSite: Optional[Sequence["_VirtualSiteDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WhereDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WhereDefinition"]:
        if not json_data:
            return None
        return cls(
            Site=deserialize_list(json_data.get("Site"), SiteDefinition),
            VirtualNetwork=deserialize_list(json_data.get("VirtualNetwork"), VirtualNetworkDefinition),
            VirtualSite=deserialize_list(json_data.get("VirtualSite"), VirtualSiteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WhereDefinition = WhereDefinition


@dataclass
class SiteDefinition(BaseModel):
    NetworkType: Optional[str]
    Ref: Optional[Sequence["_RefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SiteDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkType=json_data.get("NetworkType"),
            Ref=deserialize_list(json_data.get("Ref"), RefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SiteDefinition = SiteDefinition


@dataclass
class RefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RefDefinition = RefDefinition


@dataclass
class VirtualNetworkDefinition(BaseModel):
    Ref: Optional[Sequence["_RefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Ref=deserialize_list(json_data.get("Ref"), RefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNetworkDefinition = VirtualNetworkDefinition


@dataclass
class VirtualSiteDefinition(BaseModel):
    NetworkType: Optional[str]
    Ref: Optional[Sequence["_RefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualSiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualSiteDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkType=json_data.get("NetworkType"),
            Ref=deserialize_list(json_data.get("Ref"), RefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualSiteDefinition = VirtualSiteDefinition


