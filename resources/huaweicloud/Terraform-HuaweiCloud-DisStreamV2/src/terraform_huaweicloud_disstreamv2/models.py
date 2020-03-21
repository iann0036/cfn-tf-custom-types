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
    AutoScaleMaxPartitionCount: Optional[float]
    AutoScaleMinPartitionCount: Optional[float]
    CompressionFormat: Optional[str]
    Created: Optional[float]
    CsvDelimiter: Optional[str]
    DataSchema: Optional[str]
    DataType: Optional[str]
    PartitionCount: Optional[float]
    ReadablePartitionCount: Optional[float]
    RetentionPeriod: Optional[float]
    StreamName: Optional[str]
    StreamType: Optional[str]
    WritablePartitionCount: Optional[float]
    Tags: Optional[Sequence["_Tags"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AutoScaleMaxPartitionCount=json_data.get("AutoScaleMaxPartitionCount"),
            AutoScaleMinPartitionCount=json_data.get("AutoScaleMinPartitionCount"),
            CompressionFormat=json_data.get("CompressionFormat"),
            Created=json_data.get("Created"),
            CsvDelimiter=json_data.get("CsvDelimiter"),
            DataSchema=json_data.get("DataSchema"),
            DataType=json_data.get("DataType"),
            PartitionCount=json_data.get("PartitionCount"),
            ReadablePartitionCount=json_data.get("ReadablePartitionCount"),
            RetentionPeriod=json_data.get("RetentionPeriod"),
            StreamName=json_data.get("StreamName"),
            StreamType=json_data.get("StreamType"),
            WritablePartitionCount=json_data.get("WritablePartitionCount"),
            Tags=json_data.get("Tags"),
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


