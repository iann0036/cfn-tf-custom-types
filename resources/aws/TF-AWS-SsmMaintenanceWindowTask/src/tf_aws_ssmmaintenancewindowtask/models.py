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
    Description: Optional[str]
    Id: Optional[str]
    MaxConcurrency: Optional[str]
    MaxErrors: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    ServiceRoleArn: Optional[str]
    TaskArn: Optional[str]
    TaskType: Optional[str]
    WindowId: Optional[str]
    Targets: Optional[Sequence["_TargetsDefinition"]]
    TaskInvocationParameters: Optional[Sequence["_TaskInvocationParametersDefinition"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            MaxConcurrency=json_data.get("MaxConcurrency"),
            MaxErrors=json_data.get("MaxErrors"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            ServiceRoleArn=json_data.get("ServiceRoleArn"),
            TaskArn=json_data.get("TaskArn"),
            TaskType=json_data.get("TaskType"),
            WindowId=json_data.get("WindowId"),
            Targets=deserialize_list(json_data.get("Targets"), TargetsDefinition),
            TaskInvocationParameters=deserialize_list(json_data.get("TaskInvocationParameters"), TaskInvocationParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TargetsDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetsDefinition = TargetsDefinition


@dataclass
class TaskInvocationParametersDefinition(BaseModel):
    AutomationParameters: Optional[Sequence["_AutomationParametersDefinition"]]
    LambdaParameters: Optional[Sequence["_LambdaParametersDefinition"]]
    RunCommandParameters: Optional[Sequence["_RunCommandParametersDefinition"]]
    StepFunctionsParameters: Optional[Sequence["_StepFunctionsParametersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TaskInvocationParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskInvocationParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            AutomationParameters=deserialize_list(json_data.get("AutomationParameters"), AutomationParametersDefinition),
            LambdaParameters=deserialize_list(json_data.get("LambdaParameters"), LambdaParametersDefinition),
            RunCommandParameters=deserialize_list(json_data.get("RunCommandParameters"), RunCommandParametersDefinition),
            StepFunctionsParameters=deserialize_list(json_data.get("StepFunctionsParameters"), StepFunctionsParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskInvocationParametersDefinition = TaskInvocationParametersDefinition


@dataclass
class AutomationParametersDefinition(BaseModel):
    DocumentVersion: Optional[str]
    Parameter: Optional[Sequence["_ParameterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutomationParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutomationParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            DocumentVersion=json_data.get("DocumentVersion"),
            Parameter=deserialize_list(json_data.get("Parameter"), ParameterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutomationParametersDefinition = AutomationParametersDefinition


@dataclass
class ParameterDefinition(BaseModel):
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterDefinition = ParameterDefinition


@dataclass
class LambdaParametersDefinition(BaseModel):
    ClientContext: Optional[str]
    Payload: Optional[str]
    Qualifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientContext=json_data.get("ClientContext"),
            Payload=json_data.get("Payload"),
            Qualifier=json_data.get("Qualifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaParametersDefinition = LambdaParametersDefinition


@dataclass
class RunCommandParametersDefinition(BaseModel):
    Comment: Optional[str]
    DocumentHash: Optional[str]
    DocumentHashType: Optional[str]
    DocumentVersion: Optional[str]
    OutputS3Bucket: Optional[str]
    OutputS3KeyPrefix: Optional[str]
    ServiceRoleArn: Optional[str]
    TimeoutSeconds: Optional[float]
    CloudwatchConfig: Optional[Sequence["_CloudwatchConfigDefinition"]]
    NotificationConfig: Optional[Sequence["_NotificationConfigDefinition"]]
    Parameter: Optional[Sequence["_ParameterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RunCommandParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunCommandParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            DocumentHash=json_data.get("DocumentHash"),
            DocumentHashType=json_data.get("DocumentHashType"),
            DocumentVersion=json_data.get("DocumentVersion"),
            OutputS3Bucket=json_data.get("OutputS3Bucket"),
            OutputS3KeyPrefix=json_data.get("OutputS3KeyPrefix"),
            ServiceRoleArn=json_data.get("ServiceRoleArn"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            CloudwatchConfig=deserialize_list(json_data.get("CloudwatchConfig"), CloudwatchConfigDefinition),
            NotificationConfig=deserialize_list(json_data.get("NotificationConfig"), NotificationConfigDefinition),
            Parameter=deserialize_list(json_data.get("Parameter"), ParameterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunCommandParametersDefinition = RunCommandParametersDefinition


@dataclass
class CloudwatchConfigDefinition(BaseModel):
    CloudwatchLogGroupName: Optional[str]
    CloudwatchOutputEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudwatchLogGroupName=json_data.get("CloudwatchLogGroupName"),
            CloudwatchOutputEnabled=json_data.get("CloudwatchOutputEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchConfigDefinition = CloudwatchConfigDefinition


@dataclass
class NotificationConfigDefinition(BaseModel):
    NotificationArn: Optional[str]
    NotificationEvents: Optional[Sequence[str]]
    NotificationType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            NotificationArn=json_data.get("NotificationArn"),
            NotificationEvents=json_data.get("NotificationEvents"),
            NotificationType=json_data.get("NotificationType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationConfigDefinition = NotificationConfigDefinition


@dataclass
class StepFunctionsParametersDefinition(BaseModel):
    Input: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StepFunctionsParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepFunctionsParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Input=json_data.get("Input"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepFunctionsParametersDefinition = StepFunctionsParametersDefinition


