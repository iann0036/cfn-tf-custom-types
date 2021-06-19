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
    Attestation: Optional[Sequence["_AttestationDefinition"]]
    ExpireTime: Optional[str]
    Id: Optional[str]
    ImportJobId: Optional[str]
    ImportMethod: Optional[str]
    KeyRing: Optional[str]
    Name: Optional[str]
    ProtectionLevel: Optional[str]
    PublicKey: Optional[Sequence["_PublicKeyDefinition"]]
    State: Optional[str]
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
            Attestation=deserialize_list(json_data.get("Attestation"), AttestationDefinition),
            ExpireTime=json_data.get("ExpireTime"),
            Id=json_data.get("Id"),
            ImportJobId=json_data.get("ImportJobId"),
            ImportMethod=json_data.get("ImportMethod"),
            KeyRing=json_data.get("KeyRing"),
            Name=json_data.get("Name"),
            ProtectionLevel=json_data.get("ProtectionLevel"),
            PublicKey=deserialize_list(json_data.get("PublicKey"), PublicKeyDefinition),
            State=json_data.get("State"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AttestationDefinition(BaseModel):
    Content: Optional[str]
    Format: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttestationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttestationDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Format=json_data.get("Format"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttestationDefinition = AttestationDefinition


@dataclass
class PublicKeyDefinition(BaseModel):
    Pem: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Pem=json_data.get("Pem"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicKeyDefinition = PublicKeyDefinition


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


