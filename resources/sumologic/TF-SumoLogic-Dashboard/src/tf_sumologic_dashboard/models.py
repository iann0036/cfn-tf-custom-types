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
    Description: Optional[str]
    FolderId: Optional[str]
    Id: Optional[str]
    RefreshInterval: Optional[float]
    Theme: Optional[str]
    Title: Optional[str]
    ColoringRule: Optional[Sequence["_ColoringRuleDefinition"]]
    Layout: Optional[Sequence["_LayoutDefinition"]]
    Panel: Optional[Sequence["_PanelDefinition"]]
    TimeRange: Optional[Sequence["_TimeRangeDefinition"]]
    TopologyLabelMap: Optional[Sequence["_TopologyLabelMapDefinition"]]
    Variable: Optional[Sequence["_VariableDefinition"]]

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
            Description=json_data.get("Description"),
            FolderId=json_data.get("FolderId"),
            Id=json_data.get("Id"),
            RefreshInterval=json_data.get("RefreshInterval"),
            Theme=json_data.get("Theme"),
            Title=json_data.get("Title"),
            ColoringRule=deserialize_list(json_data.get("ColoringRule"), ColoringRuleDefinition),
            Layout=deserialize_list(json_data.get("Layout"), LayoutDefinition),
            Panel=deserialize_list(json_data.get("Panel"), PanelDefinition),
            TimeRange=deserialize_list(json_data.get("TimeRange"), TimeRangeDefinition),
            TopologyLabelMap=deserialize_list(json_data.get("TopologyLabelMap"), TopologyLabelMapDefinition),
            Variable=deserialize_list(json_data.get("Variable"), VariableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ColoringRuleDefinition(BaseModel):
    MultipleSeriesAggregateFunction: Optional[str]
    Scope: Optional[str]
    SingleSeriesAggregateFunction: Optional[str]
    ColorThreshold: Optional[Sequence["_ColorThresholdDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ColoringRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColoringRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            MultipleSeriesAggregateFunction=json_data.get("MultipleSeriesAggregateFunction"),
            Scope=json_data.get("Scope"),
            SingleSeriesAggregateFunction=json_data.get("SingleSeriesAggregateFunction"),
            ColorThreshold=deserialize_list(json_data.get("ColorThreshold"), ColorThresholdDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColoringRuleDefinition = ColoringRuleDefinition


@dataclass
class ColorThresholdDefinition(BaseModel):
    Color: Optional[str]
    Max: Optional[float]
    Min: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ColorThresholdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColorThresholdDefinition"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColorThresholdDefinition = ColorThresholdDefinition


@dataclass
class LayoutDefinition(BaseModel):
    Grid: Optional[Sequence["_GridDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LayoutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LayoutDefinition"]:
        if not json_data:
            return None
        return cls(
            Grid=deserialize_list(json_data.get("Grid"), GridDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LayoutDefinition = LayoutDefinition


@dataclass
class GridDefinition(BaseModel):
    LayoutStructure: Optional[Sequence["_LayoutStructureDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GridDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GridDefinition"]:
        if not json_data:
            return None
        return cls(
            LayoutStructure=deserialize_list(json_data.get("LayoutStructure"), LayoutStructureDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GridDefinition = GridDefinition


@dataclass
class LayoutStructureDefinition(BaseModel):
    Key: Optional[str]
    Structure: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LayoutStructureDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LayoutStructureDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Structure=json_data.get("Structure"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LayoutStructureDefinition = LayoutStructureDefinition


@dataclass
class PanelDefinition(BaseModel):
    SumoSearchPanel: Optional[Sequence["_SumoSearchPanelDefinition"]]
    TextPanel: Optional[Sequence["_TextPanelDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PanelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PanelDefinition"]:
        if not json_data:
            return None
        return cls(
            SumoSearchPanel=deserialize_list(json_data.get("SumoSearchPanel"), SumoSearchPanelDefinition),
            TextPanel=deserialize_list(json_data.get("TextPanel"), TextPanelDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PanelDefinition = PanelDefinition


@dataclass
class SumoSearchPanelDefinition(BaseModel):
    Description: Optional[str]
    KeepVisualSettingsConsistentWithParent: Optional[bool]
    Key: Optional[str]
    Title: Optional[str]
    VisualSettings: Optional[str]
    ColoringRule: Optional[Sequence["_ColoringRuleDefinition"]]
    LinkedDashboard: Optional[Sequence["_LinkedDashboardDefinition"]]
    Query: Optional[Sequence["_QueryDefinition"]]
    TimeRange: Optional[Sequence["_TimeRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SumoSearchPanelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SumoSearchPanelDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            KeepVisualSettingsConsistentWithParent=json_data.get("KeepVisualSettingsConsistentWithParent"),
            Key=json_data.get("Key"),
            Title=json_data.get("Title"),
            VisualSettings=json_data.get("VisualSettings"),
            ColoringRule=deserialize_list(json_data.get("ColoringRule"), ColoringRuleDefinition),
            LinkedDashboard=deserialize_list(json_data.get("LinkedDashboard"), LinkedDashboardDefinition),
            Query=deserialize_list(json_data.get("Query"), QueryDefinition),
            TimeRange=deserialize_list(json_data.get("TimeRange"), TimeRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SumoSearchPanelDefinition = SumoSearchPanelDefinition


@dataclass
class LinkedDashboardDefinition(BaseModel):
    Id: Optional[str]
    IncludeTimeRange: Optional[bool]
    IncludeVariables: Optional[bool]
    RelativePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LinkedDashboardDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinkedDashboardDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            IncludeTimeRange=json_data.get("IncludeTimeRange"),
            IncludeVariables=json_data.get("IncludeVariables"),
            RelativePath=json_data.get("RelativePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinkedDashboardDefinition = LinkedDashboardDefinition


@dataclass
class QueryDefinition(BaseModel):
    MetricsQueryMode: Optional[str]
    QueryKey: Optional[str]
    QueryString: Optional[str]
    QueryType: Optional[str]
    MetricsQueryData: Optional[Sequence["_MetricsQueryDataDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryDefinition"]:
        if not json_data:
            return None
        return cls(
            MetricsQueryMode=json_data.get("MetricsQueryMode"),
            QueryKey=json_data.get("QueryKey"),
            QueryString=json_data.get("QueryString"),
            QueryType=json_data.get("QueryType"),
            MetricsQueryData=deserialize_list(json_data.get("MetricsQueryData"), MetricsQueryDataDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryDefinition = QueryDefinition


@dataclass
class MetricsQueryDataDefinition(BaseModel):
    AggregationType: Optional[str]
    GroupBy: Optional[str]
    Metric: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]
    Operator: Optional[Sequence["_OperatorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricsQueryDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricsQueryDataDefinition"]:
        if not json_data:
            return None
        return cls(
            AggregationType=json_data.get("AggregationType"),
            GroupBy=json_data.get("GroupBy"),
            Metric=json_data.get("Metric"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
            Operator=deserialize_list(json_data.get("Operator"), OperatorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricsQueryDataDefinition = MetricsQueryDataDefinition


@dataclass
class FilterDefinition(BaseModel):
    Key: Optional[str]
    Negation: Optional[bool]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Negation=json_data.get("Negation"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class OperatorDefinition(BaseModel):
    OperatorName: Optional[str]
    Parameter: Optional[Sequence["_ParameterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OperatorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OperatorDefinition"]:
        if not json_data:
            return None
        return cls(
            OperatorName=json_data.get("OperatorName"),
            Parameter=deserialize_list(json_data.get("Parameter"), ParameterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OperatorDefinition = OperatorDefinition


@dataclass
class ParameterDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterDefinition = ParameterDefinition


@dataclass
class TimeRangeDefinition(BaseModel):
    BeginBoundedTimeRange: Optional[Sequence["_BeginBoundedTimeRangeDefinition"]]
    CompleteLiteralTimeRange: Optional[Sequence["_CompleteLiteralTimeRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TimeRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            BeginBoundedTimeRange=deserialize_list(json_data.get("BeginBoundedTimeRange"), BeginBoundedTimeRangeDefinition),
            CompleteLiteralTimeRange=deserialize_list(json_data.get("CompleteLiteralTimeRange"), CompleteLiteralTimeRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeRangeDefinition = TimeRangeDefinition


@dataclass
class BeginBoundedTimeRangeDefinition(BaseModel):
    From: Optional[Sequence["_FromDefinition"]]
    To: Optional[Sequence["_ToDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BeginBoundedTimeRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BeginBoundedTimeRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            From=deserialize_list(json_data.get("From"), FromDefinition),
            To=deserialize_list(json_data.get("To"), ToDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BeginBoundedTimeRangeDefinition = BeginBoundedTimeRangeDefinition


@dataclass
class FromDefinition(BaseModel):
    EpochTimeRange: Optional[Sequence["_EpochTimeRangeDefinition"]]
    Iso8601TimeRange: Optional[Sequence["_Iso8601TimeRangeDefinition"]]
    LiteralTimeRange: Optional[Sequence["_LiteralTimeRangeDefinition"]]
    RelativeTimeRange: Optional[Sequence["_RelativeTimeRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FromDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FromDefinition"]:
        if not json_data:
            return None
        return cls(
            EpochTimeRange=deserialize_list(json_data.get("EpochTimeRange"), EpochTimeRangeDefinition),
            Iso8601TimeRange=deserialize_list(json_data.get("Iso8601TimeRange"), Iso8601TimeRangeDefinition),
            LiteralTimeRange=deserialize_list(json_data.get("LiteralTimeRange"), LiteralTimeRangeDefinition),
            RelativeTimeRange=deserialize_list(json_data.get("RelativeTimeRange"), RelativeTimeRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FromDefinition = FromDefinition


@dataclass
class EpochTimeRangeDefinition(BaseModel):
    EpochMillis: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EpochTimeRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EpochTimeRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            EpochMillis=json_data.get("EpochMillis"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EpochTimeRangeDefinition = EpochTimeRangeDefinition


@dataclass
class Iso8601TimeRangeDefinition(BaseModel):
    Iso8601Time: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Iso8601TimeRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Iso8601TimeRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Iso8601Time=json_data.get("Iso8601Time"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Iso8601TimeRangeDefinition = Iso8601TimeRangeDefinition


@dataclass
class LiteralTimeRangeDefinition(BaseModel):
    RangeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LiteralTimeRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LiteralTimeRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            RangeName=json_data.get("RangeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LiteralTimeRangeDefinition = LiteralTimeRangeDefinition


@dataclass
class RelativeTimeRangeDefinition(BaseModel):
    RelativeTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelativeTimeRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelativeTimeRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            RelativeTime=json_data.get("RelativeTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelativeTimeRangeDefinition = RelativeTimeRangeDefinition


@dataclass
class ToDefinition(BaseModel):
    EpochTimeRange: Optional[Sequence["_EpochTimeRangeDefinition"]]
    Iso8601TimeRange: Optional[Sequence["_Iso8601TimeRangeDefinition"]]
    LiteralTimeRange: Optional[Sequence["_LiteralTimeRangeDefinition"]]
    RelativeTimeRange: Optional[Sequence["_RelativeTimeRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ToDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ToDefinition"]:
        if not json_data:
            return None
        return cls(
            EpochTimeRange=deserialize_list(json_data.get("EpochTimeRange"), EpochTimeRangeDefinition),
            Iso8601TimeRange=deserialize_list(json_data.get("Iso8601TimeRange"), Iso8601TimeRangeDefinition),
            LiteralTimeRange=deserialize_list(json_data.get("LiteralTimeRange"), LiteralTimeRangeDefinition),
            RelativeTimeRange=deserialize_list(json_data.get("RelativeTimeRange"), RelativeTimeRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ToDefinition = ToDefinition


@dataclass
class CompleteLiteralTimeRangeDefinition(BaseModel):
    RangeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CompleteLiteralTimeRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CompleteLiteralTimeRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            RangeName=json_data.get("RangeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CompleteLiteralTimeRangeDefinition = CompleteLiteralTimeRangeDefinition


@dataclass
class TextPanelDefinition(BaseModel):
    KeepVisualSettingsConsistentWithParent: Optional[bool]
    Key: Optional[str]
    Text: Optional[str]
    Title: Optional[str]
    VisualSettings: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TextPanelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TextPanelDefinition"]:
        if not json_data:
            return None
        return cls(
            KeepVisualSettingsConsistentWithParent=json_data.get("KeepVisualSettingsConsistentWithParent"),
            Key=json_data.get("Key"),
            Text=json_data.get("Text"),
            Title=json_data.get("Title"),
            VisualSettings=json_data.get("VisualSettings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TextPanelDefinition = TextPanelDefinition


@dataclass
class TopologyLabelMapDefinition(BaseModel):
    Data: Optional[Sequence["_DataDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TopologyLabelMapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopologyLabelMapDefinition"]:
        if not json_data:
            return None
        return cls(
            Data=deserialize_list(json_data.get("Data"), DataDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopologyLabelMapDefinition = TopologyLabelMapDefinition


@dataclass
class DataDefinition(BaseModel):
    Label: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDefinition"]:
        if not json_data:
            return None
        return cls(
            Label=json_data.get("Label"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDefinition = DataDefinition


@dataclass
class VariableDefinition(BaseModel):
    AllowMultiSelect: Optional[bool]
    DefaultValue: Optional[str]
    DisplayName: Optional[str]
    HideFromUi: Optional[bool]
    IncludeAllOption: Optional[bool]
    Name: Optional[str]
    SourceDefinition: Optional[Sequence["_SourceDefinitionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VariableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VariableDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowMultiSelect=json_data.get("AllowMultiSelect"),
            DefaultValue=json_data.get("DefaultValue"),
            DisplayName=json_data.get("DisplayName"),
            HideFromUi=json_data.get("HideFromUi"),
            IncludeAllOption=json_data.get("IncludeAllOption"),
            Name=json_data.get("Name"),
            SourceDefinition=deserialize_list(json_data.get("SourceDefinition"), SourceDefinitionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VariableDefinition = VariableDefinition


@dataclass
class SourceDefinitionDefinition(BaseModel):
    CsvVariableSourceDefinition: Optional[Sequence["_CsvVariableSourceDefinitionDefinition"]]
    LogQueryVariableSourceDefinition: Optional[Sequence["_LogQueryVariableSourceDefinitionDefinition"]]
    MetadataVariableSourceDefinition: Optional[Sequence["_MetadataVariableSourceDefinitionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            CsvVariableSourceDefinition=deserialize_list(json_data.get("CsvVariableSourceDefinition"), CsvVariableSourceDefinitionDefinition),
            LogQueryVariableSourceDefinition=deserialize_list(json_data.get("LogQueryVariableSourceDefinition"), LogQueryVariableSourceDefinitionDefinition),
            MetadataVariableSourceDefinition=deserialize_list(json_data.get("MetadataVariableSourceDefinition"), MetadataVariableSourceDefinitionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinitionDefinition = SourceDefinitionDefinition


@dataclass
class CsvVariableSourceDefinitionDefinition(BaseModel):
    Values: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CsvVariableSourceDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CsvVariableSourceDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CsvVariableSourceDefinitionDefinition = CsvVariableSourceDefinitionDefinition


@dataclass
class LogQueryVariableSourceDefinitionDefinition(BaseModel):
    Field: Optional[str]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogQueryVariableSourceDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogQueryVariableSourceDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Field=json_data.get("Field"),
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogQueryVariableSourceDefinitionDefinition = LogQueryVariableSourceDefinitionDefinition


@dataclass
class MetadataVariableSourceDefinitionDefinition(BaseModel):
    Filter: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataVariableSourceDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataVariableSourceDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Filter=json_data.get("Filter"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataVariableSourceDefinitionDefinition = MetadataVariableSourceDefinitionDefinition


