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
    ActiveTrustedSigners: Optional[Sequence["_ActiveTrustedSigners"]]
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
    Tags: Optional[Sequence["_Tags"]]
    WaitForDeployment: Optional[bool]
    WebAclId: Optional[str]
    CacheBehavior: Optional[Sequence["_CacheBehavior"]]
    CustomErrorResponse: Optional[Sequence["_CustomErrorResponse"]]
    DefaultCacheBehavior: Optional[Sequence["_DefaultCacheBehavior"]]
    LoggingConfig: Optional[Sequence["_LoggingConfig"]]
    OrderedCacheBehavior: Optional[Sequence["_OrderedCacheBehavior"]]
    Origin: Optional[Sequence["_Origin"]]
    OriginGroup: Optional[Sequence["_OriginGroup"]]
    Restrictions: Optional[Sequence["_Restrictions"]]
    ViewerCertificate: Optional[Sequence["_ViewerCertificate"]]
    ForwardedValues: Optional[Sequence["_ForwardedValues"]]
    LambdaFunctionAssociation: Optional[Sequence["_LambdaFunctionAssociation"]]
    CustomHeader: Optional[Sequence["_CustomHeader"]]
    CustomOriginConfig: Optional[Sequence["_CustomOriginConfig"]]
    S3OriginConfig: Optional[Sequence["_S3OriginConfig"]]
    FailoverCriteria: Optional[Sequence["_FailoverCriteria"]]
    Member: Optional[Sequence["_Member"]]
    GeoRestriction: Optional[Sequence["_GeoRestriction"]]
    Cookies: Optional[Sequence["_Cookies"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ActiveTrustedSigners=json_data.get("ActiveTrustedSigners"),
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
            Tags=json_data.get("Tags"),
            WaitForDeployment=json_data.get("WaitForDeployment"),
            WebAclId=json_data.get("WebAclId"),
            CacheBehavior=json_data.get("CacheBehavior"),
            CustomErrorResponse=json_data.get("CustomErrorResponse"),
            DefaultCacheBehavior=json_data.get("DefaultCacheBehavior"),
            LoggingConfig=json_data.get("LoggingConfig"),
            OrderedCacheBehavior=json_data.get("OrderedCacheBehavior"),
            Origin=json_data.get("Origin"),
            OriginGroup=json_data.get("OriginGroup"),
            Restrictions=json_data.get("Restrictions"),
            ViewerCertificate=json_data.get("ViewerCertificate"),
            ForwardedValues=json_data.get("ForwardedValues"),
            LambdaFunctionAssociation=json_data.get("LambdaFunctionAssociation"),
            CustomHeader=json_data.get("CustomHeader"),
            CustomOriginConfig=json_data.get("CustomOriginConfig"),
            S3OriginConfig=json_data.get("S3OriginConfig"),
            FailoverCriteria=json_data.get("FailoverCriteria"),
            Member=json_data.get("Member"),
            GeoRestriction=json_data.get("GeoRestriction"),
            Cookies=json_data.get("Cookies"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ActiveTrustedSigners:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActiveTrustedSigners"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActiveTrustedSigners"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActiveTrustedSigners = ActiveTrustedSigners


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
class CacheBehavior:
    AllowedMethods: Optional[Sequence[str]]
    CachedMethods: Optional[Sequence[str]]
    Compress: Optional[bool]
    DefaultTtl: Optional[float]
    FieldLevelEncryptionId: Optional[str]
    MaxTtl: Optional[float]
    MinTtl: Optional[float]
    PathPattern: Optional[str]
    SmoothStreaming: Optional[bool]
    TargetOriginId: Optional[str]
    TrustedSigners: Optional[Sequence[str]]
    ViewerProtocolPolicy: Optional[str]
    ForwardedValues: Optional[Sequence["_ForwardedValues"]]
    LambdaFunctionAssociation: Optional[Sequence["_LambdaFunctionAssociation"]]

    @classmethod
    def _deserialize(
        cls: Type["_CacheBehavior"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheBehavior"]:
        if not json_data:
            return None
        return cls(
            AllowedMethods=json_data.get("AllowedMethods"),
            CachedMethods=json_data.get("CachedMethods"),
            Compress=json_data.get("Compress"),
            DefaultTtl=json_data.get("DefaultTtl"),
            FieldLevelEncryptionId=json_data.get("FieldLevelEncryptionId"),
            MaxTtl=json_data.get("MaxTtl"),
            MinTtl=json_data.get("MinTtl"),
            PathPattern=json_data.get("PathPattern"),
            SmoothStreaming=json_data.get("SmoothStreaming"),
            TargetOriginId=json_data.get("TargetOriginId"),
            TrustedSigners=json_data.get("TrustedSigners"),
            ViewerProtocolPolicy=json_data.get("ViewerProtocolPolicy"),
            ForwardedValues=json_data.get("ForwardedValues"),
            LambdaFunctionAssociation=json_data.get("LambdaFunctionAssociation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheBehavior = CacheBehavior


@dataclass
class ForwardedValues:
    Headers: Optional[Sequence[str]]
    QueryString: Optional[bool]
    QueryStringCacheKeys: Optional[Sequence[str]]
    Cookies: Optional[Sequence["_Cookies"]]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardedValues"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardedValues"]:
        if not json_data:
            return None
        return cls(
            Headers=json_data.get("Headers"),
            QueryString=json_data.get("QueryString"),
            QueryStringCacheKeys=json_data.get("QueryStringCacheKeys"),
            Cookies=json_data.get("Cookies"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardedValues = ForwardedValues


@dataclass
class Cookies:
    Forward: Optional[str]
    WhitelistedNames: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Cookies"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cookies"]:
        if not json_data:
            return None
        return cls(
            Forward=json_data.get("Forward"),
            WhitelistedNames=json_data.get("WhitelistedNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cookies = Cookies


@dataclass
class LambdaFunctionAssociation:
    EventType: Optional[str]
    IncludeBody: Optional[bool]
    LambdaArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaFunctionAssociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaFunctionAssociation"]:
        if not json_data:
            return None
        return cls(
            EventType=json_data.get("EventType"),
            IncludeBody=json_data.get("IncludeBody"),
            LambdaArn=json_data.get("LambdaArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaFunctionAssociation = LambdaFunctionAssociation


@dataclass
class CustomErrorResponse:
    ErrorCachingMinTtl: Optional[float]
    ErrorCode: Optional[float]
    ResponseCode: Optional[float]
    ResponsePagePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomErrorResponse"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomErrorResponse"]:
        if not json_data:
            return None
        return cls(
            ErrorCachingMinTtl=json_data.get("ErrorCachingMinTtl"),
            ErrorCode=json_data.get("ErrorCode"),
            ResponseCode=json_data.get("ResponseCode"),
            ResponsePagePath=json_data.get("ResponsePagePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomErrorResponse = CustomErrorResponse


@dataclass
class DefaultCacheBehavior:
    AllowedMethods: Optional[Sequence[str]]
    CachedMethods: Optional[Sequence[str]]
    Compress: Optional[bool]
    DefaultTtl: Optional[float]
    FieldLevelEncryptionId: Optional[str]
    MaxTtl: Optional[float]
    MinTtl: Optional[float]
    SmoothStreaming: Optional[bool]
    TargetOriginId: Optional[str]
    TrustedSigners: Optional[Sequence[str]]
    ViewerProtocolPolicy: Optional[str]
    ForwardedValues: Optional[Sequence["_ForwardedValues"]]
    LambdaFunctionAssociation: Optional[Sequence["_LambdaFunctionAssociation"]]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultCacheBehavior"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultCacheBehavior"]:
        if not json_data:
            return None
        return cls(
            AllowedMethods=json_data.get("AllowedMethods"),
            CachedMethods=json_data.get("CachedMethods"),
            Compress=json_data.get("Compress"),
            DefaultTtl=json_data.get("DefaultTtl"),
            FieldLevelEncryptionId=json_data.get("FieldLevelEncryptionId"),
            MaxTtl=json_data.get("MaxTtl"),
            MinTtl=json_data.get("MinTtl"),
            SmoothStreaming=json_data.get("SmoothStreaming"),
            TargetOriginId=json_data.get("TargetOriginId"),
            TrustedSigners=json_data.get("TrustedSigners"),
            ViewerProtocolPolicy=json_data.get("ViewerProtocolPolicy"),
            ForwardedValues=json_data.get("ForwardedValues"),
            LambdaFunctionAssociation=json_data.get("LambdaFunctionAssociation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultCacheBehavior = DefaultCacheBehavior


@dataclass
class LoggingConfig:
    Bucket: Optional[str]
    IncludeCookies: Optional[bool]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingConfig"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            IncludeCookies=json_data.get("IncludeCookies"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingConfig = LoggingConfig


@dataclass
class OrderedCacheBehavior:
    AllowedMethods: Optional[Sequence[str]]
    CachedMethods: Optional[Sequence[str]]
    Compress: Optional[bool]
    DefaultTtl: Optional[float]
    FieldLevelEncryptionId: Optional[str]
    MaxTtl: Optional[float]
    MinTtl: Optional[float]
    PathPattern: Optional[str]
    SmoothStreaming: Optional[bool]
    TargetOriginId: Optional[str]
    TrustedSigners: Optional[Sequence[str]]
    ViewerProtocolPolicy: Optional[str]
    ForwardedValues: Optional[Sequence["_ForwardedValues"]]
    LambdaFunctionAssociation: Optional[Sequence["_LambdaFunctionAssociation"]]

    @classmethod
    def _deserialize(
        cls: Type["_OrderedCacheBehavior"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrderedCacheBehavior"]:
        if not json_data:
            return None
        return cls(
            AllowedMethods=json_data.get("AllowedMethods"),
            CachedMethods=json_data.get("CachedMethods"),
            Compress=json_data.get("Compress"),
            DefaultTtl=json_data.get("DefaultTtl"),
            FieldLevelEncryptionId=json_data.get("FieldLevelEncryptionId"),
            MaxTtl=json_data.get("MaxTtl"),
            MinTtl=json_data.get("MinTtl"),
            PathPattern=json_data.get("PathPattern"),
            SmoothStreaming=json_data.get("SmoothStreaming"),
            TargetOriginId=json_data.get("TargetOriginId"),
            TrustedSigners=json_data.get("TrustedSigners"),
            ViewerProtocolPolicy=json_data.get("ViewerProtocolPolicy"),
            ForwardedValues=json_data.get("ForwardedValues"),
            LambdaFunctionAssociation=json_data.get("LambdaFunctionAssociation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrderedCacheBehavior = OrderedCacheBehavior


@dataclass
class Origin:
    DomainName: Optional[str]
    OriginId: Optional[str]
    OriginPath: Optional[str]
    CustomHeader: Optional[Sequence["_CustomHeader"]]
    CustomOriginConfig: Optional[Sequence["_CustomOriginConfig"]]
    S3OriginConfig: Optional[Sequence["_S3OriginConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_Origin"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Origin"]:
        if not json_data:
            return None
        return cls(
            DomainName=json_data.get("DomainName"),
            OriginId=json_data.get("OriginId"),
            OriginPath=json_data.get("OriginPath"),
            CustomHeader=json_data.get("CustomHeader"),
            CustomOriginConfig=json_data.get("CustomOriginConfig"),
            S3OriginConfig=json_data.get("S3OriginConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Origin = Origin


@dataclass
class CustomHeader:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomHeader"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomHeader = CustomHeader


@dataclass
class CustomOriginConfig:
    HttpPort: Optional[float]
    HttpsPort: Optional[float]
    OriginKeepaliveTimeout: Optional[float]
    OriginProtocolPolicy: Optional[str]
    OriginReadTimeout: Optional[float]
    OriginSslProtocols: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomOriginConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomOriginConfig"]:
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
_CustomOriginConfig = CustomOriginConfig


@dataclass
class S3OriginConfig:
    OriginAccessIdentity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3OriginConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3OriginConfig"]:
        if not json_data:
            return None
        return cls(
            OriginAccessIdentity=json_data.get("OriginAccessIdentity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3OriginConfig = S3OriginConfig


@dataclass
class OriginGroup:
    OriginId: Optional[str]
    FailoverCriteria: Optional[Sequence["_FailoverCriteria"]]
    Member: Optional[Sequence["_Member"]]

    @classmethod
    def _deserialize(
        cls: Type["_OriginGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginGroup"]:
        if not json_data:
            return None
        return cls(
            OriginId=json_data.get("OriginId"),
            FailoverCriteria=json_data.get("FailoverCriteria"),
            Member=json_data.get("Member"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginGroup = OriginGroup


@dataclass
class FailoverCriteria:
    StatusCodes: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_FailoverCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailoverCriteria"]:
        if not json_data:
            return None
        return cls(
            StatusCodes=json_data.get("StatusCodes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailoverCriteria = FailoverCriteria


@dataclass
class Member:
    OriginId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Member"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Member"]:
        if not json_data:
            return None
        return cls(
            OriginId=json_data.get("OriginId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Member = Member


@dataclass
class Restrictions:
    GeoRestriction: Optional[Sequence["_GeoRestriction"]]

    @classmethod
    def _deserialize(
        cls: Type["_Restrictions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Restrictions"]:
        if not json_data:
            return None
        return cls(
            GeoRestriction=json_data.get("GeoRestriction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Restrictions = Restrictions


@dataclass
class GeoRestriction:
    Locations: Optional[Sequence[str]]
    RestrictionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeoRestriction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoRestriction"]:
        if not json_data:
            return None
        return cls(
            Locations=json_data.get("Locations"),
            RestrictionType=json_data.get("RestrictionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoRestriction = GeoRestriction


@dataclass
class ViewerCertificate:
    AcmCertificateArn: Optional[str]
    CloudfrontDefaultCertificate: Optional[bool]
    IamCertificateId: Optional[str]
    MinimumProtocolVersion: Optional[str]
    SslSupportMethod: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ViewerCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ViewerCertificate"]:
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
_ViewerCertificate = ViewerCertificate


