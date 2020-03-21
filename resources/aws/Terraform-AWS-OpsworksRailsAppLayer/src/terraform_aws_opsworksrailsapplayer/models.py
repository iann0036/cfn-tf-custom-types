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
    AppServer: Optional[str]
    Arn: Optional[str]
    AutoAssignElasticIps: Optional[bool]
    AutoAssignPublicIps: Optional[bool]
    AutoHealing: Optional[bool]
    BundlerVersion: Optional[str]
    CustomConfigureRecipes: Optional[Sequence[str]]
    CustomDeployRecipes: Optional[Sequence[str]]
    CustomInstanceProfileArn: Optional[str]
    CustomJson: Optional[str]
    CustomSecurityGroupIds: Optional[Sequence[str]]
    CustomSetupRecipes: Optional[Sequence[str]]
    CustomShutdownRecipes: Optional[Sequence[str]]
    CustomUndeployRecipes: Optional[Sequence[str]]
    DrainElbOnShutdown: Optional[bool]
    ElasticLoadBalancer: Optional[str]
    InstallUpdatesOnBoot: Optional[bool]
    InstanceShutdownTimeout: Optional[float]
    ManageBundler: Optional[bool]
    Name: Optional[str]
    PassengerVersion: Optional[str]
    RubyVersion: Optional[str]
    RubygemsVersion: Optional[str]
    StackId: Optional[str]
    SystemPackages: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    UseEbsOptimizedInstances: Optional[bool]
    EbsVolume: Optional[Sequence["_EbsVolume"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AppServer=json_data.get("AppServer"),
            Arn=json_data.get("Arn"),
            AutoAssignElasticIps=json_data.get("AutoAssignElasticIps"),
            AutoAssignPublicIps=json_data.get("AutoAssignPublicIps"),
            AutoHealing=json_data.get("AutoHealing"),
            BundlerVersion=json_data.get("BundlerVersion"),
            CustomConfigureRecipes=json_data.get("CustomConfigureRecipes"),
            CustomDeployRecipes=json_data.get("CustomDeployRecipes"),
            CustomInstanceProfileArn=json_data.get("CustomInstanceProfileArn"),
            CustomJson=json_data.get("CustomJson"),
            CustomSecurityGroupIds=json_data.get("CustomSecurityGroupIds"),
            CustomSetupRecipes=json_data.get("CustomSetupRecipes"),
            CustomShutdownRecipes=json_data.get("CustomShutdownRecipes"),
            CustomUndeployRecipes=json_data.get("CustomUndeployRecipes"),
            DrainElbOnShutdown=json_data.get("DrainElbOnShutdown"),
            ElasticLoadBalancer=json_data.get("ElasticLoadBalancer"),
            InstallUpdatesOnBoot=json_data.get("InstallUpdatesOnBoot"),
            InstanceShutdownTimeout=json_data.get("InstanceShutdownTimeout"),
            ManageBundler=json_data.get("ManageBundler"),
            Name=json_data.get("Name"),
            PassengerVersion=json_data.get("PassengerVersion"),
            RubyVersion=json_data.get("RubyVersion"),
            RubygemsVersion=json_data.get("RubygemsVersion"),
            StackId=json_data.get("StackId"),
            SystemPackages=json_data.get("SystemPackages"),
            Tags=json_data.get("Tags"),
            UseEbsOptimizedInstances=json_data.get("UseEbsOptimizedInstances"),
            EbsVolume=json_data.get("EbsVolume"),
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
class EbsVolume:
    Encrypted: Optional[bool]
    Iops: Optional[float]
    MountPoint: Optional[str]
    NumberOfDisks: Optional[float]
    RaidLevel: Optional[str]
    Size: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsVolume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsVolume"]:
        if not json_data:
            return None
        return cls(
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            MountPoint=json_data.get("MountPoint"),
            NumberOfDisks=json_data.get("NumberOfDisks"),
            RaidLevel=json_data.get("RaidLevel"),
            Size=json_data.get("Size"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsVolume = EbsVolume


