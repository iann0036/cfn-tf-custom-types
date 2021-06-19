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
    Enabled: Optional[bool]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TargetResourceId: Optional[str]
    Notification: Optional[Sequence["_NotificationDefinition"]]
    Profile: Optional[Sequence["_ProfileDefinition"]]
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
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TargetResourceId=json_data.get("TargetResourceId"),
            Notification=deserialize_list(json_data.get("Notification"), NotificationDefinition),
            Profile=deserialize_list(json_data.get("Profile"), ProfileDefinition),
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
class NotificationDefinition(BaseModel):
    Email: Optional[Sequence["_EmailDefinition"]]
    Webhook: Optional[Sequence["_WebhookDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationDefinition"]:
        if not json_data:
            return None
        return cls(
            Email=deserialize_list(json_data.get("Email"), EmailDefinition),
            Webhook=deserialize_list(json_data.get("Webhook"), WebhookDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationDefinition = NotificationDefinition


@dataclass
class EmailDefinition(BaseModel):
    CustomEmails: Optional[Sequence[str]]
    SendToSubscriptionAdministrator: Optional[bool]
    SendToSubscriptionCoAdministrator: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EmailDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomEmails=json_data.get("CustomEmails"),
            SendToSubscriptionAdministrator=json_data.get("SendToSubscriptionAdministrator"),
            SendToSubscriptionCoAdministrator=json_data.get("SendToSubscriptionCoAdministrator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailDefinition = EmailDefinition


@dataclass
class WebhookDefinition(BaseModel):
    Properties: Optional[Sequence["_PropertiesDefinition"]]
    ServiceUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebhookDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebhookDefinition"]:
        if not json_data:
            return None
        return cls(
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition),
            ServiceUri=json_data.get("ServiceUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebhookDefinition = WebhookDefinition


@dataclass
class PropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition = PropertiesDefinition


@dataclass
class ProfileDefinition(BaseModel):
    Name: Optional[str]
    Capacity: Optional[Sequence["_CapacityDefinition"]]
    FixedDate: Optional[Sequence["_FixedDateDefinition"]]
    Recurrence: Optional[Sequence["_RecurrenceDefinition"]]
    Rule: Optional[Sequence["_RuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Capacity=deserialize_list(json_data.get("Capacity"), CapacityDefinition),
            FixedDate=deserialize_list(json_data.get("FixedDate"), FixedDateDefinition),
            Recurrence=deserialize_list(json_data.get("Recurrence"), RecurrenceDefinition),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProfileDefinition = ProfileDefinition


@dataclass
class CapacityDefinition(BaseModel):
    Default: Optional[float]
    Maximum: Optional[float]
    Minimum: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityDefinition"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
            Maximum=json_data.get("Maximum"),
            Minimum=json_data.get("Minimum"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityDefinition = CapacityDefinition


@dataclass
class FixedDateDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]
    Timezone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FixedDateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FixedDateDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
            Timezone=json_data.get("Timezone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FixedDateDefinition = FixedDateDefinition


@dataclass
class RecurrenceDefinition(BaseModel):
    Days: Optional[Sequence[str]]
    Hours: Optional[Sequence[float]]
    Minutes: Optional[Sequence[float]]
    Timezone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecurrenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecurrenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
            Hours=json_data.get("Hours"),
            Minutes=json_data.get("Minutes"),
            Timezone=json_data.get("Timezone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecurrenceDefinition = RecurrenceDefinition


@dataclass
class RuleDefinition(BaseModel):
    MetricTrigger: Optional[Sequence["_MetricTriggerDefinition"]]
    ScaleAction: Optional[Sequence["_ScaleActionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            MetricTrigger=deserialize_list(json_data.get("MetricTrigger"), MetricTriggerDefinition),
            ScaleAction=deserialize_list(json_data.get("ScaleAction"), ScaleActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class MetricTriggerDefinition(BaseModel):
    MetricName: Optional[str]
    MetricNamespace: Optional[str]
    MetricResourceId: Optional[str]
    Operator: Optional[str]
    Statistic: Optional[str]
    Threshold: Optional[float]
    TimeAggregation: Optional[str]
    TimeGrain: Optional[str]
    TimeWindow: Optional[str]
    Dimensions: Optional[Sequence["_DimensionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricTriggerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricTriggerDefinition"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            MetricNamespace=json_data.get("MetricNamespace"),
            MetricResourceId=json_data.get("MetricResourceId"),
            Operator=json_data.get("Operator"),
            Statistic=json_data.get("Statistic"),
            Threshold=json_data.get("Threshold"),
            TimeAggregation=json_data.get("TimeAggregation"),
            TimeGrain=json_data.get("TimeGrain"),
            TimeWindow=json_data.get("TimeWindow"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricTriggerDefinition = MetricTriggerDefinition


@dataclass
class DimensionsDefinition(BaseModel):
    Name: Optional[str]
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionsDefinition = DimensionsDefinition


@dataclass
class ScaleActionDefinition(BaseModel):
    Cooldown: Optional[str]
    Direction: Optional[str]
    Type: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ScaleActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScaleActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Cooldown=json_data.get("Cooldown"),
            Direction=json_data.get("Direction"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScaleActionDefinition = ScaleActionDefinition


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


