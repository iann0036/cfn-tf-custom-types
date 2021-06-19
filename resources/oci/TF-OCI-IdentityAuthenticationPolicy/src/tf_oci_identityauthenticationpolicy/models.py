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
    CompartmentId: Optional[str]
    Id: Optional[str]
    NetworkPolicy: Optional[Sequence["_NetworkPolicyDefinition"]]
    PasswordPolicy: Optional[Sequence["_PasswordPolicyDefinition"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            Id=json_data.get("Id"),
            NetworkPolicy=deserialize_list(json_data.get("NetworkPolicy"), NetworkPolicyDefinition),
            PasswordPolicy=deserialize_list(json_data.get("PasswordPolicy"), PasswordPolicyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NetworkPolicyDefinition(BaseModel):
    NetworkSourceIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkSourceIds=json_data.get("NetworkSourceIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkPolicyDefinition = NetworkPolicyDefinition


@dataclass
class PasswordPolicyDefinition(BaseModel):
    IsLowercaseCharactersRequired: Optional[bool]
    IsNumericCharactersRequired: Optional[bool]
    IsSpecialCharactersRequired: Optional[bool]
    IsUppercaseCharactersRequired: Optional[bool]
    IsUsernameContainmentAllowed: Optional[bool]
    MinimumPasswordLength: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PasswordPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PasswordPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            IsLowercaseCharactersRequired=json_data.get("IsLowercaseCharactersRequired"),
            IsNumericCharactersRequired=json_data.get("IsNumericCharactersRequired"),
            IsSpecialCharactersRequired=json_data.get("IsSpecialCharactersRequired"),
            IsUppercaseCharactersRequired=json_data.get("IsUppercaseCharactersRequired"),
            IsUsernameContainmentAllowed=json_data.get("IsUsernameContainmentAllowed"),
            MinimumPasswordLength=json_data.get("MinimumPasswordLength"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PasswordPolicyDefinition = PasswordPolicyDefinition


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


