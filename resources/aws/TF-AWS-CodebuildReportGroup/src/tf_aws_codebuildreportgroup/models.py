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
    Created: Optional[str]
    DeleteReports: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Type: Optional[str]
    ExportConfig: Optional[Sequence["_ExportConfigDefinition"]]

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
            Created=json_data.get("Created"),
            DeleteReports=json_data.get("DeleteReports"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Type=json_data.get("Type"),
            ExportConfig=deserialize_list(json_data.get("ExportConfig"), ExportConfigDefinition),
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
class ExportConfigDefinition(BaseModel):
    Type: Optional[str]
    S3Destination: Optional[Sequence["_S3DestinationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExportConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExportConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            S3Destination=deserialize_list(json_data.get("S3Destination"), S3DestinationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExportConfigDefinition = ExportConfigDefinition


@dataclass
class S3DestinationDefinition(BaseModel):
    Bucket: Optional[str]
    EncryptionDisabled: Optional[bool]
    EncryptionKey: Optional[str]
    Packaging: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3DestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3DestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            EncryptionDisabled=json_data.get("EncryptionDisabled"),
            EncryptionKey=json_data.get("EncryptionKey"),
            Packaging=json_data.get("Packaging"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3DestinationDefinition = S3DestinationDefinition


