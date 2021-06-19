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
    AppServer: Optional[str]
    AppServerVersion: Optional[str]
    Arn: Optional[str]
    AutoAssignElasticIps: Optional[bool]
    AutoAssignPublicIps: Optional[bool]
    AutoHealing: Optional[bool]
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
    Id: Optional[str]
    InstallUpdatesOnBoot: Optional[bool]
    InstanceShutdownTimeout: Optional[float]
    JvmOptions: Optional[str]
    JvmType: Optional[str]
    JvmVersion: Optional[str]
    Name: Optional[str]
    StackId: Optional[str]
    SystemPackages: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    UseEbsOptimizedInstances: Optional[bool]
    EbsVolume: Optional[Sequence["_EbsVolumeDefinition"]]

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
            AppServer=json_data.get("AppServer"),
            AppServerVersion=json_data.get("AppServerVersion"),
            Arn=json_data.get("Arn"),
            AutoAssignElasticIps=json_data.get("AutoAssignElasticIps"),
            AutoAssignPublicIps=json_data.get("AutoAssignPublicIps"),
            AutoHealing=json_data.get("AutoHealing"),
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
            Id=json_data.get("Id"),
            InstallUpdatesOnBoot=json_data.get("InstallUpdatesOnBoot"),
            InstanceShutdownTimeout=json_data.get("InstanceShutdownTimeout"),
            JvmOptions=json_data.get("JvmOptions"),
            JvmType=json_data.get("JvmType"),
            JvmVersion=json_data.get("JvmVersion"),
            Name=json_data.get("Name"),
            StackId=json_data.get("StackId"),
            SystemPackages=json_data.get("SystemPackages"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            UseEbsOptimizedInstances=json_data.get("UseEbsOptimizedInstances"),
            EbsVolume=deserialize_list(json_data.get("EbsVolume"), EbsVolumeDefinition),
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
class EbsVolumeDefinition(BaseModel):
    Encrypted: Optional[bool]
    Iops: Optional[float]
    MountPoint: Optional[str]
    NumberOfDisks: Optional[float]
    RaidLevel: Optional[str]
    Size: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsVolumeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsVolumeDefinition"]:
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
_EbsVolumeDefinition = EbsVolumeDefinition


