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
    Amount: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    SubscriptionId: Optional[str]
    TimeGrain: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]
    Notification: Optional[Sequence["_NotificationDefinition"]]
    TimePeriod: Optional[Sequence["_TimePeriodDefinition"]]
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
            Amount=json_data.get("Amount"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SubscriptionId=json_data.get("SubscriptionId"),
            TimeGrain=json_data.get("TimeGrain"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
            Notification=deserialize_list(json_data.get("Notification"), NotificationDefinition),
            TimePeriod=deserialize_list(json_data.get("TimePeriod"), TimePeriodDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FilterDefinition(BaseModel):
    Dimension: Optional[Sequence["_DimensionDefinition"]]
    Not: Optional[Sequence["_NotDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Dimension=deserialize_list(json_data.get("Dimension"), DimensionDefinition),
            Not=deserialize_list(json_data.get("Not"), NotDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class DimensionDefinition(BaseModel):
    Name: Optional[str]
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionDefinition = DimensionDefinition


@dataclass
class NotDefinition(BaseModel):
    Dimension: Optional[Sequence["_DimensionDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NotDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotDefinition"]:
        if not json_data:
            return None
        return cls(
            Dimension=deserialize_list(json_data.get("Dimension"), DimensionDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotDefinition = NotDefinition


@dataclass
class TagDefinition(BaseModel):
    Name: Optional[str]
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


@dataclass
class NotificationDefinition(BaseModel):
    ContactEmails: Optional[Sequence[str]]
    ContactGroups: Optional[Sequence[str]]
    ContactRoles: Optional[Sequence[str]]
    Enabled: Optional[bool]
    Operator: Optional[str]
    Threshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationDefinition"]:
        if not json_data:
            return None
        return cls(
            ContactEmails=json_data.get("ContactEmails"),
            ContactGroups=json_data.get("ContactGroups"),
            ContactRoles=json_data.get("ContactRoles"),
            Enabled=json_data.get("Enabled"),
            Operator=json_data.get("Operator"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationDefinition = NotificationDefinition


@dataclass
class TimePeriodDefinition(BaseModel):
    EndDate: Optional[str]
    StartDate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimePeriodDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimePeriodDefinition"]:
        if not json_data:
            return None
        return cls(
            EndDate=json_data.get("EndDate"),
            StartDate=json_data.get("StartDate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimePeriodDefinition = TimePeriodDefinition


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


