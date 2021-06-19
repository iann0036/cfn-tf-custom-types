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
    DistributedPortGroup: Optional[str]
    DistributedSwitchPort: Optional[str]
    Host: Optional[str]
    Id: Optional[str]
    Mac: Optional[str]
    Mtu: Optional[float]
    Netstack: Optional[str]
    Portgroup: Optional[str]
    Ipv4: Optional[Sequence["_Ipv4Definition"]]
    Ipv6: Optional[Sequence["_Ipv6Definition"]]

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
            DistributedPortGroup=json_data.get("DistributedPortGroup"),
            DistributedSwitchPort=json_data.get("DistributedSwitchPort"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            Mac=json_data.get("Mac"),
            Mtu=json_data.get("Mtu"),
            Netstack=json_data.get("Netstack"),
            Portgroup=json_data.get("Portgroup"),
            Ipv4=deserialize_list(json_data.get("Ipv4"), Ipv4Definition),
            Ipv6=deserialize_list(json_data.get("Ipv6"), Ipv6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Ipv4Definition(BaseModel):
    Dhcp: Optional[bool]
    Gw: Optional[str]
    Ip: Optional[str]
    Netmask: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv4Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv4Definition"]:
        if not json_data:
            return None
        return cls(
            Dhcp=json_data.get("Dhcp"),
            Gw=json_data.get("Gw"),
            Ip=json_data.get("Ip"),
            Netmask=json_data.get("Netmask"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv4Definition = Ipv4Definition


@dataclass
class Ipv6Definition(BaseModel):
    Addresses: Optional[Sequence[str]]
    Autoconfig: Optional[bool]
    Dhcp: Optional[bool]
    Gw: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6Definition"]:
        if not json_data:
            return None
        return cls(
            Addresses=json_data.get("Addresses"),
            Autoconfig=json_data.get("Autoconfig"),
            Dhcp=json_data.get("Dhcp"),
            Gw=json_data.get("Gw"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6Definition = Ipv6Definition


