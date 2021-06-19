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
    Id: Optional[str]
    Name: Optional[str]
    ProxyAddress: Optional[str]
    ProxyPort: Optional[float]
    ResourceId: Optional[str]
    Check: Optional[Sequence["_CheckDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ProxyAddress=json_data.get("ProxyAddress"),
            ProxyPort=json_data.get("ProxyPort"),
            ResourceId=json_data.get("ResourceId"),
            Check=deserialize_list(json_data.get("Check"), CheckDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CheckDefinition(BaseModel):
    EndPoint: Optional[str]
    Endpoint: Optional[str]
    Healthy: Optional[float]
    Interval: Optional[float]
    Port: Optional[float]
    Protocol: Optional[str]
    TimeOut: Optional[float]
    Timeout: Optional[float]
    Unhealthy: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CheckDefinition"]:
        if not json_data:
            return None
        return cls(
            EndPoint=json_data.get("EndPoint"),
            Endpoint=json_data.get("Endpoint"),
            Healthy=json_data.get("Healthy"),
            Interval=json_data.get("Interval"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            TimeOut=json_data.get("TimeOut"),
            Timeout=json_data.get("Timeout"),
            Unhealthy=json_data.get("Unhealthy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CheckDefinition = CheckDefinition


