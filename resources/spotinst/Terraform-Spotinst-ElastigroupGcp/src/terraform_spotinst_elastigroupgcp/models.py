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
    AutoHealing: Optional[bool]
    AvailabilityZones: Optional[Sequence[str]]
    Description: Optional[str]
    DesiredCapacity: Optional[float]
    DrainingTimeout: Optional[float]
    FallbackToOndemand: Optional[bool]
    HealthCheckGracePeriod: Optional[float]
    HealthCheckType: Optional[str]
    InstanceTypesOndemand: Optional[str]
    InstanceTypesPreemptible: Optional[Sequence[str]]
    IpForwarding: Optional[bool]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Name: Optional[str]
    OndemandCount: Optional[float]
    PreemptiblePercentage: Optional[float]
    ServiceAccount: Optional[str]
    ShutdownScript: Optional[str]
    StartupScript: Optional[str]
    Tags: Optional[Sequence[str]]
    UnhealthyDuration: Optional[float]
    BackendServices: Optional[Sequence["_BackendServices"]]
    Disk: Optional[Sequence["_Disk"]]
    Gpu: Optional[Sequence["_Gpu"]]
    InstanceTypesCustom: Optional[Sequence["_InstanceTypesCustom"]]
    IntegrationDockerSwarm: Optional[Sequence["_IntegrationDockerSwarm"]]
    IntegrationGke: Optional[Sequence["_IntegrationGke"]]
    Labels: Optional[Sequence["_Labels"]]
    Metadata: Optional[Sequence["_Metadata"]]
    NetworkInterface: Optional[Sequence["_NetworkInterface"]]
    ScalingDownPolicy: Optional[Sequence["_ScalingDownPolicy"]]
    ScalingUpPolicy: Optional[Sequence["_ScalingUpPolicy"]]
    ScheduledTask: Optional[Sequence["_ScheduledTask"]]
    Subnets: Optional[Sequence["_Subnets"]]
    NamedPorts: Optional[Sequence["_NamedPorts"]]
    InitializeParams: Optional[Sequence["_InitializeParams"]]
    AutoscaleDown: Optional[Sequence["_AutoscaleDown"]]
    AutoscaleHeadroom: Optional[Sequence["_AutoscaleHeadroom"]]
    AutoscaleLabels: Optional[Sequence["_AutoscaleLabels"]]
    AccessConfigs: Optional[Sequence["_AccessConfigs"]]
    AliasIpRanges: Optional[Sequence["_AliasIpRanges"]]
    Dimensions: Optional[Sequence["_Dimensions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AutoHealing=json_data.get("AutoHealing"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            Description=json_data.get("Description"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            DrainingTimeout=json_data.get("DrainingTimeout"),
            FallbackToOndemand=json_data.get("FallbackToOndemand"),
            HealthCheckGracePeriod=json_data.get("HealthCheckGracePeriod"),
            HealthCheckType=json_data.get("HealthCheckType"),
            InstanceTypesOndemand=json_data.get("InstanceTypesOndemand"),
            InstanceTypesPreemptible=json_data.get("InstanceTypesPreemptible"),
            IpForwarding=json_data.get("IpForwarding"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Name=json_data.get("Name"),
            OndemandCount=json_data.get("OndemandCount"),
            PreemptiblePercentage=json_data.get("PreemptiblePercentage"),
            ServiceAccount=json_data.get("ServiceAccount"),
            ShutdownScript=json_data.get("ShutdownScript"),
            StartupScript=json_data.get("StartupScript"),
            Tags=json_data.get("Tags"),
            UnhealthyDuration=json_data.get("UnhealthyDuration"),
            BackendServices=json_data.get("BackendServices"),
            Disk=json_data.get("Disk"),
            Gpu=json_data.get("Gpu"),
            InstanceTypesCustom=json_data.get("InstanceTypesCustom"),
            IntegrationDockerSwarm=json_data.get("IntegrationDockerSwarm"),
            IntegrationGke=json_data.get("IntegrationGke"),
            Labels=json_data.get("Labels"),
            Metadata=json_data.get("Metadata"),
            NetworkInterface=json_data.get("NetworkInterface"),
            ScalingDownPolicy=json_data.get("ScalingDownPolicy"),
            ScalingUpPolicy=json_data.get("ScalingUpPolicy"),
            ScheduledTask=json_data.get("ScheduledTask"),
            Subnets=json_data.get("Subnets"),
            NamedPorts=json_data.get("NamedPorts"),
            InitializeParams=json_data.get("InitializeParams"),
            AutoscaleDown=json_data.get("AutoscaleDown"),
            AutoscaleHeadroom=json_data.get("AutoscaleHeadroom"),
            AutoscaleLabels=json_data.get("AutoscaleLabels"),
            AccessConfigs=json_data.get("AccessConfigs"),
            AliasIpRanges=json_data.get("AliasIpRanges"),
            Dimensions=json_data.get("Dimensions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackendServices:
    LocationType: Optional[str]
    Scheme: Optional[str]
    ServiceName: Optional[str]
    NamedPorts: Optional[Sequence["_NamedPorts"]]

    @classmethod
    def _deserialize(
        cls: Type["_BackendServices"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendServices"]:
        if not json_data:
            return None
        return cls(
            LocationType=json_data.get("LocationType"),
            Scheme=json_data.get("Scheme"),
            ServiceName=json_data.get("ServiceName"),
            NamedPorts=json_data.get("NamedPorts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendServices = BackendServices


@dataclass
class NamedPorts:
    Name: Optional[str]
    Ports: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NamedPorts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NamedPorts"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Ports=json_data.get("Ports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NamedPorts = NamedPorts


@dataclass
class Disk:
    AutoDelete: Optional[bool]
    Boot: Optional[bool]
    DeviceName: Optional[str]
    Interface: Optional[str]
    Mode: Optional[str]
    Source: Optional[str]
    Type: Optional[str]
    InitializeParams: Optional[Sequence["_InitializeParams"]]

    @classmethod
    def _deserialize(
        cls: Type["_Disk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Disk"]:
        if not json_data:
            return None
        return cls(
            AutoDelete=json_data.get("AutoDelete"),
            Boot=json_data.get("Boot"),
            DeviceName=json_data.get("DeviceName"),
            Interface=json_data.get("Interface"),
            Mode=json_data.get("Mode"),
            Source=json_data.get("Source"),
            Type=json_data.get("Type"),
            InitializeParams=json_data.get("InitializeParams"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Disk = Disk


@dataclass
class InitializeParams:
    DiskSizeGb: Optional[str]
    DiskType: Optional[str]
    SourceImage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InitializeParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitializeParams"]:
        if not json_data:
            return None
        return cls(
            DiskSizeGb=json_data.get("DiskSizeGb"),
            DiskType=json_data.get("DiskType"),
            SourceImage=json_data.get("SourceImage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitializeParams = InitializeParams


@dataclass
class Gpu:
    Count: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Gpu"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Gpu"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Gpu = Gpu


@dataclass
class InstanceTypesCustom:
    MemoryGib: Optional[float]
    Vcpu: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceTypesCustom"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceTypesCustom"]:
        if not json_data:
            return None
        return cls(
            MemoryGib=json_data.get("MemoryGib"),
            Vcpu=json_data.get("Vcpu"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceTypesCustom = InstanceTypesCustom


@dataclass
class IntegrationDockerSwarm:
    MasterHost: Optional[str]
    MasterPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationDockerSwarm"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationDockerSwarm"]:
        if not json_data:
            return None
        return cls(
            MasterHost=json_data.get("MasterHost"),
            MasterPort=json_data.get("MasterPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationDockerSwarm = IntegrationDockerSwarm


@dataclass
class IntegrationGke:
    AutoUpdate: Optional[bool]
    AutoscaleCooldown: Optional[float]
    AutoscaleIsAutoConfig: Optional[bool]
    AutoscaleIsEnabled: Optional[bool]
    ClusterId: Optional[str]
    Location: Optional[str]
    AutoscaleDown: Optional[Sequence["_AutoscaleDown"]]
    AutoscaleHeadroom: Optional[Sequence["_AutoscaleHeadroom"]]
    AutoscaleLabels: Optional[Sequence["_AutoscaleLabels"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationGke"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationGke"]:
        if not json_data:
            return None
        return cls(
            AutoUpdate=json_data.get("AutoUpdate"),
            AutoscaleCooldown=json_data.get("AutoscaleCooldown"),
            AutoscaleIsAutoConfig=json_data.get("AutoscaleIsAutoConfig"),
            AutoscaleIsEnabled=json_data.get("AutoscaleIsEnabled"),
            ClusterId=json_data.get("ClusterId"),
            Location=json_data.get("Location"),
            AutoscaleDown=json_data.get("AutoscaleDown"),
            AutoscaleHeadroom=json_data.get("AutoscaleHeadroom"),
            AutoscaleLabels=json_data.get("AutoscaleLabels"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationGke = IntegrationGke


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
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class Metadata:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class NetworkInterface:
    Network: Optional[str]
    AccessConfigs: Optional[Sequence["_AccessConfigs"]]
    AliasIpRanges: Optional[Sequence["_AliasIpRanges"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterface"]:
        if not json_data:
            return None
        return cls(
            Network=json_data.get("Network"),
            AccessConfigs=json_data.get("AccessConfigs"),
            AliasIpRanges=json_data.get("AliasIpRanges"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterface = NetworkInterface


@dataclass
class AccessConfigs:
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessConfigs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessConfigs"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessConfigs = AccessConfigs


@dataclass
class AliasIpRanges:
    IpCidrRange: Optional[str]
    SubnetworkRangeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AliasIpRanges"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AliasIpRanges"]:
        if not json_data:
            return None
        return cls(
            IpCidrRange=json_data.get("IpCidrRange"),
            SubnetworkRangeName=json_data.get("SubnetworkRangeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AliasIpRanges = AliasIpRanges


@dataclass
class ScalingDownPolicy:
    ActionType: Optional[str]
    Adjustment: Optional[float]
    Cooldown: Optional[float]
    EvaluationPeriods: Optional[float]
    MetricName: Optional[str]
    Namespace: Optional[str]
    Operator: Optional[str]
    Period: Optional[float]
    PolicyName: Optional[str]
    Source: Optional[str]
    Statistic: Optional[str]
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
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            Operator=json_data.get("Operator"),
            Period=json_data.get("Period"),
            PolicyName=json_data.get("PolicyName"),
            Source=json_data.get("Source"),
            Statistic=json_data.get("Statistic"),
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
class ScalingUpPolicy:
    ActionType: Optional[str]
    Adjustment: Optional[float]
    Cooldown: Optional[float]
    EvaluationPeriods: Optional[float]
    MetricName: Optional[str]
    Namespace: Optional[str]
    Operator: Optional[str]
    Period: Optional[float]
    PolicyName: Optional[str]
    Source: Optional[str]
    Statistic: Optional[str]
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
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            Operator=json_data.get("Operator"),
            Period=json_data.get("Period"),
            PolicyName=json_data.get("PolicyName"),
            Source=json_data.get("Source"),
            Statistic=json_data.get("Statistic"),
            Threshold=json_data.get("Threshold"),
            Unit=json_data.get("Unit"),
            Dimensions=json_data.get("Dimensions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingUpPolicy = ScalingUpPolicy


@dataclass
class ScheduledTask:
    CronExpression: Optional[str]
    IsEnabled: Optional[bool]
    MaxCapacity: Optional[str]
    MinCapacity: Optional[str]
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
            CronExpression=json_data.get("CronExpression"),
            IsEnabled=json_data.get("IsEnabled"),
            MaxCapacity=json_data.get("MaxCapacity"),
            MinCapacity=json_data.get("MinCapacity"),
            TargetCapacity=json_data.get("TargetCapacity"),
            TaskType=json_data.get("TaskType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledTask = ScheduledTask


@dataclass
class Subnets:
    Region: Optional[str]
    SubnetNames: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Subnets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subnets"]:
        if not json_data:
            return None
        return cls(
            Region=json_data.get("Region"),
            SubnetNames=json_data.get("SubnetNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subnets = Subnets


