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
    AppName: Optional[str]
    AutoscalingGroups: Optional[Sequence[str]]
    DeploymentConfigName: Optional[str]
    DeploymentGroupName: Optional[str]
    Id: Optional[str]
    ServiceRoleArn: Optional[str]
    AlarmConfiguration: Optional[Sequence["_AlarmConfiguration"]]
    AutoRollbackConfiguration: Optional[Sequence["_AutoRollbackConfiguration"]]
    BlueGreenDeploymentConfig: Optional[Sequence["_BlueGreenDeploymentConfig"]]
    DeploymentStyle: Optional[Sequence["_DeploymentStyle"]]
    Ec2TagFilter: Optional[Sequence["_Ec2TagFilter"]]
    Ec2TagSet: Optional[Sequence["_Ec2TagSet"]]
    EcsService: Optional[Sequence["_EcsService"]]
    LoadBalancerInfo: Optional[Sequence["_LoadBalancerInfo"]]
    OnPremisesInstanceTagFilter: Optional[Sequence["_OnPremisesInstanceTagFilter"]]
    TriggerConfiguration: Optional[Sequence["_TriggerConfiguration"]]
    DeploymentReadyOption: Optional[Sequence["_DeploymentReadyOption"]]
    GreenFleetProvisioningOption: Optional[Sequence["_GreenFleetProvisioningOption"]]
    TerminateBlueInstancesOnDeploymentSuccess: Optional[Sequence["_TerminateBlueInstancesOnDeploymentSuccess"]]
    ElbInfo: Optional[Sequence["_ElbInfo"]]
    TargetGroupInfo: Optional[Sequence["_TargetGroupInfo"]]
    TargetGroupPairInfo: Optional[Sequence["_TargetGroupPairInfo"]]
    ProdTrafficRoute: Optional[Sequence["_ProdTrafficRoute"]]
    TargetGroup: Optional[Sequence["_TargetGroup"]]
    TestTrafficRoute: Optional[Sequence["_TestTrafficRoute"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AppName=json_data.get("AppName"),
            AutoscalingGroups=json_data.get("AutoscalingGroups"),
            DeploymentConfigName=json_data.get("DeploymentConfigName"),
            DeploymentGroupName=json_data.get("DeploymentGroupName"),
            Id=json_data.get("Id"),
            ServiceRoleArn=json_data.get("ServiceRoleArn"),
            AlarmConfiguration=json_data.get("AlarmConfiguration"),
            AutoRollbackConfiguration=json_data.get("AutoRollbackConfiguration"),
            BlueGreenDeploymentConfig=json_data.get("BlueGreenDeploymentConfig"),
            DeploymentStyle=json_data.get("DeploymentStyle"),
            Ec2TagFilter=json_data.get("Ec2TagFilter"),
            Ec2TagSet=json_data.get("Ec2TagSet"),
            EcsService=json_data.get("EcsService"),
            LoadBalancerInfo=json_data.get("LoadBalancerInfo"),
            OnPremisesInstanceTagFilter=json_data.get("OnPremisesInstanceTagFilter"),
            TriggerConfiguration=json_data.get("TriggerConfiguration"),
            DeploymentReadyOption=json_data.get("DeploymentReadyOption"),
            GreenFleetProvisioningOption=json_data.get("GreenFleetProvisioningOption"),
            TerminateBlueInstancesOnDeploymentSuccess=json_data.get("TerminateBlueInstancesOnDeploymentSuccess"),
            ElbInfo=json_data.get("ElbInfo"),
            TargetGroupInfo=json_data.get("TargetGroupInfo"),
            TargetGroupPairInfo=json_data.get("TargetGroupPairInfo"),
            ProdTrafficRoute=json_data.get("ProdTrafficRoute"),
            TargetGroup=json_data.get("TargetGroup"),
            TestTrafficRoute=json_data.get("TestTrafficRoute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AlarmConfiguration:
    Alarms: Optional[Sequence[str]]
    Enabled: Optional[bool]
    IgnorePollAlarmFailure: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AlarmConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlarmConfiguration"]:
        if not json_data:
            return None
        return cls(
            Alarms=json_data.get("Alarms"),
            Enabled=json_data.get("Enabled"),
            IgnorePollAlarmFailure=json_data.get("IgnorePollAlarmFailure"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlarmConfiguration = AlarmConfiguration


@dataclass
class AutoRollbackConfiguration:
    Enabled: Optional[bool]
    Events: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoRollbackConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoRollbackConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Events=json_data.get("Events"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoRollbackConfiguration = AutoRollbackConfiguration


@dataclass
class BlueGreenDeploymentConfig:
    DeploymentReadyOption: Optional[Sequence["_DeploymentReadyOption"]]
    GreenFleetProvisioningOption: Optional[Sequence["_GreenFleetProvisioningOption"]]
    TerminateBlueInstancesOnDeploymentSuccess: Optional[Sequence["_TerminateBlueInstancesOnDeploymentSuccess"]]

    @classmethod
    def _deserialize(
        cls: Type["_BlueGreenDeploymentConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlueGreenDeploymentConfig"]:
        if not json_data:
            return None
        return cls(
            DeploymentReadyOption=json_data.get("DeploymentReadyOption"),
            GreenFleetProvisioningOption=json_data.get("GreenFleetProvisioningOption"),
            TerminateBlueInstancesOnDeploymentSuccess=json_data.get("TerminateBlueInstancesOnDeploymentSuccess"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlueGreenDeploymentConfig = BlueGreenDeploymentConfig


@dataclass
class DeploymentReadyOption:
    ActionOnTimeout: Optional[str]
    WaitTimeInMinutes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentReadyOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentReadyOption"]:
        if not json_data:
            return None
        return cls(
            ActionOnTimeout=json_data.get("ActionOnTimeout"),
            WaitTimeInMinutes=json_data.get("WaitTimeInMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentReadyOption = DeploymentReadyOption


@dataclass
class GreenFleetProvisioningOption:
    Action: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GreenFleetProvisioningOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GreenFleetProvisioningOption"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GreenFleetProvisioningOption = GreenFleetProvisioningOption


@dataclass
class TerminateBlueInstancesOnDeploymentSuccess:
    Action: Optional[str]
    TerminationWaitTimeInMinutes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TerminateBlueInstancesOnDeploymentSuccess"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TerminateBlueInstancesOnDeploymentSuccess"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            TerminationWaitTimeInMinutes=json_data.get("TerminationWaitTimeInMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TerminateBlueInstancesOnDeploymentSuccess = TerminateBlueInstancesOnDeploymentSuccess


@dataclass
class DeploymentStyle:
    DeploymentOption: Optional[str]
    DeploymentType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentStyle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentStyle"]:
        if not json_data:
            return None
        return cls(
            DeploymentOption=json_data.get("DeploymentOption"),
            DeploymentType=json_data.get("DeploymentType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentStyle = DeploymentStyle


@dataclass
class Ec2TagFilter:
    Key: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ec2TagFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ec2TagFilter"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ec2TagFilter = Ec2TagFilter


@dataclass
class Ec2TagSet:
    Ec2TagFilter: Optional[Sequence["_Ec2TagFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_Ec2TagSet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ec2TagSet"]:
        if not json_data:
            return None
        return cls(
            Ec2TagFilter=json_data.get("Ec2TagFilter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ec2TagSet = Ec2TagSet


@dataclass
class EcsService:
    ClusterName: Optional[str]
    ServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EcsService"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcsService"]:
        if not json_data:
            return None
        return cls(
            ClusterName=json_data.get("ClusterName"),
            ServiceName=json_data.get("ServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcsService = EcsService


@dataclass
class LoadBalancerInfo:
    ElbInfo: Optional[Sequence["_ElbInfo"]]
    TargetGroupInfo: Optional[Sequence["_TargetGroupInfo"]]
    TargetGroupPairInfo: Optional[Sequence["_TargetGroupPairInfo"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancerInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancerInfo"]:
        if not json_data:
            return None
        return cls(
            ElbInfo=json_data.get("ElbInfo"),
            TargetGroupInfo=json_data.get("TargetGroupInfo"),
            TargetGroupPairInfo=json_data.get("TargetGroupPairInfo"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancerInfo = LoadBalancerInfo


@dataclass
class ElbInfo:
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElbInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElbInfo"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElbInfo = ElbInfo


@dataclass
class TargetGroupInfo:
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetGroupInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetGroupInfo"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetGroupInfo = TargetGroupInfo


@dataclass
class TargetGroupPairInfo:
    ProdTrafficRoute: Optional[Sequence["_ProdTrafficRoute"]]
    TargetGroup: Optional[Sequence["_TargetGroup"]]
    TestTrafficRoute: Optional[Sequence["_TestTrafficRoute"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetGroupPairInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetGroupPairInfo"]:
        if not json_data:
            return None
        return cls(
            ProdTrafficRoute=json_data.get("ProdTrafficRoute"),
            TargetGroup=json_data.get("TargetGroup"),
            TestTrafficRoute=json_data.get("TestTrafficRoute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetGroupPairInfo = TargetGroupPairInfo


@dataclass
class ProdTrafficRoute:
    ListenerArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ProdTrafficRoute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProdTrafficRoute"]:
        if not json_data:
            return None
        return cls(
            ListenerArns=json_data.get("ListenerArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProdTrafficRoute = ProdTrafficRoute


@dataclass
class TargetGroup:
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetGroup"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetGroup = TargetGroup


@dataclass
class TestTrafficRoute:
    ListenerArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TestTrafficRoute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TestTrafficRoute"]:
        if not json_data:
            return None
        return cls(
            ListenerArns=json_data.get("ListenerArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TestTrafficRoute = TestTrafficRoute


@dataclass
class OnPremisesInstanceTagFilter:
    Key: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnPremisesInstanceTagFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnPremisesInstanceTagFilter"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnPremisesInstanceTagFilter = OnPremisesInstanceTagFilter


@dataclass
class TriggerConfiguration:
    TriggerEvents: Optional[Sequence[str]]
    TriggerName: Optional[str]
    TriggerTargetArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TriggerConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggerConfiguration"]:
        if not json_data:
            return None
        return cls(
            TriggerEvents=json_data.get("TriggerEvents"),
            TriggerName=json_data.get("TriggerName"),
            TriggerTargetArn=json_data.get("TriggerTargetArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TriggerConfiguration = TriggerConfiguration


