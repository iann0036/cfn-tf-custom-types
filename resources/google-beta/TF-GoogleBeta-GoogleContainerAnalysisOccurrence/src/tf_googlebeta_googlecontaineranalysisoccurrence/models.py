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
    CreateTime: Optional[str]
    Id: Optional[str]
    Kind: Optional[str]
    Name: Optional[str]
    NoteName: Optional[str]
    Project: Optional[str]
    Remediation: Optional[str]
    ResourceUri: Optional[str]
    UpdateTime: Optional[str]
    Attestation: Optional[Sequence["_AttestationDefinition"]]
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
            CreateTime=json_data.get("CreateTime"),
            Id=json_data.get("Id"),
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            NoteName=json_data.get("NoteName"),
            Project=json_data.get("Project"),
            Remediation=json_data.get("Remediation"),
            ResourceUri=json_data.get("ResourceUri"),
            UpdateTime=json_data.get("UpdateTime"),
            Attestation=deserialize_list(json_data.get("Attestation"), AttestationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AttestationDefinition(BaseModel):
    SerializedPayload: Optional[str]
    Signatures: Optional[Sequence["_SignaturesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AttestationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttestationDefinition"]:
        if not json_data:
            return None
        return cls(
            SerializedPayload=json_data.get("SerializedPayload"),
            Signatures=deserialize_list(json_data.get("Signatures"), SignaturesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttestationDefinition = AttestationDefinition


@dataclass
class SignaturesDefinition(BaseModel):
    PublicKeyId: Optional[str]
    Signature: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SignaturesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SignaturesDefinition"]:
        if not json_data:
            return None
        return cls(
            PublicKeyId=json_data.get("PublicKeyId"),
            Signature=json_data.get("Signature"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SignaturesDefinition = SignaturesDefinition


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


