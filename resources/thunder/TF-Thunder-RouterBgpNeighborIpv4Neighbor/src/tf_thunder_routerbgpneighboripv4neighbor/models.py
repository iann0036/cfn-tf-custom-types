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
    AcosApplicationOnly: Optional[float]
    Activate: Optional[float]
    AdvertisementInterval: Optional[float]
    AllowasIn: Optional[float]
    AllowasInCount: Optional[float]
    AsNumber: Optional[float]
    AsOriginationInterval: Optional[float]
    Bfd: Optional[float]
    BfdValue: Optional[str]
    CollideEstablished: Optional[float]
    Connect: Optional[float]
    DefaultOriginate: Optional[float]
    Description: Optional[str]
    DisallowInfiniteHoldtime: Optional[float]
    DontCapabilityNegotiate: Optional[float]
    Dynamic: Optional[float]
    EbgpMultihop: Optional[float]
    EbgpMultihopHopCount: Optional[float]
    EnforceMultihop: Optional[float]
    Ethernet: Optional[float]
    GracefulRestart: Optional[float]
    Id: Optional[str]
    Inbound: Optional[float]
    KeyId: Optional[float]
    KeyType: Optional[str]
    Lif: Optional[float]
    Loopback: Optional[float]
    MaximumPrefix: Optional[float]
    MaximumPrefixThres: Optional[float]
    Multihop: Optional[float]
    NbrRemoteAs: Optional[float]
    NeighborIpv4: Optional[str]
    NextHopSelf: Optional[float]
    OverrideCapability: Optional[float]
    PassValue: Optional[str]
    Passive: Optional[float]
    PeerGroupName: Optional[str]
    PrefixListDirection: Optional[str]
    RemovePrivateAs: Optional[float]
    RouteMap: Optional[str]
    RouteRefresh: Optional[float]
    SendCommunityVal: Optional[str]
    Shutdown: Optional[float]
    StrictCapabilityMatch: Optional[float]
    TimersHoldtime: Optional[float]
    TimersKeepalive: Optional[float]
    Trunk: Optional[float]
    Tunnel: Optional[float]
    UnsuppressMap: Optional[str]
    UpdateSourceIp: Optional[str]
    UpdateSourceIpv6: Optional[str]
    Uuid: Optional[str]
    Ve: Optional[float]
    Weight: Optional[float]
    DistributeLists: Optional[Sequence["_DistributeListsDefinition"]]
    NeighborFilterLists: Optional[Sequence["_NeighborFilterListsDefinition"]]
    NeighborPrefixLists: Optional[Sequence["_NeighborPrefixListsDefinition"]]
    NeighborRouteMapLists: Optional[Sequence["_NeighborRouteMapListsDefinition"]]

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
            AcosApplicationOnly=json_data.get("AcosApplicationOnly"),
            Activate=json_data.get("Activate"),
            AdvertisementInterval=json_data.get("AdvertisementInterval"),
            AllowasIn=json_data.get("AllowasIn"),
            AllowasInCount=json_data.get("AllowasInCount"),
            AsNumber=json_data.get("AsNumber"),
            AsOriginationInterval=json_data.get("AsOriginationInterval"),
            Bfd=json_data.get("Bfd"),
            BfdValue=json_data.get("BfdValue"),
            CollideEstablished=json_data.get("CollideEstablished"),
            Connect=json_data.get("Connect"),
            DefaultOriginate=json_data.get("DefaultOriginate"),
            Description=json_data.get("Description"),
            DisallowInfiniteHoldtime=json_data.get("DisallowInfiniteHoldtime"),
            DontCapabilityNegotiate=json_data.get("DontCapabilityNegotiate"),
            Dynamic=json_data.get("Dynamic"),
            EbgpMultihop=json_data.get("EbgpMultihop"),
            EbgpMultihopHopCount=json_data.get("EbgpMultihopHopCount"),
            EnforceMultihop=json_data.get("EnforceMultihop"),
            Ethernet=json_data.get("Ethernet"),
            GracefulRestart=json_data.get("GracefulRestart"),
            Id=json_data.get("Id"),
            Inbound=json_data.get("Inbound"),
            KeyId=json_data.get("KeyId"),
            KeyType=json_data.get("KeyType"),
            Lif=json_data.get("Lif"),
            Loopback=json_data.get("Loopback"),
            MaximumPrefix=json_data.get("MaximumPrefix"),
            MaximumPrefixThres=json_data.get("MaximumPrefixThres"),
            Multihop=json_data.get("Multihop"),
            NbrRemoteAs=json_data.get("NbrRemoteAs"),
            NeighborIpv4=json_data.get("NeighborIpv4"),
            NextHopSelf=json_data.get("NextHopSelf"),
            OverrideCapability=json_data.get("OverrideCapability"),
            PassValue=json_data.get("PassValue"),
            Passive=json_data.get("Passive"),
            PeerGroupName=json_data.get("PeerGroupName"),
            PrefixListDirection=json_data.get("PrefixListDirection"),
            RemovePrivateAs=json_data.get("RemovePrivateAs"),
            RouteMap=json_data.get("RouteMap"),
            RouteRefresh=json_data.get("RouteRefresh"),
            SendCommunityVal=json_data.get("SendCommunityVal"),
            Shutdown=json_data.get("Shutdown"),
            StrictCapabilityMatch=json_data.get("StrictCapabilityMatch"),
            TimersHoldtime=json_data.get("TimersHoldtime"),
            TimersKeepalive=json_data.get("TimersKeepalive"),
            Trunk=json_data.get("Trunk"),
            Tunnel=json_data.get("Tunnel"),
            UnsuppressMap=json_data.get("UnsuppressMap"),
            UpdateSourceIp=json_data.get("UpdateSourceIp"),
            UpdateSourceIpv6=json_data.get("UpdateSourceIpv6"),
            Uuid=json_data.get("Uuid"),
            Ve=json_data.get("Ve"),
            Weight=json_data.get("Weight"),
            DistributeLists=deserialize_list(json_data.get("DistributeLists"), DistributeListsDefinition),
            NeighborFilterLists=deserialize_list(json_data.get("NeighborFilterLists"), NeighborFilterListsDefinition),
            NeighborPrefixLists=deserialize_list(json_data.get("NeighborPrefixLists"), NeighborPrefixListsDefinition),
            NeighborRouteMapLists=deserialize_list(json_data.get("NeighborRouteMapLists"), NeighborRouteMapListsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


