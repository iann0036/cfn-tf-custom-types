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
    DesiredCapacity: Optional[float]
    EndTime: Optional[str]
    Id: Optional[str]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Recurrence: Optional[str]
    ScalingGroupId: Optional[str]
    ScheduleActionName: Optional[str]
    StartTime: Optional[str]

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
            DesiredCapacity=json_data.get("DesiredCapacity"),
            EndTime=json_data.get("EndTime"),
            Id=json_data.get("Id"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Recurrence=json_data.get("Recurrence"),
            ScalingGroupId=json_data.get("ScalingGroupId"),
            ScheduleActionName=json_data.get("ScheduleActionName"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


