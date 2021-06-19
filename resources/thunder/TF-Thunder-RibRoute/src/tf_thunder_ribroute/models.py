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
    IpDestAddr: Optional[str]
    IpMask: Optional[str]
    Uuid: Optional[str]
    IpNexthopIpv4: Optional[Sequence["_IpNexthopIpv4Definition"]]
    IpNexthopLif: Optional[Sequence["_IpNexthopLifDefinition"]]
    IpNexthopPartition: Optional[Sequence["_IpNexthopPartitionDefinition"]]
    IpNexthopTunnel: Optional[Sequence["_IpNexthopTunnelDefinition"]]

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
            IpDestAddr=json_data.get("IpDestAddr"),
            IpMask=json_data.get("IpMask"),
            Uuid=json_data.get("Uuid"),
            IpNexthopIpv4=deserialize_list(json_data.get("IpNexthopIpv4"), IpNexthopIpv4Definition),
            IpNexthopLif=deserialize_list(json_data.get("IpNexthopLif"), IpNexthopLifDefinition),
            IpNexthopPartition=deserialize_list(json_data.get("IpNexthopPartition"), IpNexthopPartitionDefinition),
            IpNexthopTunnel=deserialize_list(json_data.get("IpNexthopTunnel"), IpNexthopTunnelDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IpNexthopIpv4Definition(BaseModel):
    DescriptionNexthopIp: Optional[str]
    DistanceNexthopIp: Optional[float]
    IpNextHop: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpNexthopIpv4Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpNexthopIpv4Definition"]:
        if not json_data:
            return None
        return cls(
            DescriptionNexthopIp=json_data.get("DescriptionNexthopIp"),
            DistanceNexthopIp=json_data.get("DistanceNexthopIp"),
            IpNextHop=json_data.get("IpNextHop"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpNexthopIpv4Definition = IpNexthopIpv4Definition


@dataclass
class IpNexthopLifDefinition(BaseModel):
    DescriptionNexthopLif: Optional[str]
    Lif: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IpNexthopLifDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpNexthopLifDefinition"]:
        if not json_data:
            return None
        return cls(
            DescriptionNexthopLif=json_data.get("DescriptionNexthopLif"),
            Lif=json_data.get("Lif"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpNexthopLifDefinition = IpNexthopLifDefinition


@dataclass
class IpNexthopPartitionDefinition(BaseModel):
    DescriptionNexthopPartition: Optional[str]
    DescriptionPartitionVrid: Optional[str]
    PartitionName: Optional[str]
    VridNumInPartition: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IpNexthopPartitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpNexthopPartitionDefinition"]:
        if not json_data:
            return None
        return cls(
            DescriptionNexthopPartition=json_data.get("DescriptionNexthopPartition"),
            DescriptionPartitionVrid=json_data.get("DescriptionPartitionVrid"),
            PartitionName=json_data.get("PartitionName"),
            VridNumInPartition=json_data.get("VridNumInPartition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpNexthopPartitionDefinition = IpNexthopPartitionDefinition


@dataclass
class IpNexthopTunnelDefinition(BaseModel):
    DescriptionNexthopTunnel: Optional[str]
    DistanceNexthopTunnel: Optional[float]
    IpNextHopTunnel: Optional[str]
    Tunnel: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IpNexthopTunnelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpNexthopTunnelDefinition"]:
        if not json_data:
            return None
        return cls(
            DescriptionNexthopTunnel=json_data.get("DescriptionNexthopTunnel"),
            DistanceNexthopTunnel=json_data.get("DistanceNexthopTunnel"),
            IpNextHopTunnel=json_data.get("IpNextHopTunnel"),
            Tunnel=json_data.get("Tunnel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpNexthopTunnelDefinition = IpNexthopTunnelDefinition


