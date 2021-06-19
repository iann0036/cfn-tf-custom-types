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
    Tags: Optional[Sequence["_TagsDefinition"]]
    Throttling: Optional[float]
    TimeWindow: Optional[float]
    Action: Optional[Sequence["_ActionDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    Trigger: Optional[Sequence["_TriggerDefinition"]]

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
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Throttling=json_data.get("Throttling"),
            TimeWindow=json_data.get("TimeWindow"),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            Trigger=deserialize_list(json_data.get("Trigger"), TriggerDefinition),
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
class ActionDefinition(BaseModel):
    ActionGroup: Optional[Sequence[str]]
    CustomWebhookPayload: Optional[str]
    EmailSubject: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionGroup=json_data.get("ActionGroup"),
            CustomWebhookPayload=json_data.get("CustomWebhookPayload"),
            EmailSubject=json_data.get("EmailSubject"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


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


@dataclass
class TriggerDefinition(BaseModel):
    Operator: Optional[str]
    Threshold: Optional[float]
    MetricTrigger: Optional[Sequence["_MetricTriggerDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TriggerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggerDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Threshold=json_data.get("Threshold"),
            MetricTrigger=deserialize_list(json_data.get("MetricTrigger"), MetricTriggerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TriggerDefinition = TriggerDefinition


@dataclass
class MetricTriggerDefinition(BaseModel):
    MetricColumn: Optional[str]
    MetricTriggerType: Optional[str]
    Operator: Optional[str]
    Threshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MetricTriggerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricTriggerDefinition"]:
        if not json_data:
            return None
        return cls(
            MetricColumn=json_data.get("MetricColumn"),
            MetricTriggerType=json_data.get("MetricTriggerType"),
            Operator=json_data.get("Operator"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricTriggerDefinition = MetricTriggerDefinition


