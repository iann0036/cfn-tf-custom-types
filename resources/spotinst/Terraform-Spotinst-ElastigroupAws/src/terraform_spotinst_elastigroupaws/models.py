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
    UtilizeReservedInstances: Optional[bool]
    WaitForCapacity: Optional[float]
    WaitForCapacityTimeout: Optional[float]
    EbsBlockDevice: Optional[Sequence["_EbsBlockDevice"]]
    EphemeralBlockDevice: Optional[Sequence["_EphemeralBlockDevice"]]
    InstanceTypesWeights: Optional[Sequence["_InstanceTypesWeights"]]
    IntegrationBeanstalk: Optional[Sequence["_IntegrationBeanstalk"]]
    IntegrationCodedeploy: Optional[Sequence["_IntegrationCodedeploy"]]
    IntegrationDockerSwarm: Optional[Sequence["_IntegrationDockerSwarm"]]
    IntegrationEcs: Optional[Sequence["_IntegrationEcs"]]
    IntegrationGitlab: Optional[Sequence["_IntegrationGitlab"]]
    IntegrationKubernetes: Optional[Sequence["_IntegrationKubernetes"]]
    IntegrationMesosphere: Optional[Sequence["_IntegrationMesosphere"]]
    IntegrationMultaiRuntime: Optional[Sequence["_IntegrationMultaiRuntime"]]
    IntegrationNomad: Optional[Sequence["_IntegrationNomad"]]
    IntegrationRancher: Optional[Sequence["_IntegrationRancher"]]
    IntegrationRoute53: Optional[Sequence["_IntegrationRoute53"]]
    MultaiTargetSets: Optional[Sequence["_MultaiTargetSets"]]
    NetworkInterface: Optional[Sequence["_NetworkInterface"]]
    RevertToSpot: Optional[Sequence["_RevertToSpot"]]
    ScalingDownPolicy: Optional[Sequence["_ScalingDownPolicy"]]
    ScalingStrategy: Optional[Sequence["_ScalingStrategy"]]
    ScalingTargetPolicy: Optional[Sequence["_ScalingTargetPolicy"]]
    ScalingUpPolicy: Optional[Sequence["_ScalingUpPolicy"]]
    ScheduledTask: Optional[Sequence["_ScheduledTask"]]
    Signal: Optional[Sequence["_Signal"]]
    StatefulDeallocation: Optional[Sequence["_StatefulDeallocation"]]
    Tags: Optional[Sequence["_Tags"]]
    UpdatePolicy: Optional[Sequence["_UpdatePolicy"]]
    DeploymentPreferences: Optional[Sequence["_DeploymentPreferences"]]
    ManagedActions: Optional[Sequence["_ManagedActions"]]
    DeploymentGroups: Optional[Sequence["_DeploymentGroups"]]
    AutoscaleDown: Optional[Sequence["_AutoscaleDown"]]
    AutoscaleHeadroom: Optional[Sequence["_AutoscaleHeadroom"]]
    AutoscaleAttributes: Optional[Sequence["_AutoscaleAttributes"]]
    Runner: Optional[Sequence["_Runner"]]
    AutoscaleLabels: Optional[Sequence["_AutoscaleLabels"]]
    AutoscaleConstraints: Optional[Sequence["_AutoscaleConstraints"]]
    Domains: Optional[Sequence["_Domains"]]
    Dimensions: Optional[Sequence["_Dimensions"]]
    RollConfig: Optional[Sequence["_RollConfig"]]
    Strategy: Optional[Sequence["_Strategy"]]
    PlatformUpdate: Optional[Sequence["_PlatformUpdate"]]
    RecordSets: Optional[Sequence["_RecordSets"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            UtilizeReservedInstances=json_data.get("UtilizeReservedInstances"),
            WaitForCapacity=json_data.get("WaitForCapacity"),
            WaitForCapacityTimeout=json_data.get("WaitForCapacityTimeout"),
            EbsBlockDevice=json_data.get("EbsBlockDevice"),
            EphemeralBlockDevice=json_data.get("EphemeralBlockDevice"),
            InstanceTypesWeights=json_data.get("InstanceTypesWeights"),
            IntegrationBeanstalk=json_data.get("IntegrationBeanstalk"),
            IntegrationCodedeploy=json_data.get("IntegrationCodedeploy"),
            IntegrationDockerSwarm=json_data.get("IntegrationDockerSwarm"),
            IntegrationEcs=json_data.get("IntegrationEcs"),
            IntegrationGitlab=json_data.get("IntegrationGitlab"),
            IntegrationKubernetes=json_data.get("IntegrationKubernetes"),
            IntegrationMesosphere=json_data.get("IntegrationMesosphere"),
            IntegrationMultaiRuntime=json_data.get("IntegrationMultaiRuntime"),
            IntegrationNomad=json_data.get("IntegrationNomad"),
            IntegrationRancher=json_data.get("IntegrationRancher"),
            IntegrationRoute53=json_data.get("IntegrationRoute53"),
            MultaiTargetSets=json_data.get("MultaiTargetSets"),
            NetworkInterface=json_data.get("NetworkInterface"),
            RevertToSpot=json_data.get("RevertToSpot"),
            ScalingDownPolicy=json_data.get("ScalingDownPolicy"),
            ScalingStrategy=json_data.get("ScalingStrategy"),
            ScalingTargetPolicy=json_data.get("ScalingTargetPolicy"),
            ScalingUpPolicy=json_data.get("ScalingUpPolicy"),
            ScheduledTask=json_data.get("ScheduledTask"),
            Signal=json_data.get("Signal"),
            StatefulDeallocation=json_data.get("StatefulDeallocation"),
            Tags=json_data.get("Tags"),
            UpdatePolicy=json_data.get("UpdatePolicy"),
            DeploymentPreferences=json_data.get("DeploymentPreferences"),
            ManagedActions=json_data.get("ManagedActions"),
            DeploymentGroups=json_data.get("DeploymentGroups"),
            AutoscaleDown=json_data.get("AutoscaleDown"),
            AutoscaleHeadroom=json_data.get("AutoscaleHeadroom"),
            AutoscaleAttributes=json_data.get("AutoscaleAttributes"),
            Runner=json_data.get("Runner"),
            AutoscaleLabels=json_data.get("AutoscaleLabels"),
            AutoscaleConstraints=json_data.get("AutoscaleConstraints"),
            Domains=json_data.get("Domains"),
            Dimensions=json_data.get("Dimensions"),
            RollConfig=json_data.get("RollConfig"),
            Strategy=json_data.get("Strategy"),
            PlatformUpdate=json_data.get("PlatformUpdate"),
            RecordSets=json_data.get("RecordSets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EbsBlockDevice:
    DeleteOnTermination: Optional[bool]
    DeviceName: Optional[str]
    Encrypted: Optional[bool]
    Iops: Optional[float]
    KmsKeyId: Optional[str]
    SnapshotId: Optional[str]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsBlockDevice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsBlockDevice"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            DeviceName=json_data.get("DeviceName"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SnapshotId=json_data.get("SnapshotId"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsBlockDevice = EbsBlockDevice


@dataclass
class EphemeralBlockDevice:
    DeviceName: Optional[str]
    VirtualName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EphemeralBlockDevice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EphemeralBlockDevice"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            VirtualName=json_data.get("VirtualName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EphemeralBlockDevice = EphemeralBlockDevice


@dataclass
class InstanceTypesWeights:
    InstanceType: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceTypesWeights"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceTypesWeights"]:
        if not json_data:
            return None
        return cls(
            InstanceType=json_data.get("InstanceType"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceTypesWeights = InstanceTypesWeights


@dataclass
class IntegrationBeanstalk:
    EnvironmentId: Optional[str]
    DeploymentPreferences: Optional[Sequence["_DeploymentPreferences"]]
    ManagedActions: Optional[Sequence["_ManagedActions"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationBeanstalk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationBeanstalk"]:
        if not json_data:
            return None
        return cls(
            EnvironmentId=json_data.get("EnvironmentId"),
            DeploymentPreferences=json_data.get("DeploymentPreferences"),
            ManagedActions=json_data.get("ManagedActions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationBeanstalk = IntegrationBeanstalk


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
    BatchMinHealthyPercentage: Optional[float]
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
            BatchMinHealthyPercentage=json_data.get("BatchMinHealthyPercentage"),
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
class IntegrationCodedeploy:
    CleanupOnFailure: Optional[bool]
    TerminateInstanceOnFailure: Optional[bool]
    DeploymentGroups: Optional[Sequence["_DeploymentGroups"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationCodedeploy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationCodedeploy"]:
        if not json_data:
            return None
        return cls(
            CleanupOnFailure=json_data.get("CleanupOnFailure"),
            TerminateInstanceOnFailure=json_data.get("TerminateInstanceOnFailure"),
            DeploymentGroups=json_data.get("DeploymentGroups"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationCodedeploy = IntegrationCodedeploy


@dataclass
class DeploymentGroups:
    ApplicationName: Optional[str]
    DeploymentGroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentGroups"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentGroups"]:
        if not json_data:
            return None
        return cls(
            ApplicationName=json_data.get("ApplicationName"),
            DeploymentGroupName=json_data.get("DeploymentGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentGroups = DeploymentGroups


@dataclass
class IntegrationDockerSwarm:
    AutoscaleCooldown: Optional[float]
    AutoscaleIsEnabled: Optional[bool]
    MasterHost: Optional[str]
    MasterPort: Optional[float]
    AutoscaleDown: Optional[Sequence["_AutoscaleDown"]]
    AutoscaleHeadroom: Optional[Sequence["_AutoscaleHeadroom"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationDockerSwarm"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationDockerSwarm"]:
        if not json_data:
            return None
        return cls(
            AutoscaleCooldown=json_data.get("AutoscaleCooldown"),
            AutoscaleIsEnabled=json_data.get("AutoscaleIsEnabled"),
            MasterHost=json_data.get("MasterHost"),
            MasterPort=json_data.get("MasterPort"),
            AutoscaleDown=json_data.get("AutoscaleDown"),
            AutoscaleHeadroom=json_data.get("AutoscaleHeadroom"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationDockerSwarm = IntegrationDockerSwarm


@dataclass
class AutoscaleDown:
    EvaluationPeriods: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleDown"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleDown"]:
        if not json_data:
            return None
        return cls(
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleDown = AutoscaleDown


@dataclass
class AutoscaleHeadroom:
    CpuPerUnit: Optional[float]
    MemoryPerUnit: Optional[float]
    NumOfUnits: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleHeadroom"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleHeadroom"]:
        if not json_data:
            return None
        return cls(
            CpuPerUnit=json_data.get("CpuPerUnit"),
            MemoryPerUnit=json_data.get("MemoryPerUnit"),
            NumOfUnits=json_data.get("NumOfUnits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleHeadroom = AutoscaleHeadroom


@dataclass
class IntegrationEcs:
    AutoscaleCooldown: Optional[float]
    AutoscaleIsAutoConfig: Optional[bool]
    AutoscaleIsEnabled: Optional[bool]
    AutoscaleScaleDownNonServiceTasks: Optional[bool]
    ClusterName: Optional[str]
    AutoscaleAttributes: Optional[Sequence["_AutoscaleAttributes"]]
    AutoscaleDown: Optional[Sequence["_AutoscaleDown"]]
    AutoscaleHeadroom: Optional[Sequence["_AutoscaleHeadroom"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationEcs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationEcs"]:
        if not json_data:
            return None
        return cls(
            AutoscaleCooldown=json_data.get("AutoscaleCooldown"),
            AutoscaleIsAutoConfig=json_data.get("AutoscaleIsAutoConfig"),
            AutoscaleIsEnabled=json_data.get("AutoscaleIsEnabled"),
            AutoscaleScaleDownNonServiceTasks=json_data.get("AutoscaleScaleDownNonServiceTasks"),
            ClusterName=json_data.get("ClusterName"),
            AutoscaleAttributes=json_data.get("AutoscaleAttributes"),
            AutoscaleDown=json_data.get("AutoscaleDown"),
            AutoscaleHeadroom=json_data.get("AutoscaleHeadroom"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationEcs = IntegrationEcs


@dataclass
class AutoscaleAttributes:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleAttributes"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleAttributes = AutoscaleAttributes


@dataclass
class IntegrationGitlab:
    Runner: Optional[Sequence["_Runner"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationGitlab"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationGitlab"]:
        if not json_data:
            return None
        return cls(
            Runner=json_data.get("Runner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationGitlab = IntegrationGitlab


@dataclass
class Runner:
    IsEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Runner"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Runner"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Runner = Runner


@dataclass
class IntegrationKubernetes:
    ApiServer: Optional[str]
    AutoscaleCooldown: Optional[float]
    AutoscaleIsAutoConfig: Optional[bool]
    AutoscaleIsEnabled: Optional[bool]
    ClusterIdentifier: Optional[str]
    IntegrationMode: Optional[str]
    Token: Optional[str]
    AutoscaleDown: Optional[Sequence["_AutoscaleDown"]]
    AutoscaleHeadroom: Optional[Sequence["_AutoscaleHeadroom"]]
    AutoscaleLabels: Optional[Sequence["_AutoscaleLabels"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationKubernetes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationKubernetes"]:
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
            AutoscaleDown=json_data.get("AutoscaleDown"),
            AutoscaleHeadroom=json_data.get("AutoscaleHeadroom"),
            AutoscaleLabels=json_data.get("AutoscaleLabels"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationKubernetes = IntegrationKubernetes


@dataclass
class AutoscaleLabels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleLabels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleLabels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleLabels = AutoscaleLabels


@dataclass
class IntegrationMesosphere:
    ApiServer: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationMesosphere"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationMesosphere"]:
        if not json_data:
            return None
        return cls(
            ApiServer=json_data.get("ApiServer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationMesosphere = IntegrationMesosphere


@dataclass
class IntegrationMultaiRuntime:
    DeploymentId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationMultaiRuntime"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationMultaiRuntime"]:
        if not json_data:
            return None
        return cls(
            DeploymentId=json_data.get("DeploymentId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationMultaiRuntime = IntegrationMultaiRuntime


@dataclass
class IntegrationNomad:
    AclToken: Optional[str]
    AutoscaleCooldown: Optional[float]
    AutoscaleIsEnabled: Optional[bool]
    MasterHost: Optional[str]
    MasterPort: Optional[float]
    AutoscaleConstraints: Optional[Sequence["_AutoscaleConstraints"]]
    AutoscaleDown: Optional[Sequence["_AutoscaleDown"]]
    AutoscaleHeadroom: Optional[Sequence["_AutoscaleHeadroom"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationNomad"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationNomad"]:
        if not json_data:
            return None
        return cls(
            AclToken=json_data.get("AclToken"),
            AutoscaleCooldown=json_data.get("AutoscaleCooldown"),
            AutoscaleIsEnabled=json_data.get("AutoscaleIsEnabled"),
            MasterHost=json_data.get("MasterHost"),
            MasterPort=json_data.get("MasterPort"),
            AutoscaleConstraints=json_data.get("AutoscaleConstraints"),
            AutoscaleDown=json_data.get("AutoscaleDown"),
            AutoscaleHeadroom=json_data.get("AutoscaleHeadroom"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationNomad = IntegrationNomad


@dataclass
class AutoscaleConstraints:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleConstraints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleConstraints"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleConstraints = AutoscaleConstraints


@dataclass
class IntegrationRancher:
    AccessKey: Optional[str]
    MasterHost: Optional[str]
    SecretKey: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationRancher"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationRancher"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            MasterHost=json_data.get("MasterHost"),
            SecretKey=json_data.get("SecretKey"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationRancher = IntegrationRancher


@dataclass
class IntegrationRoute53:
    Domains: Optional[Sequence["_Domains"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationRoute53"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationRoute53"]:
        if not json_data:
            return None
        return cls(
            Domains=json_data.get("Domains"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationRoute53 = IntegrationRoute53


@dataclass
class Domains:
    HostedZoneId: Optional[str]
    SpotinstAcctId: Optional[str]
    RecordSets: Optional[Sequence["_RecordSets"]]

    @classmethod
    def _deserialize(
        cls: Type["_Domains"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Domains"]:
        if not json_data:
            return None
        return cls(
            HostedZoneId=json_data.get("HostedZoneId"),
            SpotinstAcctId=json_data.get("SpotinstAcctId"),
            RecordSets=json_data.get("RecordSets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Domains = Domains


@dataclass
class RecordSets:
    Name: Optional[str]
    UsePublicIp: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RecordSets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordSets"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            UsePublicIp=json_data.get("UsePublicIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordSets = RecordSets


@dataclass
class MultaiTargetSets:
    BalancerId: Optional[str]
    TargetSetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MultaiTargetSets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultaiTargetSets"]:
        if not json_data:
            return None
        return cls(
            BalancerId=json_data.get("BalancerId"),
            TargetSetId=json_data.get("TargetSetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultaiTargetSets = MultaiTargetSets


@dataclass
class NetworkInterface:
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
        cls: Type["_NetworkInterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterface"]:
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
_NetworkInterface = NetworkInterface


@dataclass
class RevertToSpot:
    PerformAt: Optional[str]
    TimeWindows: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RevertToSpot"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RevertToSpot"]:
        if not json_data:
            return None
        return cls(
            PerformAt=json_data.get("PerformAt"),
            TimeWindows=json_data.get("TimeWindows"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RevertToSpot = RevertToSpot


@dataclass
class ScalingDownPolicy:
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
    Dimensions: Optional[Sequence["_Dimensions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingDownPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingDownPolicy"]:
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
            Dimensions=json_data.get("Dimensions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingDownPolicy = ScalingDownPolicy


@dataclass
class Dimensions:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dimensions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dimensions"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dimensions = Dimensions


@dataclass
class ScalingStrategy:
    TerminateAtEndOfBillingHour: Optional[bool]
    TerminationPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingStrategy"]:
        if not json_data:
            return None
        return cls(
            TerminateAtEndOfBillingHour=json_data.get("TerminateAtEndOfBillingHour"),
            TerminationPolicy=json_data.get("TerminationPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingStrategy = ScalingStrategy


@dataclass
class ScalingTargetPolicy:
    Cooldown: Optional[float]
    MetricName: Optional[str]
    Namespace: Optional[str]
    PolicyName: Optional[str]
    PredictiveMode: Optional[str]
    Source: Optional[str]
    Statistic: Optional[str]
    Target: Optional[float]
    Unit: Optional[str]
    Dimensions: Optional[Sequence["_Dimensions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingTargetPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingTargetPolicy"]:
        if not json_data:
            return None
        return cls(
            Cooldown=json_data.get("Cooldown"),
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            PolicyName=json_data.get("PolicyName"),
            PredictiveMode=json_data.get("PredictiveMode"),
            Source=json_data.get("Source"),
            Statistic=json_data.get("Statistic"),
            Target=json_data.get("Target"),
            Unit=json_data.get("Unit"),
            Dimensions=json_data.get("Dimensions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingTargetPolicy = ScalingTargetPolicy


@dataclass
class ScalingUpPolicy:
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
    Dimensions: Optional[Sequence["_Dimensions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingUpPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingUpPolicy"]:
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
            Dimensions=json_data.get("Dimensions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingUpPolicy = ScalingUpPolicy


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


@dataclass
class Signal:
    Name: Optional[str]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Signal"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Signal"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Signal = Signal


@dataclass
class StatefulDeallocation:
    ShouldDeleteImages: Optional[bool]
    ShouldDeleteNetworkInterfaces: Optional[bool]
    ShouldDeleteSnapshots: Optional[bool]
    ShouldDeleteVolumes: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_StatefulDeallocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatefulDeallocation"]:
        if not json_data:
            return None
        return cls(
            ShouldDeleteImages=json_data.get("ShouldDeleteImages"),
            ShouldDeleteNetworkInterfaces=json_data.get("ShouldDeleteNetworkInterfaces"),
            ShouldDeleteSnapshots=json_data.get("ShouldDeleteSnapshots"),
            ShouldDeleteVolumes=json_data.get("ShouldDeleteVolumes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatefulDeallocation = StatefulDeallocation


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
class UpdatePolicy:
    AutoApplyTags: Optional[bool]
    ShouldResumeStateful: Optional[bool]
    ShouldRoll: Optional[bool]
    RollConfig: Optional[Sequence["_RollConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_UpdatePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpdatePolicy"]:
        if not json_data:
            return None
        return cls(
            AutoApplyTags=json_data.get("AutoApplyTags"),
            ShouldResumeStateful=json_data.get("ShouldResumeStateful"),
            ShouldRoll=json_data.get("ShouldRoll"),
            RollConfig=json_data.get("RollConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpdatePolicy = UpdatePolicy


@dataclass
class RollConfig:
    BatchSizePercentage: Optional[float]
    GracePeriod: Optional[float]
    HealthCheckType: Optional[str]
    WaitForRollPercentage: Optional[float]
    WaitForRollTimeout: Optional[float]
    Strategy: Optional[Sequence["_Strategy"]]

    @classmethod
    def _deserialize(
        cls: Type["_RollConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RollConfig"]:
        if not json_data:
            return None
        return cls(
            BatchSizePercentage=json_data.get("BatchSizePercentage"),
            GracePeriod=json_data.get("GracePeriod"),
            HealthCheckType=json_data.get("HealthCheckType"),
            WaitForRollPercentage=json_data.get("WaitForRollPercentage"),
            WaitForRollTimeout=json_data.get("WaitForRollTimeout"),
            Strategy=json_data.get("Strategy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RollConfig = RollConfig


