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
    ConnectTimeout: Optional[float]
    Domain: Optional[str]
    ForwardHost: Optional[str]
    HealthCheck: Optional[bool]
    HealthCheckMethod: Optional[str]
    HealthCheckPath: Optional[str]
    HealthCheckStatusCodes: Optional[Sequence[float]]
    Id: Optional[str]
    Interval: Optional[float]
    ListenerId: Optional[str]
    Path: Optional[str]
    RealserverType: Optional[str]
    Scheduler: Optional[str]
    Realservers: Optional[Sequence["_Realservers"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ConnectTimeout=json_data.get("ConnectTimeout"),
            Domain=json_data.get("Domain"),
            ForwardHost=json_data.get("ForwardHost"),
            HealthCheck=json_data.get("HealthCheck"),
            HealthCheckMethod=json_data.get("HealthCheckMethod"),
            HealthCheckPath=json_data.get("HealthCheckPath"),
            HealthCheckStatusCodes=json_data.get("HealthCheckStatusCodes"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            ListenerId=json_data.get("ListenerId"),
            Path=json_data.get("Path"),
            RealserverType=json_data.get("RealserverType"),
            Scheduler=json_data.get("Scheduler"),
            Realservers=json_data.get("Realservers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Realservers:
    Id: Optional[str]
    Ip: Optional[str]
    Port: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Realservers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Realservers"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            Port=json_data.get("Port"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Realservers = Realservers


