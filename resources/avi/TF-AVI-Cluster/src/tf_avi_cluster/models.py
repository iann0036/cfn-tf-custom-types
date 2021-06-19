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
    RejoinNodesAutomatically: Optional[bool]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    ClusterState: Optional[Sequence["_ClusterStateDefinition"]]
    Nodes: Optional[Sequence["_NodesDefinition"]]
    VirtualIp: Optional[Sequence["_VirtualIpDefinition"]]

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
            RejoinNodesAutomatically=json_data.get("RejoinNodesAutomatically"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            ClusterState=deserialize_list(json_data.get("ClusterState"), ClusterStateDefinition),
            Nodes=deserialize_list(json_data.get("Nodes"), NodesDefinition),
            VirtualIp=deserialize_list(json_data.get("VirtualIp"), VirtualIpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ClusterStateDefinition(BaseModel):
    Progress: Optional[float]
    State: Optional[str]
    UpSince: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterStateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterStateDefinition"]:
        if not json_data:
            return None
        return cls(
            Progress=json_data.get("Progress"),
            State=json_data.get("State"),
            UpSince=json_data.get("UpSince"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterStateDefinition = ClusterStateDefinition


@dataclass
class NodesDefinition(BaseModel):
    Categories: Optional[Sequence[str]]
    Name: Optional[str]
    Password: Optional[str]
    VmHostname: Optional[str]
    VmMor: Optional[str]
    VmName: Optional[str]
    VmUuid: Optional[str]
    Ip: Optional[Sequence["_IpDefinition"]]
    PublicIpOrName: Optional[Sequence["_PublicIpOrNameDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodesDefinition"]:
        if not json_data:
            return None
        return cls(
            Categories=json_data.get("Categories"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            VmHostname=json_data.get("VmHostname"),
            VmMor=json_data.get("VmMor"),
            VmName=json_data.get("VmName"),
            VmUuid=json_data.get("VmUuid"),
            Ip=deserialize_list(json_data.get("Ip"), IpDefinition),
            PublicIpOrName=deserialize_list(json_data.get("PublicIpOrName"), PublicIpOrNameDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodesDefinition = NodesDefinition


@dataclass
class IpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpDefinition = IpDefinition


@dataclass
class PublicIpOrNameDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicIpOrNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicIpOrNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicIpOrNameDefinition = PublicIpOrNameDefinition


@dataclass
class VirtualIpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualIpDefinition = VirtualIpDefinition


