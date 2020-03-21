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
    Description: Optional[str]
    IsReadOnly: Optional[bool]
    LayoutType: Optional[str]
    NotifyList: Optional[Sequence[str]]
    Title: Optional[str]
    TemplateVariable: Optional[Sequence["_TemplateVariable"]]
    TemplateVariablePreset: Optional[Sequence["_TemplateVariablePreset"]]
    Widget: Optional[Sequence["_Widget"]]
    AlertGraphDefinition: Optional[Sequence["_AlertGraphDefinition"]]
    AlertValueDefinition: Optional[Sequence["_AlertValueDefinition"]]
    ChangeDefinition: Optional[Sequence["_ChangeDefinition"]]
    CheckStatusDefinition: Optional[Sequence["_CheckStatusDefinition"]]
    DistributionDefinition: Optional[Sequence["_DistributionDefinition"]]
    EventStreamDefinition: Optional[Sequence["_EventStreamDefinition"]]
    EventTimelineDefinition: Optional[Sequence["_EventTimelineDefinition"]]
    FreeTextDefinition: Optional[Sequence["_FreeTextDefinition"]]
    GroupDefinition: Optional[Sequence["_GroupDefinition"]]
    HeatmapDefinition: Optional[Sequence["_HeatmapDefinition"]]
    HostmapDefinition: Optional[Sequence["_HostmapDefinition"]]
    IframeDefinition: Optional[Sequence["_IframeDefinition"]]
    ImageDefinition: Optional[Sequence["_ImageDefinition"]]
    LogStreamDefinition: Optional[Sequence["_LogStreamDefinition"]]
    ManageStatusDefinition: Optional[Sequence["_ManageStatusDefinition"]]
    NoteDefinition: Optional[Sequence["_NoteDefinition"]]
    QueryTableDefinition: Optional[Sequence["_QueryTableDefinition"]]
    QueryValueDefinition: Optional[Sequence["_QueryValueDefinition"]]
    ScatterplotDefinition: Optional[Sequence["_ScatterplotDefinition"]]
    ServiceLevelObjectiveDefinition: Optional[Sequence["_ServiceLevelObjectiveDefinition"]]
    TimeseriesDefinition: Optional[Sequence["_TimeseriesDefinition"]]
    ToplistDefinition: Optional[Sequence["_ToplistDefinition"]]
    TraceServiceDefinition: Optional[Sequence["_TraceServiceDefinition"]]
    Request: Optional[Sequence["_Request"]]
    Yaxis: Optional[Sequence["_Yaxis"]]
    Style: Optional[Sequence["_Style"]]
    Xaxis: Optional[Sequence["_Xaxis"]]
    Event: Optional[Sequence["_Event"]]
    Marker: Optional[Sequence["_Marker"]]
    ApmQuery: Optional[Sequence["_ApmQuery"]]
    ConditionalFormats: Optional[Sequence["_ConditionalFormats"]]
    LogQuery: Optional[Sequence["_LogQuery"]]
    ProcessQuery: Optional[Sequence["_ProcessQuery"]]
    GroupBy: Optional[Sequence["_GroupBy"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            IsReadOnly=json_data.get("IsReadOnly"),
            LayoutType=json_data.get("LayoutType"),
            NotifyList=json_data.get("NotifyList"),
            Title=json_data.get("Title"),
            TemplateVariable=json_data.get("TemplateVariable"),
            TemplateVariablePreset=json_data.get("TemplateVariablePreset"),
            Widget=json_data.get("Widget"),
            AlertGraphDefinition=json_data.get("AlertGraphDefinition"),
            AlertValueDefinition=json_data.get("AlertValueDefinition"),
            ChangeDefinition=json_data.get("ChangeDefinition"),
            CheckStatusDefinition=json_data.get("CheckStatusDefinition"),
            DistributionDefinition=json_data.get("DistributionDefinition"),
            EventStreamDefinition=json_data.get("EventStreamDefinition"),
            EventTimelineDefinition=json_data.get("EventTimelineDefinition"),
            FreeTextDefinition=json_data.get("FreeTextDefinition"),
            GroupDefinition=json_data.get("GroupDefinition"),
            HeatmapDefinition=json_data.get("HeatmapDefinition"),
            HostmapDefinition=json_data.get("HostmapDefinition"),
            IframeDefinition=json_data.get("IframeDefinition"),
            ImageDefinition=json_data.get("ImageDefinition"),
            LogStreamDefinition=json_data.get("LogStreamDefinition"),
            ManageStatusDefinition=json_data.get("ManageStatusDefinition"),
            NoteDefinition=json_data.get("NoteDefinition"),
            QueryTableDefinition=json_data.get("QueryTableDefinition"),
            QueryValueDefinition=json_data.get("QueryValueDefinition"),
            ScatterplotDefinition=json_data.get("ScatterplotDefinition"),
            ServiceLevelObjectiveDefinition=json_data.get("ServiceLevelObjectiveDefinition"),
            TimeseriesDefinition=json_data.get("TimeseriesDefinition"),
            ToplistDefinition=json_data.get("ToplistDefinition"),
            TraceServiceDefinition=json_data.get("TraceServiceDefinition"),
            Request=json_data.get("Request"),
            Yaxis=json_data.get("Yaxis"),
            Style=json_data.get("Style"),
            Xaxis=json_data.get("Xaxis"),
            Event=json_data.get("Event"),
            Marker=json_data.get("Marker"),
            ApmQuery=json_data.get("ApmQuery"),
            ConditionalFormats=json_data.get("ConditionalFormats"),
            LogQuery=json_data.get("LogQuery"),
            ProcessQuery=json_data.get("ProcessQuery"),
            GroupBy=json_data.get("GroupBy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TemplateVariable:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateVariable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateVariable"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateVariable = TemplateVariable


@dataclass
class TemplateVariablePreset:
    Name: Optional[str]
    TemplateVariable: Optional[Sequence["_TemplateVariable"]]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateVariablePreset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateVariablePreset"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            TemplateVariable=json_data.get("TemplateVariable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateVariablePreset = TemplateVariablePreset


@dataclass
class Widget:
    Layout: Optional[Sequence["_Layout"]]
    AlertGraphDefinition: Optional[Sequence["_AlertGraphDefinition"]]
    AlertValueDefinition: Optional[Sequence["_AlertValueDefinition"]]
    ChangeDefinition: Optional[Sequence["_ChangeDefinition"]]
    CheckStatusDefinition: Optional[Sequence["_CheckStatusDefinition"]]
    DistributionDefinition: Optional[Sequence["_DistributionDefinition"]]
    EventStreamDefinition: Optional[Sequence["_EventStreamDefinition"]]
    EventTimelineDefinition: Optional[Sequence["_EventTimelineDefinition"]]
    FreeTextDefinition: Optional[Sequence["_FreeTextDefinition"]]
    HeatmapDefinition: Optional[Sequence["_HeatmapDefinition"]]
    HostmapDefinition: Optional[Sequence["_HostmapDefinition"]]
    IframeDefinition: Optional[Sequence["_IframeDefinition"]]
    ImageDefinition: Optional[Sequence["_ImageDefinition"]]
    LogStreamDefinition: Optional[Sequence["_LogStreamDefinition"]]
    ManageStatusDefinition: Optional[Sequence["_ManageStatusDefinition"]]
    NoteDefinition: Optional[Sequence["_NoteDefinition"]]
    QueryTableDefinition: Optional[Sequence["_QueryTableDefinition"]]
    QueryValueDefinition: Optional[Sequence["_QueryValueDefinition"]]
    ScatterplotDefinition: Optional[Sequence["_ScatterplotDefinition"]]
    ServiceLevelObjectiveDefinition: Optional[Sequence["_ServiceLevelObjectiveDefinition"]]
    TimeseriesDefinition: Optional[Sequence["_TimeseriesDefinition"]]
    ToplistDefinition: Optional[Sequence["_ToplistDefinition"]]
    TraceServiceDefinition: Optional[Sequence["_TraceServiceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Widget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Widget"]:
        if not json_data:
            return None
        return cls(
            Layout=json_data.get("Layout"),
            AlertGraphDefinition=json_data.get("AlertGraphDefinition"),
            AlertValueDefinition=json_data.get("AlertValueDefinition"),
            ChangeDefinition=json_data.get("ChangeDefinition"),
            CheckStatusDefinition=json_data.get("CheckStatusDefinition"),
            DistributionDefinition=json_data.get("DistributionDefinition"),
            EventStreamDefinition=json_data.get("EventStreamDefinition"),
            EventTimelineDefinition=json_data.get("EventTimelineDefinition"),
            FreeTextDefinition=json_data.get("FreeTextDefinition"),
            HeatmapDefinition=json_data.get("HeatmapDefinition"),
            HostmapDefinition=json_data.get("HostmapDefinition"),
            IframeDefinition=json_data.get("IframeDefinition"),
            ImageDefinition=json_data.get("ImageDefinition"),
            LogStreamDefinition=json_data.get("LogStreamDefinition"),
            ManageStatusDefinition=json_data.get("ManageStatusDefinition"),
            NoteDefinition=json_data.get("NoteDefinition"),
            QueryTableDefinition=json_data.get("QueryTableDefinition"),
            QueryValueDefinition=json_data.get("QueryValueDefinition"),
            ScatterplotDefinition=json_data.get("ScatterplotDefinition"),
            ServiceLevelObjectiveDefinition=json_data.get("ServiceLevelObjectiveDefinition"),
            TimeseriesDefinition=json_data.get("TimeseriesDefinition"),
            ToplistDefinition=json_data.get("ToplistDefinition"),
            TraceServiceDefinition=json_data.get("TraceServiceDefinition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Widget = Widget


@dataclass
class Layout:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Layout"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Layout"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Layout = Layout


@dataclass
class AlertGraphDefinition:
    AlertId: Optional[str]
    Time: Optional[Sequence["_Time"]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    VizType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AlertGraphDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlertGraphDefinition"]:
        if not json_data:
            return None
        return cls(
            AlertId=json_data.get("AlertId"),
            Time=json_data.get("Time"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            VizType=json_data.get("VizType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlertGraphDefinition = AlertGraphDefinition


@dataclass
class Time:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Time"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Time"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Time = Time


@dataclass
class AlertValueDefinition:
    AlertId: Optional[str]
    Precision: Optional[float]
    TextAlign: Optional[str]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AlertValueDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlertValueDefinition"]:
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
_AlertValueDefinition = AlertValueDefinition


@dataclass
class ChangeDefinition:
    Time: Optional[Sequence["_Time2"]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    Request: Optional[Sequence["_Request"]]

    @classmethod
    def _deserialize(
        cls: Type["_ChangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Time=json_data.get("Time"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            Request=json_data.get("Request"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChangeDefinition = ChangeDefinition


@dataclass
class Time2:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Time2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Time2"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Time2 = Time2


@dataclass
class Request:
    Q: Optional[str]
    ApmQuery: Optional[Sequence["_ApmQuery"]]
    ConditionalFormats: Optional[Sequence["_ConditionalFormats"]]
    LogQuery: Optional[Sequence["_LogQuery"]]
    ProcessQuery: Optional[Sequence["_ProcessQuery"]]
    Style: Optional[Sequence["_Style"]]

    @classmethod
    def _deserialize(
        cls: Type["_Request"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Request"]:
        if not json_data:
            return None
        return cls(
            Q=json_data.get("Q"),
            ApmQuery=json_data.get("ApmQuery"),
            ConditionalFormats=json_data.get("ConditionalFormats"),
            LogQuery=json_data.get("LogQuery"),
            ProcessQuery=json_data.get("ProcessQuery"),
            Style=json_data.get("Style"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Request = Request


@dataclass
class ApmQuery:
    Compute: Optional[Sequence["_Compute"]]
    Index: Optional[str]
    Search: Optional[Sequence["_Search"]]
    GroupBy: Optional[Sequence["_GroupBy"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApmQuery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApmQuery"]:
        if not json_data:
            return None
        return cls(
            Compute=json_data.get("Compute"),
            Index=json_data.get("Index"),
            Search=json_data.get("Search"),
            GroupBy=json_data.get("GroupBy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApmQuery = ApmQuery


@dataclass
class Compute:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Compute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Compute"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Compute = Compute


@dataclass
class Search:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Search"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Search"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Search = Search


@dataclass
class GroupBy:
    Facet: Optional[str]
    Limit: Optional[float]
    Sort: Optional[Sequence["_Sort"]]

    @classmethod
    def _deserialize(
        cls: Type["_GroupBy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupBy"]:
        if not json_data:
            return None
        return cls(
            Facet=json_data.get("Facet"),
            Limit=json_data.get("Limit"),
            Sort=json_data.get("Sort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupBy = GroupBy


@dataclass
class Sort:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Sort"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sort"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sort = Sort


@dataclass
class ConditionalFormats:
    Comparator: Optional[str]
    CustomBgColor: Optional[str]
    CustomFgColor: Optional[str]
    HideValue: Optional[bool]
    ImageUrl: Optional[str]
    Palette: Optional[str]
    Timeframe: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionalFormats"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionalFormats"]:
        if not json_data:
            return None
        return cls(
            Comparator=json_data.get("Comparator"),
            CustomBgColor=json_data.get("CustomBgColor"),
            CustomFgColor=json_data.get("CustomFgColor"),
            HideValue=json_data.get("HideValue"),
            ImageUrl=json_data.get("ImageUrl"),
            Palette=json_data.get("Palette"),
            Timeframe=json_data.get("Timeframe"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionalFormats = ConditionalFormats


@dataclass
class LogQuery:
    Compute: Optional[Sequence["_Compute2"]]
    Index: Optional[str]
    Search: Optional[Sequence["_Search2"]]
    GroupBy: Optional[Sequence["_GroupBy"]]

    @classmethod
    def _deserialize(
        cls: Type["_LogQuery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogQuery"]:
        if not json_data:
            return None
        return cls(
            Compute=json_data.get("Compute"),
            Index=json_data.get("Index"),
            Search=json_data.get("Search"),
            GroupBy=json_data.get("GroupBy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogQuery = LogQuery


@dataclass
class Compute2:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Compute2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Compute2"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Compute2 = Compute2


@dataclass
class Search2:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Search2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Search2"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Search2 = Search2


@dataclass
class ProcessQuery:
    FilterBy: Optional[Sequence[str]]
    Limit: Optional[float]
    Metric: Optional[str]
    SearchBy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessQuery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessQuery"]:
        if not json_data:
            return None
        return cls(
            FilterBy=json_data.get("FilterBy"),
            Limit=json_data.get("Limit"),
            Metric=json_data.get("Metric"),
            SearchBy=json_data.get("SearchBy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessQuery = ProcessQuery


@dataclass
class Style:
    Palette: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Style"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Style"]:
        if not json_data:
            return None
        return cls(
            Palette=json_data.get("Palette"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Style = Style


@dataclass
class CheckStatusDefinition:
    Check: Optional[str]
    Group: Optional[str]
    GroupBy: Optional[Sequence[str]]
    Grouping: Optional[str]
    Tags: Optional[Sequence[str]]
    Time: Optional[Sequence["_Time3"]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CheckStatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CheckStatusDefinition"]:
        if not json_data:
            return None
        return cls(
            Check=json_data.get("Check"),
            Group=json_data.get("Group"),
            GroupBy=json_data.get("GroupBy"),
            Grouping=json_data.get("Grouping"),
            Tags=json_data.get("Tags"),
            Time=json_data.get("Time"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CheckStatusDefinition = CheckStatusDefinition


@dataclass
class Time3:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Time3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Time3"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Time3 = Time3


@dataclass
class DistributionDefinition:
    Time: Optional[Sequence["_Time4"]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    Request: Optional[Sequence["_Request"]]

    @classmethod
    def _deserialize(
        cls: Type["_DistributionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DistributionDefinition"]:
        if not json_data:
            return None
        return cls(
            Time=json_data.get("Time"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            Request=json_data.get("Request"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DistributionDefinition = DistributionDefinition


@dataclass
class Time4:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Time4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Time4"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Time4 = Time4


@dataclass
class EventStreamDefinition:
    EventSize: Optional[str]
    Query: Optional[str]
    Time: Optional[Sequence["_Time5"]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventStreamDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventStreamDefinition"]:
        if not json_data:
            return None
        return cls(
            EventSize=json_data.get("EventSize"),
            Query=json_data.get("Query"),
            Time=json_data.get("Time"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventStreamDefinition = EventStreamDefinition


@dataclass
class Time5:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Time5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Time5"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Time5 = Time5


@dataclass
class EventTimelineDefinition:
    Query: Optional[str]
    Time: Optional[Sequence["_Time6"]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventTimelineDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventTimelineDefinition"]:
        if not json_data:
            return None
        return cls(
            Query=json_data.get("Query"),
            Time=json_data.get("Time"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventTimelineDefinition = EventTimelineDefinition


@dataclass
class Time6:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Time6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Time6"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Time6 = Time6


@dataclass
class FreeTextDefinition:
    Color: Optional[str]
    FontSize: Optional[str]
    Text: Optional[str]
    TextAlign: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeTextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeTextDefinition"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
            FontSize=json_data.get("FontSize"),
            Text=json_data.get("Text"),
            TextAlign=json_data.get("TextAlign"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeTextDefinition = FreeTextDefinition


@dataclass
class HeatmapDefinition:
    Time: Optional[Sequence["_Time7"]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    Request: Optional[Sequence["_Request"]]
    Yaxis: Optional[Sequence["_Yaxis"]]

    @classmethod
    def _deserialize(
        cls: Type["_HeatmapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeatmapDefinition"]:
        if not json_data:
            return None
        return cls(
            Time=json_data.get("Time"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            Request=json_data.get("Request"),
            Yaxis=json_data.get("Yaxis"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeatmapDefinition = HeatmapDefinition


@dataclass
class Time7:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Time7"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Time7"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Time7 = Time7


@dataclass
class Yaxis:
    IncludeZero: Optional[bool]
    Label: Optional[str]
    Max: Optional[str]
    Min: Optional[str]
    Scale: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Yaxis"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Yaxis"]:
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
_Yaxis = Yaxis


@dataclass
class HostmapDefinition:
    Group: Optional[Sequence[str]]
    NoGroupHosts: Optional[bool]
    NoMetricHosts: Optional[bool]
    NodeType: Optional[str]
    Scope: Optional[Sequence[str]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    Request: Optional[Sequence["_Request"]]
    Style: Optional[Sequence["_Style"]]

    @classmethod
    def _deserialize(
        cls: Type["_HostmapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostmapDefinition"]:
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
            Request=json_data.get("Request"),
            Style=json_data.get("Style"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostmapDefinition = HostmapDefinition


@dataclass
class IframeDefinition:
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IframeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IframeDefinition"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IframeDefinition = IframeDefinition


@dataclass
class ImageDefinition:
    Margin: Optional[str]
    Sizing: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageDefinition"]:
        if not json_data:
            return None
        return cls(
            Margin=json_data.get("Margin"),
            Sizing=json_data.get("Sizing"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageDefinition = ImageDefinition


@dataclass
class LogStreamDefinition:
    Columns: Optional[Sequence[str]]
    Logset: Optional[str]
    Query: Optional[str]
    Time: Optional[Sequence["_Time8"]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogStreamDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogStreamDefinition"]:
        if not json_data:
            return None
        return cls(
            Columns=json_data.get("Columns"),
            Logset=json_data.get("Logset"),
            Query=json_data.get("Query"),
            Time=json_data.get("Time"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogStreamDefinition = LogStreamDefinition


@dataclass
class Time8:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Time8"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Time8"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Time8 = Time8


@dataclass
class ManageStatusDefinition:
    ColorPreference: Optional[str]
    Count: Optional[float]
    DisplayFormat: Optional[str]
    HideZeroCounts: Optional[bool]
    Query: Optional[str]
    ShowLastTriggered: Optional[bool]
    Sort: Optional[str]
    Start: Optional[float]
    SummaryType: Optional[str]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManageStatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManageStatusDefinition"]:
        if not json_data:
            return None
        return cls(
            ColorPreference=json_data.get("ColorPreference"),
            Count=json_data.get("Count"),
            DisplayFormat=json_data.get("DisplayFormat"),
            HideZeroCounts=json_data.get("HideZeroCounts"),
            Query=json_data.get("Query"),
            ShowLastTriggered=json_data.get("ShowLastTriggered"),
            Sort=json_data.get("Sort"),
            Start=json_data.get("Start"),
            SummaryType=json_data.get("SummaryType"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManageStatusDefinition = ManageStatusDefinition


@dataclass
class NoteDefinition:
    BackgroundColor: Optional[str]
    Content: Optional[str]
    FontSize: Optional[str]
    ShowTick: Optional[bool]
    TextAlign: Optional[str]
    TickEdge: Optional[str]
    TickPos: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NoteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NoteDefinition"]:
        if not json_data:
            return None
        return cls(
            BackgroundColor=json_data.get("BackgroundColor"),
            Content=json_data.get("Content"),
            FontSize=json_data.get("FontSize"),
            ShowTick=json_data.get("ShowTick"),
            TextAlign=json_data.get("TextAlign"),
            TickEdge=json_data.get("TickEdge"),
            TickPos=json_data.get("TickPos"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NoteDefinition = NoteDefinition


@dataclass
class QueryTableDefinition:
    Time: Optional[Sequence["_Time9"]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    Request: Optional[Sequence["_Request"]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryTableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryTableDefinition"]:
        if not json_data:
            return None
        return cls(
            Time=json_data.get("Time"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            Request=json_data.get("Request"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryTableDefinition = QueryTableDefinition


@dataclass
class Time9:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Time9"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Time9"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Time9 = Time9


@dataclass
class QueryValueDefinition:
    Autoscale: Optional[bool]
    CustomUnit: Optional[str]
    Precision: Optional[float]
    TextAlign: Optional[str]
    Time: Optional[Sequence["_Time10"]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    Request: Optional[Sequence["_Request"]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryValueDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryValueDefinition"]:
        if not json_data:
            return None
        return cls(
            Autoscale=json_data.get("Autoscale"),
            CustomUnit=json_data.get("CustomUnit"),
            Precision=json_data.get("Precision"),
            TextAlign=json_data.get("TextAlign"),
            Time=json_data.get("Time"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            Request=json_data.get("Request"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryValueDefinition = QueryValueDefinition


@dataclass
class Time10:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Time10"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Time10"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Time10 = Time10


@dataclass
class ScatterplotDefinition:
    ColorByGroups: Optional[Sequence[str]]
    Time: Optional[Sequence["_Time11"]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    Request: Optional[Sequence["_Request"]]
    Xaxis: Optional[Sequence["_Xaxis"]]
    Yaxis: Optional[Sequence["_Yaxis"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScatterplotDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScatterplotDefinition"]:
        if not json_data:
            return None
        return cls(
            ColorByGroups=json_data.get("ColorByGroups"),
            Time=json_data.get("Time"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            Request=json_data.get("Request"),
            Xaxis=json_data.get("Xaxis"),
            Yaxis=json_data.get("Yaxis"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScatterplotDefinition = ScatterplotDefinition


@dataclass
class Time11:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Time11"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Time11"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Time11 = Time11


@dataclass
class Xaxis:
    IncludeZero: Optional[bool]
    Label: Optional[str]
    Max: Optional[str]
    Min: Optional[str]
    Scale: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Xaxis"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Xaxis"]:
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
_Xaxis = Xaxis


@dataclass
class ServiceLevelObjectiveDefinition:
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
        cls: Type["_ServiceLevelObjectiveDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceLevelObjectiveDefinition"]:
        if not json_data:
            return None
        return cls(
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
_ServiceLevelObjectiveDefinition = ServiceLevelObjectiveDefinition


@dataclass
class TimeseriesDefinition:
    LegendSize: Optional[str]
    ShowLegend: Optional[bool]
    Time: Optional[Sequence["_Time12"]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    Event: Optional[Sequence["_Event"]]
    Marker: Optional[Sequence["_Marker"]]
    Request: Optional[Sequence["_Request"]]
    Yaxis: Optional[Sequence["_Yaxis"]]

    @classmethod
    def _deserialize(
        cls: Type["_TimeseriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeseriesDefinition"]:
        if not json_data:
            return None
        return cls(
            LegendSize=json_data.get("LegendSize"),
            ShowLegend=json_data.get("ShowLegend"),
            Time=json_data.get("Time"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            Event=json_data.get("Event"),
            Marker=json_data.get("Marker"),
            Request=json_data.get("Request"),
            Yaxis=json_data.get("Yaxis"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeseriesDefinition = TimeseriesDefinition


@dataclass
class Time12:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Time12"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Time12"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Time12 = Time12


@dataclass
class Event:
    Q: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Event"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Event"]:
        if not json_data:
            return None
        return cls(
            Q=json_data.get("Q"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Event = Event


@dataclass
class Marker:
    DisplayType: Optional[str]
    Label: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Marker"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Marker"]:
        if not json_data:
            return None
        return cls(
            DisplayType=json_data.get("DisplayType"),
            Label=json_data.get("Label"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Marker = Marker


@dataclass
class ToplistDefinition:
    Time: Optional[Sequence["_Time13"]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]
    Request: Optional[Sequence["_Request"]]

    @classmethod
    def _deserialize(
        cls: Type["_ToplistDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ToplistDefinition"]:
        if not json_data:
            return None
        return cls(
            Time=json_data.get("Time"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            Request=json_data.get("Request"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ToplistDefinition = ToplistDefinition


@dataclass
class Time13:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Time13"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Time13"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Time13 = Time13


@dataclass
class TraceServiceDefinition:
    DisplayFormat: Optional[str]
    Env: Optional[str]
    Service: Optional[str]
    ShowBreakdown: Optional[bool]
    ShowDistribution: Optional[bool]
    ShowErrors: Optional[bool]
    ShowHits: Optional[bool]
    ShowLatency: Optional[bool]
    ShowResourceList: Optional[bool]
    SizeFormat: Optional[str]
    SpanName: Optional[str]
    Time: Optional[Sequence["_Time14"]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TraceServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TraceServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            DisplayFormat=json_data.get("DisplayFormat"),
            Env=json_data.get("Env"),
            Service=json_data.get("Service"),
            ShowBreakdown=json_data.get("ShowBreakdown"),
            ShowDistribution=json_data.get("ShowDistribution"),
            ShowErrors=json_data.get("ShowErrors"),
            ShowHits=json_data.get("ShowHits"),
            ShowLatency=json_data.get("ShowLatency"),
            ShowResourceList=json_data.get("ShowResourceList"),
            SizeFormat=json_data.get("SizeFormat"),
            SpanName=json_data.get("SpanName"),
            Time=json_data.get("Time"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TraceServiceDefinition = TraceServiceDefinition


@dataclass
class Time14:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Time14"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Time14"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Time14 = Time14


@dataclass
class GroupDefinition:
    LayoutType: Optional[str]
    Title: Optional[str]
    Widget: Optional[Sequence["_Widget"]]

    @classmethod
    def _deserialize(
        cls: Type["_GroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupDefinition"]:
        if not json_data:
            return None
        return cls(
            LayoutType=json_data.get("LayoutType"),
            Title=json_data.get("Title"),
            Widget=json_data.get("Widget"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupDefinition = GroupDefinition


