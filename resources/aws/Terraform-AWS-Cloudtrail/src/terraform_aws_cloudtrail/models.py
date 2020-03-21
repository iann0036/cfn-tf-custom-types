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
    CloudWatchLogsGroupArn: Optional[str]
    CloudWatchLogsRoleArn: Optional[str]
    EnableLogFileValidation: Optional[bool]
    EnableLogging: Optional[bool]
    HomeRegion: Optional[str]
    IncludeGlobalServiceEvents: Optional[bool]
    IsMultiRegionTrail: Optional[bool]
    IsOrganizationTrail: Optional[bool]
    KmsKeyId: Optional[str]
    Name: Optional[str]
    S3BucketName: Optional[str]
    S3KeyPrefix: Optional[str]
    SnsTopicName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    EventSelector: Optional[Sequence["_EventSelector"]]
    DataResource: Optional[Sequence["_DataResource"]]

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
            CloudWatchLogsGroupArn=json_data.get("CloudWatchLogsGroupArn"),
            CloudWatchLogsRoleArn=json_data.get("CloudWatchLogsRoleArn"),
            EnableLogFileValidation=json_data.get("EnableLogFileValidation"),
            EnableLogging=json_data.get("EnableLogging"),
            HomeRegion=json_data.get("HomeRegion"),
            IncludeGlobalServiceEvents=json_data.get("IncludeGlobalServiceEvents"),
            IsMultiRegionTrail=json_data.get("IsMultiRegionTrail"),
            IsOrganizationTrail=json_data.get("IsOrganizationTrail"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Name=json_data.get("Name"),
            S3BucketName=json_data.get("S3BucketName"),
            S3KeyPrefix=json_data.get("S3KeyPrefix"),
            SnsTopicName=json_data.get("SnsTopicName"),
            Tags=json_data.get("Tags"),
            EventSelector=json_data.get("EventSelector"),
            DataResource=json_data.get("DataResource"),
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
class EventSelector:
    IncludeManagementEvents: Optional[bool]
    ReadWriteType: Optional[str]
    DataResource: Optional[Sequence["_DataResource"]]

    @classmethod
    def _deserialize(
        cls: Type["_EventSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventSelector"]:
        if not json_data:
            return None
        return cls(
            IncludeManagementEvents=json_data.get("IncludeManagementEvents"),
            ReadWriteType=json_data.get("ReadWriteType"),
            DataResource=json_data.get("DataResource"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventSelector = EventSelector


@dataclass
class DataResource:
    Type: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DataResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataResource"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataResource = DataResource


