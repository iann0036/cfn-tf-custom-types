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
    AppName: Optional[str]
    Arn: Optional[str]
    AutoscalingGroups: Optional[Sequence[str]]
    ComputePlatform: Optional[str]
    DeploymentConfigName: Optional[str]
    DeploymentGroupId: Optional[str]
    DeploymentGroupName: Optional[str]
    Id: Optional[str]
    ServiceRoleArn: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    AlarmConfiguration: Optional[Sequence["_AlarmConfigurationDefinition"]]
    AutoRollbackConfiguration: Optional[Sequence["_AutoRollbackConfigurationDefinition"]]
    BlueGreenDeploymentConfig: Optional[Sequence["_BlueGreenDeploymentConfigDefinition"]]
    DeploymentStyle: Optional[Sequence["_DeploymentStyleDefinition"]]
    Ec2TagFilter: Optional[Sequence["_Ec2TagFilterDefinition"]]
    Ec2TagSet: Optional[Sequence["_Ec2TagSetDefinition"]]
    EcsService: Optional[Sequence["_EcsServiceDefinition"]]
    LoadBalancerInfo: Optional[Sequence["_LoadBalancerInfoDefinition"]]
    OnPremisesInstanceTagFilter: Optional[Sequence["_OnPremisesInstanceTagFilterDefinition"]]
    TriggerConfiguration: Optional[Sequence["_TriggerConfigurationDefinition"]]

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
            AppName=json_data.get("AppName"),
            Arn=json_data.get("Arn"),
            AutoscalingGroups=json_data.get("AutoscalingGroups"),
            ComputePlatform=json_data.get("ComputePlatform"),
            DeploymentConfigName=json_data.get("DeploymentConfigName"),
            DeploymentGroupId=json_data.get("DeploymentGroupId"),
            DeploymentGroupName=json_data.get("DeploymentGroupName"),
            Id=json_data.get("Id"),
            ServiceRoleArn=json_data.get("ServiceRoleArn"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            AlarmConfiguration=deserialize_list(json_data.get("AlarmConfiguration"), AlarmConfigurationDefinition),
            AutoRollbackConfiguration=deserialize_list(json_data.get("AutoRollbackConfiguration"), AutoRollbackConfigurationDefinition),
            BlueGreenDeploymentConfig=deserialize_list(json_data.get("BlueGreenDeploymentConfig"), BlueGreenDeploymentConfigDefinition),
            DeploymentStyle=deserialize_list(json_data.get("DeploymentStyle"), DeploymentStyleDefinition),
            Ec2TagFilter=deserialize_list(json_data.get("Ec2TagFilter"), Ec2TagFilterDefinition),
            Ec2TagSet=deserialize_list(json_data.get("Ec2TagSet"), Ec2TagSetDefinition),
            EcsService=deserialize_list(json_data.get("EcsService"), EcsServiceDefinition),
            LoadBalancerInfo=deserialize_list(json_data.get("LoadBalancerInfo"), LoadBalancerInfoDefinition),
            OnPremisesInstanceTagFilter=deserialize_list(json_data.get("OnPremisesInstanceTagFilter"), OnPremisesInstanceTagFilterDefinition),
            TriggerConfiguration=deserialize_list(json_data.get("TriggerConfiguration"), TriggerConfigurationDefinition),
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
class AlarmConfigurationDefinition(BaseModel):
    Alarms: Optional[Sequence[str]]
    Enabled: Optional[bool]
    IgnorePollAlarmFailure: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AlarmConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlarmConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Alarms=json_data.get("Alarms"),
            Enabled=json_data.get("Enabled"),
            IgnorePollAlarmFailure=json_data.get("IgnorePollAlarmFailure"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlarmConfigurationDefinition = AlarmConfigurationDefinition


@dataclass
class AutoRollbackConfigurationDefinition(BaseModel):
    Enabled: Optional[bool]
    Events: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoRollbackConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoRollbackConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Events=json_data.get("Events"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoRollbackConfigurationDefinition = AutoRollbackConfigurationDefinition


@dataclass
class BlueGreenDeploymentConfigDefinition(BaseModel):
    DeploymentReadyOption: Optional[Sequence["_DeploymentReadyOptionDefinition"]]
    GreenFleetProvisioningOption: Optional[Sequence["_GreenFleetProvisioningOptionDefinition"]]
    TerminateBlueInstancesOnDeploymentSuccess: Optional[Sequence["_TerminateBlueInstancesOnDeploymentSuccessDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BlueGreenDeploymentConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlueGreenDeploymentConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DeploymentReadyOption=deserialize_list(json_data.get("DeploymentReadyOption"), DeploymentReadyOptionDefinition),
            GreenFleetProvisioningOption=deserialize_list(json_data.get("GreenFleetProvisioningOption"), GreenFleetProvisioningOptionDefinition),
            TerminateBlueInstancesOnDeploymentSuccess=deserialize_list(json_data.get("TerminateBlueInstancesOnDeploymentSuccess"), TerminateBlueInstancesOnDeploymentSuccessDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlueGreenDeploymentConfigDefinition = BlueGreenDeploymentConfigDefinition


@dataclass
class DeploymentReadyOptionDefinition(BaseModel):
    ActionOnTimeout: Optional[str]
    WaitTimeInMinutes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentReadyOptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentReadyOptionDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionOnTimeout=json_data.get("ActionOnTimeout"),
            WaitTimeInMinutes=json_data.get("WaitTimeInMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentReadyOptionDefinition = DeploymentReadyOptionDefinition


@dataclass
class GreenFleetProvisioningOptionDefinition(BaseModel):
    Action: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GreenFleetProvisioningOptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GreenFleetProvisioningOptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GreenFleetProvisioningOptionDefinition = GreenFleetProvisioningOptionDefinition


@dataclass
class TerminateBlueInstancesOnDeploymentSuccessDefinition(BaseModel):
    Action: Optional[str]
    TerminationWaitTimeInMinutes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TerminateBlueInstancesOnDeploymentSuccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TerminateBlueInstancesOnDeploymentSuccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            TerminationWaitTimeInMinutes=json_data.get("TerminationWaitTimeInMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TerminateBlueInstancesOnDeploymentSuccessDefinition = TerminateBlueInstancesOnDeploymentSuccessDefinition


@dataclass
class DeploymentStyleDefinition(BaseModel):
    DeploymentOption: Optional[str]
    DeploymentType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentStyleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentStyleDefinition"]:
        if not json_data:
            return None
        return cls(
            DeploymentOption=json_data.get("DeploymentOption"),
            DeploymentType=json_data.get("DeploymentType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentStyleDefinition = DeploymentStyleDefinition


@dataclass
class Ec2TagFilterDefinition(BaseModel):
    Key: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ec2TagFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ec2TagFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ec2TagFilterDefinition = Ec2TagFilterDefinition


@dataclass
class Ec2TagSetDefinition(BaseModel):
    Ec2TagFilter: Optional[Sequence["_Ec2TagFilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Ec2TagSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ec2TagSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Ec2TagFilter=deserialize_list(json_data.get("Ec2TagFilter"), Ec2TagFilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ec2TagSetDefinition = Ec2TagSetDefinition


@dataclass
class EcsServiceDefinition(BaseModel):
    ClusterName: Optional[str]
    ServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EcsServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcsServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterName=json_data.get("ClusterName"),
            ServiceName=json_data.get("ServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcsServiceDefinition = EcsServiceDefinition


@dataclass
class LoadBalancerInfoDefinition(BaseModel):
    ElbInfo: Optional[Sequence["_ElbInfoDefinition"]]
    TargetGroupInfo: Optional[Sequence["_TargetGroupInfoDefinition"]]
    TargetGroupPairInfo: Optional[Sequence["_TargetGroupPairInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancerInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancerInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            ElbInfo=deserialize_list(json_data.get("ElbInfo"), ElbInfoDefinition),
            TargetGroupInfo=deserialize_list(json_data.get("TargetGroupInfo"), TargetGroupInfoDefinition),
            TargetGroupPairInfo=deserialize_list(json_data.get("TargetGroupPairInfo"), TargetGroupPairInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancerInfoDefinition = LoadBalancerInfoDefinition


@dataclass
class ElbInfoDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElbInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElbInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElbInfoDefinition = ElbInfoDefinition


@dataclass
class TargetGroupInfoDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetGroupInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetGroupInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetGroupInfoDefinition = TargetGroupInfoDefinition


@dataclass
class TargetGroupPairInfoDefinition(BaseModel):
    ProdTrafficRoute: Optional[Sequence["_ProdTrafficRouteDefinition"]]
    TargetGroup: Optional[Sequence["_TargetGroupDefinition"]]
    TestTrafficRoute: Optional[Sequence["_TestTrafficRouteDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetGroupPairInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetGroupPairInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            ProdTrafficRoute=deserialize_list(json_data.get("ProdTrafficRoute"), ProdTrafficRouteDefinition),
            TargetGroup=deserialize_list(json_data.get("TargetGroup"), TargetGroupDefinition),
            TestTrafficRoute=deserialize_list(json_data.get("TestTrafficRoute"), TestTrafficRouteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetGroupPairInfoDefinition = TargetGroupPairInfoDefinition


@dataclass
class ProdTrafficRouteDefinition(BaseModel):
    ListenerArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ProdTrafficRouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProdTrafficRouteDefinition"]:
        if not json_data:
            return None
        return cls(
            ListenerArns=json_data.get("ListenerArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProdTrafficRouteDefinition = ProdTrafficRouteDefinition


@dataclass
class TargetGroupDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetGroupDefinition = TargetGroupDefinition


@dataclass
class TestTrafficRouteDefinition(BaseModel):
    ListenerArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TestTrafficRouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TestTrafficRouteDefinition"]:
        if not json_data:
            return None
        return cls(
            ListenerArns=json_data.get("ListenerArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TestTrafficRouteDefinition = TestTrafficRouteDefinition


@dataclass
class OnPremisesInstanceTagFilterDefinition(BaseModel):
    Key: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnPremisesInstanceTagFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnPremisesInstanceTagFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnPremisesInstanceTagFilterDefinition = OnPremisesInstanceTagFilterDefinition


@dataclass
class TriggerConfigurationDefinition(BaseModel):
    TriggerEvents: Optional[Sequence[str]]
    TriggerName: Optional[str]
    TriggerTargetArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TriggerConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggerConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            TriggerEvents=json_data.get("TriggerEvents"),
            TriggerName=json_data.get("TriggerName"),
            TriggerTargetArn=json_data.get("TriggerTargetArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TriggerConfigurationDefinition = TriggerConfigurationDefinition


