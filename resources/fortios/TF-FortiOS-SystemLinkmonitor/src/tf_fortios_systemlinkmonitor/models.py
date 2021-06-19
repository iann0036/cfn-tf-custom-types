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
    AddrMode: Optional[str]
    DynamicSortSubtable: Optional[str]
    Failtime: Optional[float]
    GatewayIp: Optional[str]
    GatewayIp6: Optional[str]
    HaPriority: Optional[float]
    HttpAgent: Optional[str]
    HttpGet: Optional[str]
    HttpMatch: Optional[str]
    Id: Optional[str]
    Interval: Optional[float]
    Name: Optional[str]
    PacketSize: Optional[float]
    Password: Optional[str]
    Port: Optional[float]
    ProbeCount: Optional[float]
    ProbeTimeout: Optional[float]
    Protocol: Optional[str]
    Recoverytime: Optional[float]
    SecurityMode: Optional[str]
    SourceIp: Optional[str]
    SourceIp6: Optional[str]
    Srcintf: Optional[str]
    Status: Optional[str]
    UpdateCascadeInterface: Optional[str]
    UpdateStaticRoute: Optional[str]
    Vdomparam: Optional[str]
    Server: Optional[Sequence["_ServerDefinition"]]

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
            AddrMode=json_data.get("AddrMode"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Failtime=json_data.get("Failtime"),
            GatewayIp=json_data.get("GatewayIp"),
            GatewayIp6=json_data.get("GatewayIp6"),
            HaPriority=json_data.get("HaPriority"),
            HttpAgent=json_data.get("HttpAgent"),
            HttpGet=json_data.get("HttpGet"),
            HttpMatch=json_data.get("HttpMatch"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            Name=json_data.get("Name"),
            PacketSize=json_data.get("PacketSize"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            ProbeCount=json_data.get("ProbeCount"),
            ProbeTimeout=json_data.get("ProbeTimeout"),
            Protocol=json_data.get("Protocol"),
            Recoverytime=json_data.get("Recoverytime"),
            SecurityMode=json_data.get("SecurityMode"),
            SourceIp=json_data.get("SourceIp"),
            SourceIp6=json_data.get("SourceIp6"),
            Srcintf=json_data.get("Srcintf"),
            Status=json_data.get("Status"),
            UpdateCascadeInterface=json_data.get("UpdateCascadeInterface"),
            UpdateStaticRoute=json_data.get("UpdateStaticRoute"),
            Vdomparam=json_data.get("Vdomparam"),
            Server=deserialize_list(json_data.get("Server"), ServerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ServerDefinition(BaseModel):
    Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerDefinition = ServerDefinition


