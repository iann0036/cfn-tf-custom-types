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
    Bucket: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]
    StorageClassAnalysis: Optional[Sequence["_StorageClassAnalysisDefinition"]]

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
            Bucket=json_data.get("Bucket"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
            StorageClassAnalysis=deserialize_list(json_data.get("StorageClassAnalysis"), StorageClassAnalysisDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FilterDefinition(BaseModel):
    Prefix: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


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
class StorageClassAnalysisDefinition(BaseModel):
    DataExport: Optional[Sequence["_DataExportDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StorageClassAnalysisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageClassAnalysisDefinition"]:
        if not json_data:
            return None
        return cls(
            DataExport=deserialize_list(json_data.get("DataExport"), DataExportDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageClassAnalysisDefinition = StorageClassAnalysisDefinition


@dataclass
class DataExportDefinition(BaseModel):
    OutputSchemaVersion: Optional[str]
    Destination: Optional[Sequence["_DestinationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DataExportDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataExportDefinition"]:
        if not json_data:
            return None
        return cls(
            OutputSchemaVersion=json_data.get("OutputSchemaVersion"),
            Destination=deserialize_list(json_data.get("Destination"), DestinationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataExportDefinition = DataExportDefinition


@dataclass
class DestinationDefinition(BaseModel):
    S3BucketDestination: Optional[Sequence["_S3BucketDestinationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            S3BucketDestination=deserialize_list(json_data.get("S3BucketDestination"), S3BucketDestinationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationDefinition = DestinationDefinition


@dataclass
class S3BucketDestinationDefinition(BaseModel):
    BucketAccountId: Optional[str]
    BucketArn: Optional[str]
    Format: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3BucketDestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3BucketDestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            BucketAccountId=json_data.get("BucketAccountId"),
            BucketArn=json_data.get("BucketArn"),
            Format=json_data.get("Format"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3BucketDestinationDefinition = S3BucketDestinationDefinition


