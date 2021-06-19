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
    Activate: Optional[float]
    AllowasIn: Optional[float]
    AllowasInCount: Optional[float]
    AsNumber: Optional[float]
    DefaultOriginate: Optional[float]
    Id: Optional[str]
    Inbound: Optional[float]
    MaximumPrefix: Optional[float]
    MaximumPrefixThres: Optional[float]
    NextHopSelf: Optional[float]
    PeerGroup: Optional[str]
    PrefixListDirection: Optional[str]
    ProcessId: Optional[str]
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
            AllowasIn=json_data.get("AllowasIn"),
            AllowasInCount=json_data.get("AllowasInCount"),
            AsNumber=json_data.get("AsNumber"),
            DefaultOriginate=json_data.get("DefaultOriginate"),
            Id=json_data.get("Id"),
            Inbound=json_data.get("Inbound"),
            MaximumPrefix=json_data.get("MaximumPrefix"),
            MaximumPrefixThres=json_data.get("MaximumPrefixThres"),
            NextHopSelf=json_data.get("NextHopSelf"),
            PeerGroup=json_data.get("PeerGroup"),
            PrefixListDirection=json_data.get("PrefixListDirection"),
            ProcessId=json_data.get("ProcessId"),
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


