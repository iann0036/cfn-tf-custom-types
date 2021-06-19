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
    DestinationPort: Optional[float]
    Id: Optional[str]
    ListenPort: Optional[float]
    LoadBalancerId: Optional[str]
    Protocol: Optional[str]
    Proxyprotocol: Optional[bool]
    HealthCheck: Optional[Sequence["_HealthCheckDefinition"]]
    Http: Optional[Sequence["_HttpDefinition"]]

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
            DestinationPort=json_data.get("DestinationPort"),
            Id=json_data.get("Id"),
            ListenPort=json_data.get("ListenPort"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            Protocol=json_data.get("Protocol"),
            Proxyprotocol=json_data.get("Proxyprotocol"),
            HealthCheck=deserialize_list(json_data.get("HealthCheck"), HealthCheckDefinition),
            Http=deserialize_list(json_data.get("Http"), HttpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HealthCheckDefinition(BaseModel):
    Interval: Optional[float]
    Port: Optional[float]
    Protocol: Optional[str]
    Retries: Optional[float]
    Timeout: Optional[float]
    Http: Optional[Sequence["_HttpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            Interval=json_data.get("Interval"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            Retries=json_data.get("Retries"),
            Timeout=json_data.get("Timeout"),
            Http=deserialize_list(json_data.get("Http"), HttpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckDefinition = HealthCheckDefinition


@dataclass
class HttpDefinition(BaseModel):
    Domain: Optional[str]
    Path: Optional[str]
    Response: Optional[str]
    StatusCodes: Optional[Sequence[str]]
    Tls: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_HttpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpDefinition"]:
        if not json_data:
            return None
        return cls(
            Domain=json_data.get("Domain"),
            Path=json_data.get("Path"),
            Response=json_data.get("Response"),
            StatusCodes=json_data.get("StatusCodes"),
            Tls=json_data.get("Tls"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpDefinition = HttpDefinition


