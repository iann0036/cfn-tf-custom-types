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
    Id: Optional[str]
    Unknowns: Optional[str]
    DashboardMetadata: Optional[Sequence["_DashboardMetadataDefinition"]]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Tile: Optional[Sequence["_TileDefinition"]]

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
            Id=json_data.get("Id"),
            Unknowns=json_data.get("Unknowns"),
            DashboardMetadata=deserialize_list(json_data.get("DashboardMetadata"), DashboardMetadataDefinition),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Tile=deserialize_list(json_data.get("Tile"), TileDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DashboardMetadataDefinition(BaseModel):
    Name: Optional[str]
    Owner: Optional[str]
    Shared: Optional[bool]
    Tags: Optional[Sequence[str]]
    Unknowns: Optional[str]
    ValidFilterKeys: Optional[Sequence[str]]
    DynamicFilters: Optional[Sequence["_DynamicFiltersDefinition"]]
    Filter: Optional[Sequence["_FilterDefinition"]]
    SharingDetails: Optional[Sequence["_SharingDetailsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DashboardMetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DashboardMetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Owner=json_data.get("Owner"),
            Shared=json_data.get("Shared"),
            Tags=json_data.get("Tags"),
            Unknowns=json_data.get("Unknowns"),
            ValidFilterKeys=json_data.get("ValidFilterKeys"),
            DynamicFilters=deserialize_list(json_data.get("DynamicFilters"), DynamicFiltersDefinition),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
            SharingDetails=deserialize_list(json_data.get("SharingDetails"), SharingDetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DashboardMetadataDefinition = DashboardMetadataDefinition


@dataclass
class DynamicFiltersDefinition(BaseModel):
    Filters: Optional[Sequence[str]]
    TagSuggestionTypes: Optional[Sequence[str]]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicFiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicFiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            Filters=json_data.get("Filters"),
            TagSuggestionTypes=json_data.get("TagSuggestionTypes"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicFiltersDefinition = DynamicFiltersDefinition


@dataclass
class FilterDefinition(BaseModel):
    EntityType: Optional[str]
    Match: Optional[Sequence["_MatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            EntityType=json_data.get("EntityType"),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class MatchDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class SharingDetailsDefinition(BaseModel):
    LinkShared: Optional[bool]
    Published: Optional[bool]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SharingDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SharingDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            LinkShared=json_data.get("LinkShared"),
            Published=json_data.get("Published"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SharingDetailsDefinition = SharingDetailsDefinition


@dataclass
class MetadataDefinition(BaseModel):
    ClusterVersion: Optional[str]
    ConfigurationVersions: Optional[Sequence[float]]
    CurrentConfigurationVersions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterVersion=json_data.get("ClusterVersion"),
            ConfigurationVersions=json_data.get("ConfigurationVersions"),
            CurrentConfigurationVersions=json_data.get("CurrentConfigurationVersions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class TileDefinition(BaseModel):
    AssignedEntities: Optional[Sequence[str]]
    ChartVisible: Optional[bool]
    Configured: Optional[bool]
    CustomName: Optional[str]
    ExcludeMaintenanceWindows: Optional[bool]
    Limit: Optional[float]
    Markdown: Optional[str]
    Metric: Optional[str]
    Name: Optional[str]
    Query: Optional[str]
    TileType: Optional[str]
    TimeFrameShift: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    Visualization: Optional[str]
    Bounds: Optional[Sequence["_BoundsDefinition"]]
    Filter: Optional[Sequence["_FilterDefinition"]]
    FilterConfig: Optional[Sequence["_FilterConfigDefinition"]]
    VisualizationConfig: Optional[Sequence["_VisualizationConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TileDefinition"]:
        if not json_data:
            return None
        return cls(
            AssignedEntities=json_data.get("AssignedEntities"),
            ChartVisible=json_data.get("ChartVisible"),
            Configured=json_data.get("Configured"),
            CustomName=json_data.get("CustomName"),
            ExcludeMaintenanceWindows=json_data.get("ExcludeMaintenanceWindows"),
            Limit=json_data.get("Limit"),
            Markdown=json_data.get("Markdown"),
            Metric=json_data.get("Metric"),
            Name=json_data.get("Name"),
            Query=json_data.get("Query"),
            TileType=json_data.get("TileType"),
            TimeFrameShift=json_data.get("TimeFrameShift"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Visualization=json_data.get("Visualization"),
            Bounds=deserialize_list(json_data.get("Bounds"), BoundsDefinition),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
            FilterConfig=deserialize_list(json_data.get("FilterConfig"), FilterConfigDefinition),
            VisualizationConfig=deserialize_list(json_data.get("VisualizationConfig"), VisualizationConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TileDefinition = TileDefinition


@dataclass
class BoundsDefinition(BaseModel):
    Height: Optional[float]
    Left: Optional[float]
    Top: Optional[float]
    Unknowns: Optional[str]
    Width: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BoundsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BoundsDefinition"]:
        if not json_data:
            return None
        return cls(
            Height=json_data.get("Height"),
            Left=json_data.get("Left"),
            Top=json_data.get("Top"),
            Unknowns=json_data.get("Unknowns"),
            Width=json_data.get("Width"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BoundsDefinition = BoundsDefinition


@dataclass
class FilterConfigDefinition(BaseModel):
    CustomName: Optional[str]
    DefaultName: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    ChartConfig: Optional[Sequence["_ChartConfigDefinition"]]
    Filters: Optional[Sequence["_FiltersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomName=json_data.get("CustomName"),
            DefaultName=json_data.get("DefaultName"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            ChartConfig=deserialize_list(json_data.get("ChartConfig"), ChartConfigDefinition),
            Filters=deserialize_list(json_data.get("Filters"), FiltersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterConfigDefinition = FilterConfigDefinition


@dataclass
class ChartConfigDefinition(BaseModel):
    AxisLimits: Optional[Sequence["_AxisLimitsDefinition"]]
    LeftAxisCustomUnit: Optional[str]
    Legend: Optional[bool]
    RightAxisCustomUnit: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]
    ResultMetadata: Optional[Sequence["_ResultMetadataDefinition"]]
    Series: Optional[Sequence["_SeriesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ChartConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChartConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AxisLimits=deserialize_list(json_data.get("AxisLimits"), AxisLimitsDefinition),
            LeftAxisCustomUnit=json_data.get("LeftAxisCustomUnit"),
            Legend=json_data.get("Legend"),
            RightAxisCustomUnit=json_data.get("RightAxisCustomUnit"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            ResultMetadata=deserialize_list(json_data.get("ResultMetadata"), ResultMetadataDefinition),
            Series=deserialize_list(json_data.get("Series"), SeriesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChartConfigDefinition = ChartConfigDefinition


@dataclass
class AxisLimitsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AxisLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AxisLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AxisLimitsDefinition = AxisLimitsDefinition


@dataclass
class ResultMetadataDefinition(BaseModel):
    Config: Optional[Sequence["_ConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResultMetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResultMetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResultMetadataDefinition = ResultMetadataDefinition


@dataclass
class ConfigDefinition(BaseModel):
    CustomColor: Optional[str]
    Key: Optional[str]
    LastModified: Optional[float]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomColor=json_data.get("CustomColor"),
            Key=json_data.get("Key"),
            LastModified=json_data.get("LastModified"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


@dataclass
class SeriesDefinition(BaseModel):
    Aggregation: Optional[str]
    AggregationRate: Optional[str]
    EntityType: Optional[str]
    Metric: Optional[str]
    Percentile: Optional[float]
    SortAscending: Optional[bool]
    SortColumn: Optional[bool]
    Type: Optional[str]
    Unknowns: Optional[str]
    Dimension: Optional[Sequence["_DimensionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SeriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Aggregation=json_data.get("Aggregation"),
            AggregationRate=json_data.get("AggregationRate"),
            EntityType=json_data.get("EntityType"),
            Metric=json_data.get("Metric"),
            Percentile=json_data.get("Percentile"),
            SortAscending=json_data.get("SortAscending"),
            SortColumn=json_data.get("SortColumn"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
            Dimension=deserialize_list(json_data.get("Dimension"), DimensionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeriesDefinition = SeriesDefinition


@dataclass
class DimensionDefinition(BaseModel):
    EntityDimension: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Unknowns: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionDefinition"]:
        if not json_data:
            return None
        return cls(
            EntityDimension=json_data.get("EntityDimension"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Unknowns=json_data.get("Unknowns"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionDefinition = DimensionDefinition


@dataclass
class FiltersDefinition(BaseModel):
    Filter: Optional[Sequence["_FilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FiltersDefinition = FiltersDefinition


@dataclass
class VisualizationConfigDefinition(BaseModel):
    HasAxisBucketing: Optional[bool]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VisualizationConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VisualizationConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            HasAxisBucketing=json_data.get("HasAxisBucketing"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VisualizationConfigDefinition = VisualizationConfigDefinition


