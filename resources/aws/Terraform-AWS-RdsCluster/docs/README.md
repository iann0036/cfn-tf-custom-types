# Terraform::AWS::RdsCluster

Manages a [RDS Aurora Cluster][2]. To manage cluster instances that inherit configuration from the cluster (when not running the cluster in `serverless` engine mode), see the [`aws_rds_cluster_instance` resource](/docs/providers/aws/r/rds_cluster_instance.html). To manage non-Aurora databases (e.g. MySQL, PostgreSQL, SQL Server, etc.), see the [`aws_db_instance` resource](/docs/providers/aws/r/db_instance.html).

For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.

Changes to a RDS Cluster can occur when you manually change a
parameter, such as `port`, and are reflected in the next maintenance
window. Because of this, Terraform may report a difference in its planning
phase because a modification has not yet taken place. You can use the
`apply_immediately` flag to instruct the service to apply the change immediately
(see documentation below).

~> **Note:** using `apply_immediately` can result in a
brief downtime as the server reboots. See the AWS Docs on [RDS Maintenance][4]
for more information.

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::RdsCluster",
    "Properties" : {
        "<a href="#applyimmediately" title="ApplyImmediately">ApplyImmediately</a>" : <i>Boolean</i>,
        "<a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#backtrackwindow" title="BacktrackWindow">BacktrackWindow</a>" : <i>Double</i>,
        "<a href="#backupretentionperiod" title="BackupRetentionPeriod">BackupRetentionPeriod</a>" : <i>Double</i>,
        "<a href="#clusteridentifier" title="ClusterIdentifier">ClusterIdentifier</a>" : <i>String</i>,
        "<a href="#clusteridentifierprefix" title="ClusterIdentifierPrefix">ClusterIdentifierPrefix</a>" : <i>String</i>,
        "<a href="#clustermembers" title="ClusterMembers">ClusterMembers</a>" : <i>[ String, ... ]</i>,
        "<a href="#copytagstosnapshot" title="CopyTagsToSnapshot">CopyTagsToSnapshot</a>" : <i>Boolean</i>,
        "<a href="#databasename" title="DatabaseName">DatabaseName</a>" : <i>String</i>,
        "<a href="#dbclusterparametergroupname" title="DbClusterParameterGroupName">DbClusterParameterGroupName</a>" : <i>String</i>,
        "<a href="#dbsubnetgroupname" title="DbSubnetGroupName">DbSubnetGroupName</a>" : <i>String</i>,
        "<a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>" : <i>Boolean</i>,
        "<a href="#enablehttpendpoint" title="EnableHttpEndpoint">EnableHttpEndpoint</a>" : <i>Boolean</i>,
        "<a href="#enabledcloudwatchlogsexports" title="EnabledCloudwatchLogsExports">EnabledCloudwatchLogsExports</a>" : <i>[ String, ... ]</i>,
        "<a href="#engine" title="Engine">Engine</a>" : <i>String</i>,
        "<a href="#enginemode" title="EngineMode">EngineMode</a>" : <i>String</i>,
        "<a href="#engineversion" title="EngineVersion">EngineVersion</a>" : <i>String</i>,
        "<a href="#finalsnapshotidentifier" title="FinalSnapshotIdentifier">FinalSnapshotIdentifier</a>" : <i>String</i>,
        "<a href="#globalclusteridentifier" title="GlobalClusterIdentifier">GlobalClusterIdentifier</a>" : <i>String</i>,
        "<a href="#iamdatabaseauthenticationenabled" title="IamDatabaseAuthenticationEnabled">IamDatabaseAuthenticationEnabled</a>" : <i>Boolean</i>,
        "<a href="#iamroles" title="IamRoles">IamRoles</a>" : <i>[ String, ... ]</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#masterpassword" title="MasterPassword">MasterPassword</a>" : <i>String</i>,
        "<a href="#masterusername" title="MasterUsername">MasterUsername</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#preferredbackupwindow" title="PreferredBackupWindow">PreferredBackupWindow</a>" : <i>String</i>,
        "<a href="#preferredmaintenancewindow" title="PreferredMaintenanceWindow">PreferredMaintenanceWindow</a>" : <i>String</i>,
        "<a href="#replicationsourceidentifier" title="ReplicationSourceIdentifier">ReplicationSourceIdentifier</a>" : <i>String</i>,
        "<a href="#skipfinalsnapshot" title="SkipFinalSnapshot">SkipFinalSnapshot</a>" : <i>Boolean</i>,
        "<a href="#snapshotidentifier" title="SnapshotIdentifier">SnapshotIdentifier</a>" : <i>String</i>,
        "<a href="#sourceregion" title="SourceRegion">SourceRegion</a>" : <i>String</i>,
        "<a href="#storageencrypted" title="StorageEncrypted">StorageEncrypted</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#vpcsecuritygroupids" title="VpcSecurityGroupIds">VpcSecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#s3import" title="S3Import">S3Import</a>" : <i>[ <a href="s3import.md">S3Import</a>, ... ]</i>,
        "<a href="#scalingconfiguration" title="ScalingConfiguration">ScalingConfiguration</a>" : <i>[ <a href="scalingconfiguration.md">ScalingConfiguration</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::RdsCluster
Properties:
    <a href="#applyimmediately" title="ApplyImmediately">ApplyImmediately</a>: <i>Boolean</i>
    <a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>: <i>
      - String</i>
    <a href="#backtrackwindow" title="BacktrackWindow">BacktrackWindow</a>: <i>Double</i>
    <a href="#backupretentionperiod" title="BackupRetentionPeriod">BackupRetentionPeriod</a>: <i>Double</i>
    <a href="#clusteridentifier" title="ClusterIdentifier">ClusterIdentifier</a>: <i>String</i>
    <a href="#clusteridentifierprefix" title="ClusterIdentifierPrefix">ClusterIdentifierPrefix</a>: <i>String</i>
    <a href="#clustermembers" title="ClusterMembers">ClusterMembers</a>: <i>
      - String</i>
    <a href="#copytagstosnapshot" title="CopyTagsToSnapshot">CopyTagsToSnapshot</a>: <i>Boolean</i>
    <a href="#databasename" title="DatabaseName">DatabaseName</a>: <i>String</i>
    <a href="#dbclusterparametergroupname" title="DbClusterParameterGroupName">DbClusterParameterGroupName</a>: <i>String</i>
    <a href="#dbsubnetgroupname" title="DbSubnetGroupName">DbSubnetGroupName</a>: <i>String</i>
    <a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>: <i>Boolean</i>
    <a href="#enablehttpendpoint" title="EnableHttpEndpoint">EnableHttpEndpoint</a>: <i>Boolean</i>
    <a href="#enabledcloudwatchlogsexports" title="EnabledCloudwatchLogsExports">EnabledCloudwatchLogsExports</a>: <i>
      - String</i>
    <a href="#engine" title="Engine">Engine</a>: <i>String</i>
    <a href="#enginemode" title="EngineMode">EngineMode</a>: <i>String</i>
    <a href="#engineversion" title="EngineVersion">EngineVersion</a>: <i>String</i>
    <a href="#finalsnapshotidentifier" title="FinalSnapshotIdentifier">FinalSnapshotIdentifier</a>: <i>String</i>
    <a href="#globalclusteridentifier" title="GlobalClusterIdentifier">GlobalClusterIdentifier</a>: <i>String</i>
    <a href="#iamdatabaseauthenticationenabled" title="IamDatabaseAuthenticationEnabled">IamDatabaseAuthenticationEnabled</a>: <i>Boolean</i>
    <a href="#iamroles" title="IamRoles">IamRoles</a>: <i>
      - String</i>
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#masterpassword" title="MasterPassword">MasterPassword</a>: <i>String</i>
    <a href="#masterusername" title="MasterUsername">MasterUsername</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#preferredbackupwindow" title="PreferredBackupWindow">PreferredBackupWindow</a>: <i>String</i>
    <a href="#preferredmaintenancewindow" title="PreferredMaintenanceWindow">PreferredMaintenanceWindow</a>: <i>String</i>
    <a href="#replicationsourceidentifier" title="ReplicationSourceIdentifier">ReplicationSourceIdentifier</a>: <i>String</i>
    <a href="#skipfinalsnapshot" title="SkipFinalSnapshot">SkipFinalSnapshot</a>: <i>Boolean</i>
    <a href="#snapshotidentifier" title="SnapshotIdentifier">SnapshotIdentifier</a>: <i>String</i>
    <a href="#sourceregion" title="SourceRegion">SourceRegion</a>: <i>String</i>
    <a href="#storageencrypted" title="StorageEncrypted">StorageEncrypted</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#vpcsecuritygroupids" title="VpcSecurityGroupIds">VpcSecurityGroupIds</a>: <i>
      - String</i>
    <a href="#s3import" title="S3Import">S3Import</a>: <i>
      - <a href="s3import.md">S3Import</a></i>
    <a href="#scalingconfiguration" title="ScalingConfiguration">ScalingConfiguration</a>: <i>
      - <a href="scalingconfiguration.md">ScalingConfiguration</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### ApplyImmediately

Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZones

A list of EC2 Availability Zones for the DB cluster storage where DB cluster instances can be created. RDS automatically assigns 3 AZs if less than 3 AZs are configured, which will show as a difference requiring resource recreation next Terraform apply. It is recommended to specify 3 AZs or use [the `lifecycle` configuration block `ignore_changes` argument](/docs/configuration/resources.html#ignore_changes) if necessary.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BacktrackWindow

The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupRetentionPeriod

The days to retain backups for. Default `1`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterIdentifier

The cluster identifier. If omitted, Terraform will assign a random, unique identifier.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterIdentifierPrefix

Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifier`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterMembers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CopyTagsToSnapshot

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseName

Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbClusterParameterGroupName

A cluster parameter group to associate with the cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbSubnetGroupName

A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws_rds_cluster_instance`](/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeletionProtection

If the DB instance should have deletion protection enabled. The database can't be deleted when this value is set to `true`. The default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHttpEndpoint

Enable HTTP endpoint (data API). Only valid when `engine_mode` is set to `serverless`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnabledCloudwatchLogsExports

List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`, `postgresql` (PostgreSQL).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Engine

The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineMode

The database engine mode. Valid values: `global`, `multimaster`, `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineVersion

The database engine version. Updating this argument results in an outage. See the [Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html) and [Aurora Postgres](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.html) documentation for your configured engine to determine this value. For example with Aurora MySQL 2, a potential value for this argument is `5.7.mysql_aurora.2.03.2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FinalSnapshotIdentifier

The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalClusterIdentifier

The global cluster identifier specified on [`aws_rds_global_cluster`](/docs/providers/aws/r/rds_global_cluster.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamDatabaseAuthenticationEnabled

Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) for availability and limitations.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamRoles

A List of ARNs for the IAM roles to associate to the RDS Cluster.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterPassword

Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterUsername

Username for the master DB user. Please refer to the [RDS Naming Constraints][5]. This argument does not support in-place updates and cannot be changed during a restore from snapshot.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port on which the DB accepts connections.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredBackupWindow

The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredMaintenanceWindow

The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationSourceIdentifier

ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipFinalSnapshot

Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotIdentifier

Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceRegion

The source region for an encrypted replica DB cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageEncrypted

Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `engine_mode` and `true` for `serverless` `engine_mode`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the DB cluster.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcSecurityGroupIds

List of VPC security groups to associate
with the Cluster.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Import

_Required_: No

_Type_: List of <a href="s3import.md">S3Import</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingConfiguration

_Required_: No

_Type_: List of <a href="scalingconfiguration.md">ScalingConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### ClusterResourceId

Returns the <code>ClusterResourceId</code> value.

#### Endpoint

Returns the <code>Endpoint</code> value.

#### HostedZoneId

Returns the <code>HostedZoneId</code> value.

#### Id

Returns the <code>Id</code> value.

#### ReaderEndpoint

Returns the <code>ReaderEndpoint</code> value.

