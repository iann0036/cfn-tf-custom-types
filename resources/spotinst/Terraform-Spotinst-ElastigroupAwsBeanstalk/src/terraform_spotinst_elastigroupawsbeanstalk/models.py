# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    BeanstalkEnvironmentId: Optional[str]
    BeanstalkEnvironmentName: Optional[str]
    DesiredCapacity: Optional[float]
    InstanceTypesSpot: Optional[Sequence[str]]
    Maintenance: Optional[str]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Name: Optional[str]
    Product: Optional[str]
    Region: Optional[str]
    DeploymentPreferences: Optional[Sequence["_DeploymentPreferences"]]
    ManagedActions: Optional[Sequence["_ManagedActions"]]
    ScheduledTask: Optional[Sequence["_ScheduledTask"]]
    Strategy: Optional[Sequence["_Strategy"]]
    PlatformUpdate: Optional[Sequence["_PlatformUpdate"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BeanstalkEnvironmentId=json_data.get("BeanstalkEnvironmentId"),
            BeanstalkEnvironmentName=json_data.get("BeanstalkEnvironmentName"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            InstanceTypesSpot=json_data.get("InstanceTypesSpot"),
            Maintenance=json_data.get("Maintenance"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Name=json_data.get("Name"),
            Product=json_data.get("Product"),
            Region=json_data.get("Region"),
            DeploymentPreferences=json_data.get("DeploymentPreferences"),
            ManagedActions=json_data.get("ManagedActions"),
            ScheduledTask=json_data.get("ScheduledTask"),
            Strategy=json_data.get("Strategy"),
            PlatformUpdate=json_data.get("PlatformUpdate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DeploymentPreferences:
    AutomaticRoll: Optional[bool]
    BatchSizePercentage: Optional[float]
    GracePeriod: Optional[float]
    Strategy: Optional[Sequence["_Strategy"]]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentPreferences"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentPreferences"]:
        if not json_data:
            return None
        return cls(
            AutomaticRoll=json_data.get("AutomaticRoll"),
            BatchSizePercentage=json_data.get("BatchSizePercentage"),
            GracePeriod=json_data.get("GracePeriod"),
            Strategy=json_data.get("Strategy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentPreferences = DeploymentPreferences


@dataclass
class Strategy:
    Action: Optional[str]
    ShouldDrainInstances: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Strategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Strategy"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            ShouldDrainInstances=json_data.get("ShouldDrainInstances"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Strategy = Strategy


@dataclass
class ManagedActions:
    PlatformUpdate: Optional[Sequence["_PlatformUpdate"]]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedActions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedActions"]:
        if not json_data:
            return None
        return cls(
            PlatformUpdate=json_data.get("PlatformUpdate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedActions = ManagedActions


@dataclass
class PlatformUpdate:
    PerformAt: Optional[str]
    TimeWindow: Optional[str]
    UpdateLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlatformUpdate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlatformUpdate"]:
        if not json_data:
            return None
        return cls(
            PerformAt=json_data.get("PerformAt"),
            TimeWindow=json_data.get("TimeWindow"),
            UpdateLevel=json_data.get("UpdateLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlatformUpdate = PlatformUpdate


@dataclass
class ScheduledTask:
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
        cls: Type["_ScheduledTask"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledTask"]:
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
_ScheduledTask = ScheduledTask


