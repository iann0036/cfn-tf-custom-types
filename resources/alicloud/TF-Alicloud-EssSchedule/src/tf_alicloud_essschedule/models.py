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
    Description: Optional[str]
    DesiredCapacity: Optional[float]
    Id: Optional[str]
    LaunchExpirationTime: Optional[float]
    LaunchTime: Optional[str]
    MaxValue: Optional[float]
    MinValue: Optional[float]
    RecurrenceEndTime: Optional[str]
    RecurrenceType: Optional[str]
    RecurrenceValue: Optional[str]
    ScalingGroupId: Optional[str]
    ScheduledAction: Optional[str]
    ScheduledTaskName: Optional[str]
    TaskEnabled: Optional[bool]

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
            Description=json_data.get("Description"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            Id=json_data.get("Id"),
            LaunchExpirationTime=json_data.get("LaunchExpirationTime"),
            LaunchTime=json_data.get("LaunchTime"),
            MaxValue=json_data.get("MaxValue"),
            MinValue=json_data.get("MinValue"),
            RecurrenceEndTime=json_data.get("RecurrenceEndTime"),
            RecurrenceType=json_data.get("RecurrenceType"),
            RecurrenceValue=json_data.get("RecurrenceValue"),
            ScalingGroupId=json_data.get("ScalingGroupId"),
            ScheduledAction=json_data.get("ScheduledAction"),
            ScheduledTaskName=json_data.get("ScheduledTaskName"),
            TaskEnabled=json_data.get("TaskEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


