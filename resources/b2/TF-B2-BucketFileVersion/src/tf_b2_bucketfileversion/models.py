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
    Action: Optional[str]
    BucketId: Optional[str]
    ContentMd5: Optional[str]
    ContentSha1: Optional[str]
    ContentType: Optional[str]
    FileId: Optional[str]
    FileInfo: Optional[Sequence["_FileInfoDefinition"]]
    FileName: Optional[str]
    Id: Optional[str]
    Size: Optional[float]
    Source: Optional[str]
    UploadTimestamp: Optional[float]
    ServerSideEncryption: Optional[Sequence["_ServerSideEncryptionDefinition"]]

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
            Action=json_data.get("Action"),
            BucketId=json_data.get("BucketId"),
            ContentMd5=json_data.get("ContentMd5"),
            ContentSha1=json_data.get("ContentSha1"),
            ContentType=json_data.get("ContentType"),
            FileId=json_data.get("FileId"),
            FileInfo=deserialize_list(json_data.get("FileInfo"), FileInfoDefinition),
            FileName=json_data.get("FileName"),
            Id=json_data.get("Id"),
            Size=json_data.get("Size"),
            Source=json_data.get("Source"),
            UploadTimestamp=json_data.get("UploadTimestamp"),
            ServerSideEncryption=deserialize_list(json_data.get("ServerSideEncryption"), ServerSideEncryptionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FileInfoDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileInfoDefinition = FileInfoDefinition


@dataclass
class ServerSideEncryptionDefinition(BaseModel):
    Algorithm: Optional[str]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryptionDefinition = ServerSideEncryptionDefinition


