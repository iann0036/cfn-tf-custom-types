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
    LoggingInfo: Optional[Sequence["_LoggingInfo"]]
    Targets: Optional[Sequence["_Targets"]]
    TaskInvocationParameters: Optional[Sequence["_TaskInvocationParameters"]]
    TaskParameters: Optional[Sequence["_TaskParameters"]]
    AutomationParameters: Optional[Sequence["_AutomationParameters"]]
    LambdaParameters: Optional[Sequence["_LambdaParameters"]]
    RunCommandParameters: Optional[Sequence["_RunCommandParameters"]]
    StepFunctionsParameters: Optional[Sequence["_StepFunctionsParameters"]]
    Parameter: Optional[Sequence["_Parameter"]]
    NotificationConfig: Optional[Sequence["_NotificationConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            LoggingInfo=json_data.get("LoggingInfo"),
            Targets=json_data.get("Targets"),
            TaskInvocationParameters=json_data.get("TaskInvocationParameters"),
            TaskParameters=json_data.get("TaskParameters"),
            AutomationParameters=json_data.get("AutomationParameters"),
            LambdaParameters=json_data.get("LambdaParameters"),
            RunCommandParameters=json_data.get("RunCommandParameters"),
            StepFunctionsParameters=json_data.get("StepFunctionsParameters"),
            Parameter=json_data.get("Parameter"),
            NotificationConfig=json_data.get("NotificationConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LoggingInfo:
    S3BucketName: Optional[str]
    S3BucketPrefix: Optional[str]
    S3Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingInfo"]:
        if not json_data:
            return None
        return cls(
            S3BucketName=json_data.get("S3BucketName"),
            S3BucketPrefix=json_data.get("S3BucketPrefix"),
            S3Region=json_data.get("S3Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingInfo = LoggingInfo


@dataclass
class Targets:
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Targets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Targets"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Targets = Targets


@dataclass
class TaskInvocationParameters:
    AutomationParameters: Optional[Sequence["_AutomationParameters"]]
    LambdaParameters: Optional[Sequence["_LambdaParameters"]]
    RunCommandParameters: Optional[Sequence["_RunCommandParameters"]]
    StepFunctionsParameters: Optional[Sequence["_StepFunctionsParameters"]]

    @classmethod
    def _deserialize(
        cls: Type["_TaskInvocationParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskInvocationParameters"]:
        if not json_data:
            return None
        return cls(
            AutomationParameters=json_data.get("AutomationParameters"),
            LambdaParameters=json_data.get("LambdaParameters"),
            RunCommandParameters=json_data.get("RunCommandParameters"),
            StepFunctionsParameters=json_data.get("StepFunctionsParameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskInvocationParameters = TaskInvocationParameters


@dataclass
class AutomationParameters:
    DocumentVersion: Optional[str]
    Parameter: Optional[Sequence["_Parameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutomationParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutomationParameters"]:
        if not json_data:
            return None
        return cls(
            DocumentVersion=json_data.get("DocumentVersion"),
            Parameter=json_data.get("Parameter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutomationParameters = AutomationParameters


@dataclass
class Parameter:
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Parameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameter"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameter = Parameter


@dataclass
class LambdaParameters:
    ClientContext: Optional[str]
    Payload: Optional[str]
    Qualifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaParameters"]:
        if not json_data:
            return None
        return cls(
            ClientContext=json_data.get("ClientContext"),
            Payload=json_data.get("Payload"),
            Qualifier=json_data.get("Qualifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaParameters = LambdaParameters


@dataclass
class RunCommandParameters:
    Comment: Optional[str]
    DocumentHash: Optional[str]
    DocumentHashType: Optional[str]
    OutputS3Bucket: Optional[str]
    OutputS3KeyPrefix: Optional[str]
    ServiceRoleArn: Optional[str]
    TimeoutSeconds: Optional[float]
    NotificationConfig: Optional[Sequence["_NotificationConfig"]]
    Parameter: Optional[Sequence["_Parameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_RunCommandParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunCommandParameters"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            DocumentHash=json_data.get("DocumentHash"),
            DocumentHashType=json_data.get("DocumentHashType"),
            OutputS3Bucket=json_data.get("OutputS3Bucket"),
            OutputS3KeyPrefix=json_data.get("OutputS3KeyPrefix"),
            ServiceRoleArn=json_data.get("ServiceRoleArn"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            NotificationConfig=json_data.get("NotificationConfig"),
            Parameter=json_data.get("Parameter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunCommandParameters = RunCommandParameters


@dataclass
class NotificationConfig:
    NotificationArn: Optional[str]
    NotificationEvents: Optional[Sequence[str]]
    NotificationType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationConfig"]:
        if not json_data:
            return None
        return cls(
            NotificationArn=json_data.get("NotificationArn"),
            NotificationEvents=json_data.get("NotificationEvents"),
            NotificationType=json_data.get("NotificationType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationConfig = NotificationConfig


@dataclass
class StepFunctionsParameters:
    Input: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StepFunctionsParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepFunctionsParameters"]:
        if not json_data:
            return None
        return cls(
            Input=json_data.get("Input"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepFunctionsParameters = StepFunctionsParameters


@dataclass
class TaskParameters:
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TaskParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskParameters"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskParameters = TaskParameters


