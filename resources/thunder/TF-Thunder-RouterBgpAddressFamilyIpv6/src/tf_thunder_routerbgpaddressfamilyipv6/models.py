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
    AsNumber: Optional[float]
    AutoSummary: Optional[float]
    Id: Optional[str]
    MaximumPathsValue: Optional[float]
    Originate: Optional[float]
    ProcessId: Optional[str]
    Synchronization: Optional[float]
    Uuid: Optional[str]
    AggregateAddressList: Optional[Sequence["_AggregateAddressListDefinition"]]
    Bgp: Optional[Sequence["_BgpDefinition"]]
    Distance: Optional[Sequence["_DistanceDefinition"]]
    Neighbor: Optional[Sequence["_NeighborDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
    Redistribute: Optional[Sequence["_RedistributeDefinition"]]

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
            AsNumber=json_data.get("AsNumber"),
            AutoSummary=json_data.get("AutoSummary"),
            Id=json_data.get("Id"),
            MaximumPathsValue=json_data.get("MaximumPathsValue"),
            Originate=json_data.get("Originate"),
            ProcessId=json_data.get("ProcessId"),
            Synchronization=json_data.get("Synchronization"),
            Uuid=json_data.get("Uuid"),
            AggregateAddressList=deserialize_list(json_data.get("AggregateAddressList"), AggregateAddressListDefinition),
            Bgp=deserialize_list(json_data.get("Bgp"), BgpDefinition),
            Distance=deserialize_list(json_data.get("Distance"), DistanceDefinition),
            Neighbor=deserialize_list(json_data.get("Neighbor"), NeighborDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            Redistribute=deserialize_list(json_data.get("Redistribute"), RedistributeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AggregateAddressListDefinition(BaseModel):
    AggregateAddress: Optional[str]
    AsSet: Optional[float]
    SummaryOnly: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AggregateAddressListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggregateAddressListDefinition"]:
        if not json_data:
            return None
        return cls(
            AggregateAddress=json_data.get("AggregateAddress"),
            AsSet=json_data.get("AsSet"),
            SummaryOnly=json_data.get("SummaryOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggregateAddressListDefinition = AggregateAddressListDefinition


@dataclass
class BgpDefinition(BaseModel):
    Dampening: Optional[float]
    DampeningHalf: Optional[float]
    DampeningMaxSupress: Optional[float]
    DampeningStartReuse: Optional[float]
    DampeningStartSupress: Optional[float]
    DampeningUnreachability: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BgpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpDefinition"]:
        if not json_data:
            return None
        return cls(
            Dampening=json_data.get("Dampening"),
            DampeningHalf=json_data.get("DampeningHalf"),
            DampeningMaxSupress=json_data.get("DampeningMaxSupress"),
            DampeningStartReuse=json_data.get("DampeningStartReuse"),
            DampeningStartSupress=json_data.get("DampeningStartSupress"),
            DampeningUnreachability=json_data.get("DampeningUnreachability"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpDefinition = BgpDefinition


@dataclass
class DistanceDefinition(BaseModel):
    DistanceExt: Optional[float]
    DistanceInt: Optional[float]
    DistanceLocal: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DistanceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DistanceDefinition"]:
        if not json_data:
            return None
        return cls(
            DistanceExt=json_data.get("DistanceExt"),
            DistanceInt=json_data.get("DistanceInt"),
            DistanceLocal=json_data.get("DistanceLocal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DistanceDefinition = DistanceDefinition


@dataclass
class NeighborDefinition(BaseModel):
    EthernetNeighborIpv6List: Optional[Sequence["_EthernetNeighborIpv6ListDefinition"]]
    Ipv4NeighborList: Optional[Sequence["_Ipv4NeighborListDefinition"]]
    Ipv6NeighborList: Optional[Sequence["_Ipv6NeighborListDefinition"]]
    PeerGroupNeighborList: Optional[Sequence["_PeerGroupNeighborListDefinition"]]
    Synchronization: Optional[Sequence["_SynchronizationDefinition"]]
    TrunkNeighborIpv6List: Optional[Sequence["_TrunkNeighborIpv6ListDefinition"]]
    VeNeighborIpv6List: Optional[Sequence["_VeNeighborIpv6ListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NeighborDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NeighborDefinition"]:
        if not json_data:
            return None
        return cls(
            EthernetNeighborIpv6List=deserialize_list(json_data.get("EthernetNeighborIpv6List"), EthernetNeighborIpv6ListDefinition),
            Ipv4NeighborList=deserialize_list(json_data.get("Ipv4NeighborList"), Ipv4NeighborListDefinition),
            Ipv6NeighborList=deserialize_list(json_data.get("Ipv6NeighborList"), Ipv6NeighborListDefinition),
            PeerGroupNeighborList=deserialize_list(json_data.get("PeerGroupNeighborList"), PeerGroupNeighborListDefinition),
            Synchronization=deserialize_list(json_data.get("Synchronization"), SynchronizationDefinition),
            TrunkNeighborIpv6List=deserialize_list(json_data.get("TrunkNeighborIpv6List"), TrunkNeighborIpv6ListDefinition),
            VeNeighborIpv6List=deserialize_list(json_data.get("VeNeighborIpv6List"), VeNeighborIpv6ListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NeighborDefinition = NeighborDefinition


@dataclass
class EthernetNeighborIpv6ListDefinition(BaseModel):
    Ethernet: Optional[float]
    PeerGroupName: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EthernetNeighborIpv6ListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EthernetNeighborIpv6ListDefinition"]:
        if not json_data:
            return None
        return cls(
            Ethernet=json_data.get("Ethernet"),
            PeerGroupName=json_data.get("PeerGroupName"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EthernetNeighborIpv6ListDefinition = EthernetNeighborIpv6ListDefinition


@dataclass
class Ipv4NeighborListDefinition(BaseModel):
    Activate: Optional[float]
    AllowasIn: Optional[float]
    AllowasInCount: Optional[float]
    DefaultOriginate: Optional[float]
    GracefulRestart: Optional[float]
    Inbound: Optional[float]
    MaximumPrefix: Optional[float]
    MaximumPrefixThres: Optional[float]
    NeighborIpv4: Optional[str]
    NextHopSelf: Optional[float]
    PeerGroupName: Optional[str]
    PrefixListDirection: Optional[str]
    RemovePrivateAs: Optional[float]
    RouteMap: Optional[str]
    SendCommunityVal: Optional[str]
    UnsuppressMap: Optional[str]
    Uuid: Optional[str]
    Weight: Optional[float]
    DistributeLists: Optional[Sequence["_DistributeListsDefinition"]]
    NeighborFilterLists: Optional[Sequence["_NeighborFilterListsDefinition"]]
    NeighborPrefixLists: Optional[Sequence["_NeighborPrefixListsDefinition"]]
    NeighborRouteMapLists: Optional[Sequence["_NeighborRouteMapListsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv4NeighborListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv4NeighborListDefinition"]:
        if not json_data:
            return None
        return cls(
            Activate=json_data.get("Activate"),
            AllowasIn=json_data.get("AllowasIn"),
            AllowasInCount=json_data.get("AllowasInCount"),
            DefaultOriginate=json_data.get("DefaultOriginate"),
            GracefulRestart=json_data.get("GracefulRestart"),
            Inbound=json_data.get("Inbound"),
            MaximumPrefix=json_data.get("MaximumPrefix"),
            MaximumPrefixThres=json_data.get("MaximumPrefixThres"),
            NeighborIpv4=json_data.get("NeighborIpv4"),
            NextHopSelf=json_data.get("NextHopSelf"),
            PeerGroupName=json_data.get("PeerGroupName"),
            PrefixListDirection=json_data.get("PrefixListDirection"),
            RemovePrivateAs=json_data.get("RemovePrivateAs"),
            RouteMap=json_data.get("RouteMap"),
            SendCommunityVal=json_data.get("SendCommunityVal"),
            UnsuppressMap=json_data.get("UnsuppressMap"),
            Uuid=json_data.get("Uuid"),
            Weight=json_data.get("Weight"),
            DistributeLists=deserialize_list(json_data.get("DistributeLists"), DistributeListsDefinition),
            NeighborFilterLists=deserialize_list(json_data.get("NeighborFilterLists"), NeighborFilterListsDefinition),
            NeighborPrefixLists=deserialize_list(json_data.get("NeighborPrefixLists"), NeighborPrefixListsDefinition),
            NeighborRouteMapLists=deserialize_list(json_data.get("NeighborRouteMapLists"), NeighborRouteMapListsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv4NeighborListDefinition = Ipv4NeighborListDefinition


@dataclass
class DistributeListsDefinition(BaseModel):
    DistributeList: Optional[str]
    DistributeListDirection: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DistributeListsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DistributeListsDefinition"]:
        if not json_data:
            return None
        return cls(
            DistributeList=json_data.get("DistributeList"),
            DistributeListDirection=json_data.get("DistributeListDirection"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DistributeListsDefinition = DistributeListsDefinition


@dataclass
class NeighborFilterListsDefinition(BaseModel):
    FilterList: Optional[str]
    FilterListDirection: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NeighborFilterListsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NeighborFilterListsDefinition"]:
        if not json_data:
            return None
        return cls(
            FilterList=json_data.get("FilterList"),
            FilterListDirection=json_data.get("FilterListDirection"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NeighborFilterListsDefinition = NeighborFilterListsDefinition


@dataclass
class NeighborPrefixListsDefinition(BaseModel):
    NbrPrefixList: Optional[str]
    NbrPrefixListDirection: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NeighborPrefixListsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NeighborPrefixListsDefinition"]:
        if not json_data:
            return None
        return cls(
            NbrPrefixList=json_data.get("NbrPrefixList"),
            NbrPrefixListDirection=json_data.get("NbrPrefixListDirection"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NeighborPrefixListsDefinition = NeighborPrefixListsDefinition


@dataclass
class NeighborRouteMapListsDefinition(BaseModel):
    NbrRmapDirection: Optional[str]
    NbrRouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NeighborRouteMapListsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NeighborRouteMapListsDefinition"]:
        if not json_data:
            return None
        return cls(
            NbrRmapDirection=json_data.get("NbrRmapDirection"),
            NbrRouteMap=json_data.get("NbrRouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NeighborRouteMapListsDefinition = NeighborRouteMapListsDefinition


@dataclass
class Ipv6NeighborListDefinition(BaseModel):
    Activate: Optional[float]
    AllowasIn: Optional[float]
    AllowasInCount: Optional[float]
    DefaultOriginate: Optional[float]
    GracefulRestart: Optional[float]
    Inbound: Optional[float]
    MaximumPrefix: Optional[float]
    MaximumPrefixThres: Optional[float]
    NeighborIpv6: Optional[str]
    NextHopSelf: Optional[float]
    PeerGroupName: Optional[str]
    PrefixListDirection: Optional[str]
    RemovePrivateAs: Optional[float]
    RouteMap: Optional[str]
    SendCommunityVal: Optional[str]
    UnsuppressMap: Optional[str]
    Uuid: Optional[str]
    Weight: Optional[float]
    DistributeLists: Optional[Sequence["_DistributeListsDefinition"]]
    NeighborFilterLists: Optional[Sequence["_NeighborFilterListsDefinition"]]
    NeighborPrefixLists: Optional[Sequence["_NeighborPrefixListsDefinition"]]
    NeighborRouteMapLists: Optional[Sequence["_NeighborRouteMapListsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6NeighborListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6NeighborListDefinition"]:
        if not json_data:
            return None
        return cls(
            Activate=json_data.get("Activate"),
            AllowasIn=json_data.get("AllowasIn"),
            AllowasInCount=json_data.get("AllowasInCount"),
            DefaultOriginate=json_data.get("DefaultOriginate"),
            GracefulRestart=json_data.get("GracefulRestart"),
            Inbound=json_data.get("Inbound"),
            MaximumPrefix=json_data.get("MaximumPrefix"),
            MaximumPrefixThres=json_data.get("MaximumPrefixThres"),
            NeighborIpv6=json_data.get("NeighborIpv6"),
            NextHopSelf=json_data.get("NextHopSelf"),
            PeerGroupName=json_data.get("PeerGroupName"),
            PrefixListDirection=json_data.get("PrefixListDirection"),
            RemovePrivateAs=json_data.get("RemovePrivateAs"),
            RouteMap=json_data.get("RouteMap"),
            SendCommunityVal=json_data.get("SendCommunityVal"),
            UnsuppressMap=json_data.get("UnsuppressMap"),
            Uuid=json_data.get("Uuid"),
            Weight=json_data.get("Weight"),
            DistributeLists=deserialize_list(json_data.get("DistributeLists"), DistributeListsDefinition),
            NeighborFilterLists=deserialize_list(json_data.get("NeighborFilterLists"), NeighborFilterListsDefinition),
            NeighborPrefixLists=deserialize_list(json_data.get("NeighborPrefixLists"), NeighborPrefixListsDefinition),
            NeighborRouteMapLists=deserialize_list(json_data.get("NeighborRouteMapLists"), NeighborRouteMapListsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6NeighborListDefinition = Ipv6NeighborListDefinition


@dataclass
class PeerGroupNeighborListDefinition(BaseModel):
    Activate: Optional[float]
    AllowasIn: Optional[float]
    AllowasInCount: Optional[float]
    DefaultOriginate: Optional[float]
    Inbound: Optional[float]
    MaximumPrefix: Optional[float]
    MaximumPrefixThres: Optional[float]
    NextHopSelf: Optional[float]
    PeerGroup: Optional[str]
    PrefixListDirection: Optional[str]
    RemovePrivateAs: Optional[float]
    RouteMap: Optional[str]
    SendCommunityVal: Optional[str]
    UnsuppressMap: Optional[str]
    Uuid: Optional[str]
    Weight: Optional[float]
    DistributeLists: Optional[Sequence["_DistributeListsDefinition"]]
    NeighborFilterLists: Optional[Sequence["_NeighborFilterListsDefinition"]]
    NeighborPrefixLists: Optional[Sequence["_NeighborPrefixListsDefinition"]]
    NeighborRouteMapLists: Optional[Sequence["_NeighborRouteMapListsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PeerGroupNeighborListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PeerGroupNeighborListDefinition"]:
        if not json_data:
            return None
        return cls(
            Activate=json_data.get("Activate"),
            AllowasIn=json_data.get("AllowasIn"),
            AllowasInCount=json_data.get("AllowasInCount"),
            DefaultOriginate=json_data.get("DefaultOriginate"),
            Inbound=json_data.get("Inbound"),
            MaximumPrefix=json_data.get("MaximumPrefix"),
            MaximumPrefixThres=json_data.get("MaximumPrefixThres"),
            NextHopSelf=json_data.get("NextHopSelf"),
            PeerGroup=json_data.get("PeerGroup"),
            PrefixListDirection=json_data.get("PrefixListDirection"),
            RemovePrivateAs=json_data.get("RemovePrivateAs"),
            RouteMap=json_data.get("RouteMap"),
            SendCommunityVal=json_data.get("SendCommunityVal"),
            UnsuppressMap=json_data.get("UnsuppressMap"),
            Uuid=json_data.get("Uuid"),
            Weight=json_data.get("Weight"),
            DistributeLists=deserialize_list(json_data.get("DistributeLists"), DistributeListsDefinition),
            NeighborFilterLists=deserialize_list(json_data.get("NeighborFilterLists"), NeighborFilterListsDefinition),
            NeighborPrefixLists=deserialize_list(json_data.get("NeighborPrefixLists"), NeighborPrefixListsDefinition),
            NeighborRouteMapLists=deserialize_list(json_data.get("NeighborRouteMapLists"), NeighborRouteMapListsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PeerGroupNeighborListDefinition = PeerGroupNeighborListDefinition


@dataclass
class SynchronizationDefinition(BaseModel):
    NetworkSynchronization: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SynchronizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SynchronizationDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkSynchronization=json_data.get("NetworkSynchronization"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SynchronizationDefinition = SynchronizationDefinition


@dataclass
class TrunkNeighborIpv6ListDefinition(BaseModel):
    PeerGroupName: Optional[str]
    Trunk: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrunkNeighborIpv6ListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrunkNeighborIpv6ListDefinition"]:
        if not json_data:
            return None
        return cls(
            PeerGroupName=json_data.get("PeerGroupName"),
            Trunk=json_data.get("Trunk"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrunkNeighborIpv6ListDefinition = TrunkNeighborIpv6ListDefinition


@dataclass
class VeNeighborIpv6ListDefinition(BaseModel):
    PeerGroupName: Optional[str]
    Uuid: Optional[str]
    Ve: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VeNeighborIpv6ListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VeNeighborIpv6ListDefinition"]:
        if not json_data:
            return None
        return cls(
            PeerGroupName=json_data.get("PeerGroupName"),
            Uuid=json_data.get("Uuid"),
            Ve=json_data.get("Ve"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VeNeighborIpv6ListDefinition = VeNeighborIpv6ListDefinition


@dataclass
class NetworkDefinition(BaseModel):
    Ipv6NetworkList: Optional[Sequence["_Ipv6NetworkListDefinition"]]
    Synchronization: Optional[Sequence["_SynchronizationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv6NetworkList=deserialize_list(json_data.get("Ipv6NetworkList"), Ipv6NetworkListDefinition),
            Synchronization=deserialize_list(json_data.get("Synchronization"), SynchronizationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class Ipv6NetworkListDefinition(BaseModel):
    Backdoor: Optional[float]
    CommValue: Optional[str]
    Description: Optional[str]
    NetworkIpv6: Optional[str]
    RouteMap: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6NetworkListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6NetworkListDefinition"]:
        if not json_data:
            return None
        return cls(
            Backdoor=json_data.get("Backdoor"),
            CommValue=json_data.get("CommValue"),
            Description=json_data.get("Description"),
            NetworkIpv6=json_data.get("NetworkIpv6"),
            RouteMap=json_data.get("RouteMap"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6NetworkListDefinition = Ipv6NetworkListDefinition


@dataclass
class RedistributeDefinition(BaseModel):
    Uuid: Optional[str]
    ConnectedCfg: Optional[Sequence["_ConnectedCfgDefinition"]]
    FloatingIpCfg: Optional[Sequence["_FloatingIpCfgDefinition"]]
    IpNatCfg: Optional[Sequence["_IpNatCfgDefinition"]]
    IpNatListCfg: Optional[Sequence["_IpNatListCfgDefinition"]]
    IsisCfg: Optional[Sequence["_IsisCfgDefinition"]]
    Lw4o6Cfg: Optional[Sequence["_Lw4o6CfgDefinition"]]
    Nat64Cfg: Optional[Sequence["_Nat64CfgDefinition"]]
    NatMapCfg: Optional[Sequence["_NatMapCfgDefinition"]]
    OspfCfg: Optional[Sequence["_OspfCfgDefinition"]]
    RipCfg: Optional[Sequence["_RipCfgDefinition"]]
    StaticCfg: Optional[Sequence["_StaticCfgDefinition"]]
    StaticNatCfg: Optional[Sequence["_StaticNatCfgDefinition"]]
    Vip: Optional[Sequence["_VipDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RedistributeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedistributeDefinition"]:
        if not json_data:
            return None
        return cls(
            Uuid=json_data.get("Uuid"),
            ConnectedCfg=deserialize_list(json_data.get("ConnectedCfg"), ConnectedCfgDefinition),
            FloatingIpCfg=deserialize_list(json_data.get("FloatingIpCfg"), FloatingIpCfgDefinition),
            IpNatCfg=deserialize_list(json_data.get("IpNatCfg"), IpNatCfgDefinition),
            IpNatListCfg=deserialize_list(json_data.get("IpNatListCfg"), IpNatListCfgDefinition),
            IsisCfg=deserialize_list(json_data.get("IsisCfg"), IsisCfgDefinition),
            Lw4o6Cfg=deserialize_list(json_data.get("Lw4o6Cfg"), Lw4o6CfgDefinition),
            Nat64Cfg=deserialize_list(json_data.get("Nat64Cfg"), Nat64CfgDefinition),
            NatMapCfg=deserialize_list(json_data.get("NatMapCfg"), NatMapCfgDefinition),
            OspfCfg=deserialize_list(json_data.get("OspfCfg"), OspfCfgDefinition),
            RipCfg=deserialize_list(json_data.get("RipCfg"), RipCfgDefinition),
            StaticCfg=deserialize_list(json_data.get("StaticCfg"), StaticCfgDefinition),
            StaticNatCfg=deserialize_list(json_data.get("StaticNatCfg"), StaticNatCfgDefinition),
            Vip=deserialize_list(json_data.get("Vip"), VipDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedistributeDefinition = RedistributeDefinition


@dataclass
class ConnectedCfgDefinition(BaseModel):
    Connected: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectedCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectedCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Connected=json_data.get("Connected"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectedCfgDefinition = ConnectedCfgDefinition


@dataclass
class FloatingIpCfgDefinition(BaseModel):
    FloatingIp: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FloatingIpCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FloatingIpCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            FloatingIp=json_data.get("FloatingIp"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FloatingIpCfgDefinition = FloatingIpCfgDefinition


@dataclass
class IpNatCfgDefinition(BaseModel):
    IpNat: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpNatCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpNatCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            IpNat=json_data.get("IpNat"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpNatCfgDefinition = IpNatCfgDefinition


@dataclass
class IpNatListCfgDefinition(BaseModel):
    IpNatList: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpNatListCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpNatListCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            IpNatList=json_data.get("IpNatList"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpNatListCfgDefinition = IpNatListCfgDefinition


@dataclass
class IsisCfgDefinition(BaseModel):
    Isis: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IsisCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IsisCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Isis=json_data.get("Isis"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IsisCfgDefinition = IsisCfgDefinition


@dataclass
class Lw4o6CfgDefinition(BaseModel):
    Lw4o6: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Lw4o6CfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Lw4o6CfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Lw4o6=json_data.get("Lw4o6"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Lw4o6CfgDefinition = Lw4o6CfgDefinition


@dataclass
class Nat64CfgDefinition(BaseModel):
    Nat64: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nat64CfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nat64CfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Nat64=json_data.get("Nat64"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nat64CfgDefinition = Nat64CfgDefinition


@dataclass
class NatMapCfgDefinition(BaseModel):
    NatMap: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NatMapCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NatMapCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            NatMap=json_data.get("NatMap"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NatMapCfgDefinition = NatMapCfgDefinition


@dataclass
class OspfCfgDefinition(BaseModel):
    Ospf: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OspfCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OspfCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Ospf=json_data.get("Ospf"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OspfCfgDefinition = OspfCfgDefinition


@dataclass
class RipCfgDefinition(BaseModel):
    Rip: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RipCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RipCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Rip=json_data.get("Rip"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RipCfgDefinition = RipCfgDefinition


@dataclass
class StaticCfgDefinition(BaseModel):
    RouteMap: Optional[str]
    Static: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StaticCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            RouteMap=json_data.get("RouteMap"),
            Static=json_data.get("Static"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticCfgDefinition = StaticCfgDefinition


@dataclass
class StaticNatCfgDefinition(BaseModel):
    RouteMap: Optional[str]
    StaticNat: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StaticNatCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticNatCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            RouteMap=json_data.get("RouteMap"),
            StaticNat=json_data.get("StaticNat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticNatCfgDefinition = StaticNatCfgDefinition


@dataclass
class VipDefinition(BaseModel):
    OnlyFlaggedCfg: Optional[Sequence["_OnlyFlaggedCfgDefinition"]]
    OnlyNotFlaggedCfg: Optional[Sequence["_OnlyNotFlaggedCfgDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VipDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VipDefinition"]:
        if not json_data:
            return None
        return cls(
            OnlyFlaggedCfg=deserialize_list(json_data.get("OnlyFlaggedCfg"), OnlyFlaggedCfgDefinition),
            OnlyNotFlaggedCfg=deserialize_list(json_data.get("OnlyNotFlaggedCfg"), OnlyNotFlaggedCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VipDefinition = VipDefinition


@dataclass
class OnlyFlaggedCfgDefinition(BaseModel):
    OnlyFlagged: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnlyFlaggedCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnlyFlaggedCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            OnlyFlagged=json_data.get("OnlyFlagged"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnlyFlaggedCfgDefinition = OnlyFlaggedCfgDefinition


@dataclass
class OnlyNotFlaggedCfgDefinition(BaseModel):
    OnlyNotFlagged: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnlyNotFlaggedCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnlyNotFlaggedCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            OnlyNotFlagged=json_data.get("OnlyNotFlagged"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnlyNotFlaggedCfgDefinition = OnlyNotFlaggedCfgDefinition


