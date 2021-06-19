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
    Name: Optional[str]
    Router: Optional[str]
    Servers: Optional[Sequence["_ServersDefinition"]]
    Type: Optional[str]
    Zone: Optional[str]
    IpNetwork: Optional[Sequence["_IpNetworkDefinition"]]

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
            Name=json_data.get("Name"),
            Router=json_data.get("Router"),
            Servers=deserialize_list(json_data.get("Servers"), ServersDefinition),
            Type=json_data.get("Type"),
            Zone=json_data.get("Zone"),
            IpNetwork=deserialize_list(json_data.get("IpNetwork"), IpNetworkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ServersDefinition(BaseModel):
    Id: Optional[str]
    Title: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServersDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Title=json_data.get("Title"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServersDefinition = ServersDefinition


@dataclass
class IpNetworkDefinition(BaseModel):
    Address: Optional[str]
    Dhcp: Optional[bool]
    DhcpDefaultRoute: Optional[bool]
    DhcpDns: Optional[Sequence[str]]
    Family: Optional[str]
    Gateway: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Dhcp=json_data.get("Dhcp"),
            DhcpDefaultRoute=json_data.get("DhcpDefaultRoute"),
            DhcpDns=json_data.get("DhcpDns"),
            Family=json_data.get("Family"),
            Gateway=json_data.get("Gateway"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpNetworkDefinition = IpNetworkDefinition


