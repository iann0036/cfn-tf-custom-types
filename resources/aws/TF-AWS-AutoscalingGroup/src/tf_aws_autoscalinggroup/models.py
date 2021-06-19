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
    Arn: Optional[str]
    AvailabilityZones: Optional[Sequence[str]]
    CapacityRebalance: Optional[bool]
    DefaultCooldown: Optional[float]
    DesiredCapacity: Optional[float]
    EnabledMetrics: Optional[Sequence[str]]
    ForceDelete: Optional[bool]
    ForceDeleteWarmPool: Optional[bool]
    HealthCheckGracePeriod: Optional[float]
    HealthCheckType: Optional[str]
    Id: Optional[str]
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
    Tags: Optional[Sequence[Sequence["_TagsDefinition"]]]
    TargetGroupArns: Optional[Sequence[str]]
    TerminationPolicies: Optional[Sequence[str]]
    VpcZoneIdentifier: Optional[Sequence[str]]
    WaitForCapacityTimeout: Optional[str]
    WaitForElbCapacity: Optional[float]
    InitialLifecycleHook: Optional[Sequence["_InitialLifecycleHookDefinition"]]
    InstanceRefresh: Optional[Sequence["_InstanceRefreshDefinition"]]
    LaunchTemplate: Optional[Sequence["_LaunchTemplateDefinition"]]
    MixedInstancesPolicy: Optional[Sequence["_MixedInstancesPolicyDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    WarmPool: Optional[Sequence["_WarmPoolDefinition"]]

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
            Arn=json_data.get("Arn"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            CapacityRebalance=json_data.get("CapacityRebalance"),
            DefaultCooldown=json_data.get("DefaultCooldown"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            EnabledMetrics=json_data.get("EnabledMetrics"),
            ForceDelete=json_data.get("ForceDelete"),
            ForceDeleteWarmPool=json_data.get("ForceDeleteWarmPool"),
            HealthCheckGracePeriod=json_data.get("HealthCheckGracePeriod"),
            HealthCheckType=json_data.get("HealthCheckType"),
            Id=json_data.get("Id"),
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
            Tags=deserialize_list(json_data.get("Tags"), <ResolvedType(ContainerType.MODEL, TagsDefinition)>),
            TargetGroupArns=json_data.get("TargetGroupArns"),
            TerminationPolicies=json_data.get("TerminationPolicies"),
            VpcZoneIdentifier=json_data.get("VpcZoneIdentifier"),
            WaitForCapacityTimeout=json_data.get("WaitForCapacityTimeout"),
            WaitForElbCapacity=json_data.get("WaitForElbCapacity"),
            InitialLifecycleHook=deserialize_list(json_data.get("InitialLifecycleHook"), InitialLifecycleHookDefinition),
            InstanceRefresh=deserialize_list(json_data.get("InstanceRefresh"), InstanceRefreshDefinition),
            LaunchTemplate=deserialize_list(json_data.get("LaunchTemplate"), LaunchTemplateDefinition),
            MixedInstancesPolicy=deserialize_list(json_data.get("MixedInstancesPolicy"), MixedInstancesPolicyDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            WarmPool=deserialize_list(json_data.get("WarmPool"), WarmPoolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class InitialLifecycleHookDefinition(BaseModel):
    DefaultResult: Optional[str]
    HeartbeatTimeout: Optional[float]
    LifecycleTransition: Optional[str]
    Name: Optional[str]
    NotificationMetadata: Optional[str]
    NotificationTargetArn: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InitialLifecycleHookDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitialLifecycleHookDefinition"]:
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
_InitialLifecycleHookDefinition = InitialLifecycleHookDefinition


@dataclass
class InstanceRefreshDefinition(BaseModel):
    Strategy: Optional[str]
    Triggers: Optional[Sequence[str]]
    Preferences: Optional[Sequence["_PreferencesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceRefreshDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceRefreshDefinition"]:
        if not json_data:
            return None
        return cls(
            Strategy=json_data.get("Strategy"),
            Triggers=json_data.get("Triggers"),
            Preferences=deserialize_list(json_data.get("Preferences"), PreferencesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceRefreshDefinition = InstanceRefreshDefinition


@dataclass
class PreferencesDefinition(BaseModel):
    InstanceWarmup: Optional[str]
    MinHealthyPercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PreferencesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PreferencesDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceWarmup=json_data.get("InstanceWarmup"),
            MinHealthyPercentage=json_data.get("MinHealthyPercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PreferencesDefinition = PreferencesDefinition


@dataclass
class LaunchTemplateDefinition(BaseModel):
    LaunchTemplateSpecification: Optional[Sequence["_LaunchTemplateSpecificationDefinition"]]
    Override: Optional[Sequence["_OverrideDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateSpecification=deserialize_list(json_data.get("LaunchTemplateSpecification"), LaunchTemplateSpecificationDefinition),
            Override=deserialize_list(json_data.get("Override"), OverrideDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateDefinition = LaunchTemplateDefinition


@dataclass
class LaunchTemplateSpecificationDefinition(BaseModel):
    LaunchTemplateId: Optional[str]
    LaunchTemplateName: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateId=json_data.get("LaunchTemplateId"),
            LaunchTemplateName=json_data.get("LaunchTemplateName"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateSpecificationDefinition = LaunchTemplateSpecificationDefinition


@dataclass
class OverrideDefinition(BaseModel):
    InstanceType: Optional[str]
    WeightedCapacity: Optional[str]
    LaunchTemplateSpecification: Optional[Sequence["_LaunchTemplateSpecificationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OverrideDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverrideDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceType=json_data.get("InstanceType"),
            WeightedCapacity=json_data.get("WeightedCapacity"),
            LaunchTemplateSpecification=deserialize_list(json_data.get("LaunchTemplateSpecification"), LaunchTemplateSpecificationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverrideDefinition = OverrideDefinition


@dataclass
class MixedInstancesPolicyDefinition(BaseModel):
    InstancesDistribution: Optional[Sequence["_InstancesDistributionDefinition"]]
    LaunchTemplate: Optional[Sequence["_LaunchTemplateDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MixedInstancesPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MixedInstancesPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            InstancesDistribution=deserialize_list(json_data.get("InstancesDistribution"), InstancesDistributionDefinition),
            LaunchTemplate=deserialize_list(json_data.get("LaunchTemplate"), LaunchTemplateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MixedInstancesPolicyDefinition = MixedInstancesPolicyDefinition


@dataclass
class InstancesDistributionDefinition(BaseModel):
    OnDemandAllocationStrategy: Optional[str]
    OnDemandBaseCapacity: Optional[float]
    OnDemandPercentageAboveBaseCapacity: Optional[float]
    SpotAllocationStrategy: Optional[str]
    SpotInstancePools: Optional[float]
    SpotMaxPrice: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstancesDistributionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstancesDistributionDefinition"]:
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
_InstancesDistributionDefinition = InstancesDistributionDefinition


@dataclass
class TagDefinition(BaseModel):
    Key: Optional[str]
    PropagateAtLaunch: Optional[bool]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            PropagateAtLaunch=json_data.get("PropagateAtLaunch"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class WarmPoolDefinition(BaseModel):
    MaxGroupPreparedCapacity: Optional[float]
    MinSize: Optional[float]
    PoolState: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WarmPoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WarmPoolDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxGroupPreparedCapacity=json_data.get("MaxGroupPreparedCapacity"),
            MinSize=json_data.get("MinSize"),
            PoolState=json_data.get("PoolState"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WarmPoolDefinition = WarmPoolDefinition


