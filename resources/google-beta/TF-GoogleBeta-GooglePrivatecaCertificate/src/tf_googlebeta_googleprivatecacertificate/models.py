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
    CertificateAuthority: Optional[str]
    CertificateDescription: Optional[Sequence["_CertificateDescriptionDefinition17"]]
    CreateTime: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Lifetime: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PemCertificate: Optional[str]
    PemCertificates: Optional[Sequence[str]]
    PemCsr: Optional[str]
    Project: Optional[str]
    RevocationDetails: Optional[Sequence["_RevocationDetailsDefinition"]]
    UpdateTime: Optional[str]
    Config: Optional[Sequence["_ConfigDefinition"]]
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
            CertificateAuthority=json_data.get("CertificateAuthority"),
            CertificateDescription=deserialize_list(json_data.get("CertificateDescription"), CertificateDescriptionDefinition17),
            CreateTime=json_data.get("CreateTime"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Lifetime=json_data.get("Lifetime"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PemCertificate=json_data.get("PemCertificate"),
            PemCertificates=json_data.get("PemCertificates"),
            PemCsr=json_data.get("PemCsr"),
            Project=json_data.get("Project"),
            RevocationDetails=deserialize_list(json_data.get("RevocationDetails"), RevocationDetailsDefinition),
            UpdateTime=json_data.get("UpdateTime"),
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CertificateDescriptionDefinition17(BaseModel):
    AiaIssuingCertificateUrls: Optional[Sequence[str]]
    AuthorityKeyId: Optional[Sequence["_CertificateDescriptionDefinition"]]
    CertFingerprint: Optional[Sequence["_CertificateDescriptionDefinition2"]]
    ConfigValues: Optional[Sequence["_CertificateDescriptionDefinition9"]]
    CrlDistributionPoints: Optional[Sequence[str]]
    PublicKey: Optional[Sequence["_CertificateDescriptionDefinition10"]]
    SubjectDescription: Optional[Sequence["_CertificateDescriptionDefinition15"]]
    SubjectKeyId: Optional[Sequence["_CertificateDescriptionDefinition16"]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDescriptionDefinition17"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDescriptionDefinition17"]:
        if not json_data:
            return None
        return cls(
            AiaIssuingCertificateUrls=json_data.get("AiaIssuingCertificateUrls"),
            AuthorityKeyId=deserialize_list(json_data.get("AuthorityKeyId"), CertificateDescriptionDefinition),
            CertFingerprint=deserialize_list(json_data.get("CertFingerprint"), CertificateDescriptionDefinition2),
            ConfigValues=deserialize_list(json_data.get("ConfigValues"), CertificateDescriptionDefinition9),
            CrlDistributionPoints=json_data.get("CrlDistributionPoints"),
            PublicKey=deserialize_list(json_data.get("PublicKey"), CertificateDescriptionDefinition10),
            SubjectDescription=deserialize_list(json_data.get("SubjectDescription"), CertificateDescriptionDefinition15),
            SubjectKeyId=deserialize_list(json_data.get("SubjectKeyId"), CertificateDescriptionDefinition16),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDescriptionDefinition17 = CertificateDescriptionDefinition17


@dataclass
class CertificateDescriptionDefinition(BaseModel):
    KeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDescriptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDescriptionDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyId=json_data.get("KeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDescriptionDefinition = CertificateDescriptionDefinition


@dataclass
class CertificateDescriptionDefinition2(BaseModel):
    Sha256Hash: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDescriptionDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDescriptionDefinition2"]:
        if not json_data:
            return None
        return cls(
            Sha256Hash=json_data.get("Sha256Hash"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDescriptionDefinition2 = CertificateDescriptionDefinition2


@dataclass
class CertificateDescriptionDefinition9(BaseModel):
    KeyUsage: Optional[Sequence["_CertificateDescriptionDefinition8"]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDescriptionDefinition9"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDescriptionDefinition9"]:
        if not json_data:
            return None
        return cls(
            KeyUsage=deserialize_list(json_data.get("KeyUsage"), CertificateDescriptionDefinition8),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDescriptionDefinition9 = CertificateDescriptionDefinition9


@dataclass
class CertificateDescriptionDefinition8(BaseModel):
    BaseKeyUsage: Optional[Sequence["_CertificateDescriptionDefinition4"]]
    ExtendedKeyUsage: Optional[Sequence["_CertificateDescriptionDefinition5"]]
    UnknownExtendedKeyUsages: Optional[Sequence["_CertificateDescriptionDefinition7"]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDescriptionDefinition8"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDescriptionDefinition8"]:
        if not json_data:
            return None
        return cls(
            BaseKeyUsage=deserialize_list(json_data.get("BaseKeyUsage"), CertificateDescriptionDefinition4),
            ExtendedKeyUsage=deserialize_list(json_data.get("ExtendedKeyUsage"), CertificateDescriptionDefinition5),
            UnknownExtendedKeyUsages=deserialize_list(json_data.get("UnknownExtendedKeyUsages"), CertificateDescriptionDefinition7),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDescriptionDefinition8 = CertificateDescriptionDefinition8


@dataclass
class CertificateDescriptionDefinition4(BaseModel):
    KeyUsageOptions: Optional[Sequence["_CertificateDescriptionDefinition3"]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDescriptionDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDescriptionDefinition4"]:
        if not json_data:
            return None
        return cls(
            KeyUsageOptions=deserialize_list(json_data.get("KeyUsageOptions"), CertificateDescriptionDefinition3),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDescriptionDefinition4 = CertificateDescriptionDefinition4


@dataclass
class CertificateDescriptionDefinition3(BaseModel):
    CertSign: Optional[bool]
    ContentCommitment: Optional[bool]
    CrlSign: Optional[bool]
    DataEncipherment: Optional[bool]
    DecipherOnly: Optional[bool]
    DigitalSignature: Optional[bool]
    EncipherOnly: Optional[bool]
    KeyAgreement: Optional[bool]
    KeyEncipherment: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDescriptionDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDescriptionDefinition3"]:
        if not json_data:
            return None
        return cls(
            CertSign=json_data.get("CertSign"),
            ContentCommitment=json_data.get("ContentCommitment"),
            CrlSign=json_data.get("CrlSign"),
            DataEncipherment=json_data.get("DataEncipherment"),
            DecipherOnly=json_data.get("DecipherOnly"),
            DigitalSignature=json_data.get("DigitalSignature"),
            EncipherOnly=json_data.get("EncipherOnly"),
            KeyAgreement=json_data.get("KeyAgreement"),
            KeyEncipherment=json_data.get("KeyEncipherment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDescriptionDefinition3 = CertificateDescriptionDefinition3


@dataclass
class CertificateDescriptionDefinition5(BaseModel):
    ClientAuth: Optional[bool]
    CodeSigning: Optional[bool]
    EmailProtection: Optional[bool]
    OcspSigning: Optional[bool]
    ServerAuth: Optional[bool]
    TimeStamping: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDescriptionDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDescriptionDefinition5"]:
        if not json_data:
            return None
        return cls(
            ClientAuth=json_data.get("ClientAuth"),
            CodeSigning=json_data.get("CodeSigning"),
            EmailProtection=json_data.get("EmailProtection"),
            OcspSigning=json_data.get("OcspSigning"),
            ServerAuth=json_data.get("ServerAuth"),
            TimeStamping=json_data.get("TimeStamping"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDescriptionDefinition5 = CertificateDescriptionDefinition5


@dataclass
class CertificateDescriptionDefinition7(BaseModel):
    ObectId: Optional[Sequence["_CertificateDescriptionDefinition6"]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDescriptionDefinition7"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDescriptionDefinition7"]:
        if not json_data:
            return None
        return cls(
            ObectId=deserialize_list(json_data.get("ObectId"), CertificateDescriptionDefinition6),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDescriptionDefinition7 = CertificateDescriptionDefinition7


@dataclass
class CertificateDescriptionDefinition6(BaseModel):
    ObjectIdPath: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDescriptionDefinition6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDescriptionDefinition6"]:
        if not json_data:
            return None
        return cls(
            ObjectIdPath=json_data.get("ObjectIdPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDescriptionDefinition6 = CertificateDescriptionDefinition6


@dataclass
class CertificateDescriptionDefinition10(BaseModel):
    Key: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDescriptionDefinition10"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDescriptionDefinition10"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDescriptionDefinition10 = CertificateDescriptionDefinition10


@dataclass
class CertificateDescriptionDefinition15(BaseModel):
    CommonName: Optional[str]
    HexSerialNumber: Optional[str]
    Lifetime: Optional[str]
    NotAfterTime: Optional[str]
    NotBeforeTime: Optional[str]
    Subject: Optional[Sequence["_CertificateDescriptionDefinition11"]]
    SubjectAltName: Optional[Sequence["_CertificateDescriptionDefinition14"]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDescriptionDefinition15"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDescriptionDefinition15"]:
        if not json_data:
            return None
        return cls(
            CommonName=json_data.get("CommonName"),
            HexSerialNumber=json_data.get("HexSerialNumber"),
            Lifetime=json_data.get("Lifetime"),
            NotAfterTime=json_data.get("NotAfterTime"),
            NotBeforeTime=json_data.get("NotBeforeTime"),
            Subject=deserialize_list(json_data.get("Subject"), CertificateDescriptionDefinition11),
            SubjectAltName=deserialize_list(json_data.get("SubjectAltName"), CertificateDescriptionDefinition14),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDescriptionDefinition15 = CertificateDescriptionDefinition15


@dataclass
class CertificateDescriptionDefinition11(BaseModel):
    CountryCode: Optional[str]
    Locality: Optional[str]
    Organization: Optional[str]
    OrganizationalUnit: Optional[str]
    PostalCode: Optional[str]
    Province: Optional[str]
    StreetAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDescriptionDefinition11"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDescriptionDefinition11"]:
        if not json_data:
            return None
        return cls(
            CountryCode=json_data.get("CountryCode"),
            Locality=json_data.get("Locality"),
            Organization=json_data.get("Organization"),
            OrganizationalUnit=json_data.get("OrganizationalUnit"),
            PostalCode=json_data.get("PostalCode"),
            Province=json_data.get("Province"),
            StreetAddress=json_data.get("StreetAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDescriptionDefinition11 = CertificateDescriptionDefinition11


@dataclass
class CertificateDescriptionDefinition14(BaseModel):
    CustomSans: Optional[Sequence["_CertificateDescriptionDefinition13"]]
    DnsNames: Optional[Sequence[str]]
    EmailAddresses: Optional[Sequence[str]]
    IpAddresses: Optional[Sequence[str]]
    Uris: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDescriptionDefinition14"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDescriptionDefinition14"]:
        if not json_data:
            return None
        return cls(
            CustomSans=deserialize_list(json_data.get("CustomSans"), CertificateDescriptionDefinition13),
            DnsNames=json_data.get("DnsNames"),
            EmailAddresses=json_data.get("EmailAddresses"),
            IpAddresses=json_data.get("IpAddresses"),
            Uris=json_data.get("Uris"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDescriptionDefinition14 = CertificateDescriptionDefinition14


@dataclass
class CertificateDescriptionDefinition13(BaseModel):
    Critical: Optional[bool]
    ObectId: Optional[Sequence["_CertificateDescriptionDefinition12"]]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDescriptionDefinition13"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDescriptionDefinition13"]:
        if not json_data:
            return None
        return cls(
            Critical=json_data.get("Critical"),
            ObectId=deserialize_list(json_data.get("ObectId"), CertificateDescriptionDefinition12),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDescriptionDefinition13 = CertificateDescriptionDefinition13


@dataclass
class CertificateDescriptionDefinition12(BaseModel):
    ObjectIdPath: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDescriptionDefinition12"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDescriptionDefinition12"]:
        if not json_data:
            return None
        return cls(
            ObjectIdPath=json_data.get("ObjectIdPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDescriptionDefinition12 = CertificateDescriptionDefinition12


@dataclass
class CertificateDescriptionDefinition16(BaseModel):
    KeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDescriptionDefinition16"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDescriptionDefinition16"]:
        if not json_data:
            return None
        return cls(
            KeyId=json_data.get("KeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDescriptionDefinition16 = CertificateDescriptionDefinition16


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
class RevocationDetailsDefinition(BaseModel):
    RevocationState: Optional[str]
    RevocationTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RevocationDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RevocationDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            RevocationState=json_data.get("RevocationState"),
            RevocationTime=json_data.get("RevocationTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RevocationDetailsDefinition = RevocationDetailsDefinition


@dataclass
class ConfigDefinition(BaseModel):
    PublicKey: Optional[Sequence["_PublicKeyDefinition"]]
    ReusableConfig: Optional[Sequence["_ReusableConfigDefinition"]]
    SubjectConfig: Optional[Sequence["_SubjectConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            PublicKey=deserialize_list(json_data.get("PublicKey"), PublicKeyDefinition),
            ReusableConfig=deserialize_list(json_data.get("ReusableConfig"), ReusableConfigDefinition),
            SubjectConfig=deserialize_list(json_data.get("SubjectConfig"), SubjectConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


@dataclass
class PublicKeyDefinition(BaseModel):
    Key: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicKeyDefinition = PublicKeyDefinition


@dataclass
class ReusableConfigDefinition(BaseModel):
    ReusableConfig: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReusableConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReusableConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ReusableConfig=json_data.get("ReusableConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReusableConfigDefinition = ReusableConfigDefinition


@dataclass
class SubjectConfigDefinition(BaseModel):
    CommonName: Optional[str]
    Subject: Optional[Sequence["_SubjectDefinition"]]
    SubjectAltName: Optional[Sequence["_SubjectAltNameDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubjectConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CommonName=json_data.get("CommonName"),
            Subject=deserialize_list(json_data.get("Subject"), SubjectDefinition),
            SubjectAltName=deserialize_list(json_data.get("SubjectAltName"), SubjectAltNameDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubjectConfigDefinition = SubjectConfigDefinition


@dataclass
class SubjectDefinition(BaseModel):
    CountryCode: Optional[str]
    Locality: Optional[str]
    Organization: Optional[str]
    OrganizationalUnit: Optional[str]
    PostalCode: Optional[str]
    Province: Optional[str]
    StreetAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubjectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectDefinition"]:
        if not json_data:
            return None
        return cls(
            CountryCode=json_data.get("CountryCode"),
            Locality=json_data.get("Locality"),
            Organization=json_data.get("Organization"),
            OrganizationalUnit=json_data.get("OrganizationalUnit"),
            PostalCode=json_data.get("PostalCode"),
            Province=json_data.get("Province"),
            StreetAddress=json_data.get("StreetAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubjectDefinition = SubjectDefinition


@dataclass
class SubjectAltNameDefinition(BaseModel):
    DnsNames: Optional[Sequence[str]]
    EmailAddresses: Optional[Sequence[str]]
    IpAddresses: Optional[Sequence[str]]
    Uris: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SubjectAltNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectAltNameDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsNames=json_data.get("DnsNames"),
            EmailAddresses=json_data.get("EmailAddresses"),
            IpAddresses=json_data.get("IpAddresses"),
            Uris=json_data.get("Uris"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubjectAltNameDefinition = SubjectAltNameDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


