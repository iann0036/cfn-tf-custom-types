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
    DisplayName: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    Tenant: Optional[str]
    IdpConfig: Optional[Sequence["_IdpConfigDefinition"]]
    SpConfig: Optional[Sequence["_SpConfigDefinition"]]
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
            DisplayName=json_data.get("DisplayName"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Tenant=json_data.get("Tenant"),
            IdpConfig=deserialize_list(json_data.get("IdpConfig"), IdpConfigDefinition),
            SpConfig=deserialize_list(json_data.get("SpConfig"), SpConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IdpConfigDefinition(BaseModel):
    IdpEntityId: Optional[str]
    SignRequest: Optional[bool]
    SsoUrl: Optional[str]
    IdpCertificates: Optional[Sequence["_IdpCertificatesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IdpConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdpConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            IdpEntityId=json_data.get("IdpEntityId"),
            SignRequest=json_data.get("SignRequest"),
            SsoUrl=json_data.get("SsoUrl"),
            IdpCertificates=deserialize_list(json_data.get("IdpCertificates"), IdpCertificatesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdpConfigDefinition = IdpConfigDefinition


@dataclass
class IdpCertificatesDefinition(BaseModel):
    X509Certificate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdpCertificatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdpCertificatesDefinition"]:
        if not json_data:
            return None
        return cls(
            X509Certificate=json_data.get("X509Certificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdpCertificatesDefinition = IdpCertificatesDefinition


@dataclass
class SpConfigDefinition(BaseModel):
    CallbackUri: Optional[str]
    SpEntityId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SpConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CallbackUri=json_data.get("CallbackUri"),
            SpEntityId=json_data.get("SpEntityId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpConfigDefinition = SpConfigDefinition


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


