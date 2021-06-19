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
    AvailabilityZones: Optional[Sequence[str]]
    BlockDevicesMode: Optional[str]
    CapacityUnit: Optional[str]
    CpuCredits: Optional[str]
    Description: Optional[str]
    DesiredCapacity: Optional[float]
    DrainingTimeout: Optional[float]
    EbsOptimized: Optional[bool]
    ElasticIps: Optional[Sequence[str]]
    ElasticLoadBalancers: Optional[Sequence[str]]
    EnableMonitoring: Optional[bool]
    FallbackToOndemand: Optional[bool]
    HealthCheckGracePeriod: Optional[float]
    HealthCheckType: Optional[str]
    HealthCheckUnhealthyDurationBeforeReplacement: Optional[float]
    IamInstanceProfile: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    InstanceTypesOndemand: Optional[str]
    InstanceTypesPreferredSpot: Optional[Sequence[str]]
    InstanceTypesSpot: Optional[Sequence[str]]
    KeyName: Optional[str]
    LifetimePeriod: Optional[str]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    MinimumInstanceLifetime: Optional[float]
    Name: Optional[str]
    OndemandCount: Optional[float]
    Orientation: Optional[str]
    PersistBlockDevices: Optional[bool]
    PersistPrivateIp: Optional[bool]
    PersistRootDevice: Optional[bool]
    PlacementTenancy: Optional[str]
    PreferredAvailabilityZones: Optional[Sequence[str]]
    PrivateIps: Optional[Sequence[str]]
    Product: Optional[str]
    Region: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    ShutdownScript: Optional[str]
    SpotPercentage: Optional[float]
    SubnetIds: Optional[Sequence[str]]
    TargetGroupArns: Optional[Sequence[str]]
    UserData: Optional[str]
    UtilizeCommitments: Optional[bool]
    UtilizeReservedInstances: Optional[bool]
    WaitForCapacity: Optional[float]
    WaitForCapacityTimeout: Optional[float]
    CpuOptions: Optional[Sequence["_CpuOptionsDefinition"]]
    EbsBlockDevice: Optional[Sequence["_EbsBlockDeviceDefinition"]]
    EphemeralBlockDevice: Optional[Sequence["_EphemeralBlockDeviceDefinition"]]
    InstanceTypesWeights: Optional[Sequence["_InstanceTypesWeightsDefinition"]]
    IntegrationBeanstalk: Optional[Sequence["_IntegrationBeanstalkDefinition"]]
    IntegrationCodedeploy: Optional[Sequence["_IntegrationCodedeployDefinition"]]
    IntegrationDockerSwarm: Optional[Sequence["_IntegrationDockerSwarmDefinition"]]
    IntegrationEcs: Optional[Sequence["_IntegrationEcsDefinition"]]
    IntegrationGitlab: Optional[Sequence["_IntegrationGitlabDefinition"]]
    IntegrationKubernetes: Optional[Sequence["_IntegrationKubernetesDefinition"]]
    IntegrationMesosphere: Optional[Sequence["_IntegrationMesosphereDefinition"]]
    IntegrationMultaiRuntime: Optional[Sequence["_IntegrationMultaiRuntimeDefinition"]]
    IntegrationNomad: Optional[Sequence["_IntegrationNomadDefinition"]]
    IntegrationRancher: Optional[Sequence["_IntegrationRancherDefinition"]]
    IntegrationRoute53: Optional[Sequence["_IntegrationRoute53Definition"]]
    MetadataOptions: Optional[Sequence["_MetadataOptionsDefinition"]]
    MultaiTargetSets: Optional[Sequence["_MultaiTargetSetsDefinition"]]
    NetworkInterface: Optional[Sequence["_NetworkInterfaceDefinition"]]
    RevertToSpot: Optional[Sequence["_RevertToSpotDefinition"]]
    ScalingDownPolicy: Optional[Sequence["_ScalingDownPolicyDefinition"]]
    ScalingStrategy: Optional[Sequence["_ScalingStrategyDefinition"]]
    ScalingTargetPolicy: Optional[Sequence["_ScalingTargetPolicyDefinition"]]
    ScalingUpPolicy: Optional[Sequence["_ScalingUpPolicyDefinition"]]
    ScheduledTask: Optional[Sequence["_ScheduledTaskDefinition"]]
    Signal: Optional[Sequence["_SignalDefinition"]]
    StatefulDeallocation: Optional[Sequence["_StatefulDeallocationDefinition"]]
    StatefulInstanceAction: Optional[Sequence["_StatefulInstanceActionDefinition"]]
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
            AvailabilityZones=json_data.get("AvailabilityZones"),
            BlockDevicesMode=json_data.get("BlockDevicesMode"),
            CapacityUnit=json_data.get("CapacityUnit"),
            CpuCredits=json_data.get("CpuCredits"),
            Description=json_data.get("Description"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            DrainingTimeout=json_data.get("DrainingTimeout"),
            EbsOptimized=json_data.get("EbsOptimized"),
            ElasticIps=json_data.get("ElasticIps"),
            ElasticLoadBalancers=json_data.get("ElasticLoadBalancers"),
            EnableMonitoring=json_data.get("EnableMonitoring"),
            FallbackToOndemand=json_data.get("FallbackToOndemand"),
            HealthCheckGracePeriod=json_data.get("HealthCheckGracePeriod"),
            HealthCheckType=json_data.get("HealthCheckType"),
            HealthCheckUnhealthyDurationBeforeReplacement=json_data.get("HealthCheckUnhealthyDurationBeforeReplacement"),
            IamInstanceProfile=json_data.get("IamInstanceProfile"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            InstanceTypesOndemand=json_data.get("InstanceTypesOndemand"),
            InstanceTypesPreferredSpot=json_data.get("InstanceTypesPreferredSpot"),
            InstanceTypesSpot=json_data.get("InstanceTypesSpot"),
            KeyName=json_data.get("KeyName"),
            LifetimePeriod=json_data.get("LifetimePeriod"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            MinimumInstanceLifetime=json_data.get("MinimumInstanceLifetime"),
            Name=json_data.get("Name"),
            OndemandCount=json_data.get("OndemandCount"),
            Orientation=json_data.get("Orientation"),
            PersistBlockDevices=json_data.get("PersistBlockDevices"),
            PersistPrivateIp=json_data.get("PersistPrivateIp"),
            PersistRootDevice=json_data.get("PersistRootDevice"),
            PlacementTenancy=json_data.get("PlacementTenancy"),
            PreferredAvailabilityZones=json_data.get("PreferredAvailabilityZones"),
            PrivateIps=json_data.get("PrivateIps"),
            Product=json_data.get("Product"),
            Region=json_data.get("Region"),
            SecurityGroups=json_data.get("SecurityGroups"),
            ShutdownScript=json_data.get("ShutdownScript"),
            SpotPercentage=json_data.get("SpotPercentage"),
            SubnetIds=json_data.get("SubnetIds"),
            TargetGroupArns=json_data.get("TargetGroupArns"),
            UserData=json_data.get("UserData"),
            UtilizeCommitments=json_data.get("UtilizeCommitments"),
            UtilizeReservedInstances=json_data.get("UtilizeReservedInstances"),
            WaitForCapacity=json_data.get("WaitForCapacity"),
            WaitForCapacityTimeout=json_data.get("WaitForCapacityTimeout"),
            CpuOptions=deserialize_list(json_data.get("CpuOptions"), CpuOptionsDefinition),
            EbsBlockDevice=deserialize_list(json_data.get("EbsBlockDevice"), EbsBlockDeviceDefinition),
            EphemeralBlockDevice=deserialize_list(json_data.get("EphemeralBlockDevice"), EphemeralBlockDeviceDefinition),
            InstanceTypesWeights=deserialize_list(json_data.get("InstanceTypesWeights"), InstanceTypesWeightsDefinition),
            IntegrationBeanstalk=deserialize_list(json_data.get("IntegrationBeanstalk"), IntegrationBeanstalkDefinition),
            IntegrationCodedeploy=deserialize_list(json_data.get("IntegrationCodedeploy"), IntegrationCodedeployDefinition),
            IntegrationDockerSwarm=deserialize_list(json_data.get("IntegrationDockerSwarm"), IntegrationDockerSwarmDefinition),
            IntegrationEcs=deserialize_list(json_data.get("IntegrationEcs"), IntegrationEcsDefinition),
            IntegrationGitlab=deserialize_list(json_data.get("IntegrationGitlab"), IntegrationGitlabDefinition),
            IntegrationKubernetes=deserialize_list(json_data.get("IntegrationKubernetes"), IntegrationKubernetesDefinition),
            IntegrationMesosphere=deserialize_list(json_data.get("IntegrationMesosphere"), IntegrationMesosphereDefinition),
            IntegrationMultaiRuntime=deserialize_list(json_data.get("IntegrationMultaiRuntime"), IntegrationMultaiRuntimeDefinition),
            IntegrationNomad=deserialize_list(json_data.get("IntegrationNomad"), IntegrationNomadDefinition),
            IntegrationRancher=deserialize_list(json_data.get("IntegrationRancher"), IntegrationRancherDefinition),
            IntegrationRoute53=deserialize_list(json_data.get("IntegrationRoute53"), IntegrationRoute53Definition),
            MetadataOptions=deserialize_list(json_data.get("MetadataOptions"), MetadataOptionsDefinition),
            MultaiTargetSets=deserialize_list(json_data.get("MultaiTargetSets"), MultaiTargetSetsDefinition),
            NetworkInterface=deserialize_list(json_data.get("NetworkInterface"), NetworkInterfaceDefinition),
            RevertToSpot=deserialize_list(json_data.get("RevertToSpot"), RevertToSpotDefinition),
            ScalingDownPolicy=deserialize_list(json_data.get("ScalingDownPolicy"), ScalingDownPolicyDefinition),
            ScalingStrategy=deserialize_list(json_data.get("ScalingStrategy"), ScalingStrategyDefinition),
            ScalingTargetPolicy=deserialize_list(json_data.get("ScalingTargetPolicy"), ScalingTargetPolicyDefinition),
            ScalingUpPolicy=deserialize_list(json_data.get("ScalingUpPolicy"), ScalingUpPolicyDefinition),
            ScheduledTask=deserialize_list(json_data.get("ScheduledTask"), ScheduledTaskDefinition),
            Signal=deserialize_list(json_data.get("Signal"), SignalDefinition),
            StatefulDeallocation=deserialize_list(json_data.get("StatefulDeallocation"), StatefulDeallocationDefinition),
            StatefulInstanceAction=deserialize_list(json_data.get("StatefulInstanceAction"), StatefulInstanceActionDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            UpdatePolicy=deserialize_list(json_data.get("UpdatePolicy"), UpdatePolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CpuOptionsDefinition(BaseModel):
    ThreadsPerCore: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CpuOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CpuOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ThreadsPerCore=json_data.get("ThreadsPerCore"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CpuOptionsDefinition = CpuOptionsDefinition


@dataclass
class EbsBlockDeviceDefinition(BaseModel):
    DeleteOnTermination: Optional[bool]
    DeviceName: Optional[str]
    Encrypted: Optional[bool]
    Iops: Optional[float]
    KmsKeyId: Optional[str]
    SnapshotId: Optional[str]
    Throughput: Optional[float]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsBlockDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsBlockDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            DeviceName=json_data.get("DeviceName"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SnapshotId=json_data.get("SnapshotId"),
            Throughput=json_data.get("Throughput"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsBlockDeviceDefinition = EbsBlockDeviceDefinition


@dataclass
class EphemeralBlockDeviceDefinition(BaseModel):
    DeviceName: Optional[str]
    VirtualName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EphemeralBlockDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EphemeralBlockDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            VirtualName=json_data.get("VirtualName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EphemeralBlockDeviceDefinition = EphemeralBlockDeviceDefinition


@dataclass
class InstanceTypesWeightsDefinition(BaseModel):
    InstanceType: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceTypesWeightsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceTypesWeightsDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceType=json_data.get("InstanceType"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceTypesWeightsDefinition = InstanceTypesWeightsDefinition


@dataclass
class IntegrationBeanstalkDefinition(BaseModel):
    EnvironmentId: Optional[str]
    DeploymentPreferences: Optional[Sequence["_DeploymentPreferencesDefinition"]]
    ManagedActions: Optional[Sequence["_ManagedActionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationBeanstalkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationBeanstalkDefinition"]:
        if not json_data:
            return None
        return cls(
            EnvironmentId=json_data.get("EnvironmentId"),
            DeploymentPreferences=deserialize_list(json_data.get("DeploymentPreferences"), DeploymentPreferencesDefinition),
            ManagedActions=deserialize_list(json_data.get("ManagedActions"), ManagedActionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationBeanstalkDefinition = IntegrationBeanstalkDefinition


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
    BatchMinHealthyPercentage: Optional[float]
    ShouldDrainInstances: Optional[bool]
    OnFailure: Optional[Sequence["_OnFailureDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StrategyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StrategyDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            BatchMinHealthyPercentage=json_data.get("BatchMinHealthyPercentage"),
            ShouldDrainInstances=json_data.get("ShouldDrainInstances"),
            OnFailure=deserialize_list(json_data.get("OnFailure"), OnFailureDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StrategyDefinition = StrategyDefinition


@dataclass
class OnFailureDefinition(BaseModel):
    ActionType: Optional[str]
    BatchNum: Optional[float]
    DrainingTimeout: Optional[float]
    ShouldDecrementTargetCapacity: Optional[bool]
    ShouldHandleAllBatches: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_OnFailureDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnFailureDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionType=json_data.get("ActionType"),
            BatchNum=json_data.get("BatchNum"),
            DrainingTimeout=json_data.get("DrainingTimeout"),
            ShouldDecrementTargetCapacity=json_data.get("ShouldDecrementTargetCapacity"),
            ShouldHandleAllBatches=json_data.get("ShouldHandleAllBatches"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnFailureDefinition = OnFailureDefinition


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
class IntegrationCodedeployDefinition(BaseModel):
    CleanupOnFailure: Optional[bool]
    TerminateInstanceOnFailure: Optional[bool]
    DeploymentGroups: Optional[Sequence["_DeploymentGroupsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationCodedeployDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationCodedeployDefinition"]:
        if not json_data:
            return None
        return cls(
            CleanupOnFailure=json_data.get("CleanupOnFailure"),
            TerminateInstanceOnFailure=json_data.get("TerminateInstanceOnFailure"),
            DeploymentGroups=deserialize_list(json_data.get("DeploymentGroups"), DeploymentGroupsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationCodedeployDefinition = IntegrationCodedeployDefinition


@dataclass
class DeploymentGroupsDefinition(BaseModel):
    ApplicationName: Optional[str]
    DeploymentGroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            ApplicationName=json_data.get("ApplicationName"),
            DeploymentGroupName=json_data.get("DeploymentGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentGroupsDefinition = DeploymentGroupsDefinition


@dataclass
class IntegrationDockerSwarmDefinition(BaseModel):
    AutoscaleCooldown: Optional[float]
    AutoscaleIsEnabled: Optional[bool]
    MasterHost: Optional[str]
    MasterPort: Optional[float]
    AutoscaleDown: Optional[Sequence["_AutoscaleDownDefinition"]]
    AutoscaleHeadroom: Optional[Sequence["_AutoscaleHeadroomDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationDockerSwarmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationDockerSwarmDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoscaleCooldown=json_data.get("AutoscaleCooldown"),
            AutoscaleIsEnabled=json_data.get("AutoscaleIsEnabled"),
            MasterHost=json_data.get("MasterHost"),
            MasterPort=json_data.get("MasterPort"),
            AutoscaleDown=deserialize_list(json_data.get("AutoscaleDown"), AutoscaleDownDefinition),
            AutoscaleHeadroom=deserialize_list(json_data.get("AutoscaleHeadroom"), AutoscaleHeadroomDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationDockerSwarmDefinition = IntegrationDockerSwarmDefinition


@dataclass
class AutoscaleDownDefinition(BaseModel):
    EvaluationPeriods: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleDownDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleDownDefinition"]:
        if not json_data:
            return None
        return cls(
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleDownDefinition = AutoscaleDownDefinition


@dataclass
class AutoscaleHeadroomDefinition(BaseModel):
    CpuPerUnit: Optional[float]
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
            MemoryPerUnit=json_data.get("MemoryPerUnit"),
            NumOfUnits=json_data.get("NumOfUnits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleHeadroomDefinition = AutoscaleHeadroomDefinition


@dataclass
class IntegrationEcsDefinition(BaseModel):
    AutoscaleCooldown: Optional[float]
    AutoscaleIsAutoConfig: Optional[bool]
    AutoscaleIsEnabled: Optional[bool]
    AutoscaleScaleDownNonServiceTasks: Optional[bool]
    ClusterName: Optional[str]
    AutoscaleAttributes: Optional[Sequence["_AutoscaleAttributesDefinition"]]
    AutoscaleDown: Optional[Sequence["_AutoscaleDownDefinition"]]
    AutoscaleHeadroom: Optional[Sequence["_AutoscaleHeadroomDefinition"]]
    Batch: Optional[Sequence["_BatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationEcsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationEcsDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoscaleCooldown=json_data.get("AutoscaleCooldown"),
            AutoscaleIsAutoConfig=json_data.get("AutoscaleIsAutoConfig"),
            AutoscaleIsEnabled=json_data.get("AutoscaleIsEnabled"),
            AutoscaleScaleDownNonServiceTasks=json_data.get("AutoscaleScaleDownNonServiceTasks"),
            ClusterName=json_data.get("ClusterName"),
            AutoscaleAttributes=deserialize_list(json_data.get("AutoscaleAttributes"), AutoscaleAttributesDefinition),
            AutoscaleDown=deserialize_list(json_data.get("AutoscaleDown"), AutoscaleDownDefinition),
            AutoscaleHeadroom=deserialize_list(json_data.get("AutoscaleHeadroom"), AutoscaleHeadroomDefinition),
            Batch=deserialize_list(json_data.get("Batch"), BatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationEcsDefinition = IntegrationEcsDefinition


@dataclass
class AutoscaleAttributesDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleAttributesDefinition = AutoscaleAttributesDefinition


@dataclass
class BatchDefinition(BaseModel):
    JobQueueNames: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_BatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BatchDefinition"]:
        if not json_data:
            return None
        return cls(
            JobQueueNames=json_data.get("JobQueueNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BatchDefinition = BatchDefinition


@dataclass
class IntegrationGitlabDefinition(BaseModel):
    Runner: Optional[Sequence["_RunnerDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationGitlabDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationGitlabDefinition"]:
        if not json_data:
            return None
        return cls(
            Runner=deserialize_list(json_data.get("Runner"), RunnerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationGitlabDefinition = IntegrationGitlabDefinition


@dataclass
class RunnerDefinition(BaseModel):
    IsEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RunnerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunnerDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunnerDefinition = RunnerDefinition


@dataclass
class IntegrationKubernetesDefinition(BaseModel):
    ApiServer: Optional[str]
    AutoscaleCooldown: Optional[float]
    AutoscaleIsAutoConfig: Optional[bool]
    AutoscaleIsEnabled: Optional[bool]
    ClusterIdentifier: Optional[str]
    IntegrationMode: Optional[str]
    Token: Optional[str]
    AutoscaleDown: Optional[Sequence["_AutoscaleDownDefinition"]]
    AutoscaleHeadroom: Optional[Sequence["_AutoscaleHeadroomDefinition"]]
    AutoscaleLabels: Optional[Sequence["_AutoscaleLabelsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationKubernetesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationKubernetesDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiServer=json_data.get("ApiServer"),
            AutoscaleCooldown=json_data.get("AutoscaleCooldown"),
            AutoscaleIsAutoConfig=json_data.get("AutoscaleIsAutoConfig"),
            AutoscaleIsEnabled=json_data.get("AutoscaleIsEnabled"),
            ClusterIdentifier=json_data.get("ClusterIdentifier"),
            IntegrationMode=json_data.get("IntegrationMode"),
            Token=json_data.get("Token"),
            AutoscaleDown=deserialize_list(json_data.get("AutoscaleDown"), AutoscaleDownDefinition),
            AutoscaleHeadroom=deserialize_list(json_data.get("AutoscaleHeadroom"), AutoscaleHeadroomDefinition),
            AutoscaleLabels=deserialize_list(json_data.get("AutoscaleLabels"), AutoscaleLabelsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationKubernetesDefinition = IntegrationKubernetesDefinition


@dataclass
class AutoscaleLabelsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleLabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleLabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleLabelsDefinition = AutoscaleLabelsDefinition


@dataclass
class IntegrationMesosphereDefinition(BaseModel):
    ApiServer: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationMesosphereDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationMesosphereDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiServer=json_data.get("ApiServer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationMesosphereDefinition = IntegrationMesosphereDefinition


@dataclass
class IntegrationMultaiRuntimeDefinition(BaseModel):
    DeploymentId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationMultaiRuntimeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationMultaiRuntimeDefinition"]:
        if not json_data:
            return None
        return cls(
            DeploymentId=json_data.get("DeploymentId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationMultaiRuntimeDefinition = IntegrationMultaiRuntimeDefinition


@dataclass
class IntegrationNomadDefinition(BaseModel):
    AclToken: Optional[str]
    AutoscaleCooldown: Optional[float]
    AutoscaleIsEnabled: Optional[bool]
    MasterHost: Optional[str]
    MasterPort: Optional[float]
    AutoscaleConstraints: Optional[Sequence["_AutoscaleConstraintsDefinition"]]
    AutoscaleDown: Optional[Sequence["_AutoscaleDownDefinition"]]
    AutoscaleHeadroom: Optional[Sequence["_AutoscaleHeadroomDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationNomadDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationNomadDefinition"]:
        if not json_data:
            return None
        return cls(
            AclToken=json_data.get("AclToken"),
            AutoscaleCooldown=json_data.get("AutoscaleCooldown"),
            AutoscaleIsEnabled=json_data.get("AutoscaleIsEnabled"),
            MasterHost=json_data.get("MasterHost"),
            MasterPort=json_data.get("MasterPort"),
            AutoscaleConstraints=deserialize_list(json_data.get("AutoscaleConstraints"), AutoscaleConstraintsDefinition),
            AutoscaleDown=deserialize_list(json_data.get("AutoscaleDown"), AutoscaleDownDefinition),
            AutoscaleHeadroom=deserialize_list(json_data.get("AutoscaleHeadroom"), AutoscaleHeadroomDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationNomadDefinition = IntegrationNomadDefinition


@dataclass
class AutoscaleConstraintsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleConstraintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleConstraintsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleConstraintsDefinition = AutoscaleConstraintsDefinition


@dataclass
class IntegrationRancherDefinition(BaseModel):
    AccessKey: Optional[str]
    MasterHost: Optional[str]
    SecretKey: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationRancherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationRancherDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            MasterHost=json_data.get("MasterHost"),
            SecretKey=json_data.get("SecretKey"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationRancherDefinition = IntegrationRancherDefinition


@dataclass
class IntegrationRoute53Definition(BaseModel):
    Domains: Optional[Sequence["_DomainsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationRoute53Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationRoute53Definition"]:
        if not json_data:
            return None
        return cls(
            Domains=deserialize_list(json_data.get("Domains"), DomainsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationRoute53Definition = IntegrationRoute53Definition


@dataclass
class DomainsDefinition(BaseModel):
    HostedZoneId: Optional[str]
    RecordSetType: Optional[str]
    SpotinstAcctId: Optional[str]
    RecordSets: Optional[Sequence["_RecordSetsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DomainsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainsDefinition"]:
        if not json_data:
            return None
        return cls(
            HostedZoneId=json_data.get("HostedZoneId"),
            RecordSetType=json_data.get("RecordSetType"),
            SpotinstAcctId=json_data.get("SpotinstAcctId"),
            RecordSets=deserialize_list(json_data.get("RecordSets"), RecordSetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainsDefinition = DomainsDefinition


@dataclass
class RecordSetsDefinition(BaseModel):
    Name: Optional[str]
    UsePublicDns: Optional[bool]
    UsePublicIp: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RecordSetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordSetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            UsePublicDns=json_data.get("UsePublicDns"),
            UsePublicIp=json_data.get("UsePublicIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordSetsDefinition = RecordSetsDefinition


@dataclass
class MetadataOptionsDefinition(BaseModel):
    HttpPutResponseHopLimit: Optional[float]
    HttpTokens: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            HttpPutResponseHopLimit=json_data.get("HttpPutResponseHopLimit"),
            HttpTokens=json_data.get("HttpTokens"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataOptionsDefinition = MetadataOptionsDefinition


@dataclass
class MultaiTargetSetsDefinition(BaseModel):
    BalancerId: Optional[str]
    TargetSetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MultaiTargetSetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultaiTargetSetsDefinition"]:
        if not json_data:
            return None
        return cls(
            BalancerId=json_data.get("BalancerId"),
            TargetSetId=json_data.get("TargetSetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultaiTargetSetsDefinition = MultaiTargetSetsDefinition


@dataclass
class NetworkInterfaceDefinition(BaseModel):
    AssociateIpv6Address: Optional[bool]
    AssociatePublicIpAddress: Optional[bool]
    DeleteOnTermination: Optional[bool]
    Description: Optional[str]
    DeviceIndex: Optional[str]
    NetworkInterfaceId: Optional[str]
    PrivateIpAddress: Optional[str]
    SecondaryPrivateIpAddressCount: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            AssociateIpv6Address=json_data.get("AssociateIpv6Address"),
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Description=json_data.get("Description"),
            DeviceIndex=json_data.get("DeviceIndex"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            SecondaryPrivateIpAddressCount=json_data.get("SecondaryPrivateIpAddressCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfaceDefinition = NetworkInterfaceDefinition


@dataclass
class RevertToSpotDefinition(BaseModel):
    PerformAt: Optional[str]
    TimeWindows: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RevertToSpotDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RevertToSpotDefinition"]:
        if not json_data:
            return None
        return cls(
            PerformAt=json_data.get("PerformAt"),
            TimeWindows=json_data.get("TimeWindows"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RevertToSpotDefinition = RevertToSpotDefinition


@dataclass
class ScalingDownPolicyDefinition(BaseModel):
    ActionType: Optional[str]
    Adjustment: Optional[str]
    Cooldown: Optional[float]
    EvaluationPeriods: Optional[float]
    IsEnabled: Optional[bool]
    MaxTargetCapacity: Optional[str]
    Maximum: Optional[str]
    MetricName: Optional[str]
    MinTargetCapacity: Optional[str]
    Minimum: Optional[str]
    Namespace: Optional[str]
    Operator: Optional[str]
    Period: Optional[float]
    PolicyName: Optional[str]
    Source: Optional[str]
    Statistic: Optional[str]
    Target: Optional[str]
    Threshold: Optional[float]
    Unit: Optional[str]
    Dimensions: Optional[Sequence["_DimensionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingDownPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingDownPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionType=json_data.get("ActionType"),
            Adjustment=json_data.get("Adjustment"),
            Cooldown=json_data.get("Cooldown"),
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
            IsEnabled=json_data.get("IsEnabled"),
            MaxTargetCapacity=json_data.get("MaxTargetCapacity"),
            Maximum=json_data.get("Maximum"),
            MetricName=json_data.get("MetricName"),
            MinTargetCapacity=json_data.get("MinTargetCapacity"),
            Minimum=json_data.get("Minimum"),
            Namespace=json_data.get("Namespace"),
            Operator=json_data.get("Operator"),
            Period=json_data.get("Period"),
            PolicyName=json_data.get("PolicyName"),
            Source=json_data.get("Source"),
            Statistic=json_data.get("Statistic"),
            Target=json_data.get("Target"),
            Threshold=json_data.get("Threshold"),
            Unit=json_data.get("Unit"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingDownPolicyDefinition = ScalingDownPolicyDefinition


@dataclass
class DimensionsDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionsDefinition = DimensionsDefinition


@dataclass
class ScalingStrategyDefinition(BaseModel):
    TerminateAtEndOfBillingHour: Optional[bool]
    TerminationPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingStrategyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingStrategyDefinition"]:
        if not json_data:
            return None
        return cls(
            TerminateAtEndOfBillingHour=json_data.get("TerminateAtEndOfBillingHour"),
            TerminationPolicy=json_data.get("TerminationPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingStrategyDefinition = ScalingStrategyDefinition


@dataclass
class ScalingTargetPolicyDefinition(BaseModel):
    Cooldown: Optional[float]
    MaxCapacityPerScale: Optional[str]
    MetricName: Optional[str]
    Namespace: Optional[str]
    PolicyName: Optional[str]
    PredictiveMode: Optional[str]
    Source: Optional[str]
    Statistic: Optional[str]
    Target: Optional[float]
    Unit: Optional[str]
    Dimensions: Optional[Sequence["_DimensionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingTargetPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingTargetPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Cooldown=json_data.get("Cooldown"),
            MaxCapacityPerScale=json_data.get("MaxCapacityPerScale"),
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            PolicyName=json_data.get("PolicyName"),
            PredictiveMode=json_data.get("PredictiveMode"),
            Source=json_data.get("Source"),
            Statistic=json_data.get("Statistic"),
            Target=json_data.get("Target"),
            Unit=json_data.get("Unit"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingTargetPolicyDefinition = ScalingTargetPolicyDefinition


@dataclass
class ScalingUpPolicyDefinition(BaseModel):
    ActionType: Optional[str]
    Adjustment: Optional[str]
    Cooldown: Optional[float]
    EvaluationPeriods: Optional[float]
    IsEnabled: Optional[bool]
    MaxTargetCapacity: Optional[str]
    Maximum: Optional[str]
    MetricName: Optional[str]
    MinTargetCapacity: Optional[str]
    Minimum: Optional[str]
    Namespace: Optional[str]
    Operator: Optional[str]
    Period: Optional[float]
    PolicyName: Optional[str]
    Source: Optional[str]
    Statistic: Optional[str]
    Target: Optional[str]
    Threshold: Optional[float]
    Unit: Optional[str]
    Dimensions: Optional[Sequence["_DimensionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingUpPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingUpPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionType=json_data.get("ActionType"),
            Adjustment=json_data.get("Adjustment"),
            Cooldown=json_data.get("Cooldown"),
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
            IsEnabled=json_data.get("IsEnabled"),
            MaxTargetCapacity=json_data.get("MaxTargetCapacity"),
            Maximum=json_data.get("Maximum"),
            MetricName=json_data.get("MetricName"),
            MinTargetCapacity=json_data.get("MinTargetCapacity"),
            Minimum=json_data.get("Minimum"),
            Namespace=json_data.get("Namespace"),
            Operator=json_data.get("Operator"),
            Period=json_data.get("Period"),
            PolicyName=json_data.get("PolicyName"),
            Source=json_data.get("Source"),
            Statistic=json_data.get("Statistic"),
            Target=json_data.get("Target"),
            Threshold=json_data.get("Threshold"),
            Unit=json_data.get("Unit"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingUpPolicyDefinition = ScalingUpPolicyDefinition


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


@dataclass
class SignalDefinition(BaseModel):
    Name: Optional[str]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SignalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SignalDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SignalDefinition = SignalDefinition


@dataclass
class StatefulDeallocationDefinition(BaseModel):
    ShouldDeleteImages: Optional[bool]
    ShouldDeleteNetworkInterfaces: Optional[bool]
    ShouldDeleteSnapshots: Optional[bool]
    ShouldDeleteVolumes: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_StatefulDeallocationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatefulDeallocationDefinition"]:
        if not json_data:
            return None
        return cls(
            ShouldDeleteImages=json_data.get("ShouldDeleteImages"),
            ShouldDeleteNetworkInterfaces=json_data.get("ShouldDeleteNetworkInterfaces"),
            ShouldDeleteSnapshots=json_data.get("ShouldDeleteSnapshots"),
            ShouldDeleteVolumes=json_data.get("ShouldDeleteVolumes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatefulDeallocationDefinition = StatefulDeallocationDefinition


@dataclass
class StatefulInstanceActionDefinition(BaseModel):
    StatefulInstanceId: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatefulInstanceActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatefulInstanceActionDefinition"]:
        if not json_data:
            return None
        return cls(
            StatefulInstanceId=json_data.get("StatefulInstanceId"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatefulInstanceActionDefinition = StatefulInstanceActionDefinition


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
    AutoApplyTags: Optional[bool]
    ShouldResumeStateful: Optional[bool]
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
            AutoApplyTags=json_data.get("AutoApplyTags"),
            ShouldResumeStateful=json_data.get("ShouldResumeStateful"),
            ShouldRoll=json_data.get("ShouldRoll"),
            RollConfig=deserialize_list(json_data.get("RollConfig"), RollConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpdatePolicyDefinition = UpdatePolicyDefinition


@dataclass
class RollConfigDefinition(BaseModel):
    BatchSizePercentage: Optional[float]
    GracePeriod: Optional[float]
    HealthCheckType: Optional[str]
    WaitForRollPercentage: Optional[float]
    WaitForRollTimeout: Optional[float]
    Strategy: Optional[Sequence["_StrategyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RollConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RollConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BatchSizePercentage=json_data.get("BatchSizePercentage"),
            GracePeriod=json_data.get("GracePeriod"),
            HealthCheckType=json_data.get("HealthCheckType"),
            WaitForRollPercentage=json_data.get("WaitForRollPercentage"),
            WaitForRollTimeout=json_data.get("WaitForRollTimeout"),
            Strategy=deserialize_list(json_data.get("Strategy"), StrategyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RollConfigDefinition = RollConfigDefinition


