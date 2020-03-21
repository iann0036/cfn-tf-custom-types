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
    AllowedRoles: Optional[Sequence[str]]
    Backend: Optional[str]
    Data: Optional[Sequence["_Data"]]
    Name: Optional[str]
    RootRotationStatements: Optional[Sequence[str]]
    VerifyConnection: Optional[bool]
    Cassandra: Optional[Sequence["_Cassandra"]]
    Hana: Optional[Sequence["_Hana"]]
    Mongodb: Optional[Sequence["_Mongodb"]]
    Mssql: Optional[Sequence["_Mssql"]]
    Mysql: Optional[Sequence["_Mysql"]]
    MysqlAurora: Optional[Sequence["_MysqlAurora"]]
    MysqlLegacy: Optional[Sequence["_MysqlLegacy"]]
    MysqlRds: Optional[Sequence["_MysqlRds"]]
    Oracle: Optional[Sequence["_Oracle"]]
    Postgresql: Optional[Sequence["_Postgresql"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowedRoles=json_data.get("AllowedRoles"),
            Backend=json_data.get("Backend"),
            Data=json_data.get("Data"),
            Name=json_data.get("Name"),
            RootRotationStatements=json_data.get("RootRotationStatements"),
            VerifyConnection=json_data.get("VerifyConnection"),
            Cassandra=json_data.get("Cassandra"),
            Hana=json_data.get("Hana"),
            Mongodb=json_data.get("Mongodb"),
            Mssql=json_data.get("Mssql"),
            Mysql=json_data.get("Mysql"),
            MysqlAurora=json_data.get("MysqlAurora"),
            MysqlLegacy=json_data.get("MysqlLegacy"),
            MysqlRds=json_data.get("MysqlRds"),
            Oracle=json_data.get("Oracle"),
            Postgresql=json_data.get("Postgresql"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Data:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Data"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Data"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Data = Data


@dataclass
class Cassandra:
    ConnectTimeout: Optional[float]
    Hosts: Optional[Sequence[str]]
    InsecureTls: Optional[bool]
    Password: Optional[str]
    PemBundle: Optional[str]
    PemJson: Optional[str]
    Port: Optional[float]
    ProtocolVersion: Optional[float]
    Tls: Optional[bool]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Cassandra"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cassandra"]:
        if not json_data:
            return None
        return cls(
            ConnectTimeout=json_data.get("ConnectTimeout"),
            Hosts=json_data.get("Hosts"),
            InsecureTls=json_data.get("InsecureTls"),
            Password=json_data.get("Password"),
            PemBundle=json_data.get("PemBundle"),
            PemJson=json_data.get("PemJson"),
            Port=json_data.get("Port"),
            ProtocolVersion=json_data.get("ProtocolVersion"),
            Tls=json_data.get("Tls"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cassandra = Cassandra


@dataclass
class Hana:
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Hana"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Hana"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Hana = Hana


@dataclass
class Mongodb:
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Mongodb"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Mongodb"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Mongodb = Mongodb


@dataclass
class Mssql:
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Mssql"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Mssql"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Mssql = Mssql


@dataclass
class Mysql:
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Mysql"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Mysql"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Mysql = Mysql


@dataclass
class MysqlAurora:
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MysqlAurora"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MysqlAurora"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MysqlAurora = MysqlAurora


@dataclass
class MysqlLegacy:
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MysqlLegacy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MysqlLegacy"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MysqlLegacy = MysqlLegacy


@dataclass
class MysqlRds:
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MysqlRds"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MysqlRds"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MysqlRds = MysqlRds


@dataclass
class Oracle:
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Oracle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Oracle"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Oracle = Oracle


@dataclass
class Postgresql:
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Postgresql"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Postgresql"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Postgresql = Postgresql


