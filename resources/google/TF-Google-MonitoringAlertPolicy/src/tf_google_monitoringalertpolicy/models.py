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
    Combiner: Optional[str]
    CreationRecord: Optional[Sequence["_CreationRecordDefinition"]]
    DisplayName: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    NotificationChannels: Optional[Sequence[str]]
    Project: Optional[str]
    UserLabels: Optional[Sequence["_UserLabelsDefinition"]]
    Conditions: Optional[Sequence["_ConditionsDefinition"]]
    Documentation: Optional[Sequence["_DocumentationDefinition"]]
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
            Combiner=json_data.get("Combiner"),
            CreationRecord=deserialize_list(json_data.get("CreationRecord"), CreationRecordDefinition),
            DisplayName=json_data.get("DisplayName"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NotificationChannels=json_data.get("NotificationChannels"),
            Project=json_data.get("Project"),
            UserLabels=deserialize_list(json_data.get("UserLabels"), UserLabelsDefinition),
            Conditions=deserialize_list(json_data.get("Conditions"), ConditionsDefinition),
            Documentation=deserialize_list(json_data.get("Documentation"), DocumentationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CreationRecordDefinition(BaseModel):
    MutateTime: Optional[str]
    MutatedBy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CreationRecordDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreationRecordDefinition"]:
        if not json_data:
            return None
        return cls(
            MutateTime=json_data.get("MutateTime"),
            MutatedBy=json_data.get("MutatedBy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreationRecordDefinition = CreationRecordDefinition


@dataclass
class UserLabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserLabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserLabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserLabelsDefinition = UserLabelsDefinition


@dataclass
class ConditionsDefinition(BaseModel):
    DisplayName: Optional[str]
    ConditionAbsent: Optional[Sequence["_ConditionAbsentDefinition"]]
    ConditionMonitoringQueryLanguage: Optional[Sequence["_ConditionMonitoringQueryLanguageDefinition"]]
    ConditionThreshold: Optional[Sequence["_ConditionThresholdDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            ConditionAbsent=deserialize_list(json_data.get("ConditionAbsent"), ConditionAbsentDefinition),
            ConditionMonitoringQueryLanguage=deserialize_list(json_data.get("ConditionMonitoringQueryLanguage"), ConditionMonitoringQueryLanguageDefinition),
            ConditionThreshold=deserialize_list(json_data.get("ConditionThreshold"), ConditionThresholdDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionsDefinition = ConditionsDefinition


@dataclass
class ConditionAbsentDefinition(BaseModel):
    Duration: Optional[str]
    Filter: Optional[str]
    Aggregations: Optional[Sequence["_AggregationsDefinition"]]
    Trigger: Optional[Sequence["_TriggerDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionAbsentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionAbsentDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            Filter=json_data.get("Filter"),
            Aggregations=deserialize_list(json_data.get("Aggregations"), AggregationsDefinition),
            Trigger=deserialize_list(json_data.get("Trigger"), TriggerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionAbsentDefinition = ConditionAbsentDefinition


@dataclass
class AggregationsDefinition(BaseModel):
    AlignmentPeriod: Optional[str]
    CrossSeriesReducer: Optional[str]
    GroupByFields: Optional[Sequence[str]]
    PerSeriesAligner: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AggregationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggregationsDefinition"]:
        if not json_data:
            return None
        return cls(
            AlignmentPeriod=json_data.get("AlignmentPeriod"),
            CrossSeriesReducer=json_data.get("CrossSeriesReducer"),
            GroupByFields=json_data.get("GroupByFields"),
            PerSeriesAligner=json_data.get("PerSeriesAligner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggregationsDefinition = AggregationsDefinition


@dataclass
class TriggerDefinition(BaseModel):
    Count: Optional[float]
    Percent: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TriggerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggerDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Percent=json_data.get("Percent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TriggerDefinition = TriggerDefinition


@dataclass
class ConditionMonitoringQueryLanguageDefinition(BaseModel):
    Duration: Optional[str]
    Query: Optional[str]
    Trigger: Optional[Sequence["_TriggerDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionMonitoringQueryLanguageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionMonitoringQueryLanguageDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            Query=json_data.get("Query"),
            Trigger=deserialize_list(json_data.get("Trigger"), TriggerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionMonitoringQueryLanguageDefinition = ConditionMonitoringQueryLanguageDefinition


@dataclass
class ConditionThresholdDefinition(BaseModel):
    Comparison: Optional[str]
    DenominatorFilter: Optional[str]
    Duration: Optional[str]
    Filter: Optional[str]
    ThresholdValue: Optional[float]
    Aggregations: Optional[Sequence["_AggregationsDefinition"]]
    DenominatorAggregations: Optional[Sequence["_DenominatorAggregationsDefinition"]]
    Trigger: Optional[Sequence["_TriggerDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionThresholdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionThresholdDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            DenominatorFilter=json_data.get("DenominatorFilter"),
            Duration=json_data.get("Duration"),
            Filter=json_data.get("Filter"),
            ThresholdValue=json_data.get("ThresholdValue"),
            Aggregations=deserialize_list(json_data.get("Aggregations"), AggregationsDefinition),
            DenominatorAggregations=deserialize_list(json_data.get("DenominatorAggregations"), DenominatorAggregationsDefinition),
            Trigger=deserialize_list(json_data.get("Trigger"), TriggerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionThresholdDefinition = ConditionThresholdDefinition


@dataclass
class DenominatorAggregationsDefinition(BaseModel):
    AlignmentPeriod: Optional[str]
    CrossSeriesReducer: Optional[str]
    GroupByFields: Optional[Sequence[str]]
    PerSeriesAligner: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DenominatorAggregationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DenominatorAggregationsDefinition"]:
        if not json_data:
            return None
        return cls(
            AlignmentPeriod=json_data.get("AlignmentPeriod"),
            CrossSeriesReducer=json_data.get("CrossSeriesReducer"),
            GroupByFields=json_data.get("GroupByFields"),
            PerSeriesAligner=json_data.get("PerSeriesAligner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DenominatorAggregationsDefinition = DenominatorAggregationsDefinition


@dataclass
class DocumentationDefinition(BaseModel):
    Content: Optional[str]
    MimeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DocumentationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DocumentationDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            MimeType=json_data.get("MimeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DocumentationDefinition = DocumentationDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


