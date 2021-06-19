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
    AssociatePublicIpAddress: Optional[bool]
    Blacklist: Optional[Sequence[str]]
    ControllerId: Optional[str]
    DesiredCapacity: Optional[float]
    DrainingTimeout: Optional[float]
    EbsOptimized: Optional[bool]
    FallbackToOndemand: Optional[bool]
    GracePeriod: Optional[float]
    IamInstanceProfile: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    KeyName: Optional[str]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Monitoring: Optional[bool]
    Name: Optional[str]
    Region: Optional[str]
    RootVolumeSize: Optional[float]
    SecurityGroups: Optional[Sequence[str]]
    SpotPercentage: Optional[float]
    SubnetIds: Optional[Sequence[str]]
    UseAsTemplateOnly: Optional[bool]
    UserData: Optional[str]
    UtilizeCommitments: Optional[bool]
    UtilizeReservedInstances: Optional[bool]
    Whitelist: Optional[Sequence[str]]
    Autoscaler: Optional[Sequence["_AutoscalerDefinition"]]
    LoadBalancers: Optional[Sequence["_LoadBalancersDefinition"]]
    ScheduledTask: Optional[Sequence["_ScheduledTaskDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    UpdatePolicy: Optional[Sequence["_UpdatePolicyDefinition"]]

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
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            Blacklist=json_data.get("Blacklist"),
            ControllerId=json_data.get("ControllerId"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            DrainingTimeout=json_data.get("DrainingTimeout"),
            EbsOptimized=json_data.get("EbsOptimized"),
            FallbackToOndemand=json_data.get("FallbackToOndemand"),
            GracePeriod=json_data.get("GracePeriod"),
            IamInstanceProfile=json_data.get("IamInstanceProfile"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            KeyName=json_data.get("KeyName"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Monitoring=json_data.get("Monitoring"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            RootVolumeSize=json_data.get("RootVolumeSize"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SpotPercentage=json_data.get("SpotPercentage"),
            SubnetIds=json_data.get("SubnetIds"),
            UseAsTemplateOnly=json_data.get("UseAsTemplateOnly"),
            UserData=json_data.get("UserData"),
            UtilizeCommitments=json_data.get("UtilizeCommitments"),
            UtilizeReservedInstances=json_data.get("UtilizeReservedInstances"),
            Whitelist=json_data.get("Whitelist"),
            Autoscaler=deserialize_list(json_data.get("Autoscaler"), AutoscalerDefinition),
            LoadBalancers=deserialize_list(json_data.get("LoadBalancers"), LoadBalancersDefinition),
            ScheduledTask=deserialize_list(json_data.get("ScheduledTask"), ScheduledTaskDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            UpdatePolicy=deserialize_list(json_data.get("UpdatePolicy"), UpdatePolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutoscalerDefinition(BaseModel):
    AutoHeadroomPercentage: Optional[float]
    AutoscaleCooldown: Optional[float]
    AutoscaleIsAutoConfig: Optional[bool]
    AutoscaleIsEnabled: Optional[bool]
    AutoscaleDown: Optional[Sequence["_AutoscaleDownDefinition"]]
    AutoscaleHeadroom: Optional[Sequence["_AutoscaleHeadroomDefinition"]]
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
            AutoscaleCooldown=json_data.get("AutoscaleCooldown"),
            AutoscaleIsAutoConfig=json_data.get("AutoscaleIsAutoConfig"),
            AutoscaleIsEnabled=json_data.get("AutoscaleIsEnabled"),
            AutoscaleDown=deserialize_list(json_data.get("AutoscaleDown"), AutoscaleDownDefinition),
            AutoscaleHeadroom=deserialize_list(json_data.get("AutoscaleHeadroom"), AutoscaleHeadroomDefinition),
            ResourceLimits=deserialize_list(json_data.get("ResourceLimits"), ResourceLimitsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscalerDefinition = AutoscalerDefinition


@dataclass
class AutoscaleDownDefinition(BaseModel):
    EvaluationPeriods: Optional[float]
    MaxScaleDownPercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleDownDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleDownDefinition"]:
        if not json_data:
            return None
        return cls(
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
            MaxScaleDownPercentage=json_data.get("MaxScaleDownPercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleDownDefinition = AutoscaleDownDefinition


@dataclass
class AutoscaleHeadroomDefinition(BaseModel):
    CpuPerUnit: Optional[float]
    GpuPerUnit: Optional[float]
    MemoryPerUnit: Optional[float]
    NumOfUnits: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleHeadroomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleHeadroomDefinition"]:
        if not json_data:
            return None
        return cls(
            CpuPerUnit=json_data.get("CpuPerUnit"),
            GpuPerUnit=json_data.get("GpuPerUnit"),
            MemoryPerUnit=json_data.get("MemoryPerUnit"),
            NumOfUnits=json_data.get("NumOfUnits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleHeadroomDefinition = AutoscaleHeadroomDefinition


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
class LoadBalancersDefinition(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancersDefinition"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancersDefinition = LoadBalancersDefinition


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
            CronExpression=json_data.get("CronExpression"),
            IsEnabled=json_data.get("IsEnabled"),
            TaskType=json_data.get("TaskType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TasksDefinition = TasksDefinition


@dataclass
class TagsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class UpdatePolicyDefinition(BaseModel):
    ShouldRoll: Optional[bool]
    RollConfig: Optional[Sequence["_RollConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UpdatePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpdatePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            ShouldRoll=json_data.get("ShouldRoll"),
            RollConfig=deserialize_list(json_data.get("RollConfig"), RollConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpdatePolicyDefinition = UpdatePolicyDefinition


@dataclass
class RollConfigDefinition(BaseModel):
    BatchSizePercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RollConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RollConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BatchSizePercentage=json_data.get("BatchSizePercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RollConfigDefinition = RollConfigDefinition


