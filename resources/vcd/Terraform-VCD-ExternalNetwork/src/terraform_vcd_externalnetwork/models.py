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
    Id: Optional[str]
    Name: Optional[str]
    RetainNetInfoAcrossDeployments: Optional[bool]
    IpScope: Optional[Sequence["_IpScope"]]
    VsphereNetwork: Optional[Sequence["_VsphereNetwork"]]
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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RetainNetInfoAcrossDeployments=json_data.get("RetainNetInfoAcrossDeployments"),
            IpScope=json_data.get("IpScope"),
            VsphereNetwork=json_data.get("VsphereNetwork"),
            StaticIpPool=json_data.get("StaticIpPool"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IpScope:
    Dns1: Optional[str]
    Dns2: Optional[str]
    DnsSuffix: Optional[str]
    Gateway: Optional[str]
    Netmask: Optional[str]
    StaticIpPool: Optional[Sequence["_StaticIpPool"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpScope"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpScope"]:
        if not json_data:
            return None
        return cls(
            Dns1=json_data.get("Dns1"),
            Dns2=json_data.get("Dns2"),
            DnsSuffix=json_data.get("DnsSuffix"),
            Gateway=json_data.get("Gateway"),
            Netmask=json_data.get("Netmask"),
            StaticIpPool=json_data.get("StaticIpPool"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpScope = IpScope


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


@dataclass
class VsphereNetwork:
    Name: Optional[str]
    Type: Optional[str]
    Vcenter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VsphereNetwork"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VsphereNetwork"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Vcenter=json_data.get("Vcenter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VsphereNetwork = VsphereNetwork


