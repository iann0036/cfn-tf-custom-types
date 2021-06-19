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
    CloudWatchLogsGroupArn: Optional[str]
    CloudWatchLogsRoleArn: Optional[str]
    EnableLogFileValidation: Optional[bool]
    EnableLogging: Optional[bool]
    HomeRegion: Optional[str]
    Id: Optional[str]
    IncludeGlobalServiceEvents: Optional[bool]
    IsMultiRegionTrail: Optional[bool]
    IsOrganizationTrail: Optional[bool]
    KmsKeyId: Optional[str]
    Name: Optional[str]
    S3BucketName: Optional[str]
    S3KeyPrefix: Optional[str]
    SnsTopicName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    EventSelector: Optional[Sequence["_EventSelectorDefinition"]]
    InsightSelector: Optional[Sequence["_InsightSelectorDefinition"]]

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
            CloudWatchLogsGroupArn=json_data.get("CloudWatchLogsGroupArn"),
            CloudWatchLogsRoleArn=json_data.get("CloudWatchLogsRoleArn"),
            EnableLogFileValidation=json_data.get("EnableLogFileValidation"),
            EnableLogging=json_data.get("EnableLogging"),
            HomeRegion=json_data.get("HomeRegion"),
            Id=json_data.get("Id"),
            IncludeGlobalServiceEvents=json_data.get("IncludeGlobalServiceEvents"),
            IsMultiRegionTrail=json_data.get("IsMultiRegionTrail"),
            IsOrganizationTrail=json_data.get("IsOrganizationTrail"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Name=json_data.get("Name"),
            S3BucketName=json_data.get("S3BucketName"),
            S3KeyPrefix=json_data.get("S3KeyPrefix"),
            SnsTopicName=json_data.get("SnsTopicName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            EventSelector=deserialize_list(json_data.get("EventSelector"), EventSelectorDefinition),
            InsightSelector=deserialize_list(json_data.get("InsightSelector"), InsightSelectorDefinition),
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
class EventSelectorDefinition(BaseModel):
    IncludeManagementEvents: Optional[bool]
    ReadWriteType: Optional[str]
    DataResource: Optional[Sequence["_DataResourceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EventSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            IncludeManagementEvents=json_data.get("IncludeManagementEvents"),
            ReadWriteType=json_data.get("ReadWriteType"),
            DataResource=deserialize_list(json_data.get("DataResource"), DataResourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventSelectorDefinition = EventSelectorDefinition


@dataclass
class DataResourceDefinition(BaseModel):
    Type: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DataResourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataResourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataResourceDefinition = DataResourceDefinition


@dataclass
class InsightSelectorDefinition(BaseModel):
    InsightType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InsightSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InsightSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            InsightType=json_data.get("InsightType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InsightSelectorDefinition = InsightSelectorDefinition


