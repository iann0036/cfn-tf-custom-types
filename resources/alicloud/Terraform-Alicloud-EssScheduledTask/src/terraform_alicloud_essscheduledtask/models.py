# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    LaunchExpirationTime: Optional[float]
    LaunchTime: Optional[str]
    RecurrenceEndTime: Optional[str]
    RecurrenceType: Optional[str]
    RecurrenceValue: Optional[str]
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
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            LaunchExpirationTime=json_data.get("LaunchExpirationTime"),
            LaunchTime=json_data.get("LaunchTime"),
            RecurrenceEndTime=json_data.get("RecurrenceEndTime"),
            RecurrenceType=json_data.get("RecurrenceType"),
            RecurrenceValue=json_data.get("RecurrenceValue"),
            ScheduledAction=json_data.get("ScheduledAction"),
            ScheduledTaskName=json_data.get("ScheduledTaskName"),
            TaskEnabled=json_data.get("TaskEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


