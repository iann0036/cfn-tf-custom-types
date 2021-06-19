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
    AllowedRoles: Optional[Sequence[str]]
    Backend: Optional[str]
    Data: Optional[Sequence["_DataDefinition"]]
    Id: Optional[str]
    Name: Optional[str]
    RootRotationStatements: Optional[Sequence[str]]
    VerifyConnection: Optional[bool]
    Cassandra: Optional[Sequence["_CassandraDefinition"]]
    Elasticsearch: Optional[Sequence["_ElasticsearchDefinition"]]
    Hana: Optional[Sequence["_HanaDefinition"]]
    Mongodb: Optional[Sequence["_MongodbDefinition"]]
    Mongodbatlas: Optional[Sequence["_MongodbatlasDefinition"]]
    Mssql: Optional[Sequence["_MssqlDefinition"]]
    Mysql: Optional[Sequence["_MysqlDefinition"]]
    MysqlAurora: Optional[Sequence["_MysqlAuroraDefinition"]]
    MysqlLegacy: Optional[Sequence["_MysqlLegacyDefinition"]]
    MysqlRds: Optional[Sequence["_MysqlRdsDefinition"]]
    Oracle: Optional[Sequence["_OracleDefinition"]]
    Postgresql: Optional[Sequence["_PostgresqlDefinition"]]

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
            AllowedRoles=json_data.get("AllowedRoles"),
            Backend=json_data.get("Backend"),
            Data=deserialize_list(json_data.get("Data"), DataDefinition),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RootRotationStatements=json_data.get("RootRotationStatements"),
            VerifyConnection=json_data.get("VerifyConnection"),
            Cassandra=deserialize_list(json_data.get("Cassandra"), CassandraDefinition),
            Elasticsearch=deserialize_list(json_data.get("Elasticsearch"), ElasticsearchDefinition),
            Hana=deserialize_list(json_data.get("Hana"), HanaDefinition),
            Mongodb=deserialize_list(json_data.get("Mongodb"), MongodbDefinition),
            Mongodbatlas=deserialize_list(json_data.get("Mongodbatlas"), MongodbatlasDefinition),
            Mssql=deserialize_list(json_data.get("Mssql"), MssqlDefinition),
            Mysql=deserialize_list(json_data.get("Mysql"), MysqlDefinition),
            MysqlAurora=deserialize_list(json_data.get("MysqlAurora"), MysqlAuroraDefinition),
            MysqlLegacy=deserialize_list(json_data.get("MysqlLegacy"), MysqlLegacyDefinition),
            MysqlRds=deserialize_list(json_data.get("MysqlRds"), MysqlRdsDefinition),
            Oracle=deserialize_list(json_data.get("Oracle"), OracleDefinition),
            Postgresql=deserialize_list(json_data.get("Postgresql"), PostgresqlDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDefinition = DataDefinition


@dataclass
class CassandraDefinition(BaseModel):
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
        cls: Type["_CassandraDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CassandraDefinition"]:
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
_CassandraDefinition = CassandraDefinition


@dataclass
class ElasticsearchDefinition(BaseModel):
    Password: Optional[str]
    Url: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticsearchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticsearchDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticsearchDefinition = ElasticsearchDefinition


@dataclass
class HanaDefinition(BaseModel):
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HanaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HanaDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HanaDefinition = HanaDefinition


@dataclass
class MongodbDefinition(BaseModel):
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MongodbDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MongodbDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MongodbDefinition = MongodbDefinition


@dataclass
class MongodbatlasDefinition(BaseModel):
    PrivateKey: Optional[str]
    ProjectId: Optional[str]
    PublicKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MongodbatlasDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MongodbatlasDefinition"]:
        if not json_data:
            return None
        return cls(
            PrivateKey=json_data.get("PrivateKey"),
            ProjectId=json_data.get("ProjectId"),
            PublicKey=json_data.get("PublicKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MongodbatlasDefinition = MongodbatlasDefinition


@dataclass
class MssqlDefinition(BaseModel):
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MssqlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MssqlDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MssqlDefinition = MssqlDefinition


@dataclass
class MysqlDefinition(BaseModel):
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MysqlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MysqlDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MysqlDefinition = MysqlDefinition


@dataclass
class MysqlAuroraDefinition(BaseModel):
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MysqlAuroraDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MysqlAuroraDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MysqlAuroraDefinition = MysqlAuroraDefinition


@dataclass
class MysqlLegacyDefinition(BaseModel):
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MysqlLegacyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MysqlLegacyDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MysqlLegacyDefinition = MysqlLegacyDefinition


@dataclass
class MysqlRdsDefinition(BaseModel):
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MysqlRdsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MysqlRdsDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MysqlRdsDefinition = MysqlRdsDefinition


@dataclass
class OracleDefinition(BaseModel):
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OracleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OracleDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OracleDefinition = OracleDefinition


@dataclass
class PostgresqlDefinition(BaseModel):
    ConnectionUrl: Optional[str]
    MaxConnectionLifetime: Optional[float]
    MaxIdleConnections: Optional[float]
    MaxOpenConnections: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PostgresqlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PostgresqlDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionUrl=json_data.get("ConnectionUrl"),
            MaxConnectionLifetime=json_data.get("MaxConnectionLifetime"),
            MaxIdleConnections=json_data.get("MaxIdleConnections"),
            MaxOpenConnections=json_data.get("MaxOpenConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PostgresqlDefinition = PostgresqlDefinition


