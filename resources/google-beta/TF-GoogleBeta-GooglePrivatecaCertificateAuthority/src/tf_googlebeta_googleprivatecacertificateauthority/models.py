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
    AccessUrls: Optional[Sequence["_AccessUrlsDefinition"]]
    CertificateAuthorityId: Optional[str]
    CreateTime: Optional[str]
    DisableOnDelete: Optional[bool]
    GcsBucket: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Lifetime: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PemCaCertificates: Optional[Sequence[str]]
    Project: Optional[str]
    State: Optional[str]
    Tier: Optional[str]
    Type: Optional[str]
    UpdateTime: Optional[str]
    Config: Optional[Sequence["_ConfigDefinition"]]
    IssuingOptions: Optional[Sequence["_IssuingOptionsDefinition"]]
    KeySpec: Optional[Sequence["_KeySpecDefinition"]]
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
            AccessUrls=deserialize_list(json_data.get("AccessUrls"), AccessUrlsDefinition),
            CertificateAuthorityId=json_data.get("CertificateAuthorityId"),
            CreateTime=json_data.get("CreateTime"),
            DisableOnDelete=json_data.get("DisableOnDelete"),
            GcsBucket=json_data.get("GcsBucket"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Lifetime=json_data.get("Lifetime"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PemCaCertificates=json_data.get("PemCaCertificates"),
            Project=json_data.get("Project"),
            State=json_data.get("State"),
            Tier=json_data.get("Tier"),
            Type=json_data.get("Type"),
            UpdateTime=json_data.get("UpdateTime"),
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
            IssuingOptions=deserialize_list(json_data.get("IssuingOptions"), IssuingOptionsDefinition),
            KeySpec=deserialize_list(json_data.get("KeySpec"), KeySpecDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccessUrlsDefinition(BaseModel):
    CaCertificateAccessUrl: Optional[str]
    CrlAccessUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessUrlsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessUrlsDefinition"]:
        if not json_data:
            return None
        return cls(
            CaCertificateAccessUrl=json_data.get("CaCertificateAccessUrl"),
            CrlAccessUrl=json_data.get("CrlAccessUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessUrlsDefinition = AccessUrlsDefinition


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
class ConfigDefinition(BaseModel):
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
            ReusableConfig=deserialize_list(json_data.get("ReusableConfig"), ReusableConfigDefinition),
            SubjectConfig=deserialize_list(json_data.get("SubjectConfig"), SubjectConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


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
class IssuingOptionsDefinition(BaseModel):
    IncludeCaCertUrl: Optional[bool]
    IncludeCrlAccessUrl: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_IssuingOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IssuingOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            IncludeCaCertUrl=json_data.get("IncludeCaCertUrl"),
            IncludeCrlAccessUrl=json_data.get("IncludeCrlAccessUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IssuingOptionsDefinition = IssuingOptionsDefinition


@dataclass
class KeySpecDefinition(BaseModel):
    Algorithm: Optional[str]
    CloudKmsKeyVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeySpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeySpecDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            CloudKmsKeyVersion=json_data.get("CloudKmsKeyVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeySpecDefinition = KeySpecDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


