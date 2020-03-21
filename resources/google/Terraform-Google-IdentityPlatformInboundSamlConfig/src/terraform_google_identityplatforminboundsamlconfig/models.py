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
    DisplayName: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    IdpConfig: Optional[Sequence["_IdpConfig"]]
    SpConfig: Optional[Sequence["_SpConfig"]]
    Timeouts: Optional["_Timeouts"]
    IdpCertificates: Optional[Sequence["_IdpCertificates"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DisplayName=json_data.get("DisplayName"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            IdpConfig=json_data.get("IdpConfig"),
            SpConfig=json_data.get("SpConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            IdpCertificates=json_data.get("IdpCertificates"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IdpConfig:
    IdpEntityId: Optional[str]
    SignRequest: Optional[bool]
    SsoUrl: Optional[str]
    IdpCertificates: Optional[Sequence["_IdpCertificates"]]

    @classmethod
    def _deserialize(
        cls: Type["_IdpConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdpConfig"]:
        if not json_data:
            return None
        return cls(
            IdpEntityId=json_data.get("IdpEntityId"),
            SignRequest=json_data.get("SignRequest"),
            SsoUrl=json_data.get("SsoUrl"),
            IdpCertificates=json_data.get("IdpCertificates"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdpConfig = IdpConfig


@dataclass
class IdpCertificates:
    X509Certificate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdpCertificates"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdpCertificates"]:
        if not json_data:
            return None
        return cls(
            X509Certificate=json_data.get("X509Certificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdpCertificates = IdpCertificates


@dataclass
class SpConfig:
    CallbackUri: Optional[str]
    SpEntityId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SpConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpConfig"]:
        if not json_data:
            return None
        return cls(
            CallbackUri=json_data.get("CallbackUri"),
            SpEntityId=json_data.get("SpEntityId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpConfig = SpConfig


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


