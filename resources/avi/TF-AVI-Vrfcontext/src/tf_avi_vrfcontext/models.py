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
    CloudRef: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    LldpEnable: Optional[bool]
    Name: Optional[str]
    SystemDefault: Optional[bool]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    Attrs: Optional[Sequence["_AttrsDefinition"]]
    BfdProfile: Optional[Sequence["_BfdProfileDefinition"]]
    BgpProfile: Optional[Sequence["_BgpProfileDefinition"]]
    Debugvrfcontext: Optional[Sequence["_DebugvrfcontextDefinition"]]
    GatewayMon: Optional[Sequence["_GatewayMonDefinition"]]
    InternalGatewayMonitor: Optional[Sequence["_InternalGatewayMonitorDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    StaticRoutes: Optional[Sequence["_StaticRoutesDefinition"]]

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
            CloudRef=json_data.get("CloudRef"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            LldpEnable=json_data.get("LldpEnable"),
            Name=json_data.get("Name"),
            SystemDefault=json_data.get("SystemDefault"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            Attrs=deserialize_list(json_data.get("Attrs"), AttrsDefinition),
            BfdProfile=deserialize_list(json_data.get("BfdProfile"), BfdProfileDefinition),
            BgpProfile=deserialize_list(json_data.get("BgpProfile"), BgpProfileDefinition),
            Debugvrfcontext=deserialize_list(json_data.get("Debugvrfcontext"), DebugvrfcontextDefinition),
            GatewayMon=deserialize_list(json_data.get("GatewayMon"), GatewayMonDefinition),
            InternalGatewayMonitor=deserialize_list(json_data.get("InternalGatewayMonitor"), InternalGatewayMonitorDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            StaticRoutes=deserialize_list(json_data.get("StaticRoutes"), StaticRoutesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AttrsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttrsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttrsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttrsDefinition = AttrsDefinition


@dataclass
class BfdProfileDefinition(BaseModel):
    Minrx: Optional[float]
    Mintx: Optional[float]
    Multi: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BfdProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BfdProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            Minrx=json_data.get("Minrx"),
            Mintx=json_data.get("Mintx"),
            Multi=json_data.get("Multi"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BfdProfileDefinition = BfdProfileDefinition


@dataclass
class BgpProfileDefinition(BaseModel):
    Community: Optional[Sequence[str]]
    HoldTime: Optional[float]
    Ibgp: Optional[bool]
    KeepaliveInterval: Optional[float]
    LocalAs: Optional[float]
    LocalPreference: Optional[float]
    NumAsPathPrepend: Optional[float]
    SendCommunity: Optional[bool]
    Shutdown: Optional[bool]
    IpCommunities: Optional[Sequence["_IpCommunitiesDefinition"]]
    Peers: Optional[Sequence["_PeersDefinition"]]
    RoutingOptions: Optional[Sequence["_RoutingOptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BgpProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            Community=json_data.get("Community"),
            HoldTime=json_data.get("HoldTime"),
            Ibgp=json_data.get("Ibgp"),
            KeepaliveInterval=json_data.get("KeepaliveInterval"),
            LocalAs=json_data.get("LocalAs"),
            LocalPreference=json_data.get("LocalPreference"),
            NumAsPathPrepend=json_data.get("NumAsPathPrepend"),
            SendCommunity=json_data.get("SendCommunity"),
            Shutdown=json_data.get("Shutdown"),
            IpCommunities=deserialize_list(json_data.get("IpCommunities"), IpCommunitiesDefinition),
            Peers=deserialize_list(json_data.get("Peers"), PeersDefinition),
            RoutingOptions=deserialize_list(json_data.get("RoutingOptions"), RoutingOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpProfileDefinition = BgpProfileDefinition


@dataclass
class IpCommunitiesDefinition(BaseModel):
    Community: Optional[Sequence[str]]
    IpBegin: Optional[Sequence["_IpBeginDefinition"]]
    IpEnd: Optional[Sequence["_IpEndDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpCommunitiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpCommunitiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Community=json_data.get("Community"),
            IpBegin=deserialize_list(json_data.get("IpBegin"), IpBeginDefinition),
            IpEnd=deserialize_list(json_data.get("IpEnd"), IpEndDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpCommunitiesDefinition = IpCommunitiesDefinition


@dataclass
class IpBeginDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpBeginDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpBeginDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpBeginDefinition = IpBeginDefinition


@dataclass
class IpEndDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpEndDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpEndDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpEndDefinition = IpEndDefinition


@dataclass
class PeersDefinition(BaseModel):
    AdvertiseSnatIp: Optional[bool]
    AdvertiseVip: Optional[bool]
    AdvertisementInterval: Optional[float]
    Bfd: Optional[bool]
    ConnectTimer: Optional[float]
    EbgpMultihop: Optional[float]
    HoldTime: Optional[float]
    IbgpLocalAsOverride: Optional[bool]
    KeepaliveInterval: Optional[float]
    Label: Optional[str]
    LocalAs: Optional[float]
    Md5Secret: Optional[str]
    NetworkRef: Optional[str]
    RemoteAs: Optional[float]
    Shutdown: Optional[bool]
    PeerIp: Optional[Sequence["_PeerIpDefinition"]]
    PeerIp6: Optional[Sequence["_PeerIp6Definition"]]
    Subnet: Optional[Sequence["_SubnetDefinition"]]
    Subnet6: Optional[Sequence["_Subnet6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PeersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PeersDefinition"]:
        if not json_data:
            return None
        return cls(
            AdvertiseSnatIp=json_data.get("AdvertiseSnatIp"),
            AdvertiseVip=json_data.get("AdvertiseVip"),
            AdvertisementInterval=json_data.get("AdvertisementInterval"),
            Bfd=json_data.get("Bfd"),
            ConnectTimer=json_data.get("ConnectTimer"),
            EbgpMultihop=json_data.get("EbgpMultihop"),
            HoldTime=json_data.get("HoldTime"),
            IbgpLocalAsOverride=json_data.get("IbgpLocalAsOverride"),
            KeepaliveInterval=json_data.get("KeepaliveInterval"),
            Label=json_data.get("Label"),
            LocalAs=json_data.get("LocalAs"),
            Md5Secret=json_data.get("Md5Secret"),
            NetworkRef=json_data.get("NetworkRef"),
            RemoteAs=json_data.get("RemoteAs"),
            Shutdown=json_data.get("Shutdown"),
            PeerIp=deserialize_list(json_data.get("PeerIp"), PeerIpDefinition),
            PeerIp6=deserialize_list(json_data.get("PeerIp6"), PeerIp6Definition),
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
            Subnet6=deserialize_list(json_data.get("Subnet6"), Subnet6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PeersDefinition = PeersDefinition


@dataclass
class PeerIpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PeerIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PeerIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PeerIpDefinition = PeerIpDefinition


@dataclass
class PeerIp6Definition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PeerIp6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PeerIp6Definition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PeerIp6Definition = PeerIp6Definition


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
class RoutingOptionsDefinition(BaseModel):
    AdvertiseDefaultRoute: Optional[bool]
    AdvertiseLearnedRoutes: Optional[bool]
    Label: Optional[str]
    LearnOnlyDefaultRoute: Optional[bool]
    LearnRoutes: Optional[bool]
    MaxLearnLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdvertiseDefaultRoute=json_data.get("AdvertiseDefaultRoute"),
            AdvertiseLearnedRoutes=json_data.get("AdvertiseLearnedRoutes"),
            Label=json_data.get("Label"),
            LearnOnlyDefaultRoute=json_data.get("LearnOnlyDefaultRoute"),
            LearnRoutes=json_data.get("LearnRoutes"),
            MaxLearnLimit=json_data.get("MaxLearnLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingOptionsDefinition = RoutingOptionsDefinition


@dataclass
class DebugvrfcontextDefinition(BaseModel):
    CommandBufferInterval: Optional[float]
    CommandBufferSize: Optional[float]
    Flags: Optional[Sequence["_FlagsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DebugvrfcontextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DebugvrfcontextDefinition"]:
        if not json_data:
            return None
        return cls(
            CommandBufferInterval=json_data.get("CommandBufferInterval"),
            CommandBufferSize=json_data.get("CommandBufferSize"),
            Flags=deserialize_list(json_data.get("Flags"), FlagsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DebugvrfcontextDefinition = DebugvrfcontextDefinition


@dataclass
class FlagsDefinition(BaseModel):
    Flag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FlagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Flag=json_data.get("Flag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlagsDefinition = FlagsDefinition


@dataclass
class GatewayMonDefinition(BaseModel):
    GatewayMonitorFailThreshold: Optional[float]
    GatewayMonitorInterval: Optional[float]
    GatewayMonitorSuccessThreshold: Optional[float]
    GatewayIp: Optional[Sequence["_GatewayIpDefinition"]]
    Subnet: Optional[Sequence["_SubnetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayMonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayMonDefinition"]:
        if not json_data:
            return None
        return cls(
            GatewayMonitorFailThreshold=json_data.get("GatewayMonitorFailThreshold"),
            GatewayMonitorInterval=json_data.get("GatewayMonitorInterval"),
            GatewayMonitorSuccessThreshold=json_data.get("GatewayMonitorSuccessThreshold"),
            GatewayIp=deserialize_list(json_data.get("GatewayIp"), GatewayIpDefinition),
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayMonDefinition = GatewayMonDefinition


@dataclass
class GatewayIpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayIpDefinition = GatewayIpDefinition


@dataclass
class InternalGatewayMonitorDefinition(BaseModel):
    DisableGatewayMonitor: Optional[bool]
    GatewayMonitorFailureThreshold: Optional[float]
    GatewayMonitorInterval: Optional[float]
    GatewayMonitorSuccessThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InternalGatewayMonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternalGatewayMonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableGatewayMonitor=json_data.get("DisableGatewayMonitor"),
            GatewayMonitorFailureThreshold=json_data.get("GatewayMonitorFailureThreshold"),
            GatewayMonitorInterval=json_data.get("GatewayMonitorInterval"),
            GatewayMonitorSuccessThreshold=json_data.get("GatewayMonitorSuccessThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternalGatewayMonitorDefinition = InternalGatewayMonitorDefinition


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


@dataclass
class StaticRoutesDefinition(BaseModel):
    DisableGatewayMonitor: Optional[bool]
    IfName: Optional[str]
    RouteId: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    NextHop: Optional[Sequence["_NextHopDefinition"]]
    Prefix: Optional[Sequence["_PrefixDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StaticRoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticRoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableGatewayMonitor=json_data.get("DisableGatewayMonitor"),
            IfName=json_data.get("IfName"),
            RouteId=json_data.get("RouteId"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            NextHop=deserialize_list(json_data.get("NextHop"), NextHopDefinition),
            Prefix=deserialize_list(json_data.get("Prefix"), PrefixDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticRoutesDefinition = StaticRoutesDefinition


@dataclass
class LabelsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class NextHopDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NextHopDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NextHopDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NextHopDefinition = NextHopDefinition


@dataclass
class PrefixDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixDefinition = PrefixDefinition


