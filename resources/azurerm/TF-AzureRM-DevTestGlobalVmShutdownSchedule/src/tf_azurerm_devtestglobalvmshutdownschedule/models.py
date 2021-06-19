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
    DailyRecurrenceTime: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Location: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Timezone: Optional[str]
    VirtualMachineId: Optional[str]
    NotificationSettings: Optional[Sequence["_NotificationSettingsDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            DailyRecurrenceTime=json_data.get("DailyRecurrenceTime"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Timezone=json_data.get("Timezone"),
            VirtualMachineId=json_data.get("VirtualMachineId"),
            NotificationSettings=deserialize_list(json_data.get("NotificationSettings"), NotificationSettingsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class NotificationSettingsDefinition(BaseModel):
    Enabled: Optional[bool]
    TimeInMinutes: Optional[float]
    WebhookUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            TimeInMinutes=json_data.get("TimeInMinutes"),
            WebhookUrl=json_data.get("WebhookUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationSettingsDefinition = NotificationSettingsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


