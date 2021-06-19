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
    ByDay: Optional[Sequence[str]]
    ByMonth: Optional[Sequence[float]]
    ByMonthday: Optional[Sequence[float]]
    Duration: Optional[float]
    Frequency: Optional[str]
    Id: Optional[str]
    Interval: Optional[float]
    Level: Optional[float]
    Name: Optional[str]
    RollingUsers: Optional[Sequence[Sequence[str]]]
    ScheduleId: Optional[str]
    Start: Optional[str]
    Type: Optional[str]
    Users: Optional[Sequence[str]]
    WeekStart: Optional[str]

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
            ByDay=json_data.get("ByDay"),
            ByMonth=json_data.get("ByMonth"),
            ByMonthday=json_data.get("ByMonthday"),
            Duration=json_data.get("Duration"),
            Frequency=json_data.get("Frequency"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            Level=json_data.get("Level"),
            Name=json_data.get("Name"),
            RollingUsers=json_data.get("RollingUsers"),
            ScheduleId=json_data.get("ScheduleId"),
            Start=json_data.get("Start"),
            Type=json_data.get("Type"),
            Users=json_data.get("Users"),
            WeekStart=json_data.get("WeekStart"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


