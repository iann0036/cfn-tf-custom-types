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
    AccountLockoutDurationInMins: Optional[float]
    AccountLockoutThreshold: Optional[float]
    FailedLoginResetDurationInMins: Optional[float]
    Id: Optional[str]
    MaxLength: Optional[float]
    MaxPasswordAgeInDays: Optional[float]
    MinLength: Optional[float]
    MinUniquePasswords: Optional[float]
    MustContainDigits: Optional[bool]
    MustContainLowercase: Optional[bool]
    MustContainSpecialChars: Optional[bool]
    MustContainUppercase: Optional[bool]
    RememberMfa: Optional[bool]
    RequireMfa: Optional[bool]

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
            AccountLockoutDurationInMins=json_data.get("AccountLockoutDurationInMins"),
            AccountLockoutThreshold=json_data.get("AccountLockoutThreshold"),
            FailedLoginResetDurationInMins=json_data.get("FailedLoginResetDurationInMins"),
            Id=json_data.get("Id"),
            MaxLength=json_data.get("MaxLength"),
            MaxPasswordAgeInDays=json_data.get("MaxPasswordAgeInDays"),
            MinLength=json_data.get("MinLength"),
            MinUniquePasswords=json_data.get("MinUniquePasswords"),
            MustContainDigits=json_data.get("MustContainDigits"),
            MustContainLowercase=json_data.get("MustContainLowercase"),
            MustContainSpecialChars=json_data.get("MustContainSpecialChars"),
            MustContainUppercase=json_data.get("MustContainUppercase"),
            RememberMfa=json_data.get("RememberMfa"),
            RequireMfa=json_data.get("RequireMfa"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


