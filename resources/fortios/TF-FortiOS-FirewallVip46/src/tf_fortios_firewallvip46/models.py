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
    ArpReply: Optional[str]
    Color: Optional[float]
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    Extip: Optional[str]
    Extport: Optional[str]
    Fosid: Optional[float]
    Id: Optional[str]
    LdbMethod: Optional[str]
    Mappedip: Optional[str]
    Mappedport: Optional[str]
    Name: Optional[str]
    Portforward: Optional[str]
    Protocol: Optional[str]
    ServerType: Optional[str]
    Type: Optional[str]
    Uuid: Optional[str]
    Vdomparam: Optional[str]
    Monitor: Optional[Sequence["_MonitorDefinition"]]
    Realservers: Optional[Sequence["_RealserversDefinition"]]
    SrcFilter: Optional[Sequence["_SrcFilterDefinition"]]
    SrcintfFilter: Optional[Sequence["_SrcintfFilterDefinition"]]

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
            ArpReply=json_data.get("ArpReply"),
            Color=json_data.get("Color"),
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Extip=json_data.get("Extip"),
            Extport=json_data.get("Extport"),
            Fosid=json_data.get("Fosid"),
            Id=json_data.get("Id"),
            LdbMethod=json_data.get("LdbMethod"),
            Mappedip=json_data.get("Mappedip"),
            Mappedport=json_data.get("Mappedport"),
            Name=json_data.get("Name"),
            Portforward=json_data.get("Portforward"),
            Protocol=json_data.get("Protocol"),
            ServerType=json_data.get("ServerType"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
            Vdomparam=json_data.get("Vdomparam"),
            Monitor=deserialize_list(json_data.get("Monitor"), MonitorDefinition),
            Realservers=deserialize_list(json_data.get("Realservers"), RealserversDefinition),
            SrcFilter=deserialize_list(json_data.get("SrcFilter"), SrcFilterDefinition),
            SrcintfFilter=deserialize_list(json_data.get("SrcintfFilter"), SrcintfFilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MonitorDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitorDefinition = MonitorDefinition


@dataclass
class RealserversDefinition(BaseModel):
    ClientIp: Optional[str]
    Healthcheck: Optional[str]
    HolddownInterval: Optional[float]
    Id: Optional[float]
    Ip: Optional[str]
    MaxConnections: Optional[float]
    Monitor: Optional[str]
    Port: Optional[float]
    Status: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RealserversDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RealserversDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientIp=json_data.get("ClientIp"),
            Healthcheck=json_data.get("Healthcheck"),
            HolddownInterval=json_data.get("HolddownInterval"),
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            MaxConnections=json_data.get("MaxConnections"),
            Monitor=json_data.get("Monitor"),
            Port=json_data.get("Port"),
            Status=json_data.get("Status"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RealserversDefinition = RealserversDefinition


@dataclass
class SrcFilterDefinition(BaseModel):
    Range: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Range=json_data.get("Range"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcFilterDefinition = SrcFilterDefinition


@dataclass
class SrcintfFilterDefinition(BaseModel):
    InterfaceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcintfFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcintfFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            InterfaceName=json_data.get("InterfaceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcintfFilterDefinition = SrcintfFilterDefinition


