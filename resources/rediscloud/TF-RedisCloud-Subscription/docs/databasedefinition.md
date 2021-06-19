# TF::RedisCloud::Subscription DatabaseDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#averageitemsizeinbytes" title="AverageItemSizeInBytes">AverageItemSizeInBytes</a>" : <i>Double</i>,
    "<a href="#clientsslcertificate" title="ClientSslCertificate">ClientSslCertificate</a>" : <i>String</i>,
    "<a href="#datapersistence" title="DataPersistence">DataPersistence</a>" : <i>String</i>,
    "<a href="#externalendpointforossclusterapi" title="ExternalEndpointForOssClusterApi">ExternalEndpointForOssClusterApi</a>" : <i>Boolean</i>,
    "<a href="#hashingpolicy" title="HashingPolicy">HashingPolicy</a>" : <i>[ String, ... ]</i>,
    "<a href="#memorylimitingb" title="MemoryLimitInGb">MemoryLimitInGb</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#periodicbackuppath" title="PeriodicBackupPath">PeriodicBackupPath</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#replicaof" title="ReplicaOf">ReplicaOf</a>" : <i>[ String, ... ]</i>,
    "<a href="#replication" title="Replication">Replication</a>" : <i>Boolean</i>,
    "<a href="#sourceips" title="SourceIps">SourceIps</a>" : <i>[ String, ... ]</i>,
    "<a href="#supportossclusterapi" title="SupportOssClusterApi">SupportOssClusterApi</a>" : <i>Boolean</i>,
    "<a href="#throughputmeasurementby" title="ThroughputMeasurementBy">ThroughputMeasurementBy</a>" : <i>String</i>,
    "<a href="#throughputmeasurementvalue" title="ThroughputMeasurementValue">ThroughputMeasurementValue</a>" : <i>Double</i>,
    "<a href="#alert" title="Alert">Alert</a>" : <i>[ <a href="alertdefinition.md">AlertDefinition</a>, ... ]</i>,
    "<a href="#module" title="Module">Module</a>" : <i>[ <a href="moduledefinition.md">ModuleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#averageitemsizeinbytes" title="AverageItemSizeInBytes">AverageItemSizeInBytes</a>: <i>Double</i>
<a href="#clientsslcertificate" title="ClientSslCertificate">ClientSslCertificate</a>: <i>String</i>
<a href="#datapersistence" title="DataPersistence">DataPersistence</a>: <i>String</i>
<a href="#externalendpointforossclusterapi" title="ExternalEndpointForOssClusterApi">ExternalEndpointForOssClusterApi</a>: <i>Boolean</i>
<a href="#hashingpolicy" title="HashingPolicy">HashingPolicy</a>: <i>
      - String</i>
<a href="#memorylimitingb" title="MemoryLimitInGb">MemoryLimitInGb</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#periodicbackuppath" title="PeriodicBackupPath">PeriodicBackupPath</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#replicaof" title="ReplicaOf">ReplicaOf</a>: <i>
      - String</i>
<a href="#replication" title="Replication">Replication</a>: <i>Boolean</i>
<a href="#sourceips" title="SourceIps">SourceIps</a>: <i>
      - String</i>
<a href="#supportossclusterapi" title="SupportOssClusterApi">SupportOssClusterApi</a>: <i>Boolean</i>
<a href="#throughputmeasurementby" title="ThroughputMeasurementBy">ThroughputMeasurementBy</a>: <i>String</i>
<a href="#throughputmeasurementvalue" title="ThroughputMeasurementValue">ThroughputMeasurementValue</a>: <i>Double</i>
<a href="#alert" title="Alert">Alert</a>: <i>
      - <a href="alertdefinition.md">AlertDefinition</a></i>
<a href="#module" title="Module">Module</a>: <i>
      - <a href="moduledefinition.md">ModuleDefinition</a></i>
</pre>

## Properties

#### AverageItemSizeInBytes

Relevant only to ram-and-flash clusters. Estimated average size (measured in bytes)
of the items stored in the database. Default: 1000.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSslCertificate

SSL certificate to authenticate user connections.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataPersistence

Rate of database data persistence (in persistent storage). Default: ‘none’.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalEndpointForOssClusterApi

Should use the external endpoint for open-source (OSS) Cluster API.
Can only be enabled if OSS Cluster API support is enabled. Default: 'false'.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HashingPolicy

List of regular expression rules to shard the database by. See
[the documentation on clustering](https://docs.redislabs.com/latest/rc/concepts/clustering/) for more information on the
hashing policy. This cannot be set when `support_oss_cluster_api` is set to true.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryLimitInGb

Maximum memory usage for this specific database.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A meaningful name to identify the database. Caution should be taken when changing this value - see
the top of the page for more information.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password used to access the database.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeriodicBackupPath

Path that will be used to store database backup files.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The protocol that will be used to access the database, (either ‘redis’ or 'memcached’) Default: ‘redis’.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicaOf

Set of Redis database URIs, in the format `redis://user:password@host:port`, that this
database will be a replica of. If the URI provided is Redis Labs Cloud instance, only host and port should be provided.
Cannot be enabled when `support_oss_cluster_api` is enabled.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replication

Databases replication. Default: ‘true’.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIps

Set of CIDR addresses to allow access to the database. Defaults to allowing traffic.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportOssClusterApi

Support Redis open-source (OSS) Cluster API. Default: ‘false’.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThroughputMeasurementBy

Throughput measurement method, (either ‘number-of-shards’ or ‘operations-per-second’).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThroughputMeasurementValue

Throughput value (as applies to selected measurement method).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Alert

_Required_: No

_Type_: List of <a href="alertdefinition.md">AlertDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Module

_Required_: No

_Type_: List of <a href="moduledefinition.md">ModuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

