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
    CleanupPolicy: Optional[str]
    Id: Optional[str]
    MinimumInSyncReplicas: Optional[float]
    Partitions: Optional[float]
    Project: Optional[str]
    Replication: Optional[float]
    RetentionBytes: Optional[float]
    RetentionHours: Optional[float]
    ServiceName: Optional[str]
    TerminationProtection: Optional[bool]
    TopicName: Optional[str]
    Config: Optional[Sequence["_ConfigDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            CleanupPolicy=json_data.get("CleanupPolicy"),
            Id=json_data.get("Id"),
            MinimumInSyncReplicas=json_data.get("MinimumInSyncReplicas"),
            Partitions=json_data.get("Partitions"),
            Project=json_data.get("Project"),
            Replication=json_data.get("Replication"),
            RetentionBytes=json_data.get("RetentionBytes"),
            RetentionHours=json_data.get("RetentionHours"),
            ServiceName=json_data.get("ServiceName"),
            TerminationProtection=json_data.get("TerminationProtection"),
            TopicName=json_data.get("TopicName"),
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConfigDefinition(BaseModel):
    CleanupPolicy: Optional[str]
    CompressionType: Optional[str]
    DeleteRetentionMs: Optional[str]
    FileDeleteDelayMs: Optional[str]
    FlushMessages: Optional[str]
    FlushMs: Optional[str]
    IndexIntervalBytes: Optional[str]
    MaxCompactionLagMs: Optional[str]
    MaxMessageBytes: Optional[str]
    MessageDownconversionEnable: Optional[str]
    MessageFormatVersion: Optional[str]
    MessageTimestampDifferenceMaxMs: Optional[str]
    MessageTimestampType: Optional[str]
    MinCleanableDirtyRatio: Optional[str]
    MinCompactionLagMs: Optional[str]
    MinInsyncReplicas: Optional[str]
    Preallocate: Optional[str]
    RetentionBytes: Optional[str]
    RetentionMs: Optional[str]
    SegmentBytes: Optional[str]
    SegmentIndexBytes: Optional[str]
    SegmentJitterMs: Optional[str]
    SegmentMs: Optional[str]
    UncleanLeaderElectionEnable: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CleanupPolicy=json_data.get("CleanupPolicy"),
            CompressionType=json_data.get("CompressionType"),
            DeleteRetentionMs=json_data.get("DeleteRetentionMs"),
            FileDeleteDelayMs=json_data.get("FileDeleteDelayMs"),
            FlushMessages=json_data.get("FlushMessages"),
            FlushMs=json_data.get("FlushMs"),
            IndexIntervalBytes=json_data.get("IndexIntervalBytes"),
            MaxCompactionLagMs=json_data.get("MaxCompactionLagMs"),
            MaxMessageBytes=json_data.get("MaxMessageBytes"),
            MessageDownconversionEnable=json_data.get("MessageDownconversionEnable"),
            MessageFormatVersion=json_data.get("MessageFormatVersion"),
            MessageTimestampDifferenceMaxMs=json_data.get("MessageTimestampDifferenceMaxMs"),
            MessageTimestampType=json_data.get("MessageTimestampType"),
            MinCleanableDirtyRatio=json_data.get("MinCleanableDirtyRatio"),
            MinCompactionLagMs=json_data.get("MinCompactionLagMs"),
            MinInsyncReplicas=json_data.get("MinInsyncReplicas"),
            Preallocate=json_data.get("Preallocate"),
            RetentionBytes=json_data.get("RetentionBytes"),
            RetentionMs=json_data.get("RetentionMs"),
            SegmentBytes=json_data.get("SegmentBytes"),
            SegmentIndexBytes=json_data.get("SegmentIndexBytes"),
            SegmentJitterMs=json_data.get("SegmentJitterMs"),
            SegmentMs=json_data.get("SegmentMs"),
            UncleanLeaderElectionEnable=json_data.get("UncleanLeaderElectionEnable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


@dataclass
class TagDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


