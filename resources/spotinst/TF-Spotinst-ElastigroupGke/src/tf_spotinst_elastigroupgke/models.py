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
    ClusterId: Optional[str]
    ClusterZoneName: Optional[str]
    DesiredCapacity: Optional[float]
    DrainingTimeout: Optional[float]
    FallbackToOndemand: Optional[bool]
    Id: Optional[str]
    InstanceTypesOndemand: Optional[str]
    InstanceTypesPreemptible: Optional[Sequence[str]]
    IpForwarding: Optional[bool]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Name: Optional[str]
    NodeImage: Optional[str]
    OndemandCount: Optional[float]
    PreemptiblePercentage: Optional[float]
    ServiceAccount: Optional[str]
    ShutdownScript: Optional[str]
    StartupScript: Optional[str]
    Tags: Optional[Sequence[str]]
    BackendServices: Optional[Sequence["_BackendServicesDefinition"]]
    Disk: Optional[Sequence["_DiskDefinition"]]
    Gpu: Optional[Sequence["_GpuDefinition"]]
    InstanceTypesCustom: Optional[Sequence["_InstanceTypesCustomDefinition"]]
    IntegrationDockerSwarm: Optional[Sequence["_IntegrationDockerSwarmDefinition"]]
    IntegrationGke: Optional[Sequence["_IntegrationGkeDefinition"]]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    NetworkInterface: Optional[Sequence["_NetworkInterfaceDefinition"]]
    ScalingDownPolicy: Optional[Sequence["_ScalingDownPolicyDefinition"]]
    ScalingUpPolicy: Optional[Sequence["_ScalingUpPolicyDefinition"]]

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
            ClusterId=json_data.get("ClusterId"),
            ClusterZoneName=json_data.get("ClusterZoneName"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            DrainingTimeout=json_data.get("DrainingTimeout"),
            FallbackToOndemand=json_data.get("FallbackToOndemand"),
            Id=json_data.get("Id"),
            InstanceTypesOndemand=json_data.get("InstanceTypesOndemand"),
            InstanceTypesPreemptible=json_data.get("InstanceTypesPreemptible"),
            IpForwarding=json_data.get("IpForwarding"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Name=json_data.get("Name"),
            NodeImage=json_data.get("NodeImage"),
            OndemandCount=json_data.get("OndemandCount"),
            PreemptiblePercentage=json_data.get("PreemptiblePercentage"),
            ServiceAccount=json_data.get("ServiceAccount"),
            ShutdownScript=json_data.get("ShutdownScript"),
            StartupScript=json_data.get("StartupScript"),
            Tags=json_data.get("Tags"),
            BackendServices=deserialize_list(json_data.get("BackendServices"), BackendServicesDefinition),
            Disk=deserialize_list(json_data.get("Disk"), DiskDefinition),
            Gpu=deserialize_list(json_data.get("Gpu"), GpuDefinition),
            InstanceTypesCustom=deserialize_list(json_data.get("InstanceTypesCustom"), InstanceTypesCustomDefinition),
            IntegrationDockerSwarm=deserialize_list(json_data.get("IntegrationDockerSwarm"), IntegrationDockerSwarmDefinition),
            IntegrationGke=deserialize_list(json_data.get("IntegrationGke"), IntegrationGkeDefinition),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            NetworkInterface=deserialize_list(json_data.get("NetworkInterface"), NetworkInterfaceDefinition),
            ScalingDownPolicy=deserialize_list(json_data.get("ScalingDownPolicy"), ScalingDownPolicyDefinition),
            ScalingUpPolicy=deserialize_list(json_data.get("ScalingUpPolicy"), ScalingUpPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class DiskDefinition(BaseModel):
    AutoDelete: Optional[bool]
    Boot: Optional[bool]
    DeviceName: Optional[str]
    Interface: Optional[str]
    Mode: Optional[str]
    Source: Optional[str]
    Type: Optional[str]
    InitializeParams: Optional[Sequence["_InitializeParamsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskDefinition"]:
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
            InitializeParams=deserialize_list(json_data.get("InitializeParams"), InitializeParamsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskDefinition = DiskDefinition


@dataclass
class InitializeParamsDefinition(BaseModel):
    DiskSizeGb: Optional[str]
    DiskType: Optional[str]
    SourceImage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InitializeParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitializeParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskSizeGb=json_data.get("DiskSizeGb"),
            DiskType=json_data.get("DiskType"),
            SourceImage=json_data.get("SourceImage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitializeParamsDefinition = InitializeParamsDefinition


@dataclass
class GpuDefinition(BaseModel):
    Count: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GpuDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GpuDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GpuDefinition = GpuDefinition


@dataclass
class InstanceTypesCustomDefinition(BaseModel):
    MemoryGib: Optional[float]
    Vcpu: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceTypesCustomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceTypesCustomDefinition"]:
        if not json_data:
            return None
        return cls(
            MemoryGib=json_data.get("MemoryGib"),
            Vcpu=json_data.get("Vcpu"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceTypesCustomDefinition = InstanceTypesCustomDefinition


@dataclass
class IntegrationDockerSwarmDefinition(BaseModel):
    MasterHost: Optional[str]
    MasterPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationDockerSwarmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationDockerSwarmDefinition"]:
        if not json_data:
            return None
        return cls(
            MasterHost=json_data.get("MasterHost"),
            MasterPort=json_data.get("MasterPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationDockerSwarmDefinition = IntegrationDockerSwarmDefinition


@dataclass
class IntegrationGkeDefinition(BaseModel):
    AutoUpdate: Optional[bool]
    AutoscaleCooldown: Optional[float]
    AutoscaleIsAutoConfig: Optional[bool]
    AutoscaleIsEnabled: Optional[bool]
    ClusterId: Optional[str]
    Location: Optional[str]
    AutoscaleDown: Optional[Sequence["_AutoscaleDownDefinition"]]
    AutoscaleHeadroom: Optional[Sequence["_AutoscaleHeadroomDefinition"]]
    AutoscaleLabels: Optional[Sequence["_AutoscaleLabelsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationGkeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationGkeDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoUpdate=json_data.get("AutoUpdate"),
            AutoscaleCooldown=json_data.get("AutoscaleCooldown"),
            AutoscaleIsAutoConfig=json_data.get("AutoscaleIsAutoConfig"),
            AutoscaleIsEnabled=json_data.get("AutoscaleIsEnabled"),
            ClusterId=json_data.get("ClusterId"),
            Location=json_data.get("Location"),
            AutoscaleDown=deserialize_list(json_data.get("AutoscaleDown"), AutoscaleDownDefinition),
            AutoscaleHeadroom=deserialize_list(json_data.get("AutoscaleHeadroom"), AutoscaleHeadroomDefinition),
            AutoscaleLabels=deserialize_list(json_data.get("AutoscaleLabels"), AutoscaleLabelsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationGkeDefinition = IntegrationGkeDefinition


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
class LabelsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class MetadataDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class NetworkInterfaceDefinition(BaseModel):
    Network: Optional[str]
    AccessConfigs: Optional[Sequence["_AccessConfigsDefinition"]]
    AliasIpRanges: Optional[Sequence["_AliasIpRangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Network=json_data.get("Network"),
            AccessConfigs=deserialize_list(json_data.get("AccessConfigs"), AccessConfigsDefinition),
            AliasIpRanges=deserialize_list(json_data.get("AliasIpRanges"), AliasIpRangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfaceDefinition = NetworkInterfaceDefinition


@dataclass
class AccessConfigsDefinition(BaseModel):
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessConfigsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessConfigsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessConfigsDefinition = AccessConfigsDefinition


@dataclass
class AliasIpRangesDefinition(BaseModel):
    IpCidrRange: Optional[str]
    SubnetworkRangeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AliasIpRangesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AliasIpRangesDefinition"]:
        if not json_data:
            return None
        return cls(
            IpCidrRange=json_data.get("IpCidrRange"),
            SubnetworkRangeName=json_data.get("SubnetworkRangeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AliasIpRangesDefinition = AliasIpRangesDefinition


@dataclass
class ScalingDownPolicyDefinition(BaseModel):
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
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            Operator=json_data.get("Operator"),
            Period=json_data.get("Period"),
            PolicyName=json_data.get("PolicyName"),
            Source=json_data.get("Source"),
            Statistic=json_data.get("Statistic"),
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
class ScalingUpPolicyDefinition(BaseModel):
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
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            Operator=json_data.get("Operator"),
            Period=json_data.get("Period"),
            PolicyName=json_data.get("PolicyName"),
            Source=json_data.get("Source"),
            Statistic=json_data.get("Statistic"),
            Threshold=json_data.get("Threshold"),
            Unit=json_data.get("Unit"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingUpPolicyDefinition = ScalingUpPolicyDefinition


