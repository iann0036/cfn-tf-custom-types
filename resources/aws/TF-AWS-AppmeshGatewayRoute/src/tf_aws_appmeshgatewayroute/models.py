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
    VirtualGatewayName: Optional[str]
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
            VirtualGatewayName=json_data.get("VirtualGatewayName"),
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
    GrpcRoute: Optional[Sequence["_GrpcRouteDefinition"]]
    Http2Route: Optional[Sequence["_Http2RouteDefinition"]]
    HttpRoute: Optional[Sequence["_HttpRouteDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecDefinition"]:
        if not json_data:
            return None
        return cls(
            GrpcRoute=deserialize_list(json_data.get("GrpcRoute"), GrpcRouteDefinition),
            Http2Route=deserialize_list(json_data.get("Http2Route"), Http2RouteDefinition),
            HttpRoute=deserialize_list(json_data.get("HttpRoute"), HttpRouteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecDefinition = SpecDefinition


@dataclass
class GrpcRouteDefinition(BaseModel):
    Action: Optional[Sequence["_ActionDefinition"]]
    Match: Optional[Sequence["_MatchDefinition"]]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_GrpcRouteDefinition = GrpcRouteDefinition


@dataclass
class ActionDefinition(BaseModel):
    Target: Optional[Sequence["_TargetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Target=deserialize_list(json_data.get("Target"), TargetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class TargetDefinition(BaseModel):
    VirtualService: Optional[Sequence["_VirtualServiceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetDefinition"]:
        if not json_data:
            return None
        return cls(
            VirtualService=deserialize_list(json_data.get("VirtualService"), VirtualServiceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetDefinition = TargetDefinition


@dataclass
class VirtualServiceDefinition(BaseModel):
    VirtualServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            VirtualServiceName=json_data.get("VirtualServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualServiceDefinition = VirtualServiceDefinition


@dataclass
class MatchDefinition(BaseModel):
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class Http2RouteDefinition(BaseModel):
    Action: Optional[Sequence["_ActionDefinition"]]
    Match: Optional[Sequence["_MatchDefinition"]]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Http2RouteDefinition = Http2RouteDefinition


@dataclass
class HttpRouteDefinition(BaseModel):
    Action: Optional[Sequence["_ActionDefinition"]]
    Match: Optional[Sequence["_MatchDefinition"]]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpRouteDefinition = HttpRouteDefinition


