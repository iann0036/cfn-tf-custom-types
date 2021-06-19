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
    DashboardLists: Optional[Sequence[float]]
    DashboardListsRemoved: Optional[Sequence[float]]
    Description: Optional[str]
    Id: Optional[str]
    IsReadOnly: Optional[bool]
    LayoutType: Optional[str]
    NotifyList: Optional[Sequence[str]]
    ReflowType: Optional[str]
    RestrictedRoles: Optional[Sequence[str]]
    Title: Optional[str]
    Url: Optional[str]
    TemplateVariable: Optional[Sequence["_TemplateVariableDefinition"]]
    TemplateVariablePreset: Optional[Sequence["_TemplateVariablePresetDefinition"]]
    Widget: Optional[Sequence["_WidgetDefinition"]]

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
            DashboardLists=json_data.get("DashboardLists"),
            DashboardListsRemoved=json_data.get("DashboardListsRemoved"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IsReadOnly=json_data.get("IsReadOnly"),
            LayoutType=json_data.get("LayoutType"),
            NotifyList=json_data.get("NotifyList"),
            ReflowType=json_data.get("ReflowType"),
            RestrictedRoles=json_data.get("RestrictedRoles"),
            Title=json_data.get("Title"),
            Url=json_data.get("Url"),
            TemplateVariable=deserialize_list(json_data.get("TemplateVariable"), TemplateVariableDefinition),
            TemplateVariablePreset=deserialize_list(json_data.get("TemplateVariablePreset"), TemplateVariablePresetDefinition),
            Widget=deserialize_list(json_data.get("Widget"), WidgetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TemplateVariableDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateVariableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateVariableDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateVariableDefinition = TemplateVariableDefinition


@dataclass
class TemplateVariablePresetDefinition(BaseModel):
    Name: Optional[str]
    TemplateVariable: Optional[Sequence["_TemplateVariableDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateVariablePresetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateVariablePresetDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            TemplateVariable=deserialize_list(json_data.get("TemplateVariable"), TemplateVariableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateVariablePresetDefinition = TemplateVariablePresetDefinition


@dataclass
class WidgetDefinition(BaseModel):
    AlertGraphDefinition: Optional[Sequence["_AlertGraphDefinitionDefinition"]]
    AlertValueDefinition: Optional[Sequence["_AlertValueDefinitionDefinition"]]
    ChangeDefinition: Optional[Sequence["_ChangeDefinitionDefinition"]]
    CheckStatusDefinition: Optional[Sequence["_CheckStatusDefinitionDefinition"]]
    DistributionDefinition: Optional[Sequence["_DistributionDefinitionDefinition"]]
    EventStreamDefinition: Optional[Sequence["_EventStreamDefinitionDefinition"]]
    EventTimelineDefinition: Optional[Sequence["_EventTimelineDefinitionDefinition"]]
    FreeTextDefinition: Optional[Sequence["_FreeTextDefinitionDefinition"]]
    GeomapDefinition: Optional[Sequence["_GeomapDefinitionDefinition"]]
    HeatmapDefinition: Optional[Sequence["_HeatmapDefinitionDefinition"]]
    HostmapDefinition: Optional[Sequence["_HostmapDefinitionDefinition"]]
    IframeDefinition: Optional[Sequence["_IframeDefinitionDefinition"]]
    ImageDefinition: Optional[Sequence["_ImageDefinitionDefinition"]]
    LogStreamDefinition: Optional[Sequence["_LogStreamDefinitionDefinition"]]
    ManageStatusDefinition: Optional[Sequence["_ManageStatusDefinitionDefinition"]]
    NoteDefinition: Optional[Sequence["_NoteDefinitionDefinition"]]
    QueryTableDefinition: Optional[Sequence["_QueryTableDefinitionDefinition"]]
    QueryValueDefinition: Optional[Sequence["_QueryValueDefinitionDefinition"]]
    ScatterplotDefinition: Optional[Sequence["_ScatterplotDefinitionDefinition"]]
    ServiceLevelObjectiveDefinition: Optional[Sequence["_ServiceLevelObjectiveDefinitionDefinition"]]
    ServicemapDefinition: Optional[Sequence["_ServicemapDefinitionDefinition"]]
    TimeseriesDefinition: Optional[Sequence["_TimeseriesDefinitionDefinition"]]
    ToplistDefinition: Optional[Sequence["_ToplistDefinitionDefinition"]]
    TraceServiceDefinition: Optional[Sequence["_TraceServiceDefinitionDefinition"]]
    WidgetLayout: Optional[Sequence["_WidgetLayoutDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WidgetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WidgetDefinition"]:
        if not json_data:
            return None
        return cls(
            AlertGraphDefinition=deserialize_list(json_data.get("AlertGraphDefinition"), AlertGraphDefinitionDefinition),
            AlertValueDefinition=deserialize_list(json_data.get("AlertValueDefinition"), AlertValueDefinitionDefinition),
            ChangeDefinition=deserialize_list(json_data.get("ChangeDefinition"), ChangeDefinitionDefinition),
            CheckStatusDefinition=deserialize_list(json_data.get("CheckStatusDefinition"), CheckStatusDefinitionDefinition),
            DistributionDefinition=deserialize_list(json_data.get("DistributionDefinition"), DistributionDefinitionDefinition),
            EventStreamDefinition=deserialize_list(json_data.get("EventStreamDefinition"), EventStreamDefinitionDefinition),
            EventTimelineDefinition=deserialize_list(json_data.get("EventTimelineDefinition"), EventTimelineDefinitionDefinition),
            FreeTextDefinition=deserialize_list(json_data.get("FreeTextDefinition"), FreeTextDefinitionDefinition),
            GeomapDefinition=deserialize_list(json_data.get("GeomapDefinition"), GeomapDefinitionDefinition),
            HeatmapDefinition=deserialize_list(json_data.get("HeatmapDefinition"), HeatmapDefinitionDefinition),
            HostmapDefinition=deserialize_list(json_data.get("HostmapDefinition"), HostmapDefinitionDefinition),
            IframeDefinition=deserialize_list(json_data.get("IframeDefinition"), IframeDefinitionDefinition),
            ImageDefinition=deserialize_list(json_data.get("ImageDefinition"), ImageDefinitionDefinition),
            LogStreamDefinition=deserialize_list(json_data.get("LogStreamDefinition"), LogStreamDefinitionDefinition),
            ManageStatusDefinition=deserialize_list(json_data.get("ManageStatusDefinition"), ManageStatusDefinitionDefinition),
            NoteDefinition=deserialize_list(json_data.get("NoteDefinition"), NoteDefinitionDefinition),
            QueryTableDefinition=deserialize_list(json_data.get("QueryTableDefinition"), QueryTableDefinitionDefinition),
            QueryValueDefinition=deserialize_list(json_data.get("QueryValueDefinition"), QueryValueDefinitionDefinition),
            ScatterplotDefinition=deserialize_list(json_data.get("ScatterplotDefinition"), ScatterplotDefinitionDefinition),
            ServiceLevelObjectiveDefinition=deserialize_list(json_data.get("ServiceLevelObjectiveDefinition"), ServiceLevelObjectiveDefinitionDefinition),
            ServicemapDefinition=deserialize_list(json_data.get("ServicemapDefinition"), ServicemapDefinitionDefinition),
            TimeseriesDefinition=deserialize_list(json_data.get("TimeseriesDefinition"), TimeseriesDefinitionDefinition),
            ToplistDefinition=deserialize_list(json_data.get("ToplistDefinition"), ToplistDefinitionDefinition),
            TraceServiceDefinition=deserialize_list(json_data.get("TraceServiceDefinition"), TraceServiceDefinitionDefinition),
            WidgetLayout=deserialize_list(json_data.get("WidgetLayout"), WidgetLayoutDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WidgetDefinition = WidgetDefinition


@dataclass
class AlertGraphDefinitionDefinition(BaseModel):
    AlertId: Optional[str]
    LiveSpan: Optional[str]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    VizType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AlertGraphDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlertGraphDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            AlertId=json_data.get("AlertId"),
            LiveSpan=json_data.get("LiveSpan"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            VizType=json_data.get("VizType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlertGraphDefinitionDefinition = AlertGraphDefinitionDefinition


@dataclass
class AlertValueDefinitionDefinition(BaseModel):
    AlertId: Optional[str]
    Precision: Optional[float]
    TextAlign: Optional[str]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AlertValueDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlertValueDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            AlertId=json_data.get("AlertId"),
            Precision=json_data.get("Precision"),
            TextAlign=json_data.get("TextAlign"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlertValueDefinitionDefinition = AlertValueDefinitionDefinition


@dataclass
class ChangeDefinitionDefinition(BaseModel):
    LiveSpan: Optional[str]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    CustomLink: Optional[Sequence["_CustomLinkDefinition"]]
    Request: Optional[Sequence["_RequestDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ChangeDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChangeDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            LiveSpan=json_data.get("LiveSpan"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            CustomLink=deserialize_list(json_data.get("CustomLink"), CustomLinkDefinition),
            Request=deserialize_list(json_data.get("Request"), RequestDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChangeDefinitionDefinition = ChangeDefinitionDefinition


@dataclass
class CustomLinkDefinition(BaseModel):
    IsHidden: Optional[bool]
    Label: Optional[str]
    Link: Optional[str]
    OverrideLabel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomLinkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomLinkDefinition"]:
        if not json_data:
            return None
        return cls(
            IsHidden=json_data.get("IsHidden"),
            Label=json_data.get("Label"),
            Link=json_data.get("Link"),
            OverrideLabel=json_data.get("OverrideLabel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomLinkDefinition = CustomLinkDefinition


@dataclass
class RequestDefinition(BaseModel):
    Q: Optional[str]
    ApmQuery: Optional[Sequence["_ApmQueryDefinition"]]
    ConditionalFormats: Optional[Sequence["_ConditionalFormatsDefinition"]]
    Formula: Optional[Sequence["_FormulaDefinition"]]
    LogQuery: Optional[Sequence["_LogQueryDefinition"]]
    ProcessQuery: Optional[Sequence["_ProcessQueryDefinition"]]
    Query: Optional[Sequence["_QueryDefinition"]]
    RumQuery: Optional[Sequence["_RumQueryDefinition"]]
    SecurityQuery: Optional[Sequence["_SecurityQueryDefinition"]]
    Style: Optional[Sequence["_StyleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RequestDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestDefinition"]:
        if not json_data:
            return None
        return cls(
            Q=json_data.get("Q"),
            ApmQuery=deserialize_list(json_data.get("ApmQuery"), ApmQueryDefinition),
            ConditionalFormats=deserialize_list(json_data.get("ConditionalFormats"), ConditionalFormatsDefinition),
            Formula=deserialize_list(json_data.get("Formula"), FormulaDefinition),
            LogQuery=deserialize_list(json_data.get("LogQuery"), LogQueryDefinition),
            ProcessQuery=deserialize_list(json_data.get("ProcessQuery"), ProcessQueryDefinition),
            Query=deserialize_list(json_data.get("Query"), QueryDefinition),
            RumQuery=deserialize_list(json_data.get("RumQuery"), RumQueryDefinition),
            SecurityQuery=deserialize_list(json_data.get("SecurityQuery"), SecurityQueryDefinition),
            Style=deserialize_list(json_data.get("Style"), StyleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestDefinition = RequestDefinition


@dataclass
class ApmQueryDefinition(BaseModel):
    Index: Optional[str]
    SearchQuery: Optional[str]
    ComputeQuery: Optional[Sequence["_ComputeQueryDefinition"]]
    GroupBy: Optional[Sequence["_GroupByDefinition"]]
    MultiCompute: Optional[Sequence["_MultiComputeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApmQueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApmQueryDefinition"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            SearchQuery=json_data.get("SearchQuery"),
            ComputeQuery=deserialize_list(json_data.get("ComputeQuery"), ComputeQueryDefinition),
            GroupBy=deserialize_list(json_data.get("GroupBy"), GroupByDefinition),
            MultiCompute=deserialize_list(json_data.get("MultiCompute"), MultiComputeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApmQueryDefinition = ApmQueryDefinition


@dataclass
class ComputeQueryDefinition(BaseModel):
    Aggregation: Optional[str]
    Facet: Optional[str]
    Interval: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ComputeQueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComputeQueryDefinition"]:
        if not json_data:
            return None
        return cls(
            Aggregation=json_data.get("Aggregation"),
            Facet=json_data.get("Facet"),
            Interval=json_data.get("Interval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComputeQueryDefinition = ComputeQueryDefinition


@dataclass
class GroupByDefinition(BaseModel):
    Facet: Optional[str]
    Limit: Optional[float]
    Sort: Optional[Sequence["_SortDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GroupByDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupByDefinition"]:
        if not json_data:
            return None
        return cls(
            Facet=json_data.get("Facet"),
            Limit=json_data.get("Limit"),
            Sort=deserialize_list(json_data.get("Sort"), SortDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupByDefinition = GroupByDefinition


@dataclass
class SortDefinition(BaseModel):
    Aggregation: Optional[str]
    Metric: Optional[str]
    Order: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SortDefinition"]:
        if not json_data:
            return None
        return cls(
            Aggregation=json_data.get("Aggregation"),
            Metric=json_data.get("Metric"),
            Order=json_data.get("Order"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SortDefinition = SortDefinition


@dataclass
class MultiComputeDefinition(BaseModel):
    Aggregation: Optional[str]
    Facet: Optional[str]
    Interval: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MultiComputeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultiComputeDefinition"]:
        if not json_data:
            return None
        return cls(
            Aggregation=json_data.get("Aggregation"),
            Facet=json_data.get("Facet"),
            Interval=json_data.get("Interval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultiComputeDefinition = MultiComputeDefinition


@dataclass
class ConditionalFormatsDefinition(BaseModel):
    Comparator: Optional[str]
    CustomBgColor: Optional[str]
    CustomFgColor: Optional[str]
    HideValue: Optional[bool]
    ImageUrl: Optional[str]
    Metric: Optional[str]
    Palette: Optional[str]
    Timeframe: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionalFormatsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionalFormatsDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparator=json_data.get("Comparator"),
            CustomBgColor=json_data.get("CustomBgColor"),
            CustomFgColor=json_data.get("CustomFgColor"),
            HideValue=json_data.get("HideValue"),
            ImageUrl=json_data.get("ImageUrl"),
            Metric=json_data.get("Metric"),
            Palette=json_data.get("Palette"),
            Timeframe=json_data.get("Timeframe"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionalFormatsDefinition = ConditionalFormatsDefinition


@dataclass
class FormulaDefinition(BaseModel):
    Alias: Optional[str]
    FormulaExpression: Optional[str]
    Limit: Optional[Sequence["_LimitDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FormulaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FormulaDefinition"]:
        if not json_data:
            return None
        return cls(
            Alias=json_data.get("Alias"),
            FormulaExpression=json_data.get("FormulaExpression"),
            Limit=deserialize_list(json_data.get("Limit"), LimitDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FormulaDefinition = FormulaDefinition


@dataclass
class LimitDefinition(BaseModel):
    Count: Optional[float]
    Order: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LimitDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Order=json_data.get("Order"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LimitDefinition = LimitDefinition


@dataclass
class LogQueryDefinition(BaseModel):
    Index: Optional[str]
    SearchQuery: Optional[str]
    ComputeQuery: Optional[Sequence["_ComputeQueryDefinition"]]
    GroupBy: Optional[Sequence["_GroupByDefinition"]]
    MultiCompute: Optional[Sequence["_MultiComputeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LogQueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogQueryDefinition"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            SearchQuery=json_data.get("SearchQuery"),
            ComputeQuery=deserialize_list(json_data.get("ComputeQuery"), ComputeQueryDefinition),
            GroupBy=deserialize_list(json_data.get("GroupBy"), GroupByDefinition),
            MultiCompute=deserialize_list(json_data.get("MultiCompute"), MultiComputeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogQueryDefinition = LogQueryDefinition


@dataclass
class ProcessQueryDefinition(BaseModel):
    Aggregator: Optional[str]
    DataSource: Optional[str]
    IsNormalizedCpu: Optional[bool]
    Limit: Optional[float]
    Metric: Optional[str]
    Name: Optional[str]
    Sort: Optional[str]
    TagFilters: Optional[Sequence[str]]
    TextFilter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessQueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessQueryDefinition"]:
        if not json_data:
            return None
        return cls(
            Aggregator=json_data.get("Aggregator"),
            DataSource=json_data.get("DataSource"),
            IsNormalizedCpu=json_data.get("IsNormalizedCpu"),
            Limit=json_data.get("Limit"),
            Metric=json_data.get("Metric"),
            Name=json_data.get("Name"),
            Sort=json_data.get("Sort"),
            TagFilters=json_data.get("TagFilters"),
            TextFilter=json_data.get("TextFilter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessQueryDefinition = ProcessQueryDefinition


@dataclass
class QueryDefinition(BaseModel):
    EventQuery: Optional[Sequence["_EventQueryDefinition"]]
    MetricQuery: Optional[Sequence["_MetricQueryDefinition"]]
    ProcessQuery: Optional[Sequence["_ProcessQueryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryDefinition"]:
        if not json_data:
            return None
        return cls(
            EventQuery=deserialize_list(json_data.get("EventQuery"), EventQueryDefinition),
            MetricQuery=deserialize_list(json_data.get("MetricQuery"), MetricQueryDefinition),
            ProcessQuery=deserialize_list(json_data.get("ProcessQuery"), ProcessQueryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryDefinition = QueryDefinition


@dataclass
class EventQueryDefinition(BaseModel):
    DataSource: Optional[str]
    Indexes: Optional[Sequence[str]]
    Name: Optional[str]
    Compute: Optional[Sequence["_ComputeDefinition"]]
    GroupBy: Optional[Sequence["_GroupByDefinition"]]
    Search: Optional[Sequence["_SearchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EventQueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventQueryDefinition"]:
        if not json_data:
            return None
        return cls(
            DataSource=json_data.get("DataSource"),
            Indexes=json_data.get("Indexes"),
            Name=json_data.get("Name"),
            Compute=deserialize_list(json_data.get("Compute"), ComputeDefinition),
            GroupBy=deserialize_list(json_data.get("GroupBy"), GroupByDefinition),
            Search=deserialize_list(json_data.get("Search"), SearchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventQueryDefinition = EventQueryDefinition


@dataclass
class ComputeDefinition(BaseModel):
    Aggregation: Optional[str]
    Interval: Optional[float]
    Metric: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComputeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComputeDefinition"]:
        if not json_data:
            return None
        return cls(
            Aggregation=json_data.get("Aggregation"),
            Interval=json_data.get("Interval"),
            Metric=json_data.get("Metric"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComputeDefinition = ComputeDefinition


@dataclass
class SearchDefinition(BaseModel):
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SearchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SearchDefinition"]:
        if not json_data:
            return None
        return cls(
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SearchDefinition = SearchDefinition


@dataclass
class MetricQueryDefinition(BaseModel):
    Aggregator: Optional[str]
    DataSource: Optional[str]
    Name: Optional[str]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricQueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricQueryDefinition"]:
        if not json_data:
            return None
        return cls(
            Aggregator=json_data.get("Aggregator"),
            DataSource=json_data.get("DataSource"),
            Name=json_data.get("Name"),
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricQueryDefinition = MetricQueryDefinition


@dataclass
class RumQueryDefinition(BaseModel):
    Index: Optional[str]
    SearchQuery: Optional[str]
    ComputeQuery: Optional[Sequence["_ComputeQueryDefinition"]]
    GroupBy: Optional[Sequence["_GroupByDefinition"]]
    MultiCompute: Optional[Sequence["_MultiComputeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RumQueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RumQueryDefinition"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            SearchQuery=json_data.get("SearchQuery"),
            ComputeQuery=deserialize_list(json_data.get("ComputeQuery"), ComputeQueryDefinition),
            GroupBy=deserialize_list(json_data.get("GroupBy"), GroupByDefinition),
            MultiCompute=deserialize_list(json_data.get("MultiCompute"), MultiComputeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RumQueryDefinition = RumQueryDefinition


@dataclass
class SecurityQueryDefinition(BaseModel):
    Index: Optional[str]
    SearchQuery: Optional[str]
    ComputeQuery: Optional[Sequence["_ComputeQueryDefinition"]]
    GroupBy: Optional[Sequence["_GroupByDefinition"]]
    MultiCompute: Optional[Sequence["_MultiComputeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityQueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityQueryDefinition"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            SearchQuery=json_data.get("SearchQuery"),
            ComputeQuery=deserialize_list(json_data.get("ComputeQuery"), ComputeQueryDefinition),
            GroupBy=deserialize_list(json_data.get("GroupBy"), GroupByDefinition),
            MultiCompute=deserialize_list(json_data.get("MultiCompute"), MultiComputeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityQueryDefinition = SecurityQueryDefinition


@dataclass
class StyleDefinition(BaseModel):
    Palette: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StyleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StyleDefinition"]:
        if not json_data:
            return None
        return cls(
            Palette=json_data.get("Palette"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StyleDefinition = StyleDefinition


@dataclass
class CheckStatusDefinitionDefinition(BaseModel):
    Check: Optional[str]
    Group: Optional[str]
    GroupBy: Optional[Sequence[str]]
    Grouping: Optional[str]
    LiveSpan: Optional[str]
    Tags: Optional[Sequence[str]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CheckStatusDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CheckStatusDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Check=json_data.get("Check"),
            Group=json_data.get("Group"),
            GroupBy=json_data.get("GroupBy"),
            Grouping=json_data.get("Grouping"),
            LiveSpan=json_data.get("LiveSpan"),
            Tags=json_data.get("Tags"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CheckStatusDefinitionDefinition = CheckStatusDefinitionDefinition


@dataclass
class DistributionDefinitionDefinition(BaseModel):
    LegendSize: Optional[str]
    LiveSpan: Optional[str]
    ShowLegend: Optional[bool]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    Request: Optional[Sequence["_RequestDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DistributionDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DistributionDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            LegendSize=json_data.get("LegendSize"),
            LiveSpan=json_data.get("LiveSpan"),
            ShowLegend=json_data.get("ShowLegend"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            Request=deserialize_list(json_data.get("Request"), RequestDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DistributionDefinitionDefinition = DistributionDefinitionDefinition


@dataclass
class EventStreamDefinitionDefinition(BaseModel):
    EventSize: Optional[str]
    LiveSpan: Optional[str]
    Query: Optional[str]
    TagsExecution: Optional[str]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventStreamDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventStreamDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            EventSize=json_data.get("EventSize"),
            LiveSpan=json_data.get("LiveSpan"),
            Query=json_data.get("Query"),
            TagsExecution=json_data.get("TagsExecution"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventStreamDefinitionDefinition = EventStreamDefinitionDefinition


@dataclass
class EventTimelineDefinitionDefinition(BaseModel):
    LiveSpan: Optional[str]
    Query: Optional[str]
    TagsExecution: Optional[str]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventTimelineDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventTimelineDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            LiveSpan=json_data.get("LiveSpan"),
            Query=json_data.get("Query"),
            TagsExecution=json_data.get("TagsExecution"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventTimelineDefinitionDefinition = EventTimelineDefinitionDefinition


@dataclass
class FreeTextDefinitionDefinition(BaseModel):
    Color: Optional[str]
    FontSize: Optional[str]
    Text: Optional[str]
    TextAlign: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeTextDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeTextDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
            FontSize=json_data.get("FontSize"),
            Text=json_data.get("Text"),
            TextAlign=json_data.get("TextAlign"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeTextDefinitionDefinition = FreeTextDefinitionDefinition


@dataclass
class GeomapDefinitionDefinition(BaseModel):
    LiveSpan: Optional[str]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    CustomLink: Optional[Sequence["_CustomLinkDefinition"]]
    Request: Optional[Sequence["_RequestDefinition"]]
    Style: Optional[Sequence["_StyleDefinition"]]
    View: Optional[Sequence["_ViewDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GeomapDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeomapDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            LiveSpan=json_data.get("LiveSpan"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            CustomLink=deserialize_list(json_data.get("CustomLink"), CustomLinkDefinition),
            Request=deserialize_list(json_data.get("Request"), RequestDefinition),
            Style=deserialize_list(json_data.get("Style"), StyleDefinition),
            View=deserialize_list(json_data.get("View"), ViewDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeomapDefinitionDefinition = GeomapDefinitionDefinition


@dataclass
class ViewDefinition(BaseModel):
    Focus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ViewDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ViewDefinition"]:
        if not json_data:
            return None
        return cls(
            Focus=json_data.get("Focus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ViewDefinition = ViewDefinition


@dataclass
class HeatmapDefinitionDefinition(BaseModel):
    LegendSize: Optional[str]
    LiveSpan: Optional[str]
    ShowLegend: Optional[bool]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    CustomLink: Optional[Sequence["_CustomLinkDefinition"]]
    Event: Optional[Sequence["_EventDefinition"]]
    Request: Optional[Sequence["_RequestDefinition"]]
    Yaxis: Optional[Sequence["_YaxisDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HeatmapDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeatmapDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            LegendSize=json_data.get("LegendSize"),
            LiveSpan=json_data.get("LiveSpan"),
            ShowLegend=json_data.get("ShowLegend"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            CustomLink=deserialize_list(json_data.get("CustomLink"), CustomLinkDefinition),
            Event=deserialize_list(json_data.get("Event"), EventDefinition),
            Request=deserialize_list(json_data.get("Request"), RequestDefinition),
            Yaxis=deserialize_list(json_data.get("Yaxis"), YaxisDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeatmapDefinitionDefinition = HeatmapDefinitionDefinition


@dataclass
class EventDefinition(BaseModel):
    Q: Optional[str]
    TagsExecution: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventDefinition"]:
        if not json_data:
            return None
        return cls(
            Q=json_data.get("Q"),
            TagsExecution=json_data.get("TagsExecution"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventDefinition = EventDefinition


@dataclass
class YaxisDefinition(BaseModel):
    IncludeZero: Optional[bool]
    Label: Optional[str]
    Max: Optional[str]
    Min: Optional[str]
    Scale: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_YaxisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_YaxisDefinition"]:
        if not json_data:
            return None
        return cls(
            IncludeZero=json_data.get("IncludeZero"),
            Label=json_data.get("Label"),
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
            Scale=json_data.get("Scale"),
        )


# work around possible type aliasing issues when variable has same name as a model
_YaxisDefinition = YaxisDefinition


@dataclass
class HostmapDefinitionDefinition(BaseModel):
    Group: Optional[Sequence[str]]
    NoGroupHosts: Optional[bool]
    NoMetricHosts: Optional[bool]
    NodeType: Optional[str]
    Scope: Optional[Sequence[str]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    CustomLink: Optional[Sequence["_CustomLinkDefinition"]]
    Request: Optional[Sequence["_RequestDefinition"]]
    Style: Optional[Sequence["_StyleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HostmapDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostmapDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Group=json_data.get("Group"),
            NoGroupHosts=json_data.get("NoGroupHosts"),
            NoMetricHosts=json_data.get("NoMetricHosts"),
            NodeType=json_data.get("NodeType"),
            Scope=json_data.get("Scope"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            CustomLink=deserialize_list(json_data.get("CustomLink"), CustomLinkDefinition),
            Request=deserialize_list(json_data.get("Request"), RequestDefinition),
            Style=deserialize_list(json_data.get("Style"), StyleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostmapDefinitionDefinition = HostmapDefinitionDefinition


@dataclass
class IframeDefinitionDefinition(BaseModel):
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IframeDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IframeDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IframeDefinitionDefinition = IframeDefinitionDefinition


@dataclass
class ImageDefinitionDefinition(BaseModel):
    HasBackground: Optional[bool]
    HasBorder: Optional[bool]
    HorizontalAlign: Optional[str]
    Margin: Optional[str]
    Sizing: Optional[str]
    Url: Optional[str]
    UrlDarkTheme: Optional[str]
    VerticalAlign: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImageDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            HasBackground=json_data.get("HasBackground"),
            HasBorder=json_data.get("HasBorder"),
            HorizontalAlign=json_data.get("HorizontalAlign"),
            Margin=json_data.get("Margin"),
            Sizing=json_data.get("Sizing"),
            Url=json_data.get("Url"),
            UrlDarkTheme=json_data.get("UrlDarkTheme"),
            VerticalAlign=json_data.get("VerticalAlign"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageDefinitionDefinition = ImageDefinitionDefinition


@dataclass
class LogStreamDefinitionDefinition(BaseModel):
    Columns: Optional[Sequence[str]]
    Indexes: Optional[Sequence[str]]
    LiveSpan: Optional[str]
    MessageDisplay: Optional[str]
    Query: Optional[str]
    ShowDateColumn: Optional[bool]
    ShowMessageColumn: Optional[bool]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    Sort: Optional[Sequence["_SortDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LogStreamDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogStreamDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Columns=json_data.get("Columns"),
            Indexes=json_data.get("Indexes"),
            LiveSpan=json_data.get("LiveSpan"),
            MessageDisplay=json_data.get("MessageDisplay"),
            Query=json_data.get("Query"),
            ShowDateColumn=json_data.get("ShowDateColumn"),
            ShowMessageColumn=json_data.get("ShowMessageColumn"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            Sort=deserialize_list(json_data.get("Sort"), SortDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogStreamDefinitionDefinition = LogStreamDefinitionDefinition


@dataclass
class ManageStatusDefinitionDefinition(BaseModel):
    ColorPreference: Optional[str]
    DisplayFormat: Optional[str]
    HideZeroCounts: Optional[bool]
    Query: Optional[str]
    ShowLastTriggered: Optional[bool]
    Sort: Optional[str]
    SummaryType: Optional[str]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManageStatusDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManageStatusDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            ColorPreference=json_data.get("ColorPreference"),
            DisplayFormat=json_data.get("DisplayFormat"),
            HideZeroCounts=json_data.get("HideZeroCounts"),
            Query=json_data.get("Query"),
            ShowLastTriggered=json_data.get("ShowLastTriggered"),
            Sort=json_data.get("Sort"),
            SummaryType=json_data.get("SummaryType"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManageStatusDefinitionDefinition = ManageStatusDefinitionDefinition


@dataclass
class NoteDefinitionDefinition(BaseModel):
    BackgroundColor: Optional[str]
    Content: Optional[str]
    FontSize: Optional[str]
    HasPadding: Optional[bool]
    ShowTick: Optional[bool]
    TextAlign: Optional[str]
    TickEdge: Optional[str]
    TickPos: Optional[str]
    VerticalAlign: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NoteDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NoteDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            BackgroundColor=json_data.get("BackgroundColor"),
            Content=json_data.get("Content"),
            FontSize=json_data.get("FontSize"),
            HasPadding=json_data.get("HasPadding"),
            ShowTick=json_data.get("ShowTick"),
            TextAlign=json_data.get("TextAlign"),
            TickEdge=json_data.get("TickEdge"),
            TickPos=json_data.get("TickPos"),
            VerticalAlign=json_data.get("VerticalAlign"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NoteDefinitionDefinition = NoteDefinitionDefinition


@dataclass
class QueryTableDefinitionDefinition(BaseModel):
    HasSearchBar: Optional[str]
    LiveSpan: Optional[str]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    CustomLink: Optional[Sequence["_CustomLinkDefinition"]]
    Request: Optional[Sequence["_RequestDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryTableDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryTableDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            HasSearchBar=json_data.get("HasSearchBar"),
            LiveSpan=json_data.get("LiveSpan"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            CustomLink=deserialize_list(json_data.get("CustomLink"), CustomLinkDefinition),
            Request=deserialize_list(json_data.get("Request"), RequestDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryTableDefinitionDefinition = QueryTableDefinitionDefinition


@dataclass
class QueryValueDefinitionDefinition(BaseModel):
    Autoscale: Optional[bool]
    CustomUnit: Optional[str]
    LiveSpan: Optional[str]
    Precision: Optional[float]
    TextAlign: Optional[str]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    CustomLink: Optional[Sequence["_CustomLinkDefinition"]]
    Request: Optional[Sequence["_RequestDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryValueDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryValueDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Autoscale=json_data.get("Autoscale"),
            CustomUnit=json_data.get("CustomUnit"),
            LiveSpan=json_data.get("LiveSpan"),
            Precision=json_data.get("Precision"),
            TextAlign=json_data.get("TextAlign"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            CustomLink=deserialize_list(json_data.get("CustomLink"), CustomLinkDefinition),
            Request=deserialize_list(json_data.get("Request"), RequestDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryValueDefinitionDefinition = QueryValueDefinitionDefinition


@dataclass
class ScatterplotDefinitionDefinition(BaseModel):
    ColorByGroups: Optional[Sequence[str]]
    LiveSpan: Optional[str]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    CustomLink: Optional[Sequence["_CustomLinkDefinition"]]
    Request: Optional[Sequence["_RequestDefinition"]]
    Xaxis: Optional[Sequence["_XaxisDefinition"]]
    Yaxis: Optional[Sequence["_YaxisDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScatterplotDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScatterplotDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            ColorByGroups=json_data.get("ColorByGroups"),
            LiveSpan=json_data.get("LiveSpan"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            CustomLink=deserialize_list(json_data.get("CustomLink"), CustomLinkDefinition),
            Request=deserialize_list(json_data.get("Request"), RequestDefinition),
            Xaxis=deserialize_list(json_data.get("Xaxis"), XaxisDefinition),
            Yaxis=deserialize_list(json_data.get("Yaxis"), YaxisDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScatterplotDefinitionDefinition = ScatterplotDefinitionDefinition


@dataclass
class XaxisDefinition(BaseModel):
    IncludeZero: Optional[bool]
    Label: Optional[str]
    Max: Optional[str]
    Min: Optional[str]
    Scale: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_XaxisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_XaxisDefinition"]:
        if not json_data:
            return None
        return cls(
            IncludeZero=json_data.get("IncludeZero"),
            Label=json_data.get("Label"),
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
            Scale=json_data.get("Scale"),
        )


# work around possible type aliasing issues when variable has same name as a model
_XaxisDefinition = XaxisDefinition


@dataclass
class ServiceLevelObjectiveDefinitionDefinition(BaseModel):
    GlobalTimeTarget: Optional[str]
    ShowErrorBudget: Optional[bool]
    SloId: Optional[str]
    TimeWindows: Optional[Sequence[str]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    ViewMode: Optional[str]
    ViewType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceLevelObjectiveDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceLevelObjectiveDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            GlobalTimeTarget=json_data.get("GlobalTimeTarget"),
            ShowErrorBudget=json_data.get("ShowErrorBudget"),
            SloId=json_data.get("SloId"),
            TimeWindows=json_data.get("TimeWindows"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            ViewMode=json_data.get("ViewMode"),
            ViewType=json_data.get("ViewType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceLevelObjectiveDefinitionDefinition = ServiceLevelObjectiveDefinitionDefinition


@dataclass
class ServicemapDefinitionDefinition(BaseModel):
    Filters: Optional[Sequence[str]]
    Service: Optional[str]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    CustomLink: Optional[Sequence["_CustomLinkDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServicemapDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicemapDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Filters=json_data.get("Filters"),
            Service=json_data.get("Service"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            CustomLink=deserialize_list(json_data.get("CustomLink"), CustomLinkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicemapDefinitionDefinition = ServicemapDefinitionDefinition


@dataclass
class TimeseriesDefinitionDefinition(BaseModel):
    LegendColumns: Optional[Sequence[str]]
    LegendLayout: Optional[str]
    LegendSize: Optional[str]
    LiveSpan: Optional[str]
    ShowLegend: Optional[bool]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    CustomLink: Optional[Sequence["_CustomLinkDefinition"]]
    Event: Optional[Sequence["_EventDefinition"]]
    Marker: Optional[Sequence["_MarkerDefinition"]]
    Request: Optional[Sequence["_RequestDefinition"]]
    RightYaxis: Optional[Sequence["_RightYaxisDefinition"]]
    Yaxis: Optional[Sequence["_YaxisDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TimeseriesDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeseriesDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            LegendColumns=json_data.get("LegendColumns"),
            LegendLayout=json_data.get("LegendLayout"),
            LegendSize=json_data.get("LegendSize"),
            LiveSpan=json_data.get("LiveSpan"),
            ShowLegend=json_data.get("ShowLegend"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            CustomLink=deserialize_list(json_data.get("CustomLink"), CustomLinkDefinition),
            Event=deserialize_list(json_data.get("Event"), EventDefinition),
            Marker=deserialize_list(json_data.get("Marker"), MarkerDefinition),
            Request=deserialize_list(json_data.get("Request"), RequestDefinition),
            RightYaxis=deserialize_list(json_data.get("RightYaxis"), RightYaxisDefinition),
            Yaxis=deserialize_list(json_data.get("Yaxis"), YaxisDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeseriesDefinitionDefinition = TimeseriesDefinitionDefinition


@dataclass
class MarkerDefinition(BaseModel):
    DisplayType: Optional[str]
    Label: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MarkerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkerDefinition"]:
        if not json_data:
            return None
        return cls(
            DisplayType=json_data.get("DisplayType"),
            Label=json_data.get("Label"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkerDefinition = MarkerDefinition


@dataclass
class RightYaxisDefinition(BaseModel):
    IncludeZero: Optional[bool]
    Label: Optional[str]
    Max: Optional[str]
    Min: Optional[str]
    Scale: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RightYaxisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RightYaxisDefinition"]:
        if not json_data:
            return None
        return cls(
            IncludeZero=json_data.get("IncludeZero"),
            Label=json_data.get("Label"),
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
            Scale=json_data.get("Scale"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RightYaxisDefinition = RightYaxisDefinition


@dataclass
class ToplistDefinitionDefinition(BaseModel):
    LiveSpan: Optional[str]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    CustomLink: Optional[Sequence["_CustomLinkDefinition"]]
    Request: Optional[Sequence["_RequestDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ToplistDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ToplistDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            LiveSpan=json_data.get("LiveSpan"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            CustomLink=deserialize_list(json_data.get("CustomLink"), CustomLinkDefinition),
            Request=deserialize_list(json_data.get("Request"), RequestDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ToplistDefinitionDefinition = ToplistDefinitionDefinition


@dataclass
class TraceServiceDefinitionDefinition(BaseModel):
    DisplayFormat: Optional[str]
    Env: Optional[str]
    LiveSpan: Optional[str]
    Service: Optional[str]
    ShowBreakdown: Optional[bool]
    ShowDistribution: Optional[bool]
    ShowErrors: Optional[bool]
    ShowHits: Optional[bool]
    ShowLatency: Optional[bool]
    ShowResourceList: Optional[bool]
    SizeFormat: Optional[str]
    SpanName: Optional[str]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TraceServiceDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TraceServiceDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            DisplayFormat=json_data.get("DisplayFormat"),
            Env=json_data.get("Env"),
            LiveSpan=json_data.get("LiveSpan"),
            Service=json_data.get("Service"),
            ShowBreakdown=json_data.get("ShowBreakdown"),
            ShowDistribution=json_data.get("ShowDistribution"),
            ShowErrors=json_data.get("ShowErrors"),
            ShowHits=json_data.get("ShowHits"),
            ShowLatency=json_data.get("ShowLatency"),
            ShowResourceList=json_data.get("ShowResourceList"),
            SizeFormat=json_data.get("SizeFormat"),
            SpanName=json_data.get("SpanName"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TraceServiceDefinitionDefinition = TraceServiceDefinitionDefinition


@dataclass
class WidgetLayoutDefinition(BaseModel):
    Height: Optional[float]
    IsColumnBreak: Optional[bool]
    Width: Optional[float]
    X: Optional[float]
    Y: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WidgetLayoutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WidgetLayoutDefinition"]:
        if not json_data:
            return None
        return cls(
            Height=json_data.get("Height"),
            IsColumnBreak=json_data.get("IsColumnBreak"),
            Width=json_data.get("Width"),
            X=json_data.get("X"),
            Y=json_data.get("Y"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WidgetLayoutDefinition = WidgetLayoutDefinition


