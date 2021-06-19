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
    Ecmp: Optional[bool]
    Enabled: Optional[bool]
    GatewayId: Optional[str]
    GatewayPath: Optional[str]
    GracefulRestartMode: Optional[str]
    GracefulRestartStaleRouteTimer: Optional[float]
    GracefulRestartTimer: Optional[float]
    Id: Optional[str]
    InterSrIbgp: Optional[bool]
    LocalAsNum: Optional[str]
    LocaleServiceId: Optional[str]
    MultipathRelax: Optional[bool]
    Path: Optional[str]
    Revision: Optional[float]
    SitePath: Optional[str]
    RouteAggregation: Optional[Sequence["_RouteAggregationDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

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
            Ecmp=json_data.get("Ecmp"),
            Enabled=json_data.get("Enabled"),
            GatewayId=json_data.get("GatewayId"),
            GatewayPath=json_data.get("GatewayPath"),
            GracefulRestartMode=json_data.get("GracefulRestartMode"),
            GracefulRestartStaleRouteTimer=json_data.get("GracefulRestartStaleRouteTimer"),
            GracefulRestartTimer=json_data.get("GracefulRestartTimer"),
            Id=json_data.get("Id"),
            InterSrIbgp=json_data.get("InterSrIbgp"),
            LocalAsNum=json_data.get("LocalAsNum"),
            LocaleServiceId=json_data.get("LocaleServiceId"),
            MultipathRelax=json_data.get("MultipathRelax"),
            Path=json_data.get("Path"),
            Revision=json_data.get("Revision"),
            SitePath=json_data.get("SitePath"),
            RouteAggregation=deserialize_list(json_data.get("RouteAggregation"), RouteAggregationDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RouteAggregationDefinition(BaseModel):
    Prefix: Optional[str]
    SummaryOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RouteAggregationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteAggregationDefinition"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            SummaryOnly=json_data.get("SummaryOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteAggregationDefinition = RouteAggregationDefinition


@dataclass
class TagDefinition(BaseModel):
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


