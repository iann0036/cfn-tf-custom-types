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
    AdmissionPlugins: Optional[Sequence[str]]
    ApiserverCertSans: Optional[Sequence[str]]
    ApiserverUrl: Optional[str]
    Cni: Optional[str]
    CreatedAt: Optional[str]
    DeleteAdditionalResources: Optional[bool]
    Description: Optional[str]
    FeatureGates: Optional[Sequence[str]]
    Id: Optional[str]
    Kubeconfig: Optional[Sequence["_KubeconfigDefinition"]]
    Name: Optional[str]
    OrganizationId: Optional[str]
    ProjectId: Optional[str]
    Region: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence[str]]
    UpdatedAt: Optional[str]
    UpgradeAvailable: Optional[bool]
    Version: Optional[str]
    WildcardDns: Optional[str]
    AutoUpgrade: Optional[Sequence["_AutoUpgradeDefinition"]]
    AutoscalerConfig: Optional[Sequence["_AutoscalerConfigDefinition"]]
    OpenIdConnectConfig: Optional[Sequence["_OpenIdConnectConfigDefinition"]]
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
            AdmissionPlugins=json_data.get("AdmissionPlugins"),
            ApiserverCertSans=json_data.get("ApiserverCertSans"),
            ApiserverUrl=json_data.get("ApiserverUrl"),
            Cni=json_data.get("Cni"),
            CreatedAt=json_data.get("CreatedAt"),
            DeleteAdditionalResources=json_data.get("DeleteAdditionalResources"),
            Description=json_data.get("Description"),
            FeatureGates=json_data.get("FeatureGates"),
            Id=json_data.get("Id"),
            Kubeconfig=deserialize_list(json_data.get("Kubeconfig"), KubeconfigDefinition),
            Name=json_data.get("Name"),
            OrganizationId=json_data.get("OrganizationId"),
            ProjectId=json_data.get("ProjectId"),
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            UpdatedAt=json_data.get("UpdatedAt"),
            UpgradeAvailable=json_data.get("UpgradeAvailable"),
            Version=json_data.get("Version"),
            WildcardDns=json_data.get("WildcardDns"),
            AutoUpgrade=deserialize_list(json_data.get("AutoUpgrade"), AutoUpgradeDefinition),
            AutoscalerConfig=deserialize_list(json_data.get("AutoscalerConfig"), AutoscalerConfigDefinition),
            OpenIdConnectConfig=deserialize_list(json_data.get("OpenIdConnectConfig"), OpenIdConnectConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class KubeconfigDefinition(BaseModel):
    ClusterCaCertificate: Optional[str]
    ConfigFile: Optional[str]
    Host: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubeconfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeconfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterCaCertificate=json_data.get("ClusterCaCertificate"),
            ConfigFile=json_data.get("ConfigFile"),
            Host=json_data.get("Host"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeconfigDefinition = KubeconfigDefinition


@dataclass
class AutoUpgradeDefinition(BaseModel):
    Enable: Optional[bool]
    MaintenanceWindowDay: Optional[str]
    MaintenanceWindowStartHour: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoUpgradeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoUpgradeDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            MaintenanceWindowDay=json_data.get("MaintenanceWindowDay"),
            MaintenanceWindowStartHour=json_data.get("MaintenanceWindowStartHour"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoUpgradeDefinition = AutoUpgradeDefinition


@dataclass
class AutoscalerConfigDefinition(BaseModel):
    BalanceSimilarNodeGroups: Optional[bool]
    DisableScaleDown: Optional[bool]
    Estimator: Optional[str]
    Expander: Optional[str]
    ExpendablePodsPriorityCutoff: Optional[float]
    IgnoreDaemonsetsUtilization: Optional[bool]
    MaxGracefulTerminationSec: Optional[float]
    ScaleDownDelayAfterAdd: Optional[str]
    ScaleDownUnneededTime: Optional[str]
    ScaleDownUtilizationThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscalerConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscalerConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BalanceSimilarNodeGroups=json_data.get("BalanceSimilarNodeGroups"),
            DisableScaleDown=json_data.get("DisableScaleDown"),
            Estimator=json_data.get("Estimator"),
            Expander=json_data.get("Expander"),
            ExpendablePodsPriorityCutoff=json_data.get("ExpendablePodsPriorityCutoff"),
            IgnoreDaemonsetsUtilization=json_data.get("IgnoreDaemonsetsUtilization"),
            MaxGracefulTerminationSec=json_data.get("MaxGracefulTerminationSec"),
            ScaleDownDelayAfterAdd=json_data.get("ScaleDownDelayAfterAdd"),
            ScaleDownUnneededTime=json_data.get("ScaleDownUnneededTime"),
            ScaleDownUtilizationThreshold=json_data.get("ScaleDownUtilizationThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscalerConfigDefinition = AutoscalerConfigDefinition


@dataclass
class OpenIdConnectConfigDefinition(BaseModel):
    ClientId: Optional[str]
    GroupsClaim: Optional[Sequence[str]]
    GroupsPrefix: Optional[str]
    IssuerUrl: Optional[str]
    RequiredClaim: Optional[Sequence[str]]
    UsernameClaim: Optional[str]
    UsernamePrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OpenIdConnectConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenIdConnectConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            GroupsClaim=json_data.get("GroupsClaim"),
            GroupsPrefix=json_data.get("GroupsPrefix"),
            IssuerUrl=json_data.get("IssuerUrl"),
            RequiredClaim=json_data.get("RequiredClaim"),
            UsernameClaim=json_data.get("UsernameClaim"),
            UsernamePrefix=json_data.get("UsernamePrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenIdConnectConfigDefinition = OpenIdConnectConfigDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Default: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


