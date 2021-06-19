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
    AlertRuleTemplateGuid: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    LogAnalyticsWorkspaceId: Optional[str]
    Name: Optional[str]
    Query: Optional[str]
    QueryFrequency: Optional[str]
    QueryPeriod: Optional[str]
    Severity: Optional[str]
    SuppressionDuration: Optional[str]
    SuppressionEnabled: Optional[bool]
    Tactics: Optional[Sequence[str]]
    TriggerOperator: Optional[str]
    TriggerThreshold: Optional[float]
    EventGrouping: Optional[Sequence["_EventGroupingDefinition"]]
    IncidentConfiguration: Optional[Sequence["_IncidentConfigurationDefinition"]]
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
            AlertRuleTemplateGuid=json_data.get("AlertRuleTemplateGuid"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            LogAnalyticsWorkspaceId=json_data.get("LogAnalyticsWorkspaceId"),
            Name=json_data.get("Name"),
            Query=json_data.get("Query"),
            QueryFrequency=json_data.get("QueryFrequency"),
            QueryPeriod=json_data.get("QueryPeriod"),
            Severity=json_data.get("Severity"),
            SuppressionDuration=json_data.get("SuppressionDuration"),
            SuppressionEnabled=json_data.get("SuppressionEnabled"),
            Tactics=json_data.get("Tactics"),
            TriggerOperator=json_data.get("TriggerOperator"),
            TriggerThreshold=json_data.get("TriggerThreshold"),
            EventGrouping=deserialize_list(json_data.get("EventGrouping"), EventGroupingDefinition),
            IncidentConfiguration=deserialize_list(json_data.get("IncidentConfiguration"), IncidentConfigurationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EventGroupingDefinition(BaseModel):
    AggregationMethod: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventGroupingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventGroupingDefinition"]:
        if not json_data:
            return None
        return cls(
            AggregationMethod=json_data.get("AggregationMethod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventGroupingDefinition = EventGroupingDefinition


@dataclass
class IncidentConfigurationDefinition(BaseModel):
    CreateIncident: Optional[bool]
    Grouping: Optional[Sequence["_GroupingDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IncidentConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IncidentConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            CreateIncident=json_data.get("CreateIncident"),
            Grouping=deserialize_list(json_data.get("Grouping"), GroupingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IncidentConfigurationDefinition = IncidentConfigurationDefinition


@dataclass
class GroupingDefinition(BaseModel):
    Enabled: Optional[bool]
    EntityMatchingMethod: Optional[str]
    GroupBy: Optional[Sequence[str]]
    LookbackDuration: Optional[str]
    ReopenClosedIncidents: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GroupingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupingDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            EntityMatchingMethod=json_data.get("EntityMatchingMethod"),
            GroupBy=json_data.get("GroupBy"),
            LookbackDuration=json_data.get("LookbackDuration"),
            ReopenClosedIncidents=json_data.get("ReopenClosedIncidents"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupingDefinition = GroupingDefinition


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


