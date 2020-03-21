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
    AcceptRanges: Optional[str]
    Container: Optional[str]
    Content: Optional[str]
    ContentDisposition: Optional[str]
    ContentEncoding: Optional[str]
    ContentLength: Optional[float]
    ContentType: Optional[str]
    CopyFrom: Optional[str]
    DeleteAt: Optional[float]
    Etag: Optional[str]
    File: Optional[str]
    LastModified: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    ObjectManifest: Optional[str]
    Timestamp: Optional[str]
    TransactionId: Optional[str]
    TransferEncoding: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AcceptRanges=json_data.get("AcceptRanges"),
            Container=json_data.get("Container"),
            Content=json_data.get("Content"),
            ContentDisposition=json_data.get("ContentDisposition"),
            ContentEncoding=json_data.get("ContentEncoding"),
            ContentLength=json_data.get("ContentLength"),
            ContentType=json_data.get("ContentType"),
            CopyFrom=json_data.get("CopyFrom"),
            DeleteAt=json_data.get("DeleteAt"),
            Etag=json_data.get("Etag"),
            File=json_data.get("File"),
            LastModified=json_data.get("LastModified"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            ObjectManifest=json_data.get("ObjectManifest"),
            Timestamp=json_data.get("Timestamp"),
            TransactionId=json_data.get("TransactionId"),
            TransferEncoding=json_data.get("TransferEncoding"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Metadata:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


