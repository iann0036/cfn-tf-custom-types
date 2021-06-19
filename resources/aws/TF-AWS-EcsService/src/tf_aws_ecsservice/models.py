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
    Cluster: Optional[str]
    DeploymentMaximumPercent: Optional[float]
    DeploymentMinimumHealthyPercent: Optional[float]
    DesiredCount: Optional[float]
    EnableEcsManagedTags: Optional[bool]
    EnableExecuteCommand: Optional[bool]
    ForceNewDeployment: Optional[bool]
    HealthCheckGracePeriodSeconds: Optional[float]
    IamRole: Optional[str]
    Id: Optional[str]
    LaunchType: Optional[str]
    Name: Optional[str]
    PlatformVersion: Optional[str]
    PropagateTags: Optional[str]
    SchedulingStrategy: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    TaskDefinition: Optional[str]
    WaitForSteadyState: Optional[bool]
    CapacityProviderStrategy: Optional[Sequence["_CapacityProviderStrategyDefinition"]]
    DeploymentCircuitBreaker: Optional[Sequence["_DeploymentCircuitBreakerDefinition"]]
    DeploymentController: Optional[Sequence["_DeploymentControllerDefinition"]]
    LoadBalancer: Optional[Sequence["_LoadBalancerDefinition"]]
    NetworkConfiguration: Optional[Sequence["_NetworkConfigurationDefinition"]]
    OrderedPlacementStrategy: Optional[Sequence["_OrderedPlacementStrategyDefinition"]]
    PlacementConstraints: Optional[Sequence["_PlacementConstraintsDefinition"]]
    ServiceRegistries: Optional[Sequence["_ServiceRegistriesDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Cluster=json_data.get("Cluster"),
            DeploymentMaximumPercent=json_data.get("DeploymentMaximumPercent"),
            DeploymentMinimumHealthyPercent=json_data.get("DeploymentMinimumHealthyPercent"),
            DesiredCount=json_data.get("DesiredCount"),
            EnableEcsManagedTags=json_data.get("EnableEcsManagedTags"),
            EnableExecuteCommand=json_data.get("EnableExecuteCommand"),
            ForceNewDeployment=json_data.get("ForceNewDeployment"),
            HealthCheckGracePeriodSeconds=json_data.get("HealthCheckGracePeriodSeconds"),
            IamRole=json_data.get("IamRole"),
            Id=json_data.get("Id"),
            LaunchType=json_data.get("LaunchType"),
            Name=json_data.get("Name"),
            PlatformVersion=json_data.get("PlatformVersion"),
            PropagateTags=json_data.get("PropagateTags"),
            SchedulingStrategy=json_data.get("SchedulingStrategy"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            TaskDefinition=json_data.get("TaskDefinition"),
            WaitForSteadyState=json_data.get("WaitForSteadyState"),
            CapacityProviderStrategy=deserialize_list(json_data.get("CapacityProviderStrategy"), CapacityProviderStrategyDefinition),
            DeploymentCircuitBreaker=deserialize_list(json_data.get("DeploymentCircuitBreaker"), DeploymentCircuitBreakerDefinition),
            DeploymentController=deserialize_list(json_data.get("DeploymentController"), DeploymentControllerDefinition),
            LoadBalancer=deserialize_list(json_data.get("LoadBalancer"), LoadBalancerDefinition),
            NetworkConfiguration=deserialize_list(json_data.get("NetworkConfiguration"), NetworkConfigurationDefinition),
            OrderedPlacementStrategy=deserialize_list(json_data.get("OrderedPlacementStrategy"), OrderedPlacementStrategyDefinition),
            PlacementConstraints=deserialize_list(json_data.get("PlacementConstraints"), PlacementConstraintsDefinition),
            ServiceRegistries=deserialize_list(json_data.get("ServiceRegistries"), ServiceRegistriesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class CapacityProviderStrategyDefinition(BaseModel):
    Base: Optional[float]
    CapacityProvider: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityProviderStrategyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityProviderStrategyDefinition"]:
        if not json_data:
            return None
        return cls(
            Base=json_data.get("Base"),
            CapacityProvider=json_data.get("CapacityProvider"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityProviderStrategyDefinition = CapacityProviderStrategyDefinition


@dataclass
class DeploymentCircuitBreakerDefinition(BaseModel):
    Enable: Optional[bool]
    Rollback: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentCircuitBreakerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentCircuitBreakerDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Rollback=json_data.get("Rollback"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentCircuitBreakerDefinition = DeploymentCircuitBreakerDefinition


@dataclass
class DeploymentControllerDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentControllerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentControllerDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentControllerDefinition = DeploymentControllerDefinition


@dataclass
class LoadBalancerDefinition(BaseModel):
    ContainerName: Optional[str]
    ContainerPort: Optional[float]
    ElbName: Optional[str]
    TargetGroupArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancerDefinition"]:
        if not json_data:
            return None
        return cls(
            ContainerName=json_data.get("ContainerName"),
            ContainerPort=json_data.get("ContainerPort"),
            ElbName=json_data.get("ElbName"),
            TargetGroupArn=json_data.get("TargetGroupArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancerDefinition = LoadBalancerDefinition


@dataclass
class NetworkConfigurationDefinition(BaseModel):
    AssignPublicIp: Optional[bool]
    SecurityGroups: Optional[Sequence[str]]
    Subnets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AssignPublicIp=json_data.get("AssignPublicIp"),
            SecurityGroups=json_data.get("SecurityGroups"),
            Subnets=json_data.get("Subnets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfigurationDefinition = NetworkConfigurationDefinition


@dataclass
class OrderedPlacementStrategyDefinition(BaseModel):
    Field: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OrderedPlacementStrategyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrderedPlacementStrategyDefinition"]:
        if not json_data:
            return None
        return cls(
            Field=json_data.get("Field"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrderedPlacementStrategyDefinition = OrderedPlacementStrategyDefinition


@dataclass
class PlacementConstraintsDefinition(BaseModel):
    Expression: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementConstraintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementConstraintsDefinition"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementConstraintsDefinition = PlacementConstraintsDefinition


@dataclass
class ServiceRegistriesDefinition(BaseModel):
    ContainerName: Optional[str]
    ContainerPort: Optional[float]
    Port: Optional[float]
    RegistryArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceRegistriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceRegistriesDefinition"]:
        if not json_data:
            return None
        return cls(
            ContainerName=json_data.get("ContainerName"),
            ContainerPort=json_data.get("ContainerPort"),
            Port=json_data.get("Port"),
            RegistryArn=json_data.get("RegistryArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceRegistriesDefinition = ServiceRegistriesDefinition


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


