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
    AdminRoles: Optional[Sequence[str]]
    City: Optional[str]
    CostCenter: Optional[str]
    CountryCode: Optional[str]
    CustomProfileAttributes: Optional[str]
    Department: Optional[str]
    DisplayName: Optional[str]
    Division: Optional[str]
    Email: Optional[str]
    EmployeeNumber: Optional[str]
    FirstName: Optional[str]
    GroupMemberships: Optional[Sequence[str]]
    HonorificPrefix: Optional[str]
    HonorificSuffix: Optional[str]
    Id: Optional[str]
    LastName: Optional[str]
    Locale: Optional[str]
    Login: Optional[str]
    Manager: Optional[str]
    ManagerId: Optional[str]
    MiddleName: Optional[str]
    MobilePhone: Optional[str]
    NickName: Optional[str]
    Organization: Optional[str]
    Password: Optional[str]
    PostalAddress: Optional[str]
    PreferredLanguage: Optional[str]
    PrimaryPhone: Optional[str]
    ProfileUrl: Optional[str]
    RawStatus: Optional[str]
    RecoveryAnswer: Optional[str]
    RecoveryQuestion: Optional[str]
    SecondEmail: Optional[str]
    State: Optional[str]
    Status: Optional[str]
    StreetAddress: Optional[str]
    Timezone: Optional[str]
    Title: Optional[str]
    UserType: Optional[str]
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
            AdminRoles=json_data.get("AdminRoles"),
            City=json_data.get("City"),
            CostCenter=json_data.get("CostCenter"),
            CountryCode=json_data.get("CountryCode"),
            CustomProfileAttributes=json_data.get("CustomProfileAttributes"),
            Department=json_data.get("Department"),
            DisplayName=json_data.get("DisplayName"),
            Division=json_data.get("Division"),
            Email=json_data.get("Email"),
            EmployeeNumber=json_data.get("EmployeeNumber"),
            FirstName=json_data.get("FirstName"),
            GroupMemberships=json_data.get("GroupMemberships"),
            HonorificPrefix=json_data.get("HonorificPrefix"),
            HonorificSuffix=json_data.get("HonorificSuffix"),
            Id=json_data.get("Id"),
            LastName=json_data.get("LastName"),
            Locale=json_data.get("Locale"),
            Login=json_data.get("Login"),
            Manager=json_data.get("Manager"),
            ManagerId=json_data.get("ManagerId"),
            MiddleName=json_data.get("MiddleName"),
            MobilePhone=json_data.get("MobilePhone"),
            NickName=json_data.get("NickName"),
            Organization=json_data.get("Organization"),
            Password=json_data.get("Password"),
            PostalAddress=json_data.get("PostalAddress"),
            PreferredLanguage=json_data.get("PreferredLanguage"),
            PrimaryPhone=json_data.get("PrimaryPhone"),
            ProfileUrl=json_data.get("ProfileUrl"),
            RawStatus=json_data.get("RawStatus"),
            RecoveryAnswer=json_data.get("RecoveryAnswer"),
            RecoveryQuestion=json_data.get("RecoveryQuestion"),
            SecondEmail=json_data.get("SecondEmail"),
            State=json_data.get("State"),
            Status=json_data.get("Status"),
            StreetAddress=json_data.get("StreetAddress"),
            Timezone=json_data.get("Timezone"),
            Title=json_data.get("Title"),
            UserType=json_data.get("UserType"),
            ZipCode=json_data.get("ZipCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


