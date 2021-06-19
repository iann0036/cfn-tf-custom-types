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
    AdminState: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    IpPoolId: Optional[str]
    MacPoolId: Optional[str]
    Revision: Optional[float]
    TransportZoneId: Optional[str]
    Vlan: Optional[float]
    AddressBinding: Optional[Sequence["_AddressBindingDefinition"]]
    SwitchingProfileId: Optional[Sequence["_SwitchingProfileIdDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

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
            AdminState=json_data.get("AdminState"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            IpPoolId=json_data.get("IpPoolId"),
            MacPoolId=json_data.get("MacPoolId"),
            Revision=json_data.get("Revision"),
            TransportZoneId=json_data.get("TransportZoneId"),
            Vlan=json_data.get("Vlan"),
            AddressBinding=deserialize_list(json_data.get("AddressBinding"), AddressBindingDefinition),
            SwitchingProfileId=deserialize_list(json_data.get("SwitchingProfileId"), SwitchingProfileIdDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AddressBindingDefinition(BaseModel):
    IpAddress: Optional[str]
    MacAddress: Optional[str]
    Vlan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AddressBindingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddressBindingDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            MacAddress=json_data.get("MacAddress"),
            Vlan=json_data.get("Vlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddressBindingDefinition = AddressBindingDefinition


@dataclass
class SwitchingProfileIdDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SwitchingProfileIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SwitchingProfileIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SwitchingProfileIdDefinition = SwitchingProfileIdDefinition


@dataclass
class TagDefinition(BaseModel):
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


