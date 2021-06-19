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
    CertificateData: Optional[str]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    Extensions: Optional[Sequence["_ExtensionsDefinition"]]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    IsTrustVerificationDisabled: Optional[bool]
    IssuedBy: Optional[str]
    IssuerName: Optional[Sequence["_IssuerNameDefinition"]]
    PrivateKeyData: Optional[str]
    PublicKeyInfo: Optional[Sequence["_PublicKeyInfoDefinition"]]
    SerialNumber: Optional[str]
    SignatureAlgorithm: Optional[str]
    State: Optional[str]
    SubjectName: Optional[Sequence["_SubjectNameDefinition"]]
    TimeCreated: Optional[str]
    TimeNotValidAfter: Optional[str]
    TimeNotValidBefore: Optional[str]
    Version: Optional[float]
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
            CertificateData=json_data.get("CertificateData"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            Extensions=deserialize_list(json_data.get("Extensions"), ExtensionsDefinition),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            IsTrustVerificationDisabled=json_data.get("IsTrustVerificationDisabled"),
            IssuedBy=json_data.get("IssuedBy"),
            IssuerName=deserialize_list(json_data.get("IssuerName"), IssuerNameDefinition),
            PrivateKeyData=json_data.get("PrivateKeyData"),
            PublicKeyInfo=deserialize_list(json_data.get("PublicKeyInfo"), PublicKeyInfoDefinition),
            SerialNumber=json_data.get("SerialNumber"),
            SignatureAlgorithm=json_data.get("SignatureAlgorithm"),
            State=json_data.get("State"),
            SubjectName=deserialize_list(json_data.get("SubjectName"), SubjectNameDefinition),
            TimeCreated=json_data.get("TimeCreated"),
            TimeNotValidAfter=json_data.get("TimeNotValidAfter"),
            TimeNotValidBefore=json_data.get("TimeNotValidBefore"),
            Version=json_data.get("Version"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class ExtensionsDefinition(BaseModel):
    IsCritical: Optional[bool]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtensionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtensionsDefinition"]:
        if not json_data:
            return None
        return cls(
            IsCritical=json_data.get("IsCritical"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtensionsDefinition = ExtensionsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class IssuerNameDefinition(BaseModel):
    CommonName: Optional[str]
    Country: Optional[str]
    EmailAddress: Optional[str]
    Locality: Optional[str]
    Organization: Optional[str]
    OrganizationalUnit: Optional[str]
    StateProvince: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IssuerNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IssuerNameDefinition"]:
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
_IssuerNameDefinition = IssuerNameDefinition


@dataclass
class PublicKeyInfoDefinition(BaseModel):
    Algorithm: Optional[str]
    Exponent: Optional[float]
    KeySize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PublicKeyInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicKeyInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            Exponent=json_data.get("Exponent"),
            KeySize=json_data.get("KeySize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicKeyInfoDefinition = PublicKeyInfoDefinition


@dataclass
class SubjectNameDefinition(BaseModel):
    CommonName: Optional[str]
    Country: Optional[str]
    EmailAddress: Optional[str]
    Locality: Optional[str]
    Organization: Optional[str]
    OrganizationalUnit: Optional[str]
    StateProvince: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubjectNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectNameDefinition"]:
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
_SubjectNameDefinition = SubjectNameDefinition


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


