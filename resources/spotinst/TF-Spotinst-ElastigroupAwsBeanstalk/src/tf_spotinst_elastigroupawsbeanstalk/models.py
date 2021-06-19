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
    BeanstalkEnvironmentId: Optional[str]
    BeanstalkEnvironmentName: Optional[str]
    DesiredCapacity: Optional[float]
    Id: Optional[str]
    InstanceTypesSpot: Optional[Sequence[str]]
    Maintenance: Optional[str]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Name: Optional[str]
    Product: Optional[str]
    Region: Optional[str]
    DeploymentPreferences: Optional[Sequence["_DeploymentPreferencesDefinition"]]
    ManagedActions: Optional[Sequence["_ManagedActionsDefinition"]]
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
            BeanstalkEnvironmentId=json_data.get("BeanstalkEnvironmentId"),
            BeanstalkEnvironmentName=json_data.get("BeanstalkEnvironmentName"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            Id=json_data.get("Id"),
            InstanceTypesSpot=json_data.get("InstanceTypesSpot"),
            Maintenance=json_data.get("Maintenance"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Name=json_data.get("Name"),
            Product=json_data.get("Product"),
            Region=json_data.get("Region"),
            DeploymentPreferences=deserialize_list(json_data.get("DeploymentPreferences"), DeploymentPreferencesDefinition),
            ManagedActions=deserialize_list(json_data.get("ManagedActions"), ManagedActionsDefinition),
            ScheduledTask=deserialize_list(json_data.get("ScheduledTask"), ScheduledTaskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DeploymentPreferencesDefinition(BaseModel):
    AutomaticRoll: Optional[bool]
    BatchSizePercentage: Optional[float]
    GracePeriod: Optional[float]
    Strategy: Optional[Sequence["_StrategyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentPreferencesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentPreferencesDefinition"]:
        if not json_data:
            return None
        return cls(
            AutomaticRoll=json_data.get("AutomaticRoll"),
            BatchSizePercentage=json_data.get("BatchSizePercentage"),
            GracePeriod=json_data.get("GracePeriod"),
            Strategy=deserialize_list(json_data.get("Strategy"), StrategyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentPreferencesDefinition = DeploymentPreferencesDefinition


@dataclass
class StrategyDefinition(BaseModel):
    Action: Optional[str]
    ShouldDrainInstances: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_StrategyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StrategyDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            ShouldDrainInstances=json_data.get("ShouldDrainInstances"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StrategyDefinition = StrategyDefinition


@dataclass
class ManagedActionsDefinition(BaseModel):
    PlatformUpdate: Optional[Sequence["_PlatformUpdateDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedActionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedActionsDefinition"]:
        if not json_data:
            return None
        return cls(
            PlatformUpdate=deserialize_list(json_data.get("PlatformUpdate"), PlatformUpdateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedActionsDefinition = ManagedActionsDefinition


@dataclass
class PlatformUpdateDefinition(BaseModel):
    PerformAt: Optional[str]
    TimeWindow: Optional[str]
    UpdateLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlatformUpdateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlatformUpdateDefinition"]:
        if not json_data:
            return None
        return cls(
            PerformAt=json_data.get("PerformAt"),
            TimeWindow=json_data.get("TimeWindow"),
            UpdateLevel=json_data.get("UpdateLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlatformUpdateDefinition = PlatformUpdateDefinition


@dataclass
class ScheduledTaskDefinition(BaseModel):
    Adjustment: Optional[str]
    AdjustmentPercentage: Optional[str]
    BatchSizePercentage: Optional[str]
    CronExpression: Optional[str]
    Frequency: Optional[str]
    GracePeriod: Optional[str]
    IsEnabled: Optional[bool]
    MaxCapacity: Optional[str]
    MinCapacity: Optional[str]
    ScaleMaxCapacity: Optional[str]
    ScaleMinCapacity: Optional[str]
    ScaleTargetCapacity: Optional[str]
    StartTime: Optional[str]
    TargetCapacity: Optional[str]
    TaskType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduledTaskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledTaskDefinition"]:
        if not json_data:
            return None
        return cls(
            Adjustment=json_data.get("Adjustment"),
            AdjustmentPercentage=json_data.get("AdjustmentPercentage"),
            BatchSizePercentage=json_data.get("BatchSizePercentage"),
            CronExpression=json_data.get("CronExpression"),
            Frequency=json_data.get("Frequency"),
            GracePeriod=json_data.get("GracePeriod"),
            IsEnabled=json_data.get("IsEnabled"),
            MaxCapacity=json_data.get("MaxCapacity"),
            MinCapacity=json_data.get("MinCapacity"),
            ScaleMaxCapacity=json_data.get("ScaleMaxCapacity"),
            ScaleMinCapacity=json_data.get("ScaleMinCapacity"),
            ScaleTargetCapacity=json_data.get("ScaleTargetCapacity"),
            StartTime=json_data.get("StartTime"),
            TargetCapacity=json_data.get("TargetCapacity"),
            TaskType=json_data.get("TaskType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledTaskDefinition = ScheduledTaskDefinition


