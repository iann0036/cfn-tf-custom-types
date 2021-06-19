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
    CanModify: Optional[Sequence[str]]
    CanView: Optional[Sequence[str]]
    Description: Optional[str]
    DisplayQueryParameters: Optional[bool]
    DisplaySectionTableOfContents: Optional[bool]
    EventFilterType: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence[str]]
    Url: Optional[str]
    ParameterDetails: Optional[Sequence["_ParameterDetailsDefinition"]]
    Section: Optional[Sequence["_SectionDefinition"]]

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
            CanModify=json_data.get("CanModify"),
            CanView=json_data.get("CanView"),
            Description=json_data.get("Description"),
            DisplayQueryParameters=json_data.get("DisplayQueryParameters"),
            DisplaySectionTableOfContents=json_data.get("DisplaySectionTableOfContents"),
            EventFilterType=json_data.get("EventFilterType"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Url=json_data.get("Url"),
            ParameterDetails=deserialize_list(json_data.get("ParameterDetails"), ParameterDetailsDefinition),
            Section=deserialize_list(json_data.get("Section"), SectionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ParameterDetailsDefinition(BaseModel):
    DefaultValue: Optional[str]
    DynamicFieldType: Optional[str]
    HideFromView: Optional[bool]
    Label: Optional[str]
    Name: Optional[str]
    ParameterType: Optional[str]
    QueryValue: Optional[str]
    TagKey: Optional[str]
    ValuesToReadableStrings: Optional[Sequence["_ValuesToReadableStringsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultValue=json_data.get("DefaultValue"),
            DynamicFieldType=json_data.get("DynamicFieldType"),
            HideFromView=json_data.get("HideFromView"),
            Label=json_data.get("Label"),
            Name=json_data.get("Name"),
            ParameterType=json_data.get("ParameterType"),
            QueryValue=json_data.get("QueryValue"),
            TagKey=json_data.get("TagKey"),
            ValuesToReadableStrings=deserialize_list(json_data.get("ValuesToReadableStrings"), ValuesToReadableStringsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterDetailsDefinition = ParameterDetailsDefinition


@dataclass
class ValuesToReadableStringsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValuesToReadableStringsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValuesToReadableStringsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValuesToReadableStringsDefinition = ValuesToReadableStringsDefinition


@dataclass
class SectionDefinition(BaseModel):
    Name: Optional[str]
    Row: Optional[Sequence["_RowDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SectionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SectionDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Row=deserialize_list(json_data.get("Row"), RowDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SectionDefinition = SectionDefinition


@dataclass
class RowDefinition(BaseModel):
    Chart: Optional[Sequence["_ChartDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RowDefinition"]:
        if not json_data:
            return None
        return cls(
            Chart=deserialize_list(json_data.get("Chart"), ChartDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RowDefinition = RowDefinition


@dataclass
class ChartDefinition(BaseModel):
    Base: Optional[float]
    ChartAttribute: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    Summarization: Optional[str]
    Units: Optional[str]
    ChartSetting: Optional[Sequence["_ChartSettingDefinition"]]
    Source: Optional[Sequence["_SourceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ChartDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChartDefinition"]:
        if not json_data:
            return None
        return cls(
            Base=json_data.get("Base"),
            ChartAttribute=json_data.get("ChartAttribute"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Summarization=json_data.get("Summarization"),
            Units=json_data.get("Units"),
            ChartSetting=deserialize_list(json_data.get("ChartSetting"), ChartSettingDefinition),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChartDefinition = ChartDefinition


@dataclass
class ChartSettingDefinition(BaseModel):
    AutoColumnTags: Optional[bool]
    ColumnTags: Optional[str]
    CustomTags: Optional[Sequence[str]]
    ExpectedDataSpacing: Optional[float]
    FixedLegendDisplayStats: Optional[Sequence[str]]
    FixedLegendEnabled: Optional[bool]
    FixedLegendFilterField: Optional[str]
    FixedLegendFilterLimit: Optional[float]
    FixedLegendFilterSort: Optional[str]
    FixedLegendHideLabel: Optional[bool]
    FixedLegendPosition: Optional[str]
    FixedLegendUseRawStats: Optional[bool]
    GroupBySource: Optional[bool]
    InvertDynamicLegendHoverControl: Optional[bool]
    LineType: Optional[str]
    Max: Optional[float]
    Min: Optional[float]
    NumTags: Optional[float]
    PlainMarkdownContent: Optional[str]
    ShowHosts: Optional[bool]
    ShowLabels: Optional[bool]
    ShowRawValues: Optional[bool]
    SortValuesDescending: Optional[bool]
    SparklineDecimalPrecision: Optional[float]
    SparklineDisplayColor: Optional[str]
    SparklineDisplayFontSize: Optional[str]
    SparklineDisplayHorizontalPosition: Optional[str]
    SparklineDisplayPostfix: Optional[str]
    SparklineDisplayPrefix: Optional[str]
    SparklineDisplayValueType: Optional[str]
    SparklineDisplayVerticalPosition: Optional[str]
    SparklineFillColor: Optional[str]
    SparklineLineColor: Optional[str]
    SparklineSize: Optional[str]
    SparklineValueColorMapApplyTo: Optional[str]
    SparklineValueColorMapColors: Optional[Sequence[str]]
    SparklineValueColorMapValues: Optional[Sequence[float]]
    SparklineValueColorMapValuesV2: Optional[Sequence[float]]
    SparklineValueTextMapText: Optional[Sequence[str]]
    SparklineValueTextMapThresholds: Optional[Sequence[float]]
    StackType: Optional[str]
    TagMode: Optional[str]
    TimeBasedColoring: Optional[bool]
    Type: Optional[str]
    WindowSize: Optional[float]
    Windowing: Optional[str]
    Xmax: Optional[float]
    Xmin: Optional[float]
    Y0ScaleSiBy1024: Optional[bool]
    Y0UnitAutoscaling: Optional[bool]
    Y1ScaleSiBy1024: Optional[bool]
    Y1UnitAutoscaling: Optional[bool]
    Y1Units: Optional[str]
    Y1max: Optional[float]
    Y1min: Optional[float]
    Ymax: Optional[float]
    Ymin: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ChartSettingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChartSettingDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoColumnTags=json_data.get("AutoColumnTags"),
            ColumnTags=json_data.get("ColumnTags"),
            CustomTags=json_data.get("CustomTags"),
            ExpectedDataSpacing=json_data.get("ExpectedDataSpacing"),
            FixedLegendDisplayStats=json_data.get("FixedLegendDisplayStats"),
            FixedLegendEnabled=json_data.get("FixedLegendEnabled"),
            FixedLegendFilterField=json_data.get("FixedLegendFilterField"),
            FixedLegendFilterLimit=json_data.get("FixedLegendFilterLimit"),
            FixedLegendFilterSort=json_data.get("FixedLegendFilterSort"),
            FixedLegendHideLabel=json_data.get("FixedLegendHideLabel"),
            FixedLegendPosition=json_data.get("FixedLegendPosition"),
            FixedLegendUseRawStats=json_data.get("FixedLegendUseRawStats"),
            GroupBySource=json_data.get("GroupBySource"),
            InvertDynamicLegendHoverControl=json_data.get("InvertDynamicLegendHoverControl"),
            LineType=json_data.get("LineType"),
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
            NumTags=json_data.get("NumTags"),
            PlainMarkdownContent=json_data.get("PlainMarkdownContent"),
            ShowHosts=json_data.get("ShowHosts"),
            ShowLabels=json_data.get("ShowLabels"),
            ShowRawValues=json_data.get("ShowRawValues"),
            SortValuesDescending=json_data.get("SortValuesDescending"),
            SparklineDecimalPrecision=json_data.get("SparklineDecimalPrecision"),
            SparklineDisplayColor=json_data.get("SparklineDisplayColor"),
            SparklineDisplayFontSize=json_data.get("SparklineDisplayFontSize"),
            SparklineDisplayHorizontalPosition=json_data.get("SparklineDisplayHorizontalPosition"),
            SparklineDisplayPostfix=json_data.get("SparklineDisplayPostfix"),
            SparklineDisplayPrefix=json_data.get("SparklineDisplayPrefix"),
            SparklineDisplayValueType=json_data.get("SparklineDisplayValueType"),
            SparklineDisplayVerticalPosition=json_data.get("SparklineDisplayVerticalPosition"),
            SparklineFillColor=json_data.get("SparklineFillColor"),
            SparklineLineColor=json_data.get("SparklineLineColor"),
            SparklineSize=json_data.get("SparklineSize"),
            SparklineValueColorMapApplyTo=json_data.get("SparklineValueColorMapApplyTo"),
            SparklineValueColorMapColors=json_data.get("SparklineValueColorMapColors"),
            SparklineValueColorMapValues=json_data.get("SparklineValueColorMapValues"),
            SparklineValueColorMapValuesV2=json_data.get("SparklineValueColorMapValuesV2"),
            SparklineValueTextMapText=json_data.get("SparklineValueTextMapText"),
            SparklineValueTextMapThresholds=json_data.get("SparklineValueTextMapThresholds"),
            StackType=json_data.get("StackType"),
            TagMode=json_data.get("TagMode"),
            TimeBasedColoring=json_data.get("TimeBasedColoring"),
            Type=json_data.get("Type"),
            WindowSize=json_data.get("WindowSize"),
            Windowing=json_data.get("Windowing"),
            Xmax=json_data.get("Xmax"),
            Xmin=json_data.get("Xmin"),
            Y0ScaleSiBy1024=json_data.get("Y0ScaleSiBy1024"),
            Y0UnitAutoscaling=json_data.get("Y0UnitAutoscaling"),
            Y1ScaleSiBy1024=json_data.get("Y1ScaleSiBy1024"),
            Y1UnitAutoscaling=json_data.get("Y1UnitAutoscaling"),
            Y1Units=json_data.get("Y1Units"),
            Y1max=json_data.get("Y1max"),
            Y1min=json_data.get("Y1min"),
            Ymax=json_data.get("Ymax"),
            Ymin=json_data.get("Ymin"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChartSettingDefinition = ChartSettingDefinition


@dataclass
class SourceDefinition(BaseModel):
    Disabled: Optional[bool]
    Name: Optional[str]
    Query: Optional[str]
    QueryBuilderEnabled: Optional[bool]
    ScatterPlotSource: Optional[str]
    SourceDescription: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Disabled=json_data.get("Disabled"),
            Name=json_data.get("Name"),
            Query=json_data.get("Query"),
            QueryBuilderEnabled=json_data.get("QueryBuilderEnabled"),
            ScatterPlotSource=json_data.get("ScatterPlotSource"),
            SourceDescription=json_data.get("SourceDescription"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


