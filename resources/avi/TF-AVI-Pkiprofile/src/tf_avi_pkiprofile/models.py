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
    CreatedBy: Optional[str]
    CrlCheck: Optional[bool]
    Id: Optional[str]
    IgnorePeerChain: Optional[bool]
    IsFederated: Optional[bool]
    Name: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    ValidateOnlyLeafCrl: Optional[bool]
    CaCerts: Optional[Sequence["_CaCertsDefinition"]]
    Crls: Optional[Sequence["_CrlsDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]

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
            CreatedBy=json_data.get("CreatedBy"),
            CrlCheck=json_data.get("CrlCheck"),
            Id=json_data.get("Id"),
            IgnorePeerChain=json_data.get("IgnorePeerChain"),
            IsFederated=json_data.get("IsFederated"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            ValidateOnlyLeafCrl=json_data.get("ValidateOnlyLeafCrl"),
            CaCerts=deserialize_list(json_data.get("CaCerts"), CaCertsDefinition),
            Crls=deserialize_list(json_data.get("Crls"), CrlsDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CaCertsDefinition(BaseModel):
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
        cls: Type["_CaCertsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaCertsDefinition"]:
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
_CaCertsDefinition = CaCertsDefinition


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
class CrlsDefinition(BaseModel):
    Body: Optional[str]
    CommonName: Optional[str]
    DistinguishedName: Optional[str]
    Etag: Optional[str]
    Fingerprint: Optional[str]
    LastRefreshed: Optional[str]
    LastUpdate: Optional[str]
    NextUpdate: Optional[str]
    ServerUrl: Optional[str]
    Text: Optional[str]
    UpdateInterval: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CrlsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CrlsDefinition"]:
        if not json_data:
            return None
        return cls(
            Body=json_data.get("Body"),
            CommonName=json_data.get("CommonName"),
            DistinguishedName=json_data.get("DistinguishedName"),
            Etag=json_data.get("Etag"),
            Fingerprint=json_data.get("Fingerprint"),
            LastRefreshed=json_data.get("LastRefreshed"),
            LastUpdate=json_data.get("LastUpdate"),
            NextUpdate=json_data.get("NextUpdate"),
            ServerUrl=json_data.get("ServerUrl"),
            Text=json_data.get("Text"),
            UpdateInterval=json_data.get("UpdateInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CrlsDefinition = CrlsDefinition


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


