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
    Background: Optional[str]
    Category: Optional[str]
    ColorPalette: Optional[str]
    Comments: Optional[str]
    Dataset: Optional[str]
    Dimension: Optional[str]
    DynamicSortSubtable: Optional[str]
    Favorite: Optional[str]
    GraphType: Optional[str]
    Id: Optional[str]
    Legend: Optional[str]
    LegendFontSize: Optional[float]
    Name: Optional[str]
    Period: Optional[str]
    Policy: Optional[float]
    Style: Optional[str]
    Title: Optional[str]
    TitleFontSize: Optional[float]
    Type: Optional[str]
    Vdomparam: Optional[str]
    CategorySeries: Optional[Sequence["_CategorySeriesDefinition"]]
    Column: Optional[Sequence["_ColumnDefinition"]]
    DrillDownCharts: Optional[Sequence["_DrillDownChartsDefinition"]]
    ValueSeries: Optional[Sequence["_ValueSeriesDefinition"]]
    XSeries: Optional[Sequence["_XSeriesDefinition"]]
    YSeries: Optional[Sequence["_YSeriesDefinition"]]

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
            Background=json_data.get("Background"),
            Category=json_data.get("Category"),
            ColorPalette=json_data.get("ColorPalette"),
            Comments=json_data.get("Comments"),
            Dataset=json_data.get("Dataset"),
            Dimension=json_data.get("Dimension"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Favorite=json_data.get("Favorite"),
            GraphType=json_data.get("GraphType"),
            Id=json_data.get("Id"),
            Legend=json_data.get("Legend"),
            LegendFontSize=json_data.get("LegendFontSize"),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
            Policy=json_data.get("Policy"),
            Style=json_data.get("Style"),
            Title=json_data.get("Title"),
            TitleFontSize=json_data.get("TitleFontSize"),
            Type=json_data.get("Type"),
            Vdomparam=json_data.get("Vdomparam"),
            CategorySeries=deserialize_list(json_data.get("CategorySeries"), CategorySeriesDefinition),
            Column=deserialize_list(json_data.get("Column"), ColumnDefinition),
            DrillDownCharts=deserialize_list(json_data.get("DrillDownCharts"), DrillDownChartsDefinition),
            ValueSeries=deserialize_list(json_data.get("ValueSeries"), ValueSeriesDefinition),
            XSeries=deserialize_list(json_data.get("XSeries"), XSeriesDefinition),
            YSeries=deserialize_list(json_data.get("YSeries"), YSeriesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CategorySeriesDefinition(BaseModel):
    Databind: Optional[str]
    FontSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CategorySeriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategorySeriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Databind=json_data.get("Databind"),
            FontSize=json_data.get("FontSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategorySeriesDefinition = CategorySeriesDefinition


@dataclass
class ColumnDefinition(BaseModel):
    DetailUnit: Optional[str]
    DetailValue: Optional[str]
    FooterUnit: Optional[str]
    FooterValue: Optional[str]
    HeaderValue: Optional[str]
    Id: Optional[float]
    Mapping: Optional[Sequence["_MappingDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnDefinition"]:
        if not json_data:
            return None
        return cls(
            DetailUnit=json_data.get("DetailUnit"),
            DetailValue=json_data.get("DetailValue"),
            FooterUnit=json_data.get("FooterUnit"),
            FooterValue=json_data.get("FooterValue"),
            HeaderValue=json_data.get("HeaderValue"),
            Id=json_data.get("Id"),
            Mapping=deserialize_list(json_data.get("Mapping"), MappingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnDefinition = ColumnDefinition


@dataclass
class MappingDefinition(BaseModel):
    Displayname: Optional[str]
    Id: Optional[float]
    Op: Optional[str]
    Value1: Optional[str]
    Value2: Optional[str]
    ValueType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MappingDefinition"]:
        if not json_data:
            return None
        return cls(
            Displayname=json_data.get("Displayname"),
            Id=json_data.get("Id"),
            Op=json_data.get("Op"),
            Value1=json_data.get("Value1"),
            Value2=json_data.get("Value2"),
            ValueType=json_data.get("ValueType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MappingDefinition = MappingDefinition


@dataclass
class DrillDownChartsDefinition(BaseModel):
    ChartName: Optional[str]
    Id: Optional[float]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DrillDownChartsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DrillDownChartsDefinition"]:
        if not json_data:
            return None
        return cls(
            ChartName=json_data.get("ChartName"),
            Id=json_data.get("Id"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DrillDownChartsDefinition = DrillDownChartsDefinition


@dataclass
class ValueSeriesDefinition(BaseModel):
    Databind: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValueSeriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueSeriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Databind=json_data.get("Databind"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueSeriesDefinition = ValueSeriesDefinition


@dataclass
class XSeriesDefinition(BaseModel):
    Caption: Optional[str]
    CaptionFontSize: Optional[float]
    Databind: Optional[str]
    FontSize: Optional[float]
    IsCategory: Optional[str]
    LabelAngle: Optional[str]
    ScaleDirection: Optional[str]
    ScaleFormat: Optional[str]
    ScaleStep: Optional[float]
    ScaleUnit: Optional[str]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_XSeriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_XSeriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Caption=json_data.get("Caption"),
            CaptionFontSize=json_data.get("CaptionFontSize"),
            Databind=json_data.get("Databind"),
            FontSize=json_data.get("FontSize"),
            IsCategory=json_data.get("IsCategory"),
            LabelAngle=json_data.get("LabelAngle"),
            ScaleDirection=json_data.get("ScaleDirection"),
            ScaleFormat=json_data.get("ScaleFormat"),
            ScaleStep=json_data.get("ScaleStep"),
            ScaleUnit=json_data.get("ScaleUnit"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_XSeriesDefinition = XSeriesDefinition


@dataclass
class YSeriesDefinition(BaseModel):
    Caption: Optional[str]
    CaptionFontSize: Optional[float]
    Databind: Optional[str]
    ExtraDatabind: Optional[str]
    ExtraY: Optional[str]
    ExtraYLegend: Optional[str]
    FontSize: Optional[float]
    Group: Optional[str]
    LabelAngle: Optional[str]
    Unit: Optional[str]
    YLegend: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_YSeriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_YSeriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Caption=json_data.get("Caption"),
            CaptionFontSize=json_data.get("CaptionFontSize"),
            Databind=json_data.get("Databind"),
            ExtraDatabind=json_data.get("ExtraDatabind"),
            ExtraY=json_data.get("ExtraY"),
            ExtraYLegend=json_data.get("ExtraYLegend"),
            FontSize=json_data.get("FontSize"),
            Group=json_data.get("Group"),
            LabelAngle=json_data.get("LabelAngle"),
            Unit=json_data.get("Unit"),
            YLegend=json_data.get("YLegend"),
        )


# work around possible type aliasing issues when variable has same name as a model
_YSeriesDefinition = YSeriesDefinition


