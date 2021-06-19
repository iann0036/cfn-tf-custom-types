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
    Arn: Optional[str]
    CreatedDate: Optional[str]
    Id: Optional[str]
    LastUpdatedDate: Optional[str]
    MeshName: Optional[str]
    MeshOwner: Optional[str]
    Name: Optional[str]
    ResourceOwner: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    VirtualRouterName: Optional[str]
    Spec: Optional[Sequence["_SpecDefinition"]]

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
            Arn=json_data.get("Arn"),
            CreatedDate=json_data.get("CreatedDate"),
            Id=json_data.get("Id"),
            LastUpdatedDate=json_data.get("LastUpdatedDate"),
            MeshName=json_data.get("MeshName"),
            MeshOwner=json_data.get("MeshOwner"),
            Name=json_data.get("Name"),
            ResourceOwner=json_data.get("ResourceOwner"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            VirtualRouterName=json_data.get("VirtualRouterName"),
            Spec=deserialize_list(json_data.get("Spec"), SpecDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class SpecDefinition(BaseModel):
    Priority: Optional[float]
    GrpcRoute: Optional[Sequence["_GrpcRouteDefinition"]]
    Http2Route: Optional[Sequence["_Http2RouteDefinition"]]
    HttpRoute: Optional[Sequence["_HttpRouteDefinition"]]
    TcpRoute: Optional[Sequence["_TcpRouteDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecDefinition"]:
        if not json_data:
            return None
        return cls(
            Priority=json_data.get("Priority"),
            GrpcRoute=deserialize_list(json_data.get("GrpcRoute"), GrpcRouteDefinition),
            Http2Route=deserialize_list(json_data.get("Http2Route"), Http2RouteDefinition),
            HttpRoute=deserialize_list(json_data.get("HttpRoute"), HttpRouteDefinition),
            TcpRoute=deserialize_list(json_data.get("TcpRoute"), TcpRouteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecDefinition = SpecDefinition


@dataclass
class GrpcRouteDefinition(BaseModel):
    Action: Optional[Sequence["_ActionDefinition"]]
    Match: Optional[Sequence["_MatchDefinition"]]
    RetryPolicy: Optional[Sequence["_RetryPolicyDefinition"]]
    Timeout: Optional[Sequence["_TimeoutDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GrpcRouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrpcRouteDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
            RetryPolicy=deserialize_list(json_data.get("RetryPolicy"), RetryPolicyDefinition),
            Timeout=deserialize_list(json_data.get("Timeout"), TimeoutDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrpcRouteDefinition = GrpcRouteDefinition


@dataclass
class ActionDefinition(BaseModel):
    WeightedTarget: Optional[Sequence["_WeightedTargetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            WeightedTarget=deserialize_list(json_data.get("WeightedTarget"), WeightedTargetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class WeightedTargetDefinition(BaseModel):
    VirtualNode: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WeightedTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeightedTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            VirtualNode=json_data.get("VirtualNode"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeightedTargetDefinition = WeightedTargetDefinition


@dataclass
class MatchDefinition(BaseModel):
    Exact: Optional[str]
    Prefix: Optional[str]
    Regex: Optional[str]
    Suffix: Optional[str]
    Range: Optional[Sequence["_RangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Exact=json_data.get("Exact"),
            Prefix=json_data.get("Prefix"),
            Regex=json_data.get("Regex"),
            Suffix=json_data.get("Suffix"),
            Range=deserialize_list(json_data.get("Range"), RangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class RangeDefinition(BaseModel):
    End: Optional[float]
    Start: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangeDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangeDefinition = RangeDefinition


@dataclass
class RetryPolicyDefinition(BaseModel):
    HttpRetryEvents: Optional[Sequence[str]]
    MaxRetries: Optional[float]
    TcpRetryEvents: Optional[Sequence[str]]
    PerRetryTimeout: Optional[Sequence["_PerRetryTimeoutDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RetryPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            HttpRetryEvents=json_data.get("HttpRetryEvents"),
            MaxRetries=json_data.get("MaxRetries"),
            TcpRetryEvents=json_data.get("TcpRetryEvents"),
            PerRetryTimeout=deserialize_list(json_data.get("PerRetryTimeout"), PerRetryTimeoutDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryPolicyDefinition = RetryPolicyDefinition


@dataclass
class PerRetryTimeoutDefinition(BaseModel):
    Unit: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PerRetryTimeoutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PerRetryTimeoutDefinition"]:
        if not json_data:
            return None
        return cls(
            Unit=json_data.get("Unit"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PerRetryTimeoutDefinition = PerRetryTimeoutDefinition


@dataclass
class TimeoutDefinition(BaseModel):
    Idle: Optional[Sequence["_IdleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutDefinition"]:
        if not json_data:
            return None
        return cls(
            Idle=deserialize_list(json_data.get("Idle"), IdleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutDefinition = TimeoutDefinition


@dataclass
class IdleDefinition(BaseModel):
    Unit: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IdleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdleDefinition"]:
        if not json_data:
            return None
        return cls(
            Unit=json_data.get("Unit"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdleDefinition = IdleDefinition


@dataclass
class Http2RouteDefinition(BaseModel):
    Action: Optional[Sequence["_ActionDefinition"]]
    Match: Optional[Sequence["_MatchDefinition"]]
    RetryPolicy: Optional[Sequence["_RetryPolicyDefinition"]]
    Timeout: Optional[Sequence["_TimeoutDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Http2RouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Http2RouteDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
            RetryPolicy=deserialize_list(json_data.get("RetryPolicy"), RetryPolicyDefinition),
            Timeout=deserialize_list(json_data.get("Timeout"), TimeoutDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Http2RouteDefinition = Http2RouteDefinition


@dataclass
class HttpRouteDefinition(BaseModel):
    Action: Optional[Sequence["_ActionDefinition"]]
    Match: Optional[Sequence["_MatchDefinition"]]
    RetryPolicy: Optional[Sequence["_RetryPolicyDefinition"]]
    Timeout: Optional[Sequence["_TimeoutDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpRouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpRouteDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
            RetryPolicy=deserialize_list(json_data.get("RetryPolicy"), RetryPolicyDefinition),
            Timeout=deserialize_list(json_data.get("Timeout"), TimeoutDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpRouteDefinition = HttpRouteDefinition


@dataclass
class TcpRouteDefinition(BaseModel):
    Action: Optional[Sequence["_ActionDefinition"]]
    Timeout: Optional[Sequence["_TimeoutDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TcpRouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpRouteDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            Timeout=deserialize_list(json_data.get("Timeout"), TimeoutDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpRouteDefinition = TcpRouteDefinition


