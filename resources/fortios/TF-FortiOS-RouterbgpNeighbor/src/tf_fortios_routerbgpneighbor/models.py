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
    DynamicSortSubtable: Optional[str]
    EbgpEnforceMultihop: Optional[str]
    EbgpMultihopTtl: Optional[float]
    FilterListIn: Optional[str]
    FilterListIn6: Optional[str]
    FilterListOut: Optional[str]
    FilterListOut6: Optional[str]
    HoldtimeTimer: Optional[float]
    Id: Optional[str]
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
    Vdomparam: Optional[str]
    Weight: Optional[float]
    ConditionalAdvertise: Optional[Sequence["_ConditionalAdvertiseDefinition"]]

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
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EbgpEnforceMultihop=json_data.get("EbgpEnforceMultihop"),
            EbgpMultihopTtl=json_data.get("EbgpMultihopTtl"),
            FilterListIn=json_data.get("FilterListIn"),
            FilterListIn6=json_data.get("FilterListIn6"),
            FilterListOut=json_data.get("FilterListOut"),
            FilterListOut6=json_data.get("FilterListOut6"),
            HoldtimeTimer=json_data.get("HoldtimeTimer"),
            Id=json_data.get("Id"),
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
            Vdomparam=json_data.get("Vdomparam"),
            Weight=json_data.get("Weight"),
            ConditionalAdvertise=deserialize_list(json_data.get("ConditionalAdvertise"), ConditionalAdvertiseDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


