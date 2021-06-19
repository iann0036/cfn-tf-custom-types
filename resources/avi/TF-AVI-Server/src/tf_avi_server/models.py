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
    AutoscalingGroupName: Optional[str]
    AvailabilityZone: Optional[str]
    Description: Optional[str]
    Enabled: Optional[bool]
    ExternalOrchestrationId: Optional[str]
    ExternalUuid: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    Ip: Optional[str]
    MacAddress: Optional[str]
    NwRef: Optional[str]
    PoolRef: Optional[str]
    Port: Optional[float]
    PrstHdrVal: Optional[str]
    Ratio: Optional[float]
    ResolveServerByDns: Optional[bool]
    RewriteHostHeader: Optional[bool]
    ServerNode: Optional[str]
    Static: Optional[bool]
    Type: Optional[str]
    VerifyNetwork: Optional[bool]
    VmRef: Optional[str]
    DiscoveredNetworks: Optional[Sequence["_DiscoveredNetworksDefinition"]]
    Location: Optional[Sequence["_LocationDefinition"]]

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
            AutoscalingGroupName=json_data.get("AutoscalingGroupName"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            ExternalOrchestrationId=json_data.get("ExternalOrchestrationId"),
            ExternalUuid=json_data.get("ExternalUuid"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            MacAddress=json_data.get("MacAddress"),
            NwRef=json_data.get("NwRef"),
            PoolRef=json_data.get("PoolRef"),
            Port=json_data.get("Port"),
            PrstHdrVal=json_data.get("PrstHdrVal"),
            Ratio=json_data.get("Ratio"),
            ResolveServerByDns=json_data.get("ResolveServerByDns"),
            RewriteHostHeader=json_data.get("RewriteHostHeader"),
            ServerNode=json_data.get("ServerNode"),
            Static=json_data.get("Static"),
            Type=json_data.get("Type"),
            VerifyNetwork=json_data.get("VerifyNetwork"),
            VmRef=json_data.get("VmRef"),
            DiscoveredNetworks=deserialize_list(json_data.get("DiscoveredNetworks"), DiscoveredNetworksDefinition),
            Location=deserialize_list(json_data.get("Location"), LocationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DiscoveredNetworksDefinition(BaseModel):
    NetworkRef: Optional[str]
    Subnet: Optional[Sequence["_SubnetDefinition"]]
    Subnet6: Optional[Sequence["_Subnet6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DiscoveredNetworksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiscoveredNetworksDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkRef=json_data.get("NetworkRef"),
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
            Subnet6=deserialize_list(json_data.get("Subnet6"), Subnet6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiscoveredNetworksDefinition = DiscoveredNetworksDefinition


@dataclass
class SubnetDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetDefinition = SubnetDefinition


@dataclass
class IpAddrDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddrDefinition = IpAddrDefinition


@dataclass
class Subnet6Definition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Subnet6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subnet6Definition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subnet6Definition = Subnet6Definition


@dataclass
class LocationDefinition(BaseModel):
    Latitude: Optional[float]
    Longitude: Optional[float]
    Name: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocationDefinition"]:
        if not json_data:
            return None
        return cls(
            Latitude=json_data.get("Latitude"),
            Longitude=json_data.get("Longitude"),
            Name=json_data.get("Name"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocationDefinition = LocationDefinition


