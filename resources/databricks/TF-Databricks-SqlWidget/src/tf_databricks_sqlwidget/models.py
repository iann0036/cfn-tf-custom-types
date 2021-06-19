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
    DashboardId: Optional[str]
    Id: Optional[str]
    Text: Optional[str]
    VisualizationId: Optional[str]
    WidgetId: Optional[str]
    Parameter: Optional[Sequence["_ParameterDefinition"]]
    Position: Optional[Sequence["_PositionDefinition"]]

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
            DashboardId=json_data.get("DashboardId"),
            Id=json_data.get("Id"),
            Text=json_data.get("Text"),
            VisualizationId=json_data.get("VisualizationId"),
            WidgetId=json_data.get("WidgetId"),
            Parameter=deserialize_list(json_data.get("Parameter"), ParameterDefinition),
            Position=deserialize_list(json_data.get("Position"), PositionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ParameterDefinition(BaseModel):
    MapTo: Optional[str]
    Name: Optional[str]
    Title: Optional[str]
    Type: Optional[str]
    Value: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterDefinition"]:
        if not json_data:
            return None
        return cls(
            MapTo=json_data.get("MapTo"),
            Name=json_data.get("Name"),
            Title=json_data.get("Title"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterDefinition = ParameterDefinition


@dataclass
class PositionDefinition(BaseModel):
    PosX: Optional[float]
    PosY: Optional[float]
    SizeX: Optional[float]
    SizeY: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PositionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PositionDefinition"]:
        if not json_data:
            return None
        return cls(
            PosX=json_data.get("PosX"),
            PosY=json_data.get("PosY"),
            SizeX=json_data.get("SizeX"),
            SizeY=json_data.get("SizeY"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PositionDefinition = PositionDefinition


