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
    ArtifactS3Location: Optional[str]
    EngineArn: Optional[str]
    ExecutionRoleArn: Optional[str]
    FailureRetentionPeriod: Optional[float]
    Handler: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    RuntimeVersion: Optional[str]
    S3Bucket: Optional[str]
    S3Key: Optional[str]
    S3Version: Optional[str]
    SourceLocationArn: Optional[str]
    StartCanary: Optional[bool]
    Status: Optional[str]
    SuccessRetentionPeriod: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Timeline: Optional[Sequence["_TimelineDefinition"]]
    ZipFile: Optional[str]
    RunConfig: Optional[Sequence["_RunConfigDefinition"]]
    Schedule: Optional[Sequence["_ScheduleDefinition"]]
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
            ArtifactS3Location=json_data.get("ArtifactS3Location"),
            EngineArn=json_data.get("EngineArn"),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            FailureRetentionPeriod=json_data.get("FailureRetentionPeriod"),
            Handler=json_data.get("Handler"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RuntimeVersion=json_data.get("RuntimeVersion"),
            S3Bucket=json_data.get("S3Bucket"),
            S3Key=json_data.get("S3Key"),
            S3Version=json_data.get("S3Version"),
            SourceLocationArn=json_data.get("SourceLocationArn"),
            StartCanary=json_data.get("StartCanary"),
            Status=json_data.get("Status"),
            SuccessRetentionPeriod=json_data.get("SuccessRetentionPeriod"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Timeline=deserialize_list(json_data.get("Timeline"), TimelineDefinition),
            ZipFile=json_data.get("ZipFile"),
            RunConfig=deserialize_list(json_data.get("RunConfig"), RunConfigDefinition),
            Schedule=deserialize_list(json_data.get("Schedule"), ScheduleDefinition),
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
class TimelineDefinition(BaseModel):
    Created: Optional[str]
    LastModified: Optional[str]
    LastStarted: Optional[str]
    LastStopped: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimelineDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimelineDefinition"]:
        if not json_data:
            return None
        return cls(
            Created=json_data.get("Created"),
            LastModified=json_data.get("LastModified"),
            LastStarted=json_data.get("LastStarted"),
            LastStopped=json_data.get("LastStopped"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimelineDefinition = TimelineDefinition


@dataclass
class RunConfigDefinition(BaseModel):
    ActiveTracing: Optional[bool]
    MemoryInMb: Optional[float]
    TimeoutInSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RunConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ActiveTracing=json_data.get("ActiveTracing"),
            MemoryInMb=json_data.get("MemoryInMb"),
            TimeoutInSeconds=json_data.get("TimeoutInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunConfigDefinition = RunConfigDefinition


@dataclass
class ScheduleDefinition(BaseModel):
    DurationInSeconds: Optional[float]
    Expression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            DurationInSeconds=json_data.get("DurationInSeconds"),
            Expression=json_data.get("Expression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleDefinition = ScheduleDefinition


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


