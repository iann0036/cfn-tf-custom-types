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
    AdditionalPath: Optional[str]
    AdditionalPath6: Optional[str]
    AdditionalPathSelect: Optional[float]
    AdditionalPathSelect6: Optional[float]
    AlwaysCompareMed: Optional[str]
    As: Optional[float]
    BestpathAsPathIgnore: Optional[str]
    BestpathCmpConfedAspath: Optional[str]
    BestpathCmpRouterid: Optional[str]
    BestpathMedConfed: Optional[str]
    BestpathMedMissingAsWorst: Optional[str]
    ClientToClientReflection: Optional[str]
    ClusterId: Optional[str]
    ConfederationIdentifier: Optional[float]
    Dampening: Optional[str]
    DampeningMaxSuppressTime: Optional[float]
    DampeningReachabilityHalfLife: Optional[float]
    DampeningReuse: Optional[float]
    DampeningRouteMap: Optional[str]
    DampeningSuppress: Optional[float]
    DampeningUnreachabilityHalfLife: Optional[float]
    DefaultLocalPreference: Optional[float]
    DeterministicMed: Optional[str]
    DistanceExternal: Optional[float]
    DistanceInternal: Optional[float]
    DistanceLocal: Optional[float]
    DynamicSortSubtable: Optional[str]
    EbgpMultipath: Optional[str]
    EnforceFirstAs: Optional[str]
    FastExternalFailover: Optional[str]
    GracefulEndOnTimer: Optional[str]
    GracefulRestart: Optional[str]
    GracefulRestartTime: Optional[float]
    GracefulStalepathTime: Optional[float]
    GracefulUpdateDelay: Optional[float]
    HoldtimeTimer: Optional[float]
    IbgpMultipath: Optional[str]
    Id: Optional[str]
    IgnoreOptionalCapability: Optional[str]
    KeepaliveTimer: Optional[float]
    LogNeighbourChanges: Optional[str]
    MultipathRecursiveDistance: Optional[str]
    NetworkImportCheck: Optional[str]
    RecursiveNextHop: Optional[str]
    RouterId: Optional[str]
    ScanTime: Optional[float]
    Synchronization: Optional[str]
    Vdomparam: Optional[str]
    AdminDistance: Optional[Sequence["_AdminDistanceDefinition"]]
    AggregateAddress: Optional[Sequence["_AggregateAddressDefinition"]]
    AggregateAddress6: Optional[Sequence["_AggregateAddress6Definition"]]
    ConfederationPeers: Optional[Sequence["_ConfederationPeersDefinition"]]
    Neighbor: Optional[Sequence["_NeighborDefinition"]]
    NeighborGroup: Optional[Sequence["_NeighborGroupDefinition"]]
    NeighborRange: Optional[Sequence["_NeighborRangeDefinition"]]
    NeighborRange6: Optional[Sequence["_NeighborRange6Definition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
    Network6: Optional[Sequence["_Network6Definition"]]
    Redistribute: Optional[Sequence["_RedistributeDefinition"]]
    Redistribute6: Optional[Sequence["_Redistribute6Definition"]]
    VrfLeak: Optional[Sequence["_VrfLeakDefinition"]]

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
            AdditionalPath=json_data.get("AdditionalPath"),
            AdditionalPath6=json_data.get("AdditionalPath6"),
            AdditionalPathSelect=json_data.get("AdditionalPathSelect"),
            AdditionalPathSelect6=json_data.get("AdditionalPathSelect6"),
            AlwaysCompareMed=json_data.get("AlwaysCompareMed"),
            As=json_data.get("As"),
            BestpathAsPathIgnore=json_data.get("BestpathAsPathIgnore"),
            BestpathCmpConfedAspath=json_data.get("BestpathCmpConfedAspath"),
            BestpathCmpRouterid=json_data.get("BestpathCmpRouterid"),
            BestpathMedConfed=json_data.get("BestpathMedConfed"),
            BestpathMedMissingAsWorst=json_data.get("BestpathMedMissingAsWorst"),
            ClientToClientReflection=json_data.get("ClientToClientReflection"),
            ClusterId=json_data.get("ClusterId"),
            ConfederationIdentifier=json_data.get("ConfederationIdentifier"),
            Dampening=json_data.get("Dampening"),
            DampeningMaxSuppressTime=json_data.get("DampeningMaxSuppressTime"),
            DampeningReachabilityHalfLife=json_data.get("DampeningReachabilityHalfLife"),
            DampeningReuse=json_data.get("DampeningReuse"),
            DampeningRouteMap=json_data.get("DampeningRouteMap"),
            DampeningSuppress=json_data.get("DampeningSuppress"),
            DampeningUnreachabilityHalfLife=json_data.get("DampeningUnreachabilityHalfLife"),
            DefaultLocalPreference=json_data.get("DefaultLocalPreference"),
            DeterministicMed=json_data.get("DeterministicMed"),
            DistanceExternal=json_data.get("DistanceExternal"),
            DistanceInternal=json_data.get("DistanceInternal"),
            DistanceLocal=json_data.get("DistanceLocal"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EbgpMultipath=json_data.get("EbgpMultipath"),
            EnforceFirstAs=json_data.get("EnforceFirstAs"),
            FastExternalFailover=json_data.get("FastExternalFailover"),
            GracefulEndOnTimer=json_data.get("GracefulEndOnTimer"),
            GracefulRestart=json_data.get("GracefulRestart"),
            GracefulRestartTime=json_data.get("GracefulRestartTime"),
            GracefulStalepathTime=json_data.get("GracefulStalepathTime"),
            GracefulUpdateDelay=json_data.get("GracefulUpdateDelay"),
            HoldtimeTimer=json_data.get("HoldtimeTimer"),
            IbgpMultipath=json_data.get("IbgpMultipath"),
            Id=json_data.get("Id"),
            IgnoreOptionalCapability=json_data.get("IgnoreOptionalCapability"),
            KeepaliveTimer=json_data.get("KeepaliveTimer"),
            LogNeighbourChanges=json_data.get("LogNeighbourChanges"),
            MultipathRecursiveDistance=json_data.get("MultipathRecursiveDistance"),
            NetworkImportCheck=json_data.get("NetworkImportCheck"),
            RecursiveNextHop=json_data.get("RecursiveNextHop"),
            RouterId=json_data.get("RouterId"),
            ScanTime=json_data.get("ScanTime"),
            Synchronization=json_data.get("Synchronization"),
            Vdomparam=json_data.get("Vdomparam"),
            AdminDistance=deserialize_list(json_data.get("AdminDistance"), AdminDistanceDefinition),
            AggregateAddress=deserialize_list(json_data.get("AggregateAddress"), AggregateAddressDefinition),
            AggregateAddress6=deserialize_list(json_data.get("AggregateAddress6"), AggregateAddress6Definition),
            ConfederationPeers=deserialize_list(json_data.get("ConfederationPeers"), ConfederationPeersDefinition),
            Neighbor=deserialize_list(json_data.get("Neighbor"), NeighborDefinition),
            NeighborGroup=deserialize_list(json_data.get("NeighborGroup"), NeighborGroupDefinition),
            NeighborRange=deserialize_list(json_data.get("NeighborRange"), NeighborRangeDefinition),
            NeighborRange6=deserialize_list(json_data.get("NeighborRange6"), NeighborRange6Definition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            Network6=deserialize_list(json_data.get("Network6"), Network6Definition),
            Redistribute=deserialize_list(json_data.get("Redistribute"), RedistributeDefinition),
            Redistribute6=deserialize_list(json_data.get("Redistribute6"), Redistribute6Definition),
            VrfLeak=deserialize_list(json_data.get("VrfLeak"), VrfLeakDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdminDistanceDefinition(BaseModel):
    Distance: Optional[float]
    Id: Optional[float]
    NeighbourPrefix: Optional[str]
    RouteList: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdminDistanceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdminDistanceDefinition"]:
        if not json_data:
            return None
        return cls(
            Distance=json_data.get("Distance"),
            Id=json_data.get("Id"),
            NeighbourPrefix=json_data.get("NeighbourPrefix"),
            RouteList=json_data.get("RouteList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdminDistanceDefinition = AdminDistanceDefinition


@dataclass
class AggregateAddressDefinition(BaseModel):
    AsSet: Optional[str]
    Id: Optional[float]
    Prefix: Optional[str]
    SummaryOnly: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AggregateAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggregateAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            AsSet=json_data.get("AsSet"),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
            SummaryOnly=json_data.get("SummaryOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggregateAddressDefinition = AggregateAddressDefinition


@dataclass
class AggregateAddress6Definition(BaseModel):
    AsSet: Optional[str]
    Id: Optional[float]
    Prefix6: Optional[str]
    SummaryOnly: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AggregateAddress6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggregateAddress6Definition"]:
        if not json_data:
            return None
        return cls(
            AsSet=json_data.get("AsSet"),
            Id=json_data.get("Id"),
            Prefix6=json_data.get("Prefix6"),
            SummaryOnly=json_data.get("SummaryOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggregateAddress6Definition = AggregateAddress6Definition


@dataclass
class ConfederationPeersDefinition(BaseModel):
    Peer: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfederationPeersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfederationPeersDefinition"]:
        if not json_data:
            return None
        return cls(
            Peer=json_data.get("Peer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfederationPeersDefinition = ConfederationPeersDefinition


@dataclass
class NeighborDefinition(BaseModel):
    Activate: Optional[str]
    Activate6: Optional[str]
    AdditionalPath: Optional[str]
    AdditionalPath6: Optional[str]
    AdvAdditionalPath: Optional[float]
    AdvAdditionalPath6: Optional[float]
    AdvertisementInterval: Optional[float]
    AllowasIn: Optional[float]
    AllowasIn6: Optional[float]
    AllowasInEnable: Optional[str]
    AllowasInEnable6: Optional[str]
    AsOverride: Optional[str]
    AsOverride6: Optional[str]
    AttributeUnchanged: Optional[str]
    AttributeUnchanged6: Optional[str]
    Bfd: Optional[str]
    CapabilityDefaultOriginate: Optional[str]
    CapabilityDefaultOriginate6: Optional[str]
    CapabilityDynamic: Optional[str]
    CapabilityGracefulRestart: Optional[str]
    CapabilityGracefulRestart6: Optional[str]
    CapabilityOrf: Optional[str]
    CapabilityOrf6: Optional[str]
    CapabilityRouteRefresh: Optional[str]
    ConnectTimer: Optional[float]
    DefaultOriginateRoutemap: Optional[str]
    DefaultOriginateRoutemap6: Optional[str]
    Description: Optional[str]
    DistributeListIn: Optional[str]
    DistributeListIn6: Optional[str]
    DistributeListOut: Optional[str]
    DistributeListOut6: Optional[str]
    DontCapabilityNegotiate: Optional[str]
    EbgpEnforceMultihop: Optional[str]
    EbgpMultihopTtl: Optional[float]
    FilterListIn: Optional[str]
    FilterListIn6: Optional[str]
    FilterListOut: Optional[str]
    FilterListOut6: Optional[str]
    HoldtimeTimer: Optional[float]
    Interface: Optional[str]
    Ip: Optional[str]
    KeepAliveTimer: Optional[float]
    LinkDownFailover: Optional[str]
    LocalAs: Optional[float]
    LocalAsNoPrepend: Optional[str]
    LocalAsReplaceAs: Optional[str]
    MaximumPrefix: Optional[float]
    MaximumPrefix6: Optional[float]
    MaximumPrefixThreshold: Optional[float]
    MaximumPrefixThreshold6: Optional[float]
    MaximumPrefixWarningOnly: Optional[str]
    MaximumPrefixWarningOnly6: Optional[str]
    NextHopSelf: Optional[str]
    NextHopSelf6: Optional[str]
    NextHopSelfRr: Optional[str]
    NextHopSelfRr6: Optional[str]
    OverrideCapability: Optional[str]
    Passive: Optional[str]
    Password: Optional[str]
    PrefixListIn: Optional[str]
    PrefixListIn6: Optional[str]
    PrefixListOut: Optional[str]
    PrefixListOut6: Optional[str]
    RemoteAs: Optional[float]
    RemovePrivateAs: Optional[str]
    RemovePrivateAs6: Optional[str]
    RestartTime: Optional[float]
    RetainStaleTime: Optional[float]
    RouteMapIn: Optional[str]
    RouteMapIn6: Optional[str]
    RouteMapOut: Optional[str]
    RouteMapOut6: Optional[str]
    RouteMapOut6Preferable: Optional[str]
    RouteMapOutPreferable: Optional[str]
    RouteReflectorClient: Optional[str]
    RouteReflectorClient6: Optional[str]
    RouteServerClient: Optional[str]
    RouteServerClient6: Optional[str]
    SendCommunity: Optional[str]
    SendCommunity6: Optional[str]
    Shutdown: Optional[str]
    SoftReconfiguration: Optional[str]
    SoftReconfiguration6: Optional[str]
    StaleRoute: Optional[str]
    StrictCapabilityMatch: Optional[str]
    UnsuppressMap: Optional[str]
    UnsuppressMap6: Optional[str]
    UpdateSource: Optional[str]
    Weight: Optional[float]
    ConditionalAdvertise: Optional[Sequence["_ConditionalAdvertiseDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NeighborDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NeighborDefinition"]:
        if not json_data:
            return None
        return cls(
            Activate=json_data.get("Activate"),
            Activate6=json_data.get("Activate6"),
            AdditionalPath=json_data.get("AdditionalPath"),
            AdditionalPath6=json_data.get("AdditionalPath6"),
            AdvAdditionalPath=json_data.get("AdvAdditionalPath"),
            AdvAdditionalPath6=json_data.get("AdvAdditionalPath6"),
            AdvertisementInterval=json_data.get("AdvertisementInterval"),
            AllowasIn=json_data.get("AllowasIn"),
            AllowasIn6=json_data.get("AllowasIn6"),
            AllowasInEnable=json_data.get("AllowasInEnable"),
            AllowasInEnable6=json_data.get("AllowasInEnable6"),
            AsOverride=json_data.get("AsOverride"),
            AsOverride6=json_data.get("AsOverride6"),
            AttributeUnchanged=json_data.get("AttributeUnchanged"),
            AttributeUnchanged6=json_data.get("AttributeUnchanged6"),
            Bfd=json_data.get("Bfd"),
            CapabilityDefaultOriginate=json_data.get("CapabilityDefaultOriginate"),
            CapabilityDefaultOriginate6=json_data.get("CapabilityDefaultOriginate6"),
            CapabilityDynamic=json_data.get("CapabilityDynamic"),
            CapabilityGracefulRestart=json_data.get("CapabilityGracefulRestart"),
            CapabilityGracefulRestart6=json_data.get("CapabilityGracefulRestart6"),
            CapabilityOrf=json_data.get("CapabilityOrf"),
            CapabilityOrf6=json_data.get("CapabilityOrf6"),
            CapabilityRouteRefresh=json_data.get("CapabilityRouteRefresh"),
            ConnectTimer=json_data.get("ConnectTimer"),
            DefaultOriginateRoutemap=json_data.get("DefaultOriginateRoutemap"),
            DefaultOriginateRoutemap6=json_data.get("DefaultOriginateRoutemap6"),
            Description=json_data.get("Description"),
            DistributeListIn=json_data.get("DistributeListIn"),
            DistributeListIn6=json_data.get("DistributeListIn6"),
            DistributeListOut=json_data.get("DistributeListOut"),
            DistributeListOut6=json_data.get("DistributeListOut6"),
            DontCapabilityNegotiate=json_data.get("DontCapabilityNegotiate"),
            EbgpEnforceMultihop=json_data.get("EbgpEnforceMultihop"),
            EbgpMultihopTtl=json_data.get("EbgpMultihopTtl"),
            FilterListIn=json_data.get("FilterListIn"),
            FilterListIn6=json_data.get("FilterListIn6"),
            FilterListOut=json_data.get("FilterListOut"),
            FilterListOut6=json_data.get("FilterListOut6"),
            HoldtimeTimer=json_data.get("HoldtimeTimer"),
            Interface=json_data.get("Interface"),
            Ip=json_data.get("Ip"),
            KeepAliveTimer=json_data.get("KeepAliveTimer"),
            LinkDownFailover=json_data.get("LinkDownFailover"),
            LocalAs=json_data.get("LocalAs"),
            LocalAsNoPrepend=json_data.get("LocalAsNoPrepend"),
            LocalAsReplaceAs=json_data.get("LocalAsReplaceAs"),
            MaximumPrefix=json_data.get("MaximumPrefix"),
            MaximumPrefix6=json_data.get("MaximumPrefix6"),
            MaximumPrefixThreshold=json_data.get("MaximumPrefixThreshold"),
            MaximumPrefixThreshold6=json_data.get("MaximumPrefixThreshold6"),
            MaximumPrefixWarningOnly=json_data.get("MaximumPrefixWarningOnly"),
            MaximumPrefixWarningOnly6=json_data.get("MaximumPrefixWarningOnly6"),
            NextHopSelf=json_data.get("NextHopSelf"),
            NextHopSelf6=json_data.get("NextHopSelf6"),
            NextHopSelfRr=json_data.get("NextHopSelfRr"),
            NextHopSelfRr6=json_data.get("NextHopSelfRr6"),
            OverrideCapability=json_data.get("OverrideCapability"),
            Passive=json_data.get("Passive"),
            Password=json_data.get("Password"),
            PrefixListIn=json_data.get("PrefixListIn"),
            PrefixListIn6=json_data.get("PrefixListIn6"),
            PrefixListOut=json_data.get("PrefixListOut"),
            PrefixListOut6=json_data.get("PrefixListOut6"),
            RemoteAs=json_data.get("RemoteAs"),
            RemovePrivateAs=json_data.get("RemovePrivateAs"),
            RemovePrivateAs6=json_data.get("RemovePrivateAs6"),
            RestartTime=json_data.get("RestartTime"),
            RetainStaleTime=json_data.get("RetainStaleTime"),
            RouteMapIn=json_data.get("RouteMapIn"),
            RouteMapIn6=json_data.get("RouteMapIn6"),
            RouteMapOut=json_data.get("RouteMapOut"),
            RouteMapOut6=json_data.get("RouteMapOut6"),
            RouteMapOut6Preferable=json_data.get("RouteMapOut6Preferable"),
            RouteMapOutPreferable=json_data.get("RouteMapOutPreferable"),
            RouteReflectorClient=json_data.get("RouteReflectorClient"),
            RouteReflectorClient6=json_data.get("RouteReflectorClient6"),
            RouteServerClient=json_data.get("RouteServerClient"),
            RouteServerClient6=json_data.get("RouteServerClient6"),
            SendCommunity=json_data.get("SendCommunity"),
            SendCommunity6=json_data.get("SendCommunity6"),
            Shutdown=json_data.get("Shutdown"),
            SoftReconfiguration=json_data.get("SoftReconfiguration"),
            SoftReconfiguration6=json_data.get("SoftReconfiguration6"),
            StaleRoute=json_data.get("StaleRoute"),
            StrictCapabilityMatch=json_data.get("StrictCapabilityMatch"),
            UnsuppressMap=json_data.get("UnsuppressMap"),
            UnsuppressMap6=json_data.get("UnsuppressMap6"),
            UpdateSource=json_data.get("UpdateSource"),
            Weight=json_data.get("Weight"),
            ConditionalAdvertise=deserialize_list(json_data.get("ConditionalAdvertise"), ConditionalAdvertiseDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NeighborDefinition = NeighborDefinition


@dataclass
class ConditionalAdvertiseDefinition(BaseModel):
    AdvertiseRoutemap: Optional[str]
    ConditionRoutemap: Optional[str]
    ConditionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionalAdvertiseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionalAdvertiseDefinition"]:
        if not json_data:
            return None
        return cls(
            AdvertiseRoutemap=json_data.get("AdvertiseRoutemap"),
            ConditionRoutemap=json_data.get("ConditionRoutemap"),
            ConditionType=json_data.get("ConditionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionalAdvertiseDefinition = ConditionalAdvertiseDefinition


@dataclass
class NeighborGroupDefinition(BaseModel):
    Activate: Optional[str]
    Activate6: Optional[str]
    AdditionalPath: Optional[str]
    AdditionalPath6: Optional[str]
    AdvAdditionalPath: Optional[float]
    AdvAdditionalPath6: Optional[float]
    AdvertisementInterval: Optional[float]
    AllowasIn: Optional[float]
    AllowasIn6: Optional[float]
    AllowasInEnable: Optional[str]
    AllowasInEnable6: Optional[str]
    AsOverride: Optional[str]
    AsOverride6: Optional[str]
    AttributeUnchanged: Optional[str]
    AttributeUnchanged6: Optional[str]
    Bfd: Optional[str]
    CapabilityDefaultOriginate: Optional[str]
    CapabilityDefaultOriginate6: Optional[str]
    CapabilityDynamic: Optional[str]
    CapabilityGracefulRestart: Optional[str]
    CapabilityGracefulRestart6: Optional[str]
    CapabilityOrf: Optional[str]
    CapabilityOrf6: Optional[str]
    CapabilityRouteRefresh: Optional[str]
    ConnectTimer: Optional[float]
    DefaultOriginateRoutemap: Optional[str]
    DefaultOriginateRoutemap6: Optional[str]
    Description: Optional[str]
    DistributeListIn: Optional[str]
    DistributeListIn6: Optional[str]
    DistributeListOut: Optional[str]
    DistributeListOut6: Optional[str]
    DontCapabilityNegotiate: Optional[str]
    EbgpEnforceMultihop: Optional[str]
    EbgpMultihopTtl: Optional[float]
    FilterListIn: Optional[str]
    FilterListIn6: Optional[str]
    FilterListOut: Optional[str]
    FilterListOut6: Optional[str]
    HoldtimeTimer: Optional[float]
    Interface: Optional[str]
    KeepAliveTimer: Optional[float]
    LinkDownFailover: Optional[str]
    LocalAs: Optional[float]
    LocalAsNoPrepend: Optional[str]
    LocalAsReplaceAs: Optional[str]
    MaximumPrefix: Optional[float]
    MaximumPrefix6: Optional[float]
    MaximumPrefixThreshold: Optional[float]
    MaximumPrefixThreshold6: Optional[float]
    MaximumPrefixWarningOnly: Optional[str]
    MaximumPrefixWarningOnly6: Optional[str]
    Name: Optional[str]
    NextHopSelf: Optional[str]
    NextHopSelf6: Optional[str]
    NextHopSelfRr: Optional[str]
    NextHopSelfRr6: Optional[str]
    OverrideCapability: Optional[str]
    Passive: Optional[str]
    PrefixListIn: Optional[str]
    PrefixListIn6: Optional[str]
    PrefixListOut: Optional[str]
    PrefixListOut6: Optional[str]
    RemoteAs: Optional[float]
    RemovePrivateAs: Optional[str]
    RemovePrivateAs6: Optional[str]
    RestartTime: Optional[float]
    RetainStaleTime: Optional[float]
    RouteMapIn: Optional[str]
    RouteMapIn6: Optional[str]
    RouteMapOut: Optional[str]
    RouteMapOut6: Optional[str]
    RouteMapOut6Preferable: Optional[str]
    RouteMapOutPreferable: Optional[str]
    RouteReflectorClient: Optional[str]
    RouteReflectorClient6: Optional[str]
    RouteServerClient: Optional[str]
    RouteServerClient6: Optional[str]
    SendCommunity: Optional[str]
    SendCommunity6: Optional[str]
    Shutdown: Optional[str]
    SoftReconfiguration: Optional[str]
    SoftReconfiguration6: Optional[str]
    StaleRoute: Optional[str]
    StrictCapabilityMatch: Optional[str]
    UnsuppressMap: Optional[str]
    UnsuppressMap6: Optional[str]
    UpdateSource: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NeighborGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NeighborGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Activate=json_data.get("Activate"),
            Activate6=json_data.get("Activate6"),
            AdditionalPath=json_data.get("AdditionalPath"),
            AdditionalPath6=json_data.get("AdditionalPath6"),
            AdvAdditionalPath=json_data.get("AdvAdditionalPath"),
            AdvAdditionalPath6=json_data.get("AdvAdditionalPath6"),
            AdvertisementInterval=json_data.get("AdvertisementInterval"),
            AllowasIn=json_data.get("AllowasIn"),
            AllowasIn6=json_data.get("AllowasIn6"),
            AllowasInEnable=json_data.get("AllowasInEnable"),
            AllowasInEnable6=json_data.get("AllowasInEnable6"),
            AsOverride=json_data.get("AsOverride"),
            AsOverride6=json_data.get("AsOverride6"),
            AttributeUnchanged=json_data.get("AttributeUnchanged"),
            AttributeUnchanged6=json_data.get("AttributeUnchanged6"),
            Bfd=json_data.get("Bfd"),
            CapabilityDefaultOriginate=json_data.get("CapabilityDefaultOriginate"),
            CapabilityDefaultOriginate6=json_data.get("CapabilityDefaultOriginate6"),
            CapabilityDynamic=json_data.get("CapabilityDynamic"),
            CapabilityGracefulRestart=json_data.get("CapabilityGracefulRestart"),
            CapabilityGracefulRestart6=json_data.get("CapabilityGracefulRestart6"),
            CapabilityOrf=json_data.get("CapabilityOrf"),
            CapabilityOrf6=json_data.get("CapabilityOrf6"),
            CapabilityRouteRefresh=json_data.get("CapabilityRouteRefresh"),
            ConnectTimer=json_data.get("ConnectTimer"),
            DefaultOriginateRoutemap=json_data.get("DefaultOriginateRoutemap"),
            DefaultOriginateRoutemap6=json_data.get("DefaultOriginateRoutemap6"),
            Description=json_data.get("Description"),
            DistributeListIn=json_data.get("DistributeListIn"),
            DistributeListIn6=json_data.get("DistributeListIn6"),
            DistributeListOut=json_data.get("DistributeListOut"),
            DistributeListOut6=json_data.get("DistributeListOut6"),
            DontCapabilityNegotiate=json_data.get("DontCapabilityNegotiate"),
            EbgpEnforceMultihop=json_data.get("EbgpEnforceMultihop"),
            EbgpMultihopTtl=json_data.get("EbgpMultihopTtl"),
            FilterListIn=json_data.get("FilterListIn"),
            FilterListIn6=json_data.get("FilterListIn6"),
            FilterListOut=json_data.get("FilterListOut"),
            FilterListOut6=json_data.get("FilterListOut6"),
            HoldtimeTimer=json_data.get("HoldtimeTimer"),
            Interface=json_data.get("Interface"),
            KeepAliveTimer=json_data.get("KeepAliveTimer"),
            LinkDownFailover=json_data.get("LinkDownFailover"),
            LocalAs=json_data.get("LocalAs"),
            LocalAsNoPrepend=json_data.get("LocalAsNoPrepend"),
            LocalAsReplaceAs=json_data.get("LocalAsReplaceAs"),
            MaximumPrefix=json_data.get("MaximumPrefix"),
            MaximumPrefix6=json_data.get("MaximumPrefix6"),
            MaximumPrefixThreshold=json_data.get("MaximumPrefixThreshold"),
            MaximumPrefixThreshold6=json_data.get("MaximumPrefixThreshold6"),
            MaximumPrefixWarningOnly=json_data.get("MaximumPrefixWarningOnly"),
            MaximumPrefixWarningOnly6=json_data.get("MaximumPrefixWarningOnly6"),
            Name=json_data.get("Name"),
            NextHopSelf=json_data.get("NextHopSelf"),
            NextHopSelf6=json_data.get("NextHopSelf6"),
            NextHopSelfRr=json_data.get("NextHopSelfRr"),
            NextHopSelfRr6=json_data.get("NextHopSelfRr6"),
            OverrideCapability=json_data.get("OverrideCapability"),
            Passive=json_data.get("Passive"),
            PrefixListIn=json_data.get("PrefixListIn"),
            PrefixListIn6=json_data.get("PrefixListIn6"),
            PrefixListOut=json_data.get("PrefixListOut"),
            PrefixListOut6=json_data.get("PrefixListOut6"),
            RemoteAs=json_data.get("RemoteAs"),
            RemovePrivateAs=json_data.get("RemovePrivateAs"),
            RemovePrivateAs6=json_data.get("RemovePrivateAs6"),
            RestartTime=json_data.get("RestartTime"),
            RetainStaleTime=json_data.get("RetainStaleTime"),
            RouteMapIn=json_data.get("RouteMapIn"),
            RouteMapIn6=json_data.get("RouteMapIn6"),
            RouteMapOut=json_data.get("RouteMapOut"),
            RouteMapOut6=json_data.get("RouteMapOut6"),
            RouteMapOut6Preferable=json_data.get("RouteMapOut6Preferable"),
            RouteMapOutPreferable=json_data.get("RouteMapOutPreferable"),
            RouteReflectorClient=json_data.get("RouteReflectorClient"),
            RouteReflectorClient6=json_data.get("RouteReflectorClient6"),
            RouteServerClient=json_data.get("RouteServerClient"),
            RouteServerClient6=json_data.get("RouteServerClient6"),
            SendCommunity=json_data.get("SendCommunity"),
            SendCommunity6=json_data.get("SendCommunity6"),
            Shutdown=json_data.get("Shutdown"),
            SoftReconfiguration=json_data.get("SoftReconfiguration"),
            SoftReconfiguration6=json_data.get("SoftReconfiguration6"),
            StaleRoute=json_data.get("StaleRoute"),
            StrictCapabilityMatch=json_data.get("StrictCapabilityMatch"),
            UnsuppressMap=json_data.get("UnsuppressMap"),
            UnsuppressMap6=json_data.get("UnsuppressMap6"),
            UpdateSource=json_data.get("UpdateSource"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NeighborGroupDefinition = NeighborGroupDefinition


@dataclass
class NeighborRangeDefinition(BaseModel):
    Id: Optional[float]
    MaxNeighborNum: Optional[float]
    NeighborGroup: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NeighborRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NeighborRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            MaxNeighborNum=json_data.get("MaxNeighborNum"),
            NeighborGroup=json_data.get("NeighborGroup"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NeighborRangeDefinition = NeighborRangeDefinition


@dataclass
class NeighborRange6Definition(BaseModel):
    Id: Optional[float]
    MaxNeighborNum: Optional[float]
    NeighborGroup: Optional[str]
    Prefix6: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NeighborRange6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NeighborRange6Definition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            MaxNeighborNum=json_data.get("MaxNeighborNum"),
            NeighborGroup=json_data.get("NeighborGroup"),
            Prefix6=json_data.get("Prefix6"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NeighborRange6Definition = NeighborRange6Definition


@dataclass
class NetworkDefinition(BaseModel):
    Backdoor: Optional[str]
    Id: Optional[float]
    Prefix: Optional[str]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Backdoor=json_data.get("Backdoor"),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class Network6Definition(BaseModel):
    Backdoor: Optional[str]
    Id: Optional[float]
    Prefix6: Optional[str]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Network6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Network6Definition"]:
        if not json_data:
            return None
        return cls(
            Backdoor=json_data.get("Backdoor"),
            Id=json_data.get("Id"),
            Prefix6=json_data.get("Prefix6"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Network6Definition = Network6Definition


@dataclass
class RedistributeDefinition(BaseModel):
    Name: Optional[str]
    RouteMap: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedistributeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedistributeDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            RouteMap=json_data.get("RouteMap"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedistributeDefinition = RedistributeDefinition


@dataclass
class Redistribute6Definition(BaseModel):
    Name: Optional[str]
    RouteMap: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Redistribute6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Redistribute6Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            RouteMap=json_data.get("RouteMap"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Redistribute6Definition = Redistribute6Definition


@dataclass
class VrfLeakDefinition(BaseModel):
    Vrf: Optional[str]
    Target: Optional[Sequence["_TargetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VrfLeakDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VrfLeakDefinition"]:
        if not json_data:
            return None
        return cls(
            Vrf=json_data.get("Vrf"),
            Target=deserialize_list(json_data.get("Target"), TargetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VrfLeakDefinition = VrfLeakDefinition


@dataclass
class TargetDefinition(BaseModel):
    Interface: Optional[str]
    RouteMap: Optional[str]
    Vrf: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetDefinition"]:
        if not json_data:
            return None
        return cls(
            Interface=json_data.get("Interface"),
            RouteMap=json_data.get("RouteMap"),
            Vrf=json_data.get("Vrf"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetDefinition = TargetDefinition


