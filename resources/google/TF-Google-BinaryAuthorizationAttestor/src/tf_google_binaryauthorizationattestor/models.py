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
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    AttestationAuthorityNote: Optional[Sequence["_AttestationAuthorityNoteDefinition"]]
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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            AttestationAuthorityNote=deserialize_list(json_data.get("AttestationAuthorityNote"), AttestationAuthorityNoteDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AttestationAuthorityNoteDefinition(BaseModel):
    NoteReference: Optional[str]
    PublicKeys: Optional[Sequence["_PublicKeysDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AttestationAuthorityNoteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttestationAuthorityNoteDefinition"]:
        if not json_data:
            return None
        return cls(
            NoteReference=json_data.get("NoteReference"),
            PublicKeys=deserialize_list(json_data.get("PublicKeys"), PublicKeysDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttestationAuthorityNoteDefinition = AttestationAuthorityNoteDefinition


@dataclass
class PublicKeysDefinition(BaseModel):
    AsciiArmoredPgpPublicKey: Optional[str]
    Comment: Optional[str]
    Id: Optional[str]
    PkixPublicKey: Optional[Sequence["_PkixPublicKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PublicKeysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicKeysDefinition"]:
        if not json_data:
            return None
        return cls(
            AsciiArmoredPgpPublicKey=json_data.get("AsciiArmoredPgpPublicKey"),
            Comment=json_data.get("Comment"),
            Id=json_data.get("Id"),
            PkixPublicKey=deserialize_list(json_data.get("PkixPublicKey"), PkixPublicKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicKeysDefinition = PublicKeysDefinition


@dataclass
class PkixPublicKeyDefinition(BaseModel):
    PublicKeyPem: Optional[str]
    SignatureAlgorithm: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PkixPublicKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PkixPublicKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            PublicKeyPem=json_data.get("PublicKeyPem"),
            SignatureAlgorithm=json_data.get("SignatureAlgorithm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PkixPublicKeyDefinition = PkixPublicKeyDefinition


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


