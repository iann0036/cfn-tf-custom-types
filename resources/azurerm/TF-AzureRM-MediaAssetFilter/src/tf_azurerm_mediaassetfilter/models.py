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
    AssetId: Optional[str]
    FirstQualityBitrate: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    PresentationTimeRange: Optional[Sequence["_PresentationTimeRangeDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    TrackSelection: Optional[Sequence["_TrackSelectionDefinition"]]

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
            AssetId=json_data.get("AssetId"),
            FirstQualityBitrate=json_data.get("FirstQualityBitrate"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PresentationTimeRange=deserialize_list(json_data.get("PresentationTimeRange"), PresentationTimeRangeDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            TrackSelection=deserialize_list(json_data.get("TrackSelection"), TrackSelectionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PresentationTimeRangeDefinition(BaseModel):
    EndInUnits: Optional[float]
    ForceEnd: Optional[bool]
    LiveBackoffInUnits: Optional[float]
    PresentationWindowInUnits: Optional[float]
    StartInUnits: Optional[float]
    UnitTimescaleInMiliseconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PresentationTimeRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PresentationTimeRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            EndInUnits=json_data.get("EndInUnits"),
            ForceEnd=json_data.get("ForceEnd"),
            LiveBackoffInUnits=json_data.get("LiveBackoffInUnits"),
            PresentationWindowInUnits=json_data.get("PresentationWindowInUnits"),
            StartInUnits=json_data.get("StartInUnits"),
            UnitTimescaleInMiliseconds=json_data.get("UnitTimescaleInMiliseconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PresentationTimeRangeDefinition = PresentationTimeRangeDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class TrackSelectionDefinition(BaseModel):
    Condition: Optional[Sequence["_ConditionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TrackSelectionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrackSelectionDefinition"]:
        if not json_data:
            return None
        return cls(
            Condition=deserialize_list(json_data.get("Condition"), ConditionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrackSelectionDefinition = TrackSelectionDefinition


@dataclass
class ConditionDefinition(BaseModel):
    Operation: Optional[str]
    Property: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            Operation=json_data.get("Operation"),
            Property=json_data.get("Property"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionDefinition = ConditionDefinition


