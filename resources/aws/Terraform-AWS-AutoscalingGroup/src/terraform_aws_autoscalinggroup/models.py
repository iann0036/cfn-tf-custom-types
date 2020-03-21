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
    Arn: Optional[str]
    AvailabilityZones: Optional[Sequence[str]]
    DefaultCooldown: Optional[float]
    DesiredCapacity: Optional[float]
    EnabledMetrics: Optional[Sequence[str]]
    ForceDelete: Optional[bool]
    HealthCheckGracePeriod: Optional[float]
    HealthCheckType: Optional[str]
    LaunchConfiguration: Optional[str]
    LoadBalancers: Optional[Sequence[str]]
    MaxInstanceLifetime: Optional[float]
    MaxSize: Optional[float]
    MetricsGranularity: Optional[str]
    MinElbCapacity: Optional[float]
    MinSize: Optional[float]
    Name: Optional[str]
    NamePrefix: Optional[str]
    PlacementGroup: Optional[str]
    ProtectFromScaleIn: Optional[bool]
    ServiceLinkedRoleArn: Optional[str]
    SuspendedProcesses: Optional[Sequence[str]]
    Tags: Optional[Sequence[Sequence["_Tags"]]]
    TargetGroupArns: Optional[Sequence[str]]
    TerminationPolicies: Optional[Sequence[str]]
    VpcZoneIdentifier: Optional[Sequence[str]]
    WaitForCapacityTimeout: Optional[str]
    WaitForElbCapacity: Optional[float]
    InitialLifecycleHook: Optional[Sequence["_InitialLifecycleHook"]]
    LaunchTemplate: Optional[Sequence["_LaunchTemplate"]]
    MixedInstancesPolicy: Optional[Sequence["_MixedInstancesPolicy"]]
    Tag: Optional[Sequence["_Tag"]]
    Timeouts: Optional["_Timeouts"]
    InstancesDistribution: Optional[Sequence["_InstancesDistribution"]]
    LaunchTemplateSpecification: Optional[Sequence["_LaunchTemplateSpecification"]]
    Override: Optional[Sequence["_Override"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            DefaultCooldown=json_data.get("DefaultCooldown"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            EnabledMetrics=json_data.get("EnabledMetrics"),
            ForceDelete=json_data.get("ForceDelete"),
            HealthCheckGracePeriod=json_data.get("HealthCheckGracePeriod"),
            HealthCheckType=json_data.get("HealthCheckType"),
            LaunchConfiguration=json_data.get("LaunchConfiguration"),
            LoadBalancers=json_data.get("LoadBalancers"),
            MaxInstanceLifetime=json_data.get("MaxInstanceLifetime"),
            MaxSize=json_data.get("MaxSize"),
            MetricsGranularity=json_data.get("MetricsGranularity"),
            MinElbCapacity=json_data.get("MinElbCapacity"),
            MinSize=json_data.get("MinSize"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            PlacementGroup=json_data.get("PlacementGroup"),
            ProtectFromScaleIn=json_data.get("ProtectFromScaleIn"),
            ServiceLinkedRoleArn=json_data.get("ServiceLinkedRoleArn"),
            SuspendedProcesses=json_data.get("SuspendedProcesses"),
            Tags=json_data.get("Tags"),
            TargetGroupArns=json_data.get("TargetGroupArns"),
            TerminationPolicies=json_data.get("TerminationPolicies"),
            VpcZoneIdentifier=json_data.get("VpcZoneIdentifier"),
            WaitForCapacityTimeout=json_data.get("WaitForCapacityTimeout"),
            WaitForElbCapacity=json_data.get("WaitForElbCapacity"),
            InitialLifecycleHook=json_data.get("InitialLifecycleHook"),
            LaunchTemplate=json_data.get("LaunchTemplate"),
            MixedInstancesPolicy=json_data.get("MixedInstancesPolicy"),
            Tag=json_data.get("Tag"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            InstancesDistribution=json_data.get("InstancesDistribution"),
            LaunchTemplateSpecification=json_data.get("LaunchTemplateSpecification"),
            Override=json_data.get("Override"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class InitialLifecycleHook:
    DefaultResult: Optional[str]
    HeartbeatTimeout: Optional[float]
    LifecycleTransition: Optional[str]
    Name: Optional[str]
    NotificationMetadata: Optional[str]
    NotificationTargetArn: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InitialLifecycleHook"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitialLifecycleHook"]:
        if not json_data:
            return None
        return cls(
            DefaultResult=json_data.get("DefaultResult"),
            HeartbeatTimeout=json_data.get("HeartbeatTimeout"),
            LifecycleTransition=json_data.get("LifecycleTransition"),
            Name=json_data.get("Name"),
            NotificationMetadata=json_data.get("NotificationMetadata"),
            NotificationTargetArn=json_data.get("NotificationTargetArn"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitialLifecycleHook = InitialLifecycleHook


@dataclass
class LaunchTemplate:
    LaunchTemplateSpecification: Optional[Sequence["_LaunchTemplateSpecification"]]
    Override: Optional[Sequence["_Override"]]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplate"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateSpecification=json_data.get("LaunchTemplateSpecification"),
            Override=json_data.get("Override"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplate = LaunchTemplate


@dataclass
class LaunchTemplateSpecification:
    LaunchTemplateId: Optional[str]
    LaunchTemplateName: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateSpecification"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateId=json_data.get("LaunchTemplateId"),
            LaunchTemplateName=json_data.get("LaunchTemplateName"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateSpecification = LaunchTemplateSpecification


@dataclass
class Override:
    InstanceType: Optional[str]
    WeightedCapacity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Override"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Override"]:
        if not json_data:
            return None
        return cls(
            InstanceType=json_data.get("InstanceType"),
            WeightedCapacity=json_data.get("WeightedCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Override = Override


@dataclass
class MixedInstancesPolicy:
    InstancesDistribution: Optional[Sequence["_InstancesDistribution"]]
    LaunchTemplate: Optional[Sequence["_LaunchTemplate"]]

    @classmethod
    def _deserialize(
        cls: Type["_MixedInstancesPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MixedInstancesPolicy"]:
        if not json_data:
            return None
        return cls(
            InstancesDistribution=json_data.get("InstancesDistribution"),
            LaunchTemplate=json_data.get("LaunchTemplate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MixedInstancesPolicy = MixedInstancesPolicy


@dataclass
class InstancesDistribution:
    OnDemandAllocationStrategy: Optional[str]
    OnDemandBaseCapacity: Optional[float]
    OnDemandPercentageAboveBaseCapacity: Optional[float]
    SpotAllocationStrategy: Optional[str]
    SpotInstancePools: Optional[float]
    SpotMaxPrice: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstancesDistribution"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstancesDistribution"]:
        if not json_data:
            return None
        return cls(
            OnDemandAllocationStrategy=json_data.get("OnDemandAllocationStrategy"),
            OnDemandBaseCapacity=json_data.get("OnDemandBaseCapacity"),
            OnDemandPercentageAboveBaseCapacity=json_data.get("OnDemandPercentageAboveBaseCapacity"),
            SpotAllocationStrategy=json_data.get("SpotAllocationStrategy"),
            SpotInstancePools=json_data.get("SpotInstancePools"),
            SpotMaxPrice=json_data.get("SpotMaxPrice"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstancesDistribution = InstancesDistribution


@dataclass
class Tag:
    Key: Optional[str]
    PropagateAtLaunch: Optional[bool]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            PropagateAtLaunch=json_data.get("PropagateAtLaunch"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


@dataclass
class Timeouts:
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


