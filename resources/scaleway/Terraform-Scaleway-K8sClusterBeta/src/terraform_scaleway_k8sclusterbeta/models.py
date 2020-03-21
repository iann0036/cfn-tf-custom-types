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
    AdmissionPlugins: Optional[Sequence[str]]
    ApiserverUrl: Optional[str]
    Cni: Optional[str]
    CreatedAt: Optional[str]
    Description: Optional[str]
    EnableDashboard: Optional[bool]
    FeatureGates: Optional[Sequence[str]]
    Ingress: Optional[str]
    Kubeconfig: Optional[Sequence["_Kubeconfig"]]
    Name: Optional[str]
    OrganizationId: Optional[str]
    Region: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence[str]]
    UpdatedAt: Optional[str]
    UpgradeAvailable: Optional[bool]
    Version: Optional[str]
    WildcardDns: Optional[str]
    AutoUpgrade: Optional[Sequence["_AutoUpgrade"]]
    AutoscalerConfig: Optional[Sequence["_AutoscalerConfig"]]
    DefaultPool: Optional[Sequence["_DefaultPool"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdmissionPlugins=json_data.get("AdmissionPlugins"),
            ApiserverUrl=json_data.get("ApiserverUrl"),
            Cni=json_data.get("Cni"),
            CreatedAt=json_data.get("CreatedAt"),
            Description=json_data.get("Description"),
            EnableDashboard=json_data.get("EnableDashboard"),
            FeatureGates=json_data.get("FeatureGates"),
            Ingress=json_data.get("Ingress"),
            Kubeconfig=json_data.get("Kubeconfig"),
            Name=json_data.get("Name"),
            OrganizationId=json_data.get("OrganizationId"),
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            UpdatedAt=json_data.get("UpdatedAt"),
            UpgradeAvailable=json_data.get("UpgradeAvailable"),
            Version=json_data.get("Version"),
            WildcardDns=json_data.get("WildcardDns"),
            AutoUpgrade=json_data.get("AutoUpgrade"),
            AutoscalerConfig=json_data.get("AutoscalerConfig"),
            DefaultPool=json_data.get("DefaultPool"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Kubeconfig:
    ClusterCaCertificate: Optional[str]
    ConfigFile: Optional[str]
    Host: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Kubeconfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Kubeconfig"]:
        if not json_data:
            return None
        return cls(
            ClusterCaCertificate=json_data.get("ClusterCaCertificate"),
            ConfigFile=json_data.get("ConfigFile"),
            Host=json_data.get("Host"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Kubeconfig = Kubeconfig


@dataclass
class AutoUpgrade:
    Enable: Optional[bool]
    MaintenanceWindowDay: Optional[str]
    MaintenanceWindowStartHour: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoUpgrade"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoUpgrade"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            MaintenanceWindowDay=json_data.get("MaintenanceWindowDay"),
            MaintenanceWindowStartHour=json_data.get("MaintenanceWindowStartHour"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoUpgrade = AutoUpgrade


@dataclass
class AutoscalerConfig:
    BalanceSimilarNodeGroups: Optional[bool]
    DisableScaleDown: Optional[bool]
    Estimator: Optional[str]
    Expander: Optional[str]
    ExpendablePodsPriorityCutoff: Optional[float]
    IgnoreDaemonsetsUtilization: Optional[bool]
    ScaleDownDelayAfterAdd: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscalerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscalerConfig"]:
        if not json_data:
            return None
        return cls(
            BalanceSimilarNodeGroups=json_data.get("BalanceSimilarNodeGroups"),
            DisableScaleDown=json_data.get("DisableScaleDown"),
            Estimator=json_data.get("Estimator"),
            Expander=json_data.get("Expander"),
            ExpendablePodsPriorityCutoff=json_data.get("ExpendablePodsPriorityCutoff"),
            IgnoreDaemonsetsUtilization=json_data.get("IgnoreDaemonsetsUtilization"),
            ScaleDownDelayAfterAdd=json_data.get("ScaleDownDelayAfterAdd"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscalerConfig = AutoscalerConfig


@dataclass
class DefaultPool:
    Autohealing: Optional[bool]
    Autoscaling: Optional[bool]
    ContainerRuntime: Optional[str]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    NodeType: Optional[str]
    PlacementGroupId: Optional[str]
    Size: Optional[float]
    Tags: Optional[Sequence[str]]
    WaitForPoolReady: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultPool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultPool"]:
        if not json_data:
            return None
        return cls(
            Autohealing=json_data.get("Autohealing"),
            Autoscaling=json_data.get("Autoscaling"),
            ContainerRuntime=json_data.get("ContainerRuntime"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            NodeType=json_data.get("NodeType"),
            PlacementGroupId=json_data.get("PlacementGroupId"),
            Size=json_data.get("Size"),
            Tags=json_data.get("Tags"),
            WaitForPoolReady=json_data.get("WaitForPoolReady"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultPool = DefaultPool


