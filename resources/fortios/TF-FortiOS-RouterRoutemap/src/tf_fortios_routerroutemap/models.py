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
    Comments: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Vdomparam: Optional[str]
    Rule: Optional[Sequence["_RuleDefinition"]]

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
            Comments=json_data.get("Comments"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RuleDefinition(BaseModel):
    Action: Optional[str]
    Id: Optional[float]
    MatchAsPath: Optional[str]
    MatchCommunity: Optional[str]
    MatchCommunityExact: Optional[str]
    MatchFlags: Optional[float]
    MatchInterface: Optional[str]
    MatchIp6Address: Optional[str]
    MatchIp6Nexthop: Optional[str]
    MatchIpAddress: Optional[str]
    MatchIpNexthop: Optional[str]
    MatchMetric: Optional[float]
    MatchOrigin: Optional[str]
    MatchRouteType: Optional[str]
    MatchTag: Optional[float]
    MatchVrf: Optional[float]
    SetAggregatorAs: Optional[float]
    SetAggregatorIp: Optional[str]
    SetAspathAction: Optional[str]
    SetAtomicAggregate: Optional[str]
    SetCommunityAdditive: Optional[str]
    SetCommunityDelete: Optional[str]
    SetDampeningMaxSuppress: Optional[float]
    SetDampeningReachabilityHalfLife: Optional[float]
    SetDampeningReuse: Optional[float]
    SetDampeningSuppress: Optional[float]
    SetDampeningUnreachabilityHalfLife: Optional[float]
    SetFlags: Optional[float]
    SetIp6Nexthop: Optional[str]
    SetIp6NexthopLocal: Optional[str]
    SetIpNexthop: Optional[str]
    SetLocalPreference: Optional[float]
    SetMetric: Optional[float]
    SetMetricType: Optional[str]
    SetOrigin: Optional[str]
    SetOriginatorId: Optional[str]
    SetRouteTag: Optional[float]
    SetTag: Optional[float]
    SetWeight: Optional[float]
    SetAspath: Optional[Sequence["_SetAspathDefinition"]]
    SetCommunity: Optional[Sequence["_SetCommunityDefinition"]]
    SetExtcommunityRt: Optional[Sequence["_SetExtcommunityRtDefinition"]]
    SetExtcommunitySoo: Optional[Sequence["_SetExtcommunitySooDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Id=json_data.get("Id"),
            MatchAsPath=json_data.get("MatchAsPath"),
            MatchCommunity=json_data.get("MatchCommunity"),
            MatchCommunityExact=json_data.get("MatchCommunityExact"),
            MatchFlags=json_data.get("MatchFlags"),
            MatchInterface=json_data.get("MatchInterface"),
            MatchIp6Address=json_data.get("MatchIp6Address"),
            MatchIp6Nexthop=json_data.get("MatchIp6Nexthop"),
            MatchIpAddress=json_data.get("MatchIpAddress"),
            MatchIpNexthop=json_data.get("MatchIpNexthop"),
            MatchMetric=json_data.get("MatchMetric"),
            MatchOrigin=json_data.get("MatchOrigin"),
            MatchRouteType=json_data.get("MatchRouteType"),
            MatchTag=json_data.get("MatchTag"),
            MatchVrf=json_data.get("MatchVrf"),
            SetAggregatorAs=json_data.get("SetAggregatorAs"),
            SetAggregatorIp=json_data.get("SetAggregatorIp"),
            SetAspathAction=json_data.get("SetAspathAction"),
            SetAtomicAggregate=json_data.get("SetAtomicAggregate"),
            SetCommunityAdditive=json_data.get("SetCommunityAdditive"),
            SetCommunityDelete=json_data.get("SetCommunityDelete"),
            SetDampeningMaxSuppress=json_data.get("SetDampeningMaxSuppress"),
            SetDampeningReachabilityHalfLife=json_data.get("SetDampeningReachabilityHalfLife"),
            SetDampeningReuse=json_data.get("SetDampeningReuse"),
            SetDampeningSuppress=json_data.get("SetDampeningSuppress"),
            SetDampeningUnreachabilityHalfLife=json_data.get("SetDampeningUnreachabilityHalfLife"),
            SetFlags=json_data.get("SetFlags"),
            SetIp6Nexthop=json_data.get("SetIp6Nexthop"),
            SetIp6NexthopLocal=json_data.get("SetIp6NexthopLocal"),
            SetIpNexthop=json_data.get("SetIpNexthop"),
            SetLocalPreference=json_data.get("SetLocalPreference"),
            SetMetric=json_data.get("SetMetric"),
            SetMetricType=json_data.get("SetMetricType"),
            SetOrigin=json_data.get("SetOrigin"),
            SetOriginatorId=json_data.get("SetOriginatorId"),
            SetRouteTag=json_data.get("SetRouteTag"),
            SetTag=json_data.get("SetTag"),
            SetWeight=json_data.get("SetWeight"),
            SetAspath=deserialize_list(json_data.get("SetAspath"), SetAspathDefinition),
            SetCommunity=deserialize_list(json_data.get("SetCommunity"), SetCommunityDefinition),
            SetExtcommunityRt=deserialize_list(json_data.get("SetExtcommunityRt"), SetExtcommunityRtDefinition),
            SetExtcommunitySoo=deserialize_list(json_data.get("SetExtcommunitySoo"), SetExtcommunitySooDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class SetAspathDefinition(BaseModel):
    As: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SetAspathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetAspathDefinition"]:
        if not json_data:
            return None
        return cls(
            As=json_data.get("As"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetAspathDefinition = SetAspathDefinition


@dataclass
class SetCommunityDefinition(BaseModel):
    Community: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SetCommunityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetCommunityDefinition"]:
        if not json_data:
            return None
        return cls(
            Community=json_data.get("Community"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetCommunityDefinition = SetCommunityDefinition


@dataclass
class SetExtcommunityRtDefinition(BaseModel):
    Community: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SetExtcommunityRtDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetExtcommunityRtDefinition"]:
        if not json_data:
            return None
        return cls(
            Community=json_data.get("Community"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetExtcommunityRtDefinition = SetExtcommunityRtDefinition


@dataclass
class SetExtcommunitySooDefinition(BaseModel):
    Community: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SetExtcommunitySooDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetExtcommunitySooDefinition"]:
        if not json_data:
            return None
        return cls(
            Community=json_data.get("Community"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetExtcommunitySooDefinition = SetExtcommunitySooDefinition


