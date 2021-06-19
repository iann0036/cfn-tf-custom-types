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
    Alias: Optional[str]
    CertificateId: Optional[str]
    DomainNum: Optional[float]
    Id: Optional[str]
    OrderId: Optional[str]
    ProductId: Optional[float]
    ProjectId: Optional[float]
    Status: Optional[float]
    TimeSpan: Optional[float]
    Information: Optional[Sequence["_InformationDefinition"]]

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
            Alias=json_data.get("Alias"),
            CertificateId=json_data.get("CertificateId"),
            DomainNum=json_data.get("DomainNum"),
            Id=json_data.get("Id"),
            OrderId=json_data.get("OrderId"),
            ProductId=json_data.get("ProductId"),
            ProjectId=json_data.get("ProjectId"),
            Status=json_data.get("Status"),
            TimeSpan=json_data.get("TimeSpan"),
            Information=deserialize_list(json_data.get("Information"), InformationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InformationDefinition(BaseModel):
    AdminEmail: Optional[str]
    AdminFirstName: Optional[str]
    AdminLastName: Optional[str]
    AdminPhoneNum: Optional[str]
    AdminPosition: Optional[str]
    CertificateDomain: Optional[str]
    ContactEmail: Optional[str]
    ContactFirstName: Optional[str]
    ContactLastName: Optional[str]
    ContactNumber: Optional[str]
    ContactPosition: Optional[str]
    CsrContent: Optional[str]
    CsrType: Optional[str]
    DomainList: Optional[Sequence[str]]
    KeyPassword: Optional[str]
    OrganizationAddress: Optional[str]
    OrganizationCity: Optional[str]
    OrganizationCountry: Optional[str]
    OrganizationDivision: Optional[str]
    OrganizationName: Optional[str]
    OrganizationRegion: Optional[str]
    PhoneAreaCode: Optional[str]
    PhoneNumber: Optional[str]
    PostalCode: Optional[str]
    VerifyType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InformationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InformationDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminEmail=json_data.get("AdminEmail"),
            AdminFirstName=json_data.get("AdminFirstName"),
            AdminLastName=json_data.get("AdminLastName"),
            AdminPhoneNum=json_data.get("AdminPhoneNum"),
            AdminPosition=json_data.get("AdminPosition"),
            CertificateDomain=json_data.get("CertificateDomain"),
            ContactEmail=json_data.get("ContactEmail"),
            ContactFirstName=json_data.get("ContactFirstName"),
            ContactLastName=json_data.get("ContactLastName"),
            ContactNumber=json_data.get("ContactNumber"),
            ContactPosition=json_data.get("ContactPosition"),
            CsrContent=json_data.get("CsrContent"),
            CsrType=json_data.get("CsrType"),
            DomainList=json_data.get("DomainList"),
            KeyPassword=json_data.get("KeyPassword"),
            OrganizationAddress=json_data.get("OrganizationAddress"),
            OrganizationCity=json_data.get("OrganizationCity"),
            OrganizationCountry=json_data.get("OrganizationCountry"),
            OrganizationDivision=json_data.get("OrganizationDivision"),
            OrganizationName=json_data.get("OrganizationName"),
            OrganizationRegion=json_data.get("OrganizationRegion"),
            PhoneAreaCode=json_data.get("PhoneAreaCode"),
            PhoneNumber=json_data.get("PhoneNumber"),
            PostalCode=json_data.get("PostalCode"),
            VerifyType=json_data.get("VerifyType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InformationDefinition = InformationDefinition


