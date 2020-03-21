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
    Active: Optional[bool]
    CheckByCollector: Optional[Sequence["_CheckByCollector"]]
    CheckId: Optional[str]
    Checks: Optional[Sequence[str]]
    Created: Optional[float]
    LastModified: Optional[float]
    LastModifiedBy: Optional[str]
    MetricLimit: Optional[float]
    Name: Optional[str]
    Notes: Optional[str]
    Period: Optional[str]
    ReverseConnectUrls: Optional[Sequence[str]]
    Tags: Optional[Sequence[str]]
    Target: Optional[str]
    Timeout: Optional[str]
    Type: Optional[str]
    Uuids: Optional[Sequence[str]]
    Caql: Optional[Sequence["_Caql"]]
    Cloudwatch: Optional[Sequence["_Cloudwatch"]]
    Collector: Optional[Sequence["_Collector"]]
    Consul: Optional[Sequence["_Consul"]]
    Dns: Optional[Sequence["_Dns"]]
    External: Optional[Sequence["_External"]]
    Http: Optional[Sequence["_Http"]]
    Httptrap: Optional[Sequence["_Httptrap"]]
    IcmpPing: Optional[Sequence["_IcmpPing"]]
    Jmx: Optional[Sequence["_Jmx"]]
    Json: Optional[Sequence["_Json"]]
    Memcached: Optional[Sequence["_Memcached"]]
    Metric: Optional[Sequence["_Metric"]]
    MetricFilter: Optional[Sequence["_MetricFilter"]]
    Mysql: Optional[Sequence["_Mysql"]]
    Postgresql: Optional[Sequence["_Postgresql"]]
    Promtext: Optional[Sequence["_Promtext"]]
    Redis: Optional[Sequence["_Redis"]]
    Snmp: Optional[Sequence["_Snmp"]]
    Statsd: Optional[Sequence["_Statsd"]]
    Tcp: Optional[Sequence["_Tcp"]]
    MbeanProperties: Optional[Sequence["_MbeanProperties"]]
    Oid: Optional[Sequence["_Oid"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Active=json_data.get("Active"),
            CheckByCollector=json_data.get("CheckByCollector"),
            CheckId=json_data.get("CheckId"),
            Checks=json_data.get("Checks"),
            Created=json_data.get("Created"),
            LastModified=json_data.get("LastModified"),
            LastModifiedBy=json_data.get("LastModifiedBy"),
            MetricLimit=json_data.get("MetricLimit"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Period=json_data.get("Period"),
            ReverseConnectUrls=json_data.get("ReverseConnectUrls"),
            Tags=json_data.get("Tags"),
            Target=json_data.get("Target"),
            Timeout=json_data.get("Timeout"),
            Type=json_data.get("Type"),
            Uuids=json_data.get("Uuids"),
            Caql=json_data.get("Caql"),
            Cloudwatch=json_data.get("Cloudwatch"),
            Collector=json_data.get("Collector"),
            Consul=json_data.get("Consul"),
            Dns=json_data.get("Dns"),
            External=json_data.get("External"),
            Http=json_data.get("Http"),
            Httptrap=json_data.get("Httptrap"),
            IcmpPing=json_data.get("IcmpPing"),
            Jmx=json_data.get("Jmx"),
            Json=json_data.get("Json"),
            Memcached=json_data.get("Memcached"),
            Metric=json_data.get("Metric"),
            MetricFilter=json_data.get("MetricFilter"),
            Mysql=json_data.get("Mysql"),
            Postgresql=json_data.get("Postgresql"),
            Promtext=json_data.get("Promtext"),
            Redis=json_data.get("Redis"),
            Snmp=json_data.get("Snmp"),
            Statsd=json_data.get("Statsd"),
            Tcp=json_data.get("Tcp"),
            MbeanProperties=json_data.get("MbeanProperties"),
            Oid=json_data.get("Oid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CheckByCollector:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CheckByCollector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CheckByCollector"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CheckByCollector = CheckByCollector


@dataclass
class Caql:
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Caql"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Caql"]:
        if not json_data:
            return None
        return cls(
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Caql = Caql


@dataclass
class Cloudwatch:
    ApiKey: Optional[str]
    ApiSecret: Optional[str]
    Dimmensions: Optional[Sequence["_Dimmensions"]]
    Metric: Optional[Sequence[str]]
    Namespace: Optional[str]
    Url: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Cloudwatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cloudwatch"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
            ApiSecret=json_data.get("ApiSecret"),
            Dimmensions=json_data.get("Dimmensions"),
            Metric=json_data.get("Metric"),
            Namespace=json_data.get("Namespace"),
            Url=json_data.get("Url"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cloudwatch = Cloudwatch


@dataclass
class Dimmensions:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dimmensions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dimmensions"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dimmensions = Dimmensions


@dataclass
class Collector:
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Collector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Collector"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Collector = Collector


@dataclass
class Consul:
    AclToken: Optional[str]
    AllowStale: Optional[bool]
    CaChain: Optional[str]
    CertificateFile: Optional[str]
    CheckBlacklist: Optional[Sequence[str]]
    Ciphers: Optional[str]
    Dc: Optional[str]
    Headers: Optional[Sequence["_Headers"]]
    HttpAddr: Optional[str]
    KeyFile: Optional[str]
    Node: Optional[str]
    NodeBlacklist: Optional[Sequence[str]]
    Service: Optional[str]
    ServiceBlacklist: Optional[Sequence[str]]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Consul"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Consul"]:
        if not json_data:
            return None
        return cls(
            AclToken=json_data.get("AclToken"),
            AllowStale=json_data.get("AllowStale"),
            CaChain=json_data.get("CaChain"),
            CertificateFile=json_data.get("CertificateFile"),
            CheckBlacklist=json_data.get("CheckBlacklist"),
            Ciphers=json_data.get("Ciphers"),
            Dc=json_data.get("Dc"),
            Headers=json_data.get("Headers"),
            HttpAddr=json_data.get("HttpAddr"),
            KeyFile=json_data.get("KeyFile"),
            Node=json_data.get("Node"),
            NodeBlacklist=json_data.get("NodeBlacklist"),
            Service=json_data.get("Service"),
            ServiceBlacklist=json_data.get("ServiceBlacklist"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Consul = Consul


@dataclass
class Headers:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers = Headers


@dataclass
class Dns:
    Ctype: Optional[str]
    Nameserver: Optional[str]
    Query: Optional[str]
    Rtype: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dns"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dns"]:
        if not json_data:
            return None
        return cls(
            Ctype=json_data.get("Ctype"),
            Nameserver=json_data.get("Nameserver"),
            Query=json_data.get("Query"),
            Rtype=json_data.get("Rtype"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dns = Dns


@dataclass
class External:
    Arg1: Optional[str]
    Arg10: Optional[str]
    Arg2: Optional[str]
    Arg3: Optional[str]
    Arg4: Optional[str]
    Arg5: Optional[str]
    Arg6: Optional[str]
    Arg7: Optional[str]
    Arg8: Optional[str]
    Arg9: Optional[str]
    Command: Optional[str]
    OutputExtract: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_External"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_External"]:
        if not json_data:
            return None
        return cls(
            Arg1=json_data.get("Arg1"),
            Arg10=json_data.get("Arg10"),
            Arg2=json_data.get("Arg2"),
            Arg3=json_data.get("Arg3"),
            Arg4=json_data.get("Arg4"),
            Arg5=json_data.get("Arg5"),
            Arg6=json_data.get("Arg6"),
            Arg7=json_data.get("Arg7"),
            Arg8=json_data.get("Arg8"),
            Arg9=json_data.get("Arg9"),
            Command=json_data.get("Command"),
            OutputExtract=json_data.get("OutputExtract"),
        )


# work around possible type aliasing issues when variable has same name as a model
_External = External


@dataclass
class Http:
    AuthMethod: Optional[str]
    AuthPassword: Optional[str]
    AuthUser: Optional[str]
    BodyRegexp: Optional[str]
    CaChain: Optional[str]
    CertificateFile: Optional[str]
    Ciphers: Optional[str]
    Code: Optional[str]
    Extract: Optional[str]
    Headers: Optional[Sequence["_Headers2"]]
    KeyFile: Optional[str]
    Method: Optional[str]
    Payload: Optional[str]
    ReadLimit: Optional[float]
    Url: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Http"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Http"]:
        if not json_data:
            return None
        return cls(
            AuthMethod=json_data.get("AuthMethod"),
            AuthPassword=json_data.get("AuthPassword"),
            AuthUser=json_data.get("AuthUser"),
            BodyRegexp=json_data.get("BodyRegexp"),
            CaChain=json_data.get("CaChain"),
            CertificateFile=json_data.get("CertificateFile"),
            Ciphers=json_data.get("Ciphers"),
            Code=json_data.get("Code"),
            Extract=json_data.get("Extract"),
            Headers=json_data.get("Headers"),
            KeyFile=json_data.get("KeyFile"),
            Method=json_data.get("Method"),
            Payload=json_data.get("Payload"),
            ReadLimit=json_data.get("ReadLimit"),
            Url=json_data.get("Url"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Http = Http


@dataclass
class Headers2:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers2"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers2 = Headers2


@dataclass
class Httptrap:
    AsyncMetrics: Optional[bool]
    Secret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Httptrap"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Httptrap"]:
        if not json_data:
            return None
        return cls(
            AsyncMetrics=json_data.get("AsyncMetrics"),
            Secret=json_data.get("Secret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Httptrap = Httptrap


@dataclass
class IcmpPing:
    Availability: Optional[float]
    Count: Optional[float]
    Interval: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IcmpPing"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IcmpPing"]:
        if not json_data:
            return None
        return cls(
            Availability=json_data.get("Availability"),
            Count=json_data.get("Count"),
            Interval=json_data.get("Interval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IcmpPing = IcmpPing


@dataclass
class Jmx:
    Host: Optional[str]
    MbeanDomains: Optional[Sequence[str]]
    Password: Optional[str]
    Port: Optional[float]
    Uri: Optional[str]
    Username: Optional[str]
    MbeanProperties: Optional[Sequence["_MbeanProperties"]]

    @classmethod
    def _deserialize(
        cls: Type["_Jmx"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Jmx"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            MbeanDomains=json_data.get("MbeanDomains"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Uri=json_data.get("Uri"),
            Username=json_data.get("Username"),
            MbeanProperties=json_data.get("MbeanProperties"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Jmx = Jmx


@dataclass
class MbeanProperties:
    Index: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MbeanProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MbeanProperties"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MbeanProperties = MbeanProperties


@dataclass
class Json:
    AuthMethod: Optional[str]
    AuthPassword: Optional[str]
    AuthUser: Optional[str]
    CaChain: Optional[str]
    CertificateFile: Optional[str]
    Ciphers: Optional[str]
    Headers: Optional[Sequence["_Headers3"]]
    KeyFile: Optional[str]
    Method: Optional[str]
    Payload: Optional[str]
    Port: Optional[float]
    ReadLimit: Optional[float]
    Url: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Json"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Json"]:
        if not json_data:
            return None
        return cls(
            AuthMethod=json_data.get("AuthMethod"),
            AuthPassword=json_data.get("AuthPassword"),
            AuthUser=json_data.get("AuthUser"),
            CaChain=json_data.get("CaChain"),
            CertificateFile=json_data.get("CertificateFile"),
            Ciphers=json_data.get("Ciphers"),
            Headers=json_data.get("Headers"),
            KeyFile=json_data.get("KeyFile"),
            Method=json_data.get("Method"),
            Payload=json_data.get("Payload"),
            Port=json_data.get("Port"),
            ReadLimit=json_data.get("ReadLimit"),
            Url=json_data.get("Url"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Json = Json


@dataclass
class Headers3:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers3"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers3 = Headers3


@dataclass
class Memcached:
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Memcached"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Memcached"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Memcached = Memcached


@dataclass
class Metric:
    Active: Optional[bool]
    Name: Optional[str]
    Tags: Optional[Sequence[str]]
    Type: Optional[str]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metric"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metric = Metric


@dataclass
class MetricFilter:
    Comment: Optional[str]
    Regex: Optional[str]
    TagQuery: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricFilter"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            Regex=json_data.get("Regex"),
            TagQuery=json_data.get("TagQuery"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricFilter = MetricFilter


@dataclass
class Mysql:
    Dsn: Optional[str]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Mysql"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Mysql"]:
        if not json_data:
            return None
        return cls(
            Dsn=json_data.get("Dsn"),
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Mysql = Mysql


@dataclass
class Postgresql:
    Dsn: Optional[str]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Postgresql"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Postgresql"]:
        if not json_data:
            return None
        return cls(
            Dsn=json_data.get("Dsn"),
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Postgresql = Postgresql


@dataclass
class Promtext:
    Port: Optional[float]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Promtext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Promtext"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Promtext = Promtext


@dataclass
class Redis:
    Command: Optional[str]
    DbIndex: Optional[float]
    Password: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Redis"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Redis"]:
        if not json_data:
            return None
        return cls(
            Command=json_data.get("Command"),
            DbIndex=json_data.get("DbIndex"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Redis = Redis


@dataclass
class Snmp:
    AuthPassphrase: Optional[str]
    AuthProtocol: Optional[str]
    Community: Optional[str]
    ContextEngine: Optional[str]
    ContextName: Optional[str]
    Port: Optional[float]
    PrivacyPassphrase: Optional[str]
    PrivacyProtocol: Optional[str]
    SecurityEngine: Optional[str]
    SecurityLevel: Optional[str]
    SecurityName: Optional[str]
    SeparateQueries: Optional[bool]
    Version: Optional[str]
    Oid: Optional[Sequence["_Oid"]]

    @classmethod
    def _deserialize(
        cls: Type["_Snmp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Snmp"]:
        if not json_data:
            return None
        return cls(
            AuthPassphrase=json_data.get("AuthPassphrase"),
            AuthProtocol=json_data.get("AuthProtocol"),
            Community=json_data.get("Community"),
            ContextEngine=json_data.get("ContextEngine"),
            ContextName=json_data.get("ContextName"),
            Port=json_data.get("Port"),
            PrivacyPassphrase=json_data.get("PrivacyPassphrase"),
            PrivacyProtocol=json_data.get("PrivacyProtocol"),
            SecurityEngine=json_data.get("SecurityEngine"),
            SecurityLevel=json_data.get("SecurityLevel"),
            SecurityName=json_data.get("SecurityName"),
            SeparateQueries=json_data.get("SeparateQueries"),
            Version=json_data.get("Version"),
            Oid=json_data.get("Oid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Snmp = Snmp


@dataclass
class Oid:
    Name: Optional[str]
    Path: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Oid"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Oid"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Oid = Oid


@dataclass
class Statsd:
    SourceIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Statsd"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Statsd"]:
        if not json_data:
            return None
        return cls(
            SourceIp=json_data.get("SourceIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Statsd = Statsd


@dataclass
class Tcp:
    BannerRegexp: Optional[str]
    CaChain: Optional[str]
    CertificateFile: Optional[str]
    Ciphers: Optional[str]
    Host: Optional[str]
    KeyFile: Optional[str]
    Port: Optional[float]
    Tls: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Tcp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tcp"]:
        if not json_data:
            return None
        return cls(
            BannerRegexp=json_data.get("BannerRegexp"),
            CaChain=json_data.get("CaChain"),
            CertificateFile=json_data.get("CertificateFile"),
            Ciphers=json_data.get("Ciphers"),
            Host=json_data.get("Host"),
            KeyFile=json_data.get("KeyFile"),
            Port=json_data.get("Port"),
            Tls=json_data.get("Tls"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tcp = Tcp


