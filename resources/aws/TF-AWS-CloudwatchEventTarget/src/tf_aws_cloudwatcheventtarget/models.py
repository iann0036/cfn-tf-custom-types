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
    Arn: Optional[str]
    EventBusName: Optional[str]
    Id: Optional[str]
    Input: Optional[str]
    InputPath: Optional[str]
    RoleArn: Optional[str]
    Rule: Optional[str]
    TargetId: Optional[str]
    BatchTarget: Optional[Sequence["_BatchTargetDefinition"]]
    DeadLetterConfig: Optional[Sequence["_DeadLetterConfigDefinition"]]
    EcsTarget: Optional[Sequence["_EcsTargetDefinition"]]
    HttpTarget: Optional[Sequence["_HttpTargetDefinition"]]
    InputTransformer: Optional[Sequence["_InputTransformerDefinition"]]
    KinesisTarget: Optional[Sequence["_KinesisTargetDefinition"]]
    RetryPolicy: Optional[Sequence["_RetryPolicyDefinition"]]
    RunCommandTargets: Optional[Sequence["_RunCommandTargetsDefinition"]]
    SqsTarget: Optional[Sequence["_SqsTargetDefinition"]]

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
            Arn=json_data.get("Arn"),
            EventBusName=json_data.get("EventBusName"),
            Id=json_data.get("Id"),
            Input=json_data.get("Input"),
            InputPath=json_data.get("InputPath"),
            RoleArn=json_data.get("RoleArn"),
            Rule=json_data.get("Rule"),
            TargetId=json_data.get("TargetId"),
            BatchTarget=deserialize_list(json_data.get("BatchTarget"), BatchTargetDefinition),
            DeadLetterConfig=deserialize_list(json_data.get("DeadLetterConfig"), DeadLetterConfigDefinition),
            EcsTarget=deserialize_list(json_data.get("EcsTarget"), EcsTargetDefinition),
            HttpTarget=deserialize_list(json_data.get("HttpTarget"), HttpTargetDefinition),
            InputTransformer=deserialize_list(json_data.get("InputTransformer"), InputTransformerDefinition),
            KinesisTarget=deserialize_list(json_data.get("KinesisTarget"), KinesisTargetDefinition),
            RetryPolicy=deserialize_list(json_data.get("RetryPolicy"), RetryPolicyDefinition),
            RunCommandTargets=deserialize_list(json_data.get("RunCommandTargets"), RunCommandTargetsDefinition),
            SqsTarget=deserialize_list(json_data.get("SqsTarget"), SqsTargetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BatchTargetDefinition(BaseModel):
    ArraySize: Optional[float]
    JobAttempts: Optional[float]
    JobDefinition: Optional[str]
    JobName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BatchTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BatchTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            ArraySize=json_data.get("ArraySize"),
            JobAttempts=json_data.get("JobAttempts"),
            JobDefinition=json_data.get("JobDefinition"),
            JobName=json_data.get("JobName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BatchTargetDefinition = BatchTargetDefinition


@dataclass
class DeadLetterConfigDefinition(BaseModel):
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeadLetterConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeadLetterConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeadLetterConfigDefinition = DeadLetterConfigDefinition


@dataclass
class EcsTargetDefinition(BaseModel):
    Group: Optional[str]
    LaunchType: Optional[str]
    PlatformVersion: Optional[str]
    TaskCount: Optional[float]
    TaskDefinitionArn: Optional[str]
    NetworkConfiguration: Optional[Sequence["_NetworkConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EcsTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcsTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            Group=json_data.get("Group"),
            LaunchType=json_data.get("LaunchType"),
            PlatformVersion=json_data.get("PlatformVersion"),
            TaskCount=json_data.get("TaskCount"),
            TaskDefinitionArn=json_data.get("TaskDefinitionArn"),
            NetworkConfiguration=deserialize_list(json_data.get("NetworkConfiguration"), NetworkConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcsTargetDefinition = EcsTargetDefinition


@dataclass
class NetworkConfigurationDefinition(BaseModel):
    AssignPublicIp: Optional[bool]
    SecurityGroups: Optional[Sequence[str]]
    Subnets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AssignPublicIp=json_data.get("AssignPublicIp"),
            SecurityGroups=json_data.get("SecurityGroups"),
            Subnets=json_data.get("Subnets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfigurationDefinition = NetworkConfigurationDefinition


@dataclass
class HttpTargetDefinition(BaseModel):
    HeaderParameters: Optional[Sequence["_HeaderParametersDefinition"]]
    PathParameterValues: Optional[Sequence[str]]
    QueryStringParameters: Optional[Sequence["_QueryStringParametersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            HeaderParameters=deserialize_list(json_data.get("HeaderParameters"), HeaderParametersDefinition),
            PathParameterValues=json_data.get("PathParameterValues"),
            QueryStringParameters=deserialize_list(json_data.get("QueryStringParameters"), QueryStringParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpTargetDefinition = HttpTargetDefinition


@dataclass
class HeaderParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderParametersDefinition = HeaderParametersDefinition


@dataclass
class QueryStringParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueryStringParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryStringParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryStringParametersDefinition = QueryStringParametersDefinition


@dataclass
class InputTransformerDefinition(BaseModel):
    InputPaths: Optional[Sequence["_InputPathsDefinition"]]
    InputTemplate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputTransformerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputTransformerDefinition"]:
        if not json_data:
            return None
        return cls(
            InputPaths=deserialize_list(json_data.get("InputPaths"), InputPathsDefinition),
            InputTemplate=json_data.get("InputTemplate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputTransformerDefinition = InputTransformerDefinition


@dataclass
class InputPathsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputPathsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputPathsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputPathsDefinition = InputPathsDefinition


@dataclass
class KinesisTargetDefinition(BaseModel):
    PartitionKeyPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            PartitionKeyPath=json_data.get("PartitionKeyPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisTargetDefinition = KinesisTargetDefinition


@dataclass
class RetryPolicyDefinition(BaseModel):
    MaximumEventAgeInSeconds: Optional[float]
    MaximumRetryAttempts: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RetryPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            MaximumEventAgeInSeconds=json_data.get("MaximumEventAgeInSeconds"),
            MaximumRetryAttempts=json_data.get("MaximumRetryAttempts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryPolicyDefinition = RetryPolicyDefinition


@dataclass
class RunCommandTargetsDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RunCommandTargetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunCommandTargetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunCommandTargetsDefinition = RunCommandTargetsDefinition


@dataclass
class SqsTargetDefinition(BaseModel):
    MessageGroupId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SqsTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SqsTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            MessageGroupId=json_data.get("MessageGroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SqsTargetDefinition = SqsTargetDefinition


