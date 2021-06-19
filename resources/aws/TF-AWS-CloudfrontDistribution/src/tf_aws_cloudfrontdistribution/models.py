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
    Aliases: Optional[Sequence[str]]
    Arn: Optional[str]
    CallerReference: Optional[str]
    Comment: Optional[str]
    DefaultRootObject: Optional[str]
    DomainName: Optional[str]
    Enabled: Optional[bool]
    Etag: Optional[str]
    HostedZoneId: Optional[str]
    HttpVersion: Optional[str]
    Id: Optional[str]
    InProgressValidationBatches: Optional[float]
    IsIpv6Enabled: Optional[bool]
    LastModifiedTime: Optional[str]
    PriceClass: Optional[str]
    RetainOnDelete: Optional[bool]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    TrustedKeyGroups: Optional[Sequence["_TrustedKeyGroupsDefinition2"]]
    TrustedSigners: Optional[Sequence["_TrustedSignersDefinition2"]]
    WaitForDeployment: Optional[bool]
    WebAclId: Optional[str]
    CustomErrorResponse: Optional[Sequence["_CustomErrorResponseDefinition"]]
    DefaultCacheBehavior: Optional[Sequence["_DefaultCacheBehaviorDefinition"]]
    LoggingConfig: Optional[Sequence["_LoggingConfigDefinition"]]
    OrderedCacheBehavior: Optional[Sequence["_OrderedCacheBehaviorDefinition"]]
    Origin: Optional[Sequence["_OriginDefinition"]]
    OriginGroup: Optional[Sequence["_OriginGroupDefinition"]]
    Restrictions: Optional[Sequence["_RestrictionsDefinition"]]
    ViewerCertificate: Optional[Sequence["_ViewerCertificateDefinition"]]

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
            Aliases=json_data.get("Aliases"),
            Arn=json_data.get("Arn"),
            CallerReference=json_data.get("CallerReference"),
            Comment=json_data.get("Comment"),
            DefaultRootObject=json_data.get("DefaultRootObject"),
            DomainName=json_data.get("DomainName"),
            Enabled=json_data.get("Enabled"),
            Etag=json_data.get("Etag"),
            HostedZoneId=json_data.get("HostedZoneId"),
            HttpVersion=json_data.get("HttpVersion"),
            Id=json_data.get("Id"),
            InProgressValidationBatches=json_data.get("InProgressValidationBatches"),
            IsIpv6Enabled=json_data.get("IsIpv6Enabled"),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            PriceClass=json_data.get("PriceClass"),
            RetainOnDelete=json_data.get("RetainOnDelete"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            TrustedKeyGroups=deserialize_list(json_data.get("TrustedKeyGroups"), TrustedKeyGroupsDefinition2),
            TrustedSigners=deserialize_list(json_data.get("TrustedSigners"), TrustedSignersDefinition2),
            WaitForDeployment=json_data.get("WaitForDeployment"),
            WebAclId=json_data.get("WebAclId"),
            CustomErrorResponse=deserialize_list(json_data.get("CustomErrorResponse"), CustomErrorResponseDefinition),
            DefaultCacheBehavior=deserialize_list(json_data.get("DefaultCacheBehavior"), DefaultCacheBehaviorDefinition),
            LoggingConfig=deserialize_list(json_data.get("LoggingConfig"), LoggingConfigDefinition),
            OrderedCacheBehavior=deserialize_list(json_data.get("OrderedCacheBehavior"), OrderedCacheBehaviorDefinition),
            Origin=deserialize_list(json_data.get("Origin"), OriginDefinition),
            OriginGroup=deserialize_list(json_data.get("OriginGroup"), OriginGroupDefinition),
            Restrictions=deserialize_list(json_data.get("Restrictions"), RestrictionsDefinition),
            ViewerCertificate=deserialize_list(json_data.get("ViewerCertificate"), ViewerCertificateDefinition),
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
class TrustedKeyGroupsDefinition2(BaseModel):
    Enabled: Optional[bool]
    Items: Optional[Sequence["_TrustedKeyGroupsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TrustedKeyGroupsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrustedKeyGroupsDefinition2"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Items=deserialize_list(json_data.get("Items"), TrustedKeyGroupsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrustedKeyGroupsDefinition2 = TrustedKeyGroupsDefinition2


@dataclass
class TrustedKeyGroupsDefinition(BaseModel):
    KeyGroupId: Optional[str]
    KeyPairIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TrustedKeyGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrustedKeyGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyGroupId=json_data.get("KeyGroupId"),
            KeyPairIds=json_data.get("KeyPairIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrustedKeyGroupsDefinition = TrustedKeyGroupsDefinition


@dataclass
class TrustedSignersDefinition2(BaseModel):
    Enabled: Optional[bool]
    Items: Optional[Sequence["_TrustedSignersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TrustedSignersDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrustedSignersDefinition2"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Items=deserialize_list(json_data.get("Items"), TrustedSignersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrustedSignersDefinition2 = TrustedSignersDefinition2


@dataclass
class TrustedSignersDefinition(BaseModel):
    AwsAccountNumber: Optional[str]
    KeyPairIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TrustedSignersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrustedSignersDefinition"]:
        if not json_data:
            return None
        return cls(
            AwsAccountNumber=json_data.get("AwsAccountNumber"),
            KeyPairIds=json_data.get("KeyPairIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrustedSignersDefinition = TrustedSignersDefinition


@dataclass
class CustomErrorResponseDefinition(BaseModel):
    ErrorCachingMinTtl: Optional[float]
    ErrorCode: Optional[float]
    ResponseCode: Optional[float]
    ResponsePagePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomErrorResponseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomErrorResponseDefinition"]:
        if not json_data:
            return None
        return cls(
            ErrorCachingMinTtl=json_data.get("ErrorCachingMinTtl"),
            ErrorCode=json_data.get("ErrorCode"),
            ResponseCode=json_data.get("ResponseCode"),
            ResponsePagePath=json_data.get("ResponsePagePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomErrorResponseDefinition = CustomErrorResponseDefinition


@dataclass
class DefaultCacheBehaviorDefinition(BaseModel):
    AllowedMethods: Optional[Sequence[str]]
    CachePolicyId: Optional[str]
    CachedMethods: Optional[Sequence[str]]
    Compress: Optional[bool]
    DefaultTtl: Optional[float]
    FieldLevelEncryptionId: Optional[str]
    MaxTtl: Optional[float]
    MinTtl: Optional[float]
    OriginRequestPolicyId: Optional[str]
    RealtimeLogConfigArn: Optional[str]
    SmoothStreaming: Optional[bool]
    TargetOriginId: Optional[str]
    TrustedKeyGroups: Optional[Sequence[str]]
    TrustedSigners: Optional[Sequence[str]]
    ViewerProtocolPolicy: Optional[str]
    ForwardedValues: Optional[Sequence["_ForwardedValuesDefinition"]]
    FunctionAssociation: Optional[Sequence["_FunctionAssociationDefinition"]]
    LambdaFunctionAssociation: Optional[Sequence["_LambdaFunctionAssociationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultCacheBehaviorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultCacheBehaviorDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedMethods=json_data.get("AllowedMethods"),
            CachePolicyId=json_data.get("CachePolicyId"),
            CachedMethods=json_data.get("CachedMethods"),
            Compress=json_data.get("Compress"),
            DefaultTtl=json_data.get("DefaultTtl"),
            FieldLevelEncryptionId=json_data.get("FieldLevelEncryptionId"),
            MaxTtl=json_data.get("MaxTtl"),
            MinTtl=json_data.get("MinTtl"),
            OriginRequestPolicyId=json_data.get("OriginRequestPolicyId"),
            RealtimeLogConfigArn=json_data.get("RealtimeLogConfigArn"),
            SmoothStreaming=json_data.get("SmoothStreaming"),
            TargetOriginId=json_data.get("TargetOriginId"),
            TrustedKeyGroups=json_data.get("TrustedKeyGroups"),
            TrustedSigners=json_data.get("TrustedSigners"),
            ViewerProtocolPolicy=json_data.get("ViewerProtocolPolicy"),
            ForwardedValues=deserialize_list(json_data.get("ForwardedValues"), ForwardedValuesDefinition),
            FunctionAssociation=deserialize_list(json_data.get("FunctionAssociation"), FunctionAssociationDefinition),
            LambdaFunctionAssociation=deserialize_list(json_data.get("LambdaFunctionAssociation"), LambdaFunctionAssociationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultCacheBehaviorDefinition = DefaultCacheBehaviorDefinition


@dataclass
class ForwardedValuesDefinition(BaseModel):
    Headers: Optional[Sequence[str]]
    QueryString: Optional[bool]
    QueryStringCacheKeys: Optional[Sequence[str]]
    Cookies: Optional[Sequence["_CookiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardedValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardedValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=json_data.get("Headers"),
            QueryString=json_data.get("QueryString"),
            QueryStringCacheKeys=json_data.get("QueryStringCacheKeys"),
            Cookies=deserialize_list(json_data.get("Cookies"), CookiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardedValuesDefinition = ForwardedValuesDefinition


@dataclass
class CookiesDefinition(BaseModel):
    Forward: Optional[str]
    WhitelistedNames: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CookiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Forward=json_data.get("Forward"),
            WhitelistedNames=json_data.get("WhitelistedNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CookiesDefinition = CookiesDefinition


@dataclass
class FunctionAssociationDefinition(BaseModel):
    EventType: Optional[str]
    FunctionArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FunctionAssociationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FunctionAssociationDefinition"]:
        if not json_data:
            return None
        return cls(
            EventType=json_data.get("EventType"),
            FunctionArn=json_data.get("FunctionArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FunctionAssociationDefinition = FunctionAssociationDefinition


@dataclass
class LambdaFunctionAssociationDefinition(BaseModel):
    EventType: Optional[str]
    IncludeBody: Optional[bool]
    LambdaArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaFunctionAssociationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaFunctionAssociationDefinition"]:
        if not json_data:
            return None
        return cls(
            EventType=json_data.get("EventType"),
            IncludeBody=json_data.get("IncludeBody"),
            LambdaArn=json_data.get("LambdaArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaFunctionAssociationDefinition = LambdaFunctionAssociationDefinition


@dataclass
class LoggingConfigDefinition(BaseModel):
    Bucket: Optional[str]
    IncludeCookies: Optional[bool]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            IncludeCookies=json_data.get("IncludeCookies"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingConfigDefinition = LoggingConfigDefinition


@dataclass
class OrderedCacheBehaviorDefinition(BaseModel):
    AllowedMethods: Optional[Sequence[str]]
    CachePolicyId: Optional[str]
    CachedMethods: Optional[Sequence[str]]
    Compress: Optional[bool]
    DefaultTtl: Optional[float]
    FieldLevelEncryptionId: Optional[str]
    MaxTtl: Optional[float]
    MinTtl: Optional[float]
    OriginRequestPolicyId: Optional[str]
    PathPattern: Optional[str]
    RealtimeLogConfigArn: Optional[str]
    SmoothStreaming: Optional[bool]
    TargetOriginId: Optional[str]
    TrustedKeyGroups: Optional[Sequence[str]]
    TrustedSigners: Optional[Sequence[str]]
    ViewerProtocolPolicy: Optional[str]
    ForwardedValues: Optional[Sequence["_ForwardedValuesDefinition"]]
    FunctionAssociation: Optional[Sequence["_FunctionAssociationDefinition"]]
    LambdaFunctionAssociation: Optional[Sequence["_LambdaFunctionAssociationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OrderedCacheBehaviorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrderedCacheBehaviorDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedMethods=json_data.get("AllowedMethods"),
            CachePolicyId=json_data.get("CachePolicyId"),
            CachedMethods=json_data.get("CachedMethods"),
            Compress=json_data.get("Compress"),
            DefaultTtl=json_data.get("DefaultTtl"),
            FieldLevelEncryptionId=json_data.get("FieldLevelEncryptionId"),
            MaxTtl=json_data.get("MaxTtl"),
            MinTtl=json_data.get("MinTtl"),
            OriginRequestPolicyId=json_data.get("OriginRequestPolicyId"),
            PathPattern=json_data.get("PathPattern"),
            RealtimeLogConfigArn=json_data.get("RealtimeLogConfigArn"),
            SmoothStreaming=json_data.get("SmoothStreaming"),
            TargetOriginId=json_data.get("TargetOriginId"),
            TrustedKeyGroups=json_data.get("TrustedKeyGroups"),
            TrustedSigners=json_data.get("TrustedSigners"),
            ViewerProtocolPolicy=json_data.get("ViewerProtocolPolicy"),
            ForwardedValues=deserialize_list(json_data.get("ForwardedValues"), ForwardedValuesDefinition),
            FunctionAssociation=deserialize_list(json_data.get("FunctionAssociation"), FunctionAssociationDefinition),
            LambdaFunctionAssociation=deserialize_list(json_data.get("LambdaFunctionAssociation"), LambdaFunctionAssociationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrderedCacheBehaviorDefinition = OrderedCacheBehaviorDefinition


@dataclass
class OriginDefinition(BaseModel):
    ConnectionAttempts: Optional[float]
    ConnectionTimeout: Optional[float]
    DomainName: Optional[str]
    OriginId: Optional[str]
    OriginPath: Optional[str]
    CustomHeader: Optional[Sequence["_CustomHeaderDefinition"]]
    CustomOriginConfig: Optional[Sequence["_CustomOriginConfigDefinition"]]
    OriginShield: Optional[Sequence["_OriginShieldDefinition"]]
    S3OriginConfig: Optional[Sequence["_S3OriginConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OriginDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionAttempts=json_data.get("ConnectionAttempts"),
            ConnectionTimeout=json_data.get("ConnectionTimeout"),
            DomainName=json_data.get("DomainName"),
            OriginId=json_data.get("OriginId"),
            OriginPath=json_data.get("OriginPath"),
            CustomHeader=deserialize_list(json_data.get("CustomHeader"), CustomHeaderDefinition),
            CustomOriginConfig=deserialize_list(json_data.get("CustomOriginConfig"), CustomOriginConfigDefinition),
            OriginShield=deserialize_list(json_data.get("OriginShield"), OriginShieldDefinition),
            S3OriginConfig=deserialize_list(json_data.get("S3OriginConfig"), S3OriginConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginDefinition = OriginDefinition


@dataclass
class CustomHeaderDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomHeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomHeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomHeaderDefinition = CustomHeaderDefinition


@dataclass
class CustomOriginConfigDefinition(BaseModel):
    HttpPort: Optional[float]
    HttpsPort: Optional[float]
    OriginKeepaliveTimeout: Optional[float]
    OriginProtocolPolicy: Optional[str]
    OriginReadTimeout: Optional[float]
    OriginSslProtocols: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomOriginConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomOriginConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            HttpPort=json_data.get("HttpPort"),
            HttpsPort=json_data.get("HttpsPort"),
            OriginKeepaliveTimeout=json_data.get("OriginKeepaliveTimeout"),
            OriginProtocolPolicy=json_data.get("OriginProtocolPolicy"),
            OriginReadTimeout=json_data.get("OriginReadTimeout"),
            OriginSslProtocols=json_data.get("OriginSslProtocols"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomOriginConfigDefinition = CustomOriginConfigDefinition


@dataclass
class OriginShieldDefinition(BaseModel):
    Enabled: Optional[bool]
    OriginShieldRegion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OriginShieldDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginShieldDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            OriginShieldRegion=json_data.get("OriginShieldRegion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginShieldDefinition = OriginShieldDefinition


@dataclass
class S3OriginConfigDefinition(BaseModel):
    OriginAccessIdentity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3OriginConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3OriginConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            OriginAccessIdentity=json_data.get("OriginAccessIdentity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3OriginConfigDefinition = S3OriginConfigDefinition


@dataclass
class OriginGroupDefinition(BaseModel):
    OriginId: Optional[str]
    FailoverCriteria: Optional[Sequence["_FailoverCriteriaDefinition"]]
    Member: Optional[Sequence["_MemberDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OriginGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            OriginId=json_data.get("OriginId"),
            FailoverCriteria=deserialize_list(json_data.get("FailoverCriteria"), FailoverCriteriaDefinition),
            Member=deserialize_list(json_data.get("Member"), MemberDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginGroupDefinition = OriginGroupDefinition


@dataclass
class FailoverCriteriaDefinition(BaseModel):
    StatusCodes: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_FailoverCriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailoverCriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            StatusCodes=json_data.get("StatusCodes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailoverCriteriaDefinition = FailoverCriteriaDefinition


@dataclass
class MemberDefinition(BaseModel):
    OriginId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MemberDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemberDefinition"]:
        if not json_data:
            return None
        return cls(
            OriginId=json_data.get("OriginId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemberDefinition = MemberDefinition


@dataclass
class RestrictionsDefinition(BaseModel):
    GeoRestriction: Optional[Sequence["_GeoRestrictionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RestrictionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestrictionsDefinition"]:
        if not json_data:
            return None
        return cls(
            GeoRestriction=deserialize_list(json_data.get("GeoRestriction"), GeoRestrictionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestrictionsDefinition = RestrictionsDefinition


@dataclass
class GeoRestrictionDefinition(BaseModel):
    Locations: Optional[Sequence[str]]
    RestrictionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeoRestrictionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoRestrictionDefinition"]:
        if not json_data:
            return None
        return cls(
            Locations=json_data.get("Locations"),
            RestrictionType=json_data.get("RestrictionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoRestrictionDefinition = GeoRestrictionDefinition


@dataclass
class ViewerCertificateDefinition(BaseModel):
    AcmCertificateArn: Optional[str]
    CloudfrontDefaultCertificate: Optional[bool]
    IamCertificateId: Optional[str]
    MinimumProtocolVersion: Optional[str]
    SslSupportMethod: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ViewerCertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ViewerCertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            AcmCertificateArn=json_data.get("AcmCertificateArn"),
            CloudfrontDefaultCertificate=json_data.get("CloudfrontDefaultCertificate"),
            IamCertificateId=json_data.get("IamCertificateId"),
            MinimumProtocolVersion=json_data.get("MinimumProtocolVersion"),
            SslSupportMethod=json_data.get("SslSupportMethod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ViewerCertificateDefinition = ViewerCertificateDefinition


