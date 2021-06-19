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
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Type: Optional[str]
    CertificateAuthorityConfiguration: Optional[Sequence["_CertificateAuthorityConfigurationDefinition"]]
    RevocationConfiguration: Optional[Sequence["_RevocationConfigurationDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Type=json_data.get("Type"),
            CertificateAuthorityConfiguration=deserialize_list(json_data.get("CertificateAuthorityConfiguration"), CertificateAuthorityConfigurationDefinition),
            RevocationConfiguration=deserialize_list(json_data.get("RevocationConfiguration"), RevocationConfigurationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class CertificateAuthorityConfigurationDefinition(BaseModel):
    KeyAlgorithm: Optional[str]
    SigningAlgorithm: Optional[str]
    Subject: Optional[Sequence["_SubjectDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateAuthorityConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateAuthorityConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyAlgorithm=json_data.get("KeyAlgorithm"),
            SigningAlgorithm=json_data.get("SigningAlgorithm"),
            Subject=deserialize_list(json_data.get("Subject"), SubjectDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateAuthorityConfigurationDefinition = CertificateAuthorityConfigurationDefinition


@dataclass
class SubjectDefinition(BaseModel):
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
        cls: Type["_SubjectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectDefinition"]:
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
_SubjectDefinition = SubjectDefinition


@dataclass
class RevocationConfigurationDefinition(BaseModel):
    CrlConfiguration: Optional[Sequence["_CrlConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RevocationConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RevocationConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            CrlConfiguration=deserialize_list(json_data.get("CrlConfiguration"), CrlConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RevocationConfigurationDefinition = RevocationConfigurationDefinition


@dataclass
class CrlConfigurationDefinition(BaseModel):
    CustomCname: Optional[str]
    Enabled: Optional[bool]
    ExpirationInDays: Optional[float]
    S3BucketName: Optional[str]
    S3ObjectAcl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CrlConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CrlConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomCname=json_data.get("CustomCname"),
            Enabled=json_data.get("Enabled"),
            ExpirationInDays=json_data.get("ExpirationInDays"),
            S3BucketName=json_data.get("S3BucketName"),
            S3ObjectAcl=json_data.get("S3ObjectAcl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CrlConfigurationDefinition = CrlConfigurationDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


