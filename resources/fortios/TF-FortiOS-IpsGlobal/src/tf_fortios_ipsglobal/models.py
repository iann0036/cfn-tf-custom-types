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
    AnomalyMode: Optional[str]
    Database: Optional[str]
    DeepAppInspDbLimit: Optional[float]
    DeepAppInspTimeout: Optional[float]
    EngineCount: Optional[float]
    ExcludeSignatures: Optional[str]
    FailOpen: Optional[str]
    Id: Optional[str]
    IntelligentMode: Optional[str]
    NgfwMaxScanRange: Optional[float]
    PacketLogQueueDepth: Optional[float]
    SessionLimitMode: Optional[str]
    SkypeClientPublicIpaddr: Optional[str]
    SocketSize: Optional[float]
    SyncSessionTtl: Optional[str]
    TrafficSubmit: Optional[str]
    Vdomparam: Optional[str]
    TlsActiveProbe: Optional[Sequence["_TlsActiveProbeDefinition"]]

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
            AnomalyMode=json_data.get("AnomalyMode"),
            Database=json_data.get("Database"),
            DeepAppInspDbLimit=json_data.get("DeepAppInspDbLimit"),
            DeepAppInspTimeout=json_data.get("DeepAppInspTimeout"),
            EngineCount=json_data.get("EngineCount"),
            ExcludeSignatures=json_data.get("ExcludeSignatures"),
            FailOpen=json_data.get("FailOpen"),
            Id=json_data.get("Id"),
            IntelligentMode=json_data.get("IntelligentMode"),
            NgfwMaxScanRange=json_data.get("NgfwMaxScanRange"),
            PacketLogQueueDepth=json_data.get("PacketLogQueueDepth"),
            SessionLimitMode=json_data.get("SessionLimitMode"),
            SkypeClientPublicIpaddr=json_data.get("SkypeClientPublicIpaddr"),
            SocketSize=json_data.get("SocketSize"),
            SyncSessionTtl=json_data.get("SyncSessionTtl"),
            TrafficSubmit=json_data.get("TrafficSubmit"),
            Vdomparam=json_data.get("Vdomparam"),
            TlsActiveProbe=deserialize_list(json_data.get("TlsActiveProbe"), TlsActiveProbeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TlsActiveProbeDefinition(BaseModel):
    Interface: Optional[str]
    InterfaceSelectMethod: Optional[str]
    SourceIp: Optional[str]
    SourceIp6: Optional[str]
    Vdom: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TlsActiveProbeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsActiveProbeDefinition"]:
        if not json_data:
            return None
        return cls(
            Interface=json_data.get("Interface"),
            InterfaceSelectMethod=json_data.get("InterfaceSelectMethod"),
            SourceIp=json_data.get("SourceIp"),
            SourceIp6=json_data.get("SourceIp6"),
            Vdom=json_data.get("Vdom"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsActiveProbeDefinition = TlsActiveProbeDefinition


