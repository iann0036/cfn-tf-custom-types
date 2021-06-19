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
    Id: Optional[str]
    EthernetList: Optional[Sequence["_EthernetListDefinition"]]

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
            Id=json_data.get("Id"),
            EthernetList=deserialize_list(json_data.get("EthernetList"), EthernetListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EthernetListDefinition(BaseModel):
    Action: Optional[str]
    Duplexity: Optional[str]
    FlowControl: Optional[float]
    Ifnum: Optional[float]
    L3VlanFwdDisable: Optional[float]
    LoadInterval: Optional[float]
    Mtu: Optional[float]
    Speed: Optional[str]
    TrapSource: Optional[float]
    Uuid: Optional[str]
    Ip: Optional[Sequence["_IpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EthernetListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EthernetListDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Duplexity=json_data.get("Duplexity"),
            FlowControl=json_data.get("FlowControl"),
            Ifnum=json_data.get("Ifnum"),
            L3VlanFwdDisable=json_data.get("L3VlanFwdDisable"),
            LoadInterval=json_data.get("LoadInterval"),
            Mtu=json_data.get("Mtu"),
            Speed=json_data.get("Speed"),
            TrapSource=json_data.get("TrapSource"),
            Uuid=json_data.get("Uuid"),
            Ip=deserialize_list(json_data.get("Ip"), IpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EthernetListDefinition = EthernetListDefinition


@dataclass
class IpDefinition(BaseModel):
    Dhcp: Optional[float]
    Uuid: Optional[str]
    AddressList: Optional[Sequence["_AddressListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpDefinition"]:
        if not json_data:
            return None
        return cls(
            Dhcp=json_data.get("Dhcp"),
            Uuid=json_data.get("Uuid"),
            AddressList=deserialize_list(json_data.get("AddressList"), AddressListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpDefinition = IpDefinition


@dataclass
class AddressListDefinition(BaseModel):
    Ipv4Address: Optional[str]
    Ipv4Netmask: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddressListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddressListDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv4Netmask=json_data.get("Ipv4Netmask"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddressListDefinition = AddressListDefinition


