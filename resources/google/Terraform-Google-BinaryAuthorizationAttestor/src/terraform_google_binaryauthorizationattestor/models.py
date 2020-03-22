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
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    AttestationAuthorityNote: Optional[Sequence["_AttestationAuthorityNote"]]
    Timeouts: Optional["_Timeouts"]
    PublicKeys: Optional[Sequence["_PublicKeys"]]
    PkixPublicKey: Optional[Sequence["_PkixPublicKey"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            AttestationAuthorityNote=json_data.get("AttestationAuthorityNote"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            PublicKeys=json_data.get("PublicKeys"),
            PkixPublicKey=json_data.get("PkixPublicKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AttestationAuthorityNote:
    NoteReference: Optional[str]
    PublicKeys: Optional[Sequence["_PublicKeys"]]

    @classmethod
    def _deserialize(
        cls: Type["_AttestationAuthorityNote"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttestationAuthorityNote"]:
        if not json_data:
            return None
        return cls(
            NoteReference=json_data.get("NoteReference"),
            PublicKeys=json_data.get("PublicKeys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttestationAuthorityNote = AttestationAuthorityNote


@dataclass
class PublicKeys:
    AsciiArmoredPgpPublicKey: Optional[str]
    Comment: Optional[str]
    Id: Optional[str]
    PkixPublicKey: Optional[Sequence["_PkixPublicKey"]]

    @classmethod
    def _deserialize(
        cls: Type["_PublicKeys"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicKeys"]:
        if not json_data:
            return None
        return cls(
            AsciiArmoredPgpPublicKey=json_data.get("AsciiArmoredPgpPublicKey"),
            Comment=json_data.get("Comment"),
            Id=json_data.get("Id"),
            PkixPublicKey=json_data.get("PkixPublicKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicKeys = PublicKeys


@dataclass
class PkixPublicKey:
    PublicKeyPem: Optional[str]
    SignatureAlgorithm: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PkixPublicKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PkixPublicKey"]:
        if not json_data:
            return None
        return cls(
            PublicKeyPem=json_data.get("PublicKeyPem"),
            SignatureAlgorithm=json_data.get("SignatureAlgorithm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PkixPublicKey = PkixPublicKey


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


