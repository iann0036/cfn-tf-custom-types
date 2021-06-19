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
    AddRoute: Optional[str]
    AutoNegotiate: Optional[str]
    Comments: Optional[str]
    DhcpIpsec: Optional[str]
    Dhgrp: Optional[str]
    Diffserv: Optional[str]
    Diffservcode: Optional[str]
    DstAddrType: Optional[str]
    DstEndIp: Optional[str]
    DstEndIp6: Optional[str]
    DstName: Optional[str]
    DstName6: Optional[str]
    DstPort: Optional[float]
    DstStartIp: Optional[str]
    DstStartIp6: Optional[str]
    DstSubnet: Optional[str]
    DstSubnet6: Optional[str]
    Encapsulation: Optional[str]
    Id: Optional[str]
    InitiatorTsNarrow: Optional[str]
    Ipv4Df: Optional[str]
    Keepalive: Optional[str]
    KeylifeType: Optional[str]
    Keylifekbs: Optional[float]
    Keylifeseconds: Optional[float]
    L2tp: Optional[str]
    Name: Optional[str]
    Pfs: Optional[str]
    Phase1name: Optional[str]
    Proposal: Optional[str]
    Protocol: Optional[float]
    Replay: Optional[str]
    RouteOverlap: Optional[str]
    SelectorMatch: Optional[str]
    SingleSource: Optional[str]
    SrcAddrType: Optional[str]
    SrcEndIp: Optional[str]
    SrcEndIp6: Optional[str]
    SrcName: Optional[str]
    SrcName6: Optional[str]
    SrcPort: Optional[float]
    SrcStartIp: Optional[str]
    SrcStartIp6: Optional[str]
    SrcSubnet: Optional[str]
    SrcSubnet6: Optional[str]
    UseNatip: Optional[str]
    Vdomparam: Optional[str]

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
            AddRoute=json_data.get("AddRoute"),
            AutoNegotiate=json_data.get("AutoNegotiate"),
            Comments=json_data.get("Comments"),
            DhcpIpsec=json_data.get("DhcpIpsec"),
            Dhgrp=json_data.get("Dhgrp"),
            Diffserv=json_data.get("Diffserv"),
            Diffservcode=json_data.get("Diffservcode"),
            DstAddrType=json_data.get("DstAddrType"),
            DstEndIp=json_data.get("DstEndIp"),
            DstEndIp6=json_data.get("DstEndIp6"),
            DstName=json_data.get("DstName"),
            DstName6=json_data.get("DstName6"),
            DstPort=json_data.get("DstPort"),
            DstStartIp=json_data.get("DstStartIp"),
            DstStartIp6=json_data.get("DstStartIp6"),
            DstSubnet=json_data.get("DstSubnet"),
            DstSubnet6=json_data.get("DstSubnet6"),
            Encapsulation=json_data.get("Encapsulation"),
            Id=json_data.get("Id"),
            InitiatorTsNarrow=json_data.get("InitiatorTsNarrow"),
            Ipv4Df=json_data.get("Ipv4Df"),
            Keepalive=json_data.get("Keepalive"),
            KeylifeType=json_data.get("KeylifeType"),
            Keylifekbs=json_data.get("Keylifekbs"),
            Keylifeseconds=json_data.get("Keylifeseconds"),
            L2tp=json_data.get("L2tp"),
            Name=json_data.get("Name"),
            Pfs=json_data.get("Pfs"),
            Phase1name=json_data.get("Phase1name"),
            Proposal=json_data.get("Proposal"),
            Protocol=json_data.get("Protocol"),
            Replay=json_data.get("Replay"),
            RouteOverlap=json_data.get("RouteOverlap"),
            SelectorMatch=json_data.get("SelectorMatch"),
            SingleSource=json_data.get("SingleSource"),
            SrcAddrType=json_data.get("SrcAddrType"),
            SrcEndIp=json_data.get("SrcEndIp"),
            SrcEndIp6=json_data.get("SrcEndIp6"),
            SrcName=json_data.get("SrcName"),
            SrcName6=json_data.get("SrcName6"),
            SrcPort=json_data.get("SrcPort"),
            SrcStartIp=json_data.get("SrcStartIp"),
            SrcStartIp6=json_data.get("SrcStartIp6"),
            SrcSubnet=json_data.get("SrcSubnet"),
            SrcSubnet6=json_data.get("SrcSubnet6"),
            UseNatip=json_data.get("UseNatip"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


