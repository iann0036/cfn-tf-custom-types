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
    CertificateBase64: Optional[bool]
    CertificateManagementProfileRef: Optional[str]
    CreatedBy: Optional[str]
    EnableOcspStapling: Optional[bool]
    EnckeyBase64: Optional[str]
    EnckeyName: Optional[str]
    Format: Optional[str]
    HardwaresecuritymodulegroupRef: Optional[str]
    Id: Optional[str]
    Key: Optional[str]
    KeyBase64: Optional[bool]
    KeyPassphrase: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    TenantRef: Optional[str]
    Type: Optional[str]
    Uuid: Optional[str]
    CaCerts: Optional[Sequence["_CaCertsDefinition"]]
    Certificate: Optional[Sequence["_CertificateDefinition"]]
    DynamicParams: Optional[Sequence["_DynamicParamsDefinition"]]
    KeyParams: Optional[Sequence["_KeyParamsDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    OcspConfig: Optional[Sequence["_OcspConfigDefinition"]]

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
            CertificateBase64=json_data.get("CertificateBase64"),
            CertificateManagementProfileRef=json_data.get("CertificateManagementProfileRef"),
            CreatedBy=json_data.get("CreatedBy"),
            EnableOcspStapling=json_data.get("EnableOcspStapling"),
            EnckeyBase64=json_data.get("EnckeyBase64"),
            EnckeyName=json_data.get("EnckeyName"),
            Format=json_data.get("Format"),
            HardwaresecuritymodulegroupRef=json_data.get("HardwaresecuritymodulegroupRef"),
            Id=json_data.get("Id"),
            Key=json_data.get("Key"),
            KeyBase64=json_data.get("KeyBase64"),
            KeyPassphrase=json_data.get("KeyPassphrase"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            TenantRef=json_data.get("TenantRef"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
            CaCerts=deserialize_list(json_data.get("CaCerts"), CaCertsDefinition),
            Certificate=deserialize_list(json_data.get("Certificate"), CertificateDefinition),
            DynamicParams=deserialize_list(json_data.get("DynamicParams"), DynamicParamsDefinition),
            KeyParams=deserialize_list(json_data.get("KeyParams"), KeyParamsDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            OcspConfig=deserialize_list(json_data.get("OcspConfig"), OcspConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CaCertsDefinition(BaseModel):
    CaRef: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CaCertsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaCertsDefinition"]:
        if not json_data:
            return None
        return cls(
            CaRef=json_data.get("CaRef"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaCertsDefinition = CaCertsDefinition


@dataclass
class CertificateDefinition(BaseModel):
    Certificate: Optional[str]
    CertificateSigningRequest: Optional[str]
    ChainVerified: Optional[bool]
    DaysUntilExpire: Optional[float]
    ExpiryStatus: Optional[str]
    Fingerprint: Optional[str]
    NotAfter: Optional[str]
    NotBefore: Optional[str]
    PublicKey: Optional[str]
    SelfSigned: Optional[bool]
    SerialNumber: Optional[str]
    Signature: Optional[str]
    SignatureAlgorithm: Optional[str]
    SubjectAltNames: Optional[Sequence[str]]
    Text: Optional[str]
    Version: Optional[str]
    Issuer: Optional[Sequence["_IssuerDefinition"]]
    KeyParams: Optional[Sequence["_KeyParamsDefinition"]]
    Subject: Optional[Sequence["_SubjectDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            CertificateSigningRequest=json_data.get("CertificateSigningRequest"),
            ChainVerified=json_data.get("ChainVerified"),
            DaysUntilExpire=json_data.get("DaysUntilExpire"),
            ExpiryStatus=json_data.get("ExpiryStatus"),
            Fingerprint=json_data.get("Fingerprint"),
            NotAfter=json_data.get("NotAfter"),
            NotBefore=json_data.get("NotBefore"),
            PublicKey=json_data.get("PublicKey"),
            SelfSigned=json_data.get("SelfSigned"),
            SerialNumber=json_data.get("SerialNumber"),
            Signature=json_data.get("Signature"),
            SignatureAlgorithm=json_data.get("SignatureAlgorithm"),
            SubjectAltNames=json_data.get("SubjectAltNames"),
            Text=json_data.get("Text"),
            Version=json_data.get("Version"),
            Issuer=deserialize_list(json_data.get("Issuer"), IssuerDefinition),
            KeyParams=deserialize_list(json_data.get("KeyParams"), KeyParamsDefinition),
            Subject=deserialize_list(json_data.get("Subject"), SubjectDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDefinition = CertificateDefinition


@dataclass
class IssuerDefinition(BaseModel):
    CommonName: Optional[str]
    Country: Optional[str]
    DistinguishedName: Optional[str]
    EmailAddress: Optional[str]
    Locality: Optional[str]
    Organization: Optional[str]
    OrganizationUnit: Optional[str]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IssuerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IssuerDefinition"]:
        if not json_data:
            return None
        return cls(
            CommonName=json_data.get("CommonName"),
            Country=json_data.get("Country"),
            DistinguishedName=json_data.get("DistinguishedName"),
            EmailAddress=json_data.get("EmailAddress"),
            Locality=json_data.get("Locality"),
            Organization=json_data.get("Organization"),
            OrganizationUnit=json_data.get("OrganizationUnit"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IssuerDefinition = IssuerDefinition


@dataclass
class KeyParamsDefinition(BaseModel):
    Algorithm: Optional[str]
    EcParams: Optional[Sequence["_EcParamsDefinition"]]
    RsaParams: Optional[Sequence["_RsaParamsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_KeyParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            EcParams=deserialize_list(json_data.get("EcParams"), EcParamsDefinition),
            RsaParams=deserialize_list(json_data.get("RsaParams"), RsaParamsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyParamsDefinition = KeyParamsDefinition


@dataclass
class EcParamsDefinition(BaseModel):
    Curve: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EcParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            Curve=json_data.get("Curve"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcParamsDefinition = EcParamsDefinition


@dataclass
class RsaParamsDefinition(BaseModel):
    Exponent: Optional[float]
    KeySize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RsaParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RsaParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            Exponent=json_data.get("Exponent"),
            KeySize=json_data.get("KeySize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RsaParamsDefinition = RsaParamsDefinition


@dataclass
class SubjectDefinition(BaseModel):
    CommonName: Optional[str]
    Country: Optional[str]
    DistinguishedName: Optional[str]
    EmailAddress: Optional[str]
    Locality: Optional[str]
    Organization: Optional[str]
    OrganizationUnit: Optional[str]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubjectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectDefinition"]:
        if not json_data:
            return None
        return cls(
            CommonName=json_data.get("CommonName"),
            Country=json_data.get("Country"),
            DistinguishedName=json_data.get("DistinguishedName"),
            EmailAddress=json_data.get("EmailAddress"),
            Locality=json_data.get("Locality"),
            Organization=json_data.get("Organization"),
            OrganizationUnit=json_data.get("OrganizationUnit"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubjectDefinition = SubjectDefinition


@dataclass
class DynamicParamsDefinition(BaseModel):
    IsDynamic: Optional[bool]
    IsSensitive: Optional[bool]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            IsDynamic=json_data.get("IsDynamic"),
            IsSensitive=json_data.get("IsSensitive"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicParamsDefinition = DynamicParamsDefinition


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


@dataclass
class OcspConfigDefinition(BaseModel):
    FailedOcspJobsRetryInterval: Optional[float]
    MaxTries: Optional[float]
    OcspReqInterval: Optional[float]
    OcspRespTimeout: Optional[float]
    ResponderUrlLists: Optional[Sequence[str]]
    UrlAction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OcspConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OcspConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            FailedOcspJobsRetryInterval=json_data.get("FailedOcspJobsRetryInterval"),
            MaxTries=json_data.get("MaxTries"),
            OcspReqInterval=json_data.get("OcspReqInterval"),
            OcspRespTimeout=json_data.get("OcspRespTimeout"),
            ResponderUrlLists=json_data.get("ResponderUrlLists"),
            UrlAction=json_data.get("UrlAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OcspConfigDefinition = OcspConfigDefinition


