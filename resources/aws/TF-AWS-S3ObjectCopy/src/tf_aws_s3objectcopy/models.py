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
    Acl: Optional[str]
    Bucket: Optional[str]
    BucketKeyEnabled: Optional[bool]
    CacheControl: Optional[str]
    ContentDisposition: Optional[str]
    ContentEncoding: Optional[str]
    ContentLanguage: Optional[str]
    ContentType: Optional[str]
    CopyIfMatch: Optional[str]
    CopyIfModifiedSince: Optional[str]
    CopyIfNoneMatch: Optional[str]
    CopyIfUnmodifiedSince: Optional[str]
    CustomerAlgorithm: Optional[str]
    CustomerKey: Optional[str]
    CustomerKeyMd5: Optional[str]
    Etag: Optional[str]
    ExpectedBucketOwner: Optional[str]
    ExpectedSourceBucketOwner: Optional[str]
    Expiration: Optional[str]
    Expires: Optional[str]
    ForceDestroy: Optional[bool]
    Id: Optional[str]
    Key: Optional[str]
    KmsEncryptionContext: Optional[str]
    KmsKeyId: Optional[str]
    LastModified: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    MetadataDirective: Optional[str]
    ObjectLockLegalHoldStatus: Optional[str]
    ObjectLockMode: Optional[str]
    ObjectLockRetainUntilDate: Optional[str]
    RequestCharged: Optional[bool]
    RequestPayer: Optional[str]
    ServerSideEncryption: Optional[str]
    Source: Optional[str]
    SourceCustomerAlgorithm: Optional[str]
    SourceCustomerKey: Optional[str]
    SourceCustomerKeyMd5: Optional[str]
    SourceVersionId: Optional[str]
    StorageClass: Optional[str]
    TaggingDirective: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    VersionId: Optional[str]
    WebsiteRedirect: Optional[str]
    Grant: Optional[Sequence["_GrantDefinition"]]

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
            Acl=json_data.get("Acl"),
            Bucket=json_data.get("Bucket"),
            BucketKeyEnabled=json_data.get("BucketKeyEnabled"),
            CacheControl=json_data.get("CacheControl"),
            ContentDisposition=json_data.get("ContentDisposition"),
            ContentEncoding=json_data.get("ContentEncoding"),
            ContentLanguage=json_data.get("ContentLanguage"),
            ContentType=json_data.get("ContentType"),
            CopyIfMatch=json_data.get("CopyIfMatch"),
            CopyIfModifiedSince=json_data.get("CopyIfModifiedSince"),
            CopyIfNoneMatch=json_data.get("CopyIfNoneMatch"),
            CopyIfUnmodifiedSince=json_data.get("CopyIfUnmodifiedSince"),
            CustomerAlgorithm=json_data.get("CustomerAlgorithm"),
            CustomerKey=json_data.get("CustomerKey"),
            CustomerKeyMd5=json_data.get("CustomerKeyMd5"),
            Etag=json_data.get("Etag"),
            ExpectedBucketOwner=json_data.get("ExpectedBucketOwner"),
            ExpectedSourceBucketOwner=json_data.get("ExpectedSourceBucketOwner"),
            Expiration=json_data.get("Expiration"),
            Expires=json_data.get("Expires"),
            ForceDestroy=json_data.get("ForceDestroy"),
            Id=json_data.get("Id"),
            Key=json_data.get("Key"),
            KmsEncryptionContext=json_data.get("KmsEncryptionContext"),
            KmsKeyId=json_data.get("KmsKeyId"),
            LastModified=json_data.get("LastModified"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            MetadataDirective=json_data.get("MetadataDirective"),
            ObjectLockLegalHoldStatus=json_data.get("ObjectLockLegalHoldStatus"),
            ObjectLockMode=json_data.get("ObjectLockMode"),
            ObjectLockRetainUntilDate=json_data.get("ObjectLockRetainUntilDate"),
            RequestCharged=json_data.get("RequestCharged"),
            RequestPayer=json_data.get("RequestPayer"),
            ServerSideEncryption=json_data.get("ServerSideEncryption"),
            Source=json_data.get("Source"),
            SourceCustomerAlgorithm=json_data.get("SourceCustomerAlgorithm"),
            SourceCustomerKey=json_data.get("SourceCustomerKey"),
            SourceCustomerKeyMd5=json_data.get("SourceCustomerKeyMd5"),
            SourceVersionId=json_data.get("SourceVersionId"),
            StorageClass=json_data.get("StorageClass"),
            TaggingDirective=json_data.get("TaggingDirective"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            VersionId=json_data.get("VersionId"),
            WebsiteRedirect=json_data.get("WebsiteRedirect"),
            Grant=deserialize_list(json_data.get("Grant"), GrantDefinition),
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
class GrantDefinition(BaseModel):
    Email: Optional[str]
    Id: Optional[str]
    Permissions: Optional[Sequence[str]]
    Type: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GrantDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrantDefinition"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            Id=json_data.get("Id"),
            Permissions=json_data.get("Permissions"),
            Type=json_data.get("Type"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrantDefinition = GrantDefinition


