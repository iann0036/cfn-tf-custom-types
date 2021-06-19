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
    ConnectionTimeout: Optional[float]
    DefaultSubset: Optional[Sequence["_DefaultSubsetDefinition"]]
    Description: Optional[str]
    Disable: Optional[bool]
    EndpointSelection: Optional[str]
    FallbackPolicy: Optional[str]
    HttpIdleTimeout: Optional[float]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    LoadbalancerAlgorithm: Optional[str]
    Name: Optional[str]
    Namespace: Optional[str]
    NoPanicThreshold: Optional[bool]
    PanicThreshold: Optional[float]
    CircuitBreaker: Optional[Sequence["_CircuitBreakerDefinition"]]
    EndpointSubsets: Optional[Sequence["_EndpointSubsetsDefinition"]]
    Endpoints: Optional[Sequence["_EndpointsDefinition"]]
    HealthChecks: Optional[Sequence["_HealthChecksDefinition"]]
    Http2Options: Optional[Sequence["_Http2OptionsDefinition"]]
    OutlierDetection: Optional[Sequence["_OutlierDetectionDefinition"]]
    TlsParameters: Optional[Sequence["_TlsParametersDefinition"]]

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
            ConnectionTimeout=json_data.get("ConnectionTimeout"),
            DefaultSubset=deserialize_list(json_data.get("DefaultSubset"), DefaultSubsetDefinition),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            EndpointSelection=json_data.get("EndpointSelection"),
            FallbackPolicy=json_data.get("FallbackPolicy"),
            HttpIdleTimeout=json_data.get("HttpIdleTimeout"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            LoadbalancerAlgorithm=json_data.get("LoadbalancerAlgorithm"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            NoPanicThreshold=json_data.get("NoPanicThreshold"),
            PanicThreshold=json_data.get("PanicThreshold"),
            CircuitBreaker=deserialize_list(json_data.get("CircuitBreaker"), CircuitBreakerDefinition),
            EndpointSubsets=deserialize_list(json_data.get("EndpointSubsets"), EndpointSubsetsDefinition),
            Endpoints=deserialize_list(json_data.get("Endpoints"), EndpointsDefinition),
            HealthChecks=deserialize_list(json_data.get("HealthChecks"), HealthChecksDefinition),
            Http2Options=deserialize_list(json_data.get("Http2Options"), Http2OptionsDefinition),
            OutlierDetection=deserialize_list(json_data.get("OutlierDetection"), OutlierDetectionDefinition),
            TlsParameters=deserialize_list(json_data.get("TlsParameters"), TlsParametersDefinition),
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
class DefaultSubsetDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultSubsetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultSubsetDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultSubsetDefinition = DefaultSubsetDefinition


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
class CircuitBreakerDefinition(BaseModel):
    ConnectionLimit: Optional[float]
    MaxRequests: Optional[float]
    PendingRequests: Optional[float]
    Priority: Optional[str]
    Retries: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CircuitBreakerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CircuitBreakerDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionLimit=json_data.get("ConnectionLimit"),
            MaxRequests=json_data.get("MaxRequests"),
            PendingRequests=json_data.get("PendingRequests"),
            Priority=json_data.get("Priority"),
            Retries=json_data.get("Retries"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CircuitBreakerDefinition = CircuitBreakerDefinition


@dataclass
class EndpointSubsetsDefinition(BaseModel):
    Keys: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointSubsetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointSubsetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Keys=json_data.get("Keys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointSubsetsDefinition = EndpointSubsetsDefinition


@dataclass
class EndpointsDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointsDefinition = EndpointsDefinition


@dataclass
class HealthChecksDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HealthChecksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthChecksDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthChecksDefinition = HealthChecksDefinition


@dataclass
class Http2OptionsDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Http2OptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Http2OptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Http2OptionsDefinition = Http2OptionsDefinition


@dataclass
class OutlierDetectionDefinition(BaseModel):
    BaseEjectionTime: Optional[float]
    Consecutive5xx: Optional[float]
    ConsecutiveGatewayFailure: Optional[float]
    Interval: Optional[float]
    MaxEjectionPercent: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OutlierDetectionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutlierDetectionDefinition"]:
        if not json_data:
            return None
        return cls(
            BaseEjectionTime=json_data.get("BaseEjectionTime"),
            Consecutive5xx=json_data.get("Consecutive5xx"),
            ConsecutiveGatewayFailure=json_data.get("ConsecutiveGatewayFailure"),
            Interval=json_data.get("Interval"),
            MaxEjectionPercent=json_data.get("MaxEjectionPercent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutlierDetectionDefinition = OutlierDetectionDefinition


@dataclass
class TlsParametersDefinition(BaseModel):
    DisableSni: Optional[bool]
    Sni: Optional[str]
    UseHostHeaderAsSni: Optional[bool]
    CommonParams: Optional[Sequence["_CommonParamsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TlsParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableSni=json_data.get("DisableSni"),
            Sni=json_data.get("Sni"),
            UseHostHeaderAsSni=json_data.get("UseHostHeaderAsSni"),
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


