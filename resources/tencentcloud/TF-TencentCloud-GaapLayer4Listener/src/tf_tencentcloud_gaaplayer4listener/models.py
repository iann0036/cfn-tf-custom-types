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
    ConnectTimeout: Optional[float]
    CreateTime: Optional[str]
    HealthCheck: Optional[bool]
    Id: Optional[str]
    Interval: Optional[float]
    Name: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    ProxyId: Optional[str]
    RealserverType: Optional[str]
    Scheduler: Optional[str]
    Status: Optional[float]
    RealserverBindSet: Optional[Sequence["_RealserverBindSetDefinition"]]

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
            ConnectTimeout=json_data.get("ConnectTimeout"),
            CreateTime=json_data.get("CreateTime"),
            HealthCheck=json_data.get("HealthCheck"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            ProxyId=json_data.get("ProxyId"),
            RealserverType=json_data.get("RealserverType"),
            Scheduler=json_data.get("Scheduler"),
            Status=json_data.get("Status"),
            RealserverBindSet=deserialize_list(json_data.get("RealserverBindSet"), RealserverBindSetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RealserverBindSetDefinition(BaseModel):
    Id: Optional[str]
    Ip: Optional[str]
    Port: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RealserverBindSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RealserverBindSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            Port=json_data.get("Port"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RealserverBindSetDefinition = RealserverBindSetDefinition


