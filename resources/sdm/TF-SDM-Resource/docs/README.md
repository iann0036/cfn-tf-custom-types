# TF::SDM::Resource

A Resource is a database or server for which strongDM manages access.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SDM::Resource",
    "Properties" : {
        "<a href="#aks" title="Aks">Aks</a>" : <i>[ <a href="aksdefinition.md">AksDefinition</a>, ... ]</i>,
        "<a href="#aksbasicauth" title="AksBasicAuth">AksBasicAuth</a>" : <i>[ <a href="aksbasicauthdefinition.md">AksBasicAuthDefinition</a>, ... ]</i>,
        "<a href="#aksserviceaccount" title="AksServiceAccount">AksServiceAccount</a>" : <i>[ <a href="aksserviceaccountdefinition.md">AksServiceAccountDefinition</a>, ... ]</i>,
        "<a href="#aksserviceaccountuserimpersonation" title="AksServiceAccountUserImpersonation">AksServiceAccountUserImpersonation</a>" : <i>[ <a href="aksserviceaccountuserimpersonationdefinition.md">AksServiceAccountUserImpersonationDefinition</a>, ... ]</i>,
        "<a href="#aksuserimpersonation" title="AksUserImpersonation">AksUserImpersonation</a>" : <i>[ <a href="aksuserimpersonationdefinition.md">AksUserImpersonationDefinition</a>, ... ]</i>,
        "<a href="#amazoneks" title="AmazonEks">AmazonEks</a>" : <i>[ <a href="amazoneksdefinition.md">AmazonEksDefinition</a>, ... ]</i>,
        "<a href="#amazoneksuserimpersonation" title="AmazonEksUserImpersonation">AmazonEksUserImpersonation</a>" : <i>[ <a href="amazoneksuserimpersonationdefinition.md">AmazonEksUserImpersonationDefinition</a>, ... ]</i>,
        "<a href="#amazones" title="AmazonEs">AmazonEs</a>" : <i>[ <a href="amazonesdefinition.md">AmazonEsDefinition</a>, ... ]</i>,
        "<a href="#amazonmqamqp091" title="AmazonmqAmqp091">AmazonmqAmqp091</a>" : <i>[ <a href="amazonmqamqp091definition.md">AmazonmqAmqp091Definition</a>, ... ]</i>,
        "<a href="#athena" title="Athena">Athena</a>" : <i>[ <a href="athenadefinition.md">AthenaDefinition</a>, ... ]</i>,
        "<a href="#auroramysql" title="AuroraMysql">AuroraMysql</a>" : <i>[ <a href="auroramysqldefinition.md">AuroraMysqlDefinition</a>, ... ]</i>,
        "<a href="#aurorapostgres" title="AuroraPostgres">AuroraPostgres</a>" : <i>[ <a href="aurorapostgresdefinition.md">AuroraPostgresDefinition</a>, ... ]</i>,
        "<a href="#aws" title="Aws">Aws</a>" : <i>[ <a href="awsdefinition.md">AwsDefinition</a>, ... ]</i>,
        "<a href="#bigquery" title="BigQuery">BigQuery</a>" : <i>[ <a href="bigquerydefinition.md">BigQueryDefinition</a>, ... ]</i>,
        "<a href="#cassandra" title="Cassandra">Cassandra</a>" : <i>[ <a href="cassandradefinition.md">CassandraDefinition</a>, ... ]</i>,
        "<a href="#citus" title="Citus">Citus</a>" : <i>[ <a href="citusdefinition.md">CitusDefinition</a>, ... ]</i>,
        "<a href="#clustrix" title="Clustrix">Clustrix</a>" : <i>[ <a href="clustrixdefinition.md">ClustrixDefinition</a>, ... ]</i>,
        "<a href="#cockroach" title="Cockroach">Cockroach</a>" : <i>[ <a href="cockroachdefinition.md">CockroachDefinition</a>, ... ]</i>,
        "<a href="#db2i" title="Db2I">Db2I</a>" : <i>[ <a href="db2idefinition.md">Db2IDefinition</a>, ... ]</i>,
        "<a href="#db2luw" title="Db2Luw">Db2Luw</a>" : <i>[ <a href="db2luwdefinition.md">Db2LuwDefinition</a>, ... ]</i>,
        "<a href="#druid" title="Druid">Druid</a>" : <i>[ <a href="druiddefinition.md">DruidDefinition</a>, ... ]</i>,
        "<a href="#dynamodb" title="DynamoDb">DynamoDb</a>" : <i>[ <a href="dynamodbdefinition.md">DynamoDbDefinition</a>, ... ]</i>,
        "<a href="#elastic" title="Elastic">Elastic</a>" : <i>[ <a href="elasticdefinition.md">ElasticDefinition</a>, ... ]</i>,
        "<a href="#elasticacheredis" title="ElasticacheRedis">ElasticacheRedis</a>" : <i>[ <a href="elasticacheredisdefinition.md">ElasticacheRedisDefinition</a>, ... ]</i>,
        "<a href="#googlegke" title="GoogleGke">GoogleGke</a>" : <i>[ <a href="googlegkedefinition.md">GoogleGkeDefinition</a>, ... ]</i>,
        "<a href="#googlegkeuserimpersonation" title="GoogleGkeUserImpersonation">GoogleGkeUserImpersonation</a>" : <i>[ <a href="googlegkeuserimpersonationdefinition.md">GoogleGkeUserImpersonationDefinition</a>, ... ]</i>,
        "<a href="#greenplum" title="Greenplum">Greenplum</a>" : <i>[ <a href="greenplumdefinition.md">GreenplumDefinition</a>, ... ]</i>,
        "<a href="#httpauth" title="HttpAuth">HttpAuth</a>" : <i>[ <a href="httpauthdefinition.md">HttpAuthDefinition</a>, ... ]</i>,
        "<a href="#httpbasicauth" title="HttpBasicAuth">HttpBasicAuth</a>" : <i>[ <a href="httpbasicauthdefinition.md">HttpBasicAuthDefinition</a>, ... ]</i>,
        "<a href="#httpnoauth" title="HttpNoAuth">HttpNoAuth</a>" : <i>[ <a href="httpnoauthdefinition.md">HttpNoAuthDefinition</a>, ... ]</i>,
        "<a href="#kubernetes" title="Kubernetes">Kubernetes</a>" : <i>[ <a href="kubernetesdefinition.md">KubernetesDefinition</a>, ... ]</i>,
        "<a href="#kubernetesbasicauth" title="KubernetesBasicAuth">KubernetesBasicAuth</a>" : <i>[ <a href="kubernetesbasicauthdefinition.md">KubernetesBasicAuthDefinition</a>, ... ]</i>,
        "<a href="#kubernetesserviceaccount" title="KubernetesServiceAccount">KubernetesServiceAccount</a>" : <i>[ <a href="kubernetesserviceaccountdefinition.md">KubernetesServiceAccountDefinition</a>, ... ]</i>,
        "<a href="#kubernetesserviceaccountuserimpersonation" title="KubernetesServiceAccountUserImpersonation">KubernetesServiceAccountUserImpersonation</a>" : <i>[ <a href="kubernetesserviceaccountuserimpersonationdefinition.md">KubernetesServiceAccountUserImpersonationDefinition</a>, ... ]</i>,
        "<a href="#kubernetesuserimpersonation" title="KubernetesUserImpersonation">KubernetesUserImpersonation</a>" : <i>[ <a href="kubernetesuserimpersonationdefinition.md">KubernetesUserImpersonationDefinition</a>, ... ]</i>,
        "<a href="#maria" title="Maria">Maria</a>" : <i>[ <a href="mariadefinition.md">MariaDefinition</a>, ... ]</i>,
        "<a href="#memcached" title="Memcached">Memcached</a>" : <i>[ <a href="memcacheddefinition.md">MemcachedDefinition</a>, ... ]</i>,
        "<a href="#memsql" title="Memsql">Memsql</a>" : <i>[ <a href="memsqldefinition.md">MemsqlDefinition</a>, ... ]</i>,
        "<a href="#mongohost" title="MongoHost">MongoHost</a>" : <i>[ <a href="mongohostdefinition.md">MongoHostDefinition</a>, ... ]</i>,
        "<a href="#mongolegacyhost" title="MongoLegacyHost">MongoLegacyHost</a>" : <i>[ <a href="mongolegacyhostdefinition.md">MongoLegacyHostDefinition</a>, ... ]</i>,
        "<a href="#mongolegacyreplicaset" title="MongoLegacyReplicaset">MongoLegacyReplicaset</a>" : <i>[ <a href="mongolegacyreplicasetdefinition.md">MongoLegacyReplicasetDefinition</a>, ... ]</i>,
        "<a href="#mongoreplicaset" title="MongoReplicaSet">MongoReplicaSet</a>" : <i>[ <a href="mongoreplicasetdefinition.md">MongoReplicaSetDefinition</a>, ... ]</i>,
        "<a href="#mysql" title="Mysql">Mysql</a>" : <i>[ <a href="mysqldefinition.md">MysqlDefinition</a>, ... ]</i>,
        "<a href="#oracle" title="Oracle">Oracle</a>" : <i>[ <a href="oracledefinition.md">OracleDefinition</a>, ... ]</i>,
        "<a href="#postgres" title="Postgres">Postgres</a>" : <i>[ <a href="postgresdefinition.md">PostgresDefinition</a>, ... ]</i>,
        "<a href="#presto" title="Presto">Presto</a>" : <i>[ <a href="prestodefinition.md">PrestoDefinition</a>, ... ]</i>,
        "<a href="#rabbitmqamqp091" title="RabbitmqAmqp091">RabbitmqAmqp091</a>" : <i>[ <a href="rabbitmqamqp091definition.md">RabbitmqAmqp091Definition</a>, ... ]</i>,
        "<a href="#rdp" title="Rdp">Rdp</a>" : <i>[ <a href="rdpdefinition.md">RdpDefinition</a>, ... ]</i>,
        "<a href="#redis" title="Redis">Redis</a>" : <i>[ <a href="redisdefinition.md">RedisDefinition</a>, ... ]</i>,
        "<a href="#redshift" title="Redshift">Redshift</a>" : <i>[ <a href="redshiftdefinition.md">RedshiftDefinition</a>, ... ]</i>,
        "<a href="#snowflake" title="Snowflake">Snowflake</a>" : <i>[ <a href="snowflakedefinition.md">SnowflakeDefinition</a>, ... ]</i>,
        "<a href="#sqlserver" title="SqlServer">SqlServer</a>" : <i>[ <a href="sqlserverdefinition.md">SqlServerDefinition</a>, ... ]</i>,
        "<a href="#ssh" title="Ssh">Ssh</a>" : <i>[ <a href="sshdefinition.md">SshDefinition</a>, ... ]</i>,
        "<a href="#sshcert" title="SshCert">SshCert</a>" : <i>[ <a href="sshcertdefinition.md">SshCertDefinition</a>, ... ]</i>,
        "<a href="#sshcustomerkey" title="SshCustomerKey">SshCustomerKey</a>" : <i>[ <a href="sshcustomerkeydefinition.md">SshCustomerKeyDefinition</a>, ... ]</i>,
        "<a href="#sybase" title="Sybase">Sybase</a>" : <i>[ <a href="sybasedefinition.md">SybaseDefinition</a>, ... ]</i>,
        "<a href="#sybaseiq" title="SybaseIq">SybaseIq</a>" : <i>[ <a href="sybaseiqdefinition.md">SybaseIqDefinition</a>, ... ]</i>,
        "<a href="#teradata" title="Teradata">Teradata</a>" : <i>[ <a href="teradatadefinition.md">TeradataDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SDM::Resource
Properties:
    <a href="#aks" title="Aks">Aks</a>: <i>
      - <a href="aksdefinition.md">AksDefinition</a></i>
    <a href="#aksbasicauth" title="AksBasicAuth">AksBasicAuth</a>: <i>
      - <a href="aksbasicauthdefinition.md">AksBasicAuthDefinition</a></i>
    <a href="#aksserviceaccount" title="AksServiceAccount">AksServiceAccount</a>: <i>
      - <a href="aksserviceaccountdefinition.md">AksServiceAccountDefinition</a></i>
    <a href="#aksserviceaccountuserimpersonation" title="AksServiceAccountUserImpersonation">AksServiceAccountUserImpersonation</a>: <i>
      - <a href="aksserviceaccountuserimpersonationdefinition.md">AksServiceAccountUserImpersonationDefinition</a></i>
    <a href="#aksuserimpersonation" title="AksUserImpersonation">AksUserImpersonation</a>: <i>
      - <a href="aksuserimpersonationdefinition.md">AksUserImpersonationDefinition</a></i>
    <a href="#amazoneks" title="AmazonEks">AmazonEks</a>: <i>
      - <a href="amazoneksdefinition.md">AmazonEksDefinition</a></i>
    <a href="#amazoneksuserimpersonation" title="AmazonEksUserImpersonation">AmazonEksUserImpersonation</a>: <i>
      - <a href="amazoneksuserimpersonationdefinition.md">AmazonEksUserImpersonationDefinition</a></i>
    <a href="#amazones" title="AmazonEs">AmazonEs</a>: <i>
      - <a href="amazonesdefinition.md">AmazonEsDefinition</a></i>
    <a href="#amazonmqamqp091" title="AmazonmqAmqp091">AmazonmqAmqp091</a>: <i>
      - <a href="amazonmqamqp091definition.md">AmazonmqAmqp091Definition</a></i>
    <a href="#athena" title="Athena">Athena</a>: <i>
      - <a href="athenadefinition.md">AthenaDefinition</a></i>
    <a href="#auroramysql" title="AuroraMysql">AuroraMysql</a>: <i>
      - <a href="auroramysqldefinition.md">AuroraMysqlDefinition</a></i>
    <a href="#aurorapostgres" title="AuroraPostgres">AuroraPostgres</a>: <i>
      - <a href="aurorapostgresdefinition.md">AuroraPostgresDefinition</a></i>
    <a href="#aws" title="Aws">Aws</a>: <i>
      - <a href="awsdefinition.md">AwsDefinition</a></i>
    <a href="#bigquery" title="BigQuery">BigQuery</a>: <i>
      - <a href="bigquerydefinition.md">BigQueryDefinition</a></i>
    <a href="#cassandra" title="Cassandra">Cassandra</a>: <i>
      - <a href="cassandradefinition.md">CassandraDefinition</a></i>
    <a href="#citus" title="Citus">Citus</a>: <i>
      - <a href="citusdefinition.md">CitusDefinition</a></i>
    <a href="#clustrix" title="Clustrix">Clustrix</a>: <i>
      - <a href="clustrixdefinition.md">ClustrixDefinition</a></i>
    <a href="#cockroach" title="Cockroach">Cockroach</a>: <i>
      - <a href="cockroachdefinition.md">CockroachDefinition</a></i>
    <a href="#db2i" title="Db2I">Db2I</a>: <i>
      - <a href="db2idefinition.md">Db2IDefinition</a></i>
    <a href="#db2luw" title="Db2Luw">Db2Luw</a>: <i>
      - <a href="db2luwdefinition.md">Db2LuwDefinition</a></i>
    <a href="#druid" title="Druid">Druid</a>: <i>
      - <a href="druiddefinition.md">DruidDefinition</a></i>
    <a href="#dynamodb" title="DynamoDb">DynamoDb</a>: <i>
      - <a href="dynamodbdefinition.md">DynamoDbDefinition</a></i>
    <a href="#elastic" title="Elastic">Elastic</a>: <i>
      - <a href="elasticdefinition.md">ElasticDefinition</a></i>
    <a href="#elasticacheredis" title="ElasticacheRedis">ElasticacheRedis</a>: <i>
      - <a href="elasticacheredisdefinition.md">ElasticacheRedisDefinition</a></i>
    <a href="#googlegke" title="GoogleGke">GoogleGke</a>: <i>
      - <a href="googlegkedefinition.md">GoogleGkeDefinition</a></i>
    <a href="#googlegkeuserimpersonation" title="GoogleGkeUserImpersonation">GoogleGkeUserImpersonation</a>: <i>
      - <a href="googlegkeuserimpersonationdefinition.md">GoogleGkeUserImpersonationDefinition</a></i>
    <a href="#greenplum" title="Greenplum">Greenplum</a>: <i>
      - <a href="greenplumdefinition.md">GreenplumDefinition</a></i>
    <a href="#httpauth" title="HttpAuth">HttpAuth</a>: <i>
      - <a href="httpauthdefinition.md">HttpAuthDefinition</a></i>
    <a href="#httpbasicauth" title="HttpBasicAuth">HttpBasicAuth</a>: <i>
      - <a href="httpbasicauthdefinition.md">HttpBasicAuthDefinition</a></i>
    <a href="#httpnoauth" title="HttpNoAuth">HttpNoAuth</a>: <i>
      - <a href="httpnoauthdefinition.md">HttpNoAuthDefinition</a></i>
    <a href="#kubernetes" title="Kubernetes">Kubernetes</a>: <i>
      - <a href="kubernetesdefinition.md">KubernetesDefinition</a></i>
    <a href="#kubernetesbasicauth" title="KubernetesBasicAuth">KubernetesBasicAuth</a>: <i>
      - <a href="kubernetesbasicauthdefinition.md">KubernetesBasicAuthDefinition</a></i>
    <a href="#kubernetesserviceaccount" title="KubernetesServiceAccount">KubernetesServiceAccount</a>: <i>
      - <a href="kubernetesserviceaccountdefinition.md">KubernetesServiceAccountDefinition</a></i>
    <a href="#kubernetesserviceaccountuserimpersonation" title="KubernetesServiceAccountUserImpersonation">KubernetesServiceAccountUserImpersonation</a>: <i>
      - <a href="kubernetesserviceaccountuserimpersonationdefinition.md">KubernetesServiceAccountUserImpersonationDefinition</a></i>
    <a href="#kubernetesuserimpersonation" title="KubernetesUserImpersonation">KubernetesUserImpersonation</a>: <i>
      - <a href="kubernetesuserimpersonationdefinition.md">KubernetesUserImpersonationDefinition</a></i>
    <a href="#maria" title="Maria">Maria</a>: <i>
      - <a href="mariadefinition.md">MariaDefinition</a></i>
    <a href="#memcached" title="Memcached">Memcached</a>: <i>
      - <a href="memcacheddefinition.md">MemcachedDefinition</a></i>
    <a href="#memsql" title="Memsql">Memsql</a>: <i>
      - <a href="memsqldefinition.md">MemsqlDefinition</a></i>
    <a href="#mongohost" title="MongoHost">MongoHost</a>: <i>
      - <a href="mongohostdefinition.md">MongoHostDefinition</a></i>
    <a href="#mongolegacyhost" title="MongoLegacyHost">MongoLegacyHost</a>: <i>
      - <a href="mongolegacyhostdefinition.md">MongoLegacyHostDefinition</a></i>
    <a href="#mongolegacyreplicaset" title="MongoLegacyReplicaset">MongoLegacyReplicaset</a>: <i>
      - <a href="mongolegacyreplicasetdefinition.md">MongoLegacyReplicasetDefinition</a></i>
    <a href="#mongoreplicaset" title="MongoReplicaSet">MongoReplicaSet</a>: <i>
      - <a href="mongoreplicasetdefinition.md">MongoReplicaSetDefinition</a></i>
    <a href="#mysql" title="Mysql">Mysql</a>: <i>
      - <a href="mysqldefinition.md">MysqlDefinition</a></i>
    <a href="#oracle" title="Oracle">Oracle</a>: <i>
      - <a href="oracledefinition.md">OracleDefinition</a></i>
    <a href="#postgres" title="Postgres">Postgres</a>: <i>
      - <a href="postgresdefinition.md">PostgresDefinition</a></i>
    <a href="#presto" title="Presto">Presto</a>: <i>
      - <a href="prestodefinition.md">PrestoDefinition</a></i>
    <a href="#rabbitmqamqp091" title="RabbitmqAmqp091">RabbitmqAmqp091</a>: <i>
      - <a href="rabbitmqamqp091definition.md">RabbitmqAmqp091Definition</a></i>
    <a href="#rdp" title="Rdp">Rdp</a>: <i>
      - <a href="rdpdefinition.md">RdpDefinition</a></i>
    <a href="#redis" title="Redis">Redis</a>: <i>
      - <a href="redisdefinition.md">RedisDefinition</a></i>
    <a href="#redshift" title="Redshift">Redshift</a>: <i>
      - <a href="redshiftdefinition.md">RedshiftDefinition</a></i>
    <a href="#snowflake" title="Snowflake">Snowflake</a>: <i>
      - <a href="snowflakedefinition.md">SnowflakeDefinition</a></i>
    <a href="#sqlserver" title="SqlServer">SqlServer</a>: <i>
      - <a href="sqlserverdefinition.md">SqlServerDefinition</a></i>
    <a href="#ssh" title="Ssh">Ssh</a>: <i>
      - <a href="sshdefinition.md">SshDefinition</a></i>
    <a href="#sshcert" title="SshCert">SshCert</a>: <i>
      - <a href="sshcertdefinition.md">SshCertDefinition</a></i>
    <a href="#sshcustomerkey" title="SshCustomerKey">SshCustomerKey</a>: <i>
      - <a href="sshcustomerkeydefinition.md">SshCustomerKeyDefinition</a></i>
    <a href="#sybase" title="Sybase">Sybase</a>: <i>
      - <a href="sybasedefinition.md">SybaseDefinition</a></i>
    <a href="#sybaseiq" title="SybaseIq">SybaseIq</a>: <i>
      - <a href="sybaseiqdefinition.md">SybaseIqDefinition</a></i>
    <a href="#teradata" title="Teradata">Teradata</a>: <i>
      - <a href="teradatadefinition.md">TeradataDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Aks

_Required_: No

_Type_: List of <a href="aksdefinition.md">AksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AksBasicAuth

_Required_: No

_Type_: List of <a href="aksbasicauthdefinition.md">AksBasicAuthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AksServiceAccount

_Required_: No

_Type_: List of <a href="aksserviceaccountdefinition.md">AksServiceAccountDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AksServiceAccountUserImpersonation

_Required_: No

_Type_: List of <a href="aksserviceaccountuserimpersonationdefinition.md">AksServiceAccountUserImpersonationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AksUserImpersonation

_Required_: No

_Type_: List of <a href="aksuserimpersonationdefinition.md">AksUserImpersonationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AmazonEks

_Required_: No

_Type_: List of <a href="amazoneksdefinition.md">AmazonEksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AmazonEksUserImpersonation

_Required_: No

_Type_: List of <a href="amazoneksuserimpersonationdefinition.md">AmazonEksUserImpersonationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AmazonEs

_Required_: No

_Type_: List of <a href="amazonesdefinition.md">AmazonEsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AmazonmqAmqp091

_Required_: No

_Type_: List of <a href="amazonmqamqp091definition.md">AmazonmqAmqp091Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Athena

_Required_: No

_Type_: List of <a href="athenadefinition.md">AthenaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuroraMysql

_Required_: No

_Type_: List of <a href="auroramysqldefinition.md">AuroraMysqlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuroraPostgres

_Required_: No

_Type_: List of <a href="aurorapostgresdefinition.md">AuroraPostgresDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Aws

_Required_: No

_Type_: List of <a href="awsdefinition.md">AwsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigQuery

_Required_: No

_Type_: List of <a href="bigquerydefinition.md">BigQueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cassandra

_Required_: No

_Type_: List of <a href="cassandradefinition.md">CassandraDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Citus

_Required_: No

_Type_: List of <a href="citusdefinition.md">CitusDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Clustrix

_Required_: No

_Type_: List of <a href="clustrixdefinition.md">ClustrixDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cockroach

_Required_: No

_Type_: List of <a href="cockroachdefinition.md">CockroachDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Db2I

_Required_: No

_Type_: List of <a href="db2idefinition.md">Db2IDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Db2Luw

_Required_: No

_Type_: List of <a href="db2luwdefinition.md">Db2LuwDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Druid

_Required_: No

_Type_: List of <a href="druiddefinition.md">DruidDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamoDb

_Required_: No

_Type_: List of <a href="dynamodbdefinition.md">DynamoDbDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Elastic

_Required_: No

_Type_: List of <a href="elasticdefinition.md">ElasticDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticacheRedis

_Required_: No

_Type_: List of <a href="elasticacheredisdefinition.md">ElasticacheRedisDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GoogleGke

_Required_: No

_Type_: List of <a href="googlegkedefinition.md">GoogleGkeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GoogleGkeUserImpersonation

_Required_: No

_Type_: List of <a href="googlegkeuserimpersonationdefinition.md">GoogleGkeUserImpersonationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Greenplum

_Required_: No

_Type_: List of <a href="greenplumdefinition.md">GreenplumDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpAuth

_Required_: No

_Type_: List of <a href="httpauthdefinition.md">HttpAuthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpBasicAuth

_Required_: No

_Type_: List of <a href="httpbasicauthdefinition.md">HttpBasicAuthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpNoAuth

_Required_: No

_Type_: List of <a href="httpnoauthdefinition.md">HttpNoAuthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kubernetes

_Required_: No

_Type_: List of <a href="kubernetesdefinition.md">KubernetesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesBasicAuth

_Required_: No

_Type_: List of <a href="kubernetesbasicauthdefinition.md">KubernetesBasicAuthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesServiceAccount

_Required_: No

_Type_: List of <a href="kubernetesserviceaccountdefinition.md">KubernetesServiceAccountDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesServiceAccountUserImpersonation

_Required_: No

_Type_: List of <a href="kubernetesserviceaccountuserimpersonationdefinition.md">KubernetesServiceAccountUserImpersonationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesUserImpersonation

_Required_: No

_Type_: List of <a href="kubernetesuserimpersonationdefinition.md">KubernetesUserImpersonationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Maria

_Required_: No

_Type_: List of <a href="mariadefinition.md">MariaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memcached

_Required_: No

_Type_: List of <a href="memcacheddefinition.md">MemcachedDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memsql

_Required_: No

_Type_: List of <a href="memsqldefinition.md">MemsqlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MongoHost

_Required_: No

_Type_: List of <a href="mongohostdefinition.md">MongoHostDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MongoLegacyHost

_Required_: No

_Type_: List of <a href="mongolegacyhostdefinition.md">MongoLegacyHostDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MongoLegacyReplicaset

_Required_: No

_Type_: List of <a href="mongolegacyreplicasetdefinition.md">MongoLegacyReplicasetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MongoReplicaSet

_Required_: No

_Type_: List of <a href="mongoreplicasetdefinition.md">MongoReplicaSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mysql

_Required_: No

_Type_: List of <a href="mysqldefinition.md">MysqlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Oracle

_Required_: No

_Type_: List of <a href="oracledefinition.md">OracleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Postgres

_Required_: No

_Type_: List of <a href="postgresdefinition.md">PostgresDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Presto

_Required_: No

_Type_: List of <a href="prestodefinition.md">PrestoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RabbitmqAmqp091

_Required_: No

_Type_: List of <a href="rabbitmqamqp091definition.md">RabbitmqAmqp091Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rdp

_Required_: No

_Type_: List of <a href="rdpdefinition.md">RdpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redis

_Required_: No

_Type_: List of <a href="redisdefinition.md">RedisDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redshift

_Required_: No

_Type_: List of <a href="redshiftdefinition.md">RedshiftDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snowflake

_Required_: No

_Type_: List of <a href="snowflakedefinition.md">SnowflakeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlServer

_Required_: No

_Type_: List of <a href="sqlserverdefinition.md">SqlServerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ssh

_Required_: No

_Type_: List of <a href="sshdefinition.md">SshDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshCert

_Required_: No

_Type_: List of <a href="sshcertdefinition.md">SshCertDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshCustomerKey

_Required_: No

_Type_: List of <a href="sshcustomerkeydefinition.md">SshCustomerKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sybase

_Required_: No

_Type_: List of <a href="sybasedefinition.md">SybaseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SybaseIq

_Required_: No

_Type_: List of <a href="sybaseiqdefinition.md">SybaseIqDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Teradata

_Required_: No

_Type_: List of <a href="teradatadefinition.md">TeradataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

