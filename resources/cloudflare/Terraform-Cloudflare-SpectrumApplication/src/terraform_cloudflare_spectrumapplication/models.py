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
    IpFirewall: Optional[bool]
    OriginDirect: Optional[Sequence[str]]
    OriginPort: Optional[float]
    Protocol: Optional[str]
    ProxyProtocol: Optional[str]
    Tls: Optional[str]
    TrafficType: Optional[str]
    ZoneId: Optional[str]
    Dns: Optional[Sequence["_Dns"]]
    OriginDns: Optional[Sequence["_OriginDns"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            IpFirewall=json_data.get("IpFirewall"),
            OriginDirect=json_data.get("OriginDirect"),
            OriginPort=json_data.get("OriginPort"),
            Protocol=json_data.get("Protocol"),
            ProxyProtocol=json_data.get("ProxyProtocol"),
            Tls=json_data.get("Tls"),
            TrafficType=json_data.get("TrafficType"),
            ZoneId=json_data.get("ZoneId"),
            Dns=json_data.get("Dns"),
            OriginDns=json_data.get("OriginDns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Dns:
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dns"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dns"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dns = Dns


@dataclass
class OriginDns:
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OriginDns"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginDns"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginDns = OriginDns


