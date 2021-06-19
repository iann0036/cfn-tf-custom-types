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
    Consumers: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    LoadBalancer: Optional[str]
    Name: Optional[str]
    OperationDetails: Optional[bool]
    Servers: Optional[Sequence[str]]
    State: Optional[str]
    Status: Optional[bool]
    Tags: Optional[Sequence[str]]
    Uri: Optional[str]
    VnicSet: Optional[str]
    HealthCheck: Optional[Sequence["_HealthCheckDefinition"]]

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
            Consumers=json_data.get("Consumers"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            LoadBalancer=json_data.get("LoadBalancer"),
            Name=json_data.get("Name"),
            OperationDetails=json_data.get("OperationDetails"),
            Servers=json_data.get("Servers"),
            State=json_data.get("State"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            Uri=json_data.get("Uri"),
            VnicSet=json_data.get("VnicSet"),
            HealthCheck=deserialize_list(json_data.get("HealthCheck"), HealthCheckDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HealthCheckDefinition(BaseModel):
    AcceptedReturnCodes: Optional[Sequence[str]]
    Enabled: Optional[bool]
    HealthyThreshold: Optional[float]
    Interval: Optional[float]
    Path: Optional[str]
    Timeout: Optional[float]
    Type: Optional[str]
    UnhealthyThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            AcceptedReturnCodes=json_data.get("AcceptedReturnCodes"),
            Enabled=json_data.get("Enabled"),
            HealthyThreshold=json_data.get("HealthyThreshold"),
            Interval=json_data.get("Interval"),
            Path=json_data.get("Path"),
            Timeout=json_data.get("Timeout"),
            Type=json_data.get("Type"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckDefinition = HealthCheckDefinition


