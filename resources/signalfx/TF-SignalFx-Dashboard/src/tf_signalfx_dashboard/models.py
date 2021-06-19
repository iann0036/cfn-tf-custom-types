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
    AuthorizedWriterTeams: Optional[Sequence[str]]
    AuthorizedWriterUsers: Optional[Sequence[str]]
    ChartsResolution: Optional[str]
    DashboardGroup: Optional[str]
    Description: Optional[str]
    DiscoveryOptionsQuery: Optional[str]
    DiscoveryOptionsSelectors: Optional[Sequence[str]]
    EndTime: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    StartTime: Optional[float]
    TimeRange: Optional[str]
    Url: Optional[str]
    Chart: Optional[Sequence["_ChartDefinition"]]
    Column: Optional[Sequence["_ColumnDefinition"]]
    EventOverlay: Optional[Sequence["_EventOverlayDefinition"]]
    Filter: Optional[Sequence["_FilterDefinition"]]
    Grid: Optional[Sequence["_GridDefinition"]]
    SelectedEventOverlay: Optional[Sequence["_SelectedEventOverlayDefinition"]]
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
            AuthorizedWriterTeams=json_data.get("AuthorizedWriterTeams"),
            AuthorizedWriterUsers=json_data.get("AuthorizedWriterUsers"),
            ChartsResolution=json_data.get("ChartsResolution"),
            DashboardGroup=json_data.get("DashboardGroup"),
            Description=json_data.get("Description"),
            DiscoveryOptionsQuery=json_data.get("DiscoveryOptionsQuery"),
            DiscoveryOptionsSelectors=json_data.get("DiscoveryOptionsSelectors"),
            EndTime=json_data.get("EndTime"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            StartTime=json_data.get("StartTime"),
            TimeRange=json_data.get("TimeRange"),
            Url=json_data.get("Url"),
            Chart=deserialize_list(json_data.get("Chart"), ChartDefinition),
            Column=deserialize_list(json_data.get("Column"), ColumnDefinition),
            EventOverlay=deserialize_list(json_data.get("EventOverlay"), EventOverlayDefinition),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
            Grid=deserialize_list(json_data.get("Grid"), GridDefinition),
            SelectedEventOverlay=deserialize_list(json_data.get("SelectedEventOverlay"), SelectedEventOverlayDefinition),
            Variable=deserialize_list(json_data.get("Variable"), VariableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ChartDefinition(BaseModel):
    ChartId: Optional[str]
    Column: Optional[float]
    Height: Optional[float]
    Row: Optional[float]
    Width: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ChartDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChartDefinition"]:
        if not json_data:
            return None
        return cls(
            ChartId=json_data.get("ChartId"),
            Column=json_data.get("Column"),
            Height=json_data.get("Height"),
            Row=json_data.get("Row"),
            Width=json_data.get("Width"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChartDefinition = ChartDefinition


@dataclass
class ColumnDefinition(BaseModel):
    ChartIds: Optional[Sequence[str]]
    Column: Optional[float]
    Height: Optional[float]
    Width: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnDefinition"]:
        if not json_data:
            return None
        return cls(
            ChartIds=json_data.get("ChartIds"),
            Column=json_data.get("Column"),
            Height=json_data.get("Height"),
            Width=json_data.get("Width"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnDefinition = ColumnDefinition


@dataclass
class EventOverlayDefinition(BaseModel):
    Color: Optional[str]
    Label: Optional[str]
    Line: Optional[bool]
    Signal: Optional[str]
    Type: Optional[str]
    Source: Optional[Sequence["_SourceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EventOverlayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventOverlayDefinition"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
            Label=json_data.get("Label"),
            Line=json_data.get("Line"),
            Signal=json_data.get("Signal"),
            Type=json_data.get("Type"),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventOverlayDefinition = EventOverlayDefinition


@dataclass
class SourceDefinition(BaseModel):
    Negated: Optional[bool]
    Property: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Negated=json_data.get("Negated"),
            Property=json_data.get("Property"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


@dataclass
class FilterDefinition(BaseModel):
    ApplyIfExist: Optional[bool]
    Negated: Optional[bool]
    Property: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            ApplyIfExist=json_data.get("ApplyIfExist"),
            Negated=json_data.get("Negated"),
            Property=json_data.get("Property"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class GridDefinition(BaseModel):
    ChartIds: Optional[Sequence[str]]
    Height: Optional[float]
    Width: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_GridDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GridDefinition"]:
        if not json_data:
            return None
        return cls(
            ChartIds=json_data.get("ChartIds"),
            Height=json_data.get("Height"),
            Width=json_data.get("Width"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GridDefinition = GridDefinition


@dataclass
class SelectedEventOverlayDefinition(BaseModel):
    Signal: Optional[str]
    Type: Optional[str]
    Source: Optional[Sequence["_SourceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SelectedEventOverlayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelectedEventOverlayDefinition"]:
        if not json_data:
            return None
        return cls(
            Signal=json_data.get("Signal"),
            Type=json_data.get("Type"),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelectedEventOverlayDefinition = SelectedEventOverlayDefinition


@dataclass
class VariableDefinition(BaseModel):
    Alias: Optional[str]
    ApplyIfExist: Optional[bool]
    Description: Optional[str]
    Property: Optional[str]
    ReplaceOnly: Optional[bool]
    RestrictedSuggestions: Optional[bool]
    ValueRequired: Optional[bool]
    Values: Optional[Sequence[str]]
    ValuesSuggested: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VariableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VariableDefinition"]:
        if not json_data:
            return None
        return cls(
            Alias=json_data.get("Alias"),
            ApplyIfExist=json_data.get("ApplyIfExist"),
            Description=json_data.get("Description"),
            Property=json_data.get("Property"),
            ReplaceOnly=json_data.get("ReplaceOnly"),
            RestrictedSuggestions=json_data.get("RestrictedSuggestions"),
            ValueRequired=json_data.get("ValueRequired"),
            Values=json_data.get("Values"),
            ValuesSuggested=json_data.get("ValuesSuggested"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VariableDefinition = VariableDefinition


