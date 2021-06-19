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
    AutomaticVlanId: Optional[bool]
    Bridge: Optional[str]
    Clusters: Optional[Sequence[float]]
    Description: Optional[str]
    Dns: Optional[str]
    Gateway: Optional[str]
    Gid: Optional[float]
    Gname: Optional[str]
    Group: Optional[str]
    GuestMtu: Optional[float]
    HoldIps: Optional[Sequence[str]]
    HoldSize: Optional[float]
    Id: Optional[str]
    IpHold: Optional[str]
    Mtu: Optional[float]
    Name: Optional[str]
    NetworkMask: Optional[str]
    Permissions: Optional[str]
    PhysicalDevice: Optional[str]
    ReservationSize: Optional[float]
    ReservationVnet: Optional[float]
    SecurityGroups: Optional[Sequence[float]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Type: Optional[str]
    Uid: Optional[float]
    Uname: Optional[str]
    VlanId: Optional[str]
    Ar: Optional[Sequence["_ArDefinition"]]

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
            AutomaticVlanId=json_data.get("AutomaticVlanId"),
            Bridge=json_data.get("Bridge"),
            Clusters=json_data.get("Clusters"),
            Description=json_data.get("Description"),
            Dns=json_data.get("Dns"),
            Gateway=json_data.get("Gateway"),
            Gid=json_data.get("Gid"),
            Gname=json_data.get("Gname"),
            Group=json_data.get("Group"),
            GuestMtu=json_data.get("GuestMtu"),
            HoldIps=json_data.get("HoldIps"),
            HoldSize=json_data.get("HoldSize"),
            Id=json_data.get("Id"),
            IpHold=json_data.get("IpHold"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            NetworkMask=json_data.get("NetworkMask"),
            Permissions=json_data.get("Permissions"),
            PhysicalDevice=json_data.get("PhysicalDevice"),
            ReservationSize=json_data.get("ReservationSize"),
            ReservationVnet=json_data.get("ReservationVnet"),
            SecurityGroups=json_data.get("SecurityGroups"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Type=json_data.get("Type"),
            Uid=json_data.get("Uid"),
            Uname=json_data.get("Uname"),
            VlanId=json_data.get("VlanId"),
            Ar=deserialize_list(json_data.get("Ar"), ArDefinition),
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
class ArDefinition(BaseModel):
    ArType: Optional[str]
    GlobalPrefix: Optional[str]
    Ip4: Optional[str]
    Ip6: Optional[str]
    Mac: Optional[str]
    PrefixLength: Optional[str]
    Size: Optional[float]
    UlaPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ArDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArDefinition"]:
        if not json_data:
            return None
        return cls(
            ArType=json_data.get("ArType"),
            GlobalPrefix=json_data.get("GlobalPrefix"),
            Ip4=json_data.get("Ip4"),
            Ip6=json_data.get("Ip6"),
            Mac=json_data.get("Mac"),
            PrefixLength=json_data.get("PrefixLength"),
            Size=json_data.get("Size"),
            UlaPrefix=json_data.get("UlaPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArDefinition = ArDefinition


