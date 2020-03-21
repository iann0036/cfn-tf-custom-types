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
    AuthorizedResourceIds: Optional[Sequence[str]]
    DataSourceId: Optional[str]
    Description: Optional[str]
    Enabled: Optional[bool]
    Frequency: Optional[float]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    Query: Optional[str]
    QueryType: Optional[str]
    ResourceGroupName: Optional[str]
    Severity: Optional[float]
    Tags: Optional[Sequence["_Tags"]]
    Throttling: Optional[float]
    TimeWindow: Optional[float]
    Action: Optional[Sequence["_Action"]]
    Timeouts: Optional["_Timeouts"]
    Trigger: Optional[Sequence["_Trigger"]]
    MetricTrigger: Optional[Sequence["_MetricTrigger"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AuthorizedResourceIds=json_data.get("AuthorizedResourceIds"),
            DataSourceId=json_data.get("DataSourceId"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Frequency=json_data.get("Frequency"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Query=json_data.get("Query"),
            QueryType=json_data.get("QueryType"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Severity=json_data.get("Severity"),
            Tags=json_data.get("Tags"),
            Throttling=json_data.get("Throttling"),
            TimeWindow=json_data.get("TimeWindow"),
            Action=json_data.get("Action"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Trigger=json_data.get("Trigger"),
            MetricTrigger=json_data.get("MetricTrigger"),
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
class Action:
    ActionGroup: Optional[Sequence[str]]
    CustomWebhookPayload: Optional[str]
    EmailSubject: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            ActionGroup=json_data.get("ActionGroup"),
            CustomWebhookPayload=json_data.get("CustomWebhookPayload"),
            EmailSubject=json_data.get("EmailSubject"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


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


@dataclass
class Trigger:
    Operator: Optional[str]
    Threshold: Optional[float]
    MetricTrigger: Optional[Sequence["_MetricTrigger"]]

    @classmethod
    def _deserialize(
        cls: Type["_Trigger"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Trigger"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Threshold=json_data.get("Threshold"),
            MetricTrigger=json_data.get("MetricTrigger"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Trigger = Trigger


@dataclass
class MetricTrigger:
    MetricColumn: Optional[str]
    MetricTriggerType: Optional[str]
    Operator: Optional[str]
    Threshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MetricTrigger"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricTrigger"]:
        if not json_data:
            return None
        return cls(
            MetricColumn=json_data.get("MetricColumn"),
            MetricTriggerType=json_data.get("MetricTriggerType"),
            Operator=json_data.get("Operator"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricTrigger = MetricTrigger


