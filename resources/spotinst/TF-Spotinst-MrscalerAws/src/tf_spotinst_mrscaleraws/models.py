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
    CoreUnit: Optional[str]
    CustomAmiId: Optional[str]
    Description: Optional[str]
    EbsRootVolumeSize: Optional[float]
    Ec2KeyName: Optional[str]
    ExposeClusterId: Optional[bool]
    Id: Optional[str]
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
    TaskUnit: Optional[str]
    TerminationProtected: Optional[bool]
    VisibleToAllUsers: Optional[bool]
    Applications: Optional[Sequence["_ApplicationsDefinition"]]
    BootstrapActionsFile: Optional[Sequence["_BootstrapActionsFileDefinition"]]
    ConfigurationsFile: Optional[Sequence["_ConfigurationsFileDefinition"]]
    CoreEbsBlockDevice: Optional[Sequence["_CoreEbsBlockDeviceDefinition"]]
    CoreScalingDownPolicy: Optional[Sequence["_CoreScalingDownPolicyDefinition"]]
    CoreScalingUpPolicy: Optional[Sequence["_CoreScalingUpPolicyDefinition"]]
    InstanceWeights: Optional[Sequence["_InstanceWeightsDefinition"]]
    MasterEbsBlockDevice: Optional[Sequence["_MasterEbsBlockDeviceDefinition"]]
    ProvisioningTimeout: Optional[Sequence["_ProvisioningTimeoutDefinition"]]
    ScheduledTask: Optional[Sequence["_ScheduledTaskDefinition"]]
    StepsFile: Optional[Sequence["_StepsFileDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TaskEbsBlockDevice: Optional[Sequence["_TaskEbsBlockDeviceDefinition"]]
    TaskScalingDownPolicy: Optional[Sequence["_TaskScalingDownPolicyDefinition"]]
    TaskScalingUpPolicy: Optional[Sequence["_TaskScalingUpPolicyDefinition"]]
    TerminationPolicies: Optional[Sequence["_TerminationPoliciesDefinition"]]

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
            CoreUnit=json_data.get("CoreUnit"),
            CustomAmiId=json_data.get("CustomAmiId"),
            Description=json_data.get("Description"),
            EbsRootVolumeSize=json_data.get("EbsRootVolumeSize"),
            Ec2KeyName=json_data.get("Ec2KeyName"),
            ExposeClusterId=json_data.get("ExposeClusterId"),
            Id=json_data.get("Id"),
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
            TaskUnit=json_data.get("TaskUnit"),
            TerminationProtected=json_data.get("TerminationProtected"),
            VisibleToAllUsers=json_data.get("VisibleToAllUsers"),
            Applications=deserialize_list(json_data.get("Applications"), ApplicationsDefinition),
            BootstrapActionsFile=deserialize_list(json_data.get("BootstrapActionsFile"), BootstrapActionsFileDefinition),
            ConfigurationsFile=deserialize_list(json_data.get("ConfigurationsFile"), ConfigurationsFileDefinition),
            CoreEbsBlockDevice=deserialize_list(json_data.get("CoreEbsBlockDevice"), CoreEbsBlockDeviceDefinition),
            CoreScalingDownPolicy=deserialize_list(json_data.get("CoreScalingDownPolicy"), CoreScalingDownPolicyDefinition),
            CoreScalingUpPolicy=deserialize_list(json_data.get("CoreScalingUpPolicy"), CoreScalingUpPolicyDefinition),
            InstanceWeights=deserialize_list(json_data.get("InstanceWeights"), InstanceWeightsDefinition),
            MasterEbsBlockDevice=deserialize_list(json_data.get("MasterEbsBlockDevice"), MasterEbsBlockDeviceDefinition),
            ProvisioningTimeout=deserialize_list(json_data.get("ProvisioningTimeout"), ProvisioningTimeoutDefinition),
            ScheduledTask=deserialize_list(json_data.get("ScheduledTask"), ScheduledTaskDefinition),
            StepsFile=deserialize_list(json_data.get("StepsFile"), StepsFileDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TaskEbsBlockDevice=deserialize_list(json_data.get("TaskEbsBlockDevice"), TaskEbsBlockDeviceDefinition),
            TaskScalingDownPolicy=deserialize_list(json_data.get("TaskScalingDownPolicy"), TaskScalingDownPolicyDefinition),
            TaskScalingUpPolicy=deserialize_list(json_data.get("TaskScalingUpPolicy"), TaskScalingUpPolicyDefinition),
            TerminationPolicies=deserialize_list(json_data.get("TerminationPolicies"), TerminationPoliciesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ApplicationsDefinition(BaseModel):
    Args: Optional[Sequence[str]]
    Name: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationsDefinition"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            Name=json_data.get("Name"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationsDefinition = ApplicationsDefinition


@dataclass
class BootstrapActionsFileDefinition(BaseModel):
    Bucket: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BootstrapActionsFileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BootstrapActionsFileDefinition"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BootstrapActionsFileDefinition = BootstrapActionsFileDefinition


@dataclass
class ConfigurationsFileDefinition(BaseModel):
    Bucket: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationsFileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationsFileDefinition"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationsFileDefinition = ConfigurationsFileDefinition


@dataclass
class CoreEbsBlockDeviceDefinition(BaseModel):
    Iops: Optional[float]
    SizeInGb: Optional[float]
    VolumeType: Optional[str]
    VolumesPerInstance: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CoreEbsBlockDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoreEbsBlockDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            Iops=json_data.get("Iops"),
            SizeInGb=json_data.get("SizeInGb"),
            VolumeType=json_data.get("VolumeType"),
            VolumesPerInstance=json_data.get("VolumesPerInstance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CoreEbsBlockDeviceDefinition = CoreEbsBlockDeviceDefinition


@dataclass
class CoreScalingDownPolicyDefinition(BaseModel):
    ActionType: Optional[str]
    Adjustment: Optional[str]
    Cooldown: Optional[float]
    Dimensions: Optional[Sequence["_DimensionsDefinition"]]
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
        cls: Type["_CoreScalingDownPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoreScalingDownPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionType=json_data.get("ActionType"),
            Adjustment=json_data.get("Adjustment"),
            Cooldown=json_data.get("Cooldown"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition),
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
_CoreScalingDownPolicyDefinition = CoreScalingDownPolicyDefinition


@dataclass
class DimensionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionsDefinition = DimensionsDefinition


@dataclass
class CoreScalingUpPolicyDefinition(BaseModel):
    ActionType: Optional[str]
    Adjustment: Optional[str]
    Cooldown: Optional[float]
    Dimensions: Optional[Sequence["_DimensionsDefinition2"]]
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
        cls: Type["_CoreScalingUpPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoreScalingUpPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionType=json_data.get("ActionType"),
            Adjustment=json_data.get("Adjustment"),
            Cooldown=json_data.get("Cooldown"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition2),
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
_CoreScalingUpPolicyDefinition = CoreScalingUpPolicyDefinition


@dataclass
class DimensionsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionsDefinition2 = DimensionsDefinition2


@dataclass
class InstanceWeightsDefinition(BaseModel):
    InstanceType: Optional[str]
    WeightedCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceWeightsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceWeightsDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceType=json_data.get("InstanceType"),
            WeightedCapacity=json_data.get("WeightedCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceWeightsDefinition = InstanceWeightsDefinition


@dataclass
class MasterEbsBlockDeviceDefinition(BaseModel):
    Iops: Optional[float]
    SizeInGb: Optional[float]
    VolumeType: Optional[str]
    VolumesPerInstance: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MasterEbsBlockDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterEbsBlockDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            Iops=json_data.get("Iops"),
            SizeInGb=json_data.get("SizeInGb"),
            VolumeType=json_data.get("VolumeType"),
            VolumesPerInstance=json_data.get("VolumesPerInstance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterEbsBlockDeviceDefinition = MasterEbsBlockDeviceDefinition


@dataclass
class ProvisioningTimeoutDefinition(BaseModel):
    Timeout: Optional[float]
    TimeoutAction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProvisioningTimeoutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProvisioningTimeoutDefinition"]:
        if not json_data:
            return None
        return cls(
            Timeout=json_data.get("Timeout"),
            TimeoutAction=json_data.get("TimeoutAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProvisioningTimeoutDefinition = ProvisioningTimeoutDefinition


@dataclass
class ScheduledTaskDefinition(BaseModel):
    Cron: Optional[str]
    DesiredCapacity: Optional[str]
    InstanceGroupType: Optional[str]
    IsEnabled: Optional[bool]
    MaxCapacity: Optional[str]
    MinCapacity: Optional[str]
    TaskType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduledTaskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledTaskDefinition"]:
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
_ScheduledTaskDefinition = ScheduledTaskDefinition


@dataclass
class StepsFileDefinition(BaseModel):
    Bucket: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StepsFileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepsFileDefinition"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepsFileDefinition = StepsFileDefinition


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
class TaskEbsBlockDeviceDefinition(BaseModel):
    Iops: Optional[float]
    SizeInGb: Optional[float]
    VolumeType: Optional[str]
    VolumesPerInstance: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TaskEbsBlockDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskEbsBlockDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            Iops=json_data.get("Iops"),
            SizeInGb=json_data.get("SizeInGb"),
            VolumeType=json_data.get("VolumeType"),
            VolumesPerInstance=json_data.get("VolumesPerInstance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskEbsBlockDeviceDefinition = TaskEbsBlockDeviceDefinition


@dataclass
class TaskScalingDownPolicyDefinition(BaseModel):
    ActionType: Optional[str]
    Adjustment: Optional[str]
    Cooldown: Optional[float]
    Dimensions: Optional[Sequence["_DimensionsDefinition3"]]
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
        cls: Type["_TaskScalingDownPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskScalingDownPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionType=json_data.get("ActionType"),
            Adjustment=json_data.get("Adjustment"),
            Cooldown=json_data.get("Cooldown"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition3),
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
_TaskScalingDownPolicyDefinition = TaskScalingDownPolicyDefinition


@dataclass
class DimensionsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionsDefinition3 = DimensionsDefinition3


@dataclass
class TaskScalingUpPolicyDefinition(BaseModel):
    ActionType: Optional[str]
    Adjustment: Optional[str]
    Cooldown: Optional[float]
    Dimensions: Optional[Sequence["_DimensionsDefinition4"]]
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
        cls: Type["_TaskScalingUpPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskScalingUpPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionType=json_data.get("ActionType"),
            Adjustment=json_data.get("Adjustment"),
            Cooldown=json_data.get("Cooldown"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition4),
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
_TaskScalingUpPolicyDefinition = TaskScalingUpPolicyDefinition


@dataclass
class DimensionsDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionsDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionsDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionsDefinition4 = DimensionsDefinition4


@dataclass
class TerminationPoliciesDefinition(BaseModel):
    Statements: Optional[Sequence["_StatementsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TerminationPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TerminationPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Statements=deserialize_list(json_data.get("Statements"), StatementsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TerminationPoliciesDefinition = TerminationPoliciesDefinition


@dataclass
class StatementsDefinition(BaseModel):
    EvaluationPeriods: Optional[float]
    MetricName: Optional[str]
    Namespace: Optional[str]
    Operator: Optional[str]
    Period: Optional[float]
    Statistic: Optional[str]
    Threshold: Optional[float]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatementsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatementsDefinition"]:
        if not json_data:
            return None
        return cls(
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            Operator=json_data.get("Operator"),
            Period=json_data.get("Period"),
            Statistic=json_data.get("Statistic"),
            Threshold=json_data.get("Threshold"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatementsDefinition = StatementsDefinition


