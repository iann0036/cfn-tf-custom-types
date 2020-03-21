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
    CreateTime: Optional[str]
    HealthCheck: Optional[bool]
    Interval: Optional[float]
    Name: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    ProxyId: Optional[str]
    RealserverType: Optional[str]
    Scheduler: Optional[str]
    Status: Optional[float]
    RealserverBindSet: Optional[Sequence["_RealserverBindSet"]]

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
            CreateTime=json_data.get("CreateTime"),
            HealthCheck=json_data.get("HealthCheck"),
            Interval=json_data.get("Interval"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            ProxyId=json_data.get("ProxyId"),
            RealserverType=json_data.get("RealserverType"),
            Scheduler=json_data.get("Scheduler"),
            Status=json_data.get("Status"),
            RealserverBindSet=json_data.get("RealserverBindSet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RealserverBindSet:
    Id: Optional[str]
    Ip: Optional[str]
    Port: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RealserverBindSet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RealserverBindSet"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            Port=json_data.get("Port"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RealserverBindSet = RealserverBindSet


