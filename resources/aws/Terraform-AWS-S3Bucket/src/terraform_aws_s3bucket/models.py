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
    AccelerationStatus: Optional[str]
    Acl: Optional[str]
    Arn: Optional[str]
    Bucket: Optional[str]
    BucketDomainName: Optional[str]
    BucketPrefix: Optional[str]
    BucketRegionalDomainName: Optional[str]
    ForceDestroy: Optional[bool]
    HostedZoneId: Optional[str]
    Id: Optional[str]
    Policy: Optional[str]
    Region: Optional[str]
    RequestPayer: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    WebsiteDomain: Optional[str]
    WebsiteEndpoint: Optional[str]
    CorsRule: Optional[Sequence["_CorsRule"]]
    Grant: Optional[Sequence["_Grant"]]
    LifecycleRule: Optional[Sequence["_LifecycleRule"]]
    Logging: Optional[Sequence["_Logging"]]
    ObjectLockConfiguration: Optional[Sequence["_ObjectLockConfiguration"]]
    ReplicationConfiguration: Optional[Sequence["_ReplicationConfiguration"]]
    ServerSideEncryptionConfiguration: Optional[Sequence["_ServerSideEncryptionConfiguration"]]
    Versioning: Optional[Sequence["_Versioning"]]
    Website: Optional[Sequence["_Website"]]
    Expiration: Optional[Sequence["_Expiration"]]
    NoncurrentVersionExpiration: Optional[Sequence["_NoncurrentVersionExpiration"]]
    NoncurrentVersionTransition: Optional[Sequence["_NoncurrentVersionTransition"]]
    Transition: Optional[Sequence["_Transition"]]
    Rule: Optional[Sequence["_Rule"]]
    Rules: Optional[Sequence["_Rules"]]
    ApplyServerSideEncryptionByDefault: Optional[Sequence["_ApplyServerSideEncryptionByDefault"]]
    Destination: Optional[Sequence["_Destination"]]
    Filter: Optional[Sequence["_Filter"]]
    SourceSelectionCriteria: Optional[Sequence["_SourceSelectionCriteria"]]
    AccessControlTranslation: Optional[Sequence["_AccessControlTranslation"]]
    SseKmsEncryptedObjects: Optional[Sequence["_SseKmsEncryptedObjects"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccelerationStatus=json_data.get("AccelerationStatus"),
            Acl=json_data.get("Acl"),
            Arn=json_data.get("Arn"),
            Bucket=json_data.get("Bucket"),
            BucketDomainName=json_data.get("BucketDomainName"),
            BucketPrefix=json_data.get("BucketPrefix"),
            BucketRegionalDomainName=json_data.get("BucketRegionalDomainName"),
            ForceDestroy=json_data.get("ForceDestroy"),
            HostedZoneId=json_data.get("HostedZoneId"),
            Id=json_data.get("Id"),
            Policy=json_data.get("Policy"),
            Region=json_data.get("Region"),
            RequestPayer=json_data.get("RequestPayer"),
            Tags=json_data.get("Tags"),
            WebsiteDomain=json_data.get("WebsiteDomain"),
            WebsiteEndpoint=json_data.get("WebsiteEndpoint"),
            CorsRule=json_data.get("CorsRule"),
            Grant=json_data.get("Grant"),
            LifecycleRule=json_data.get("LifecycleRule"),
            Logging=json_data.get("Logging"),
            ObjectLockConfiguration=json_data.get("ObjectLockConfiguration"),
            ReplicationConfiguration=json_data.get("ReplicationConfiguration"),
            ServerSideEncryptionConfiguration=json_data.get("ServerSideEncryptionConfiguration"),
            Versioning=json_data.get("Versioning"),
            Website=json_data.get("Website"),
            Expiration=json_data.get("Expiration"),
            NoncurrentVersionExpiration=json_data.get("NoncurrentVersionExpiration"),
            NoncurrentVersionTransition=json_data.get("NoncurrentVersionTransition"),
            Transition=json_data.get("Transition"),
            Rule=json_data.get("Rule"),
            Rules=json_data.get("Rules"),
            ApplyServerSideEncryptionByDefault=json_data.get("ApplyServerSideEncryptionByDefault"),
            Destination=json_data.get("Destination"),
            Filter=json_data.get("Filter"),
            SourceSelectionCriteria=json_data.get("SourceSelectionCriteria"),
            AccessControlTranslation=json_data.get("AccessControlTranslation"),
            SseKmsEncryptedObjects=json_data.get("SseKmsEncryptedObjects"),
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
class Grant:
    Id: Optional[str]
    Permissions: Optional[Sequence[str]]
    Type: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Grant"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Grant"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Permissions=json_data.get("Permissions"),
            Type=json_data.get("Type"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Grant = Grant


@dataclass
class LifecycleRule:
    AbortIncompleteMultipartUploadDays: Optional[float]
    Enabled: Optional[bool]
    Id: Optional[str]
    Prefix: Optional[str]
    Tags: Optional[Sequence["_Tags2"]]
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
            AbortIncompleteMultipartUploadDays=json_data.get("AbortIncompleteMultipartUploadDays"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
            Tags=json_data.get("Tags"),
            Expiration=json_data.get("Expiration"),
            NoncurrentVersionExpiration=json_data.get("NoncurrentVersionExpiration"),
            NoncurrentVersionTransition=json_data.get("NoncurrentVersionTransition"),
            Transition=json_data.get("Transition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleRule = LifecycleRule


@dataclass
class Tags2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags2 = Tags2


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
    Date: Optional[str]
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
            Date=json_data.get("Date"),
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
class ObjectLockConfiguration:
    ObjectLockEnabled: Optional[str]
    Rule: Optional[Sequence["_Rule"]]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectLockConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectLockConfiguration"]:
        if not json_data:
            return None
        return cls(
            ObjectLockEnabled=json_data.get("ObjectLockEnabled"),
            Rule=json_data.get("Rule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectLockConfiguration = ObjectLockConfiguration


@dataclass
class Rule:
    ApplyServerSideEncryptionByDefault: Optional[Sequence["_ApplyServerSideEncryptionByDefault"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            ApplyServerSideEncryptionByDefault=json_data.get("ApplyServerSideEncryptionByDefault"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class ApplyServerSideEncryptionByDefault:
    KmsMasterKeyId: Optional[str]
    SseAlgorithm: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplyServerSideEncryptionByDefault"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplyServerSideEncryptionByDefault"]:
        if not json_data:
            return None
        return cls(
            KmsMasterKeyId=json_data.get("KmsMasterKeyId"),
            SseAlgorithm=json_data.get("SseAlgorithm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplyServerSideEncryptionByDefault = ApplyServerSideEncryptionByDefault


@dataclass
class ReplicationConfiguration:
    Role: Optional[str]
    Rules: Optional[Sequence["_Rules"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationConfiguration"]:
        if not json_data:
            return None
        return cls(
            Role=json_data.get("Role"),
            Rules=json_data.get("Rules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationConfiguration = ReplicationConfiguration


@dataclass
class Rules:
    Id: Optional[str]
    Prefix: Optional[str]
    Priority: Optional[float]
    Status: Optional[str]
    Destination: Optional[Sequence["_Destination"]]
    Filter: Optional[Sequence["_Filter"]]
    SourceSelectionCriteria: Optional[Sequence["_SourceSelectionCriteria"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rules"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
            Priority=json_data.get("Priority"),
            Status=json_data.get("Status"),
            Destination=json_data.get("Destination"),
            Filter=json_data.get("Filter"),
            SourceSelectionCriteria=json_data.get("SourceSelectionCriteria"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rules = Rules


@dataclass
class Destination:
    AccountId: Optional[str]
    Bucket: Optional[str]
    ReplicaKmsKeyId: Optional[str]
    StorageClass: Optional[str]
    AccessControlTranslation: Optional[Sequence["_AccessControlTranslation"]]

    @classmethod
    def _deserialize(
        cls: Type["_Destination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Destination"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            Bucket=json_data.get("Bucket"),
            ReplicaKmsKeyId=json_data.get("ReplicaKmsKeyId"),
            StorageClass=json_data.get("StorageClass"),
            AccessControlTranslation=json_data.get("AccessControlTranslation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Destination = Destination


@dataclass
class AccessControlTranslation:
    Owner: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessControlTranslation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessControlTranslation"]:
        if not json_data:
            return None
        return cls(
            Owner=json_data.get("Owner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessControlTranslation = AccessControlTranslation


@dataclass
class Filter:
    Prefix: Optional[str]
    Tags: Optional[Sequence["_Tags3"]]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


@dataclass
class Tags3:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags3 = Tags3


@dataclass
class SourceSelectionCriteria:
    SseKmsEncryptedObjects: Optional[Sequence["_SseKmsEncryptedObjects"]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceSelectionCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceSelectionCriteria"]:
        if not json_data:
            return None
        return cls(
            SseKmsEncryptedObjects=json_data.get("SseKmsEncryptedObjects"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceSelectionCriteria = SourceSelectionCriteria


@dataclass
class SseKmsEncryptedObjects:
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SseKmsEncryptedObjects"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SseKmsEncryptedObjects"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SseKmsEncryptedObjects = SseKmsEncryptedObjects


@dataclass
class ServerSideEncryptionConfiguration:
    Rule: Optional[Sequence["_Rule"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            Rule=json_data.get("Rule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryptionConfiguration = ServerSideEncryptionConfiguration


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


