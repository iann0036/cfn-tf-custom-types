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
    BucketDomainName: Optional[str]
    ForceDestroy: Optional[bool]
    Region: Optional[str]
    StorageClass: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Versioning: Optional[bool]
    CorsRule: Optional[Sequence["_CorsRule"]]
    LifecycleRule: Optional[Sequence["_LifecycleRule"]]
    Logging: Optional[Sequence["_Logging"]]
    Website: Optional[Sequence["_Website"]]
    Expiration: Optional[Sequence["_Expiration"]]
    NoncurrentVersionExpiration: Optional[Sequence["_NoncurrentVersionExpiration"]]
    NoncurrentVersionTransition: Optional[Sequence["_NoncurrentVersionTransition"]]
    Transition: Optional[Sequence["_Transition"]]

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
            BucketDomainName=json_data.get("BucketDomainName"),
            ForceDestroy=json_data.get("ForceDestroy"),
            Region=json_data.get("Region"),
            StorageClass=json_data.get("StorageClass"),
            Tags=json_data.get("Tags"),
            Versioning=json_data.get("Versioning"),
            CorsRule=json_data.get("CorsRule"),
            LifecycleRule=json_data.get("LifecycleRule"),
            Logging=json_data.get("Logging"),
            Website=json_data.get("Website"),
            Expiration=json_data.get("Expiration"),
            NoncurrentVersionExpiration=json_data.get("NoncurrentVersionExpiration"),
            NoncurrentVersionTransition=json_data.get("NoncurrentVersionTransition"),
            Transition=json_data.get("Transition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
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
    Enabled: Optional[bool]
    Name: Optional[str]
    Prefix: Optional[str]
    Expiration: Optional[Sequence["_Expiration"]]
    NoncurrentVersionExpiration: Optional[Sequence["_NoncurrentVersionExpiration"]]
    NoncurrentVersionTransition: Optional[Sequence["_NoncurrentVersionTransition"]]
    Transition: Optional[Sequence["_Transition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleRule"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Name=json_data.get("Name"),
            Prefix=json_data.get("Prefix"),
            Expiration=json_data.get("Expiration"),
            NoncurrentVersionExpiration=json_data.get("NoncurrentVersionExpiration"),
            NoncurrentVersionTransition=json_data.get("NoncurrentVersionTransition"),
            Transition=json_data.get("Transition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleRule = LifecycleRule


@dataclass
class Expiration:
    Days: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Expiration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Expiration"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
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
class NoncurrentVersionTransition:
    Days: Optional[float]
    StorageClass: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NoncurrentVersionTransition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NoncurrentVersionTransition"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
            StorageClass=json_data.get("StorageClass"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NoncurrentVersionTransition = NoncurrentVersionTransition


@dataclass
class Transition:
    Days: Optional[float]
    StorageClass: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Transition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Transition"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
            StorageClass=json_data.get("StorageClass"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Transition = Transition


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


