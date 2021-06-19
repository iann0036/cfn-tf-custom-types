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
    CustomData: Optional[str]
    DesiredCapacity: Optional[float]
    Id: Optional[str]
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
    HealthCheck: Optional[Sequence["_HealthCheckDefinition"]]
    Image: Optional[Sequence["_ImageDefinition"]]
    IntegrationKubernetes: Optional[Sequence["_IntegrationKubernetesDefinition"]]
    IntegrationMultaiRuntime: Optional[Sequence["_IntegrationMultaiRuntimeDefinition"]]
    LoadBalancers: Optional[Sequence["_LoadBalancersDefinition"]]
    Login: Optional[Sequence["_LoginDefinition"]]
    ManagedServiceIdentities: Optional[Sequence["_ManagedServiceIdentitiesDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
    ScalingDownPolicy: Optional[Sequence["_ScalingDownPolicyDefinition"]]
    ScalingUpPolicy: Optional[Sequence["_ScalingUpPolicyDefinition"]]
    ScheduledTask: Optional[Sequence["_ScheduledTaskDefinition"]]
    Strategy: Optional[Sequence["_StrategyDefinition"]]
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
            CustomData=json_data.get("CustomData"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            Id=json_data.get("Id"),
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
            HealthCheck=deserialize_list(json_data.get("HealthCheck"), HealthCheckDefinition),
            Image=deserialize_list(json_data.get("Image"), ImageDefinition),
            IntegrationKubernetes=deserialize_list(json_data.get("IntegrationKubernetes"), IntegrationKubernetesDefinition),
            IntegrationMultaiRuntime=deserialize_list(json_data.get("IntegrationMultaiRuntime"), IntegrationMultaiRuntimeDefinition),
            LoadBalancers=deserialize_list(json_data.get("LoadBalancers"), LoadBalancersDefinition),
            Login=deserialize_list(json_data.get("Login"), LoginDefinition),
            ManagedServiceIdentities=deserialize_list(json_data.get("ManagedServiceIdentities"), ManagedServiceIdentitiesDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            ScalingDownPolicy=deserialize_list(json_data.get("ScalingDownPolicy"), ScalingDownPolicyDefinition),
            ScalingUpPolicy=deserialize_list(json_data.get("ScalingUpPolicy"), ScalingUpPolicyDefinition),
            ScheduledTask=deserialize_list(json_data.get("ScheduledTask"), ScheduledTaskDefinition),
            Strategy=deserialize_list(json_data.get("Strategy"), StrategyDefinition),
            UpdatePolicy=deserialize_list(json_data.get("UpdatePolicy"), UpdatePolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HealthCheckDefinition(BaseModel):
    AutoHealing: Optional[bool]
    GracePeriod: Optional[float]
    HealthCheckType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoHealing=json_data.get("AutoHealing"),
            GracePeriod=json_data.get("GracePeriod"),
            HealthCheckType=json_data.get("HealthCheckType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckDefinition = HealthCheckDefinition


@dataclass
class ImageDefinition(BaseModel):
    Custom: Optional[Sequence["_CustomDefinition"]]
    Marketplace: Optional[Sequence["_MarketplaceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ImageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageDefinition"]:
        if not json_data:
            return None
        return cls(
            Custom=deserialize_list(json_data.get("Custom"), CustomDefinition),
            Marketplace=deserialize_list(json_data.get("Marketplace"), MarketplaceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageDefinition = ImageDefinition


@dataclass
class CustomDefinition(BaseModel):
    ImageName: Optional[str]
    ResourceGroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomDefinition"]:
        if not json_data:
            return None
        return cls(
            ImageName=json_data.get("ImageName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomDefinition = CustomDefinition


@dataclass
class MarketplaceDefinition(BaseModel):
    Offer: Optional[str]
    Publisher: Optional[str]
    Sku: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MarketplaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarketplaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Offer=json_data.get("Offer"),
            Publisher=json_data.get("Publisher"),
            Sku=json_data.get("Sku"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarketplaceDefinition = MarketplaceDefinition


@dataclass
class IntegrationKubernetesDefinition(BaseModel):
    ClusterIdentifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationKubernetesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationKubernetesDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterIdentifier=json_data.get("ClusterIdentifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationKubernetesDefinition = IntegrationKubernetesDefinition


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
class LoadBalancersDefinition(BaseModel):
    AutoWeight: Optional[bool]
    BalancerId: Optional[str]
    TargetSetId: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancersDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoWeight=json_data.get("AutoWeight"),
            BalancerId=json_data.get("BalancerId"),
            TargetSetId=json_data.get("TargetSetId"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancersDefinition = LoadBalancersDefinition


@dataclass
class LoginDefinition(BaseModel):
    Password: Optional[str]
    SshPublicKey: Optional[str]
    UserName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoginDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoginDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            SshPublicKey=json_data.get("SshPublicKey"),
            UserName=json_data.get("UserName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoginDefinition = LoginDefinition


@dataclass
class ManagedServiceIdentitiesDefinition(BaseModel):
    Name: Optional[str]
    ResourceGroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedServiceIdentitiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedServiceIdentitiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedServiceIdentitiesDefinition = ManagedServiceIdentitiesDefinition


@dataclass
class NetworkDefinition(BaseModel):
    AssignPublicIp: Optional[bool]
    ResourceGroupName: Optional[str]
    SubnetName: Optional[str]
    VirtualNetworkName: Optional[str]
    AdditionalIpConfigs: Optional[Sequence["_AdditionalIpConfigsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            AssignPublicIp=json_data.get("AssignPublicIp"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SubnetName=json_data.get("SubnetName"),
            VirtualNetworkName=json_data.get("VirtualNetworkName"),
            AdditionalIpConfigs=deserialize_list(json_data.get("AdditionalIpConfigs"), AdditionalIpConfigsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class AdditionalIpConfigsDefinition(BaseModel):
    Name: Optional[str]
    PrivateIpVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalIpConfigsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalIpConfigsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PrivateIpVersion=json_data.get("PrivateIpVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalIpConfigsDefinition = AdditionalIpConfigsDefinition


@dataclass
class ScalingDownPolicyDefinition(BaseModel):
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
    GracePeriod: Optional[str]
    IsEnabled: Optional[bool]
    ScaleMaxCapacity: Optional[str]
    ScaleMinCapacity: Optional[str]
    ScaleTargetCapacity: Optional[str]
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
            GracePeriod=json_data.get("GracePeriod"),
            IsEnabled=json_data.get("IsEnabled"),
            ScaleMaxCapacity=json_data.get("ScaleMaxCapacity"),
            ScaleMinCapacity=json_data.get("ScaleMinCapacity"),
            ScaleTargetCapacity=json_data.get("ScaleTargetCapacity"),
            TaskType=json_data.get("TaskType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledTaskDefinition = ScheduledTaskDefinition


@dataclass
class StrategyDefinition(BaseModel):
    DrainingTimeout: Optional[float]
    LowPriorityPercentage: Optional[float]
    OdCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StrategyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StrategyDefinition"]:
        if not json_data:
            return None
        return cls(
            DrainingTimeout=json_data.get("DrainingTimeout"),
            LowPriorityPercentage=json_data.get("LowPriorityPercentage"),
            OdCount=json_data.get("OdCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StrategyDefinition = StrategyDefinition


@dataclass
class UpdatePolicyDefinition(BaseModel):
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
        )


# work around possible type aliasing issues when variable has same name as a model
_RollConfigDefinition = RollConfigDefinition


