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
    CheckIntervalSec: Optional[float]
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    HealthyThreshold: Optional[float]
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    SelfLink: Optional[str]
    TimeoutSec: Optional[float]
    Type: Optional[str]
    UnhealthyThreshold: Optional[float]
    Http2HealthCheck: Optional[Sequence["_Http2HealthCheck"]]
    HttpHealthCheck: Optional[Sequence["_HttpHealthCheck"]]
    HttpsHealthCheck: Optional[Sequence["_HttpsHealthCheck"]]
    SslHealthCheck: Optional[Sequence["_SslHealthCheck"]]
    TcpHealthCheck: Optional[Sequence["_TcpHealthCheck"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CheckIntervalSec=json_data.get("CheckIntervalSec"),
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            HealthyThreshold=json_data.get("HealthyThreshold"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            SelfLink=json_data.get("SelfLink"),
            TimeoutSec=json_data.get("TimeoutSec"),
            Type=json_data.get("Type"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
            Http2HealthCheck=json_data.get("Http2HealthCheck"),
            HttpHealthCheck=json_data.get("HttpHealthCheck"),
            HttpsHealthCheck=json_data.get("HttpsHealthCheck"),
            SslHealthCheck=json_data.get("SslHealthCheck"),
            TcpHealthCheck=json_data.get("TcpHealthCheck"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Http2HealthCheck:
    Host: Optional[str]
    Port: Optional[float]
    PortName: Optional[str]
    PortSpecification: Optional[str]
    ProxyHeader: Optional[str]
    RequestPath: Optional[str]
    Response: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Http2HealthCheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Http2HealthCheck"]:
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
_Http2HealthCheck = Http2HealthCheck


@dataclass
class HttpHealthCheck:
    Host: Optional[str]
    Port: Optional[float]
    PortName: Optional[str]
    PortSpecification: Optional[str]
    ProxyHeader: Optional[str]
    RequestPath: Optional[str]
    Response: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpHealthCheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpHealthCheck"]:
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
_HttpHealthCheck = HttpHealthCheck


@dataclass
class HttpsHealthCheck:
    Host: Optional[str]
    Port: Optional[float]
    PortName: Optional[str]
    PortSpecification: Optional[str]
    ProxyHeader: Optional[str]
    RequestPath: Optional[str]
    Response: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpsHealthCheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpsHealthCheck"]:
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
_HttpsHealthCheck = HttpsHealthCheck


@dataclass
class SslHealthCheck:
    Port: Optional[float]
    PortName: Optional[str]
    PortSpecification: Optional[str]
    ProxyHeader: Optional[str]
    Request: Optional[str]
    Response: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslHealthCheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslHealthCheck"]:
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
_SslHealthCheck = SslHealthCheck


@dataclass
class TcpHealthCheck:
    Port: Optional[float]
    PortName: Optional[str]
    PortSpecification: Optional[str]
    ProxyHeader: Optional[str]
    Request: Optional[str]
    Response: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TcpHealthCheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpHealthCheck"]:
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
_TcpHealthCheck = TcpHealthCheck


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


