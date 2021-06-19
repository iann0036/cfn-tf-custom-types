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
    DashboardUrl: Optional[str]
    Editable: Optional[str]
    GridColumnCount: Optional[float]
    Icon: Optional[str]
    Id: Optional[str]
    Title: Optional[str]
    Visibility: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]
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
            DashboardUrl=json_data.get("DashboardUrl"),
            Editable=json_data.get("Editable"),
            GridColumnCount=json_data.get("GridColumnCount"),
            Icon=json_data.get("Icon"),
            Id=json_data.get("Id"),
            Title=json_data.get("Title"),
            Visibility=json_data.get("Visibility"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
            Widget=deserialize_list(json_data.get("Widget"), WidgetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FilterDefinition(BaseModel):
    Attributes: Optional[Sequence[str]]
    EventTypes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Attributes=json_data.get("Attributes"),
            EventTypes=json_data.get("EventTypes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class WidgetDefinition(BaseModel):
    AccountId: Optional[float]
    Column: Optional[float]
    DrilldownDashboardId: Optional[float]
    Duration: Optional[float]
    EndTime: Optional[float]
    EntityIds: Optional[Sequence[float]]
    Facet: Optional[str]
    Height: Optional[float]
    Limit: Optional[float]
    Notes: Optional[str]
    Nrql: Optional[str]
    OrderBy: Optional[str]
    Row: Optional[float]
    Source: Optional[str]
    ThresholdRed: Optional[float]
    ThresholdYellow: Optional[float]
    Title: Optional[str]
    Visualization: Optional[str]
    Width: Optional[float]
    CompareWith: Optional[Sequence["_CompareWithDefinition"]]
    Metric: Optional[Sequence["_MetricDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WidgetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WidgetDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            Column=json_data.get("Column"),
            DrilldownDashboardId=json_data.get("DrilldownDashboardId"),
            Duration=json_data.get("Duration"),
            EndTime=json_data.get("EndTime"),
            EntityIds=json_data.get("EntityIds"),
            Facet=json_data.get("Facet"),
            Height=json_data.get("Height"),
            Limit=json_data.get("Limit"),
            Notes=json_data.get("Notes"),
            Nrql=json_data.get("Nrql"),
            OrderBy=json_data.get("OrderBy"),
            Row=json_data.get("Row"),
            Source=json_data.get("Source"),
            ThresholdRed=json_data.get("ThresholdRed"),
            ThresholdYellow=json_data.get("ThresholdYellow"),
            Title=json_data.get("Title"),
            Visualization=json_data.get("Visualization"),
            Width=json_data.get("Width"),
            CompareWith=deserialize_list(json_data.get("CompareWith"), CompareWithDefinition),
            Metric=deserialize_list(json_data.get("Metric"), MetricDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WidgetDefinition = WidgetDefinition


@dataclass
class CompareWithDefinition(BaseModel):
    OffsetDuration: Optional[str]
    Presentation: Optional[Sequence["_PresentationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CompareWithDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CompareWithDefinition"]:
        if not json_data:
            return None
        return cls(
            OffsetDuration=json_data.get("OffsetDuration"),
            Presentation=deserialize_list(json_data.get("Presentation"), PresentationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CompareWithDefinition = CompareWithDefinition


@dataclass
class PresentationDefinition(BaseModel):
    Color: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PresentationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PresentationDefinition"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PresentationDefinition = PresentationDefinition


@dataclass
class MetricDefinition(BaseModel):
    Name: Optional[str]
    Scope: Optional[str]
    Units: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Scope=json_data.get("Scope"),
            Units=json_data.get("Units"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDefinition = MetricDefinition


