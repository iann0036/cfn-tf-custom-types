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
    Combiner: Optional[str]
    CreationRecord: Optional[Sequence["_CreationRecord"]]
    DisplayName: Optional[str]
    Enabled: Optional[bool]
    Labels: Optional[Sequence[str]]
    Name: Optional[str]
    NotificationChannels: Optional[Sequence[str]]
    Project: Optional[str]
    UserLabels: Optional[Sequence["_UserLabels"]]
    Conditions: Optional[Sequence["_Conditions"]]
    Documentation: Optional[Sequence["_Documentation"]]
    Timeouts: Optional["_Timeouts"]
    ConditionAbsent: Optional[Sequence["_ConditionAbsent"]]
    ConditionThreshold: Optional[Sequence["_ConditionThreshold"]]
    Aggregations: Optional[Sequence["_Aggregations"]]
    Trigger: Optional[Sequence["_Trigger"]]
    DenominatorAggregations: Optional[Sequence["_DenominatorAggregations"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Combiner=json_data.get("Combiner"),
            CreationRecord=json_data.get("CreationRecord"),
            DisplayName=json_data.get("DisplayName"),
            Enabled=json_data.get("Enabled"),
            Labels=json_data.get("Labels"),
            Name=json_data.get("Name"),
            NotificationChannels=json_data.get("NotificationChannels"),
            Project=json_data.get("Project"),
            UserLabels=json_data.get("UserLabels"),
            Conditions=json_data.get("Conditions"),
            Documentation=json_data.get("Documentation"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            ConditionAbsent=json_data.get("ConditionAbsent"),
            ConditionThreshold=json_data.get("ConditionThreshold"),
            Aggregations=json_data.get("Aggregations"),
            Trigger=json_data.get("Trigger"),
            DenominatorAggregations=json_data.get("DenominatorAggregations"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CreationRecord:
    MutateTime: Optional[str]
    MutatedBy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CreationRecord"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreationRecord"]:
        if not json_data:
            return None
        return cls(
            MutateTime=json_data.get("MutateTime"),
            MutatedBy=json_data.get("MutatedBy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreationRecord = CreationRecord


@dataclass
class UserLabels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserLabels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserLabels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserLabels = UserLabels


@dataclass
class Conditions:
    DisplayName: Optional[str]
    ConditionAbsent: Optional[Sequence["_ConditionAbsent"]]
    ConditionThreshold: Optional[Sequence["_ConditionThreshold"]]

    @classmethod
    def _deserialize(
        cls: Type["_Conditions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Conditions"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            ConditionAbsent=json_data.get("ConditionAbsent"),
            ConditionThreshold=json_data.get("ConditionThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Conditions = Conditions


@dataclass
class ConditionAbsent:
    Duration: Optional[str]
    Filter: Optional[str]
    Aggregations: Optional[Sequence["_Aggregations"]]
    Trigger: Optional[Sequence["_Trigger"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionAbsent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionAbsent"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            Filter=json_data.get("Filter"),
            Aggregations=json_data.get("Aggregations"),
            Trigger=json_data.get("Trigger"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionAbsent = ConditionAbsent


@dataclass
class Aggregations:
    AlignmentPeriod: Optional[str]
    CrossSeriesReducer: Optional[str]
    GroupByFields: Optional[Sequence[str]]
    PerSeriesAligner: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Aggregations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Aggregations"]:
        if not json_data:
            return None
        return cls(
            AlignmentPeriod=json_data.get("AlignmentPeriod"),
            CrossSeriesReducer=json_data.get("CrossSeriesReducer"),
            GroupByFields=json_data.get("GroupByFields"),
            PerSeriesAligner=json_data.get("PerSeriesAligner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Aggregations = Aggregations


@dataclass
class Trigger:
    Count: Optional[float]
    Percent: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Trigger"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Trigger"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Percent=json_data.get("Percent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Trigger = Trigger


@dataclass
class ConditionThreshold:
    Comparison: Optional[str]
    DenominatorFilter: Optional[str]
    Duration: Optional[str]
    Filter: Optional[str]
    ThresholdValue: Optional[float]
    Aggregations: Optional[Sequence["_Aggregations"]]
    DenominatorAggregations: Optional[Sequence["_DenominatorAggregations"]]
    Trigger: Optional[Sequence["_Trigger"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionThreshold"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionThreshold"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            DenominatorFilter=json_data.get("DenominatorFilter"),
            Duration=json_data.get("Duration"),
            Filter=json_data.get("Filter"),
            ThresholdValue=json_data.get("ThresholdValue"),
            Aggregations=json_data.get("Aggregations"),
            DenominatorAggregations=json_data.get("DenominatorAggregations"),
            Trigger=json_data.get("Trigger"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionThreshold = ConditionThreshold


@dataclass
class DenominatorAggregations:
    AlignmentPeriod: Optional[str]
    CrossSeriesReducer: Optional[str]
    GroupByFields: Optional[Sequence[str]]
    PerSeriesAligner: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DenominatorAggregations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DenominatorAggregations"]:
        if not json_data:
            return None
        return cls(
            AlignmentPeriod=json_data.get("AlignmentPeriod"),
            CrossSeriesReducer=json_data.get("CrossSeriesReducer"),
            GroupByFields=json_data.get("GroupByFields"),
            PerSeriesAligner=json_data.get("PerSeriesAligner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DenominatorAggregations = DenominatorAggregations


@dataclass
class Documentation:
    Content: Optional[str]
    MimeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Documentation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Documentation"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            MimeType=json_data.get("MimeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Documentation = Documentation


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


