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
    Arn: Optional[str]
    Bucket: Optional[str]
    BucketDomainName: Optional[str]
    BucketPrefix: Optional[str]
    ForceDestroy: Optional[bool]
    HostedZoneId: Optional[str]
    Id: Optional[str]
    Policy: Optional[str]
    Region: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    WebsiteDomain: Optional[str]
    WebsiteEndpoint: Optional[str]
    CorsRule: Optional[Sequence["_CorsRule"]]
    LifecycleRule: Optional[Sequence["_LifecycleRule"]]
    Logging: Optional[Sequence["_Logging"]]
    Versioning: Optional[Sequence["_Versioning"]]
    Website: Optional[Sequence["_Website"]]
    Expiration: Optional[Sequence["_Expiration"]]
    NoncurrentVersionExpiration: Optional[Sequence["_NoncurrentVersionExpiration"]]

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
            Arn=json_data.get("Arn"),
            Bucket=json_data.get("Bucket"),
            BucketDomainName=json_data.get("BucketDomainName"),
            BucketPrefix=json_data.get("BucketPrefix"),
            ForceDestroy=json_data.get("ForceDestroy"),
            HostedZoneId=json_data.get("HostedZoneId"),
            Id=json_data.get("Id"),
            Policy=json_data.get("Policy"),
            Region=json_data.get("Region"),
            Tags=json_data.get("Tags"),
            WebsiteDomain=json_data.get("WebsiteDomain"),
            WebsiteEndpoint=json_data.get("WebsiteEndpoint"),
            CorsRule=json_data.get("CorsRule"),
            LifecycleRule=json_data.get("LifecycleRule"),
            Logging=json_data.get("Logging"),
            Versioning=json_data.get("Versioning"),
            Website=json_data.get("Website"),
            Expiration=json_data.get("Expiration"),
            NoncurrentVersionExpiration=json_data.get("NoncurrentVersionExpiration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class CorsRule:
    AllowedHeaders: Optional[Sequence[str]]
    AllowedMethods: Optional[Sequence[str]]
    AllowedOrigins: Optional[Sequence[str]]
    ExposeHeaders: Optional[Sequence[str]]
    MaxAgeSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CorsRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsRule"]:
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
_CorsRule = CorsRule


@dataclass
class LifecycleRule:
    AbortIncompleteMultipartUploadDays: Optional[float]
    Enabled: Optional[bool]
    Id: Optional[str]
    Prefix: Optional[str]
    Expiration: Optional[Sequence["_Expiration"]]
    NoncurrentVersionExpiration: Optional[Sequence["_NoncurrentVersionExpiration"]]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleRule"]:
        if not json_data:
            return None
        return cls(
            AbortIncompleteMultipartUploadDays=json_data.get("AbortIncompleteMultipartUploadDays"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
            Expiration=json_data.get("Expiration"),
            NoncurrentVersionExpiration=json_data.get("NoncurrentVersionExpiration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleRule = LifecycleRule


@dataclass
class Expiration:
    Date: Optional[str]
    Days: Optional[float]
    ExpiredObjectDeleteMarker: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Expiration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Expiration"]:
        if not json_data:
            return None
        return cls(
            Date=json_data.get("Date"),
            Days=json_data.get("Days"),
            ExpiredObjectDeleteMarker=json_data.get("ExpiredObjectDeleteMarker"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Expiration = Expiration


@dataclass
class NoncurrentVersionExpiration:
    Days: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NoncurrentVersionExpiration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NoncurrentVersionExpiration"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NoncurrentVersionExpiration = NoncurrentVersionExpiration


@dataclass
class Logging:
    TargetBucket: Optional[str]
    TargetPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Logging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Logging"]:
        if not json_data:
            return None
        return cls(
            TargetBucket=json_data.get("TargetBucket"),
            TargetPrefix=json_data.get("TargetPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Logging = Logging


@dataclass
class Versioning:
    Enabled: Optional[bool]
    MfaDelete: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Versioning"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Versioning"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            MfaDelete=json_data.get("MfaDelete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Versioning = Versioning


@dataclass
class Website:
    ErrorDocument: Optional[str]
    IndexDocument: Optional[str]
    RedirectAllRequestsTo: Optional[str]
    RoutingRules: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Website"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Website"]:
        if not json_data:
            return None
        return cls(
            ErrorDocument=json_data.get("ErrorDocument"),
            IndexDocument=json_data.get("IndexDocument"),
            RedirectAllRequestsTo=json_data.get("RedirectAllRequestsTo"),
            RoutingRules=json_data.get("RoutingRules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Website = Website


