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
    CannotChangePassword: Optional[bool]
    City: Optional[str]
    Company: Optional[str]
    Container: Optional[str]
    Country: Optional[str]
    CustomAttributes: Optional[str]
    Department: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Division: Optional[str]
    EmailAddress: Optional[str]
    EmployeeId: Optional[str]
    EmployeeNumber: Optional[str]
    Enabled: Optional[bool]
    Fax: Optional[str]
    GivenName: Optional[str]
    HomeDirectory: Optional[str]
    HomeDrive: Optional[str]
    HomePage: Optional[str]
    HomePhone: Optional[str]
    Id: Optional[str]
    InitialPassword: Optional[str]
    Initials: Optional[str]
    MobilePhone: Optional[str]
    Office: Optional[str]
    OfficePhone: Optional[str]
    Organization: Optional[str]
    OtherName: Optional[str]
    PasswordNeverExpires: Optional[bool]
    PoBox: Optional[str]
    PostalCode: Optional[str]
    PrincipalName: Optional[str]
    SamAccountName: Optional[str]
    Sid: Optional[str]
    SmartCardLogonRequired: Optional[bool]
    State: Optional[str]
    StreetAddress: Optional[str]
    Surname: Optional[str]
    Title: Optional[str]
    TrustedForDelegation: Optional[bool]

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
            CannotChangePassword=json_data.get("CannotChangePassword"),
            City=json_data.get("City"),
            Company=json_data.get("Company"),
            Container=json_data.get("Container"),
            Country=json_data.get("Country"),
            CustomAttributes=json_data.get("CustomAttributes"),
            Department=json_data.get("Department"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Division=json_data.get("Division"),
            EmailAddress=json_data.get("EmailAddress"),
            EmployeeId=json_data.get("EmployeeId"),
            EmployeeNumber=json_data.get("EmployeeNumber"),
            Enabled=json_data.get("Enabled"),
            Fax=json_data.get("Fax"),
            GivenName=json_data.get("GivenName"),
            HomeDirectory=json_data.get("HomeDirectory"),
            HomeDrive=json_data.get("HomeDrive"),
            HomePage=json_data.get("HomePage"),
            HomePhone=json_data.get("HomePhone"),
            Id=json_data.get("Id"),
            InitialPassword=json_data.get("InitialPassword"),
            Initials=json_data.get("Initials"),
            MobilePhone=json_data.get("MobilePhone"),
            Office=json_data.get("Office"),
            OfficePhone=json_data.get("OfficePhone"),
            Organization=json_data.get("Organization"),
            OtherName=json_data.get("OtherName"),
            PasswordNeverExpires=json_data.get("PasswordNeverExpires"),
            PoBox=json_data.get("PoBox"),
            PostalCode=json_data.get("PostalCode"),
            PrincipalName=json_data.get("PrincipalName"),
            SamAccountName=json_data.get("SamAccountName"),
            Sid=json_data.get("Sid"),
            SmartCardLogonRequired=json_data.get("SmartCardLogonRequired"),
            State=json_data.get("State"),
            StreetAddress=json_data.get("StreetAddress"),
            Surname=json_data.get("Surname"),
            Title=json_data.get("Title"),
            TrustedForDelegation=json_data.get("TrustedForDelegation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


