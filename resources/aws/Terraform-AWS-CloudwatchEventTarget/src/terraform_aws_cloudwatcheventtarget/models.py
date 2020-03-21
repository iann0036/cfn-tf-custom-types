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
    Arn: Optional[str]
    Input: Optional[str]
    InputPath: Optional[str]
    RoleArn: Optional[str]
    Rule: Optional[str]
    TargetId: Optional[str]
    BatchTarget: Optional[Sequence["_BatchTarget"]]
    EcsTarget: Optional[Sequence["_EcsTarget"]]
    InputTransformer: Optional[Sequence["_InputTransformer"]]
    KinesisTarget: Optional[Sequence["_KinesisTarget"]]
    RunCommandTargets: Optional[Sequence["_RunCommandTargets"]]
    SqsTarget: Optional[Sequence["_SqsTarget"]]
    NetworkConfiguration: Optional[Sequence["_NetworkConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Input=json_data.get("Input"),
            InputPath=json_data.get("InputPath"),
            RoleArn=json_data.get("RoleArn"),
            Rule=json_data.get("Rule"),
            TargetId=json_data.get("TargetId"),
            BatchTarget=json_data.get("BatchTarget"),
            EcsTarget=json_data.get("EcsTarget"),
            InputTransformer=json_data.get("InputTransformer"),
            KinesisTarget=json_data.get("KinesisTarget"),
            RunCommandTargets=json_data.get("RunCommandTargets"),
            SqsTarget=json_data.get("SqsTarget"),
            NetworkConfiguration=json_data.get("NetworkConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BatchTarget:
    ArraySize: Optional[float]
    JobAttempts: Optional[float]
    JobDefinition: Optional[str]
    JobName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BatchTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BatchTarget"]:
        if not json_data:
            return None
        return cls(
            ArraySize=json_data.get("ArraySize"),
            JobAttempts=json_data.get("JobAttempts"),
            JobDefinition=json_data.get("JobDefinition"),
            JobName=json_data.get("JobName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BatchTarget = BatchTarget


@dataclass
class EcsTarget:
    Group: Optional[str]
    LaunchType: Optional[str]
    PlatformVersion: Optional[str]
    TaskCount: Optional[float]
    TaskDefinitionArn: Optional[str]
    NetworkConfiguration: Optional[Sequence["_NetworkConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_EcsTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcsTarget"]:
        if not json_data:
            return None
        return cls(
            Group=json_data.get("Group"),
            LaunchType=json_data.get("LaunchType"),
            PlatformVersion=json_data.get("PlatformVersion"),
            TaskCount=json_data.get("TaskCount"),
            TaskDefinitionArn=json_data.get("TaskDefinitionArn"),
            NetworkConfiguration=json_data.get("NetworkConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcsTarget = EcsTarget


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
class InputTransformer:
    InputPaths: Optional[Sequence["_InputPaths"]]
    InputTemplate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputTransformer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputTransformer"]:
        if not json_data:
            return None
        return cls(
            InputPaths=json_data.get("InputPaths"),
            InputTemplate=json_data.get("InputTemplate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputTransformer = InputTransformer


@dataclass
class InputPaths:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputPaths"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputPaths"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputPaths = InputPaths


@dataclass
class KinesisTarget:
    PartitionKeyPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisTarget"]:
        if not json_data:
            return None
        return cls(
            PartitionKeyPath=json_data.get("PartitionKeyPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisTarget = KinesisTarget


@dataclass
class RunCommandTargets:
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RunCommandTargets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunCommandTargets"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunCommandTargets = RunCommandTargets


@dataclass
class SqsTarget:
    MessageGroupId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SqsTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SqsTarget"]:
        if not json_data:
            return None
        return cls(
            MessageGroupId=json_data.get("MessageGroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SqsTarget = SqsTarget


