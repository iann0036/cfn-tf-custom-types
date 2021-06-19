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
    ClusterControllerId: Optional[str]
    ClusterName: Optional[str]
    ControllerClusterId: Optional[str]
    DesiredCapacity: Optional[float]
    Id: Optional[str]
    Location: Optional[str]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Whitelist: Optional[Sequence[str]]
    Autoscaler: Optional[Sequence["_AutoscalerDefinition"]]
    BackendServices: Optional[Sequence["_BackendServicesDefinition"]]
    ScheduledTask: Optional[Sequence["_ScheduledTaskDefinition"]]

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
            ClusterControllerId=json_data.get("ClusterControllerId"),
            ClusterName=json_data.get("ClusterName"),
            ControllerClusterId=json_data.get("ControllerClusterId"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Whitelist=json_data.get("Whitelist"),
            Autoscaler=deserialize_list(json_data.get("Autoscaler"), AutoscalerDefinition),
            BackendServices=deserialize_list(json_data.get("BackendServices"), BackendServicesDefinition),
            ScheduledTask=deserialize_list(json_data.get("ScheduledTask"), ScheduledTaskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutoscalerDefinition(BaseModel):
    AutoHeadroomPercentage: Optional[float]
    Cooldown: Optional[float]
    IsAutoConfig: Optional[bool]
    IsEnabled: Optional[bool]
    Down: Optional[Sequence["_DownDefinition"]]
    Headroom: Optional[Sequence["_HeadroomDefinition"]]
    ResourceLimits: Optional[Sequence["_ResourceLimitsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscalerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscalerDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoHeadroomPercentage=json_data.get("AutoHeadroomPercentage"),
            Cooldown=json_data.get("Cooldown"),
            IsAutoConfig=json_data.get("IsAutoConfig"),
            IsEnabled=json_data.get("IsEnabled"),
            Down=deserialize_list(json_data.get("Down"), DownDefinition),
            Headroom=deserialize_list(json_data.get("Headroom"), HeadroomDefinition),
            ResourceLimits=deserialize_list(json_data.get("ResourceLimits"), ResourceLimitsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscalerDefinition = AutoscalerDefinition


@dataclass
class DownDefinition(BaseModel):
    EvaluationPeriods: Optional[float]
    MaxScaleDownPercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DownDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DownDefinition"]:
        if not json_data:
            return None
        return cls(
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
            MaxScaleDownPercentage=json_data.get("MaxScaleDownPercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DownDefinition = DownDefinition


@dataclass
class HeadroomDefinition(BaseModel):
    CpuPerUnit: Optional[float]
    GpuPerUnit: Optional[float]
    MemoryPerUnit: Optional[float]
    NumOfUnits: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HeadroomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadroomDefinition"]:
        if not json_data:
            return None
        return cls(
            CpuPerUnit=json_data.get("CpuPerUnit"),
            GpuPerUnit=json_data.get("GpuPerUnit"),
            MemoryPerUnit=json_data.get("MemoryPerUnit"),
            NumOfUnits=json_data.get("NumOfUnits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadroomDefinition = HeadroomDefinition


@dataclass
class ResourceLimitsDefinition(BaseModel):
    MaxMemoryGib: Optional[float]
    MaxVcpu: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxMemoryGib=json_data.get("MaxMemoryGib"),
            MaxVcpu=json_data.get("MaxVcpu"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceLimitsDefinition = ResourceLimitsDefinition


@dataclass
class BackendServicesDefinition(BaseModel):
    LocationType: Optional[str]
    Scheme: Optional[str]
    ServiceName: Optional[str]
    NamedPorts: Optional[Sequence["_NamedPortsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BackendServicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendServicesDefinition"]:
        if not json_data:
            return None
        return cls(
            LocationType=json_data.get("LocationType"),
            Scheme=json_data.get("Scheme"),
            ServiceName=json_data.get("ServiceName"),
            NamedPorts=deserialize_list(json_data.get("NamedPorts"), NamedPortsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendServicesDefinition = BackendServicesDefinition


@dataclass
class NamedPortsDefinition(BaseModel):
    Name: Optional[str]
    Ports: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NamedPortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NamedPortsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Ports=json_data.get("Ports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NamedPortsDefinition = NamedPortsDefinition


@dataclass
class ScheduledTaskDefinition(BaseModel):
    ShutdownHours: Optional[Sequence["_ShutdownHoursDefinition"]]
    Tasks: Optional[Sequence["_TasksDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduledTaskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledTaskDefinition"]:
        if not json_data:
            return None
        return cls(
            ShutdownHours=deserialize_list(json_data.get("ShutdownHours"), ShutdownHoursDefinition),
            Tasks=deserialize_list(json_data.get("Tasks"), TasksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledTaskDefinition = ScheduledTaskDefinition


@dataclass
class ShutdownHoursDefinition(BaseModel):
    IsEnabled: Optional[bool]
    TimeWindows: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ShutdownHoursDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShutdownHoursDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            TimeWindows=json_data.get("TimeWindows"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShutdownHoursDefinition = ShutdownHoursDefinition


@dataclass
class TasksDefinition(BaseModel):
    BatchSizePercentage: Optional[float]
    CronExpression: Optional[str]
    IsEnabled: Optional[bool]
    TaskType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TasksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TasksDefinition"]:
        if not json_data:
            return None
        return cls(
            BatchSizePercentage=json_data.get("BatchSizePercentage"),
            CronExpression=json_data.get("CronExpression"),
            IsEnabled=json_data.get("IsEnabled"),
            TaskType=json_data.get("TaskType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TasksDefinition = TasksDefinition


