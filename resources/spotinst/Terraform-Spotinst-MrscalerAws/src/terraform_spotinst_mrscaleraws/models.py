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
    AdditionalInfo: Optional[str]
    AdditionalPrimarySecurityGroups: Optional[Sequence[str]]
    AdditionalReplicaSecurityGroups: Optional[Sequence[str]]
    AvailabilityZones: Optional[Sequence[str]]
    ClusterId: Optional[str]
    CoreDesiredCapacity: Optional[float]
    CoreEbsOptimized: Optional[bool]
    CoreInstanceTypes: Optional[Sequence[str]]
    CoreLifecycle: Optional[str]
    CoreMaxSize: Optional[float]
    CoreMinSize: Optional[float]
    CustomAmiId: Optional[str]
    Description: Optional[str]
    EbsRootVolumeSize: Optional[float]
    Ec2KeyName: Optional[str]
    ExposeClusterId: Optional[bool]
    JobFlowRole: Optional[str]
    KeepJobFlowAlive: Optional[bool]
    LogUri: Optional[str]
    ManagedPrimarySecurityGroup: Optional[str]
    ManagedReplicaSecurityGroup: Optional[str]
    MasterEbsOptimized: Optional[bool]
    MasterInstanceTypes: Optional[Sequence[str]]
    MasterLifecycle: Optional[str]
    Name: Optional[str]
    OutputClusterId: Optional[str]
    Region: Optional[str]
    ReleaseLabel: Optional[str]
    RepoUpgradeOnBoot: Optional[str]
    Retries: Optional[float]
    SecurityConfig: Optional[str]
    ServiceAccessSecurityGroup: Optional[str]
    ServiceRole: Optional[str]
    Strategy: Optional[str]
    TaskDesiredCapacity: Optional[float]
    TaskEbsOptimized: Optional[bool]
    TaskInstanceTypes: Optional[Sequence[str]]
    TaskLifecycle: Optional[str]
    TaskMaxSize: Optional[float]
    TaskMinSize: Optional[float]
    TerminationProtected: Optional[bool]
    VisibleToAllUsers: Optional[bool]
    Applications: Optional[Sequence["_Applications"]]
    BootstrapActionsFile: Optional[Sequence["_BootstrapActionsFile"]]
    ConfigurationsFile: Optional[Sequence["_ConfigurationsFile"]]
    CoreEbsBlockDevice: Optional[Sequence["_CoreEbsBlockDevice"]]
    CoreScalingDownPolicy: Optional[Sequence["_CoreScalingDownPolicy"]]
    CoreScalingUpPolicy: Optional[Sequence["_CoreScalingUpPolicy"]]
    InstanceWeights: Optional[Sequence["_InstanceWeights"]]
    MasterEbsBlockDevice: Optional[Sequence["_MasterEbsBlockDevice"]]
    ProvisioningTimeout: Optional[Sequence["_ProvisioningTimeout"]]
    ScheduledTask: Optional[Sequence["_ScheduledTask"]]
    StepsFile: Optional[Sequence["_StepsFile"]]
    Tags: Optional[Sequence["_Tags"]]
    TaskEbsBlockDevice: Optional[Sequence["_TaskEbsBlockDevice"]]
    TaskScalingDownPolicy: Optional[Sequence["_TaskScalingDownPolicy"]]
    TaskScalingUpPolicy: Optional[Sequence["_TaskScalingUpPolicy"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdditionalInfo=json_data.get("AdditionalInfo"),
            AdditionalPrimarySecurityGroups=json_data.get("AdditionalPrimarySecurityGroups"),
            AdditionalReplicaSecurityGroups=json_data.get("AdditionalReplicaSecurityGroups"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            ClusterId=json_data.get("ClusterId"),
            CoreDesiredCapacity=json_data.get("CoreDesiredCapacity"),
            CoreEbsOptimized=json_data.get("CoreEbsOptimized"),
            CoreInstanceTypes=json_data.get("CoreInstanceTypes"),
            CoreLifecycle=json_data.get("CoreLifecycle"),
            CoreMaxSize=json_data.get("CoreMaxSize"),
            CoreMinSize=json_data.get("CoreMinSize"),
            CustomAmiId=json_data.get("CustomAmiId"),
            Description=json_data.get("Description"),
            EbsRootVolumeSize=json_data.get("EbsRootVolumeSize"),
            Ec2KeyName=json_data.get("Ec2KeyName"),
            ExposeClusterId=json_data.get("ExposeClusterId"),
            JobFlowRole=json_data.get("JobFlowRole"),
            KeepJobFlowAlive=json_data.get("KeepJobFlowAlive"),
            LogUri=json_data.get("LogUri"),
            ManagedPrimarySecurityGroup=json_data.get("ManagedPrimarySecurityGroup"),
            ManagedReplicaSecurityGroup=json_data.get("ManagedReplicaSecurityGroup"),
            MasterEbsOptimized=json_data.get("MasterEbsOptimized"),
            MasterInstanceTypes=json_data.get("MasterInstanceTypes"),
            MasterLifecycle=json_data.get("MasterLifecycle"),
            Name=json_data.get("Name"),
            OutputClusterId=json_data.get("OutputClusterId"),
            Region=json_data.get("Region"),
            ReleaseLabel=json_data.get("ReleaseLabel"),
            RepoUpgradeOnBoot=json_data.get("RepoUpgradeOnBoot"),
            Retries=json_data.get("Retries"),
            SecurityConfig=json_data.get("SecurityConfig"),
            ServiceAccessSecurityGroup=json_data.get("ServiceAccessSecurityGroup"),
            ServiceRole=json_data.get("ServiceRole"),
            Strategy=json_data.get("Strategy"),
            TaskDesiredCapacity=json_data.get("TaskDesiredCapacity"),
            TaskEbsOptimized=json_data.get("TaskEbsOptimized"),
            TaskInstanceTypes=json_data.get("TaskInstanceTypes"),
            TaskLifecycle=json_data.get("TaskLifecycle"),
            TaskMaxSize=json_data.get("TaskMaxSize"),
            TaskMinSize=json_data.get("TaskMinSize"),
            TerminationProtected=json_data.get("TerminationProtected"),
            VisibleToAllUsers=json_data.get("VisibleToAllUsers"),
            Applications=json_data.get("Applications"),
            BootstrapActionsFile=json_data.get("BootstrapActionsFile"),
            ConfigurationsFile=json_data.get("ConfigurationsFile"),
            CoreEbsBlockDevice=json_data.get("CoreEbsBlockDevice"),
            CoreScalingDownPolicy=json_data.get("CoreScalingDownPolicy"),
            CoreScalingUpPolicy=json_data.get("CoreScalingUpPolicy"),
            InstanceWeights=json_data.get("InstanceWeights"),
            MasterEbsBlockDevice=json_data.get("MasterEbsBlockDevice"),
            ProvisioningTimeout=json_data.get("ProvisioningTimeout"),
            ScheduledTask=json_data.get("ScheduledTask"),
            StepsFile=json_data.get("StepsFile"),
            Tags=json_data.get("Tags"),
            TaskEbsBlockDevice=json_data.get("TaskEbsBlockDevice"),
            TaskScalingDownPolicy=json_data.get("TaskScalingDownPolicy"),
            TaskScalingUpPolicy=json_data.get("TaskScalingUpPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Applications:
    Args: Optional[Sequence[str]]
    Name: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Applications"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Applications"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            Name=json_data.get("Name"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Applications = Applications


@dataclass
class BootstrapActionsFile:
    Bucket: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BootstrapActionsFile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BootstrapActionsFile"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BootstrapActionsFile = BootstrapActionsFile


@dataclass
class ConfigurationsFile:
    Bucket: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationsFile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationsFile"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationsFile = ConfigurationsFile


@dataclass
class CoreEbsBlockDevice:
    Iops: Optional[float]
    SizeInGb: Optional[float]
    VolumeType: Optional[str]
    VolumesPerInstance: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CoreEbsBlockDevice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoreEbsBlockDevice"]:
        if not json_data:
            return None
        return cls(
            Iops=json_data.get("Iops"),
            SizeInGb=json_data.get("SizeInGb"),
            VolumeType=json_data.get("VolumeType"),
            VolumesPerInstance=json_data.get("VolumesPerInstance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CoreEbsBlockDevice = CoreEbsBlockDevice


@dataclass
class CoreScalingDownPolicy:
    ActionType: Optional[str]
    Adjustment: Optional[str]
    Cooldown: Optional[float]
    Dimensions: Optional[Sequence["_Dimensions"]]
    EvaluationPeriods: Optional[float]
    MaxTargetCapacity: Optional[str]
    Maximum: Optional[str]
    MetricName: Optional[str]
    MinTargetCapacity: Optional[str]
    Minimum: Optional[str]
    Namespace: Optional[str]
    Operator: Optional[str]
    Period: Optional[float]
    PolicyName: Optional[str]
    Statistic: Optional[str]
    Target: Optional[str]
    Threshold: Optional[float]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CoreScalingDownPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoreScalingDownPolicy"]:
        if not json_data:
            return None
        return cls(
            ActionType=json_data.get("ActionType"),
            Adjustment=json_data.get("Adjustment"),
            Cooldown=json_data.get("Cooldown"),
            Dimensions=json_data.get("Dimensions"),
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
            MaxTargetCapacity=json_data.get("MaxTargetCapacity"),
            Maximum=json_data.get("Maximum"),
            MetricName=json_data.get("MetricName"),
            MinTargetCapacity=json_data.get("MinTargetCapacity"),
            Minimum=json_data.get("Minimum"),
            Namespace=json_data.get("Namespace"),
            Operator=json_data.get("Operator"),
            Period=json_data.get("Period"),
            PolicyName=json_data.get("PolicyName"),
            Statistic=json_data.get("Statistic"),
            Target=json_data.get("Target"),
            Threshold=json_data.get("Threshold"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CoreScalingDownPolicy = CoreScalingDownPolicy


@dataclass
class Dimensions:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dimensions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dimensions"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dimensions = Dimensions


@dataclass
class CoreScalingUpPolicy:
    ActionType: Optional[str]
    Adjustment: Optional[str]
    Cooldown: Optional[float]
    Dimensions: Optional[Sequence["_Dimensions2"]]
    EvaluationPeriods: Optional[float]
    MaxTargetCapacity: Optional[str]
    Maximum: Optional[str]
    MetricName: Optional[str]
    MinTargetCapacity: Optional[str]
    Minimum: Optional[str]
    Namespace: Optional[str]
    Operator: Optional[str]
    Period: Optional[float]
    PolicyName: Optional[str]
    Statistic: Optional[str]
    Target: Optional[str]
    Threshold: Optional[float]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CoreScalingUpPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoreScalingUpPolicy"]:
        if not json_data:
            return None
        return cls(
            ActionType=json_data.get("ActionType"),
            Adjustment=json_data.get("Adjustment"),
            Cooldown=json_data.get("Cooldown"),
            Dimensions=json_data.get("Dimensions"),
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
            MaxTargetCapacity=json_data.get("MaxTargetCapacity"),
            Maximum=json_data.get("Maximum"),
            MetricName=json_data.get("MetricName"),
            MinTargetCapacity=json_data.get("MinTargetCapacity"),
            Minimum=json_data.get("Minimum"),
            Namespace=json_data.get("Namespace"),
            Operator=json_data.get("Operator"),
            Period=json_data.get("Period"),
            PolicyName=json_data.get("PolicyName"),
            Statistic=json_data.get("Statistic"),
            Target=json_data.get("Target"),
            Threshold=json_data.get("Threshold"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CoreScalingUpPolicy = CoreScalingUpPolicy


@dataclass
class Dimensions2:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dimensions2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dimensions2"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dimensions2 = Dimensions2


@dataclass
class InstanceWeights:
    InstanceType: Optional[str]
    WeightedCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceWeights"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceWeights"]:
        if not json_data:
            return None
        return cls(
            InstanceType=json_data.get("InstanceType"),
            WeightedCapacity=json_data.get("WeightedCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceWeights = InstanceWeights


@dataclass
class MasterEbsBlockDevice:
    Iops: Optional[float]
    SizeInGb: Optional[float]
    VolumeType: Optional[str]
    VolumesPerInstance: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MasterEbsBlockDevice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterEbsBlockDevice"]:
        if not json_data:
            return None
        return cls(
            Iops=json_data.get("Iops"),
            SizeInGb=json_data.get("SizeInGb"),
            VolumeType=json_data.get("VolumeType"),
            VolumesPerInstance=json_data.get("VolumesPerInstance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterEbsBlockDevice = MasterEbsBlockDevice


@dataclass
class ProvisioningTimeout:
    Timeout: Optional[float]
    TimeoutAction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProvisioningTimeout"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProvisioningTimeout"]:
        if not json_data:
            return None
        return cls(
            Timeout=json_data.get("Timeout"),
            TimeoutAction=json_data.get("TimeoutAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProvisioningTimeout = ProvisioningTimeout


@dataclass
class ScheduledTask:
    Cron: Optional[str]
    DesiredCapacity: Optional[str]
    InstanceGroupType: Optional[str]
    IsEnabled: Optional[bool]
    MaxCapacity: Optional[str]
    MinCapacity: Optional[str]
    TaskType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduledTask"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledTask"]:
        if not json_data:
            return None
        return cls(
            Cron=json_data.get("Cron"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            InstanceGroupType=json_data.get("InstanceGroupType"),
            IsEnabled=json_data.get("IsEnabled"),
            MaxCapacity=json_data.get("MaxCapacity"),
            MinCapacity=json_data.get("MinCapacity"),
            TaskType=json_data.get("TaskType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledTask = ScheduledTask


@dataclass
class StepsFile:
    Bucket: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StepsFile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepsFile"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepsFile = StepsFile


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class TaskEbsBlockDevice:
    Iops: Optional[float]
    SizeInGb: Optional[float]
    VolumeType: Optional[str]
    VolumesPerInstance: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TaskEbsBlockDevice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskEbsBlockDevice"]:
        if not json_data:
            return None
        return cls(
            Iops=json_data.get("Iops"),
            SizeInGb=json_data.get("SizeInGb"),
            VolumeType=json_data.get("VolumeType"),
            VolumesPerInstance=json_data.get("VolumesPerInstance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskEbsBlockDevice = TaskEbsBlockDevice


@dataclass
class TaskScalingDownPolicy:
    ActionType: Optional[str]
    Adjustment: Optional[str]
    Cooldown: Optional[float]
    Dimensions: Optional[Sequence["_Dimensions3"]]
    EvaluationPeriods: Optional[float]
    MaxTargetCapacity: Optional[str]
    Maximum: Optional[str]
    MetricName: Optional[str]
    MinTargetCapacity: Optional[str]
    Minimum: Optional[str]
    Namespace: Optional[str]
    Operator: Optional[str]
    Period: Optional[float]
    PolicyName: Optional[str]
    Statistic: Optional[str]
    Target: Optional[str]
    Threshold: Optional[float]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaskScalingDownPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskScalingDownPolicy"]:
        if not json_data:
            return None
        return cls(
            ActionType=json_data.get("ActionType"),
            Adjustment=json_data.get("Adjustment"),
            Cooldown=json_data.get("Cooldown"),
            Dimensions=json_data.get("Dimensions"),
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
            MaxTargetCapacity=json_data.get("MaxTargetCapacity"),
            Maximum=json_data.get("Maximum"),
            MetricName=json_data.get("MetricName"),
            MinTargetCapacity=json_data.get("MinTargetCapacity"),
            Minimum=json_data.get("Minimum"),
            Namespace=json_data.get("Namespace"),
            Operator=json_data.get("Operator"),
            Period=json_data.get("Period"),
            PolicyName=json_data.get("PolicyName"),
            Statistic=json_data.get("Statistic"),
            Target=json_data.get("Target"),
            Threshold=json_data.get("Threshold"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskScalingDownPolicy = TaskScalingDownPolicy


@dataclass
class Dimensions3:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dimensions3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dimensions3"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dimensions3 = Dimensions3


@dataclass
class TaskScalingUpPolicy:
    ActionType: Optional[str]
    Adjustment: Optional[str]
    Cooldown: Optional[float]
    Dimensions: Optional[Sequence["_Dimensions4"]]
    EvaluationPeriods: Optional[float]
    MaxTargetCapacity: Optional[str]
    Maximum: Optional[str]
    MetricName: Optional[str]
    MinTargetCapacity: Optional[str]
    Minimum: Optional[str]
    Namespace: Optional[str]
    Operator: Optional[str]
    Period: Optional[float]
    PolicyName: Optional[str]
    Statistic: Optional[str]
    Target: Optional[str]
    Threshold: Optional[float]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaskScalingUpPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskScalingUpPolicy"]:
        if not json_data:
            return None
        return cls(
            ActionType=json_data.get("ActionType"),
            Adjustment=json_data.get("Adjustment"),
            Cooldown=json_data.get("Cooldown"),
            Dimensions=json_data.get("Dimensions"),
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
            MaxTargetCapacity=json_data.get("MaxTargetCapacity"),
            Maximum=json_data.get("Maximum"),
            MetricName=json_data.get("MetricName"),
            MinTargetCapacity=json_data.get("MinTargetCapacity"),
            Minimum=json_data.get("Minimum"),
            Namespace=json_data.get("Namespace"),
            Operator=json_data.get("Operator"),
            Period=json_data.get("Period"),
            PolicyName=json_data.get("PolicyName"),
            Statistic=json_data.get("Statistic"),
            Target=json_data.get("Target"),
            Threshold=json_data.get("Threshold"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskScalingUpPolicy = TaskScalingUpPolicy


@dataclass
class Dimensions4:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dimensions4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dimensions4"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dimensions4 = Dimensions4


