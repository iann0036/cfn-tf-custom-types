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
    CollectorIp: Optional[str]
    CollectorPort: Optional[float]
    DynamicSortSubtable: Optional[str]
    Format: Optional[str]
    Id: Optional[str]
    Level: Optional[str]
    MaxExportPktSize: Optional[float]
    SampleMode: Optional[str]
    SampleRate: Optional[float]
    TimeoutGeneral: Optional[float]
    TimeoutIcmp: Optional[float]
    TimeoutMax: Optional[float]
    TimeoutTcp: Optional[float]
    TimeoutTcpFin: Optional[float]
    TimeoutTcpRst: Optional[float]
    TimeoutUdp: Optional[float]
    Transport: Optional[str]
    Vdomparam: Optional[str]
    Aggregates: Optional[Sequence["_AggregatesDefinition"]]

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
            CollectorIp=json_data.get("CollectorIp"),
            CollectorPort=json_data.get("CollectorPort"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Format=json_data.get("Format"),
            Id=json_data.get("Id"),
            Level=json_data.get("Level"),
            MaxExportPktSize=json_data.get("MaxExportPktSize"),
            SampleMode=json_data.get("SampleMode"),
            SampleRate=json_data.get("SampleRate"),
            TimeoutGeneral=json_data.get("TimeoutGeneral"),
            TimeoutIcmp=json_data.get("TimeoutIcmp"),
            TimeoutMax=json_data.get("TimeoutMax"),
            TimeoutTcp=json_data.get("TimeoutTcp"),
            TimeoutTcpFin=json_data.get("TimeoutTcpFin"),
            TimeoutTcpRst=json_data.get("TimeoutTcpRst"),
            TimeoutUdp=json_data.get("TimeoutUdp"),
            Transport=json_data.get("Transport"),
            Vdomparam=json_data.get("Vdomparam"),
            Aggregates=deserialize_list(json_data.get("Aggregates"), AggregatesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AggregatesDefinition(BaseModel):
    Id: Optional[float]
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AggregatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggregatesDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggregatesDefinition = AggregatesDefinition


