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
    BucketDomainName: Optional[str]
    ForceDestroy: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
    Urn: Optional[str]
    CorsRule: Optional[Sequence["_CorsRuleDefinition"]]
    LifecycleRule: Optional[Sequence["_LifecycleRuleDefinition"]]
    Versioning: Optional[Sequence["_VersioningDefinition"]]

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
            BucketDomainName=json_data.get("BucketDomainName"),
            ForceDestroy=json_data.get("ForceDestroy"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            Urn=json_data.get("Urn"),
            CorsRule=deserialize_list(json_data.get("CorsRule"), CorsRuleDefinition),
            LifecycleRule=deserialize_list(json_data.get("LifecycleRule"), LifecycleRuleDefinition),
            Versioning=deserialize_list(json_data.get("Versioning"), VersioningDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CorsRuleDefinition(BaseModel):
    AllowedHeaders: Optional[Sequence[str]]
    AllowedMethods: Optional[Sequence[str]]
    AllowedOrigins: Optional[Sequence[str]]
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
            MaxAgeSeconds=json_data.get("MaxAgeSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsRuleDefinition = CorsRuleDefinition


@dataclass
class LifecycleRuleDefinition(BaseModel):
    AbortIncompleteMultipartUploadDays: Optional[float]
    Enabled: Optional[bool]
    Id: Optional[str]
    Prefix: Optional[str]
    Expiration: Optional[Sequence["_ExpirationDefinition"]]
    NoncurrentVersionExpiration: Optional[Sequence["_NoncurrentVersionExpirationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            AbortIncompleteMultipartUploadDays=json_data.get("AbortIncompleteMultipartUploadDays"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
            Expiration=deserialize_list(json_data.get("Expiration"), ExpirationDefinition),
            NoncurrentVersionExpiration=deserialize_list(json_data.get("NoncurrentVersionExpiration"), NoncurrentVersionExpirationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleRuleDefinition = LifecycleRuleDefinition


@dataclass
class ExpirationDefinition(BaseModel):
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
class VersioningDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_VersioningDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersioningDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersioningDefinition = VersioningDefinition


