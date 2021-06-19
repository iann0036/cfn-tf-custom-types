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
    Action: Optional[Sequence["_ActionDefinition"]]
    CategoryId: Optional[str]
    CompartmentId: Optional[str]
    CompartmentName: Optional[str]
    EstimatedCostSaving: Optional[float]
    ExtendedMetadata: Optional[Sequence["_ExtendedMetadataDefinition"]]
    Id: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    RecommendationId: Optional[str]
    ResourceActionId: Optional[str]
    ResourceId: Optional[str]
    ResourceType: Optional[str]
    State: Optional[str]
    Status: Optional[str]
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
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            CategoryId=json_data.get("CategoryId"),
            CompartmentId=json_data.get("CompartmentId"),
            CompartmentName=json_data.get("CompartmentName"),
            EstimatedCostSaving=json_data.get("EstimatedCostSaving"),
            ExtendedMetadata=deserialize_list(json_data.get("ExtendedMetadata"), ExtendedMetadataDefinition),
            Id=json_data.get("Id"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            RecommendationId=json_data.get("RecommendationId"),
            ResourceActionId=json_data.get("ResourceActionId"),
            ResourceId=json_data.get("ResourceId"),
            ResourceType=json_data.get("ResourceType"),
            State=json_data.get("State"),
            Status=json_data.get("Status"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeStatusBegin=json_data.get("TimeStatusBegin"),
            TimeStatusEnd=json_data.get("TimeStatusEnd"),
            TimeUpdated=json_data.get("TimeUpdated"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ActionDefinition(BaseModel):
    Description: Optional[str]
    Type: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class ExtendedMetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtendedMetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtendedMetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtendedMetadataDefinition = ExtendedMetadataDefinition


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


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


