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
    CallRecovery: Optional[str]
    DefaultAuthProvider: Optional[str]
    DefaultIncludedGroupId: Optional[str]
    Description: Optional[str]
    EmailRecovery: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PasswordAutoUnlockMinutes: Optional[float]
    PasswordDictionaryLookup: Optional[bool]
    PasswordExcludeFirstName: Optional[bool]
    PasswordExcludeLastName: Optional[bool]
    PasswordExcludeUsername: Optional[bool]
    PasswordExpireWarnDays: Optional[float]
    PasswordHistoryCount: Optional[float]
    PasswordLockoutNotificationChannels: Optional[Sequence[str]]
    PasswordMaxAgeDays: Optional[float]
    PasswordMaxLockoutAttempts: Optional[float]
    PasswordMinAgeMinutes: Optional[float]
    PasswordMinLength: Optional[float]
    PasswordMinLowercase: Optional[float]
    PasswordMinNumber: Optional[float]
    PasswordMinSymbol: Optional[float]
    PasswordMinUppercase: Optional[float]
    PasswordShowLockoutFailures: Optional[bool]
    Priority: Optional[float]
    QuestionMinLength: Optional[float]
    QuestionRecovery: Optional[str]
    RecoveryEmailToken: Optional[float]
    SkipUnlock: Optional[bool]
    SmsRecovery: Optional[str]
    Status: Optional[str]

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
            CallRecovery=json_data.get("CallRecovery"),
            DefaultAuthProvider=json_data.get("DefaultAuthProvider"),
            DefaultIncludedGroupId=json_data.get("DefaultIncludedGroupId"),
            Description=json_data.get("Description"),
            EmailRecovery=json_data.get("EmailRecovery"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PasswordAutoUnlockMinutes=json_data.get("PasswordAutoUnlockMinutes"),
            PasswordDictionaryLookup=json_data.get("PasswordDictionaryLookup"),
            PasswordExcludeFirstName=json_data.get("PasswordExcludeFirstName"),
            PasswordExcludeLastName=json_data.get("PasswordExcludeLastName"),
            PasswordExcludeUsername=json_data.get("PasswordExcludeUsername"),
            PasswordExpireWarnDays=json_data.get("PasswordExpireWarnDays"),
            PasswordHistoryCount=json_data.get("PasswordHistoryCount"),
            PasswordLockoutNotificationChannels=json_data.get("PasswordLockoutNotificationChannels"),
            PasswordMaxAgeDays=json_data.get("PasswordMaxAgeDays"),
            PasswordMaxLockoutAttempts=json_data.get("PasswordMaxLockoutAttempts"),
            PasswordMinAgeMinutes=json_data.get("PasswordMinAgeMinutes"),
            PasswordMinLength=json_data.get("PasswordMinLength"),
            PasswordMinLowercase=json_data.get("PasswordMinLowercase"),
            PasswordMinNumber=json_data.get("PasswordMinNumber"),
            PasswordMinSymbol=json_data.get("PasswordMinSymbol"),
            PasswordMinUppercase=json_data.get("PasswordMinUppercase"),
            PasswordShowLockoutFailures=json_data.get("PasswordShowLockoutFailures"),
            Priority=json_data.get("Priority"),
            QuestionMinLength=json_data.get("QuestionMinLength"),
            QuestionRecovery=json_data.get("QuestionRecovery"),
            RecoveryEmailToken=json_data.get("RecoveryEmailToken"),
            SkipUnlock=json_data.get("SkipUnlock"),
            SmsRecovery=json_data.get("SmsRecovery"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


