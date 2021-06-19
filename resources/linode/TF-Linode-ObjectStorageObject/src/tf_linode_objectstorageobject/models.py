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
    AccessKey: Optional[str]
    Acl: Optional[str]
    Bucket: Optional[str]
    CacheControl: Optional[str]
    Cluster: Optional[str]
    Content: Optional[str]
    ContentBase64: Optional[str]
    ContentDisposition: Optional[str]
    ContentEncoding: Optional[str]
    ContentLanguage: Optional[str]
    ContentType: Optional[str]
    Etag: Optional[str]
    ForceDestroy: Optional[bool]
    Id: Optional[str]
    Key: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    SecretKey: Optional[str]
    Source: Optional[str]
    VersionId: Optional[str]
    WebsiteRedirect: Optional[str]

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
            AccessKey=json_data.get("AccessKey"),
            Acl=json_data.get("Acl"),
            Bucket=json_data.get("Bucket"),
            CacheControl=json_data.get("CacheControl"),
            Cluster=json_data.get("Cluster"),
            Content=json_data.get("Content"),
            ContentBase64=json_data.get("ContentBase64"),
            ContentDisposition=json_data.get("ContentDisposition"),
            ContentEncoding=json_data.get("ContentEncoding"),
            ContentLanguage=json_data.get("ContentLanguage"),
            ContentType=json_data.get("ContentType"),
            Etag=json_data.get("Etag"),
            ForceDestroy=json_data.get("ForceDestroy"),
            Id=json_data.get("Id"),
            Key=json_data.get("Key"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            SecretKey=json_data.get("SecretKey"),
            Source=json_data.get("Source"),
            VersionId=json_data.get("VersionId"),
            WebsiteRedirect=json_data.get("WebsiteRedirect"),
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


