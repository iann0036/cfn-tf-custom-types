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
    ContentLength: Optional[str]
    ContentMd5: Optional[str]
    ContentType: Optional[str]
    DeleteAllObjectVersions: Optional[bool]
    Id: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Namespace: Optional[str]
    Object: Optional[str]
    Source: Optional[str]
    State: Optional[str]
    StorageTier: Optional[str]
    VersionId: Optional[str]
    WorkRequestId: Optional[str]
    SourceUriDetails: Optional[Sequence["_SourceUriDetailsDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            ContentLength=json_data.get("ContentLength"),
            ContentMd5=json_data.get("ContentMd5"),
            ContentType=json_data.get("ContentType"),
            DeleteAllObjectVersions=json_data.get("DeleteAllObjectVersions"),
            Id=json_data.get("Id"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Namespace=json_data.get("Namespace"),
            Object=json_data.get("Object"),
            Source=json_data.get("Source"),
            State=json_data.get("State"),
            StorageTier=json_data.get("StorageTier"),
            VersionId=json_data.get("VersionId"),
            WorkRequestId=json_data.get("WorkRequestId"),
            SourceUriDetails=deserialize_list(json_data.get("SourceUriDetails"), SourceUriDetailsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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


@dataclass
class SourceUriDetailsDefinition(BaseModel):
    Bucket: Optional[str]
    DestinationObjectIfMatchEtag: Optional[str]
    DestinationObjectIfNoneMatchEtag: Optional[str]
    Namespace: Optional[str]
    Object: Optional[str]
    Region: Optional[str]
    SourceObjectIfMatchEtag: Optional[str]
    SourceVersionId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceUriDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceUriDetailsDefinition"]:
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
            SourceVersionId=json_data.get("SourceVersionId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceUriDetailsDefinition = SourceUriDetailsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


