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
    AutoMitigate: Optional[bool]
    Description: Optional[str]
    Enabled: Optional[bool]
    Frequency: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Scopes: Optional[Sequence[str]]
    Severity: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TargetResourceLocation: Optional[str]
    TargetResourceType: Optional[str]
    WindowSize: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    ApplicationInsightsWebTestLocationAvailabilityCriteria: Optional[Sequence["_ApplicationInsightsWebTestLocationAvailabilityCriteriaDefinition"]]
    Criteria: Optional[Sequence["_CriteriaDefinition"]]
    DynamicCriteria: Optional[Sequence["_DynamicCriteriaDefinition"]]
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
            AutoMitigate=json_data.get("AutoMitigate"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Frequency=json_data.get("Frequency"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Scopes=json_data.get("Scopes"),
            Severity=json_data.get("Severity"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TargetResourceLocation=json_data.get("TargetResourceLocation"),
            TargetResourceType=json_data.get("TargetResourceType"),
            WindowSize=json_data.get("WindowSize"),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            ApplicationInsightsWebTestLocationAvailabilityCriteria=deserialize_list(json_data.get("ApplicationInsightsWebTestLocationAvailabilityCriteria"), ApplicationInsightsWebTestLocationAvailabilityCriteriaDefinition),
            Criteria=deserialize_list(json_data.get("Criteria"), CriteriaDefinition),
            DynamicCriteria=deserialize_list(json_data.get("DynamicCriteria"), DynamicCriteriaDefinition),
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
class ActionDefinition(BaseModel):
    ActionGroupId: Optional[str]
    WebhookProperties: Optional[Sequence["_WebhookPropertiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionGroupId=json_data.get("ActionGroupId"),
            WebhookProperties=deserialize_list(json_data.get("WebhookProperties"), WebhookPropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class WebhookPropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebhookPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebhookPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebhookPropertiesDefinition = WebhookPropertiesDefinition


@dataclass
class ApplicationInsightsWebTestLocationAvailabilityCriteriaDefinition(BaseModel):
    ComponentId: Optional[str]
    FailedLocationCount: Optional[float]
    WebTestId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationInsightsWebTestLocationAvailabilityCriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationInsightsWebTestLocationAvailabilityCriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            ComponentId=json_data.get("ComponentId"),
            FailedLocationCount=json_data.get("FailedLocationCount"),
            WebTestId=json_data.get("WebTestId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationInsightsWebTestLocationAvailabilityCriteriaDefinition = ApplicationInsightsWebTestLocationAvailabilityCriteriaDefinition


@dataclass
class CriteriaDefinition(BaseModel):
    Aggregation: Optional[str]
    MetricName: Optional[str]
    MetricNamespace: Optional[str]
    Operator: Optional[str]
    SkipMetricValidation: Optional[bool]
    Threshold: Optional[float]
    Dimension: Optional[Sequence["_DimensionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            Aggregation=json_data.get("Aggregation"),
            MetricName=json_data.get("MetricName"),
            MetricNamespace=json_data.get("MetricNamespace"),
            Operator=json_data.get("Operator"),
            SkipMetricValidation=json_data.get("SkipMetricValidation"),
            Threshold=json_data.get("Threshold"),
            Dimension=deserialize_list(json_data.get("Dimension"), DimensionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CriteriaDefinition = CriteriaDefinition


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
class DynamicCriteriaDefinition(BaseModel):
    Aggregation: Optional[str]
    AlertSensitivity: Optional[str]
    EvaluationFailureCount: Optional[float]
    EvaluationTotalCount: Optional[float]
    IgnoreDataBefore: Optional[str]
    MetricName: Optional[str]
    MetricNamespace: Optional[str]
    Operator: Optional[str]
    SkipMetricValidation: Optional[bool]
    Dimension: Optional[Sequence["_DimensionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicCriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicCriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            Aggregation=json_data.get("Aggregation"),
            AlertSensitivity=json_data.get("AlertSensitivity"),
            EvaluationFailureCount=json_data.get("EvaluationFailureCount"),
            EvaluationTotalCount=json_data.get("EvaluationTotalCount"),
            IgnoreDataBefore=json_data.get("IgnoreDataBefore"),
            MetricName=json_data.get("MetricName"),
            MetricNamespace=json_data.get("MetricNamespace"),
            Operator=json_data.get("Operator"),
            SkipMetricValidation=json_data.get("SkipMetricValidation"),
            Dimension=deserialize_list(json_data.get("Dimension"), DimensionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicCriteriaDefinition = DynamicCriteriaDefinition


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


