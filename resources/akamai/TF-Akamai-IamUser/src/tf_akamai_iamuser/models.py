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
    Address: Optional[str]
    AuthGrantsJson: Optional[str]
    City: Optional[str]
    ContactType: Optional[str]
    Country: Optional[str]
    Email: Optional[str]
    EmailUpdatePending: Optional[bool]
    EnableTfa: Optional[bool]
    FirstName: Optional[str]
    Id: Optional[str]
    IsLocked: Optional[bool]
    JobTitle: Optional[str]
    LastLogin: Optional[str]
    LastName: Optional[str]
    MobilePhone: Optional[str]
    PasswordExpiredAfter: Optional[str]
    Phone: Optional[str]
    PreferredLanguage: Optional[str]
    SecondaryEmail: Optional[str]
    SessionTimeout: Optional[float]
    State: Optional[str]
    TfaConfigured: Optional[bool]
    TimeZone: Optional[str]
    UserName: Optional[str]
    ZipCode: Optional[str]

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
            Address=json_data.get("Address"),
            AuthGrantsJson=json_data.get("AuthGrantsJson"),
            City=json_data.get("City"),
            ContactType=json_data.get("ContactType"),
            Country=json_data.get("Country"),
            Email=json_data.get("Email"),
            EmailUpdatePending=json_data.get("EmailUpdatePending"),
            EnableTfa=json_data.get("EnableTfa"),
            FirstName=json_data.get("FirstName"),
            Id=json_data.get("Id"),
            IsLocked=json_data.get("IsLocked"),
            JobTitle=json_data.get("JobTitle"),
            LastLogin=json_data.get("LastLogin"),
            LastName=json_data.get("LastName"),
            MobilePhone=json_data.get("MobilePhone"),
            PasswordExpiredAfter=json_data.get("PasswordExpiredAfter"),
            Phone=json_data.get("Phone"),
            PreferredLanguage=json_data.get("PreferredLanguage"),
            SecondaryEmail=json_data.get("SecondaryEmail"),
            SessionTimeout=json_data.get("SessionTimeout"),
            State=json_data.get("State"),
            TfaConfigured=json_data.get("TfaConfigured"),
            TimeZone=json_data.get("TimeZone"),
            UserName=json_data.get("UserName"),
            ZipCode=json_data.get("ZipCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


