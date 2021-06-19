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
    ColorBy: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IsTimestampHidden: Optional[bool]
    MaxDelay: Optional[float]
    MaxPrecision: Optional[float]
    Name: Optional[str]
    ProgramText: Optional[str]
    RefreshInterval: Optional[float]
    SecondaryVisualization: Optional[str]
    ShowSparkLine: Optional[bool]
    Timezone: Optional[str]
    UnitPrefix: Optional[str]
    Url: Optional[str]
    ColorScale: Optional[Sequence["_ColorScaleDefinition"]]
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
            ColorBy=json_data.get("ColorBy"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IsTimestampHidden=json_data.get("IsTimestampHidden"),
            MaxDelay=json_data.get("MaxDelay"),
            MaxPrecision=json_data.get("MaxPrecision"),
            Name=json_data.get("Name"),
            ProgramText=json_data.get("ProgramText"),
            RefreshInterval=json_data.get("RefreshInterval"),
            SecondaryVisualization=json_data.get("SecondaryVisualization"),
            ShowSparkLine=json_data.get("ShowSparkLine"),
            Timezone=json_data.get("Timezone"),
            UnitPrefix=json_data.get("UnitPrefix"),
            Url=json_data.get("Url"),
            ColorScale=deserialize_list(json_data.get("ColorScale"), ColorScaleDefinition),
            VizOptions=deserialize_list(json_data.get("VizOptions"), VizOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ColorScaleDefinition(BaseModel):
    Color: Optional[str]
    Gt: Optional[float]
    Gte: Optional[float]
    Lt: Optional[float]
    Lte: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ColorScaleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColorScaleDefinition"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
            Gt=json_data.get("Gt"),
            Gte=json_data.get("Gte"),
            Lt=json_data.get("Lt"),
            Lte=json_data.get("Lte"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColorScaleDefinition = ColorScaleDefinition


@dataclass
class VizOptionsDefinition(BaseModel):
    Color: Optional[str]
    DisplayName: Optional[str]
    Label: Optional[str]
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
            Color=json_data.get("Color"),
            DisplayName=json_data.get("DisplayName"),
            Label=json_data.get("Label"),
            ValuePrefix=json_data.get("ValuePrefix"),
            ValueSuffix=json_data.get("ValueSuffix"),
            ValueUnit=json_data.get("ValueUnit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VizOptionsDefinition = VizOptionsDefinition


