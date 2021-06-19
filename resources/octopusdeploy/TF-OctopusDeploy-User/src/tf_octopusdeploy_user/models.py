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
    CanPasswordBeEdited: Optional[bool]
    DisplayName: Optional[str]
    EmailAddress: Optional[str]
    Id: Optional[str]
    IsActive: Optional[bool]
    IsRequestor: Optional[bool]
    IsService: Optional[bool]
    Password: Optional[str]
    Username: Optional[str]
    Identity: Optional[Sequence["_IdentityDefinition"]]

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
            CanPasswordBeEdited=json_data.get("CanPasswordBeEdited"),
            DisplayName=json_data.get("DisplayName"),
            EmailAddress=json_data.get("EmailAddress"),
            Id=json_data.get("Id"),
            IsActive=json_data.get("IsActive"),
            IsRequestor=json_data.get("IsRequestor"),
            IsService=json_data.get("IsService"),
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IdentityDefinition(BaseModel):
    Provider: Optional[str]
    Claim: Optional[Sequence["_ClaimDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityDefinition"]:
        if not json_data:
            return None
        return cls(
            Provider=json_data.get("Provider"),
            Claim=deserialize_list(json_data.get("Claim"), ClaimDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityDefinition = IdentityDefinition


@dataclass
class ClaimDefinition(BaseModel):
    IsIdentifyingClaim: Optional[bool]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClaimDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClaimDefinition"]:
        if not json_data:
            return None
        return cls(
            IsIdentifyingClaim=json_data.get("IsIdentifyingClaim"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClaimDefinition = ClaimDefinition


