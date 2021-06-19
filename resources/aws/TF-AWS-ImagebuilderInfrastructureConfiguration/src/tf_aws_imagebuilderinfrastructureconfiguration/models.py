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
    DateCreated: Optional[str]
    DateUpdated: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    InstanceProfileName: Optional[str]
    InstanceTypes: Optional[Sequence[str]]
    KeyPair: Optional[str]
    Name: Optional[str]
    ResourceTags: Optional[Sequence["_ResourceTagsDefinition"]]
    SecurityGroupIds: Optional[Sequence[str]]
    SnsTopicArn: Optional[str]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    TerminateInstanceOnFailure: Optional[bool]
    Logging: Optional[Sequence["_LoggingDefinition"]]

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
            DateCreated=json_data.get("DateCreated"),
            DateUpdated=json_data.get("DateUpdated"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            InstanceProfileName=json_data.get("InstanceProfileName"),
            InstanceTypes=json_data.get("InstanceTypes"),
            KeyPair=json_data.get("KeyPair"),
            Name=json_data.get("Name"),
            ResourceTags=deserialize_list(json_data.get("ResourceTags"), ResourceTagsDefinition),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SnsTopicArn=json_data.get("SnsTopicArn"),
            SubnetId=json_data.get("SubnetId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            TerminateInstanceOnFailure=json_data.get("TerminateInstanceOnFailure"),
            Logging=deserialize_list(json_data.get("Logging"), LoggingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ResourceTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceTagsDefinition = ResourceTagsDefinition


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
class LoggingDefinition(BaseModel):
    S3Logs: Optional[Sequence["_S3LogsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingDefinition"]:
        if not json_data:
            return None
        return cls(
            S3Logs=deserialize_list(json_data.get("S3Logs"), S3LogsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingDefinition = LoggingDefinition


@dataclass
class S3LogsDefinition(BaseModel):
    S3BucketName: Optional[str]
    S3KeyPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3LogsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3LogsDefinition"]:
        if not json_data:
            return None
        return cls(
            S3BucketName=json_data.get("S3BucketName"),
            S3KeyPrefix=json_data.get("S3KeyPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3LogsDefinition = S3LogsDefinition


