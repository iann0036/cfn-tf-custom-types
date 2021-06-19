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
    Action: Optional[str]
    FqdnName: Optional[str]
    HealthCheck: Optional[str]
    HealthCheckDisable: Optional[float]
    Host: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ResolveAs: Optional[str]
    ServerIpv6Addr: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    PortList: Optional[Sequence["_PortListDefinition"]]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]

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
            Action=json_data.get("Action"),
            FqdnName=json_data.get("FqdnName"),
            HealthCheck=json_data.get("HealthCheck"),
            HealthCheckDisable=json_data.get("HealthCheckDisable"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResolveAs=json_data.get("ResolveAs"),
            ServerIpv6Addr=json_data.get("ServerIpv6Addr"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            PortList=deserialize_list(json_data.get("PortList"), PortListDefinition),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PortListDefinition(BaseModel):
    Action: Optional[str]
    HealthCheck: Optional[str]
    HealthCheckDisable: Optional[float]
    PortNumber: Optional[float]
    Protocol: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PortListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortListDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            HealthCheck=json_data.get("HealthCheck"),
            HealthCheckDisable=json_data.get("HealthCheckDisable"),
            PortNumber=json_data.get("PortNumber"),
            Protocol=json_data.get("Protocol"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortListDefinition = PortListDefinition


@dataclass
class SamplingEnableDefinition(BaseModel):
    Counters1: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SamplingEnableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SamplingEnableDefinition"]:
        if not json_data:
            return None
        return cls(
            Counters1=json_data.get("Counters1"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SamplingEnableDefinition = SamplingEnableDefinition


