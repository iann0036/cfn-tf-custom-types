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
    CacheControl: Optional[str]
    Content: Optional[str]
    ContentDisposition: Optional[str]
    ContentEncoding: Optional[str]
    ContentLanguage: Optional[str]
    ContentLength: Optional[str]
    ContentMd5: Optional[str]
    ContentType: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    Namespace: Optional[str]
    Object: Optional[str]
    Source: Optional[str]
    State: Optional[str]
    WorkRequestId: Optional[str]
    SourceUriDetails: Optional[Sequence["_SourceUriDetails"]]
    Timeouts: Optional["_Timeouts"]

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
            CacheControl=json_data.get("CacheControl"),
            Content=json_data.get("Content"),
            ContentDisposition=json_data.get("ContentDisposition"),
            ContentEncoding=json_data.get("ContentEncoding"),
            ContentLanguage=json_data.get("ContentLanguage"),
            ContentLength=json_data.get("ContentLength"),
            ContentMd5=json_data.get("ContentMd5"),
            ContentType=json_data.get("ContentType"),
            Metadata=json_data.get("Metadata"),
            Namespace=json_data.get("Namespace"),
            Object=json_data.get("Object"),
            Source=json_data.get("Source"),
            State=json_data.get("State"),
            WorkRequestId=json_data.get("WorkRequestId"),
            SourceUriDetails=json_data.get("SourceUriDetails"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
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


@dataclass
class SourceUriDetails:
    Bucket: Optional[str]
    DestinationObjectIfMatchEtag: Optional[str]
    DestinationObjectIfNoneMatchEtag: Optional[str]
    Namespace: Optional[str]
    Object: Optional[str]
    Region: Optional[str]
    SourceObjectIfMatchEtag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceUriDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceUriDetails"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            DestinationObjectIfMatchEtag=json_data.get("DestinationObjectIfMatchEtag"),
            DestinationObjectIfNoneMatchEtag=json_data.get("DestinationObjectIfNoneMatchEtag"),
            Namespace=json_data.get("Namespace"),
            Object=json_data.get("Object"),
            Region=json_data.get("Region"),
            SourceObjectIfMatchEtag=json_data.get("SourceObjectIfMatchEtag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceUriDetails = SourceUriDetails


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


