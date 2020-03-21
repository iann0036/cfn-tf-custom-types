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
    GraphStyle: Optional[str]
    Id: Optional[str]
    Left: Optional[Sequence["_Left"]]
    LineStyle: Optional[str]
    Name: Optional[str]
    Notes: Optional[str]
    Right: Optional[Sequence["_Right"]]
    Tags: Optional[Sequence[str]]
    Guide: Optional[Sequence["_Guide"]]
    Metric: Optional[Sequence["_Metric"]]
    MetricCluster: Optional[Sequence["_MetricCluster"]]

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
            GraphStyle=json_data.get("GraphStyle"),
            Id=json_data.get("Id"),
            Left=json_data.get("Left"),
            LineStyle=json_data.get("LineStyle"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Right=json_data.get("Right"),
            Tags=json_data.get("Tags"),
            Guide=json_data.get("Guide"),
            Metric=json_data.get("Metric"),
            MetricCluster=json_data.get("MetricCluster"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Left:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Left"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Left"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Left = Left


@dataclass
class Right:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Right"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Right"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Right = Right


@dataclass
class Guide:
    Color: Optional[str]
    Formula: Optional[str]
    Hidden: Optional[bool]
    LegendFormula: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Guide"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Guide"]:
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
_Guide = Guide


@dataclass
class Metric:
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
        cls: Type["_Metric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metric"]:
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
_Metric = Metric


@dataclass
class MetricCluster:
    Active: Optional[bool]
    Aggregate: Optional[str]
    Axis: Optional[str]
    Color: Optional[str]
    Name: Optional[str]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricCluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricCluster"]:
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
_MetricCluster = MetricCluster


