# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    BypassUrlPatterns: Optional[Sequence[str]]
    Description: Optional[str]
    Disabled: Optional[bool]
    Period: Optional[float]
    Threshold: Optional[float]
    ZoneId: Optional[str]
    Action: Optional[Sequence["_Action"]]
    Correlate: Optional[Sequence["_Correlate"]]
    Match: Optional[Sequence["_Match"]]
    Response: Optional[Sequence["_Response"]]
    Request: Optional[Sequence["_Request"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BypassUrlPatterns=json_data.get("BypassUrlPatterns"),
            Description=json_data.get("Description"),
            Disabled=json_data.get("Disabled"),
            Period=json_data.get("Period"),
            Threshold=json_data.get("Threshold"),
            ZoneId=json_data.get("ZoneId"),
            Action=json_data.get("Action"),
            Correlate=json_data.get("Correlate"),
            Match=json_data.get("Match"),
            Response=json_data.get("Response"),
            Request=json_data.get("Request"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Action:
    Mode: Optional[str]
    Timeout: Optional[float]
    Response: Optional[Sequence["_Response"]]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            Timeout=json_data.get("Timeout"),
            Response=json_data.get("Response"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class Response:
    OriginTraffic: Optional[bool]
    Statuses: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_Response"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Response"]:
        if not json_data:
            return None
        return cls(
            OriginTraffic=json_data.get("OriginTraffic"),
            Statuses=json_data.get("Statuses"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Response = Response


@dataclass
class Correlate:
    By: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Correlate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Correlate"]:
        if not json_data:
            return None
        return cls(
            By=json_data.get("By"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Correlate = Correlate


@dataclass
class Match:
    Request: Optional[Sequence["_Request"]]
    Response: Optional[Sequence["_Response"]]

    @classmethod
    def _deserialize(
        cls: Type["_Match"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Match"]:
        if not json_data:
            return None
        return cls(
            Request=json_data.get("Request"),
            Response=json_data.get("Response"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Match = Match


@dataclass
class Request:
    Methods: Optional[Sequence[str]]
    Schemes: Optional[Sequence[str]]
    UrlPattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Request"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Request"]:
        if not json_data:
            return None
        return cls(
            Methods=json_data.get("Methods"),
            Schemes=json_data.get("Schemes"),
            UrlPattern=json_data.get("UrlPattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Request = Request


