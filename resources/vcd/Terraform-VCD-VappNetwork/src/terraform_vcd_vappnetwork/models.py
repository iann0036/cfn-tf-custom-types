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
    Description: Optional[str]
    Dns1: Optional[str]
    Dns2: Optional[str]
    DnsSuffix: Optional[str]
    FirewallEnabled: Optional[bool]
    Gateway: Optional[str]
    GuestVlanAllowed: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    NatEnabled: Optional[bool]
    Netmask: Optional[str]
    Org: Optional[str]
    OrgNetworkName: Optional[str]
    RetainIpMacEnabled: Optional[bool]
    VappName: Optional[str]
    Vdc: Optional[str]
    DhcpPool: Optional[Sequence["_DhcpPool"]]
    StaticIpPool: Optional[Sequence["_StaticIpPool"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Dns1=json_data.get("Dns1"),
            Dns2=json_data.get("Dns2"),
            DnsSuffix=json_data.get("DnsSuffix"),
            FirewallEnabled=json_data.get("FirewallEnabled"),
            Gateway=json_data.get("Gateway"),
            GuestVlanAllowed=json_data.get("GuestVlanAllowed"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NatEnabled=json_data.get("NatEnabled"),
            Netmask=json_data.get("Netmask"),
            Org=json_data.get("Org"),
            OrgNetworkName=json_data.get("OrgNetworkName"),
            RetainIpMacEnabled=json_data.get("RetainIpMacEnabled"),
            VappName=json_data.get("VappName"),
            Vdc=json_data.get("Vdc"),
            DhcpPool=json_data.get("DhcpPool"),
            StaticIpPool=json_data.get("StaticIpPool"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DhcpPool:
    DefaultLeaseTime: Optional[float]
    Enabled: Optional[bool]
    EndAddress: Optional[str]
    MaxLeaseTime: Optional[float]
    StartAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DhcpPool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DhcpPool"]:
        if not json_data:
            return None
        return cls(
            DefaultLeaseTime=json_data.get("DefaultLeaseTime"),
            Enabled=json_data.get("Enabled"),
            EndAddress=json_data.get("EndAddress"),
            MaxLeaseTime=json_data.get("MaxLeaseTime"),
            StartAddress=json_data.get("StartAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DhcpPool = DhcpPool


@dataclass
class StaticIpPool:
    EndAddress: Optional[str]
    StartAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StaticIpPool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticIpPool"]:
        if not json_data:
            return None
        return cls(
            EndAddress=json_data.get("EndAddress"),
            StartAddress=json_data.get("StartAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticIpPool = StaticIpPool


