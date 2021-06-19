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
    Comment: Optional[str]
    Company: Optional[str]
    CustomAttributes: Optional[Sequence["_CustomAttributesDefinition"]]
    Department: Optional[str]
    DirectoryId: Optional[float]
    DistinguishedName: Optional[str]
    Email: Optional[str]
    ExternalId: Optional[float]
    Firstname: Optional[str]
    GroupId: Optional[float]
    Id: Optional[str]
    Lastname: Optional[str]
    ManagerAdId: Optional[float]
    ManagerUserId: Optional[float]
    MemberOf: Optional[str]
    Phone: Optional[str]
    Samaccountname: Optional[str]
    State: Optional[float]
    Status: Optional[float]
    Title: Optional[str]
    TrustedIdpId: Optional[float]
    Username: Optional[str]
    Userprincipalname: Optional[str]

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
            Comment=json_data.get("Comment"),
            Company=json_data.get("Company"),
            CustomAttributes=deserialize_list(json_data.get("CustomAttributes"), CustomAttributesDefinition),
            Department=json_data.get("Department"),
            DirectoryId=json_data.get("DirectoryId"),
            DistinguishedName=json_data.get("DistinguishedName"),
            Email=json_data.get("Email"),
            ExternalId=json_data.get("ExternalId"),
            Firstname=json_data.get("Firstname"),
            GroupId=json_data.get("GroupId"),
            Id=json_data.get("Id"),
            Lastname=json_data.get("Lastname"),
            ManagerAdId=json_data.get("ManagerAdId"),
            ManagerUserId=json_data.get("ManagerUserId"),
            MemberOf=json_data.get("MemberOf"),
            Phone=json_data.get("Phone"),
            Samaccountname=json_data.get("Samaccountname"),
            State=json_data.get("State"),
            Status=json_data.get("Status"),
            Title=json_data.get("Title"),
            TrustedIdpId=json_data.get("TrustedIdpId"),
            Username=json_data.get("Username"),
            Userprincipalname=json_data.get("Userprincipalname"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomAttributesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomAttributesDefinition = CustomAttributesDefinition


