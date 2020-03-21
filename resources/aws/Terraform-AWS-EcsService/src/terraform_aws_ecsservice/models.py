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
    Cluster: Optional[str]
    DeploymentMaximumPercent: Optional[float]
    DeploymentMinimumHealthyPercent: Optional[float]
    DesiredCount: Optional[float]
    EnableEcsManagedTags: Optional[bool]
    HealthCheckGracePeriodSeconds: Optional[float]
    IamRole: Optional[str]
    Id: Optional[str]
    LaunchType: Optional[str]
    Name: Optional[str]
    PlatformVersion: Optional[str]
    PropagateTags: Optional[str]
    SchedulingStrategy: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TaskDefinition: Optional[str]
    CapacityProviderStrategy: Optional[Sequence["_CapacityProviderStrategy"]]
    DeploymentController: Optional[Sequence["_DeploymentController"]]
    LoadBalancer: Optional[Sequence["_LoadBalancer"]]
    NetworkConfiguration: Optional[Sequence["_NetworkConfiguration"]]
    OrderedPlacementStrategy: Optional[Sequence["_OrderedPlacementStrategy"]]
    PlacementConstraints: Optional[Sequence["_PlacementConstraints"]]
    PlacementStrategy: Optional[Sequence["_PlacementStrategy"]]
    ServiceRegistries: Optional[Sequence["_ServiceRegistries"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Cluster=json_data.get("Cluster"),
            DeploymentMaximumPercent=json_data.get("DeploymentMaximumPercent"),
            DeploymentMinimumHealthyPercent=json_data.get("DeploymentMinimumHealthyPercent"),
            DesiredCount=json_data.get("DesiredCount"),
            EnableEcsManagedTags=json_data.get("EnableEcsManagedTags"),
            HealthCheckGracePeriodSeconds=json_data.get("HealthCheckGracePeriodSeconds"),
            IamRole=json_data.get("IamRole"),
            Id=json_data.get("Id"),
            LaunchType=json_data.get("LaunchType"),
            Name=json_data.get("Name"),
            PlatformVersion=json_data.get("PlatformVersion"),
            PropagateTags=json_data.get("PropagateTags"),
            SchedulingStrategy=json_data.get("SchedulingStrategy"),
            Tags=json_data.get("Tags"),
            TaskDefinition=json_data.get("TaskDefinition"),
            CapacityProviderStrategy=json_data.get("CapacityProviderStrategy"),
            DeploymentController=json_data.get("DeploymentController"),
            LoadBalancer=json_data.get("LoadBalancer"),
            NetworkConfiguration=json_data.get("NetworkConfiguration"),
            OrderedPlacementStrategy=json_data.get("OrderedPlacementStrategy"),
            PlacementConstraints=json_data.get("PlacementConstraints"),
            PlacementStrategy=json_data.get("PlacementStrategy"),
            ServiceRegistries=json_data.get("ServiceRegistries"),
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
class CapacityProviderStrategy:
    Base: Optional[float]
    CapacityProvider: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityProviderStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityProviderStrategy"]:
        if not json_data:
            return None
        return cls(
            Base=json_data.get("Base"),
            CapacityProvider=json_data.get("CapacityProvider"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityProviderStrategy = CapacityProviderStrategy


@dataclass
class DeploymentController:
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentController"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentController"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentController = DeploymentController


@dataclass
class LoadBalancer:
    ContainerName: Optional[str]
    ContainerPort: Optional[float]
    ElbName: Optional[str]
    TargetGroupArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancer"]:
        if not json_data:
            return None
        return cls(
            ContainerName=json_data.get("ContainerName"),
            ContainerPort=json_data.get("ContainerPort"),
            ElbName=json_data.get("ElbName"),
            TargetGroupArn=json_data.get("TargetGroupArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancer = LoadBalancer


@dataclass
class NetworkConfiguration:
    AssignPublicIp: Optional[bool]
    SecurityGroups: Optional[Sequence[str]]
    Subnets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfiguration"]:
        if not json_data:
            return None
        return cls(
            AssignPublicIp=json_data.get("AssignPublicIp"),
            SecurityGroups=json_data.get("SecurityGroups"),
            Subnets=json_data.get("Subnets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfiguration = NetworkConfiguration


@dataclass
class OrderedPlacementStrategy:
    Field: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OrderedPlacementStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrderedPlacementStrategy"]:
        if not json_data:
            return None
        return cls(
            Field=json_data.get("Field"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrderedPlacementStrategy = OrderedPlacementStrategy


@dataclass
class PlacementConstraints:
    Expression: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementConstraints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementConstraints"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementConstraints = PlacementConstraints


@dataclass
class PlacementStrategy:
    Field: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementStrategy"]:
        if not json_data:
            return None
        return cls(
            Field=json_data.get("Field"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementStrategy = PlacementStrategy


@dataclass
class ServiceRegistries:
    ContainerName: Optional[str]
    ContainerPort: Optional[float]
    Port: Optional[float]
    RegistryArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceRegistries"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceRegistries"]:
        if not json_data:
            return None
        return cls(
            ContainerName=json_data.get("ContainerName"),
            ContainerPort=json_data.get("ContainerPort"),
            Port=json_data.get("Port"),
            RegistryArn=json_data.get("RegistryArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceRegistries = ServiceRegistries


