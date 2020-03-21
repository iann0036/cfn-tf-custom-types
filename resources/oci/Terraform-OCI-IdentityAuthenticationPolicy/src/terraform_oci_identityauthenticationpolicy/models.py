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
    CompartmentId: Optional[str]
    PasswordPolicy: Optional[Sequence["_PasswordPolicy"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CompartmentId=json_data.get("CompartmentId"),
            PasswordPolicy=json_data.get("PasswordPolicy"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PasswordPolicy:
    IsLowercaseCharactersRequired: Optional[bool]
    IsNumericCharactersRequired: Optional[bool]
    IsSpecialCharactersRequired: Optional[bool]
    IsUppercaseCharactersRequired: Optional[bool]
    IsUsernameContainmentAllowed: Optional[bool]
    MinimumPasswordLength: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PasswordPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PasswordPolicy"]:
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
_PasswordPolicy = PasswordPolicy


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


