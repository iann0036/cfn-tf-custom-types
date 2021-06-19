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
    CacheControl: Optional[str]
    Content: Optional[str]
    ContentDisposition: Optional[str]
    ContentEncoding: Optional[str]
    ContentLanguage: Optional[str]
    ContentType: Optional[str]
    Crc32c: Optional[str]
    DetectMd5hash: Optional[str]
    Id: Optional[str]
    KmsKeyName: Optional[str]
    Md5hash: Optional[str]
    MediaLink: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    OutputName: Optional[str]
    SelfLink: Optional[str]
    Source: Optional[str]
    StorageClass: Optional[str]

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
            CacheControl=json_data.get("CacheControl"),
            Content=json_data.get("Content"),
            ContentDisposition=json_data.get("ContentDisposition"),
            ContentEncoding=json_data.get("ContentEncoding"),
            ContentLanguage=json_data.get("ContentLanguage"),
            ContentType=json_data.get("ContentType"),
            Crc32c=json_data.get("Crc32c"),
            DetectMd5hash=json_data.get("DetectMd5hash"),
            Id=json_data.get("Id"),
            KmsKeyName=json_data.get("KmsKeyName"),
            Md5hash=json_data.get("Md5hash"),
            MediaLink=json_data.get("MediaLink"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            OutputName=json_data.get("OutputName"),
            SelfLink=json_data.get("SelfLink"),
            Source=json_data.get("Source"),
            StorageClass=json_data.get("StorageClass"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


