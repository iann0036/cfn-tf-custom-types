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
    Activate: Optional[bool]
    ActiveVersion: Optional[float]
    ClonedVersion: Optional[float]
    Comment: Optional[str]
    DefaultHost: Optional[str]
    DefaultTtl: Optional[float]
    ForceDestroy: Optional[bool]
    Name: Optional[str]
    VersionComment: Optional[str]
    Acl: Optional[Sequence["_Acl"]]
    Backend: Optional[Sequence["_Backend"]]
    Bigquerylogging: Optional[Sequence["_Bigquerylogging"]]
    Blobstoragelogging: Optional[Sequence["_Blobstoragelogging"]]
    CacheSetting: Optional[Sequence["_CacheSetting"]]
    Condition: Optional[Sequence["_Condition"]]
    Dictionary: Optional[Sequence["_Dictionary"]]
    Director: Optional[Sequence["_Director"]]
    Domain: Optional[Sequence["_Domain"]]
    Dynamicsnippet: Optional[Sequence["_Dynamicsnippet"]]
    Gcslogging: Optional[Sequence["_Gcslogging"]]
    Gzip: Optional[Sequence["_Gzip"]]
    Header: Optional[Sequence["_Header"]]
    Healthcheck: Optional[Sequence["_Healthcheck"]]
    Logentries: Optional[Sequence["_Logentries"]]
    Papertrail: Optional[Sequence["_Papertrail"]]
    RequestSetting: Optional[Sequence["_RequestSetting"]]
    ResponseObject: Optional[Sequence["_ResponseObject"]]
    S3logging: Optional[Sequence["_S3logging"]]
    Snippet: Optional[Sequence["_Snippet"]]
    Splunk: Optional[Sequence["_Splunk"]]
    Sumologic: Optional[Sequence["_Sumologic"]]
    Syslog: Optional[Sequence["_Syslog"]]
    Vcl: Optional[Sequence["_Vcl"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Activate=json_data.get("Activate"),
            ActiveVersion=json_data.get("ActiveVersion"),
            ClonedVersion=json_data.get("ClonedVersion"),
            Comment=json_data.get("Comment"),
            DefaultHost=json_data.get("DefaultHost"),
            DefaultTtl=json_data.get("DefaultTtl"),
            ForceDestroy=json_data.get("ForceDestroy"),
            Name=json_data.get("Name"),
            VersionComment=json_data.get("VersionComment"),
            Acl=json_data.get("Acl"),
            Backend=json_data.get("Backend"),
            Bigquerylogging=json_data.get("Bigquerylogging"),
            Blobstoragelogging=json_data.get("Blobstoragelogging"),
            CacheSetting=json_data.get("CacheSetting"),
            Condition=json_data.get("Condition"),
            Dictionary=json_data.get("Dictionary"),
            Director=json_data.get("Director"),
            Domain=json_data.get("Domain"),
            Dynamicsnippet=json_data.get("Dynamicsnippet"),
            Gcslogging=json_data.get("Gcslogging"),
            Gzip=json_data.get("Gzip"),
            Header=json_data.get("Header"),
            Healthcheck=json_data.get("Healthcheck"),
            Logentries=json_data.get("Logentries"),
            Papertrail=json_data.get("Papertrail"),
            RequestSetting=json_data.get("RequestSetting"),
            ResponseObject=json_data.get("ResponseObject"),
            S3logging=json_data.get("S3logging"),
            Snippet=json_data.get("Snippet"),
            Splunk=json_data.get("Splunk"),
            Sumologic=json_data.get("Sumologic"),
            Syslog=json_data.get("Syslog"),
            Vcl=json_data.get("Vcl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Acl:
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Acl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Acl"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Acl = Acl


@dataclass
class Backend:
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
        cls: Type["_Backend"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Backend"]:
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
_Backend = Backend


@dataclass
class Bigquerylogging:
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
        cls: Type["_Bigquerylogging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Bigquerylogging"]:
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
_Bigquerylogging = Bigquerylogging


@dataclass
class Blobstoragelogging:
    AccountName: Optional[str]
    Container: Optional[str]
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
        cls: Type["_Blobstoragelogging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Blobstoragelogging"]:
        if not json_data:
            return None
        return cls(
            AccountName=json_data.get("AccountName"),
            Container=json_data.get("Container"),
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
_Blobstoragelogging = Blobstoragelogging


@dataclass
class CacheSetting:
    Action: Optional[str]
    CacheCondition: Optional[str]
    Name: Optional[str]
    StaleTtl: Optional[float]
    Ttl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CacheSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheSetting"]:
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
_CacheSetting = CacheSetting


@dataclass
class Condition:
    Name: Optional[str]
    Priority: Optional[float]
    Statement: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Condition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Condition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Statement=json_data.get("Statement"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Condition = Condition


@dataclass
class Dictionary:
    Name: Optional[str]
    WriteOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Dictionary"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dictionary"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            WriteOnly=json_data.get("WriteOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dictionary = Dictionary


@dataclass
class Director:
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
        cls: Type["_Director"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Director"]:
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
_Director = Director


@dataclass
class Domain:
    Comment: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Domain"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Domain"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Domain = Domain


@dataclass
class Dynamicsnippet:
    Name: Optional[str]
    Priority: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dynamicsnippet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dynamicsnippet"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dynamicsnippet = Dynamicsnippet


@dataclass
class Gcslogging:
    BucketName: Optional[str]
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
        cls: Type["_Gcslogging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Gcslogging"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
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
_Gcslogging = Gcslogging


@dataclass
class Gzip:
    CacheCondition: Optional[str]
    ContentTypes: Optional[Sequence[str]]
    Extensions: Optional[Sequence[str]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Gzip"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Gzip"]:
        if not json_data:
            return None
        return cls(
            CacheCondition=json_data.get("CacheCondition"),
            ContentTypes=json_data.get("ContentTypes"),
            Extensions=json_data.get("Extensions"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Gzip = Gzip


@dataclass
class Header:
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
        cls: Type["_Header"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Header"]:
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
_Header = Header


@dataclass
class Healthcheck:
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
        cls: Type["_Healthcheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Healthcheck"]:
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
_Healthcheck = Healthcheck


@dataclass
class Logentries:
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
        cls: Type["_Logentries"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Logentries"]:
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
_Logentries = Logentries


@dataclass
class Papertrail:
    Address: Optional[str]
    Format: Optional[str]
    Name: Optional[str]
    Placement: Optional[str]
    Port: Optional[float]
    ResponseCondition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Papertrail"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Papertrail"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Format=json_data.get("Format"),
            Name=json_data.get("Name"),
            Placement=json_data.get("Placement"),
            Port=json_data.get("Port"),
            ResponseCondition=json_data.get("ResponseCondition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Papertrail = Papertrail


@dataclass
class RequestSetting:
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
        cls: Type["_RequestSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestSetting"]:
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
_RequestSetting = RequestSetting


@dataclass
class ResponseObject:
    CacheCondition: Optional[str]
    Content: Optional[str]
    ContentType: Optional[str]
    Name: Optional[str]
    RequestCondition: Optional[str]
    Response: Optional[str]
    Status: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseObject"]:
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
_ResponseObject = ResponseObject


@dataclass
class S3logging:
    BucketName: Optional[str]
    Domain: Optional[str]
    Format: Optional[str]
    FormatVersion: Optional[float]
    GzipLevel: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Period: Optional[float]
    Placement: Optional[str]
    Redundancy: Optional[str]
    ResponseCondition: Optional[str]
    S3AccessKey: Optional[str]
    S3SecretKey: Optional[str]
    TimestampFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3logging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3logging"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            Domain=json_data.get("Domain"),
            Format=json_data.get("Format"),
            FormatVersion=json_data.get("FormatVersion"),
            GzipLevel=json_data.get("GzipLevel"),
            MessageType=json_data.get("MessageType"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Period=json_data.get("Period"),
            Placement=json_data.get("Placement"),
            Redundancy=json_data.get("Redundancy"),
            ResponseCondition=json_data.get("ResponseCondition"),
            S3AccessKey=json_data.get("S3AccessKey"),
            S3SecretKey=json_data.get("S3SecretKey"),
            TimestampFormat=json_data.get("TimestampFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3logging = S3logging


@dataclass
class Snippet:
    Content: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Snippet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Snippet"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Snippet = Snippet


@dataclass
class Splunk:
    Format: Optional[str]
    FormatVersion: Optional[float]
    Name: Optional[str]
    Placement: Optional[str]
    ResponseCondition: Optional[str]
    Token: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Splunk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Splunk"]:
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
_Splunk = Splunk


@dataclass
class Sumologic:
    Format: Optional[str]
    FormatVersion: Optional[float]
    MessageType: Optional[str]
    Name: Optional[str]
    Placement: Optional[str]
    ResponseCondition: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Sumologic"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sumologic"]:
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
_Sumologic = Sumologic


@dataclass
class Syslog:
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
        cls: Type["_Syslog"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Syslog"]:
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
_Syslog = Syslog


@dataclass
class Vcl:
    Content: Optional[str]
    Main: Optional[bool]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Vcl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Vcl"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Main=json_data.get("Main"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Vcl = Vcl


