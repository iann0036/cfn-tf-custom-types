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
    AccountKeyPem: Optional[str]
    CertificateDomain: Optional[str]
    CertificateP12: Optional[str]
    CertificateP12Password: Optional[str]
    CertificatePem: Optional[str]
    CertificateRequestPem: Optional[str]
    CertificateUrl: Optional[str]
    CommonName: Optional[str]
    Id: Optional[str]
    IssuerPem: Optional[str]
    KeyType: Optional[str]
    MinDaysRemaining: Optional[float]
    MustStaple: Optional[bool]
    PrivateKeyPem: Optional[str]
    RecursiveNameservers: Optional[Sequence[str]]
    SubjectAlternativeNames: Optional[Sequence[str]]
    DnsChallenge: Optional[Sequence["_DnsChallenge"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccountKeyPem=json_data.get("AccountKeyPem"),
            CertificateDomain=json_data.get("CertificateDomain"),
            CertificateP12=json_data.get("CertificateP12"),
            CertificateP12Password=json_data.get("CertificateP12Password"),
            CertificatePem=json_data.get("CertificatePem"),
            CertificateRequestPem=json_data.get("CertificateRequestPem"),
            CertificateUrl=json_data.get("CertificateUrl"),
            CommonName=json_data.get("CommonName"),
            Id=json_data.get("Id"),
            IssuerPem=json_data.get("IssuerPem"),
            KeyType=json_data.get("KeyType"),
            MinDaysRemaining=json_data.get("MinDaysRemaining"),
            MustStaple=json_data.get("MustStaple"),
            PrivateKeyPem=json_data.get("PrivateKeyPem"),
            RecursiveNameservers=json_data.get("RecursiveNameservers"),
            SubjectAlternativeNames=json_data.get("SubjectAlternativeNames"),
            DnsChallenge=json_data.get("DnsChallenge"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DnsChallenge:
    Config: Optional[Sequence["_Config"]]
    Provider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsChallenge"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsChallenge"]:
        if not json_data:
            return None
        return cls(
            Config=json_data.get("Config"),
            Provider=json_data.get("Provider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsChallenge = DnsChallenge


@dataclass
class Config:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Config"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Config = Config


