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
    Cidr: Optional[str]
    DnsNameservers: Optional[Sequence[str]]
    EnableDhcp: Optional[bool]
    GatewayIp: Optional[str]
    Id: Optional[str]
    IpVersion: Optional[float]
    Ipv6AddressMode: Optional[str]
    Ipv6RaMode: Optional[str]
    Name: Optional[str]
    NetworkId: Optional[str]
    NoGateway: Optional[bool]
    Region: Optional[str]
    TenantId: Optional[str]
    ValueSpecs: Optional[Sequence["_ValueSpecs"]]
    AllocationPools: Optional[Sequence["_AllocationPools"]]
    HostRoutes: Optional[Sequence["_HostRoutes"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Cidr=json_data.get("Cidr"),
            DnsNameservers=json_data.get("DnsNameservers"),
            EnableDhcp=json_data.get("EnableDhcp"),
            GatewayIp=json_data.get("GatewayIp"),
            Id=json_data.get("Id"),
            IpVersion=json_data.get("IpVersion"),
            Ipv6AddressMode=json_data.get("Ipv6AddressMode"),
            Ipv6RaMode=json_data.get("Ipv6RaMode"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            NoGateway=json_data.get("NoGateway"),
            Region=json_data.get("Region"),
            TenantId=json_data.get("TenantId"),
            ValueSpecs=json_data.get("ValueSpecs"),
            AllocationPools=json_data.get("AllocationPools"),
            HostRoutes=json_data.get("HostRoutes"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ValueSpecs:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValueSpecs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueSpecs"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueSpecs = ValueSpecs


@dataclass
class AllocationPools:
    End: Optional[str]
    Start: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllocationPools"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllocationPools"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllocationPools = AllocationPools


@dataclass
class HostRoutes:
    DestinationCidr: Optional[str]
    NextHop: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostRoutes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostRoutes"]:
        if not json_data:
            return None
        return cls(
            DestinationCidr=json_data.get("DestinationCidr"),
            NextHop=json_data.get("NextHop"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostRoutes = HostRoutes


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


