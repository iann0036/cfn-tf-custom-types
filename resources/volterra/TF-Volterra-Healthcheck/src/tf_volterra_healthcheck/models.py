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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Description: Optional[str]
    Disable: Optional[bool]
    HealthyThreshold: Optional[float]
    Id: Optional[str]
    Interval: Optional[float]
    JitterPercent: Optional[float]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    Timeout: Optional[float]
    UnhealthyThreshold: Optional[float]
    HttpHealthCheck: Optional[Sequence["_HttpHealthCheckDefinition"]]
    TcpHealthCheck: Optional[Sequence["_TcpHealthCheckDefinition"]]

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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            HealthyThreshold=json_data.get("HealthyThreshold"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            JitterPercent=json_data.get("JitterPercent"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Timeout=json_data.get("Timeout"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
            HttpHealthCheck=deserialize_list(json_data.get("HttpHealthCheck"), HttpHealthCheckDefinition),
            TcpHealthCheck=deserialize_list(json_data.get("TcpHealthCheck"), TcpHealthCheckDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class HttpHealthCheckDefinition(BaseModel):
    Headers: Optional[Sequence["_HeadersDefinition"]]
    HostHeader: Optional[str]
    Path: Optional[str]
    RequestHeadersToRemove: Optional[Sequence[str]]
    UseHttp2: Optional[bool]
    UseOriginServerName: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_HttpHealthCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpHealthCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
            HostHeader=json_data.get("HostHeader"),
            Path=json_data.get("Path"),
            RequestHeadersToRemove=json_data.get("RequestHeadersToRemove"),
            UseHttp2=json_data.get("UseHttp2"),
            UseOriginServerName=json_data.get("UseOriginServerName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpHealthCheckDefinition = HttpHealthCheckDefinition


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
class TcpHealthCheckDefinition(BaseModel):
    ExpectedResponse: Optional[str]
    SendPayload: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TcpHealthCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpHealthCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            ExpectedResponse=json_data.get("ExpectedResponse"),
            SendPayload=json_data.get("SendPayload"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpHealthCheckDefinition = TcpHealthCheckDefinition


