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
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    WebsiteDomain: Optional[str]
    WebsiteEndpoint: Optional[str]
    CorsRule: Optional[Sequence["_CorsRuleDefinition"]]
    Grant: Optional[Sequence["_GrantDefinition"]]
    LifecycleRule: Optional[Sequence["_LifecycleRuleDefinition"]]
    Logging: Optional[Sequence["_LoggingDefinition"]]
    ObjectLockConfiguration: Optional[Sequence["_ObjectLockConfigurationDefinition"]]
    ReplicationConfiguration: Optional[Sequence["_ReplicationConfigurationDefinition"]]
    ServerSideEncryptionConfiguration: Optional[Sequence["_ServerSideEncryptionConfigurationDefinition"]]
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
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            WebsiteDomain=json_data.get("WebsiteDomain"),
            WebsiteEndpoint=json_data.get("WebsiteEndpoint"),
            CorsRule=deserialize_list(json_data.get("CorsRule"), CorsRuleDefinition),
            Grant=deserialize_list(json_data.get("Grant"), GrantDefinition),
            LifecycleRule=deserialize_list(json_data.get("LifecycleRule"), LifecycleRuleDefinition),
            Logging=deserialize_list(json_data.get("Logging"), LoggingDefinition),
            ObjectLockConfiguration=deserialize_list(json_data.get("ObjectLockConfiguration"), ObjectLockConfigurationDefinition),
            ReplicationConfiguration=deserialize_list(json_data.get("ReplicationConfiguration"), ReplicationConfigurationDefinition),
            ServerSideEncryptionConfiguration=deserialize_list(json_data.get("ServerSideEncryptionConfiguration"), ServerSideEncryptionConfigurationDefinition),
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
class GrantDefinition(BaseModel):
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
            Id=json_data.get("Id"),
            Permissions=json_data.get("Permissions"),
            Type=json_data.get("Type"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrantDefinition = GrantDefinition


@dataclass
class LifecycleRuleDefinition(BaseModel):
    AbortIncompleteMultipartUploadDays: Optional[float]
    Enabled: Optional[bool]
    Id: Optional[str]
    Prefix: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition2"]]
    Expiration: Optional[Sequence["_ExpirationDefinition"]]
    NoncurrentVersionExpiration: Optional[Sequence["_NoncurrentVersionExpirationDefinition"]]
    NoncurrentVersionTransition: Optional[Sequence["_NoncurrentVersionTransitionDefinition"]]
    Transition: Optional[Sequence["_TransitionDefinition"]]

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
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition2),
            Expiration=deserialize_list(json_data.get("Expiration"), ExpirationDefinition),
            NoncurrentVersionExpiration=deserialize_list(json_data.get("NoncurrentVersionExpiration"), NoncurrentVersionExpirationDefinition),
            NoncurrentVersionTransition=deserialize_list(json_data.get("NoncurrentVersionTransition"), NoncurrentVersionTransitionDefinition),
            Transition=deserialize_list(json_data.get("Transition"), TransitionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleRuleDefinition = LifecycleRuleDefinition


@dataclass
class TagsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition2 = TagsDefinition2


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
class TransitionDefinition(BaseModel):
    Date: Optional[str]
    Days: Optional[float]
    StorageClass: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TransitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Date=json_data.get("Date"),
            Days=json_data.get("Days"),
            StorageClass=json_data.get("StorageClass"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransitionDefinition = TransitionDefinition


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
class ObjectLockConfigurationDefinition(BaseModel):
    ObjectLockEnabled: Optional[str]
    Rule: Optional[Sequence["_RuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectLockConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectLockConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ObjectLockEnabled=json_data.get("ObjectLockEnabled"),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectLockConfigurationDefinition = ObjectLockConfigurationDefinition


@dataclass
class RuleDefinition(BaseModel):
    BucketKeyEnabled: Optional[bool]
    ApplyServerSideEncryptionByDefault: Optional[Sequence["_ApplyServerSideEncryptionByDefaultDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            BucketKeyEnabled=json_data.get("BucketKeyEnabled"),
            ApplyServerSideEncryptionByDefault=deserialize_list(json_data.get("ApplyServerSideEncryptionByDefault"), ApplyServerSideEncryptionByDefaultDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class ApplyServerSideEncryptionByDefaultDefinition(BaseModel):
    KmsMasterKeyId: Optional[str]
    SseAlgorithm: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplyServerSideEncryptionByDefaultDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplyServerSideEncryptionByDefaultDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsMasterKeyId=json_data.get("KmsMasterKeyId"),
            SseAlgorithm=json_data.get("SseAlgorithm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplyServerSideEncryptionByDefaultDefinition = ApplyServerSideEncryptionByDefaultDefinition


@dataclass
class ReplicationConfigurationDefinition(BaseModel):
    Role: Optional[str]
    Rules: Optional[Sequence["_RulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Role=json_data.get("Role"),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationConfigurationDefinition = ReplicationConfigurationDefinition


@dataclass
class RulesDefinition(BaseModel):
    Id: Optional[str]
    Prefix: Optional[str]
    Priority: Optional[float]
    Status: Optional[str]
    Destination: Optional[Sequence["_DestinationDefinition"]]
    Filter: Optional[Sequence["_FilterDefinition"]]
    SourceSelectionCriteria: Optional[Sequence["_SourceSelectionCriteriaDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
            Priority=json_data.get("Priority"),
            Status=json_data.get("Status"),
            Destination=deserialize_list(json_data.get("Destination"), DestinationDefinition),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
            SourceSelectionCriteria=deserialize_list(json_data.get("SourceSelectionCriteria"), SourceSelectionCriteriaDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class DestinationDefinition(BaseModel):
    AccountId: Optional[str]
    Bucket: Optional[str]
    ReplicaKmsKeyId: Optional[str]
    StorageClass: Optional[str]
    AccessControlTranslation: Optional[Sequence["_AccessControlTranslationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            Bucket=json_data.get("Bucket"),
            ReplicaKmsKeyId=json_data.get("ReplicaKmsKeyId"),
            StorageClass=json_data.get("StorageClass"),
            AccessControlTranslation=deserialize_list(json_data.get("AccessControlTranslation"), AccessControlTranslationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationDefinition = DestinationDefinition


@dataclass
class AccessControlTranslationDefinition(BaseModel):
    Owner: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessControlTranslationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessControlTranslationDefinition"]:
        if not json_data:
            return None
        return cls(
            Owner=json_data.get("Owner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessControlTranslationDefinition = AccessControlTranslationDefinition


@dataclass
class FilterDefinition(BaseModel):
    Prefix: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition3"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition3),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class TagsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition3 = TagsDefinition3


@dataclass
class SourceSelectionCriteriaDefinition(BaseModel):
    SseKmsEncryptedObjects: Optional[Sequence["_SseKmsEncryptedObjectsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceSelectionCriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceSelectionCriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            SseKmsEncryptedObjects=deserialize_list(json_data.get("SseKmsEncryptedObjects"), SseKmsEncryptedObjectsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceSelectionCriteriaDefinition = SourceSelectionCriteriaDefinition


@dataclass
class SseKmsEncryptedObjectsDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SseKmsEncryptedObjectsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SseKmsEncryptedObjectsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SseKmsEncryptedObjectsDefinition = SseKmsEncryptedObjectsDefinition


@dataclass
class ServerSideEncryptionConfigurationDefinition(BaseModel):
    Rule: Optional[Sequence["_RuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryptionConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryptionConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryptionConfigurationDefinition = ServerSideEncryptionConfigurationDefinition


@dataclass
class VersioningDefinition(BaseModel):
    Enabled: Optional[bool]
    MfaDelete: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_VersioningDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersioningDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            MfaDelete=json_data.get("MfaDelete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersioningDefinition = VersioningDefinition


@dataclass
class WebsiteDefinition(BaseModel):
    ErrorDocument: Optional[str]
    IndexDocument: Optional[str]
    RedirectAllRequestsTo: Optional[str]
    RoutingRules: Optional[str]

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
            RedirectAllRequestsTo=json_data.get("RedirectAllRequestsTo"),
            RoutingRules=json_data.get("RoutingRules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebsiteDefinition = WebsiteDefinition


