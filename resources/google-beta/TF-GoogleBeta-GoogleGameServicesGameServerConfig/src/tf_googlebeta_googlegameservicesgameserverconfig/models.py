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
    ConfigId: Optional[str]
    DeploymentId: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Location: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    FleetConfigs: Optional[Sequence["_FleetConfigsDefinition"]]
    ScalingConfigs: Optional[Sequence["_ScalingConfigsDefinition"]]
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
            ConfigId=json_data.get("ConfigId"),
            DeploymentId=json_data.get("DeploymentId"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            FleetConfigs=deserialize_list(json_data.get("FleetConfigs"), FleetConfigsDefinition),
            ScalingConfigs=deserialize_list(json_data.get("ScalingConfigs"), ScalingConfigsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class FleetConfigsDefinition(BaseModel):
    FleetSpec: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FleetConfigsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FleetConfigsDefinition"]:
        if not json_data:
            return None
        return cls(
            FleetSpec=json_data.get("FleetSpec"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FleetConfigsDefinition = FleetConfigsDefinition


@dataclass
class ScalingConfigsDefinition(BaseModel):
    FleetAutoscalerSpec: Optional[str]
    Name: Optional[str]
    Schedules: Optional[Sequence["_SchedulesDefinition"]]
    Selectors: Optional[Sequence["_SelectorsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingConfigsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingConfigsDefinition"]:
        if not json_data:
            return None
        return cls(
            FleetAutoscalerSpec=json_data.get("FleetAutoscalerSpec"),
            Name=json_data.get("Name"),
            Schedules=deserialize_list(json_data.get("Schedules"), SchedulesDefinition),
            Selectors=deserialize_list(json_data.get("Selectors"), SelectorsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingConfigsDefinition = ScalingConfigsDefinition


@dataclass
class SchedulesDefinition(BaseModel):
    CronJobDuration: Optional[str]
    CronSpec: Optional[str]
    EndTime: Optional[str]
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchedulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchedulesDefinition"]:
        if not json_data:
            return None
        return cls(
            CronJobDuration=json_data.get("CronJobDuration"),
            CronSpec=json_data.get("CronSpec"),
            EndTime=json_data.get("EndTime"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchedulesDefinition = SchedulesDefinition


@dataclass
class SelectorsDefinition(BaseModel):
    Labels: Optional[Sequence["_LabelsDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_SelectorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelectorsDefinition"]:
        if not json_data:
            return None
        return cls(
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelectorsDefinition = SelectorsDefinition


@dataclass
class LabelsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition2 = LabelsDefinition2


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


