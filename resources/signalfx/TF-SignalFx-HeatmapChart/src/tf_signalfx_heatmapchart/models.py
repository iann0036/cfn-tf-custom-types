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
    DisableSampling: Optional[bool]
    GroupBy: Optional[Sequence[str]]
    HideTimestamp: Optional[bool]
    Id: Optional[str]
    MaxDelay: Optional[float]
    MinimumResolution: Optional[float]
    Name: Optional[str]
    ProgramText: Optional[str]
    RefreshInterval: Optional[float]
    SortBy: Optional[str]
    Timezone: Optional[str]
    UnitPrefix: Optional[str]
    Url: Optional[str]
    ColorRange: Optional[Sequence["_ColorRangeDefinition"]]
    ColorScale: Optional[Sequence["_ColorScaleDefinition"]]

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
            DisableSampling=json_data.get("DisableSampling"),
            GroupBy=json_data.get("GroupBy"),
            HideTimestamp=json_data.get("HideTimestamp"),
            Id=json_data.get("Id"),
            MaxDelay=json_data.get("MaxDelay"),
            MinimumResolution=json_data.get("MinimumResolution"),
            Name=json_data.get("Name"),
            ProgramText=json_data.get("ProgramText"),
            RefreshInterval=json_data.get("RefreshInterval"),
            SortBy=json_data.get("SortBy"),
            Timezone=json_data.get("Timezone"),
            UnitPrefix=json_data.get("UnitPrefix"),
            Url=json_data.get("Url"),
            ColorRange=deserialize_list(json_data.get("ColorRange"), ColorRangeDefinition),
            ColorScale=deserialize_list(json_data.get("ColorScale"), ColorScaleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ColorRangeDefinition(BaseModel):
    Color: Optional[str]
    MaxValue: Optional[float]
    MinValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ColorRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColorRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
            MaxValue=json_data.get("MaxValue"),
            MinValue=json_data.get("MinValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColorRangeDefinition = ColorRangeDefinition


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


