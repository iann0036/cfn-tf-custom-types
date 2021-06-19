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
    BypassUrlPatterns: Optional[Sequence[str]]
    Description: Optional[str]
    Disabled: Optional[bool]
    Id: Optional[str]
    Period: Optional[float]
    Threshold: Optional[float]
    ZoneId: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    Correlate: Optional[Sequence["_CorrelateDefinition"]]
    Match: Optional[Sequence["_MatchDefinition"]]

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
            BypassUrlPatterns=json_data.get("BypassUrlPatterns"),
            Description=json_data.get("Description"),
            Disabled=json_data.get("Disabled"),
            Id=json_data.get("Id"),
            Period=json_data.get("Period"),
            Threshold=json_data.get("Threshold"),
            ZoneId=json_data.get("ZoneId"),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            Correlate=deserialize_list(json_data.get("Correlate"), CorrelateDefinition),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ActionDefinition(BaseModel):
    Mode: Optional[str]
    Timeout: Optional[float]
    Response: Optional[Sequence["_ResponseDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            Timeout=json_data.get("Timeout"),
            Response=deserialize_list(json_data.get("Response"), ResponseDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class ResponseDefinition(BaseModel):
    Headers: Optional[Sequence[Sequence["_HeadersDefinition"]]]
    OriginTraffic: Optional[bool]
    Statuses: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), <ResolvedType(ContainerType.MODEL, HeadersDefinition)>),
            OriginTraffic=json_data.get("OriginTraffic"),
            Statuses=json_data.get("Statuses"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseDefinition = ResponseDefinition


@dataclass
class HeadersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


@dataclass
class CorrelateDefinition(BaseModel):
    By: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CorrelateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorrelateDefinition"]:
        if not json_data:
            return None
        return cls(
            By=json_data.get("By"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorrelateDefinition = CorrelateDefinition


@dataclass
class MatchDefinition(BaseModel):
    Request: Optional[Sequence["_RequestDefinition"]]
    Response: Optional[Sequence["_ResponseDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Request=deserialize_list(json_data.get("Request"), RequestDefinition),
            Response=deserialize_list(json_data.get("Response"), ResponseDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class RequestDefinition(BaseModel):
    Methods: Optional[Sequence[str]]
    Schemes: Optional[Sequence[str]]
    UrlPattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestDefinition"]:
        if not json_data:
            return None
        return cls(
            Methods=json_data.get("Methods"),
            Schemes=json_data.get("Schemes"),
            UrlPattern=json_data.get("UrlPattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestDefinition = RequestDefinition


