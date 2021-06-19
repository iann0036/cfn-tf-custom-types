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
    ForceDestroy: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    VersionComment: Optional[str]
    Backend: Optional[Sequence["_BackendDefinition"]]
    Bigquerylogging: Optional[Sequence["_BigqueryloggingDefinition"]]
    Blobstoragelogging: Optional[Sequence["_BlobstorageloggingDefinition"]]
    Dictionary: Optional[Sequence["_DictionaryDefinition"]]
    Director: Optional[Sequence["_DirectorDefinition"]]
    Domain: Optional[Sequence["_DomainDefinition"]]
    Gcslogging: Optional[Sequence["_GcsloggingDefinition"]]
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
    Package: Optional[Sequence["_PackageDefinition"]]
    Papertrail: Optional[Sequence["_PapertrailDefinition"]]
    S3logging: Optional[Sequence["_S3loggingDefinition"]]
    Splunk: Optional[Sequence["_SplunkDefinition"]]
    Sumologic: Optional[Sequence["_SumologicDefinition"]]
    Syslog: Optional[Sequence["_SyslogDefinition"]]

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
            ForceDestroy=json_data.get("ForceDestroy"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            VersionComment=json_data.get("VersionComment"),
            Backend=deserialize_list(json_data.get("Backend"), BackendDefinition),
            Bigquerylogging=deserialize_list(json_data.get("Bigquerylogging"), BigqueryloggingDefinition),
            Blobstoragelogging=deserialize_list(json_data.get("Blobstoragelogging"), BlobstorageloggingDefinition),
            Dictionary=deserialize_list(json_data.get("Dictionary"), DictionaryDefinition),
            Director=deserialize_list(json_data.get("Director"), DirectorDefinition),
            Domain=deserialize_list(json_data.get("Domain"), DomainDefinition),
            Gcslogging=deserialize_list(json_data.get("Gcslogging"), GcsloggingDefinition),
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
            Package=deserialize_list(json_data.get("Package"), PackageDefinition),
            Papertrail=deserialize_list(json_data.get("Papertrail"), PapertrailDefinition),
            S3logging=deserialize_list(json_data.get("S3logging"), S3loggingDefinition),
            Splunk=deserialize_list(json_data.get("Splunk"), SplunkDefinition),
            Sumologic=deserialize_list(json_data.get("Sumologic"), SumologicDefinition),
            Syslog=deserialize_list(json_data.get("Syslog"), SyslogDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
    Name: Optional[str]
    ProjectId: Optional[str]
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
            Name=json_data.get("Name"),
            ProjectId=json_data.get("ProjectId"),
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
    GzipLevel: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Period: Optional[float]
    PublicKey: Optional[str]
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
            GzipLevel=json_data.get("GzipLevel"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Period=json_data.get("Period"),
            PublicKey=json_data.get("PublicKey"),
            SasToken=json_data.get("SasToken"),
            TimestampFormat=json_data.get("TimestampFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlobstorageloggingDefinition = BlobstorageloggingDefinition


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
class GcsloggingDefinition(BaseModel):
    BucketName: Optional[str]
    CompressionCodec: Optional[str]
    Email: Optional[str]
    GzipLevel: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Period: Optional[float]
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
            GzipLevel=json_data.get("GzipLevel"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Period=json_data.get("Period"),
            SecretKey=json_data.get("SecretKey"),
            TimestampFormat=json_data.get("TimestampFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcsloggingDefinition = GcsloggingDefinition


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
    HeaderName: Optional[str]
    HeaderValue: Optional[str]
    JsonFormat: Optional[str]
    MessageType: Optional[str]
    Method: Optional[str]
    Name: Optional[str]
    RequestMaxBytes: Optional[float]
    RequestMaxEntries: Optional[float]
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
            HeaderName=json_data.get("HeaderName"),
            HeaderValue=json_data.get("HeaderValue"),
            JsonFormat=json_data.get("JsonFormat"),
            MessageType=json_data.get("MessageType"),
            Method=json_data.get("Method"),
            Name=json_data.get("Name"),
            RequestMaxBytes=json_data.get("RequestMaxBytes"),
            RequestMaxEntries=json_data.get("RequestMaxEntries"),
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
    Name: Optional[str]
    Port: Optional[float]
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
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
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
    GzipLevel: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Period: Optional[float]
    PublicKey: Optional[str]
    Region: Optional[str]
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
            GzipLevel=json_data.get("GzipLevel"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Period=json_data.get("Period"),
            PublicKey=json_data.get("PublicKey"),
            Region=json_data.get("Region"),
            TimestampFormat=json_data.get("TimestampFormat"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingCloudfilesDefinition = LoggingCloudfilesDefinition


@dataclass
class LoggingDatadogDefinition(BaseModel):
    Name: Optional[str]
    Region: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingDatadogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingDatadogDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
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
    GzipLevel: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Period: Optional[float]
    PublicKey: Optional[str]
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
            GzipLevel=json_data.get("GzipLevel"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Period=json_data.get("Period"),
            PublicKey=json_data.get("PublicKey"),
            SecretKey=json_data.get("SecretKey"),
            TimestampFormat=json_data.get("TimestampFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingDigitaloceanDefinition = LoggingDigitaloceanDefinition


@dataclass
class LoggingElasticsearchDefinition(BaseModel):
    Index: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Pipeline: Optional[str]
    RequestMaxBytes: Optional[float]
    RequestMaxEntries: Optional[float]
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
            Index=json_data.get("Index"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Pipeline=json_data.get("Pipeline"),
            RequestMaxBytes=json_data.get("RequestMaxBytes"),
            RequestMaxEntries=json_data.get("RequestMaxEntries"),
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
    GzipLevel: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Path: Optional[str]
    Period: Optional[float]
    Port: Optional[float]
    PublicKey: Optional[str]
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
            GzipLevel=json_data.get("GzipLevel"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Path=json_data.get("Path"),
            Period=json_data.get("Period"),
            Port=json_data.get("Port"),
            PublicKey=json_data.get("PublicKey"),
            TimestampFormat=json_data.get("TimestampFormat"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingFtpDefinition = LoggingFtpDefinition


@dataclass
class LoggingGooglepubsubDefinition(BaseModel):
    Name: Optional[str]
    ProjectId: Optional[str]
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
            Name=json_data.get("Name"),
            ProjectId=json_data.get("ProjectId"),
            SecretKey=json_data.get("SecretKey"),
            Topic=json_data.get("Topic"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingGooglepubsubDefinition = LoggingGooglepubsubDefinition


@dataclass
class LoggingHerokuDefinition(BaseModel):
    Name: Optional[str]
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
            Name=json_data.get("Name"),
            Token=json_data.get("Token"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingHerokuDefinition = LoggingHerokuDefinition


@dataclass
class LoggingHoneycombDefinition(BaseModel):
    Dataset: Optional[str]
    Name: Optional[str]
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
            Name=json_data.get("Name"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingHoneycombDefinition = LoggingHoneycombDefinition


@dataclass
class LoggingKafkaDefinition(BaseModel):
    AuthMethod: Optional[str]
    Brokers: Optional[str]
    CompressionCodec: Optional[str]
    Name: Optional[str]
    ParseLogKeyvals: Optional[bool]
    Password: Optional[str]
    RequestMaxBytes: Optional[float]
    RequiredAcks: Optional[str]
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
            Name=json_data.get("Name"),
            ParseLogKeyvals=json_data.get("ParseLogKeyvals"),
            Password=json_data.get("Password"),
            RequestMaxBytes=json_data.get("RequestMaxBytes"),
            RequiredAcks=json_data.get("RequiredAcks"),
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
    IamRole: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
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
            IamRole=json_data.get("IamRole"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            SecretKey=json_data.get("SecretKey"),
            Topic=json_data.get("Topic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingKinesisDefinition = LoggingKinesisDefinition


@dataclass
class LoggingLogglyDefinition(BaseModel):
    Name: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingLogglyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingLogglyDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingLogglyDefinition = LoggingLogglyDefinition


@dataclass
class LoggingLogshuttleDefinition(BaseModel):
    Name: Optional[str]
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
            Name=json_data.get("Name"),
            Token=json_data.get("Token"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingLogshuttleDefinition = LoggingLogshuttleDefinition


@dataclass
class LoggingNewrelicDefinition(BaseModel):
    Name: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingNewrelicDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingNewrelicDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingNewrelicDefinition = LoggingNewrelicDefinition


@dataclass
class LoggingOpenstackDefinition(BaseModel):
    AccessKey: Optional[str]
    BucketName: Optional[str]
    CompressionCodec: Optional[str]
    GzipLevel: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Period: Optional[float]
    PublicKey: Optional[str]
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
            GzipLevel=json_data.get("GzipLevel"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Period=json_data.get("Period"),
            PublicKey=json_data.get("PublicKey"),
            TimestampFormat=json_data.get("TimestampFormat"),
            Url=json_data.get("Url"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingOpenstackDefinition = LoggingOpenstackDefinition


@dataclass
class LoggingScalyrDefinition(BaseModel):
    Name: Optional[str]
    Region: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingScalyrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingScalyrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingScalyrDefinition = LoggingScalyrDefinition


@dataclass
class LoggingSftpDefinition(BaseModel):
    Address: Optional[str]
    CompressionCodec: Optional[str]
    GzipLevel: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Path: Optional[str]
    Period: Optional[float]
    Port: Optional[float]
    PublicKey: Optional[str]
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
            GzipLevel=json_data.get("GzipLevel"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Path=json_data.get("Path"),
            Period=json_data.get("Period"),
            Port=json_data.get("Port"),
            PublicKey=json_data.get("PublicKey"),
            SecretKey=json_data.get("SecretKey"),
            SshKnownHosts=json_data.get("SshKnownHosts"),
            TimestampFormat=json_data.get("TimestampFormat"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingSftpDefinition = LoggingSftpDefinition


@dataclass
class PackageDefinition(BaseModel):
    Filename: Optional[str]
    SourceCodeHash: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PackageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PackageDefinition"]:
        if not json_data:
            return None
        return cls(
            Filename=json_data.get("Filename"),
            SourceCodeHash=json_data.get("SourceCodeHash"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PackageDefinition = PackageDefinition


@dataclass
class PapertrailDefinition(BaseModel):
    Address: Optional[str]
    Name: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PapertrailDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PapertrailDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PapertrailDefinition = PapertrailDefinition


@dataclass
class S3loggingDefinition(BaseModel):
    Acl: Optional[str]
    BucketName: Optional[str]
    CompressionCodec: Optional[str]
    Domain: Optional[str]
    GzipLevel: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Period: Optional[float]
    PublicKey: Optional[str]
    Redundancy: Optional[str]
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
            GzipLevel=json_data.get("GzipLevel"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Period=json_data.get("Period"),
            PublicKey=json_data.get("PublicKey"),
            Redundancy=json_data.get("Redundancy"),
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
class SplunkDefinition(BaseModel):
    Name: Optional[str]
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
            Name=json_data.get("Name"),
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
    MessageType: Optional[str]
    Name: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SumologicDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SumologicDefinition"]:
        if not json_data:
            return None
        return cls(
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SumologicDefinition = SumologicDefinition


@dataclass
class SyslogDefinition(BaseModel):
    Address: Optional[str]
    MessageType: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
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
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            TlsCaCert=json_data.get("TlsCaCert"),
            TlsClientCert=json_data.get("TlsClientCert"),
            TlsClientKey=json_data.get("TlsClientKey"),
            TlsHostname=json_data.get("TlsHostname"),
            Token=json_data.get("Token"),
            UseTls=json_data.get("UseTls"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SyslogDefinition = SyslogDefinition


