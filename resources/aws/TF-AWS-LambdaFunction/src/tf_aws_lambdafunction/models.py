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
    CodeSigningConfigArn: Optional[str]
    Description: Optional[str]
    Filename: Optional[str]
    FunctionName: Optional[str]
    Handler: Optional[str]
    Id: Optional[str]
    ImageUri: Optional[str]
    InvokeArn: Optional[str]
    KmsKeyArn: Optional[str]
    LastModified: Optional[str]
    Layers: Optional[Sequence[str]]
    MemorySize: Optional[float]
    PackageType: Optional[str]
    Publish: Optional[bool]
    QualifiedArn: Optional[str]
    ReservedConcurrentExecutions: Optional[float]
    Role: Optional[str]
    Runtime: Optional[str]
    S3Bucket: Optional[str]
    S3Key: Optional[str]
    S3ObjectVersion: Optional[str]
    SigningJobArn: Optional[str]
    SigningProfileVersionArn: Optional[str]
    SourceCodeHash: Optional[str]
    SourceCodeSize: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Timeout: Optional[float]
    Version: Optional[str]
    DeadLetterConfig: Optional[Sequence["_DeadLetterConfigDefinition"]]
    Environment: Optional[Sequence["_EnvironmentDefinition"]]
    FileSystemConfig: Optional[Sequence["_FileSystemConfigDefinition"]]
    ImageConfig: Optional[Sequence["_ImageConfigDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    TracingConfig: Optional[Sequence["_TracingConfigDefinition"]]
    VpcConfig: Optional[Sequence["_VpcConfigDefinition"]]

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
            CodeSigningConfigArn=json_data.get("CodeSigningConfigArn"),
            Description=json_data.get("Description"),
            Filename=json_data.get("Filename"),
            FunctionName=json_data.get("FunctionName"),
            Handler=json_data.get("Handler"),
            Id=json_data.get("Id"),
            ImageUri=json_data.get("ImageUri"),
            InvokeArn=json_data.get("InvokeArn"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            LastModified=json_data.get("LastModified"),
            Layers=json_data.get("Layers"),
            MemorySize=json_data.get("MemorySize"),
            PackageType=json_data.get("PackageType"),
            Publish=json_data.get("Publish"),
            QualifiedArn=json_data.get("QualifiedArn"),
            ReservedConcurrentExecutions=json_data.get("ReservedConcurrentExecutions"),
            Role=json_data.get("Role"),
            Runtime=json_data.get("Runtime"),
            S3Bucket=json_data.get("S3Bucket"),
            S3Key=json_data.get("S3Key"),
            S3ObjectVersion=json_data.get("S3ObjectVersion"),
            SigningJobArn=json_data.get("SigningJobArn"),
            SigningProfileVersionArn=json_data.get("SigningProfileVersionArn"),
            SourceCodeHash=json_data.get("SourceCodeHash"),
            SourceCodeSize=json_data.get("SourceCodeSize"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Timeout=json_data.get("Timeout"),
            Version=json_data.get("Version"),
            DeadLetterConfig=deserialize_list(json_data.get("DeadLetterConfig"), DeadLetterConfigDefinition),
            Environment=deserialize_list(json_data.get("Environment"), EnvironmentDefinition),
            FileSystemConfig=deserialize_list(json_data.get("FileSystemConfig"), FileSystemConfigDefinition),
            ImageConfig=deserialize_list(json_data.get("ImageConfig"), ImageConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            TracingConfig=deserialize_list(json_data.get("TracingConfig"), TracingConfigDefinition),
            VpcConfig=deserialize_list(json_data.get("VpcConfig"), VpcConfigDefinition),
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
class DeadLetterConfigDefinition(BaseModel):
    TargetArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeadLetterConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeadLetterConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetArn=json_data.get("TargetArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeadLetterConfigDefinition = DeadLetterConfigDefinition


@dataclass
class EnvironmentDefinition(BaseModel):
    Variables: Optional[Sequence["_VariablesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentDefinition"]:
        if not json_data:
            return None
        return cls(
            Variables=deserialize_list(json_data.get("Variables"), VariablesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentDefinition = EnvironmentDefinition


@dataclass
class VariablesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VariablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VariablesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VariablesDefinition = VariablesDefinition


@dataclass
class FileSystemConfigDefinition(BaseModel):
    Arn: Optional[str]
    LocalMountPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileSystemConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileSystemConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            LocalMountPath=json_data.get("LocalMountPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileSystemConfigDefinition = FileSystemConfigDefinition


@dataclass
class ImageConfigDefinition(BaseModel):
    Command: Optional[Sequence[str]]
    EntryPoint: Optional[Sequence[str]]
    WorkingDirectory: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImageConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Command=json_data.get("Command"),
            EntryPoint=json_data.get("EntryPoint"),
            WorkingDirectory=json_data.get("WorkingDirectory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageConfigDefinition = ImageConfigDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class TracingConfigDefinition(BaseModel):
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TracingConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TracingConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TracingConfigDefinition = TracingConfigDefinition


@dataclass
class VpcConfigDefinition(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfigDefinition = VpcConfigDefinition


