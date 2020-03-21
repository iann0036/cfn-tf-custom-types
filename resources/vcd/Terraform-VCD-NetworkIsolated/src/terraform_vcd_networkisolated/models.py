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
    Gateway: Optional[str]
    Href: Optional[str]
    Name: Optional[str]
    Netmask: Optional[str]
    Org: Optional[str]
    Shared: Optional[bool]
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
            Gateway=json_data.get("Gateway"),
            Href=json_data.get("Href"),
            Name=json_data.get("Name"),
            Netmask=json_data.get("Netmask"),
            Org=json_data.get("Org"),
            Shared=json_data.get("Shared"),
            Vdc=json_data.get("Vdc"),
            DhcpPool=json_data.get("DhcpPool"),
            StaticIpPool=json_data.get("StaticIpPool"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DhcpPool:
    DefaultLeaseTime: Optional[float]
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


