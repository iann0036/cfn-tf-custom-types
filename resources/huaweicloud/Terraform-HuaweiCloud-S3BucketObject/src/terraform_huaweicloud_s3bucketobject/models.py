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
    Acl: Optional[str]
    Bucket: Optional[str]
    CacheControl: Optional[str]
    Content: Optional[str]
    ContentDisposition: Optional[str]
    ContentEncoding: Optional[str]
    ContentLanguage: Optional[str]
    ContentType: Optional[str]
    Etag: Optional[str]
    Id: Optional[str]
    Key: Optional[str]
    ServerSideEncryption: Optional[str]
    Source: Optional[str]
    SseKmsKeyId: Optional[str]
    VersionId: Optional[str]
    WebsiteRedirect: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Acl=json_data.get("Acl"),
            Bucket=json_data.get("Bucket"),
            CacheControl=json_data.get("CacheControl"),
            Content=json_data.get("Content"),
            ContentDisposition=json_data.get("ContentDisposition"),
            ContentEncoding=json_data.get("ContentEncoding"),
            ContentLanguage=json_data.get("ContentLanguage"),
            ContentType=json_data.get("ContentType"),
            Etag=json_data.get("Etag"),
            Id=json_data.get("Id"),
            Key=json_data.get("Key"),
            ServerSideEncryption=json_data.get("ServerSideEncryption"),
            Source=json_data.get("Source"),
            SseKmsKeyId=json_data.get("SseKmsKeyId"),
            VersionId=json_data.get("VersionId"),
            WebsiteRedirect=json_data.get("WebsiteRedirect"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


