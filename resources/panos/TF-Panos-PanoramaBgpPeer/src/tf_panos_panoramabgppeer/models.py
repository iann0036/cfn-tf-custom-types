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
    AddressFamilyType: Optional[str]
    AllowIncomingConnections: Optional[bool]
    AllowOutgoingConnections: Optional[bool]
    AuthProfile: Optional[str]
    BfdProfile: Optional[str]
    BgpPeerGroup: Optional[str]
    Enable: Optional[bool]
    EnableMpBgp: Optional[bool]
    EnableSenderSideLoopDetection: Optional[bool]
    HoldTime: Optional[float]
    Id: Optional[str]
    IdleHoldTime: Optional[float]
    IncomingConnectionsRemotePort: Optional[float]
    KeepAliveInterval: Optional[float]
    LocalAddressInterface: Optional[str]
    LocalAddressIp: Optional[str]
    MaxPrefixes: Optional[str]
    MinRouteAdvertisementInterval: Optional[float]
    MultiHop: Optional[float]
    Name: Optional[str]
    OpenDelayTime: Optional[float]
    OutgoingConnectionsLocalPort: Optional[float]
    PeerAddressIp: Optional[str]
    PeerAs: Optional[str]
    PeeringType: Optional[str]
    ReflectorClient: Optional[str]
    SubsequentAddressFamilyMulticast: Optional[bool]
    SubsequentAddressFamilyUnicast: Optional[bool]
    Template: Optional[str]
    TemplateStack: Optional[str]
    VirtualRouter: Optional[str]

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
            AddressFamilyType=json_data.get("AddressFamilyType"),
            AllowIncomingConnections=json_data.get("AllowIncomingConnections"),
            AllowOutgoingConnections=json_data.get("AllowOutgoingConnections"),
            AuthProfile=json_data.get("AuthProfile"),
            BfdProfile=json_data.get("BfdProfile"),
            BgpPeerGroup=json_data.get("BgpPeerGroup"),
            Enable=json_data.get("Enable"),
            EnableMpBgp=json_data.get("EnableMpBgp"),
            EnableSenderSideLoopDetection=json_data.get("EnableSenderSideLoopDetection"),
            HoldTime=json_data.get("HoldTime"),
            Id=json_data.get("Id"),
            IdleHoldTime=json_data.get("IdleHoldTime"),
            IncomingConnectionsRemotePort=json_data.get("IncomingConnectionsRemotePort"),
            KeepAliveInterval=json_data.get("KeepAliveInterval"),
            LocalAddressInterface=json_data.get("LocalAddressInterface"),
            LocalAddressIp=json_data.get("LocalAddressIp"),
            MaxPrefixes=json_data.get("MaxPrefixes"),
            MinRouteAdvertisementInterval=json_data.get("MinRouteAdvertisementInterval"),
            MultiHop=json_data.get("MultiHop"),
            Name=json_data.get("Name"),
            OpenDelayTime=json_data.get("OpenDelayTime"),
            OutgoingConnectionsLocalPort=json_data.get("OutgoingConnectionsLocalPort"),
            PeerAddressIp=json_data.get("PeerAddressIp"),
            PeerAs=json_data.get("PeerAs"),
            PeeringType=json_data.get("PeeringType"),
            ReflectorClient=json_data.get("ReflectorClient"),
            SubsequentAddressFamilyMulticast=json_data.get("SubsequentAddressFamilyMulticast"),
            SubsequentAddressFamilyUnicast=json_data.get("SubsequentAddressFamilyUnicast"),
            Template=json_data.get("Template"),
            TemplateStack=json_data.get("TemplateStack"),
            VirtualRouter=json_data.get("VirtualRouter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


