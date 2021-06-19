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
    Activate: Optional[bool]
    ActiveVersion: Optional[float]
    ClonedVersion: Optional[float]
    Comment: Optional[str]
    DefaultHost: Optional[str]
    DefaultTtl: Optional[float]
    ForceDestroy: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    VersionComment: Optional[str]
    Acl: Optional[Sequence["_AclDefinition"]]
    Backend: Optional[Sequence["_BackendDefinition"]]
    Bigquerylogging: Optional[Sequence["_BigqueryloggingDefinition"]]
    Blobstoragelogging: Optional[Sequence["_BlobstorageloggingDefinition"]]
    CacheSetting: Optional[Sequence["_CacheSettingDefinition"]]
    Condition: Optional[Sequence["_ConditionDefinition"]]
    Dictionary: Optional[Sequence["_DictionaryDefinition"]]
    Director: Optional[Sequence["_DirectorDefinition"]]
    Domain: Optional[Sequence["_DomainDefinition"]]
    Dynamicsnippet: Optional[Sequence["_DynamicsnippetDefinition"]]
    Gcslogging: Optional[Sequence["_GcsloggingDefinition"]]
    Gzip: Optional[Sequence["_GzipDefinition"]]
    Header: Optional[Sequence["_HeaderDefinition"]]
    Healthcheck: Optional[Sequence["_HealthcheckDefinition"]]
    Httpslogging: Optional[Sequence["_HttpsloggingDefinition"]]
    Logentries: Optional[Sequence["_LogentriesDefinition"]]
    LoggingCloudfiles: Optional[Sequence["_LoggingCloudfilesDefinition"]]
    LoggingDatadog: Optional[Sequence["_LoggingDatadogDefinition"]]
    LoggingDigitalocean: Optional[Sequence["_LoggingDigitaloceanDefinition"]]
    LoggingElasticsearch: Optional[Sequence["_LoggingElasticsearchDefinition"]]
    LoggingFtp: Optional[Sequence["_LoggingFtpDefinition"]]
    LoggingGooglepubsub: Optional[Sequence["_LoggingGooglepubsubDefinition"]]
    LoggingHeroku: Optional[Sequence["_LoggingHerokuDefinition"]]
    LoggingHoneycomb: Optional[Sequence["_LoggingHoneycombDefinition"]]
    LoggingKafka: Optional[Sequence["_LoggingKafkaDefinition"]]
    LoggingKinesis: Optional[Sequence["_LoggingKinesisDefinition"]]
    LoggingLoggly: Optional[Sequence["_LoggingLogglyDefinition"]]
    LoggingLogshuttle: Optional[Sequence["_LoggingLogshuttleDefinition"]]
    LoggingNewrelic: Optional[Sequence["_LoggingNewrelicDefinition"]]
    LoggingOpenstack: Optional[Sequence["_LoggingOpenstackDefinition"]]
    LoggingScalyr: Optional[Sequence["_LoggingScalyrDefinition"]]
    LoggingSftp: Optional[Sequence["_LoggingSftpDefinition"]]
    Papertrail: Optional[Sequence["_PapertrailDefinition"]]
    RequestSetting: Optional[Sequence["_RequestSettingDefinition"]]
    ResponseObject: Optional[Sequence["_ResponseObjectDefinition"]]
    S3logging: Optional[Sequence["_S3loggingDefinition"]]
    Snippet: Optional[Sequence["_SnippetDefinition"]]
    Splunk: Optional[Sequence["_SplunkDefinition"]]
    Sumologic: Optional[Sequence["_SumologicDefinition"]]
    Syslog: Optional[Sequence["_SyslogDefinition"]]
    Vcl: Optional[Sequence["_VclDefinition"]]
    Waf: Optional[Sequence["_WafDefinition"]]

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
            Activate=json_data.get("Activate"),
            ActiveVersion=json_data.get("ActiveVersion"),
            ClonedVersion=json_data.get("ClonedVersion"),
            Comment=json_data.get("Comment"),
            DefaultHost=json_data.get("DefaultHost"),
            DefaultTtl=json_data.get("DefaultTtl"),
            ForceDestroy=json_data.get("ForceDestroy"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            VersionComment=json_data.get("VersionComment"),
            Acl=deserialize_list(json_data.get("Acl"), AclDefinition),
            Backend=deserialize_list(json_data.get("Backend"), BackendDefinition),
            Bigquerylogging=deserialize_list(json_data.get("Bigquerylogging"), BigqueryloggingDefinition),
            Blobstoragelogging=deserialize_list(json_data.get("Blobstoragelogging"), BlobstorageloggingDefinition),
            CacheSetting=deserialize_list(json_data.get("CacheSetting"), CacheSettingDefinition),
            Condition=deserialize_list(json_data.get("Condition"), ConditionDefinition),
            Dictionary=deserialize_list(json_data.get("Dictionary"), DictionaryDefinition),
            Director=deserialize_list(json_data.get("Director"), DirectorDefinition),
            Domain=deserialize_list(json_data.get("Domain"), DomainDefinition),
            Dynamicsnippet=deserialize_list(json_data.get("Dynamicsnippet"), DynamicsnippetDefinition),
            Gcslogging=deserialize_list(json_data.get("Gcslogging"), GcsloggingDefinition),
            Gzip=deserialize_list(json_data.get("Gzip"), GzipDefinition),
            Header=deserialize_list(json_data.get("Header"), HeaderDefinition),
            Healthcheck=deserialize_list(json_data.get("Healthcheck"), HealthcheckDefinition),
            Httpslogging=deserialize_list(json_data.get("Httpslogging"), HttpsloggingDefinition),
            Logentries=deserialize_list(json_data.get("Logentries"), LogentriesDefinition),
            LoggingCloudfiles=deserialize_list(json_data.get("LoggingCloudfiles"), LoggingCloudfilesDefinition),
            LoggingDatadog=deserialize_list(json_data.get("LoggingDatadog"), LoggingDatadogDefinition),
            LoggingDigitalocean=deserialize_list(json_data.get("LoggingDigitalocean"), LoggingDigitaloceanDefinition),
            LoggingElasticsearch=deserialize_list(json_data.get("LoggingElasticsearch"), LoggingElasticsearchDefinition),
            LoggingFtp=deserialize_list(json_data.get("LoggingFtp"), LoggingFtpDefinition),
            LoggingGooglepubsub=deserialize_list(json_data.get("LoggingGooglepubsub"), LoggingGooglepubsubDefinition),
            LoggingHeroku=deserialize_list(json_data.get("LoggingHeroku"), LoggingHerokuDefinition),
            LoggingHoneycomb=deserialize_list(json_data.get("LoggingHoneycomb"), LoggingHoneycombDefinition),
            LoggingKafka=deserialize_list(json_data.get("LoggingKafka"), LoggingKafkaDefinition),
            LoggingKinesis=deserialize_list(json_data.get("LoggingKinesis"), LoggingKinesisDefinition),
            LoggingLoggly=deserialize_list(json_data.get("LoggingLoggly"), LoggingLogglyDefinition),
            LoggingLogshuttle=deserialize_list(json_data.get("LoggingLogshuttle"), LoggingLogshuttleDefinition),
            LoggingNewrelic=deserialize_list(json_data.get("LoggingNewrelic"), LoggingNewrelicDefinition),
            LoggingOpenstack=deserialize_list(json_data.get("LoggingOpenstack"), LoggingOpenstackDefinition),
            LoggingScalyr=deserialize_list(json_data.get("LoggingScalyr"), LoggingScalyrDefinition),
            LoggingSftp=deserialize_list(json_data.get("LoggingSftp"), LoggingSftpDefinition),
            Papertrail=deserialize_list(json_data.get("Papertrail"), PapertrailDefinition),
            RequestSetting=deserialize_list(json_data.get("RequestSetting"), RequestSettingDefinition),
            ResponseObject=deserialize_list(json_data.get("ResponseObject"), ResponseObjectDefinition),
            S3logging=deserialize_list(json_data.get("S3logging"), S3loggingDefinition),
            Snippet=deserialize_list(json_data.get("Snippet"), SnippetDefinition),
            Splunk=deserialize_list(json_data.get("Splunk"), SplunkDefinition),
            Sumologic=deserialize_list(json_data.get("Sumologic"), SumologicDefinition),
            Syslog=deserialize_list(json_data.get("Syslog"), SyslogDefinition),
            Vcl=deserialize_list(json_data.get("Vcl"), VclDefinition),
            Waf=deserialize_list(json_data.get("Waf"), WafDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AclDefinition(BaseModel):
    ForceDestroy: Optional[bool]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AclDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AclDefinition"]:
        if not json_data:
            return None
        return cls(
            ForceDestroy=json_data.get("ForceDestroy"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AclDefinition = AclDefinition


@dataclass
class BackendDefinition(BaseModel):
    Address: Optional[str]
    AutoLoadbalance: Optional[bool]
    BetweenBytesTimeout: Optional[float]
    ConnectTimeout: Optional[float]
    ErrorThreshold: Optional[float]
    FirstByteTimeout: Optional[float]
    Healthcheck: Optional[str]
    MaxConn: Optional[float]
    MaxTlsVersion: Optional[str]
    MinTlsVersion: Optional[str]
    Name: Optional[str]
    OverrideHost: Optional[str]
    Port: Optional[float]
    RequestCondition: Optional[str]
    Shield: Optional[str]
    SslCaCert: Optional[str]
    SslCertHostname: Optional[str]
    SslCheckCert: Optional[bool]
    SslCiphers: Optional[str]
    SslClientCert: Optional[str]
    SslClientKey: Optional[str]
    SslHostname: Optional[str]
    SslSniHostname: Optional[str]
    UseSsl: Optional[bool]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BackendDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            AutoLoadbalance=json_data.get("AutoLoadbalance"),
            BetweenBytesTimeout=json_data.get("BetweenBytesTimeout"),
            ConnectTimeout=json_data.get("ConnectTimeout"),
            ErrorThreshold=json_data.get("ErrorThreshold"),
            FirstByteTimeout=json_data.get("FirstByteTimeout"),
            Healthcheck=json_data.get("Healthcheck"),
            MaxConn=json_data.get("MaxConn"),
            MaxTlsVersion=json_data.get("MaxTlsVersion"),
            MinTlsVersion=json_data.get("MinTlsVersion"),
            Name=json_data.get("Name"),
            OverrideHost=json_data.get("OverrideHost"),
            Port=json_data.get("Port"),
            RequestCondition=json_data.get("RequestCondition"),
            Shield=json_data.get("Shield"),
            SslCaCert=json_data.get("SslCaCert"),
            SslCertHostname=json_data.get("SslCertHostname"),
            SslCheckCert=json_data.get("SslCheckCert"),
            SslCiphers=json_data.get("SslCiphers"),
            SslClientCert=json_data.get("SslClientCert"),
            SslClientKey=json_data.get("SslClientKey"),
            SslHostname=json_data.get("SslHostname"),
            SslSniHostname=json_data.get("SslSniHostname"),
            UseSsl=json_data.get("UseSsl"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendDefinition = BackendDefinition


@dataclass
class BigqueryloggingDefinition(BaseModel):
    Dataset: Optional[str]
    Email: Optional[str]
    Format: Optional[str]
    Name: Optional[str]
    Placement: Optional[str]
    ProjectId: Optional[str]
    ResponseCondition: Optional[str]
    SecretKey: Optional[str]
    Table: Optional[str]
    Template: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BigqueryloggingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BigqueryloggingDefinition"]:
        if not json_data:
            return None
        return cls(
            Dataset=json_data.get("Dataset"),
            Email=json_data.get("Email"),
            Format=json_data.get("Format"),
            Name=json_data.get("Name"),
            Placement=json_data.get("Placement"),
            ProjectId=json_data.get("ProjectId"),
            ResponseCondition=json_data.get("ResponseCondition"),
            SecretKey=json_data.get("SecretKey"),
            Table=json_data.get("Table"),
            Template=json_data.get("Template"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BigqueryloggingDefinition = BigqueryloggingDefinition


@dataclass
class BlobstorageloggingDefinition(BaseModel):
    AccountName: Optional[str]
    CompressionCodec: Optional[str]
    Container: Optional[str]
    FileMaxBytes: Optional[float]
    Format: Optional[str]
    FormatVersion: Optional[float]
    GzipLevel: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Period: Optional[float]
    Placement: Optional[str]
    PublicKey: Optional[str]
    ResponseCondition: Optional[str]
    SasToken: Optional[str]
    TimestampFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlobstorageloggingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlobstorageloggingDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountName=json_data.get("AccountName"),
            CompressionCodec=json_data.get("CompressionCodec"),
            Container=json_data.get("Container"),
            FileMaxBytes=json_data.get("FileMaxBytes"),
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            GzipLevel=json_data.get("GzipLevel"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Period=json_data.get("Period"),
            Placement=json_data.get("Placement"),
            PublicKey=json_data.get("PublicKey"),
            ResponseCondition=json_data.get("ResponseCondition"),
            SasToken=json_data.get("SasToken"),
            TimestampFormat=json_data.get("TimestampFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlobstorageloggingDefinition = BlobstorageloggingDefinition


@dataclass
class CacheSettingDefinition(BaseModel):
    Action: Optional[str]
    CacheCondition: Optional[str]
    Name: Optional[str]
    StaleTtl: Optional[float]
    Ttl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CacheSettingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheSettingDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            CacheCondition=json_data.get("CacheCondition"),
            Name=json_data.get("Name"),
            StaleTtl=json_data.get("StaleTtl"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheSettingDefinition = CacheSettingDefinition


@dataclass
class ConditionDefinition(BaseModel):
    Name: Optional[str]
    Priority: Optional[float]
    Statement: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Statement=json_data.get("Statement"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionDefinition = ConditionDefinition


@dataclass
class DictionaryDefinition(BaseModel):
    ForceDestroy: Optional[bool]
    Name: Optional[str]
    WriteOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DictionaryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DictionaryDefinition"]:
        if not json_data:
            return None
        return cls(
            ForceDestroy=json_data.get("ForceDestroy"),
            Name=json_data.get("Name"),
            WriteOnly=json_data.get("WriteOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DictionaryDefinition = DictionaryDefinition


@dataclass
class DirectorDefinition(BaseModel):
    Backends: Optional[Sequence[str]]
    Capacity: Optional[float]
    Comment: Optional[str]
    Name: Optional[str]
    Quorum: Optional[float]
    Retries: Optional[float]
    Shield: Optional[str]
    Type: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DirectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DirectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Backends=json_data.get("Backends"),
            Capacity=json_data.get("Capacity"),
            Comment=json_data.get("Comment"),
            Name=json_data.get("Name"),
            Quorum=json_data.get("Quorum"),
            Retries=json_data.get("Retries"),
            Shield=json_data.get("Shield"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DirectorDefinition = DirectorDefinition


@dataclass
class DomainDefinition(BaseModel):
    Comment: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainDefinition"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainDefinition = DomainDefinition


@dataclass
class DynamicsnippetDefinition(BaseModel):
    Name: Optional[str]
    Priority: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicsnippetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicsnippetDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicsnippetDefinition = DynamicsnippetDefinition


@dataclass
class GcsloggingDefinition(BaseModel):
    BucketName: Optional[str]
    CompressionCodec: Optional[str]
    Email: Optional[str]
    Format: Optional[str]
    GzipLevel: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Period: Optional[float]
    Placement: Optional[str]
    ResponseCondition: Optional[str]
    SecretKey: Optional[str]
    TimestampFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GcsloggingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcsloggingDefinition"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            CompressionCodec=json_data.get("CompressionCodec"),
            Email=json_data.get("Email"),
            Format=json_data.get("Format"),
            GzipLevel=json_data.get("GzipLevel"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Period=json_data.get("Period"),
            Placement=json_data.get("Placement"),
            ResponseCondition=json_data.get("ResponseCondition"),
            SecretKey=json_data.get("SecretKey"),
            TimestampFormat=json_data.get("TimestampFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcsloggingDefinition = GcsloggingDefinition


@dataclass
class GzipDefinition(BaseModel):
    CacheCondition: Optional[str]
    ContentTypes: Optional[Sequence[str]]
    Extensions: Optional[Sequence[str]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GzipDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GzipDefinition"]:
        if not json_data:
            return None
        return cls(
            CacheCondition=json_data.get("CacheCondition"),
            ContentTypes=json_data.get("ContentTypes"),
            Extensions=json_data.get("Extensions"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GzipDefinition = GzipDefinition


@dataclass
class HeaderDefinition(BaseModel):
    Action: Optional[str]
    CacheCondition: Optional[str]
    Destination: Optional[str]
    IgnoreIfSet: Optional[bool]
    Name: Optional[str]
    Priority: Optional[float]
    Regex: Optional[str]
    RequestCondition: Optional[str]
    ResponseCondition: Optional[str]
    Source: Optional[str]
    Substitution: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            CacheCondition=json_data.get("CacheCondition"),
            Destination=json_data.get("Destination"),
            IgnoreIfSet=json_data.get("IgnoreIfSet"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Regex=json_data.get("Regex"),
            RequestCondition=json_data.get("RequestCondition"),
            ResponseCondition=json_data.get("ResponseCondition"),
            Source=json_data.get("Source"),
            Substitution=json_data.get("Substitution"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderDefinition = HeaderDefinition


@dataclass
class HealthcheckDefinition(BaseModel):
    CheckInterval: Optional[float]
    ExpectedResponse: Optional[float]
    Host: Optional[str]
    HttpVersion: Optional[str]
    Initial: Optional[float]
    Method: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Threshold: Optional[float]
    Timeout: Optional[float]
    Window: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthcheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthcheckDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckInterval=json_data.get("CheckInterval"),
            ExpectedResponse=json_data.get("ExpectedResponse"),
            Host=json_data.get("Host"),
            HttpVersion=json_data.get("HttpVersion"),
            Initial=json_data.get("Initial"),
            Method=json_data.get("Method"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Threshold=json_data.get("Threshold"),
            Timeout=json_data.get("Timeout"),
            Window=json_data.get("Window"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthcheckDefinition = HealthcheckDefinition


@dataclass
class HttpsloggingDefinition(BaseModel):
    ContentType: Optional[str]
    Format: Optional[str]
    FormatVersion: Optional[float]
    HeaderName: Optional[str]
    HeaderValue: Optional[str]
    JsonFormat: Optional[str]
    MessageType: Optional[str]
    Method: Optional[str]
    Name: Optional[str]
    Placement: Optional[str]
    RequestMaxBytes: Optional[float]
    RequestMaxEntries: Optional[float]
    ResponseCondition: Optional[str]
    TlsCaCert: Optional[str]
    TlsClientCert: Optional[str]
    TlsClientKey: Optional[str]
    TlsHostname: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpsloggingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpsloggingDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentType=json_data.get("ContentType"),
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            HeaderName=json_data.get("HeaderName"),
            HeaderValue=json_data.get("HeaderValue"),
            JsonFormat=json_data.get("JsonFormat"),
            MessageType=json_data.get("MessageType"),
            Method=json_data.get("Method"),
            Name=json_data.get("Name"),
            Placement=json_data.get("Placement"),
            RequestMaxBytes=json_data.get("RequestMaxBytes"),
            RequestMaxEntries=json_data.get("RequestMaxEntries"),
            ResponseCondition=json_data.get("ResponseCondition"),
            TlsCaCert=json_data.get("TlsCaCert"),
            TlsClientCert=json_data.get("TlsClientCert"),
            TlsClientKey=json_data.get("TlsClientKey"),
            TlsHostname=json_data.get("TlsHostname"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpsloggingDefinition = HttpsloggingDefinition


@dataclass
class LogentriesDefinition(BaseModel):
    Format: Optional[str]
    FormatVersion: Optional[float]
    Name: Optional[str]
    Placement: Optional[str]
    Port: Optional[float]
    ResponseCondition: Optional[str]
    Token: Optional[str]
    UseTls: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_LogentriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogentriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            Name=json_data.get("Name"),
            Placement=json_data.get("Placement"),
            Port=json_data.get("Port"),
            ResponseCondition=json_data.get("ResponseCondition"),
            Token=json_data.get("Token"),
            UseTls=json_data.get("UseTls"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogentriesDefinition = LogentriesDefinition


@dataclass
class LoggingCloudfilesDefinition(BaseModel):
    AccessKey: Optional[str]
    BucketName: Optional[str]
    CompressionCodec: Optional[str]
    Format: Optional[str]
    FormatVersion: Optional[float]
    GzipLevel: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Period: Optional[float]
    Placement: Optional[str]
    PublicKey: Optional[str]
    Region: Optional[str]
    ResponseCondition: Optional[str]
    TimestampFormat: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingCloudfilesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingCloudfilesDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            BucketName=json_data.get("BucketName"),
            CompressionCodec=json_data.get("CompressionCodec"),
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            GzipLevel=json_data.get("GzipLevel"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Period=json_data.get("Period"),
            Placement=json_data.get("Placement"),
            PublicKey=json_data.get("PublicKey"),
            Region=json_data.get("Region"),
            ResponseCondition=json_data.get("ResponseCondition"),
            TimestampFormat=json_data.get("TimestampFormat"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingCloudfilesDefinition = LoggingCloudfilesDefinition


@dataclass
class LoggingDatadogDefinition(BaseModel):
    Format: Optional[str]
    FormatVersion: Optional[float]
    Name: Optional[str]
    Placement: Optional[str]
    Region: Optional[str]
    ResponseCondition: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingDatadogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingDatadogDefinition"]:
        if not json_data:
            return None
        return cls(
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            Name=json_data.get("Name"),
            Placement=json_data.get("Placement"),
            Region=json_data.get("Region"),
            ResponseCondition=json_data.get("ResponseCondition"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingDatadogDefinition = LoggingDatadogDefinition


@dataclass
class LoggingDigitaloceanDefinition(BaseModel):
    AccessKey: Optional[str]
    BucketName: Optional[str]
    CompressionCodec: Optional[str]
    Domain: Optional[str]
    Format: Optional[str]
    FormatVersion: Optional[float]
    GzipLevel: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Period: Optional[float]
    Placement: Optional[str]
    PublicKey: Optional[str]
    ResponseCondition: Optional[str]
    SecretKey: Optional[str]
    TimestampFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingDigitaloceanDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingDigitaloceanDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            BucketName=json_data.get("BucketName"),
            CompressionCodec=json_data.get("CompressionCodec"),
            Domain=json_data.get("Domain"),
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            GzipLevel=json_data.get("GzipLevel"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Period=json_data.get("Period"),
            Placement=json_data.get("Placement"),
            PublicKey=json_data.get("PublicKey"),
            ResponseCondition=json_data.get("ResponseCondition"),
            SecretKey=json_data.get("SecretKey"),
            TimestampFormat=json_data.get("TimestampFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingDigitaloceanDefinition = LoggingDigitaloceanDefinition


@dataclass
class LoggingElasticsearchDefinition(BaseModel):
    Format: Optional[str]
    FormatVersion: Optional[float]
    Index: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Pipeline: Optional[str]
    Placement: Optional[str]
    RequestMaxBytes: Optional[float]
    RequestMaxEntries: Optional[float]
    ResponseCondition: Optional[str]
    TlsCaCert: Optional[str]
    TlsClientCert: Optional[str]
    TlsClientKey: Optional[str]
    TlsHostname: Optional[str]
    Url: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingElasticsearchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingElasticsearchDefinition"]:
        if not json_data:
            return None
        return cls(
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            Index=json_data.get("Index"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Pipeline=json_data.get("Pipeline"),
            Placement=json_data.get("Placement"),
            RequestMaxBytes=json_data.get("RequestMaxBytes"),
            RequestMaxEntries=json_data.get("RequestMaxEntries"),
            ResponseCondition=json_data.get("ResponseCondition"),
            TlsCaCert=json_data.get("TlsCaCert"),
            TlsClientCert=json_data.get("TlsClientCert"),
            TlsClientKey=json_data.get("TlsClientKey"),
            TlsHostname=json_data.get("TlsHostname"),
            Url=json_data.get("Url"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingElasticsearchDefinition = LoggingElasticsearchDefinition


@dataclass
class LoggingFtpDefinition(BaseModel):
    Address: Optional[str]
    CompressionCodec: Optional[str]
    Format: Optional[str]
    FormatVersion: Optional[float]
    GzipLevel: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Path: Optional[str]
    Period: Optional[float]
    Placement: Optional[str]
    Port: Optional[float]
    PublicKey: Optional[str]
    ResponseCondition: Optional[str]
    TimestampFormat: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingFtpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingFtpDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            CompressionCodec=json_data.get("CompressionCodec"),
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            GzipLevel=json_data.get("GzipLevel"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Path=json_data.get("Path"),
            Period=json_data.get("Period"),
            Placement=json_data.get("Placement"),
            Port=json_data.get("Port"),
            PublicKey=json_data.get("PublicKey"),
            ResponseCondition=json_data.get("ResponseCondition"),
            TimestampFormat=json_data.get("TimestampFormat"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingFtpDefinition = LoggingFtpDefinition


@dataclass
class LoggingGooglepubsubDefinition(BaseModel):
    Format: Optional[str]
    FormatVersion: Optional[float]
    Name: Optional[str]
    Placement: Optional[str]
    ProjectId: Optional[str]
    ResponseCondition: Optional[str]
    SecretKey: Optional[str]
    Topic: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingGooglepubsubDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingGooglepubsubDefinition"]:
        if not json_data:
            return None
        return cls(
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            Name=json_data.get("Name"),
            Placement=json_data.get("Placement"),
            ProjectId=json_data.get("ProjectId"),
            ResponseCondition=json_data.get("ResponseCondition"),
            SecretKey=json_data.get("SecretKey"),
            Topic=json_data.get("Topic"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingGooglepubsubDefinition = LoggingGooglepubsubDefinition


@dataclass
class LoggingHerokuDefinition(BaseModel):
    Format: Optional[str]
    FormatVersion: Optional[float]
    Name: Optional[str]
    Placement: Optional[str]
    ResponseCondition: Optional[str]
    Token: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingHerokuDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingHerokuDefinition"]:
        if not json_data:
            return None
        return cls(
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            Name=json_data.get("Name"),
            Placement=json_data.get("Placement"),
            ResponseCondition=json_data.get("ResponseCondition"),
            Token=json_data.get("Token"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingHerokuDefinition = LoggingHerokuDefinition


@dataclass
class LoggingHoneycombDefinition(BaseModel):
    Dataset: Optional[str]
    Format: Optional[str]
    FormatVersion: Optional[float]
    Name: Optional[str]
    Placement: Optional[str]
    ResponseCondition: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingHoneycombDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingHoneycombDefinition"]:
        if not json_data:
            return None
        return cls(
            Dataset=json_data.get("Dataset"),
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            Name=json_data.get("Name"),
            Placement=json_data.get("Placement"),
            ResponseCondition=json_data.get("ResponseCondition"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingHoneycombDefinition = LoggingHoneycombDefinition


@dataclass
class LoggingKafkaDefinition(BaseModel):
    AuthMethod: Optional[str]
    Brokers: Optional[str]
    CompressionCodec: Optional[str]
    Format: Optional[str]
    FormatVersion: Optional[float]
    Name: Optional[str]
    ParseLogKeyvals: Optional[bool]
    Password: Optional[str]
    Placement: Optional[str]
    RequestMaxBytes: Optional[float]
    RequiredAcks: Optional[str]
    ResponseCondition: Optional[str]
    TlsCaCert: Optional[str]
    TlsClientCert: Optional[str]
    TlsClientKey: Optional[str]
    TlsHostname: Optional[str]
    Topic: Optional[str]
    UseTls: Optional[bool]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingKafkaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingKafkaDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthMethod=json_data.get("AuthMethod"),
            Brokers=json_data.get("Brokers"),
            CompressionCodec=json_data.get("CompressionCodec"),
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            Name=json_data.get("Name"),
            ParseLogKeyvals=json_data.get("ParseLogKeyvals"),
            Password=json_data.get("Password"),
            Placement=json_data.get("Placement"),
            RequestMaxBytes=json_data.get("RequestMaxBytes"),
            RequiredAcks=json_data.get("RequiredAcks"),
            ResponseCondition=json_data.get("ResponseCondition"),
            TlsCaCert=json_data.get("TlsCaCert"),
            TlsClientCert=json_data.get("TlsClientCert"),
            TlsClientKey=json_data.get("TlsClientKey"),
            TlsHostname=json_data.get("TlsHostname"),
            Topic=json_data.get("Topic"),
            UseTls=json_data.get("UseTls"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingKafkaDefinition = LoggingKafkaDefinition


@dataclass
class LoggingKinesisDefinition(BaseModel):
    AccessKey: Optional[str]
    Format: Optional[str]
    FormatVersion: Optional[float]
    IamRole: Optional[str]
    Name: Optional[str]
    Placement: Optional[str]
    Region: Optional[str]
    ResponseCondition: Optional[str]
    SecretKey: Optional[str]
    Topic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingKinesisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingKinesisDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            IamRole=json_data.get("IamRole"),
            Name=json_data.get("Name"),
            Placement=json_data.get("Placement"),
            Region=json_data.get("Region"),
            ResponseCondition=json_data.get("ResponseCondition"),
            SecretKey=json_data.get("SecretKey"),
            Topic=json_data.get("Topic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingKinesisDefinition = LoggingKinesisDefinition


@dataclass
class LoggingLogglyDefinition(BaseModel):
    Format: Optional[str]
    FormatVersion: Optional[float]
    Name: Optional[str]
    Placement: Optional[str]
    ResponseCondition: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingLogglyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingLogglyDefinition"]:
        if not json_data:
            return None
        return cls(
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            Name=json_data.get("Name"),
            Placement=json_data.get("Placement"),
            ResponseCondition=json_data.get("ResponseCondition"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingLogglyDefinition = LoggingLogglyDefinition


@dataclass
class LoggingLogshuttleDefinition(BaseModel):
    Format: Optional[str]
    FormatVersion: Optional[float]
    Name: Optional[str]
    Placement: Optional[str]
    ResponseCondition: Optional[str]
    Token: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingLogshuttleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingLogshuttleDefinition"]:
        if not json_data:
            return None
        return cls(
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            Name=json_data.get("Name"),
            Placement=json_data.get("Placement"),
            ResponseCondition=json_data.get("ResponseCondition"),
            Token=json_data.get("Token"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingLogshuttleDefinition = LoggingLogshuttleDefinition


@dataclass
class LoggingNewrelicDefinition(BaseModel):
    Format: Optional[str]
    FormatVersion: Optional[float]
    Name: Optional[str]
    Placement: Optional[str]
    ResponseCondition: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingNewrelicDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingNewrelicDefinition"]:
        if not json_data:
            return None
        return cls(
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            Name=json_data.get("Name"),
            Placement=json_data.get("Placement"),
            ResponseCondition=json_data.get("ResponseCondition"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingNewrelicDefinition = LoggingNewrelicDefinition


@dataclass
class LoggingOpenstackDefinition(BaseModel):
    AccessKey: Optional[str]
    BucketName: Optional[str]
    CompressionCodec: Optional[str]
    Format: Optional[str]
    FormatVersion: Optional[float]
    GzipLevel: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Period: Optional[float]
    Placement: Optional[str]
    PublicKey: Optional[str]
    ResponseCondition: Optional[str]
    TimestampFormat: Optional[str]
    Url: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingOpenstackDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingOpenstackDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            BucketName=json_data.get("BucketName"),
            CompressionCodec=json_data.get("CompressionCodec"),
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            GzipLevel=json_data.get("GzipLevel"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Period=json_data.get("Period"),
            Placement=json_data.get("Placement"),
            PublicKey=json_data.get("PublicKey"),
            ResponseCondition=json_data.get("ResponseCondition"),
            TimestampFormat=json_data.get("TimestampFormat"),
            Url=json_data.get("Url"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingOpenstackDefinition = LoggingOpenstackDefinition


@dataclass
class LoggingScalyrDefinition(BaseModel):
    Format: Optional[str]
    FormatVersion: Optional[float]
    Name: Optional[str]
    Placement: Optional[str]
    Region: Optional[str]
    ResponseCondition: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingScalyrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingScalyrDefinition"]:
        if not json_data:
            return None
        return cls(
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            Name=json_data.get("Name"),
            Placement=json_data.get("Placement"),
            Region=json_data.get("Region"),
            ResponseCondition=json_data.get("ResponseCondition"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingScalyrDefinition = LoggingScalyrDefinition


@dataclass
class LoggingSftpDefinition(BaseModel):
    Address: Optional[str]
    CompressionCodec: Optional[str]
    Format: Optional[str]
    FormatVersion: Optional[float]
    GzipLevel: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Path: Optional[str]
    Period: Optional[float]
    Placement: Optional[str]
    Port: Optional[float]
    PublicKey: Optional[str]
    ResponseCondition: Optional[str]
    SecretKey: Optional[str]
    SshKnownHosts: Optional[str]
    TimestampFormat: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingSftpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingSftpDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            CompressionCodec=json_data.get("CompressionCodec"),
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            GzipLevel=json_data.get("GzipLevel"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Path=json_data.get("Path"),
            Period=json_data.get("Period"),
            Placement=json_data.get("Placement"),
            Port=json_data.get("Port"),
            PublicKey=json_data.get("PublicKey"),
            ResponseCondition=json_data.get("ResponseCondition"),
            SecretKey=json_data.get("SecretKey"),
            SshKnownHosts=json_data.get("SshKnownHosts"),
            TimestampFormat=json_data.get("TimestampFormat"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingSftpDefinition = LoggingSftpDefinition


@dataclass
class PapertrailDefinition(BaseModel):
    Address: Optional[str]
    Format: Optional[str]
    FormatVersion: Optional[float]
    Name: Optional[str]
    Placement: Optional[str]
    Port: Optional[float]
    ResponseCondition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PapertrailDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PapertrailDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            Name=json_data.get("Name"),
            Placement=json_data.get("Placement"),
            Port=json_data.get("Port"),
            ResponseCondition=json_data.get("ResponseCondition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PapertrailDefinition = PapertrailDefinition


@dataclass
class RequestSettingDefinition(BaseModel):
    Action: Optional[str]
    BypassBusyWait: Optional[bool]
    DefaultHost: Optional[str]
    ForceMiss: Optional[bool]
    ForceSsl: Optional[bool]
    GeoHeaders: Optional[bool]
    HashKeys: Optional[str]
    MaxStaleAge: Optional[float]
    Name: Optional[str]
    RequestCondition: Optional[str]
    TimerSupport: Optional[bool]
    Xff: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestSettingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestSettingDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            BypassBusyWait=json_data.get("BypassBusyWait"),
            DefaultHost=json_data.get("DefaultHost"),
            ForceMiss=json_data.get("ForceMiss"),
            ForceSsl=json_data.get("ForceSsl"),
            GeoHeaders=json_data.get("GeoHeaders"),
            HashKeys=json_data.get("HashKeys"),
            MaxStaleAge=json_data.get("MaxStaleAge"),
            Name=json_data.get("Name"),
            RequestCondition=json_data.get("RequestCondition"),
            TimerSupport=json_data.get("TimerSupport"),
            Xff=json_data.get("Xff"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestSettingDefinition = RequestSettingDefinition


@dataclass
class ResponseObjectDefinition(BaseModel):
    CacheCondition: Optional[str]
    Content: Optional[str]
    ContentType: Optional[str]
    Name: Optional[str]
    RequestCondition: Optional[str]
    Response: Optional[str]
    Status: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseObjectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseObjectDefinition"]:
        if not json_data:
            return None
        return cls(
            CacheCondition=json_data.get("CacheCondition"),
            Content=json_data.get("Content"),
            ContentType=json_data.get("ContentType"),
            Name=json_data.get("Name"),
            RequestCondition=json_data.get("RequestCondition"),
            Response=json_data.get("Response"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseObjectDefinition = ResponseObjectDefinition


@dataclass
class S3loggingDefinition(BaseModel):
    Acl: Optional[str]
    BucketName: Optional[str]
    CompressionCodec: Optional[str]
    Domain: Optional[str]
    Format: Optional[str]
    FormatVersion: Optional[float]
    GzipLevel: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Period: Optional[float]
    Placement: Optional[str]
    PublicKey: Optional[str]
    Redundancy: Optional[str]
    ResponseCondition: Optional[str]
    S3AccessKey: Optional[str]
    S3IamRole: Optional[str]
    S3SecretKey: Optional[str]
    ServerSideEncryption: Optional[str]
    ServerSideEncryptionKmsKeyId: Optional[str]
    TimestampFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3loggingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3loggingDefinition"]:
        if not json_data:
            return None
        return cls(
            Acl=json_data.get("Acl"),
            BucketName=json_data.get("BucketName"),
            CompressionCodec=json_data.get("CompressionCodec"),
            Domain=json_data.get("Domain"),
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            GzipLevel=json_data.get("GzipLevel"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Period=json_data.get("Period"),
            Placement=json_data.get("Placement"),
            PublicKey=json_data.get("PublicKey"),
            Redundancy=json_data.get("Redundancy"),
            ResponseCondition=json_data.get("ResponseCondition"),
            S3AccessKey=json_data.get("S3AccessKey"),
            S3IamRole=json_data.get("S3IamRole"),
            S3SecretKey=json_data.get("S3SecretKey"),
            ServerSideEncryption=json_data.get("ServerSideEncryption"),
            ServerSideEncryptionKmsKeyId=json_data.get("ServerSideEncryptionKmsKeyId"),
            TimestampFormat=json_data.get("TimestampFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3loggingDefinition = S3loggingDefinition


@dataclass
class SnippetDefinition(BaseModel):
    Content: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnippetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnippetDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnippetDefinition = SnippetDefinition


@dataclass
class SplunkDefinition(BaseModel):
    Format: Optional[str]
    FormatVersion: Optional[float]
    Name: Optional[str]
    Placement: Optional[str]
    ResponseCondition: Optional[str]
    TlsCaCert: Optional[str]
    TlsClientCert: Optional[str]
    TlsClientKey: Optional[str]
    TlsHostname: Optional[str]
    Token: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SplunkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SplunkDefinition"]:
        if not json_data:
            return None
        return cls(
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            Name=json_data.get("Name"),
            Placement=json_data.get("Placement"),
            ResponseCondition=json_data.get("ResponseCondition"),
            TlsCaCert=json_data.get("TlsCaCert"),
            TlsClientCert=json_data.get("TlsClientCert"),
            TlsClientKey=json_data.get("TlsClientKey"),
            TlsHostname=json_data.get("TlsHostname"),
            Token=json_data.get("Token"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SplunkDefinition = SplunkDefinition


@dataclass
class SumologicDefinition(BaseModel):
    Format: Optional[str]
    FormatVersion: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Placement: Optional[str]
    ResponseCondition: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SumologicDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SumologicDefinition"]:
        if not json_data:
            return None
        return cls(
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Placement=json_data.get("Placement"),
            ResponseCondition=json_data.get("ResponseCondition"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SumologicDefinition = SumologicDefinition


@dataclass
class SyslogDefinition(BaseModel):
    Address: Optional[str]
    Format: Optional[str]
    FormatVersion: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Placement: Optional[str]
    Port: Optional[float]
    ResponseCondition: Optional[str]
    TlsCaCert: Optional[str]
    TlsClientCert: Optional[str]
    TlsClientKey: Optional[str]
    TlsHostname: Optional[str]
    Token: Optional[str]
    UseTls: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SyslogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SyslogDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Placement=json_data.get("Placement"),
            Port=json_data.get("Port"),
            ResponseCondition=json_data.get("ResponseCondition"),
            TlsCaCert=json_data.get("TlsCaCert"),
            TlsClientCert=json_data.get("TlsClientCert"),
            TlsClientKey=json_data.get("TlsClientKey"),
            TlsHostname=json_data.get("TlsHostname"),
            Token=json_data.get("Token"),
            UseTls=json_data.get("UseTls"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SyslogDefinition = SyslogDefinition


@dataclass
class VclDefinition(BaseModel):
    Content: Optional[str]
    Main: Optional[bool]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VclDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VclDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Main=json_data.get("Main"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VclDefinition = VclDefinition


@dataclass
class WafDefinition(BaseModel):
    Disabled: Optional[bool]
    PrefetchCondition: Optional[str]
    ResponseObject: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WafDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WafDefinition"]:
        if not json_data:
            return None
        return cls(
            Disabled=json_data.get("Disabled"),
            PrefetchCondition=json_data.get("PrefetchCondition"),
            ResponseObject=json_data.get("ResponseObject"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WafDefinition = WafDefinition


