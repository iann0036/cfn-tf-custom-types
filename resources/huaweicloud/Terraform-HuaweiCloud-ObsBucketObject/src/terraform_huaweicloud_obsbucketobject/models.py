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
    Content: Optional[str]
    ContentType: Optional[str]
    Encryption: Optional[bool]
    Etag: Optional[str]
    Id: Optional[str]
    Key: Optional[str]
    KmsKeyId: Optional[str]
    Size: Optional[float]
    Source: Optional[str]
    StorageClass: Optional[str]
    VersionId: Optional[str]

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
            Content=json_data.get("Content"),
            ContentType=json_data.get("ContentType"),
            Encryption=json_data.get("Encryption"),
            Etag=json_data.get("Etag"),
            Id=json_data.get("Id"),
            Key=json_data.get("Key"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Size=json_data.get("Size"),
            Source=json_data.get("Source"),
            StorageClass=json_data.get("StorageClass"),
            VersionId=json_data.get("VersionId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


