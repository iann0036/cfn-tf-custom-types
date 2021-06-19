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
    Id: Optional[str]
    Aks: Optional[Sequence["_AksDefinition"]]
    AksBasicAuth: Optional[Sequence["_AksBasicAuthDefinition"]]
    AksServiceAccount: Optional[Sequence["_AksServiceAccountDefinition"]]
    AksServiceAccountUserImpersonation: Optional[Sequence["_AksServiceAccountUserImpersonationDefinition"]]
    AksUserImpersonation: Optional[Sequence["_AksUserImpersonationDefinition"]]
    AmazonEks: Optional[Sequence["_AmazonEksDefinition"]]
    AmazonEksUserImpersonation: Optional[Sequence["_AmazonEksUserImpersonationDefinition"]]
    AmazonEs: Optional[Sequence["_AmazonEsDefinition"]]
    AmazonmqAmqp091: Optional[Sequence["_AmazonmqAmqp091Definition"]]
    Athena: Optional[Sequence["_AthenaDefinition"]]
    AuroraMysql: Optional[Sequence["_AuroraMysqlDefinition"]]
    AuroraPostgres: Optional[Sequence["_AuroraPostgresDefinition"]]
    Aws: Optional[Sequence["_AwsDefinition"]]
    BigQuery: Optional[Sequence["_BigQueryDefinition"]]
    Cassandra: Optional[Sequence["_CassandraDefinition"]]
    Citus: Optional[Sequence["_CitusDefinition"]]
    Clustrix: Optional[Sequence["_ClustrixDefinition"]]
    Cockroach: Optional[Sequence["_CockroachDefinition"]]
    Db2I: Optional[Sequence["_Db2IDefinition"]]
    Db2Luw: Optional[Sequence["_Db2LuwDefinition"]]
    Druid: Optional[Sequence["_DruidDefinition"]]
    DynamoDb: Optional[Sequence["_DynamoDbDefinition"]]
    Elastic: Optional[Sequence["_ElasticDefinition"]]
    ElasticacheRedis: Optional[Sequence["_ElasticacheRedisDefinition"]]
    GoogleGke: Optional[Sequence["_GoogleGkeDefinition"]]
    GoogleGkeUserImpersonation: Optional[Sequence["_GoogleGkeUserImpersonationDefinition"]]
    Greenplum: Optional[Sequence["_GreenplumDefinition"]]
    HttpAuth: Optional[Sequence["_HttpAuthDefinition"]]
    HttpBasicAuth: Optional[Sequence["_HttpBasicAuthDefinition"]]
    HttpNoAuth: Optional[Sequence["_HttpNoAuthDefinition"]]
    Kubernetes: Optional[Sequence["_KubernetesDefinition"]]
    KubernetesBasicAuth: Optional[Sequence["_KubernetesBasicAuthDefinition"]]
    KubernetesServiceAccount: Optional[Sequence["_KubernetesServiceAccountDefinition"]]
    KubernetesServiceAccountUserImpersonation: Optional[Sequence["_KubernetesServiceAccountUserImpersonationDefinition"]]
    KubernetesUserImpersonation: Optional[Sequence["_KubernetesUserImpersonationDefinition"]]
    Maria: Optional[Sequence["_MariaDefinition"]]
    Memcached: Optional[Sequence["_MemcachedDefinition"]]
    Memsql: Optional[Sequence["_MemsqlDefinition"]]
    MongoHost: Optional[Sequence["_MongoHostDefinition"]]
    MongoLegacyHost: Optional[Sequence["_MongoLegacyHostDefinition"]]
    MongoLegacyReplicaset: Optional[Sequence["_MongoLegacyReplicasetDefinition"]]
    MongoReplicaSet: Optional[Sequence["_MongoReplicaSetDefinition"]]
    Mysql: Optional[Sequence["_MysqlDefinition"]]
    Oracle: Optional[Sequence["_OracleDefinition"]]
    Postgres: Optional[Sequence["_PostgresDefinition"]]
    Presto: Optional[Sequence["_PrestoDefinition"]]
    RabbitmqAmqp091: Optional[Sequence["_RabbitmqAmqp091Definition"]]
    Rdp: Optional[Sequence["_RdpDefinition"]]
    Redis: Optional[Sequence["_RedisDefinition"]]
    Redshift: Optional[Sequence["_RedshiftDefinition"]]
    Snowflake: Optional[Sequence["_SnowflakeDefinition"]]
    SqlServer: Optional[Sequence["_SqlServerDefinition"]]
    Ssh: Optional[Sequence["_SshDefinition"]]
    SshCert: Optional[Sequence["_SshCertDefinition"]]
    SshCustomerKey: Optional[Sequence["_SshCustomerKeyDefinition"]]
    Sybase: Optional[Sequence["_SybaseDefinition"]]
    SybaseIq: Optional[Sequence["_SybaseIqDefinition"]]
    Teradata: Optional[Sequence["_TeradataDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Id=json_data.get("Id"),
            Aks=deserialize_list(json_data.get("Aks"), AksDefinition),
            AksBasicAuth=deserialize_list(json_data.get("AksBasicAuth"), AksBasicAuthDefinition),
            AksServiceAccount=deserialize_list(json_data.get("AksServiceAccount"), AksServiceAccountDefinition),
            AksServiceAccountUserImpersonation=deserialize_list(json_data.get("AksServiceAccountUserImpersonation"), AksServiceAccountUserImpersonationDefinition),
            AksUserImpersonation=deserialize_list(json_data.get("AksUserImpersonation"), AksUserImpersonationDefinition),
            AmazonEks=deserialize_list(json_data.get("AmazonEks"), AmazonEksDefinition),
            AmazonEksUserImpersonation=deserialize_list(json_data.get("AmazonEksUserImpersonation"), AmazonEksUserImpersonationDefinition),
            AmazonEs=deserialize_list(json_data.get("AmazonEs"), AmazonEsDefinition),
            AmazonmqAmqp091=deserialize_list(json_data.get("AmazonmqAmqp091"), AmazonmqAmqp091Definition),
            Athena=deserialize_list(json_data.get("Athena"), AthenaDefinition),
            AuroraMysql=deserialize_list(json_data.get("AuroraMysql"), AuroraMysqlDefinition),
            AuroraPostgres=deserialize_list(json_data.get("AuroraPostgres"), AuroraPostgresDefinition),
            Aws=deserialize_list(json_data.get("Aws"), AwsDefinition),
            BigQuery=deserialize_list(json_data.get("BigQuery"), BigQueryDefinition),
            Cassandra=deserialize_list(json_data.get("Cassandra"), CassandraDefinition),
            Citus=deserialize_list(json_data.get("Citus"), CitusDefinition),
            Clustrix=deserialize_list(json_data.get("Clustrix"), ClustrixDefinition),
            Cockroach=deserialize_list(json_data.get("Cockroach"), CockroachDefinition),
            Db2I=deserialize_list(json_data.get("Db2I"), Db2IDefinition),
            Db2Luw=deserialize_list(json_data.get("Db2Luw"), Db2LuwDefinition),
            Druid=deserialize_list(json_data.get("Druid"), DruidDefinition),
            DynamoDb=deserialize_list(json_data.get("DynamoDb"), DynamoDbDefinition),
            Elastic=deserialize_list(json_data.get("Elastic"), ElasticDefinition),
            ElasticacheRedis=deserialize_list(json_data.get("ElasticacheRedis"), ElasticacheRedisDefinition),
            GoogleGke=deserialize_list(json_data.get("GoogleGke"), GoogleGkeDefinition),
            GoogleGkeUserImpersonation=deserialize_list(json_data.get("GoogleGkeUserImpersonation"), GoogleGkeUserImpersonationDefinition),
            Greenplum=deserialize_list(json_data.get("Greenplum"), GreenplumDefinition),
            HttpAuth=deserialize_list(json_data.get("HttpAuth"), HttpAuthDefinition),
            HttpBasicAuth=deserialize_list(json_data.get("HttpBasicAuth"), HttpBasicAuthDefinition),
            HttpNoAuth=deserialize_list(json_data.get("HttpNoAuth"), HttpNoAuthDefinition),
            Kubernetes=deserialize_list(json_data.get("Kubernetes"), KubernetesDefinition),
            KubernetesBasicAuth=deserialize_list(json_data.get("KubernetesBasicAuth"), KubernetesBasicAuthDefinition),
            KubernetesServiceAccount=deserialize_list(json_data.get("KubernetesServiceAccount"), KubernetesServiceAccountDefinition),
            KubernetesServiceAccountUserImpersonation=deserialize_list(json_data.get("KubernetesServiceAccountUserImpersonation"), KubernetesServiceAccountUserImpersonationDefinition),
            KubernetesUserImpersonation=deserialize_list(json_data.get("KubernetesUserImpersonation"), KubernetesUserImpersonationDefinition),
            Maria=deserialize_list(json_data.get("Maria"), MariaDefinition),
            Memcached=deserialize_list(json_data.get("Memcached"), MemcachedDefinition),
            Memsql=deserialize_list(json_data.get("Memsql"), MemsqlDefinition),
            MongoHost=deserialize_list(json_data.get("MongoHost"), MongoHostDefinition),
            MongoLegacyHost=deserialize_list(json_data.get("MongoLegacyHost"), MongoLegacyHostDefinition),
            MongoLegacyReplicaset=deserialize_list(json_data.get("MongoLegacyReplicaset"), MongoLegacyReplicasetDefinition),
            MongoReplicaSet=deserialize_list(json_data.get("MongoReplicaSet"), MongoReplicaSetDefinition),
            Mysql=deserialize_list(json_data.get("Mysql"), MysqlDefinition),
            Oracle=deserialize_list(json_data.get("Oracle"), OracleDefinition),
            Postgres=deserialize_list(json_data.get("Postgres"), PostgresDefinition),
            Presto=deserialize_list(json_data.get("Presto"), PrestoDefinition),
            RabbitmqAmqp091=deserialize_list(json_data.get("RabbitmqAmqp091"), RabbitmqAmqp091Definition),
            Rdp=deserialize_list(json_data.get("Rdp"), RdpDefinition),
            Redis=deserialize_list(json_data.get("Redis"), RedisDefinition),
            Redshift=deserialize_list(json_data.get("Redshift"), RedshiftDefinition),
            Snowflake=deserialize_list(json_data.get("Snowflake"), SnowflakeDefinition),
            SqlServer=deserialize_list(json_data.get("SqlServer"), SqlServerDefinition),
            Ssh=deserialize_list(json_data.get("Ssh"), SshDefinition),
            SshCert=deserialize_list(json_data.get("SshCert"), SshCertDefinition),
            SshCustomerKey=deserialize_list(json_data.get("SshCustomerKey"), SshCustomerKeyDefinition),
            Sybase=deserialize_list(json_data.get("Sybase"), SybaseDefinition),
            SybaseIq=deserialize_list(json_data.get("SybaseIq"), SybaseIqDefinition),
            Teradata=deserialize_list(json_data.get("Teradata"), TeradataDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AksDefinition(BaseModel):
    CertificateAuthority: Optional[str]
    ClientCertificate: Optional[str]
    ClientKey: Optional[str]
    EgressFilter: Optional[str]
    HealthcheckNamespace: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    SecretStoreCertificateAuthorityKey: Optional[str]
    SecretStoreCertificateAuthorityPath: Optional[str]
    SecretStoreClientCertificateKey: Optional[str]
    SecretStoreClientCertificatePath: Optional[str]
    SecretStoreClientKeyKey: Optional[str]
    SecretStoreClientKeyPath: Optional[str]
    SecretStoreId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AksDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateAuthority=json_data.get("CertificateAuthority"),
            ClientCertificate=json_data.get("ClientCertificate"),
            ClientKey=json_data.get("ClientKey"),
            EgressFilter=json_data.get("EgressFilter"),
            HealthcheckNamespace=json_data.get("HealthcheckNamespace"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            SecretStoreCertificateAuthorityKey=json_data.get("SecretStoreCertificateAuthorityKey"),
            SecretStoreCertificateAuthorityPath=json_data.get("SecretStoreCertificateAuthorityPath"),
            SecretStoreClientCertificateKey=json_data.get("SecretStoreClientCertificateKey"),
            SecretStoreClientCertificatePath=json_data.get("SecretStoreClientCertificatePath"),
            SecretStoreClientKeyKey=json_data.get("SecretStoreClientKeyKey"),
            SecretStoreClientKeyPath=json_data.get("SecretStoreClientKeyPath"),
            SecretStoreId=json_data.get("SecretStoreId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AksDefinition = AksDefinition


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
class AksBasicAuthDefinition(BaseModel):
    EgressFilter: Optional[str]
    HealthcheckNamespace: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition2"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AksBasicAuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AksBasicAuthDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            HealthcheckNamespace=json_data.get("HealthcheckNamespace"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition2),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AksBasicAuthDefinition = AksBasicAuthDefinition


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
class AksServiceAccountDefinition(BaseModel):
    EgressFilter: Optional[str]
    HealthcheckNamespace: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStoreTokenKey: Optional[str]
    SecretStoreTokenPath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition3"]]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AksServiceAccountDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AksServiceAccountDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            HealthcheckNamespace=json_data.get("HealthcheckNamespace"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStoreTokenKey=json_data.get("SecretStoreTokenKey"),
            SecretStoreTokenPath=json_data.get("SecretStoreTokenPath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition3),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AksServiceAccountDefinition = AksServiceAccountDefinition


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
class AksServiceAccountUserImpersonationDefinition(BaseModel):
    EgressFilter: Optional[str]
    HealthcheckNamespace: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStoreTokenKey: Optional[str]
    SecretStoreTokenPath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition4"]]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AksServiceAccountUserImpersonationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AksServiceAccountUserImpersonationDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            HealthcheckNamespace=json_data.get("HealthcheckNamespace"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStoreTokenKey=json_data.get("SecretStoreTokenKey"),
            SecretStoreTokenPath=json_data.get("SecretStoreTokenPath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition4),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AksServiceAccountUserImpersonationDefinition = AksServiceAccountUserImpersonationDefinition


@dataclass
class TagsDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition4 = TagsDefinition4


@dataclass
class AksUserImpersonationDefinition(BaseModel):
    CertificateAuthority: Optional[str]
    ClientCertificate: Optional[str]
    ClientKey: Optional[str]
    EgressFilter: Optional[str]
    HealthcheckNamespace: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    SecretStoreCertificateAuthorityKey: Optional[str]
    SecretStoreCertificateAuthorityPath: Optional[str]
    SecretStoreClientCertificateKey: Optional[str]
    SecretStoreClientCertificatePath: Optional[str]
    SecretStoreClientKeyKey: Optional[str]
    SecretStoreClientKeyPath: Optional[str]
    SecretStoreId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition5"]]

    @classmethod
    def _deserialize(
        cls: Type["_AksUserImpersonationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AksUserImpersonationDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateAuthority=json_data.get("CertificateAuthority"),
            ClientCertificate=json_data.get("ClientCertificate"),
            ClientKey=json_data.get("ClientKey"),
            EgressFilter=json_data.get("EgressFilter"),
            HealthcheckNamespace=json_data.get("HealthcheckNamespace"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            SecretStoreCertificateAuthorityKey=json_data.get("SecretStoreCertificateAuthorityKey"),
            SecretStoreCertificateAuthorityPath=json_data.get("SecretStoreCertificateAuthorityPath"),
            SecretStoreClientCertificateKey=json_data.get("SecretStoreClientCertificateKey"),
            SecretStoreClientCertificatePath=json_data.get("SecretStoreClientCertificatePath"),
            SecretStoreClientKeyKey=json_data.get("SecretStoreClientKeyKey"),
            SecretStoreClientKeyPath=json_data.get("SecretStoreClientKeyPath"),
            SecretStoreId=json_data.get("SecretStoreId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition5),
        )


# work around possible type aliasing issues when variable has same name as a model
_AksUserImpersonationDefinition = AksUserImpersonationDefinition


@dataclass
class TagsDefinition5(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition5"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition5 = TagsDefinition5


@dataclass
class AmazonEksDefinition(BaseModel):
    AccessKey: Optional[str]
    CertificateAuthority: Optional[str]
    ClusterName: Optional[str]
    EgressFilter: Optional[str]
    Endpoint: Optional[str]
    HealthcheckNamespace: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
    RoleArn: Optional[str]
    RoleExternalId: Optional[str]
    SecretAccessKey: Optional[str]
    SecretStoreAccessKeyKey: Optional[str]
    SecretStoreAccessKeyPath: Optional[str]
    SecretStoreCertificateAuthorityKey: Optional[str]
    SecretStoreCertificateAuthorityPath: Optional[str]
    SecretStoreId: Optional[str]
    SecretStoreRoleArnKey: Optional[str]
    SecretStoreRoleArnPath: Optional[str]
    SecretStoreRoleExternalIdKey: Optional[str]
    SecretStoreRoleExternalIdPath: Optional[str]
    SecretStoreSecretAccessKeyKey: Optional[str]
    SecretStoreSecretAccessKeyPath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition6"]]

    @classmethod
    def _deserialize(
        cls: Type["_AmazonEksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmazonEksDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            CertificateAuthority=json_data.get("CertificateAuthority"),
            ClusterName=json_data.get("ClusterName"),
            EgressFilter=json_data.get("EgressFilter"),
            Endpoint=json_data.get("Endpoint"),
            HealthcheckNamespace=json_data.get("HealthcheckNamespace"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            RoleArn=json_data.get("RoleArn"),
            RoleExternalId=json_data.get("RoleExternalId"),
            SecretAccessKey=json_data.get("SecretAccessKey"),
            SecretStoreAccessKeyKey=json_data.get("SecretStoreAccessKeyKey"),
            SecretStoreAccessKeyPath=json_data.get("SecretStoreAccessKeyPath"),
            SecretStoreCertificateAuthorityKey=json_data.get("SecretStoreCertificateAuthorityKey"),
            SecretStoreCertificateAuthorityPath=json_data.get("SecretStoreCertificateAuthorityPath"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStoreRoleArnKey=json_data.get("SecretStoreRoleArnKey"),
            SecretStoreRoleArnPath=json_data.get("SecretStoreRoleArnPath"),
            SecretStoreRoleExternalIdKey=json_data.get("SecretStoreRoleExternalIdKey"),
            SecretStoreRoleExternalIdPath=json_data.get("SecretStoreRoleExternalIdPath"),
            SecretStoreSecretAccessKeyKey=json_data.get("SecretStoreSecretAccessKeyKey"),
            SecretStoreSecretAccessKeyPath=json_data.get("SecretStoreSecretAccessKeyPath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition6),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmazonEksDefinition = AmazonEksDefinition


@dataclass
class TagsDefinition6(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition6"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition6 = TagsDefinition6


@dataclass
class AmazonEksUserImpersonationDefinition(BaseModel):
    AccessKey: Optional[str]
    CertificateAuthority: Optional[str]
    ClusterName: Optional[str]
    EgressFilter: Optional[str]
    Endpoint: Optional[str]
    HealthcheckNamespace: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
    RoleArn: Optional[str]
    RoleExternalId: Optional[str]
    SecretAccessKey: Optional[str]
    SecretStoreAccessKeyKey: Optional[str]
    SecretStoreAccessKeyPath: Optional[str]
    SecretStoreCertificateAuthorityKey: Optional[str]
    SecretStoreCertificateAuthorityPath: Optional[str]
    SecretStoreId: Optional[str]
    SecretStoreRoleArnKey: Optional[str]
    SecretStoreRoleArnPath: Optional[str]
    SecretStoreRoleExternalIdKey: Optional[str]
    SecretStoreRoleExternalIdPath: Optional[str]
    SecretStoreSecretAccessKeyKey: Optional[str]
    SecretStoreSecretAccessKeyPath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition7"]]

    @classmethod
    def _deserialize(
        cls: Type["_AmazonEksUserImpersonationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmazonEksUserImpersonationDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            CertificateAuthority=json_data.get("CertificateAuthority"),
            ClusterName=json_data.get("ClusterName"),
            EgressFilter=json_data.get("EgressFilter"),
            Endpoint=json_data.get("Endpoint"),
            HealthcheckNamespace=json_data.get("HealthcheckNamespace"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            RoleArn=json_data.get("RoleArn"),
            RoleExternalId=json_data.get("RoleExternalId"),
            SecretAccessKey=json_data.get("SecretAccessKey"),
            SecretStoreAccessKeyKey=json_data.get("SecretStoreAccessKeyKey"),
            SecretStoreAccessKeyPath=json_data.get("SecretStoreAccessKeyPath"),
            SecretStoreCertificateAuthorityKey=json_data.get("SecretStoreCertificateAuthorityKey"),
            SecretStoreCertificateAuthorityPath=json_data.get("SecretStoreCertificateAuthorityPath"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStoreRoleArnKey=json_data.get("SecretStoreRoleArnKey"),
            SecretStoreRoleArnPath=json_data.get("SecretStoreRoleArnPath"),
            SecretStoreRoleExternalIdKey=json_data.get("SecretStoreRoleExternalIdKey"),
            SecretStoreRoleExternalIdPath=json_data.get("SecretStoreRoleExternalIdPath"),
            SecretStoreSecretAccessKeyKey=json_data.get("SecretStoreSecretAccessKeyKey"),
            SecretStoreSecretAccessKeyPath=json_data.get("SecretStoreSecretAccessKeyPath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition7),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmazonEksUserImpersonationDefinition = AmazonEksUserImpersonationDefinition


@dataclass
class TagsDefinition7(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition7"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition7"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition7 = TagsDefinition7


@dataclass
class AmazonEsDefinition(BaseModel):
    AccessKey: Optional[str]
    EgressFilter: Optional[str]
    Endpoint: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
    RoleArn: Optional[str]
    RoleExternalId: Optional[str]
    SecretAccessKey: Optional[str]
    SecretStoreAccessKeyKey: Optional[str]
    SecretStoreAccessKeyPath: Optional[str]
    SecretStoreId: Optional[str]
    SecretStoreRoleArnKey: Optional[str]
    SecretStoreRoleArnPath: Optional[str]
    SecretStoreRoleExternalIdKey: Optional[str]
    SecretStoreRoleExternalIdPath: Optional[str]
    SecretStoreSecretAccessKeyKey: Optional[str]
    SecretStoreSecretAccessKeyPath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition8"]]

    @classmethod
    def _deserialize(
        cls: Type["_AmazonEsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmazonEsDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            EgressFilter=json_data.get("EgressFilter"),
            Endpoint=json_data.get("Endpoint"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            RoleArn=json_data.get("RoleArn"),
            RoleExternalId=json_data.get("RoleExternalId"),
            SecretAccessKey=json_data.get("SecretAccessKey"),
            SecretStoreAccessKeyKey=json_data.get("SecretStoreAccessKeyKey"),
            SecretStoreAccessKeyPath=json_data.get("SecretStoreAccessKeyPath"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStoreRoleArnKey=json_data.get("SecretStoreRoleArnKey"),
            SecretStoreRoleArnPath=json_data.get("SecretStoreRoleArnPath"),
            SecretStoreRoleExternalIdKey=json_data.get("SecretStoreRoleExternalIdKey"),
            SecretStoreRoleExternalIdPath=json_data.get("SecretStoreRoleExternalIdPath"),
            SecretStoreSecretAccessKeyKey=json_data.get("SecretStoreSecretAccessKeyKey"),
            SecretStoreSecretAccessKeyPath=json_data.get("SecretStoreSecretAccessKeyPath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition8),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmazonEsDefinition = AmazonEsDefinition


@dataclass
class TagsDefinition8(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition8"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition8"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition8 = TagsDefinition8


@dataclass
class AmazonmqAmqp091Definition(BaseModel):
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition9"]]
    TlsRequired: Optional[bool]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AmazonmqAmqp091Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmazonmqAmqp091Definition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition9),
            TlsRequired=json_data.get("TlsRequired"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmazonmqAmqp091Definition = AmazonmqAmqp091Definition


@dataclass
class TagsDefinition9(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition9"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition9"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition9 = TagsDefinition9


@dataclass
class AthenaDefinition(BaseModel):
    AccessKey: Optional[str]
    EgressFilter: Optional[str]
    Name: Optional[str]
    Output: Optional[str]
    Region: Optional[str]
    RoleArn: Optional[str]
    RoleExternalId: Optional[str]
    SecretAccessKey: Optional[str]
    SecretStoreAccessKeyKey: Optional[str]
    SecretStoreAccessKeyPath: Optional[str]
    SecretStoreId: Optional[str]
    SecretStoreRoleArnKey: Optional[str]
    SecretStoreRoleArnPath: Optional[str]
    SecretStoreRoleExternalIdKey: Optional[str]
    SecretStoreRoleExternalIdPath: Optional[str]
    SecretStoreSecretAccessKeyKey: Optional[str]
    SecretStoreSecretAccessKeyPath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition10"]]

    @classmethod
    def _deserialize(
        cls: Type["_AthenaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AthenaDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            EgressFilter=json_data.get("EgressFilter"),
            Name=json_data.get("Name"),
            Output=json_data.get("Output"),
            Region=json_data.get("Region"),
            RoleArn=json_data.get("RoleArn"),
            RoleExternalId=json_data.get("RoleExternalId"),
            SecretAccessKey=json_data.get("SecretAccessKey"),
            SecretStoreAccessKeyKey=json_data.get("SecretStoreAccessKeyKey"),
            SecretStoreAccessKeyPath=json_data.get("SecretStoreAccessKeyPath"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStoreRoleArnKey=json_data.get("SecretStoreRoleArnKey"),
            SecretStoreRoleArnPath=json_data.get("SecretStoreRoleArnPath"),
            SecretStoreRoleExternalIdKey=json_data.get("SecretStoreRoleExternalIdKey"),
            SecretStoreRoleExternalIdPath=json_data.get("SecretStoreRoleExternalIdPath"),
            SecretStoreSecretAccessKeyKey=json_data.get("SecretStoreSecretAccessKeyKey"),
            SecretStoreSecretAccessKeyPath=json_data.get("SecretStoreSecretAccessKeyPath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition10),
        )


# work around possible type aliasing issues when variable has same name as a model
_AthenaDefinition = AthenaDefinition


@dataclass
class TagsDefinition10(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition10"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition10"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition10 = TagsDefinition10


@dataclass
class AuroraMysqlDefinition(BaseModel):
    Database: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition11"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuroraMysqlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuroraMysqlDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition11),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuroraMysqlDefinition = AuroraMysqlDefinition


@dataclass
class TagsDefinition11(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition11"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition11"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition11 = TagsDefinition11


@dataclass
class AuroraPostgresDefinition(BaseModel):
    Database: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    OverrideDatabase: Optional[bool]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition12"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuroraPostgresDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuroraPostgresDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            OverrideDatabase=json_data.get("OverrideDatabase"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition12),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuroraPostgresDefinition = AuroraPostgresDefinition


@dataclass
class TagsDefinition12(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition12"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition12"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition12 = TagsDefinition12


@dataclass
class AwsDefinition(BaseModel):
    AccessKey: Optional[str]
    EgressFilter: Optional[str]
    HealthcheckRegion: Optional[str]
    Name: Optional[str]
    RoleArn: Optional[str]
    RoleExternalId: Optional[str]
    SecretAccessKey: Optional[str]
    SecretStoreAccessKeyKey: Optional[str]
    SecretStoreAccessKeyPath: Optional[str]
    SecretStoreId: Optional[str]
    SecretStoreRoleArnKey: Optional[str]
    SecretStoreRoleArnPath: Optional[str]
    SecretStoreRoleExternalIdKey: Optional[str]
    SecretStoreRoleExternalIdPath: Optional[str]
    SecretStoreSecretAccessKeyKey: Optional[str]
    SecretStoreSecretAccessKeyPath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition13"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            EgressFilter=json_data.get("EgressFilter"),
            HealthcheckRegion=json_data.get("HealthcheckRegion"),
            Name=json_data.get("Name"),
            RoleArn=json_data.get("RoleArn"),
            RoleExternalId=json_data.get("RoleExternalId"),
            SecretAccessKey=json_data.get("SecretAccessKey"),
            SecretStoreAccessKeyKey=json_data.get("SecretStoreAccessKeyKey"),
            SecretStoreAccessKeyPath=json_data.get("SecretStoreAccessKeyPath"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStoreRoleArnKey=json_data.get("SecretStoreRoleArnKey"),
            SecretStoreRoleArnPath=json_data.get("SecretStoreRoleArnPath"),
            SecretStoreRoleExternalIdKey=json_data.get("SecretStoreRoleExternalIdKey"),
            SecretStoreRoleExternalIdPath=json_data.get("SecretStoreRoleExternalIdPath"),
            SecretStoreSecretAccessKeyKey=json_data.get("SecretStoreSecretAccessKeyKey"),
            SecretStoreSecretAccessKeyPath=json_data.get("SecretStoreSecretAccessKeyPath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition13),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDefinition = AwsDefinition


@dataclass
class TagsDefinition13(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition13"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition13"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition13 = TagsDefinition13


@dataclass
class BigQueryDefinition(BaseModel):
    EgressFilter: Optional[str]
    Endpoint: Optional[str]
    Name: Optional[str]
    PrivateKey: Optional[str]
    Project: Optional[str]
    SecretStoreId: Optional[str]
    SecretStorePrivateKeyKey: Optional[str]
    SecretStorePrivateKeyPath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition14"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BigQueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BigQueryDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            Endpoint=json_data.get("Endpoint"),
            Name=json_data.get("Name"),
            PrivateKey=json_data.get("PrivateKey"),
            Project=json_data.get("Project"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePrivateKeyKey=json_data.get("SecretStorePrivateKeyKey"),
            SecretStorePrivateKeyPath=json_data.get("SecretStorePrivateKeyPath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition14),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BigQueryDefinition = BigQueryDefinition


@dataclass
class TagsDefinition14(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition14"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition14"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition14 = TagsDefinition14


@dataclass
class CassandraDefinition(BaseModel):
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition15"]]
    TlsRequired: Optional[bool]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CassandraDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CassandraDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition15),
            TlsRequired=json_data.get("TlsRequired"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CassandraDefinition = CassandraDefinition


@dataclass
class TagsDefinition15(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition15"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition15"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition15 = TagsDefinition15


@dataclass
class CitusDefinition(BaseModel):
    Database: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    OverrideDatabase: Optional[bool]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition16"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CitusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CitusDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            OverrideDatabase=json_data.get("OverrideDatabase"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition16),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CitusDefinition = CitusDefinition


@dataclass
class TagsDefinition16(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition16"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition16"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition16 = TagsDefinition16


@dataclass
class ClustrixDefinition(BaseModel):
    Database: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition17"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClustrixDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClustrixDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition17),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClustrixDefinition = ClustrixDefinition


@dataclass
class TagsDefinition17(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition17"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition17"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition17 = TagsDefinition17


@dataclass
class CockroachDefinition(BaseModel):
    Database: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    OverrideDatabase: Optional[bool]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition18"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CockroachDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CockroachDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            OverrideDatabase=json_data.get("OverrideDatabase"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition18),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CockroachDefinition = CockroachDefinition


@dataclass
class TagsDefinition18(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition18"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition18"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition18 = TagsDefinition18


@dataclass
class Db2IDefinition(BaseModel):
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition19"]]
    TlsRequired: Optional[bool]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Db2IDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Db2IDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition19),
            TlsRequired=json_data.get("TlsRequired"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Db2IDefinition = Db2IDefinition


@dataclass
class TagsDefinition19(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition19"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition19"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition19 = TagsDefinition19


@dataclass
class Db2LuwDefinition(BaseModel):
    Database: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition20"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Db2LuwDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Db2LuwDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition20),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Db2LuwDefinition = Db2LuwDefinition


@dataclass
class TagsDefinition20(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition20"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition20"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition20 = TagsDefinition20


@dataclass
class DruidDefinition(BaseModel):
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition21"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DruidDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DruidDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition21),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DruidDefinition = DruidDefinition


@dataclass
class TagsDefinition21(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition21"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition21"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition21 = TagsDefinition21


@dataclass
class DynamoDbDefinition(BaseModel):
    AccessKey: Optional[str]
    EgressFilter: Optional[str]
    Endpoint: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
    RoleArn: Optional[str]
    RoleExternalId: Optional[str]
    SecretAccessKey: Optional[str]
    SecretStoreAccessKeyKey: Optional[str]
    SecretStoreAccessKeyPath: Optional[str]
    SecretStoreId: Optional[str]
    SecretStoreRoleArnKey: Optional[str]
    SecretStoreRoleArnPath: Optional[str]
    SecretStoreRoleExternalIdKey: Optional[str]
    SecretStoreRoleExternalIdPath: Optional[str]
    SecretStoreSecretAccessKeyKey: Optional[str]
    SecretStoreSecretAccessKeyPath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition22"]]

    @classmethod
    def _deserialize(
        cls: Type["_DynamoDbDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamoDbDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            EgressFilter=json_data.get("EgressFilter"),
            Endpoint=json_data.get("Endpoint"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            RoleArn=json_data.get("RoleArn"),
            RoleExternalId=json_data.get("RoleExternalId"),
            SecretAccessKey=json_data.get("SecretAccessKey"),
            SecretStoreAccessKeyKey=json_data.get("SecretStoreAccessKeyKey"),
            SecretStoreAccessKeyPath=json_data.get("SecretStoreAccessKeyPath"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStoreRoleArnKey=json_data.get("SecretStoreRoleArnKey"),
            SecretStoreRoleArnPath=json_data.get("SecretStoreRoleArnPath"),
            SecretStoreRoleExternalIdKey=json_data.get("SecretStoreRoleExternalIdKey"),
            SecretStoreRoleExternalIdPath=json_data.get("SecretStoreRoleExternalIdPath"),
            SecretStoreSecretAccessKeyKey=json_data.get("SecretStoreSecretAccessKeyKey"),
            SecretStoreSecretAccessKeyPath=json_data.get("SecretStoreSecretAccessKeyPath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition22),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamoDbDefinition = DynamoDbDefinition


@dataclass
class TagsDefinition22(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition22"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition22"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition22 = TagsDefinition22


@dataclass
class ElasticDefinition(BaseModel):
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition23"]]
    TlsRequired: Optional[bool]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition23),
            TlsRequired=json_data.get("TlsRequired"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticDefinition = ElasticDefinition


@dataclass
class TagsDefinition23(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition23"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition23"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition23 = TagsDefinition23


@dataclass
class ElasticacheRedisDefinition(BaseModel):
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition24"]]
    TlsRequired: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticacheRedisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticacheRedisDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition24),
            TlsRequired=json_data.get("TlsRequired"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticacheRedisDefinition = ElasticacheRedisDefinition


@dataclass
class TagsDefinition24(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition24"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition24"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition24 = TagsDefinition24


@dataclass
class GoogleGkeDefinition(BaseModel):
    CertificateAuthority: Optional[str]
    EgressFilter: Optional[str]
    Endpoint: Optional[str]
    HealthcheckNamespace: Optional[str]
    Name: Optional[str]
    SecretStoreCertificateAuthorityKey: Optional[str]
    SecretStoreCertificateAuthorityPath: Optional[str]
    SecretStoreId: Optional[str]
    SecretStoreServiceAccountKeyKey: Optional[str]
    SecretStoreServiceAccountKeyPath: Optional[str]
    ServiceAccountKey: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition25"]]

    @classmethod
    def _deserialize(
        cls: Type["_GoogleGkeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GoogleGkeDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateAuthority=json_data.get("CertificateAuthority"),
            EgressFilter=json_data.get("EgressFilter"),
            Endpoint=json_data.get("Endpoint"),
            HealthcheckNamespace=json_data.get("HealthcheckNamespace"),
            Name=json_data.get("Name"),
            SecretStoreCertificateAuthorityKey=json_data.get("SecretStoreCertificateAuthorityKey"),
            SecretStoreCertificateAuthorityPath=json_data.get("SecretStoreCertificateAuthorityPath"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStoreServiceAccountKeyKey=json_data.get("SecretStoreServiceAccountKeyKey"),
            SecretStoreServiceAccountKeyPath=json_data.get("SecretStoreServiceAccountKeyPath"),
            ServiceAccountKey=json_data.get("ServiceAccountKey"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition25),
        )


# work around possible type aliasing issues when variable has same name as a model
_GoogleGkeDefinition = GoogleGkeDefinition


@dataclass
class TagsDefinition25(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition25"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition25"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition25 = TagsDefinition25


@dataclass
class GoogleGkeUserImpersonationDefinition(BaseModel):
    CertificateAuthority: Optional[str]
    EgressFilter: Optional[str]
    Endpoint: Optional[str]
    HealthcheckNamespace: Optional[str]
    Name: Optional[str]
    SecretStoreCertificateAuthorityKey: Optional[str]
    SecretStoreCertificateAuthorityPath: Optional[str]
    SecretStoreId: Optional[str]
    SecretStoreServiceAccountKeyKey: Optional[str]
    SecretStoreServiceAccountKeyPath: Optional[str]
    ServiceAccountKey: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition26"]]

    @classmethod
    def _deserialize(
        cls: Type["_GoogleGkeUserImpersonationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GoogleGkeUserImpersonationDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateAuthority=json_data.get("CertificateAuthority"),
            EgressFilter=json_data.get("EgressFilter"),
            Endpoint=json_data.get("Endpoint"),
            HealthcheckNamespace=json_data.get("HealthcheckNamespace"),
            Name=json_data.get("Name"),
            SecretStoreCertificateAuthorityKey=json_data.get("SecretStoreCertificateAuthorityKey"),
            SecretStoreCertificateAuthorityPath=json_data.get("SecretStoreCertificateAuthorityPath"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStoreServiceAccountKeyKey=json_data.get("SecretStoreServiceAccountKeyKey"),
            SecretStoreServiceAccountKeyPath=json_data.get("SecretStoreServiceAccountKeyPath"),
            ServiceAccountKey=json_data.get("ServiceAccountKey"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition26),
        )


# work around possible type aliasing issues when variable has same name as a model
_GoogleGkeUserImpersonationDefinition = GoogleGkeUserImpersonationDefinition


@dataclass
class TagsDefinition26(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition26"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition26"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition26 = TagsDefinition26


@dataclass
class GreenplumDefinition(BaseModel):
    Database: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    OverrideDatabase: Optional[bool]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition27"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GreenplumDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GreenplumDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            OverrideDatabase=json_data.get("OverrideDatabase"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition27),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GreenplumDefinition = GreenplumDefinition


@dataclass
class TagsDefinition27(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition27"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition27"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition27 = TagsDefinition27


@dataclass
class HttpAuthDefinition(BaseModel):
    AuthHeader: Optional[str]
    DefaultPath: Optional[str]
    EgressFilter: Optional[str]
    HeadersBlacklist: Optional[str]
    HealthcheckPath: Optional[str]
    Name: Optional[str]
    SecretStoreAuthHeaderKey: Optional[str]
    SecretStoreAuthHeaderPath: Optional[str]
    SecretStoreId: Optional[str]
    Subdomain: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition28"]]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpAuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpAuthDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthHeader=json_data.get("AuthHeader"),
            DefaultPath=json_data.get("DefaultPath"),
            EgressFilter=json_data.get("EgressFilter"),
            HeadersBlacklist=json_data.get("HeadersBlacklist"),
            HealthcheckPath=json_data.get("HealthcheckPath"),
            Name=json_data.get("Name"),
            SecretStoreAuthHeaderKey=json_data.get("SecretStoreAuthHeaderKey"),
            SecretStoreAuthHeaderPath=json_data.get("SecretStoreAuthHeaderPath"),
            SecretStoreId=json_data.get("SecretStoreId"),
            Subdomain=json_data.get("Subdomain"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition28),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpAuthDefinition = HttpAuthDefinition


@dataclass
class TagsDefinition28(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition28"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition28"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition28 = TagsDefinition28


@dataclass
class HttpBasicAuthDefinition(BaseModel):
    DefaultPath: Optional[str]
    EgressFilter: Optional[str]
    HeadersBlacklist: Optional[str]
    HealthcheckPath: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Subdomain: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition29"]]
    Url: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpBasicAuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpBasicAuthDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultPath=json_data.get("DefaultPath"),
            EgressFilter=json_data.get("EgressFilter"),
            HeadersBlacklist=json_data.get("HeadersBlacklist"),
            HealthcheckPath=json_data.get("HealthcheckPath"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Subdomain=json_data.get("Subdomain"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition29),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpBasicAuthDefinition = HttpBasicAuthDefinition


@dataclass
class TagsDefinition29(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition29"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition29"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition29 = TagsDefinition29


@dataclass
class HttpNoAuthDefinition(BaseModel):
    DefaultPath: Optional[str]
    EgressFilter: Optional[str]
    HeadersBlacklist: Optional[str]
    HealthcheckPath: Optional[str]
    Name: Optional[str]
    SecretStoreId: Optional[str]
    Subdomain: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition30"]]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpNoAuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpNoAuthDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultPath=json_data.get("DefaultPath"),
            EgressFilter=json_data.get("EgressFilter"),
            HeadersBlacklist=json_data.get("HeadersBlacklist"),
            HealthcheckPath=json_data.get("HealthcheckPath"),
            Name=json_data.get("Name"),
            SecretStoreId=json_data.get("SecretStoreId"),
            Subdomain=json_data.get("Subdomain"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition30),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpNoAuthDefinition = HttpNoAuthDefinition


@dataclass
class TagsDefinition30(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition30"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition30"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition30 = TagsDefinition30


@dataclass
class KubernetesDefinition(BaseModel):
    CertificateAuthority: Optional[str]
    ClientCertificate: Optional[str]
    ClientKey: Optional[str]
    EgressFilter: Optional[str]
    HealthcheckNamespace: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    SecretStoreCertificateAuthorityKey: Optional[str]
    SecretStoreCertificateAuthorityPath: Optional[str]
    SecretStoreClientCertificateKey: Optional[str]
    SecretStoreClientCertificatePath: Optional[str]
    SecretStoreClientKeyKey: Optional[str]
    SecretStoreClientKeyPath: Optional[str]
    SecretStoreId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition31"]]

    @classmethod
    def _deserialize(
        cls: Type["_KubernetesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubernetesDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateAuthority=json_data.get("CertificateAuthority"),
            ClientCertificate=json_data.get("ClientCertificate"),
            ClientKey=json_data.get("ClientKey"),
            EgressFilter=json_data.get("EgressFilter"),
            HealthcheckNamespace=json_data.get("HealthcheckNamespace"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            SecretStoreCertificateAuthorityKey=json_data.get("SecretStoreCertificateAuthorityKey"),
            SecretStoreCertificateAuthorityPath=json_data.get("SecretStoreCertificateAuthorityPath"),
            SecretStoreClientCertificateKey=json_data.get("SecretStoreClientCertificateKey"),
            SecretStoreClientCertificatePath=json_data.get("SecretStoreClientCertificatePath"),
            SecretStoreClientKeyKey=json_data.get("SecretStoreClientKeyKey"),
            SecretStoreClientKeyPath=json_data.get("SecretStoreClientKeyPath"),
            SecretStoreId=json_data.get("SecretStoreId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition31),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubernetesDefinition = KubernetesDefinition


@dataclass
class TagsDefinition31(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition31"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition31"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition31 = TagsDefinition31


@dataclass
class KubernetesBasicAuthDefinition(BaseModel):
    EgressFilter: Optional[str]
    HealthcheckNamespace: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition32"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubernetesBasicAuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubernetesBasicAuthDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            HealthcheckNamespace=json_data.get("HealthcheckNamespace"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition32),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubernetesBasicAuthDefinition = KubernetesBasicAuthDefinition


@dataclass
class TagsDefinition32(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition32"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition32"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition32 = TagsDefinition32


@dataclass
class KubernetesServiceAccountDefinition(BaseModel):
    EgressFilter: Optional[str]
    HealthcheckNamespace: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStoreTokenKey: Optional[str]
    SecretStoreTokenPath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition33"]]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubernetesServiceAccountDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubernetesServiceAccountDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            HealthcheckNamespace=json_data.get("HealthcheckNamespace"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStoreTokenKey=json_data.get("SecretStoreTokenKey"),
            SecretStoreTokenPath=json_data.get("SecretStoreTokenPath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition33),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubernetesServiceAccountDefinition = KubernetesServiceAccountDefinition


@dataclass
class TagsDefinition33(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition33"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition33"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition33 = TagsDefinition33


@dataclass
class KubernetesServiceAccountUserImpersonationDefinition(BaseModel):
    EgressFilter: Optional[str]
    HealthcheckNamespace: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStoreTokenKey: Optional[str]
    SecretStoreTokenPath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition34"]]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubernetesServiceAccountUserImpersonationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubernetesServiceAccountUserImpersonationDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            HealthcheckNamespace=json_data.get("HealthcheckNamespace"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStoreTokenKey=json_data.get("SecretStoreTokenKey"),
            SecretStoreTokenPath=json_data.get("SecretStoreTokenPath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition34),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubernetesServiceAccountUserImpersonationDefinition = KubernetesServiceAccountUserImpersonationDefinition


@dataclass
class TagsDefinition34(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition34"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition34"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition34 = TagsDefinition34


@dataclass
class KubernetesUserImpersonationDefinition(BaseModel):
    CertificateAuthority: Optional[str]
    ClientCertificate: Optional[str]
    ClientKey: Optional[str]
    EgressFilter: Optional[str]
    HealthcheckNamespace: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    SecretStoreCertificateAuthorityKey: Optional[str]
    SecretStoreCertificateAuthorityPath: Optional[str]
    SecretStoreClientCertificateKey: Optional[str]
    SecretStoreClientCertificatePath: Optional[str]
    SecretStoreClientKeyKey: Optional[str]
    SecretStoreClientKeyPath: Optional[str]
    SecretStoreId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition35"]]

    @classmethod
    def _deserialize(
        cls: Type["_KubernetesUserImpersonationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubernetesUserImpersonationDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateAuthority=json_data.get("CertificateAuthority"),
            ClientCertificate=json_data.get("ClientCertificate"),
            ClientKey=json_data.get("ClientKey"),
            EgressFilter=json_data.get("EgressFilter"),
            HealthcheckNamespace=json_data.get("HealthcheckNamespace"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            SecretStoreCertificateAuthorityKey=json_data.get("SecretStoreCertificateAuthorityKey"),
            SecretStoreCertificateAuthorityPath=json_data.get("SecretStoreCertificateAuthorityPath"),
            SecretStoreClientCertificateKey=json_data.get("SecretStoreClientCertificateKey"),
            SecretStoreClientCertificatePath=json_data.get("SecretStoreClientCertificatePath"),
            SecretStoreClientKeyKey=json_data.get("SecretStoreClientKeyKey"),
            SecretStoreClientKeyPath=json_data.get("SecretStoreClientKeyPath"),
            SecretStoreId=json_data.get("SecretStoreId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition35),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubernetesUserImpersonationDefinition = KubernetesUserImpersonationDefinition


@dataclass
class TagsDefinition35(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition35"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition35"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition35 = TagsDefinition35


@dataclass
class MariaDefinition(BaseModel):
    Database: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition36"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MariaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MariaDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition36),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MariaDefinition = MariaDefinition


@dataclass
class TagsDefinition36(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition36"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition36"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition36 = TagsDefinition36


@dataclass
class MemcachedDefinition(BaseModel):
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition37"]]

    @classmethod
    def _deserialize(
        cls: Type["_MemcachedDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemcachedDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition37),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemcachedDefinition = MemcachedDefinition


@dataclass
class TagsDefinition37(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition37"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition37"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition37 = TagsDefinition37


@dataclass
class MemsqlDefinition(BaseModel):
    Database: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition38"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MemsqlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemsqlDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition38),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemsqlDefinition = MemsqlDefinition


@dataclass
class TagsDefinition38(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition38"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition38"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition38 = TagsDefinition38


@dataclass
class MongoHostDefinition(BaseModel):
    AuthDatabase: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition39"]]
    TlsRequired: Optional[bool]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MongoHostDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MongoHostDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthDatabase=json_data.get("AuthDatabase"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition39),
            TlsRequired=json_data.get("TlsRequired"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MongoHostDefinition = MongoHostDefinition


@dataclass
class TagsDefinition39(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition39"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition39"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition39 = TagsDefinition39


@dataclass
class MongoLegacyHostDefinition(BaseModel):
    AuthDatabase: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    ReplicaSet: Optional[str]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition40"]]
    TlsRequired: Optional[bool]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MongoLegacyHostDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MongoLegacyHostDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthDatabase=json_data.get("AuthDatabase"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            ReplicaSet=json_data.get("ReplicaSet"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition40),
            TlsRequired=json_data.get("TlsRequired"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MongoLegacyHostDefinition = MongoLegacyHostDefinition


@dataclass
class TagsDefinition40(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition40"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition40"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition40 = TagsDefinition40


@dataclass
class MongoLegacyReplicasetDefinition(BaseModel):
    AuthDatabase: Optional[str]
    ConnectToReplica: Optional[bool]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    ReplicaSet: Optional[str]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition41"]]
    TlsRequired: Optional[bool]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MongoLegacyReplicasetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MongoLegacyReplicasetDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthDatabase=json_data.get("AuthDatabase"),
            ConnectToReplica=json_data.get("ConnectToReplica"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            ReplicaSet=json_data.get("ReplicaSet"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition41),
            TlsRequired=json_data.get("TlsRequired"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MongoLegacyReplicasetDefinition = MongoLegacyReplicasetDefinition


@dataclass
class TagsDefinition41(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition41"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition41"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition41 = TagsDefinition41


@dataclass
class MongoReplicaSetDefinition(BaseModel):
    AuthDatabase: Optional[str]
    ConnectToReplica: Optional[bool]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    ReplicaSet: Optional[str]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition42"]]
    TlsRequired: Optional[bool]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MongoReplicaSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MongoReplicaSetDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthDatabase=json_data.get("AuthDatabase"),
            ConnectToReplica=json_data.get("ConnectToReplica"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            ReplicaSet=json_data.get("ReplicaSet"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition42),
            TlsRequired=json_data.get("TlsRequired"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MongoReplicaSetDefinition = MongoReplicaSetDefinition


@dataclass
class TagsDefinition42(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition42"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition42"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition42 = TagsDefinition42


@dataclass
class MysqlDefinition(BaseModel):
    Database: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition43"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MysqlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MysqlDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition43),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MysqlDefinition = MysqlDefinition


@dataclass
class TagsDefinition43(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition43"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition43"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition43 = TagsDefinition43


@dataclass
class OracleDefinition(BaseModel):
    Database: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition44"]]
    TlsRequired: Optional[bool]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OracleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OracleDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition44),
            TlsRequired=json_data.get("TlsRequired"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OracleDefinition = OracleDefinition


@dataclass
class TagsDefinition44(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition44"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition44"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition44 = TagsDefinition44


@dataclass
class PostgresDefinition(BaseModel):
    Database: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    OverrideDatabase: Optional[bool]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition45"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PostgresDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PostgresDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            OverrideDatabase=json_data.get("OverrideDatabase"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition45),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PostgresDefinition = PostgresDefinition


@dataclass
class TagsDefinition45(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition45"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition45"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition45 = TagsDefinition45


@dataclass
class PrestoDefinition(BaseModel):
    Database: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition46"]]
    TlsRequired: Optional[bool]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrestoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrestoDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition46),
            TlsRequired=json_data.get("TlsRequired"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrestoDefinition = PrestoDefinition


@dataclass
class TagsDefinition46(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition46"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition46"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition46 = TagsDefinition46


@dataclass
class RabbitmqAmqp091Definition(BaseModel):
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition47"]]
    TlsRequired: Optional[bool]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RabbitmqAmqp091Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RabbitmqAmqp091Definition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition47),
            TlsRequired=json_data.get("TlsRequired"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RabbitmqAmqp091Definition = RabbitmqAmqp091Definition


@dataclass
class TagsDefinition47(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition47"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition47"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition47 = TagsDefinition47


@dataclass
class RdpDefinition(BaseModel):
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition48"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RdpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RdpDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition48),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RdpDefinition = RdpDefinition


@dataclass
class TagsDefinition48(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition48"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition48"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition48 = TagsDefinition48


@dataclass
class RedisDefinition(BaseModel):
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition49"]]

    @classmethod
    def _deserialize(
        cls: Type["_RedisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedisDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition49),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedisDefinition = RedisDefinition


@dataclass
class TagsDefinition49(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition49"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition49"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition49 = TagsDefinition49


@dataclass
class RedshiftDefinition(BaseModel):
    Database: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    OverrideDatabase: Optional[bool]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition50"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedshiftDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedshiftDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            OverrideDatabase=json_data.get("OverrideDatabase"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition50),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedshiftDefinition = RedshiftDefinition


@dataclass
class TagsDefinition50(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition50"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition50"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition50 = TagsDefinition50


@dataclass
class SnowflakeDefinition(BaseModel):
    Database: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Schema: Optional[str]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition51"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnowflakeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnowflakeDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Schema=json_data.get("Schema"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition51),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnowflakeDefinition = SnowflakeDefinition


@dataclass
class TagsDefinition51(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition51"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition51"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition51 = TagsDefinition51


@dataclass
class SqlServerDefinition(BaseModel):
    Database: Optional[str]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    OverrideDatabase: Optional[bool]
    Password: Optional[str]
    Port: Optional[float]
    Schema: Optional[str]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition52"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SqlServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SqlServerDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=json_data.get("Database"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            OverrideDatabase=json_data.get("OverrideDatabase"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Schema=json_data.get("Schema"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition52),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SqlServerDefinition = SqlServerDefinition


@dataclass
class TagsDefinition52(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition52"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition52"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition52 = TagsDefinition52


@dataclass
class SshDefinition(BaseModel):
    AllowDeprecatedKeyExchanges: Optional[bool]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    PortForwarding: Optional[bool]
    SecretStoreId: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition53"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SshDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SshDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowDeprecatedKeyExchanges=json_data.get("AllowDeprecatedKeyExchanges"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            PortForwarding=json_data.get("PortForwarding"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition53),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SshDefinition = SshDefinition


@dataclass
class TagsDefinition53(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition53"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition53"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition53 = TagsDefinition53


@dataclass
class SshCertDefinition(BaseModel):
    AllowDeprecatedKeyExchanges: Optional[bool]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    PortForwarding: Optional[bool]
    SecretStoreId: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition54"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SshCertDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SshCertDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowDeprecatedKeyExchanges=json_data.get("AllowDeprecatedKeyExchanges"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            PortForwarding=json_data.get("PortForwarding"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition54),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SshCertDefinition = SshCertDefinition


@dataclass
class TagsDefinition54(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition54"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition54"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition54 = TagsDefinition54


@dataclass
class SshCustomerKeyDefinition(BaseModel):
    AllowDeprecatedKeyExchanges: Optional[bool]
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    PortForwarding: Optional[bool]
    PrivateKey: Optional[str]
    SecretStoreId: Optional[str]
    SecretStorePrivateKeyKey: Optional[str]
    SecretStorePrivateKeyPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition55"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SshCustomerKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SshCustomerKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowDeprecatedKeyExchanges=json_data.get("AllowDeprecatedKeyExchanges"),
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            PortForwarding=json_data.get("PortForwarding"),
            PrivateKey=json_data.get("PrivateKey"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePrivateKeyKey=json_data.get("SecretStorePrivateKeyKey"),
            SecretStorePrivateKeyPath=json_data.get("SecretStorePrivateKeyPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition55),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SshCustomerKeyDefinition = SshCustomerKeyDefinition


@dataclass
class TagsDefinition55(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition55"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition55"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition55 = TagsDefinition55


@dataclass
class SybaseDefinition(BaseModel):
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition56"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SybaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SybaseDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition56),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SybaseDefinition = SybaseDefinition


@dataclass
class TagsDefinition56(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition56"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition56"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition56 = TagsDefinition56


@dataclass
class SybaseIqDefinition(BaseModel):
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition57"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SybaseIqDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SybaseIqDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition57),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SybaseIqDefinition = SybaseIqDefinition


@dataclass
class TagsDefinition57(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition57"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition57"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition57 = TagsDefinition57


@dataclass
class TeradataDefinition(BaseModel):
    EgressFilter: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    SecretStoreId: Optional[str]
    SecretStorePasswordKey: Optional[str]
    SecretStorePasswordPath: Optional[str]
    SecretStoreUsernameKey: Optional[str]
    SecretStoreUsernamePath: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition58"]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TeradataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TeradataDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=json_data.get("EgressFilter"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretStoreId=json_data.get("SecretStoreId"),
            SecretStorePasswordKey=json_data.get("SecretStorePasswordKey"),
            SecretStorePasswordPath=json_data.get("SecretStorePasswordPath"),
            SecretStoreUsernameKey=json_data.get("SecretStoreUsernameKey"),
            SecretStoreUsernamePath=json_data.get("SecretStoreUsernamePath"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition58),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TeradataDefinition = TeradataDefinition


@dataclass
class TagsDefinition58(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition58"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition58"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition58 = TagsDefinition58


@dataclass
class TimeoutsDefinition(BaseModel):
    Default: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


