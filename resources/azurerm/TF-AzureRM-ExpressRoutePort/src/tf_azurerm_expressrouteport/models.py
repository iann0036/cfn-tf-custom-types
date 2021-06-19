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
    BandwidthInGbps: Optional[float]
    Encapsulation: Optional[str]
    Ethertype: Optional[str]
    Guid: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Mtu: Optional[str]
    Name: Optional[str]
    PeeringLocation: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Identity: Optional[Sequence["_IdentityDefinition"]]
    Link1: Optional[Sequence["_Link1Definition"]]
    Link2: Optional[Sequence["_Link2Definition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            BandwidthInGbps=json_data.get("BandwidthInGbps"),
            Encapsulation=json_data.get("Encapsulation"),
            Ethertype=json_data.get("Ethertype"),
            Guid=json_data.get("Guid"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            PeeringLocation=json_data.get("PeeringLocation"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            Link1=deserialize_list(json_data.get("Link1"), Link1Definition),
            Link2=deserialize_list(json_data.get("Link2"), Link2Definition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class IdentityDefinition(BaseModel):
    IdentityIds: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityDefinition"]:
        if not json_data:
            return None
        return cls(
            IdentityIds=json_data.get("IdentityIds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityDefinition = IdentityDefinition


@dataclass
class Link1Definition(BaseModel):
    AdminEnabled: Optional[bool]
    MacsecCakKeyvaultSecretId: Optional[str]
    MacsecCipher: Optional[str]
    MacsecCknKeyvaultSecretId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Link1Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Link1Definition"]:
        if not json_data:
            return None
        return cls(
            AdminEnabled=json_data.get("AdminEnabled"),
            MacsecCakKeyvaultSecretId=json_data.get("MacsecCakKeyvaultSecretId"),
            MacsecCipher=json_data.get("MacsecCipher"),
            MacsecCknKeyvaultSecretId=json_data.get("MacsecCknKeyvaultSecretId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Link1Definition = Link1Definition


@dataclass
class Link2Definition(BaseModel):
    AdminEnabled: Optional[bool]
    MacsecCakKeyvaultSecretId: Optional[str]
    MacsecCipher: Optional[str]
    MacsecCknKeyvaultSecretId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Link2Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Link2Definition"]:
        if not json_data:
            return None
        return cls(
            AdminEnabled=json_data.get("AdminEnabled"),
            MacsecCakKeyvaultSecretId=json_data.get("MacsecCakKeyvaultSecretId"),
            MacsecCipher=json_data.get("MacsecCipher"),
            MacsecCknKeyvaultSecretId=json_data.get("MacsecCknKeyvaultSecretId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Link2Definition = Link2Definition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


