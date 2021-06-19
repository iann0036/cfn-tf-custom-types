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
    Id: Optional[str]
    Name: Optional[str]
    Overflow: Optional[bool]
    TimeZone: Optional[str]
    Layer: Optional[Sequence["_LayerDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Overflow=json_data.get("Overflow"),
            TimeZone=json_data.get("TimeZone"),
            Layer=deserialize_list(json_data.get("Layer"), LayerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LayerDefinition(BaseModel):
    End: Optional[str]
    Name: Optional[str]
    RotationTurnLengthSeconds: Optional[float]
    RotationVirtualStart: Optional[str]
    Start: Optional[str]
    Users: Optional[Sequence[str]]
    Restriction: Optional[Sequence["_RestrictionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LayerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LayerDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Name=json_data.get("Name"),
            RotationTurnLengthSeconds=json_data.get("RotationTurnLengthSeconds"),
            RotationVirtualStart=json_data.get("RotationVirtualStart"),
            Start=json_data.get("Start"),
            Users=json_data.get("Users"),
            Restriction=deserialize_list(json_data.get("Restriction"), RestrictionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LayerDefinition = LayerDefinition


@dataclass
class RestrictionDefinition(BaseModel):
    DurationSeconds: Optional[float]
    StartDayOfWeek: Optional[float]
    StartTimeOfDay: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RestrictionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestrictionDefinition"]:
        if not json_data:
            return None
        return cls(
            DurationSeconds=json_data.get("DurationSeconds"),
            StartDayOfWeek=json_data.get("StartDayOfWeek"),
            StartTimeOfDay=json_data.get("StartTimeOfDay"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestrictionDefinition = RestrictionDefinition


