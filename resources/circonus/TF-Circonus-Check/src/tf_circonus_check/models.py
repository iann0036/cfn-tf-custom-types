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
    Active: Optional[bool]
    CheckByCollector: Optional[Sequence["_CheckByCollectorDefinition"]]
    CheckId: Optional[str]
    Checks: Optional[Sequence[str]]
    Created: Optional[float]
    Id: Optional[str]
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
    Caql: Optional[Sequence["_CaqlDefinition"]]
    Cloudwatch: Optional[Sequence["_CloudwatchDefinition"]]
    Collector: Optional[Sequence["_CollectorDefinition"]]
    Consul: Optional[Sequence["_ConsulDefinition"]]
    Dns: Optional[Sequence["_DnsDefinition"]]
    External: Optional[Sequence["_ExternalDefinition"]]
    Http: Optional[Sequence["_HttpDefinition"]]
    Httptrap: Optional[Sequence["_HttptrapDefinition"]]
    IcmpPing: Optional[Sequence["_IcmpPingDefinition"]]
    Jmx: Optional[Sequence["_JmxDefinition"]]
    Json: Optional[Sequence["_JsonDefinition"]]
    Memcached: Optional[Sequence["_MemcachedDefinition"]]
    Metric: Optional[Sequence["_MetricDefinition"]]
    MetricFilter: Optional[Sequence["_MetricFilterDefinition"]]
    Mysql: Optional[Sequence["_MysqlDefinition"]]
    Ntp: Optional[Sequence["_NtpDefinition"]]
    Postgresql: Optional[Sequence["_PostgresqlDefinition"]]
    Promtext: Optional[Sequence["_PromtextDefinition"]]
    Redis: Optional[Sequence["_RedisDefinition"]]
    Smtp: Optional[Sequence["_SmtpDefinition"]]
    Snmp: Optional[Sequence["_SnmpDefinition"]]
    Statsd: Optional[Sequence["_StatsdDefinition"]]
    Tcp: Optional[Sequence["_TcpDefinition"]]

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
            Active=json_data.get("Active"),
            CheckByCollector=deserialize_list(json_data.get("CheckByCollector"), CheckByCollectorDefinition),
            CheckId=json_data.get("CheckId"),
            Checks=json_data.get("Checks"),
            Created=json_data.get("Created"),
            Id=json_data.get("Id"),
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
            Caql=deserialize_list(json_data.get("Caql"), CaqlDefinition),
            Cloudwatch=deserialize_list(json_data.get("Cloudwatch"), CloudwatchDefinition),
            Collector=deserialize_list(json_data.get("Collector"), CollectorDefinition),
            Consul=deserialize_list(json_data.get("Consul"), ConsulDefinition),
            Dns=deserialize_list(json_data.get("Dns"), DnsDefinition),
            External=deserialize_list(json_data.get("External"), ExternalDefinition),
            Http=deserialize_list(json_data.get("Http"), HttpDefinition),
            Httptrap=deserialize_list(json_data.get("Httptrap"), HttptrapDefinition),
            IcmpPing=deserialize_list(json_data.get("IcmpPing"), IcmpPingDefinition),
            Jmx=deserialize_list(json_data.get("Jmx"), JmxDefinition),
            Json=deserialize_list(json_data.get("Json"), JsonDefinition),
            Memcached=deserialize_list(json_data.get("Memcached"), MemcachedDefinition),
            Metric=deserialize_list(json_data.get("Metric"), MetricDefinition),
            MetricFilter=deserialize_list(json_data.get("MetricFilter"), MetricFilterDefinition),
            Mysql=deserialize_list(json_data.get("Mysql"), MysqlDefinition),
            Ntp=deserialize_list(json_data.get("Ntp"), NtpDefinition),
            Postgresql=deserialize_list(json_data.get("Postgresql"), PostgresqlDefinition),
            Promtext=deserialize_list(json_data.get("Promtext"), PromtextDefinition),
            Redis=deserialize_list(json_data.get("Redis"), RedisDefinition),
            Smtp=deserialize_list(json_data.get("Smtp"), SmtpDefinition),
            Snmp=deserialize_list(json_data.get("Snmp"), SnmpDefinition),
            Statsd=deserialize_list(json_data.get("Statsd"), StatsdDefinition),
            Tcp=deserialize_list(json_data.get("Tcp"), TcpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CheckByCollectorDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CheckByCollectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CheckByCollectorDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CheckByCollectorDefinition = CheckByCollectorDefinition


@dataclass
class CaqlDefinition(BaseModel):
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CaqlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaqlDefinition"]:
        if not json_data:
            return None
        return cls(
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaqlDefinition = CaqlDefinition


@dataclass
class CloudwatchDefinition(BaseModel):
    ApiKey: Optional[str]
    ApiSecret: Optional[str]
    Dimmensions: Optional[Sequence["_DimmensionsDefinition"]]
    Metric: Optional[Sequence[str]]
    Namespace: Optional[str]
    Url: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
            ApiSecret=json_data.get("ApiSecret"),
            Dimmensions=deserialize_list(json_data.get("Dimmensions"), DimmensionsDefinition),
            Metric=json_data.get("Metric"),
            Namespace=json_data.get("Namespace"),
            Url=json_data.get("Url"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchDefinition = CloudwatchDefinition


@dataclass
class DimmensionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimmensionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimmensionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimmensionsDefinition = DimmensionsDefinition


@dataclass
class CollectorDefinition(BaseModel):
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CollectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CollectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CollectorDefinition = CollectorDefinition


@dataclass
class ConsulDefinition(BaseModel):
    AclToken: Optional[str]
    AllowStale: Optional[bool]
    CaChain: Optional[str]
    CertificateFile: Optional[str]
    CheckBlacklist: Optional[Sequence[str]]
    Ciphers: Optional[str]
    Dc: Optional[str]
    Headers: Optional[Sequence["_HeadersDefinition"]]
    HttpAddr: Optional[str]
    KeyFile: Optional[str]
    Node: Optional[str]
    NodeBlacklist: Optional[Sequence[str]]
    Service: Optional[str]
    ServiceBlacklist: Optional[Sequence[str]]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConsulDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConsulDefinition"]:
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
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
            HttpAddr=json_data.get("HttpAddr"),
            KeyFile=json_data.get("KeyFile"),
            Node=json_data.get("Node"),
            NodeBlacklist=json_data.get("NodeBlacklist"),
            Service=json_data.get("Service"),
            ServiceBlacklist=json_data.get("ServiceBlacklist"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConsulDefinition = ConsulDefinition


@dataclass
class HeadersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


@dataclass
class DnsDefinition(BaseModel):
    Ctype: Optional[str]
    Nameserver: Optional[str]
    Query: Optional[str]
    Rtype: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsDefinition"]:
        if not json_data:
            return None
        return cls(
            Ctype=json_data.get("Ctype"),
            Nameserver=json_data.get("Nameserver"),
            Query=json_data.get("Query"),
            Rtype=json_data.get("Rtype"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsDefinition = DnsDefinition


@dataclass
class ExternalDefinition(BaseModel):
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
    Env: Optional[Sequence["_EnvDefinition"]]
    OutputExtract: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalDefinition"]:
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
            Env=deserialize_list(json_data.get("Env"), EnvDefinition),
            OutputExtract=json_data.get("OutputExtract"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalDefinition = ExternalDefinition


@dataclass
class EnvDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvDefinition = EnvDefinition


@dataclass
class HttpDefinition(BaseModel):
    AuthMethod: Optional[str]
    AuthPassword: Optional[str]
    AuthUser: Optional[str]
    BodyRegexp: Optional[str]
    CaChain: Optional[str]
    CertificateFile: Optional[str]
    Ciphers: Optional[str]
    Code: Optional[str]
    Extract: Optional[str]
    Headers: Optional[Sequence["_HeadersDefinition2"]]
    KeyFile: Optional[str]
    Method: Optional[str]
    Payload: Optional[str]
    ReadLimit: Optional[float]
    Redirects: Optional[str]
    Url: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpDefinition"]:
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
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition2),
            KeyFile=json_data.get("KeyFile"),
            Method=json_data.get("Method"),
            Payload=json_data.get("Payload"),
            ReadLimit=json_data.get("ReadLimit"),
            Redirects=json_data.get("Redirects"),
            Url=json_data.get("Url"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpDefinition = HttpDefinition


@dataclass
class HeadersDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition2 = HeadersDefinition2


@dataclass
class HttptrapDefinition(BaseModel):
    AsyncMetrics: Optional[bool]
    Secret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttptrapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttptrapDefinition"]:
        if not json_data:
            return None
        return cls(
            AsyncMetrics=json_data.get("AsyncMetrics"),
            Secret=json_data.get("Secret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttptrapDefinition = HttptrapDefinition


@dataclass
class IcmpPingDefinition(BaseModel):
    Availability: Optional[float]
    Count: Optional[float]
    Interval: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IcmpPingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IcmpPingDefinition"]:
        if not json_data:
            return None
        return cls(
            Availability=json_data.get("Availability"),
            Count=json_data.get("Count"),
            Interval=json_data.get("Interval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IcmpPingDefinition = IcmpPingDefinition


@dataclass
class JmxDefinition(BaseModel):
    Host: Optional[str]
    MbeanDomains: Optional[Sequence[str]]
    Password: Optional[str]
    Port: Optional[float]
    Uri: Optional[str]
    Username: Optional[str]
    MbeanProperties: Optional[Sequence["_MbeanPropertiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_JmxDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JmxDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            MbeanDomains=json_data.get("MbeanDomains"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Uri=json_data.get("Uri"),
            Username=json_data.get("Username"),
            MbeanProperties=deserialize_list(json_data.get("MbeanProperties"), MbeanPropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_JmxDefinition = JmxDefinition


@dataclass
class MbeanPropertiesDefinition(BaseModel):
    Index: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MbeanPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MbeanPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MbeanPropertiesDefinition = MbeanPropertiesDefinition


@dataclass
class JsonDefinition(BaseModel):
    AuthMethod: Optional[str]
    AuthPassword: Optional[str]
    AuthUser: Optional[str]
    CaChain: Optional[str]
    CertificateFile: Optional[str]
    Ciphers: Optional[str]
    Headers: Optional[Sequence["_HeadersDefinition3"]]
    KeyFile: Optional[str]
    Method: Optional[str]
    Payload: Optional[str]
    Port: Optional[float]
    ReadLimit: Optional[float]
    Url: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JsonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsonDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthMethod=json_data.get("AuthMethod"),
            AuthPassword=json_data.get("AuthPassword"),
            AuthUser=json_data.get("AuthUser"),
            CaChain=json_data.get("CaChain"),
            CertificateFile=json_data.get("CertificateFile"),
            Ciphers=json_data.get("Ciphers"),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition3),
            KeyFile=json_data.get("KeyFile"),
            Method=json_data.get("Method"),
            Payload=json_data.get("Payload"),
            Port=json_data.get("Port"),
            ReadLimit=json_data.get("ReadLimit"),
            Url=json_data.get("Url"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsonDefinition = JsonDefinition


@dataclass
class HeadersDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition3 = HeadersDefinition3


@dataclass
class MemcachedDefinition(BaseModel):
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MemcachedDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemcachedDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemcachedDefinition = MemcachedDefinition


@dataclass
class MetricDefinition(BaseModel):
    Active: Optional[bool]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDefinition"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDefinition = MetricDefinition


@dataclass
class MetricFilterDefinition(BaseModel):
    Comment: Optional[str]
    Regex: Optional[str]
    TagQuery: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            Regex=json_data.get("Regex"),
            TagQuery=json_data.get("TagQuery"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricFilterDefinition = MetricFilterDefinition


@dataclass
class MysqlDefinition(BaseModel):
    Dsn: Optional[str]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MysqlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MysqlDefinition"]:
        if not json_data:
            return None
        return cls(
            Dsn=json_data.get("Dsn"),
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MysqlDefinition = MysqlDefinition


@dataclass
class NtpDefinition(BaseModel):
    Port: Optional[float]
    UseControl: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NtpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NtpDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            UseControl=json_data.get("UseControl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NtpDefinition = NtpDefinition


@dataclass
class PostgresqlDefinition(BaseModel):
    Dsn: Optional[str]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PostgresqlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PostgresqlDefinition"]:
        if not json_data:
            return None
        return cls(
            Dsn=json_data.get("Dsn"),
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PostgresqlDefinition = PostgresqlDefinition


@dataclass
class PromtextDefinition(BaseModel):
    Port: Optional[float]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PromtextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PromtextDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PromtextDefinition = PromtextDefinition


@dataclass
class RedisDefinition(BaseModel):
    Command: Optional[str]
    DbIndex: Optional[float]
    Password: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RedisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedisDefinition"]:
        if not json_data:
            return None
        return cls(
            Command=json_data.get("Command"),
            DbIndex=json_data.get("DbIndex"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedisDefinition = RedisDefinition


@dataclass
class SmtpDefinition(BaseModel):
    Ehlo: Optional[str]
    From: Optional[str]
    Payload: Optional[str]
    Port: Optional[float]
    ProxyDestAddress: Optional[str]
    ProxyDestPort: Optional[float]
    ProxyFamily: Optional[str]
    ProxyProtocol: Optional[bool]
    ProxySourceAddress: Optional[str]
    ProxySourcePort: Optional[float]
    SaslAuthId: Optional[str]
    SaslAuthentication: Optional[str]
    SaslPassword: Optional[str]
    SaslUser: Optional[str]
    Starttls: Optional[bool]
    To: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmtpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmtpDefinition"]:
        if not json_data:
            return None
        return cls(
            Ehlo=json_data.get("Ehlo"),
            From=json_data.get("From"),
            Payload=json_data.get("Payload"),
            Port=json_data.get("Port"),
            ProxyDestAddress=json_data.get("ProxyDestAddress"),
            ProxyDestPort=json_data.get("ProxyDestPort"),
            ProxyFamily=json_data.get("ProxyFamily"),
            ProxyProtocol=json_data.get("ProxyProtocol"),
            ProxySourceAddress=json_data.get("ProxySourceAddress"),
            ProxySourcePort=json_data.get("ProxySourcePort"),
            SaslAuthId=json_data.get("SaslAuthId"),
            SaslAuthentication=json_data.get("SaslAuthentication"),
            SaslPassword=json_data.get("SaslPassword"),
            SaslUser=json_data.get("SaslUser"),
            Starttls=json_data.get("Starttls"),
            To=json_data.get("To"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmtpDefinition = SmtpDefinition


@dataclass
class SnmpDefinition(BaseModel):
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
    Oid: Optional[Sequence["_OidDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SnmpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnmpDefinition"]:
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
            Oid=deserialize_list(json_data.get("Oid"), OidDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnmpDefinition = SnmpDefinition


@dataclass
class OidDefinition(BaseModel):
    Name: Optional[str]
    Path: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OidDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OidDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OidDefinition = OidDefinition


@dataclass
class StatsdDefinition(BaseModel):
    SourceIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatsdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatsdDefinition"]:
        if not json_data:
            return None
        return cls(
            SourceIp=json_data.get("SourceIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatsdDefinition = StatsdDefinition


@dataclass
class TcpDefinition(BaseModel):
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
        cls: Type["_TcpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpDefinition"]:
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
_TcpDefinition = TcpDefinition


