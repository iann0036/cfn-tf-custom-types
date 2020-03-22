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
    Id: Optional[str]
    ReadOnly: Optional[bool]
    Title: Optional[str]
    Graph: Optional[Sequence["_Graph"]]
    TemplateVariable: Optional[Sequence["_TemplateVariable"]]
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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            ReadOnly=json_data.get("ReadOnly"),
            Title=json_data.get("Title"),
            Graph=json_data.get("Graph"),
            TemplateVariable=json_data.get("TemplateVariable"),
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
class Graph:
    Autoscale: Optional[bool]
    CustomUnit: Optional[str]
    Events: Optional[Sequence[str]]
    Group: Optional[Sequence[str]]
    IncludeNoMetricHosts: Optional[bool]
    IncludeUngroupedHosts: Optional[bool]
    NodeType: Optional[str]
    Precision: Optional[str]
    Scope: Optional[Sequence[str]]
    Style: Optional[Sequence["_Style"]]
    TextAlign: Optional[str]
    Title: Optional[str]
    Viz: Optional[str]
    Yaxis: Optional[Sequence["_Yaxis"]]
    Marker: Optional[Sequence["_Marker"]]
    Request: Optional[Sequence["_Request"]]

    @classmethod
    def _deserialize(
        cls: Type["_Graph"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Graph"]:
        if not json_data:
            return None
        return cls(
            Autoscale=json_data.get("Autoscale"),
            CustomUnit=json_data.get("CustomUnit"),
            Events=json_data.get("Events"),
            Group=json_data.get("Group"),
            IncludeNoMetricHosts=json_data.get("IncludeNoMetricHosts"),
            IncludeUngroupedHosts=json_data.get("IncludeUngroupedHosts"),
            NodeType=json_data.get("NodeType"),
            Precision=json_data.get("Precision"),
            Scope=json_data.get("Scope"),
            Style=json_data.get("Style"),
            TextAlign=json_data.get("TextAlign"),
            Title=json_data.get("Title"),
            Viz=json_data.get("Viz"),
            Yaxis=json_data.get("Yaxis"),
            Marker=json_data.get("Marker"),
            Request=json_data.get("Request"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Graph = Graph


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
class Yaxis:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Yaxis"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Yaxis"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Yaxis = Yaxis


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
    MetadataJson: Optional[str]
    OrderBy: Optional[str]
    OrderDirection: Optional[str]
    Q: Optional[str]
    Stacked: Optional[bool]
    Style: Optional[Sequence["_Style2"]]
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
            MetadataJson=json_data.get("MetadataJson"),
            OrderBy=json_data.get("OrderBy"),
            OrderDirection=json_data.get("OrderDirection"),
            Q=json_data.get("Q"),
            Stacked=json_data.get("Stacked"),
            Style=json_data.get("Style"),
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
    Interval: Optional[float]

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
    Comparator: Optional[str]
    CustomBgColor: Optional[str]
    CustomFgColor: Optional[str]
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
            Comparator=json_data.get("Comparator"),
            CustomBgColor=json_data.get("CustomBgColor"),
            CustomFgColor=json_data.get("CustomFgColor"),
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


