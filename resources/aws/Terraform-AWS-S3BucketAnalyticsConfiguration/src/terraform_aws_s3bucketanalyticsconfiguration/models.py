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
    Bucket: Optional[str]
    Name: Optional[str]
    Filter: Optional[Sequence["_Filter"]]
    StorageClassAnalysis: Optional[Sequence["_StorageClassAnalysis"]]
    DataExport: Optional[Sequence["_DataExport"]]
    Destination: Optional[Sequence["_Destination"]]
    S3BucketDestination: Optional[Sequence["_S3BucketDestination"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Bucket=json_data.get("Bucket"),
            Name=json_data.get("Name"),
            Filter=json_data.get("Filter"),
            StorageClassAnalysis=json_data.get("StorageClassAnalysis"),
            DataExport=json_data.get("DataExport"),
            Destination=json_data.get("Destination"),
            S3BucketDestination=json_data.get("S3BucketDestination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Filter:
    Prefix: Optional[str]
    Tags: Optional[Sequence["_Tags"]]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


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
class StorageClassAnalysis:
    DataExport: Optional[Sequence["_DataExport"]]

    @classmethod
    def _deserialize(
        cls: Type["_StorageClassAnalysis"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageClassAnalysis"]:
        if not json_data:
            return None
        return cls(
            DataExport=json_data.get("DataExport"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageClassAnalysis = StorageClassAnalysis


@dataclass
class DataExport:
    OutputSchemaVersion: Optional[str]
    Destination: Optional[Sequence["_Destination"]]

    @classmethod
    def _deserialize(
        cls: Type["_DataExport"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataExport"]:
        if not json_data:
            return None
        return cls(
            OutputSchemaVersion=json_data.get("OutputSchemaVersion"),
            Destination=json_data.get("Destination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataExport = DataExport


@dataclass
class Destination:
    S3BucketDestination: Optional[Sequence["_S3BucketDestination"]]

    @classmethod
    def _deserialize(
        cls: Type["_Destination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Destination"]:
        if not json_data:
            return None
        return cls(
            S3BucketDestination=json_data.get("S3BucketDestination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Destination = Destination


@dataclass
class S3BucketDestination:
    BucketAccountId: Optional[str]
    BucketArn: Optional[str]
    Format: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3BucketDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3BucketDestination"]:
        if not json_data:
            return None
        return cls(
            BucketAccountId=json_data.get("BucketAccountId"),
            BucketArn=json_data.get("BucketArn"),
            Format=json_data.get("Format"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3BucketDestination = S3BucketDestination


