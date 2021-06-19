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
    CheckIntervalSec: Optional[float]
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    HealthyThreshold: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    TimeoutSec: Optional[float]
    Type: Optional[str]
    UnhealthyThreshold: Optional[float]
    GrpcHealthCheck: Optional[Sequence["_GrpcHealthCheckDefinition"]]
    Http2HealthCheck: Optional[Sequence["_Http2HealthCheckDefinition"]]
    HttpHealthCheck: Optional[Sequence["_HttpHealthCheckDefinition"]]
    HttpsHealthCheck: Optional[Sequence["_HttpsHealthCheckDefinition"]]
    LogConfig: Optional[Sequence["_LogConfigDefinition"]]
    SslHealthCheck: Optional[Sequence["_SslHealthCheckDefinition"]]
    TcpHealthCheck: Optional[Sequence["_TcpHealthCheckDefinition"]]
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
            CheckIntervalSec=json_data.get("CheckIntervalSec"),
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            HealthyThreshold=json_data.get("HealthyThreshold"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            TimeoutSec=json_data.get("TimeoutSec"),
            Type=json_data.get("Type"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
            GrpcHealthCheck=deserialize_list(json_data.get("GrpcHealthCheck"), GrpcHealthCheckDefinition),
            Http2HealthCheck=deserialize_list(json_data.get("Http2HealthCheck"), Http2HealthCheckDefinition),
            HttpHealthCheck=deserialize_list(json_data.get("HttpHealthCheck"), HttpHealthCheckDefinition),
            HttpsHealthCheck=deserialize_list(json_data.get("HttpsHealthCheck"), HttpsHealthCheckDefinition),
            LogConfig=deserialize_list(json_data.get("LogConfig"), LogConfigDefinition),
            SslHealthCheck=deserialize_list(json_data.get("SslHealthCheck"), SslHealthCheckDefinition),
            TcpHealthCheck=deserialize_list(json_data.get("TcpHealthCheck"), TcpHealthCheckDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GrpcHealthCheckDefinition(BaseModel):
    GrpcServiceName: Optional[str]
    Port: Optional[float]
    PortName: Optional[str]
    PortSpecification: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GrpcHealthCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrpcHealthCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            GrpcServiceName=json_data.get("GrpcServiceName"),
            Port=json_data.get("Port"),
            PortName=json_data.get("PortName"),
            PortSpecification=json_data.get("PortSpecification"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrpcHealthCheckDefinition = GrpcHealthCheckDefinition


@dataclass
class Http2HealthCheckDefinition(BaseModel):
    Host: Optional[str]
    Port: Optional[float]
    PortName: Optional[str]
    PortSpecification: Optional[str]
    ProxyHeader: Optional[str]
    RequestPath: Optional[str]
    Response: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Http2HealthCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Http2HealthCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Port=json_data.get("Port"),
            PortName=json_data.get("PortName"),
            PortSpecification=json_data.get("PortSpecification"),
            ProxyHeader=json_data.get("ProxyHeader"),
            RequestPath=json_data.get("RequestPath"),
            Response=json_data.get("Response"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Http2HealthCheckDefinition = Http2HealthCheckDefinition


@dataclass
class HttpHealthCheckDefinition(BaseModel):
    Host: Optional[str]
    Port: Optional[float]
    PortName: Optional[str]
    PortSpecification: Optional[str]
    ProxyHeader: Optional[str]
    RequestPath: Optional[str]
    Response: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpHealthCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpHealthCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Port=json_data.get("Port"),
            PortName=json_data.get("PortName"),
            PortSpecification=json_data.get("PortSpecification"),
            ProxyHeader=json_data.get("ProxyHeader"),
            RequestPath=json_data.get("RequestPath"),
            Response=json_data.get("Response"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpHealthCheckDefinition = HttpHealthCheckDefinition


@dataclass
class HttpsHealthCheckDefinition(BaseModel):
    Host: Optional[str]
    Port: Optional[float]
    PortName: Optional[str]
    PortSpecification: Optional[str]
    ProxyHeader: Optional[str]
    RequestPath: Optional[str]
    Response: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpsHealthCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpsHealthCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Port=json_data.get("Port"),
            PortName=json_data.get("PortName"),
            PortSpecification=json_data.get("PortSpecification"),
            ProxyHeader=json_data.get("ProxyHeader"),
            RequestPath=json_data.get("RequestPath"),
            Response=json_data.get("Response"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpsHealthCheckDefinition = HttpsHealthCheckDefinition


@dataclass
class LogConfigDefinition(BaseModel):
    Enable: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfigDefinition = LogConfigDefinition


@dataclass
class SslHealthCheckDefinition(BaseModel):
    Port: Optional[float]
    PortName: Optional[str]
    PortSpecification: Optional[str]
    ProxyHeader: Optional[str]
    Request: Optional[str]
    Response: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslHealthCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslHealthCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            PortName=json_data.get("PortName"),
            PortSpecification=json_data.get("PortSpecification"),
            ProxyHeader=json_data.get("ProxyHeader"),
            Request=json_data.get("Request"),
            Response=json_data.get("Response"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslHealthCheckDefinition = SslHealthCheckDefinition


@dataclass
class TcpHealthCheckDefinition(BaseModel):
    Port: Optional[float]
    PortName: Optional[str]
    PortSpecification: Optional[str]
    ProxyHeader: Optional[str]
    Request: Optional[str]
    Response: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TcpHealthCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpHealthCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            PortName=json_data.get("PortName"),
            PortSpecification=json_data.get("PortSpecification"),
            ProxyHeader=json_data.get("ProxyHeader"),
            Request=json_data.get("Request"),
            Response=json_data.get("Response"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpHealthCheckDefinition = TcpHealthCheckDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


