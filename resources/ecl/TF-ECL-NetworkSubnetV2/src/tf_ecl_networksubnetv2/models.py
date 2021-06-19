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
    Cidr: Optional[str]
    Description: Optional[str]
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
    NtpServers: Optional[Sequence[str]]
    Region: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TenantId: Optional[str]
    AllocationPools: Optional[Sequence["_AllocationPoolsDefinition"]]
    HostRoutes: Optional[Sequence["_HostRoutesDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Cidr=json_data.get("Cidr"),
            Description=json_data.get("Description"),
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
            NtpServers=json_data.get("NtpServers"),
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TenantId=json_data.get("TenantId"),
            AllocationPools=deserialize_list(json_data.get("AllocationPools"), AllocationPoolsDefinition),
            HostRoutes=deserialize_list(json_data.get("HostRoutes"), HostRoutesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class AllocationPoolsDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllocationPoolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllocationPoolsDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllocationPoolsDefinition = AllocationPoolsDefinition


@dataclass
class HostRoutesDefinition(BaseModel):
    DestinationCidr: Optional[str]
    NextHop: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostRoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostRoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationCidr=json_data.get("DestinationCidr"),
            NextHop=json_data.get("NextHop"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostRoutesDefinition = HostRoutesDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


