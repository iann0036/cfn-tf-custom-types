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
    AccessVlans: Optional[str]
    AdminState: Optional[bool]
    AllowedVlans: Optional[str]
    BpduGaurdFlag: Optional[str]
    Configuration: Optional[str]
    Deploy: Optional[bool]
    Description: Optional[str]
    EthernetSpeed: Optional[str]
    FabricName: Optional[str]
    Id: Optional[str]
    Ipv4: Optional[str]
    Ipv4Prefix: Optional[str]
    Ipv6: Optional[str]
    Ipv6Prefix: Optional[str]
    LoopbackLsRouting: Optional[str]
    LoopbackReplicationMode: Optional[str]
    LoopbackRouterId: Optional[str]
    LoopbackRoutingTag: Optional[str]
    LoopbackTag: Optional[str]
    Mode: Optional[str]
    Mtu: Optional[str]
    Name: Optional[str]
    PcInterface: Optional[Sequence[str]]
    Policy: Optional[str]
    PortFastFlag: Optional[bool]
    SerialNumber: Optional[str]
    SubinterfaceMtu: Optional[str]
    SubinterfaceVlan: Optional[float]
    SwitchName1: Optional[str]
    SwitchName2: Optional[str]
    Type: Optional[str]
    VpcPeer1AccessVlans: Optional[str]
    VpcPeer1AllowedVlans: Optional[str]
    VpcPeer1Conf: Optional[str]
    VpcPeer1Desc: Optional[str]
    VpcPeer1Id: Optional[float]
    VpcPeer1Interface: Optional[Sequence[str]]
    VpcPeer2AccessVlans: Optional[str]
    VpcPeer2AllowedVlans: Optional[str]
    VpcPeer2Conf: Optional[str]
    VpcPeer2Desc: Optional[str]
    VpcPeer2Id: Optional[float]
    VpcPeer2Interface: Optional[Sequence[str]]
    Vrf: Optional[str]

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
            AccessVlans=json_data.get("AccessVlans"),
            AdminState=json_data.get("AdminState"),
            AllowedVlans=json_data.get("AllowedVlans"),
            BpduGaurdFlag=json_data.get("BpduGaurdFlag"),
            Configuration=json_data.get("Configuration"),
            Deploy=json_data.get("Deploy"),
            Description=json_data.get("Description"),
            EthernetSpeed=json_data.get("EthernetSpeed"),
            FabricName=json_data.get("FabricName"),
            Id=json_data.get("Id"),
            Ipv4=json_data.get("Ipv4"),
            Ipv4Prefix=json_data.get("Ipv4Prefix"),
            Ipv6=json_data.get("Ipv6"),
            Ipv6Prefix=json_data.get("Ipv6Prefix"),
            LoopbackLsRouting=json_data.get("LoopbackLsRouting"),
            LoopbackReplicationMode=json_data.get("LoopbackReplicationMode"),
            LoopbackRouterId=json_data.get("LoopbackRouterId"),
            LoopbackRoutingTag=json_data.get("LoopbackRoutingTag"),
            LoopbackTag=json_data.get("LoopbackTag"),
            Mode=json_data.get("Mode"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            PcInterface=json_data.get("PcInterface"),
            Policy=json_data.get("Policy"),
            PortFastFlag=json_data.get("PortFastFlag"),
            SerialNumber=json_data.get("SerialNumber"),
            SubinterfaceMtu=json_data.get("SubinterfaceMtu"),
            SubinterfaceVlan=json_data.get("SubinterfaceVlan"),
            SwitchName1=json_data.get("SwitchName1"),
            SwitchName2=json_data.get("SwitchName2"),
            Type=json_data.get("Type"),
            VpcPeer1AccessVlans=json_data.get("VpcPeer1AccessVlans"),
            VpcPeer1AllowedVlans=json_data.get("VpcPeer1AllowedVlans"),
            VpcPeer1Conf=json_data.get("VpcPeer1Conf"),
            VpcPeer1Desc=json_data.get("VpcPeer1Desc"),
            VpcPeer1Id=json_data.get("VpcPeer1Id"),
            VpcPeer1Interface=json_data.get("VpcPeer1Interface"),
            VpcPeer2AccessVlans=json_data.get("VpcPeer2AccessVlans"),
            VpcPeer2AllowedVlans=json_data.get("VpcPeer2AllowedVlans"),
            VpcPeer2Conf=json_data.get("VpcPeer2Conf"),
            VpcPeer2Desc=json_data.get("VpcPeer2Desc"),
            VpcPeer2Id=json_data.get("VpcPeer2Id"),
            VpcPeer2Interface=json_data.get("VpcPeer2Interface"),
            Vrf=json_data.get("Vrf"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


