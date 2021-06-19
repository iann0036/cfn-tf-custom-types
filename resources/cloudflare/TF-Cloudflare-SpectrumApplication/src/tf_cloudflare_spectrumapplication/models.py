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
    ArgoSmartRouting: Optional[bool]
    EdgeIpConnectivity: Optional[str]
    EdgeIps: Optional[Sequence[str]]
    Id: Optional[str]
    IpFirewall: Optional[bool]
    OriginDirect: Optional[Sequence[str]]
    OriginPort: Optional[float]
    Protocol: Optional[str]
    ProxyProtocol: Optional[str]
    Tls: Optional[str]
    TrafficType: Optional[str]
    ZoneId: Optional[str]
    Dns: Optional[Sequence["_DnsDefinition"]]
    OriginDns: Optional[Sequence["_OriginDnsDefinition"]]
    OriginPortRange: Optional[Sequence["_OriginPortRangeDefinition"]]

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
            ArgoSmartRouting=json_data.get("ArgoSmartRouting"),
            EdgeIpConnectivity=json_data.get("EdgeIpConnectivity"),
            EdgeIps=json_data.get("EdgeIps"),
            Id=json_data.get("Id"),
            IpFirewall=json_data.get("IpFirewall"),
            OriginDirect=json_data.get("OriginDirect"),
            OriginPort=json_data.get("OriginPort"),
            Protocol=json_data.get("Protocol"),
            ProxyProtocol=json_data.get("ProxyProtocol"),
            Tls=json_data.get("Tls"),
            TrafficType=json_data.get("TrafficType"),
            ZoneId=json_data.get("ZoneId"),
            Dns=deserialize_list(json_data.get("Dns"), DnsDefinition),
            OriginDns=deserialize_list(json_data.get("OriginDns"), OriginDnsDefinition),
            OriginPortRange=deserialize_list(json_data.get("OriginPortRange"), OriginPortRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DnsDefinition(BaseModel):
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsDefinition = DnsDefinition


@dataclass
class OriginDnsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OriginDnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginDnsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginDnsDefinition = OriginDnsDefinition


@dataclass
class OriginPortRangeDefinition(BaseModel):
    End: Optional[float]
    Start: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OriginPortRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginPortRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginPortRangeDefinition = OriginPortRangeDefinition


