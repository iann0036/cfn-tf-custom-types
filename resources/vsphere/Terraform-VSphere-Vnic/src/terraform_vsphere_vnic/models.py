# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    DistributedPortGroup: Optional[str]
    DistributedSwitchPort: Optional[str]
    Host: Optional[str]
    Id: Optional[str]
    Mac: Optional[str]
    Mtu: Optional[float]
    Netstack: Optional[str]
    Portgroup: Optional[str]
    Ipv4: Optional[Sequence["_Ipv4"]]
    Ipv6: Optional[Sequence["_Ipv6"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            Ipv4=json_data.get("Ipv4"),
            Ipv6=json_data.get("Ipv6"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Ipv4:
    Dhcp: Optional[bool]
    Gw: Optional[str]
    Ip: Optional[str]
    Netmask: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv4"]:
        if not json_data:
            return None
        return cls(
            Dhcp=json_data.get("Dhcp"),
            Gw=json_data.get("Gw"),
            Ip=json_data.get("Ip"),
            Netmask=json_data.get("Netmask"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv4 = Ipv4


@dataclass
class Ipv6:
    Addresses: Optional[Sequence[str]]
    Autoconfig: Optional[bool]
    Dhcp: Optional[bool]
    Gw: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6"]:
        if not json_data:
            return None
        return cls(
            Addresses=json_data.get("Addresses"),
            Autoconfig=json_data.get("Autoconfig"),
            Dhcp=json_data.get("Dhcp"),
            Gw=json_data.get("Gw"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6 = Ipv6


