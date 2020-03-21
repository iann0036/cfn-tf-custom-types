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
    CustomData: Optional[str]
    DesiredCapacity: Optional[float]
    LowPrioritySizes: Optional[Sequence[str]]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Name: Optional[str]
    OdSizes: Optional[Sequence[str]]
    Product: Optional[str]
    Region: Optional[str]
    ResourceGroupName: Optional[str]
    ShutdownScript: Optional[str]
    UserData: Optional[str]
    HealthCheck: Optional[Sequence["_HealthCheck"]]
    Image: Optional[Sequence["_Image"]]
    IntegrationKubernetes: Optional[Sequence["_IntegrationKubernetes"]]
    IntegrationMultaiRuntime: Optional[Sequence["_IntegrationMultaiRuntime"]]
    LoadBalancers: Optional[Sequence["_LoadBalancers"]]
    Login: Optional[Sequence["_Login"]]
    ManagedServiceIdentities: Optional[Sequence["_ManagedServiceIdentities"]]
    Network: Optional[Sequence["_Network"]]
    ScalingDownPolicy: Optional[Sequence["_ScalingDownPolicy"]]
    ScalingUpPolicy: Optional[Sequence["_ScalingUpPolicy"]]
    ScheduledTask: Optional[Sequence["_ScheduledTask"]]
    Strategy: Optional[Sequence["_Strategy"]]
    UpdatePolicy: Optional[Sequence["_UpdatePolicy"]]
    Custom: Optional[Sequence["_Custom"]]
    Marketplace: Optional[Sequence["_Marketplace"]]
    AdditionalIpConfigs: Optional[Sequence["_AdditionalIpConfigs"]]
    Dimensions: Optional[Sequence["_Dimensions"]]
    RollConfig: Optional[Sequence["_RollConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CustomData=json_data.get("CustomData"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            LowPrioritySizes=json_data.get("LowPrioritySizes"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Name=json_data.get("Name"),
            OdSizes=json_data.get("OdSizes"),
            Product=json_data.get("Product"),
            Region=json_data.get("Region"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ShutdownScript=json_data.get("ShutdownScript"),
            UserData=json_data.get("UserData"),
            HealthCheck=json_data.get("HealthCheck"),
            Image=json_data.get("Image"),
            IntegrationKubernetes=json_data.get("IntegrationKubernetes"),
            IntegrationMultaiRuntime=json_data.get("IntegrationMultaiRuntime"),
            LoadBalancers=json_data.get("LoadBalancers"),
            Login=json_data.get("Login"),
            ManagedServiceIdentities=json_data.get("ManagedServiceIdentities"),
            Network=json_data.get("Network"),
            ScalingDownPolicy=json_data.get("ScalingDownPolicy"),
            ScalingUpPolicy=json_data.get("ScalingUpPolicy"),
            ScheduledTask=json_data.get("ScheduledTask"),
            Strategy=json_data.get("Strategy"),
            UpdatePolicy=json_data.get("UpdatePolicy"),
            Custom=json_data.get("Custom"),
            Marketplace=json_data.get("Marketplace"),
            AdditionalIpConfigs=json_data.get("AdditionalIpConfigs"),
            Dimensions=json_data.get("Dimensions"),
            RollConfig=json_data.get("RollConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HealthCheck:
    AutoHealing: Optional[bool]
    GracePeriod: Optional[float]
    HealthCheckType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheck"]:
        if not json_data:
            return None
        return cls(
            AutoHealing=json_data.get("AutoHealing"),
            GracePeriod=json_data.get("GracePeriod"),
            HealthCheckType=json_data.get("HealthCheckType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheck = HealthCheck


@dataclass
class Image:
    Custom: Optional[Sequence["_Custom"]]
    Marketplace: Optional[Sequence["_Marketplace"]]

    @classmethod
    def _deserialize(
        cls: Type["_Image"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Image"]:
        if not json_data:
            return None
        return cls(
            Custom=json_data.get("Custom"),
            Marketplace=json_data.get("Marketplace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Image = Image


@dataclass
class Custom:
    ImageName: Optional[str]
    ResourceGroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Custom"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Custom"]:
        if not json_data:
            return None
        return cls(
            ImageName=json_data.get("ImageName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Custom = Custom


@dataclass
class Marketplace:
    Offer: Optional[str]
    Publisher: Optional[str]
    Sku: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Marketplace"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Marketplace"]:
        if not json_data:
            return None
        return cls(
            Offer=json_data.get("Offer"),
            Publisher=json_data.get("Publisher"),
            Sku=json_data.get("Sku"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Marketplace = Marketplace


@dataclass
class IntegrationKubernetes:
    ClusterIdentifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationKubernetes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationKubernetes"]:
        if not json_data:
            return None
        return cls(
            ClusterIdentifier=json_data.get("ClusterIdentifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationKubernetes = IntegrationKubernetes


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
class LoadBalancers:
    AutoWeight: Optional[bool]
    BalancerId: Optional[str]
    TargetSetId: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancers"]:
        if not json_data:
            return None
        return cls(
            AutoWeight=json_data.get("AutoWeight"),
            BalancerId=json_data.get("BalancerId"),
            TargetSetId=json_data.get("TargetSetId"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancers = LoadBalancers


@dataclass
class Login:
    Password: Optional[str]
    SshPublicKey: Optional[str]
    UserName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Login"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Login"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            SshPublicKey=json_data.get("SshPublicKey"),
            UserName=json_data.get("UserName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Login = Login


@dataclass
class ManagedServiceIdentities:
    Name: Optional[str]
    ResourceGroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedServiceIdentities"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedServiceIdentities"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedServiceIdentities = ManagedServiceIdentities


@dataclass
class Network:
    AssignPublicIp: Optional[bool]
    ResourceGroupName: Optional[str]
    SubnetName: Optional[str]
    VirtualNetworkName: Optional[str]
    AdditionalIpConfigs: Optional[Sequence["_AdditionalIpConfigs"]]

    @classmethod
    def _deserialize(
        cls: Type["_Network"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Network"]:
        if not json_data:
            return None
        return cls(
            AssignPublicIp=json_data.get("AssignPublicIp"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SubnetName=json_data.get("SubnetName"),
            VirtualNetworkName=json_data.get("VirtualNetworkName"),
            AdditionalIpConfigs=json_data.get("AdditionalIpConfigs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Network = Network


@dataclass
class AdditionalIpConfigs:
    Name: Optional[str]
    PrivateIpVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalIpConfigs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalIpConfigs"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PrivateIpVersion=json_data.get("PrivateIpVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalIpConfigs = AdditionalIpConfigs


@dataclass
class ScalingDownPolicy:
    ActionType: Optional[str]
    Adjustment: Optional[str]
    Cooldown: Optional[float]
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
    Adjustment: Optional[str]
    Cooldown: Optional[float]
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
    GracePeriod: Optional[str]
    IsEnabled: Optional[bool]
    ScaleMaxCapacity: Optional[str]
    ScaleMinCapacity: Optional[str]
    ScaleTargetCapacity: Optional[str]
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
            GracePeriod=json_data.get("GracePeriod"),
            IsEnabled=json_data.get("IsEnabled"),
            ScaleMaxCapacity=json_data.get("ScaleMaxCapacity"),
            ScaleMinCapacity=json_data.get("ScaleMinCapacity"),
            ScaleTargetCapacity=json_data.get("ScaleTargetCapacity"),
            TaskType=json_data.get("TaskType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledTask = ScheduledTask


@dataclass
class Strategy:
    DrainingTimeout: Optional[float]
    LowPriorityPercentage: Optional[float]
    OdCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Strategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Strategy"]:
        if not json_data:
            return None
        return cls(
            DrainingTimeout=json_data.get("DrainingTimeout"),
            LowPriorityPercentage=json_data.get("LowPriorityPercentage"),
            OdCount=json_data.get("OdCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Strategy = Strategy


@dataclass
class UpdatePolicy:
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
        )


# work around possible type aliasing issues when variable has same name as a model
_RollConfig = RollConfig


