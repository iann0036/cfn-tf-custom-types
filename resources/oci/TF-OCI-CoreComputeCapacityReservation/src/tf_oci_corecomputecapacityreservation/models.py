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
    AvailabilityDomain: Optional[str]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    IsDefaultReservation: Optional[bool]
    ReservedInstanceCount: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    UsedInstanceCount: Optional[str]
    InstanceReservationConfigs: Optional[Sequence["_InstanceReservationConfigsDefinition"]]
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
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            IsDefaultReservation=json_data.get("IsDefaultReservation"),
            ReservedInstanceCount=json_data.get("ReservedInstanceCount"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            UsedInstanceCount=json_data.get("UsedInstanceCount"),
            InstanceReservationConfigs=deserialize_list(json_data.get("InstanceReservationConfigs"), InstanceReservationConfigsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class InstanceReservationConfigsDefinition(BaseModel):
    FaultDomain: Optional[str]
    InstanceShape: Optional[str]
    ReservedCount: Optional[str]
    InstanceShapeConfig: Optional[Sequence["_InstanceShapeConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceReservationConfigsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceReservationConfigsDefinition"]:
        if not json_data:
            return None
        return cls(
            FaultDomain=json_data.get("FaultDomain"),
            InstanceShape=json_data.get("InstanceShape"),
            ReservedCount=json_data.get("ReservedCount"),
            InstanceShapeConfig=deserialize_list(json_data.get("InstanceShapeConfig"), InstanceShapeConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceReservationConfigsDefinition = InstanceReservationConfigsDefinition


@dataclass
class InstanceShapeConfigDefinition(BaseModel):
    MemoryInGbs: Optional[float]
    Ocpus: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceShapeConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceShapeConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MemoryInGbs=json_data.get("MemoryInGbs"),
            Ocpus=json_data.get("Ocpus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceShapeConfigDefinition = InstanceShapeConfigDefinition


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


