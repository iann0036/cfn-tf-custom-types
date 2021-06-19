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
    FullName: Optional[str]
    Id: Optional[str]
    Locale: Optional[str]
    Role: Optional[str]
    SkypeUsername: Optional[str]
    Tags: Optional[Sequence[str]]
    Timezone: Optional[str]
    UserDetails: Optional[Sequence["_UserDetailsDefinition"]]
    Username: Optional[str]
    UserAddress: Optional[Sequence["_UserAddressDefinition"]]

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
            FullName=json_data.get("FullName"),
            Id=json_data.get("Id"),
            Locale=json_data.get("Locale"),
            Role=json_data.get("Role"),
            SkypeUsername=json_data.get("SkypeUsername"),
            Tags=json_data.get("Tags"),
            Timezone=json_data.get("Timezone"),
            UserDetails=deserialize_list(json_data.get("UserDetails"), UserDetailsDefinition),
            Username=json_data.get("Username"),
            UserAddress=deserialize_list(json_data.get("UserAddress"), UserAddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class UserDetailsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserDetailsDefinition = UserDetailsDefinition


@dataclass
class UserAddressDefinition(BaseModel):
    City: Optional[str]
    Country: Optional[str]
    Line: Optional[str]
    State: Optional[str]
    Zipcode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            City=json_data.get("City"),
            Country=json_data.get("Country"),
            Line=json_data.get("Line"),
            State=json_data.get("State"),
            Zipcode=json_data.get("Zipcode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserAddressDefinition = UserAddressDefinition


