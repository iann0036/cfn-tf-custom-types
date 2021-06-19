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
    Diffserv: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    ServerName: Optional[str]
    Status: Optional[str]
    UpdateInbandwidth: Optional[str]
    UpdateInbandwidthMaximum: Optional[float]
    UpdateInbandwidthMinimum: Optional[float]
    UpdateOutbandwidth: Optional[str]
    UpdateOutbandwidthMaximum: Optional[float]
    UpdateOutbandwidthMinimum: Optional[float]
    Vdomparam: Optional[str]
    Schedules: Optional[Sequence["_SchedulesDefinition"]]

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
            Diffserv=json_data.get("Diffserv"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            ServerName=json_data.get("ServerName"),
            Status=json_data.get("Status"),
            UpdateInbandwidth=json_data.get("UpdateInbandwidth"),
            UpdateInbandwidthMaximum=json_data.get("UpdateInbandwidthMaximum"),
            UpdateInbandwidthMinimum=json_data.get("UpdateInbandwidthMinimum"),
            UpdateOutbandwidth=json_data.get("UpdateOutbandwidth"),
            UpdateOutbandwidthMaximum=json_data.get("UpdateOutbandwidthMaximum"),
            UpdateOutbandwidthMinimum=json_data.get("UpdateOutbandwidthMinimum"),
            Vdomparam=json_data.get("Vdomparam"),
            Schedules=deserialize_list(json_data.get("Schedules"), SchedulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SchedulesDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchedulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchedulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchedulesDefinition = SchedulesDefinition


