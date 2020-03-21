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
    Arn: Optional[str]
    Certificate: Optional[str]
    CertificateChain: Optional[str]
    CertificateSigningRequest: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    NotAfter: Optional[str]
    NotBefore: Optional[str]
    PermanentDeletionTimeInDays: Optional[float]
    Serial: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Type: Optional[str]
    CertificateAuthorityConfiguration: Optional[Sequence["_CertificateAuthorityConfiguration"]]
    RevocationConfiguration: Optional[Sequence["_RevocationConfiguration"]]
    Timeouts: Optional["_Timeouts"]
    Subject: Optional[Sequence["_Subject"]]
    CrlConfiguration: Optional[Sequence["_CrlConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Certificate=json_data.get("Certificate"),
            CertificateChain=json_data.get("CertificateChain"),
            CertificateSigningRequest=json_data.get("CertificateSigningRequest"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            NotAfter=json_data.get("NotAfter"),
            NotBefore=json_data.get("NotBefore"),
            PermanentDeletionTimeInDays=json_data.get("PermanentDeletionTimeInDays"),
            Serial=json_data.get("Serial"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            CertificateAuthorityConfiguration=json_data.get("CertificateAuthorityConfiguration"),
            RevocationConfiguration=json_data.get("RevocationConfiguration"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Subject=json_data.get("Subject"),
            CrlConfiguration=json_data.get("CrlConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class CertificateAuthorityConfiguration:
    KeyAlgorithm: Optional[str]
    SigningAlgorithm: Optional[str]
    Subject: Optional[Sequence["_Subject"]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateAuthorityConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateAuthorityConfiguration"]:
        if not json_data:
            return None
        return cls(
            KeyAlgorithm=json_data.get("KeyAlgorithm"),
            SigningAlgorithm=json_data.get("SigningAlgorithm"),
            Subject=json_data.get("Subject"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateAuthorityConfiguration = CertificateAuthorityConfiguration


@dataclass
class Subject:
    CommonName: Optional[str]
    Country: Optional[str]
    DistinguishedNameQualifier: Optional[str]
    GenerationQualifier: Optional[str]
    GivenName: Optional[str]
    Initials: Optional[str]
    Locality: Optional[str]
    Organization: Optional[str]
    OrganizationalUnit: Optional[str]
    Pseudonym: Optional[str]
    State: Optional[str]
    Surname: Optional[str]
    Title: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Subject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subject"]:
        if not json_data:
            return None
        return cls(
            CommonName=json_data.get("CommonName"),
            Country=json_data.get("Country"),
            DistinguishedNameQualifier=json_data.get("DistinguishedNameQualifier"),
            GenerationQualifier=json_data.get("GenerationQualifier"),
            GivenName=json_data.get("GivenName"),
            Initials=json_data.get("Initials"),
            Locality=json_data.get("Locality"),
            Organization=json_data.get("Organization"),
            OrganizationalUnit=json_data.get("OrganizationalUnit"),
            Pseudonym=json_data.get("Pseudonym"),
            State=json_data.get("State"),
            Surname=json_data.get("Surname"),
            Title=json_data.get("Title"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subject = Subject


@dataclass
class RevocationConfiguration:
    CrlConfiguration: Optional[Sequence["_CrlConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_RevocationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RevocationConfiguration"]:
        if not json_data:
            return None
        return cls(
            CrlConfiguration=json_data.get("CrlConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RevocationConfiguration = RevocationConfiguration


@dataclass
class CrlConfiguration:
    CustomCname: Optional[str]
    Enabled: Optional[bool]
    ExpirationInDays: Optional[float]
    S3BucketName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CrlConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CrlConfiguration"]:
        if not json_data:
            return None
        return cls(
            CustomCname=json_data.get("CustomCname"),
            Enabled=json_data.get("Enabled"),
            ExpirationInDays=json_data.get("ExpirationInDays"),
            S3BucketName=json_data.get("S3BucketName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CrlConfiguration = CrlConfiguration


@dataclass
class Timeouts:
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


