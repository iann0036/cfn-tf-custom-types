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
    CategoryId: Optional[str]
    CompartmentId: Optional[str]
    Description: Optional[str]
    EstimatedCostSaving: Optional[float]
    Id: Optional[str]
    Importance: Optional[str]
    Name: Optional[str]
    RecommendationId: Optional[str]
    ResourceCounts: Optional[Sequence["_ResourceCountsDefinition"]]
    State: Optional[str]
    Status: Optional[str]
    SupportedLevels: Optional[Sequence["_SupportedLevelsDefinition2"]]
    TimeCreated: Optional[str]
    TimeStatusBegin: Optional[str]
    TimeStatusEnd: Optional[str]
    TimeUpdated: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            CategoryId=json_data.get("CategoryId"),
            CompartmentId=json_data.get("CompartmentId"),
            Description=json_data.get("Description"),
            EstimatedCostSaving=json_data.get("EstimatedCostSaving"),
            Id=json_data.get("Id"),
            Importance=json_data.get("Importance"),
            Name=json_data.get("Name"),
            RecommendationId=json_data.get("RecommendationId"),
            ResourceCounts=deserialize_list(json_data.get("ResourceCounts"), ResourceCountsDefinition),
            State=json_data.get("State"),
            Status=json_data.get("Status"),
            SupportedLevels=deserialize_list(json_data.get("SupportedLevels"), SupportedLevelsDefinition2),
            TimeCreated=json_data.get("TimeCreated"),
            TimeStatusBegin=json_data.get("TimeStatusBegin"),
            TimeStatusEnd=json_data.get("TimeStatusEnd"),
            TimeUpdated=json_data.get("TimeUpdated"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ResourceCountsDefinition(BaseModel):
    Count: Optional[float]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceCountsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceCountsDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceCountsDefinition = ResourceCountsDefinition


@dataclass
class SupportedLevelsDefinition2(BaseModel):
    Items: Optional[Sequence["_SupportedLevelsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SupportedLevelsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SupportedLevelsDefinition2"]:
        if not json_data:
            return None
        return cls(
            Items=deserialize_list(json_data.get("Items"), SupportedLevelsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SupportedLevelsDefinition2 = SupportedLevelsDefinition2


@dataclass
class SupportedLevelsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SupportedLevelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SupportedLevelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SupportedLevelsDefinition = SupportedLevelsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


