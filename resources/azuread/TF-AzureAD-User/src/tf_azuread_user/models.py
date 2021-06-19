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
    AccountEnabled: Optional[bool]
    City: Optional[str]
    CompanyName: Optional[str]
    Country: Optional[str]
    Department: Optional[str]
    DisplayName: Optional[str]
    ForcePasswordChange: Optional[bool]
    GivenName: Optional[str]
    Id: Optional[str]
    ImmutableId: Optional[str]
    JobTitle: Optional[str]
    Mail: Optional[str]
    MailNickname: Optional[str]
    Mobile: Optional[str]
    MobilePhone: Optional[str]
    ObjectId: Optional[str]
    OfficeLocation: Optional[str]
    OnpremisesImmutableId: Optional[str]
    OnpremisesSamAccountName: Optional[str]
    OnpremisesUserPrincipalName: Optional[str]
    Password: Optional[str]
    PhysicalDeliveryOfficeName: Optional[str]
    PostalCode: Optional[str]
    State: Optional[str]
    StreetAddress: Optional[str]
    Surname: Optional[str]
    UsageLocation: Optional[str]
    UserPrincipalName: Optional[str]
    UserType: Optional[str]

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
            AccountEnabled=json_data.get("AccountEnabled"),
            City=json_data.get("City"),
            CompanyName=json_data.get("CompanyName"),
            Country=json_data.get("Country"),
            Department=json_data.get("Department"),
            DisplayName=json_data.get("DisplayName"),
            ForcePasswordChange=json_data.get("ForcePasswordChange"),
            GivenName=json_data.get("GivenName"),
            Id=json_data.get("Id"),
            ImmutableId=json_data.get("ImmutableId"),
            JobTitle=json_data.get("JobTitle"),
            Mail=json_data.get("Mail"),
            MailNickname=json_data.get("MailNickname"),
            Mobile=json_data.get("Mobile"),
            MobilePhone=json_data.get("MobilePhone"),
            ObjectId=json_data.get("ObjectId"),
            OfficeLocation=json_data.get("OfficeLocation"),
            OnpremisesImmutableId=json_data.get("OnpremisesImmutableId"),
            OnpremisesSamAccountName=json_data.get("OnpremisesSamAccountName"),
            OnpremisesUserPrincipalName=json_data.get("OnpremisesUserPrincipalName"),
            Password=json_data.get("Password"),
            PhysicalDeliveryOfficeName=json_data.get("PhysicalDeliveryOfficeName"),
            PostalCode=json_data.get("PostalCode"),
            State=json_data.get("State"),
            StreetAddress=json_data.get("StreetAddress"),
            Surname=json_data.get("Surname"),
            UsageLocation=json_data.get("UsageLocation"),
            UserPrincipalName=json_data.get("UserPrincipalName"),
            UserType=json_data.get("UserType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


