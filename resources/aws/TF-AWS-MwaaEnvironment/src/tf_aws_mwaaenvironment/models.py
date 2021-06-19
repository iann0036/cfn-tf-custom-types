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
    AirflowConfigurationOptions: Optional[Sequence["_AirflowConfigurationOptionsDefinition"]]
    AirflowVersion: Optional[str]
    Arn: Optional[str]
    CreatedAt: Optional[str]
    DagS3Path: Optional[str]
    EnvironmentClass: Optional[str]
    ExecutionRoleArn: Optional[str]
    Id: Optional[str]
    KmsKey: Optional[str]
    LastUpdated: Optional[Sequence["_LastUpdatedDefinition2"]]
    MaxWorkers: Optional[float]
    MinWorkers: Optional[float]
    Name: Optional[str]
    PluginsS3ObjectVersion: Optional[str]
    PluginsS3Path: Optional[str]
    RequirementsS3ObjectVersion: Optional[str]
    RequirementsS3Path: Optional[str]
    ServiceRoleArn: Optional[str]
    SourceBucketArn: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    WebserverAccessMode: Optional[str]
    WebserverUrl: Optional[str]
    WeeklyMaintenanceWindowStart: Optional[str]
    LoggingConfiguration: Optional[Sequence["_LoggingConfigurationDefinition"]]
    NetworkConfiguration: Optional[Sequence["_NetworkConfigurationDefinition"]]

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
            AirflowConfigurationOptions=deserialize_list(json_data.get("AirflowConfigurationOptions"), AirflowConfigurationOptionsDefinition),
            AirflowVersion=json_data.get("AirflowVersion"),
            Arn=json_data.get("Arn"),
            CreatedAt=json_data.get("CreatedAt"),
            DagS3Path=json_data.get("DagS3Path"),
            EnvironmentClass=json_data.get("EnvironmentClass"),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            Id=json_data.get("Id"),
            KmsKey=json_data.get("KmsKey"),
            LastUpdated=deserialize_list(json_data.get("LastUpdated"), LastUpdatedDefinition2),
            MaxWorkers=json_data.get("MaxWorkers"),
            MinWorkers=json_data.get("MinWorkers"),
            Name=json_data.get("Name"),
            PluginsS3ObjectVersion=json_data.get("PluginsS3ObjectVersion"),
            PluginsS3Path=json_data.get("PluginsS3Path"),
            RequirementsS3ObjectVersion=json_data.get("RequirementsS3ObjectVersion"),
            RequirementsS3Path=json_data.get("RequirementsS3Path"),
            ServiceRoleArn=json_data.get("ServiceRoleArn"),
            SourceBucketArn=json_data.get("SourceBucketArn"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            WebserverAccessMode=json_data.get("WebserverAccessMode"),
            WebserverUrl=json_data.get("WebserverUrl"),
            WeeklyMaintenanceWindowStart=json_data.get("WeeklyMaintenanceWindowStart"),
            LoggingConfiguration=deserialize_list(json_data.get("LoggingConfiguration"), LoggingConfigurationDefinition),
            NetworkConfiguration=deserialize_list(json_data.get("NetworkConfiguration"), NetworkConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AirflowConfigurationOptionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AirflowConfigurationOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AirflowConfigurationOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AirflowConfigurationOptionsDefinition = AirflowConfigurationOptionsDefinition


@dataclass
class LastUpdatedDefinition2(BaseModel):
    CreatedAt: Optional[str]
    Error: Optional[Sequence["_LastUpdatedDefinition"]]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LastUpdatedDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LastUpdatedDefinition2"]:
        if not json_data:
            return None
        return cls(
            CreatedAt=json_data.get("CreatedAt"),
            Error=deserialize_list(json_data.get("Error"), LastUpdatedDefinition),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LastUpdatedDefinition2 = LastUpdatedDefinition2


@dataclass
class LastUpdatedDefinition(BaseModel):
    ErrorCode: Optional[str]
    ErrorMessage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LastUpdatedDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LastUpdatedDefinition"]:
        if not json_data:
            return None
        return cls(
            ErrorCode=json_data.get("ErrorCode"),
            ErrorMessage=json_data.get("ErrorMessage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LastUpdatedDefinition = LastUpdatedDefinition


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
class LoggingConfigurationDefinition(BaseModel):
    DagProcessingLogs: Optional[Sequence["_DagProcessingLogsDefinition"]]
    SchedulerLogs: Optional[Sequence["_SchedulerLogsDefinition"]]
    TaskLogs: Optional[Sequence["_TaskLogsDefinition"]]
    WebserverLogs: Optional[Sequence["_WebserverLogsDefinition"]]
    WorkerLogs: Optional[Sequence["_WorkerLogsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            DagProcessingLogs=deserialize_list(json_data.get("DagProcessingLogs"), DagProcessingLogsDefinition),
            SchedulerLogs=deserialize_list(json_data.get("SchedulerLogs"), SchedulerLogsDefinition),
            TaskLogs=deserialize_list(json_data.get("TaskLogs"), TaskLogsDefinition),
            WebserverLogs=deserialize_list(json_data.get("WebserverLogs"), WebserverLogsDefinition),
            WorkerLogs=deserialize_list(json_data.get("WorkerLogs"), WorkerLogsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingConfigurationDefinition = LoggingConfigurationDefinition


@dataclass
class DagProcessingLogsDefinition(BaseModel):
    Enabled: Optional[bool]
    LogLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DagProcessingLogsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DagProcessingLogsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            LogLevel=json_data.get("LogLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DagProcessingLogsDefinition = DagProcessingLogsDefinition


@dataclass
class SchedulerLogsDefinition(BaseModel):
    Enabled: Optional[bool]
    LogLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchedulerLogsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchedulerLogsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            LogLevel=json_data.get("LogLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchedulerLogsDefinition = SchedulerLogsDefinition


@dataclass
class TaskLogsDefinition(BaseModel):
    Enabled: Optional[bool]
    LogLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaskLogsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskLogsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            LogLevel=json_data.get("LogLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskLogsDefinition = TaskLogsDefinition


@dataclass
class WebserverLogsDefinition(BaseModel):
    Enabled: Optional[bool]
    LogLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebserverLogsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebserverLogsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            LogLevel=json_data.get("LogLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebserverLogsDefinition = WebserverLogsDefinition


@dataclass
class WorkerLogsDefinition(BaseModel):
    Enabled: Optional[bool]
    LogLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerLogsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerLogsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            LogLevel=json_data.get("LogLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerLogsDefinition = WorkerLogsDefinition


@dataclass
class NetworkConfigurationDefinition(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfigurationDefinition = NetworkConfigurationDefinition


