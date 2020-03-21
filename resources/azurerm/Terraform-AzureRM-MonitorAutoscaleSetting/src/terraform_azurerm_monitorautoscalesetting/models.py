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
    Enabled: Optional[bool]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TargetResourceId: Optional[str]
    Notification: Optional[Sequence["_Notification"]]
    Profile: Optional[Sequence["_Profile"]]
    Timeouts: Optional["_Timeouts"]
    Email: Optional[Sequence["_Email"]]
    Webhook: Optional[Sequence["_Webhook"]]
    Capacity: Optional[Sequence["_Capacity"]]
    FixedDate: Optional[Sequence["_FixedDate"]]
    Recurrence: Optional[Sequence["_Recurrence"]]
    Rule: Optional[Sequence["_Rule"]]
    MetricTrigger: Optional[Sequence["_MetricTrigger"]]
    ScaleAction: Optional[Sequence["_ScaleAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Enabled=json_data.get("Enabled"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=json_data.get("Tags"),
            TargetResourceId=json_data.get("TargetResourceId"),
            Notification=json_data.get("Notification"),
            Profile=json_data.get("Profile"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Email=json_data.get("Email"),
            Webhook=json_data.get("Webhook"),
            Capacity=json_data.get("Capacity"),
            FixedDate=json_data.get("FixedDate"),
            Recurrence=json_data.get("Recurrence"),
            Rule=json_data.get("Rule"),
            MetricTrigger=json_data.get("MetricTrigger"),
            ScaleAction=json_data.get("ScaleAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Notification:
    Email: Optional[Sequence["_Email"]]
    Webhook: Optional[Sequence["_Webhook"]]

    @classmethod
    def _deserialize(
        cls: Type["_Notification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Notification"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            Webhook=json_data.get("Webhook"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Notification = Notification


@dataclass
class Email:
    CustomEmails: Optional[Sequence[str]]
    SendToSubscriptionAdministrator: Optional[bool]
    SendToSubscriptionCoAdministrator: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Email"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Email"]:
        if not json_data:
            return None
        return cls(
            CustomEmails=json_data.get("CustomEmails"),
            SendToSubscriptionAdministrator=json_data.get("SendToSubscriptionAdministrator"),
            SendToSubscriptionCoAdministrator=json_data.get("SendToSubscriptionCoAdministrator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Email = Email


@dataclass
class Webhook:
    Properties: Optional[Sequence["_Properties"]]
    ServiceUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Webhook"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Webhook"]:
        if not json_data:
            return None
        return cls(
            Properties=json_data.get("Properties"),
            ServiceUri=json_data.get("ServiceUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Webhook = Webhook


@dataclass
class Properties:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Properties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Properties"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Properties = Properties


@dataclass
class Profile:
    Name: Optional[str]
    Capacity: Optional[Sequence["_Capacity"]]
    FixedDate: Optional[Sequence["_FixedDate"]]
    Recurrence: Optional[Sequence["_Recurrence"]]
    Rule: Optional[Sequence["_Rule"]]

    @classmethod
    def _deserialize(
        cls: Type["_Profile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Profile"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Capacity=json_data.get("Capacity"),
            FixedDate=json_data.get("FixedDate"),
            Recurrence=json_data.get("Recurrence"),
            Rule=json_data.get("Rule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Profile = Profile


@dataclass
class Capacity:
    Default: Optional[float]
    Maximum: Optional[float]
    Minimum: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Capacity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Capacity"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
            Maximum=json_data.get("Maximum"),
            Minimum=json_data.get("Minimum"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Capacity = Capacity


@dataclass
class FixedDate:
    End: Optional[str]
    Start: Optional[str]
    Timezone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FixedDate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FixedDate"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
            Timezone=json_data.get("Timezone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FixedDate = FixedDate


@dataclass
class Recurrence:
    Days: Optional[Sequence[str]]
    Hours: Optional[Sequence[float]]
    Minutes: Optional[Sequence[float]]
    Timezone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Recurrence"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Recurrence"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
            Hours=json_data.get("Hours"),
            Minutes=json_data.get("Minutes"),
            Timezone=json_data.get("Timezone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Recurrence = Recurrence


@dataclass
class Rule:
    MetricTrigger: Optional[Sequence["_MetricTrigger"]]
    ScaleAction: Optional[Sequence["_ScaleAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            MetricTrigger=json_data.get("MetricTrigger"),
            ScaleAction=json_data.get("ScaleAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class MetricTrigger:
    MetricName: Optional[str]
    MetricResourceId: Optional[str]
    Operator: Optional[str]
    Statistic: Optional[str]
    Threshold: Optional[float]
    TimeAggregation: Optional[str]
    TimeGrain: Optional[str]
    TimeWindow: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricTrigger"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricTrigger"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            MetricResourceId=json_data.get("MetricResourceId"),
            Operator=json_data.get("Operator"),
            Statistic=json_data.get("Statistic"),
            Threshold=json_data.get("Threshold"),
            TimeAggregation=json_data.get("TimeAggregation"),
            TimeGrain=json_data.get("TimeGrain"),
            TimeWindow=json_data.get("TimeWindow"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricTrigger = MetricTrigger


@dataclass
class ScaleAction:
    Cooldown: Optional[str]
    Direction: Optional[str]
    Type: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ScaleAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScaleAction"]:
        if not json_data:
            return None
        return cls(
            Cooldown=json_data.get("Cooldown"),
            Direction=json_data.get("Direction"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScaleAction = ScaleAction


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


