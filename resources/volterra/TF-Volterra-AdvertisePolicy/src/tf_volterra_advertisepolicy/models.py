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
    Address: Optional[str]
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Description: Optional[str]
    Disable: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    SkipXffAppend: Optional[bool]
    PublicIp: Optional[Sequence["_PublicIpDefinition"]]
    TlsParameters: Optional[Sequence["_TlsParametersDefinition"]]
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
            Address=json_data.get("Address"),
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            SkipXffAppend=json_data.get("SkipXffAppend"),
            PublicIp=deserialize_list(json_data.get("PublicIp"), PublicIpDefinition),
            TlsParameters=deserialize_list(json_data.get("TlsParameters"), TlsParametersDefinition),
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


