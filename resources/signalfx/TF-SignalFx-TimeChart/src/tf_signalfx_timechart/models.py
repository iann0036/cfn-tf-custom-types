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
    AxesIncludeZero: Optional[bool]
    AxesPrecision: Optional[float]
    ColorBy: Optional[str]
    Description: Optional[str]
    DisableSampling: Optional[bool]
    EndTime: Optional[float]
    Id: Optional[str]
    LegendFieldsToHide: Optional[Sequence[str]]
    MaxDelay: Optional[float]
    MinimumResolution: Optional[float]
    Name: Optional[str]
    OnChartLegendDimension: Optional[str]
    PlotType: Optional[str]
    ProgramText: Optional[str]
    ShowDataMarkers: Optional[bool]
    ShowEventLines: Optional[bool]
    Stacked: Optional[bool]
    StartTime: Optional[float]
    Tags: Optional[Sequence[str]]
    TimeRange: Optional[float]
    Timezone: Optional[str]
    UnitPrefix: Optional[str]
    Url: Optional[str]
    AxisLeft: Optional[Sequence["_AxisLeftDefinition"]]
    AxisRight: Optional[Sequence["_AxisRightDefinition"]]
    EventOptions: Optional[Sequence["_EventOptionsDefinition"]]
    HistogramOptions: Optional[Sequence["_HistogramOptionsDefinition"]]
    LegendOptionsFields: Optional[Sequence["_LegendOptionsFieldsDefinition"]]
    VizOptions: Optional[Sequence["_VizOptionsDefinition"]]

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
            AxesIncludeZero=json_data.get("AxesIncludeZero"),
            AxesPrecision=json_data.get("AxesPrecision"),
            ColorBy=json_data.get("ColorBy"),
            Description=json_data.get("Description"),
            DisableSampling=json_data.get("DisableSampling"),
            EndTime=json_data.get("EndTime"),
            Id=json_data.get("Id"),
            LegendFieldsToHide=json_data.get("LegendFieldsToHide"),
            MaxDelay=json_data.get("MaxDelay"),
            MinimumResolution=json_data.get("MinimumResolution"),
            Name=json_data.get("Name"),
            OnChartLegendDimension=json_data.get("OnChartLegendDimension"),
            PlotType=json_data.get("PlotType"),
            ProgramText=json_data.get("ProgramText"),
            ShowDataMarkers=json_data.get("ShowDataMarkers"),
            ShowEventLines=json_data.get("ShowEventLines"),
            Stacked=json_data.get("Stacked"),
            StartTime=json_data.get("StartTime"),
            Tags=json_data.get("Tags"),
            TimeRange=json_data.get("TimeRange"),
            Timezone=json_data.get("Timezone"),
            UnitPrefix=json_data.get("UnitPrefix"),
            Url=json_data.get("Url"),
            AxisLeft=deserialize_list(json_data.get("AxisLeft"), AxisLeftDefinition),
            AxisRight=deserialize_list(json_data.get("AxisRight"), AxisRightDefinition),
            EventOptions=deserialize_list(json_data.get("EventOptions"), EventOptionsDefinition),
            HistogramOptions=deserialize_list(json_data.get("HistogramOptions"), HistogramOptionsDefinition),
            LegendOptionsFields=deserialize_list(json_data.get("LegendOptionsFields"), LegendOptionsFieldsDefinition),
            VizOptions=deserialize_list(json_data.get("VizOptions"), VizOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AxisLeftDefinition(BaseModel):
    HighWatermark: Optional[float]
    HighWatermarkLabel: Optional[str]
    Label: Optional[str]
    LowWatermark: Optional[float]
    LowWatermarkLabel: Optional[str]
    MaxValue: Optional[float]
    MinValue: Optional[float]
    Watermarks: Optional[Sequence["_WatermarksDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AxisLeftDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AxisLeftDefinition"]:
        if not json_data:
            return None
        return cls(
            HighWatermark=json_data.get("HighWatermark"),
            HighWatermarkLabel=json_data.get("HighWatermarkLabel"),
            Label=json_data.get("Label"),
            LowWatermark=json_data.get("LowWatermark"),
            LowWatermarkLabel=json_data.get("LowWatermarkLabel"),
            MaxValue=json_data.get("MaxValue"),
            MinValue=json_data.get("MinValue"),
            Watermarks=deserialize_list(json_data.get("Watermarks"), WatermarksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AxisLeftDefinition = AxisLeftDefinition


@dataclass
class WatermarksDefinition(BaseModel):
    Label: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WatermarksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WatermarksDefinition"]:
        if not json_data:
            return None
        return cls(
            Label=json_data.get("Label"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WatermarksDefinition = WatermarksDefinition


@dataclass
class AxisRightDefinition(BaseModel):
    HighWatermark: Optional[float]
    HighWatermarkLabel: Optional[str]
    Label: Optional[str]
    LowWatermark: Optional[float]
    LowWatermarkLabel: Optional[str]
    MaxValue: Optional[float]
    MinValue: Optional[float]
    Watermarks: Optional[Sequence["_WatermarksDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AxisRightDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AxisRightDefinition"]:
        if not json_data:
            return None
        return cls(
            HighWatermark=json_data.get("HighWatermark"),
            HighWatermarkLabel=json_data.get("HighWatermarkLabel"),
            Label=json_data.get("Label"),
            LowWatermark=json_data.get("LowWatermark"),
            LowWatermarkLabel=json_data.get("LowWatermarkLabel"),
            MaxValue=json_data.get("MaxValue"),
            MinValue=json_data.get("MinValue"),
            Watermarks=deserialize_list(json_data.get("Watermarks"), WatermarksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AxisRightDefinition = AxisRightDefinition


@dataclass
class EventOptionsDefinition(BaseModel):
    Color: Optional[str]
    DisplayName: Optional[str]
    Label: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
            DisplayName=json_data.get("DisplayName"),
            Label=json_data.get("Label"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventOptionsDefinition = EventOptionsDefinition


@dataclass
class HistogramOptionsDefinition(BaseModel):
    ColorTheme: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HistogramOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HistogramOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ColorTheme=json_data.get("ColorTheme"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HistogramOptionsDefinition = HistogramOptionsDefinition


@dataclass
class LegendOptionsFieldsDefinition(BaseModel):
    Enabled: Optional[bool]
    Property: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LegendOptionsFieldsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LegendOptionsFieldsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Property=json_data.get("Property"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LegendOptionsFieldsDefinition = LegendOptionsFieldsDefinition


@dataclass
class VizOptionsDefinition(BaseModel):
    Axis: Optional[str]
    Color: Optional[str]
    DisplayName: Optional[str]
    Label: Optional[str]
    PlotType: Optional[str]
    ValuePrefix: Optional[str]
    ValueSuffix: Optional[str]
    ValueUnit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VizOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VizOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Axis=json_data.get("Axis"),
            Color=json_data.get("Color"),
            DisplayName=json_data.get("DisplayName"),
            Label=json_data.get("Label"),
            PlotType=json_data.get("PlotType"),
            ValuePrefix=json_data.get("ValuePrefix"),
            ValueSuffix=json_data.get("ValueSuffix"),
            ValueUnit=json_data.get("ValueUnit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VizOptionsDefinition = VizOptionsDefinition


