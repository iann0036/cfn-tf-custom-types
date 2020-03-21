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
    CertificateData: Optional[str]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    Extensions: Optional[Sequence["_Extensions"]]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Id: Optional[str]
    IsTrustVerificationDisabled: Optional[bool]
    IssuedBy: Optional[str]
    IssuerName: Optional[Sequence["_IssuerName"]]
    PrivateKeyData: Optional[str]
    PublicKeyInfo: Optional[Sequence["_PublicKeyInfo"]]
    SerialNumber: Optional[str]
    SignatureAlgorithm: Optional[str]
    State: Optional[str]
    SubjectName: Optional[Sequence["_SubjectName"]]
    TimeCreated: Optional[str]
    TimeNotValidAfter: Optional[str]
    TimeNotValidBefore: Optional[str]
    Version: Optional[float]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CertificateData=json_data.get("CertificateData"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            Extensions=json_data.get("Extensions"),
            FreeformTags=json_data.get("FreeformTags"),
            Id=json_data.get("Id"),
            IsTrustVerificationDisabled=json_data.get("IsTrustVerificationDisabled"),
            IssuedBy=json_data.get("IssuedBy"),
            IssuerName=json_data.get("IssuerName"),
            PrivateKeyData=json_data.get("PrivateKeyData"),
            PublicKeyInfo=json_data.get("PublicKeyInfo"),
            SerialNumber=json_data.get("SerialNumber"),
            SignatureAlgorithm=json_data.get("SignatureAlgorithm"),
            State=json_data.get("State"),
            SubjectName=json_data.get("SubjectName"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeNotValidAfter=json_data.get("TimeNotValidAfter"),
            TimeNotValidBefore=json_data.get("TimeNotValidBefore"),
            Version=json_data.get("Version"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class Extensions:
    IsCritical: Optional[bool]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Extensions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Extensions"]:
        if not json_data:
            return None
        return cls(
            IsCritical=json_data.get("IsCritical"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Extensions = Extensions


@dataclass
class FreeformTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class IssuerName:
    CommonName: Optional[str]
    Country: Optional[str]
    EmailAddress: Optional[str]
    Locality: Optional[str]
    Organization: Optional[str]
    OrganizationalUnit: Optional[str]
    StateProvince: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IssuerName"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IssuerName"]:
        if not json_data:
            return None
        return cls(
            CommonName=json_data.get("CommonName"),
            Country=json_data.get("Country"),
            EmailAddress=json_data.get("EmailAddress"),
            Locality=json_data.get("Locality"),
            Organization=json_data.get("Organization"),
            OrganizationalUnit=json_data.get("OrganizationalUnit"),
            StateProvince=json_data.get("StateProvince"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IssuerName = IssuerName


@dataclass
class PublicKeyInfo:
    Algorithm: Optional[str]
    Exponent: Optional[float]
    KeySize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PublicKeyInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicKeyInfo"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            Exponent=json_data.get("Exponent"),
            KeySize=json_data.get("KeySize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicKeyInfo = PublicKeyInfo


@dataclass
class SubjectName:
    CommonName: Optional[str]
    Country: Optional[str]
    EmailAddress: Optional[str]
    Locality: Optional[str]
    Organization: Optional[str]
    OrganizationalUnit: Optional[str]
    StateProvince: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubjectName"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectName"]:
        if not json_data:
            return None
        return cls(
            CommonName=json_data.get("CommonName"),
            Country=json_data.get("Country"),
            EmailAddress=json_data.get("EmailAddress"),
            Locality=json_data.get("Locality"),
            Organization=json_data.get("Organization"),
            OrganizationalUnit=json_data.get("OrganizationalUnit"),
            StateProvince=json_data.get("StateProvince"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubjectName = SubjectName


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


