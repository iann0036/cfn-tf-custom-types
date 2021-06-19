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
    Description: Optional[str]
    GraphStyle: Optional[str]
    Id: Optional[str]
    Left: Optional[Sequence["_LeftDefinition"]]
    LineStyle: Optional[str]
    Name: Optional[str]
    Notes: Optional[str]
    Right: Optional[Sequence["_RightDefinition"]]
    Tags: Optional[Sequence[str]]
    Guide: Optional[Sequence["_GuideDefinition"]]
    Metric: Optional[Sequence["_MetricDefinition"]]
    MetricCluster: Optional[Sequence["_MetricClusterDefinition"]]

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
            Description=json_data.get("Description"),
            GraphStyle=json_data.get("GraphStyle"),
            Id=json_data.get("Id"),
            Left=deserialize_list(json_data.get("Left"), LeftDefinition),
            LineStyle=json_data.get("LineStyle"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Right=deserialize_list(json_data.get("Right"), RightDefinition),
            Tags=json_data.get("Tags"),
            Guide=deserialize_list(json_data.get("Guide"), GuideDefinition),
            Metric=deserialize_list(json_data.get("Metric"), MetricDefinition),
            MetricCluster=deserialize_list(json_data.get("MetricCluster"), MetricClusterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LeftDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LeftDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LeftDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LeftDefinition = LeftDefinition


@dataclass
class RightDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RightDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RightDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RightDefinition = RightDefinition


@dataclass
class GuideDefinition(BaseModel):
    Color: Optional[str]
    Formula: Optional[str]
    Hidden: Optional[bool]
    LegendFormula: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuideDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuideDefinition"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
            Formula=json_data.get("Formula"),
            Hidden=json_data.get("Hidden"),
            LegendFormula=json_data.get("LegendFormula"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuideDefinition = GuideDefinition


@dataclass
class MetricDefinition(BaseModel):
    Active: Optional[bool]
    Alpha: Optional[str]
    Axis: Optional[str]
    Caql: Optional[str]
    Check: Optional[str]
    Color: Optional[str]
    Formula: Optional[str]
    Function: Optional[str]
    LegendFormula: Optional[str]
    MetricName: Optional[str]
    MetricType: Optional[str]
    Name: Optional[str]
    Search: Optional[str]
    Stack: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDefinition"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
            Alpha=json_data.get("Alpha"),
            Axis=json_data.get("Axis"),
            Caql=json_data.get("Caql"),
            Check=json_data.get("Check"),
            Color=json_data.get("Color"),
            Formula=json_data.get("Formula"),
            Function=json_data.get("Function"),
            LegendFormula=json_data.get("LegendFormula"),
            MetricName=json_data.get("MetricName"),
            MetricType=json_data.get("MetricType"),
            Name=json_data.get("Name"),
            Search=json_data.get("Search"),
            Stack=json_data.get("Stack"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDefinition = MetricDefinition


@dataclass
class MetricClusterDefinition(BaseModel):
    Active: Optional[bool]
    Aggregate: Optional[str]
    Axis: Optional[str]
    Color: Optional[str]
    Name: Optional[str]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricClusterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricClusterDefinition"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
            Aggregate=json_data.get("Aggregate"),
            Axis=json_data.get("Axis"),
            Color=json_data.get("Color"),
            Name=json_data.get("Name"),
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricClusterDefinition = MetricClusterDefinition


