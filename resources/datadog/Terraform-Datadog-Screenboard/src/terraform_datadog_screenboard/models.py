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
    Height: Optional[str]
    Id: Optional[str]
    ReadOnly: Optional[bool]
    Shared: Optional[bool]
    Title: Optional[str]
    Width: Optional[str]
    TemplateVariable: Optional[Sequence["_TemplateVariable"]]
    Widget: Optional[Sequence["_Widget"]]
    Rule: Optional[Sequence["_Rule"]]
    TileDef: Optional[Sequence["_TileDef"]]
    Event: Optional[Sequence["_Event"]]
    Marker: Optional[Sequence["_Marker"]]
    Request: Optional[Sequence["_Request"]]
    ApmQuery: Optional[Sequence["_ApmQuery"]]
    ConditionalFormat: Optional[Sequence["_ConditionalFormat"]]
    LogQuery: Optional[Sequence["_LogQuery"]]
    ProcessQuery: Optional[Sequence["_ProcessQuery"]]
    Compute: Optional[Sequence["_Compute"]]
    GroupBy: Optional[Sequence["_GroupBy"]]
    Search: Optional[Sequence["_Search"]]
    Sort: Optional[Sequence["_Sort"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Height=json_data.get("Height"),
            Id=json_data.get("Id"),
            ReadOnly=json_data.get("ReadOnly"),
            Shared=json_data.get("Shared"),
            Title=json_data.get("Title"),
            Width=json_data.get("Width"),
            TemplateVariable=json_data.get("TemplateVariable"),
            Widget=json_data.get("Widget"),
            Rule=json_data.get("Rule"),
            TileDef=json_data.get("TileDef"),
            Event=json_data.get("Event"),
            Marker=json_data.get("Marker"),
            Request=json_data.get("Request"),
            ApmQuery=json_data.get("ApmQuery"),
            ConditionalFormat=json_data.get("ConditionalFormat"),
            LogQuery=json_data.get("LogQuery"),
            ProcessQuery=json_data.get("ProcessQuery"),
            Compute=json_data.get("Compute"),
            GroupBy=json_data.get("GroupBy"),
            Search=json_data.get("Search"),
            Sort=json_data.get("Sort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TemplateVariable:
    Default: Optional[str]
    Name: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateVariable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateVariable"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
            Name=json_data.get("Name"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateVariable = TemplateVariable


@dataclass
class Widget:
    AlertId: Optional[float]
    AutoRefresh: Optional[bool]
    Bgcolor: Optional[str]
    Check: Optional[str]
    Color: Optional[str]
    ColorPreference: Optional[str]
    Columns: Optional[str]
    DisplayFormat: Optional[str]
    Env: Optional[str]
    EventSize: Optional[str]
    FontSize: Optional[str]
    Group: Optional[str]
    GroupBy: Optional[Sequence[str]]
    Grouping: Optional[str]
    Height: Optional[float]
    HideZeroCounts: Optional[bool]
    Html: Optional[str]
    LayoutVersion: Optional[str]
    Legend: Optional[bool]
    LegendSize: Optional[str]
    Logset: Optional[str]
    ManageStatusShowTitle: Optional[bool]
    ManageStatusTitleAlign: Optional[str]
    ManageStatusTitleSize: Optional[str]
    ManageStatusTitleText: Optional[str]
    Margin: Optional[str]
    Monitor: Optional[Sequence["_Monitor"]]
    MustShowBreakdown: Optional[bool]
    MustShowDistribution: Optional[bool]
    MustShowErrors: Optional[bool]
    MustShowHits: Optional[bool]
    MustShowLatency: Optional[bool]
    MustShowResourceList: Optional[bool]
    Params: Optional[Sequence["_Params"]]
    Precision: Optional[str]
    Query: Optional[str]
    ServiceName: Optional[str]
    ServiceService: Optional[str]
    ShowLastTriggered: Optional[bool]
    SizeVersion: Optional[str]
    Sizing: Optional[str]
    SummaryType: Optional[str]
    Tags: Optional[Sequence[str]]
    Text: Optional[str]
    TextAlign: Optional[str]
    TextSize: Optional[str]
    Tick: Optional[bool]
    TickEdge: Optional[str]
    TickPos: Optional[str]
    Time: Optional[Sequence["_Time"]]
    Timeframes: Optional[Sequence[str]]
    Title: Optional[str]
    TitleAlign: Optional[str]
    TitleSize: Optional[float]
    Type: Optional[str]
    Unit: Optional[str]
    Url: Optional[str]
    VizType: Optional[str]
    Width: Optional[float]
    X: Optional[float]
    Y: Optional[float]
    Rule: Optional[Sequence["_Rule"]]
    TileDef: Optional[Sequence["_TileDef"]]

    @classmethod
    def _deserialize(
        cls: Type["_Widget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Widget"]:
        if not json_data:
            return None
        return cls(
            AlertId=json_data.get("AlertId"),
            AutoRefresh=json_data.get("AutoRefresh"),
            Bgcolor=json_data.get("Bgcolor"),
            Check=json_data.get("Check"),
            Color=json_data.get("Color"),
            ColorPreference=json_data.get("ColorPreference"),
            Columns=json_data.get("Columns"),
            DisplayFormat=json_data.get("DisplayFormat"),
            Env=json_data.get("Env"),
            EventSize=json_data.get("EventSize"),
            FontSize=json_data.get("FontSize"),
            Group=json_data.get("Group"),
            GroupBy=json_data.get("GroupBy"),
            Grouping=json_data.get("Grouping"),
            Height=json_data.get("Height"),
            HideZeroCounts=json_data.get("HideZeroCounts"),
            Html=json_data.get("Html"),
            LayoutVersion=json_data.get("LayoutVersion"),
            Legend=json_data.get("Legend"),
            LegendSize=json_data.get("LegendSize"),
            Logset=json_data.get("Logset"),
            ManageStatusShowTitle=json_data.get("ManageStatusShowTitle"),
            ManageStatusTitleAlign=json_data.get("ManageStatusTitleAlign"),
            ManageStatusTitleSize=json_data.get("ManageStatusTitleSize"),
            ManageStatusTitleText=json_data.get("ManageStatusTitleText"),
            Margin=json_data.get("Margin"),
            Monitor=json_data.get("Monitor"),
            MustShowBreakdown=json_data.get("MustShowBreakdown"),
            MustShowDistribution=json_data.get("MustShowDistribution"),
            MustShowErrors=json_data.get("MustShowErrors"),
            MustShowHits=json_data.get("MustShowHits"),
            MustShowLatency=json_data.get("MustShowLatency"),
            MustShowResourceList=json_data.get("MustShowResourceList"),
            Params=json_data.get("Params"),
            Precision=json_data.get("Precision"),
            Query=json_data.get("Query"),
            ServiceName=json_data.get("ServiceName"),
            ServiceService=json_data.get("ServiceService"),
            ShowLastTriggered=json_data.get("ShowLastTriggered"),
            SizeVersion=json_data.get("SizeVersion"),
            Sizing=json_data.get("Sizing"),
            SummaryType=json_data.get("SummaryType"),
            Tags=json_data.get("Tags"),
            Text=json_data.get("Text"),
            TextAlign=json_data.get("TextAlign"),
            TextSize=json_data.get("TextSize"),
            Tick=json_data.get("Tick"),
            TickEdge=json_data.get("TickEdge"),
            TickPos=json_data.get("TickPos"),
            Time=json_data.get("Time"),
            Timeframes=json_data.get("Timeframes"),
            Title=json_data.get("Title"),
            TitleAlign=json_data.get("TitleAlign"),
            TitleSize=json_data.get("TitleSize"),
            Type=json_data.get("Type"),
            Unit=json_data.get("Unit"),
            Url=json_data.get("Url"),
            VizType=json_data.get("VizType"),
            Width=json_data.get("Width"),
            X=json_data.get("X"),
            Y=json_data.get("Y"),
            Rule=json_data.get("Rule"),
            TileDef=json_data.get("TileDef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Widget = Widget


@dataclass
class Monitor:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Monitor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Monitor"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Monitor = Monitor


@dataclass
class Params:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Params"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Params"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Params = Params


@dataclass
class Time:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Time"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Time"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Time = Time


@dataclass
class Rule:
    Color: Optional[str]
    Threshold: Optional[float]
    Timeframe: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
            Threshold=json_data.get("Threshold"),
            Timeframe=json_data.get("Timeframe"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class TileDef:
    Autoscale: Optional[bool]
    CustomUnit: Optional[str]
    Group: Optional[Sequence[str]]
    NoGroupHosts: Optional[bool]
    NoMetricHosts: Optional[bool]
    NodeType: Optional[str]
    Precision: Optional[str]
    Scope: Optional[Sequence[str]]
    Style: Optional[Sequence["_Style"]]
    TextAlign: Optional[str]
    Viz: Optional[str]
    Event: Optional[Sequence["_Event"]]
    Marker: Optional[Sequence["_Marker"]]
    Request: Optional[Sequence["_Request"]]

    @classmethod
    def _deserialize(
        cls: Type["_TileDef"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TileDef"]:
        if not json_data:
            return None
        return cls(
            Autoscale=json_data.get("Autoscale"),
            CustomUnit=json_data.get("CustomUnit"),
            Group=json_data.get("Group"),
            NoGroupHosts=json_data.get("NoGroupHosts"),
            NoMetricHosts=json_data.get("NoMetricHosts"),
            NodeType=json_data.get("NodeType"),
            Precision=json_data.get("Precision"),
            Scope=json_data.get("Scope"),
            Style=json_data.get("Style"),
            TextAlign=json_data.get("TextAlign"),
            Viz=json_data.get("Viz"),
            Event=json_data.get("Event"),
            Marker=json_data.get("Marker"),
            Request=json_data.get("Request"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TileDef = TileDef


@dataclass
class Style:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Style"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Style"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Style = Style


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
    Label: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Marker"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Marker"]:
        if not json_data:
            return None
        return cls(
            Label=json_data.get("Label"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Marker = Marker


@dataclass
class Request:
    Aggregator: Optional[str]
    ChangeType: Optional[str]
    CompareTo: Optional[str]
    ExtraCol: Optional[str]
    IncreaseGood: Optional[bool]
    Limit: Optional[float]
    MetadataJson: Optional[str]
    Metric: Optional[str]
    OrderBy: Optional[str]
    OrderDir: Optional[str]
    Q: Optional[str]
    QueryType: Optional[str]
    Style: Optional[Sequence["_Style2"]]
    TagFilters: Optional[Sequence[str]]
    TextFilter: Optional[str]
    Type: Optional[str]
    ApmQuery: Optional[Sequence["_ApmQuery"]]
    ConditionalFormat: Optional[Sequence["_ConditionalFormat"]]
    LogQuery: Optional[Sequence["_LogQuery"]]
    ProcessQuery: Optional[Sequence["_ProcessQuery"]]

    @classmethod
    def _deserialize(
        cls: Type["_Request"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Request"]:
        if not json_data:
            return None
        return cls(
            Aggregator=json_data.get("Aggregator"),
            ChangeType=json_data.get("ChangeType"),
            CompareTo=json_data.get("CompareTo"),
            ExtraCol=json_data.get("ExtraCol"),
            IncreaseGood=json_data.get("IncreaseGood"),
            Limit=json_data.get("Limit"),
            MetadataJson=json_data.get("MetadataJson"),
            Metric=json_data.get("Metric"),
            OrderBy=json_data.get("OrderBy"),
            OrderDir=json_data.get("OrderDir"),
            Q=json_data.get("Q"),
            QueryType=json_data.get("QueryType"),
            Style=json_data.get("Style"),
            TagFilters=json_data.get("TagFilters"),
            TextFilter=json_data.get("TextFilter"),
            Type=json_data.get("Type"),
            ApmQuery=json_data.get("ApmQuery"),
            ConditionalFormat=json_data.get("ConditionalFormat"),
            LogQuery=json_data.get("LogQuery"),
            ProcessQuery=json_data.get("ProcessQuery"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Request = Request


@dataclass
class Style2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Style2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Style2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Style2 = Style2


@dataclass
class ApmQuery:
    Index: Optional[str]
    Compute: Optional[Sequence["_Compute"]]
    GroupBy: Optional[Sequence["_GroupBy"]]
    Search: Optional[Sequence["_Search"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApmQuery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApmQuery"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            Compute=json_data.get("Compute"),
            GroupBy=json_data.get("GroupBy"),
            Search=json_data.get("Search"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApmQuery = ApmQuery


@dataclass
class Compute:
    Aggregation: Optional[str]
    Facet: Optional[str]
    Interval: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Compute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Compute"]:
        if not json_data:
            return None
        return cls(
            Aggregation=json_data.get("Aggregation"),
            Facet=json_data.get("Facet"),
            Interval=json_data.get("Interval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Compute = Compute


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
    Aggregation: Optional[str]
    Facet: Optional[str]
    Order: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Sort"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sort"]:
        if not json_data:
            return None
        return cls(
            Aggregation=json_data.get("Aggregation"),
            Facet=json_data.get("Facet"),
            Order=json_data.get("Order"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sort = Sort


@dataclass
class Search:
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Search"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Search"]:
        if not json_data:
            return None
        return cls(
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Search = Search


@dataclass
class ConditionalFormat:
    Color: Optional[str]
    Comparator: Optional[str]
    CustomBgColor: Optional[str]
    Invert: Optional[bool]
    Palette: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionalFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionalFormat"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
            Comparator=json_data.get("Comparator"),
            CustomBgColor=json_data.get("CustomBgColor"),
            Invert=json_data.get("Invert"),
            Palette=json_data.get("Palette"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionalFormat = ConditionalFormat


@dataclass
class LogQuery:
    Index: Optional[str]
    Compute: Optional[Sequence["_Compute"]]
    GroupBy: Optional[Sequence["_GroupBy"]]
    Search: Optional[Sequence["_Search"]]

    @classmethod
    def _deserialize(
        cls: Type["_LogQuery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogQuery"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            Compute=json_data.get("Compute"),
            GroupBy=json_data.get("GroupBy"),
            Search=json_data.get("Search"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogQuery = LogQuery


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


