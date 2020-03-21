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
    DashboardUrl: Optional[str]
    Editable: Optional[str]
    Icon: Optional[str]
    Title: Optional[str]
    Visibility: Optional[str]
    Filter: Optional[Sequence["_Filter"]]
    Widget: Optional[Sequence["_Widget"]]
    CompareWith: Optional[Sequence["_CompareWith"]]
    Metric: Optional[Sequence["_Metric"]]
    Presentation: Optional[Sequence["_Presentation"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DashboardUrl=json_data.get("DashboardUrl"),
            Editable=json_data.get("Editable"),
            Icon=json_data.get("Icon"),
            Title=json_data.get("Title"),
            Visibility=json_data.get("Visibility"),
            Filter=json_data.get("Filter"),
            Widget=json_data.get("Widget"),
            CompareWith=json_data.get("CompareWith"),
            Metric=json_data.get("Metric"),
            Presentation=json_data.get("Presentation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Filter:
    Attributes: Optional[Sequence[str]]
    EventTypes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            Attributes=json_data.get("Attributes"),
            EventTypes=json_data.get("EventTypes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


@dataclass
class Widget:
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
    CompareWith: Optional[Sequence["_CompareWith"]]
    Metric: Optional[Sequence["_Metric"]]

    @classmethod
    def _deserialize(
        cls: Type["_Widget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Widget"]:
        if not json_data:
            return None
        return cls(
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
            CompareWith=json_data.get("CompareWith"),
            Metric=json_data.get("Metric"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Widget = Widget


@dataclass
class CompareWith:
    OffsetDuration: Optional[str]
    Presentation: Optional[Sequence["_Presentation"]]

    @classmethod
    def _deserialize(
        cls: Type["_CompareWith"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CompareWith"]:
        if not json_data:
            return None
        return cls(
            OffsetDuration=json_data.get("OffsetDuration"),
            Presentation=json_data.get("Presentation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CompareWith = CompareWith


@dataclass
class Presentation:
    Color: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Presentation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Presentation"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Presentation = Presentation


@dataclass
class Metric:
    Name: Optional[str]
    Scope: Optional[str]
    Units: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Metric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metric"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Scope=json_data.get("Scope"),
            Units=json_data.get("Units"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metric = Metric


