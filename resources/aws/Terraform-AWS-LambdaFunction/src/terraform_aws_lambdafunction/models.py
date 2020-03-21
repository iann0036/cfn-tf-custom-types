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
    Description: Optional[str]
    Filename: Optional[str]
    FunctionName: Optional[str]
    Handler: Optional[str]
    InvokeArn: Optional[str]
    KmsKeyArn: Optional[str]
    LastModified: Optional[str]
    Layers: Optional[Sequence[str]]
    MemorySize: Optional[float]
    Publish: Optional[bool]
    QualifiedArn: Optional[str]
    ReservedConcurrentExecutions: Optional[float]
    Role: Optional[str]
    Runtime: Optional[str]
    S3Bucket: Optional[str]
    S3Key: Optional[str]
    S3ObjectVersion: Optional[str]
    SourceCodeHash: Optional[str]
    SourceCodeSize: Optional[float]
    Tags: Optional[Sequence["_Tags"]]
    Timeout: Optional[float]
    Version: Optional[str]
    DeadLetterConfig: Optional[Sequence["_DeadLetterConfig"]]
    Environment: Optional[Sequence["_Environment"]]
    Timeouts: Optional["_Timeouts"]
    TracingConfig: Optional[Sequence["_TracingConfig"]]
    VpcConfig: Optional[Sequence["_VpcConfig"]]

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
            Description=json_data.get("Description"),
            Filename=json_data.get("Filename"),
            FunctionName=json_data.get("FunctionName"),
            Handler=json_data.get("Handler"),
            InvokeArn=json_data.get("InvokeArn"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            LastModified=json_data.get("LastModified"),
            Layers=json_data.get("Layers"),
            MemorySize=json_data.get("MemorySize"),
            Publish=json_data.get("Publish"),
            QualifiedArn=json_data.get("QualifiedArn"),
            ReservedConcurrentExecutions=json_data.get("ReservedConcurrentExecutions"),
            Role=json_data.get("Role"),
            Runtime=json_data.get("Runtime"),
            S3Bucket=json_data.get("S3Bucket"),
            S3Key=json_data.get("S3Key"),
            S3ObjectVersion=json_data.get("S3ObjectVersion"),
            SourceCodeHash=json_data.get("SourceCodeHash"),
            SourceCodeSize=json_data.get("SourceCodeSize"),
            Tags=json_data.get("Tags"),
            Timeout=json_data.get("Timeout"),
            Version=json_data.get("Version"),
            DeadLetterConfig=json_data.get("DeadLetterConfig"),
            Environment=json_data.get("Environment"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            TracingConfig=json_data.get("TracingConfig"),
            VpcConfig=json_data.get("VpcConfig"),
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
class DeadLetterConfig:
    TargetArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeadLetterConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeadLetterConfig"]:
        if not json_data:
            return None
        return cls(
            TargetArn=json_data.get("TargetArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeadLetterConfig = DeadLetterConfig


@dataclass
class Environment:
    Variables: Optional[Sequence["_Variables"]]

    @classmethod
    def _deserialize(
        cls: Type["_Environment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Environment"]:
        if not json_data:
            return None
        return cls(
            Variables=json_data.get("Variables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Environment = Environment


@dataclass
class Variables:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Variables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Variables"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Variables = Variables


@dataclass
class Timeouts:
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


@dataclass
class TracingConfig:
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TracingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TracingConfig"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TracingConfig = TracingConfig


@dataclass
class VpcConfig:
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfig"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfig = VpcConfig


