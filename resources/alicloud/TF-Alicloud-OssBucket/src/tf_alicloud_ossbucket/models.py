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
    CreationDate: Optional[str]
    ExtranetEndpoint: Optional[str]
    ForceDestroy: Optional[bool]
    Id: Optional[str]
    IntranetEndpoint: Optional[str]
    Location: Optional[str]
    LoggingIsenable: Optional[bool]
    Owner: Optional[str]
    Policy: Optional[str]
    RedundancyType: Optional[str]
    StorageClass: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    CorsRule: Optional[Sequence["_CorsRuleDefinition"]]
    LifecycleRule: Optional[Sequence["_LifecycleRuleDefinition"]]
    Logging: Optional[Sequence["_LoggingDefinition"]]
    RefererConfig: Optional[Sequence["_RefererConfigDefinition"]]
    ServerSideEncryptionRule: Optional[Sequence["_ServerSideEncryptionRuleDefinition"]]
    TransferAcceleration: Optional[Sequence["_TransferAccelerationDefinition"]]
    Versioning: Optional[Sequence["_VersioningDefinition"]]
    Website: Optional[Sequence["_WebsiteDefinition"]]

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
            CreationDate=json_data.get("CreationDate"),
            ExtranetEndpoint=json_data.get("ExtranetEndpoint"),
            ForceDestroy=json_data.get("ForceDestroy"),
            Id=json_data.get("Id"),
            IntranetEndpoint=json_data.get("IntranetEndpoint"),
            Location=json_data.get("Location"),
            LoggingIsenable=json_data.get("LoggingIsenable"),
            Owner=json_data.get("Owner"),
            Policy=json_data.get("Policy"),
            RedundancyType=json_data.get("RedundancyType"),
            StorageClass=json_data.get("StorageClass"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            CorsRule=deserialize_list(json_data.get("CorsRule"), CorsRuleDefinition),
            LifecycleRule=deserialize_list(json_data.get("LifecycleRule"), LifecycleRuleDefinition),
            Logging=deserialize_list(json_data.get("Logging"), LoggingDefinition),
            RefererConfig=deserialize_list(json_data.get("RefererConfig"), RefererConfigDefinition),
            ServerSideEncryptionRule=deserialize_list(json_data.get("ServerSideEncryptionRule"), ServerSideEncryptionRuleDefinition),
            TransferAcceleration=deserialize_list(json_data.get("TransferAcceleration"), TransferAccelerationDefinition),
            Versioning=deserialize_list(json_data.get("Versioning"), VersioningDefinition),
            Website=deserialize_list(json_data.get("Website"), WebsiteDefinition),
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
class CorsRuleDefinition(BaseModel):
    AllowedHeaders: Optional[Sequence[str]]
    AllowedMethods: Optional[Sequence[str]]
    AllowedOrigins: Optional[Sequence[str]]
    ExposeHeaders: Optional[Sequence[str]]
    MaxAgeSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CorsRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedHeaders=json_data.get("AllowedHeaders"),
            AllowedMethods=json_data.get("AllowedMethods"),
            AllowedOrigins=json_data.get("AllowedOrigins"),
            ExposeHeaders=json_data.get("ExposeHeaders"),
            MaxAgeSeconds=json_data.get("MaxAgeSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsRuleDefinition = CorsRuleDefinition


@dataclass
class LifecycleRuleDefinition(BaseModel):
    Enabled: Optional[bool]
    Id: Optional[str]
    Prefix: Optional[str]
    AbortMultipartUpload: Optional[Sequence["_AbortMultipartUploadDefinition"]]
    Expiration: Optional[Sequence["_ExpirationDefinition"]]
    NoncurrentVersionExpiration: Optional[Sequence["_NoncurrentVersionExpirationDefinition"]]
    NoncurrentVersionTransition: Optional[Sequence["_NoncurrentVersionTransitionDefinition"]]
    Transitions: Optional[Sequence["_TransitionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
            AbortMultipartUpload=deserialize_list(json_data.get("AbortMultipartUpload"), AbortMultipartUploadDefinition),
            Expiration=deserialize_list(json_data.get("Expiration"), ExpirationDefinition),
            NoncurrentVersionExpiration=deserialize_list(json_data.get("NoncurrentVersionExpiration"), NoncurrentVersionExpirationDefinition),
            NoncurrentVersionTransition=deserialize_list(json_data.get("NoncurrentVersionTransition"), NoncurrentVersionTransitionDefinition),
            Transitions=deserialize_list(json_data.get("Transitions"), TransitionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleRuleDefinition = LifecycleRuleDefinition


@dataclass
class AbortMultipartUploadDefinition(BaseModel):
    CreatedBeforeDate: Optional[str]
    Days: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AbortMultipartUploadDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AbortMultipartUploadDefinition"]:
        if not json_data:
            return None
        return cls(
            CreatedBeforeDate=json_data.get("CreatedBeforeDate"),
            Days=json_data.get("Days"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AbortMultipartUploadDefinition = AbortMultipartUploadDefinition


@dataclass
class ExpirationDefinition(BaseModel):
    CreatedBeforeDate: Optional[str]
    Date: Optional[str]
    Days: Optional[float]
    ExpiredObjectDeleteMarker: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ExpirationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExpirationDefinition"]:
        if not json_data:
            return None
        return cls(
            CreatedBeforeDate=json_data.get("CreatedBeforeDate"),
            Date=json_data.get("Date"),
            Days=json_data.get("Days"),
            ExpiredObjectDeleteMarker=json_data.get("ExpiredObjectDeleteMarker"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExpirationDefinition = ExpirationDefinition


@dataclass
class NoncurrentVersionExpirationDefinition(BaseModel):
    Days: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NoncurrentVersionExpirationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NoncurrentVersionExpirationDefinition"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NoncurrentVersionExpirationDefinition = NoncurrentVersionExpirationDefinition


@dataclass
class NoncurrentVersionTransitionDefinition(BaseModel):
    Days: Optional[float]
    StorageClass: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NoncurrentVersionTransitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NoncurrentVersionTransitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
            StorageClass=json_data.get("StorageClass"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NoncurrentVersionTransitionDefinition = NoncurrentVersionTransitionDefinition


@dataclass
class TransitionsDefinition(BaseModel):
    CreatedBeforeDate: Optional[str]
    Days: Optional[float]
    StorageClass: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TransitionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransitionsDefinition"]:
        if not json_data:
            return None
        return cls(
            CreatedBeforeDate=json_data.get("CreatedBeforeDate"),
            Days=json_data.get("Days"),
            StorageClass=json_data.get("StorageClass"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransitionsDefinition = TransitionsDefinition


@dataclass
class LoggingDefinition(BaseModel):
    TargetBucket: Optional[str]
    TargetPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetBucket=json_data.get("TargetBucket"),
            TargetPrefix=json_data.get("TargetPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingDefinition = LoggingDefinition


@dataclass
class RefererConfigDefinition(BaseModel):
    AllowEmpty: Optional[bool]
    Referers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RefererConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RefererConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowEmpty=json_data.get("AllowEmpty"),
            Referers=json_data.get("Referers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RefererConfigDefinition = RefererConfigDefinition


@dataclass
class ServerSideEncryptionRuleDefinition(BaseModel):
    KmsMasterKeyId: Optional[str]
    SseAlgorithm: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryptionRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryptionRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsMasterKeyId=json_data.get("KmsMasterKeyId"),
            SseAlgorithm=json_data.get("SseAlgorithm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryptionRuleDefinition = ServerSideEncryptionRuleDefinition


@dataclass
class TransferAccelerationDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TransferAccelerationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransferAccelerationDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransferAccelerationDefinition = TransferAccelerationDefinition


@dataclass
class VersioningDefinition(BaseModel):
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersioningDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersioningDefinition"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersioningDefinition = VersioningDefinition


@dataclass
class WebsiteDefinition(BaseModel):
    ErrorDocument: Optional[str]
    IndexDocument: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebsiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebsiteDefinition"]:
        if not json_data:
            return None
        return cls(
            ErrorDocument=json_data.get("ErrorDocument"),
            IndexDocument=json_data.get("IndexDocument"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebsiteDefinition = WebsiteDefinition


