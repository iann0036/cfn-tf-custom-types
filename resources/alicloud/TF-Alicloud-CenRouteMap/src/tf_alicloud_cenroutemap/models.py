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
    AsPathMatchMode: Optional[str]
    CenId: Optional[str]
    CenRegionId: Optional[str]
    CidrMatchMode: Optional[str]
    CommunityMatchMode: Optional[str]
    CommunityOperateMode: Optional[str]
    Description: Optional[str]
    DestinationChildInstanceTypes: Optional[Sequence[str]]
    DestinationCidrBlocks: Optional[Sequence[str]]
    DestinationInstanceIds: Optional[Sequence[str]]
    DestinationInstanceIdsReverseMatch: Optional[bool]
    DestinationRouteTableIds: Optional[Sequence[str]]
    Id: Optional[str]
    MapResult: Optional[str]
    MatchAsns: Optional[Sequence[str]]
    MatchCommunitySet: Optional[Sequence[str]]
    NextPriority: Optional[float]
    OperateCommunitySet: Optional[Sequence[str]]
    Preference: Optional[float]
    PrependAsPath: Optional[Sequence[str]]
    Priority: Optional[float]
    RouteMapId: Optional[str]
    RouteTypes: Optional[Sequence[str]]
    SourceChildInstanceTypes: Optional[Sequence[str]]
    SourceInstanceIds: Optional[Sequence[str]]
    SourceInstanceIdsReverseMatch: Optional[bool]
    SourceRegionIds: Optional[Sequence[str]]
    SourceRouteTableIds: Optional[Sequence[str]]
    Status: Optional[str]
    TransmitDirection: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AsPathMatchMode=json_data.get("AsPathMatchMode"),
            CenId=json_data.get("CenId"),
            CenRegionId=json_data.get("CenRegionId"),
            CidrMatchMode=json_data.get("CidrMatchMode"),
            CommunityMatchMode=json_data.get("CommunityMatchMode"),
            CommunityOperateMode=json_data.get("CommunityOperateMode"),
            Description=json_data.get("Description"),
            DestinationChildInstanceTypes=json_data.get("DestinationChildInstanceTypes"),
            DestinationCidrBlocks=json_data.get("DestinationCidrBlocks"),
            DestinationInstanceIds=json_data.get("DestinationInstanceIds"),
            DestinationInstanceIdsReverseMatch=json_data.get("DestinationInstanceIdsReverseMatch"),
            DestinationRouteTableIds=json_data.get("DestinationRouteTableIds"),
            Id=json_data.get("Id"),
            MapResult=json_data.get("MapResult"),
            MatchAsns=json_data.get("MatchAsns"),
            MatchCommunitySet=json_data.get("MatchCommunitySet"),
            NextPriority=json_data.get("NextPriority"),
            OperateCommunitySet=json_data.get("OperateCommunitySet"),
            Preference=json_data.get("Preference"),
            PrependAsPath=json_data.get("PrependAsPath"),
            Priority=json_data.get("Priority"),
            RouteMapId=json_data.get("RouteMapId"),
            RouteTypes=json_data.get("RouteTypes"),
            SourceChildInstanceTypes=json_data.get("SourceChildInstanceTypes"),
            SourceInstanceIds=json_data.get("SourceInstanceIds"),
            SourceInstanceIdsReverseMatch=json_data.get("SourceInstanceIdsReverseMatch"),
            SourceRegionIds=json_data.get("SourceRegionIds"),
            SourceRouteTableIds=json_data.get("SourceRouteTableIds"),
            Status=json_data.get("Status"),
            TransmitDirection=json_data.get("TransmitDirection"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


