# TF::Google::SqlDatabaseInstance

Creates a new Google SQL Database Instance. For more information, see the [official documentation](https://cloud.google.com/sql/),
or the [JSON API](https://cloud.google.com/sql/docs/admin-api/v1beta4/instances).

~> **NOTE on `google_sql_database_instance`:** - First-generation instances have been
deprecated and should no longer be created, see [upgrade docs](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
for more details.
To upgrade your First-generation instance, update your Terraform config that the instance has
* `settings.ip_configuration.ipv4_enabled=true`
* `settings.backup_configuration.enabled=true`
* `settings.backup_configuration.binary_log_enabled=true`.  
Apply the terraform config, then upgrade the instance in the console as described in the documentation.
Once upgraded, update the following attributes in your Terraform config to the correct value according to
the above documentation:
* `region`
* `database_version` (if applicable)
* `tier`  
Remove any fields that are not applica...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::SqlDatabaseInstance",
    "Properties" : {
        "<a href="#databaseversion" title="DatabaseVersion">DatabaseVersion</a>" : <i>String</i>,
        "<a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>" : <i>Boolean</i>,
        "<a href="#masterinstancename" title="MasterInstanceName">MasterInstanceName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#rootpassword" title="RootPassword">RootPassword</a>" : <i>String</i>,
        "<a href="#clone" title="Clone">Clone</a>" : <i>[ <a href="clonedefinition.md">CloneDefinition</a>, ... ]</i>,
        "<a href="#replicaconfiguration" title="ReplicaConfiguration">ReplicaConfiguration</a>" : <i>[ <a href="replicaconfigurationdefinition.md">ReplicaConfigurationDefinition</a>, ... ]</i>,
        "<a href="#restorebackupcontext" title="RestoreBackupContext">RestoreBackupContext</a>" : <i>[ <a href="restorebackupcontextdefinition.md">RestoreBackupContextDefinition</a>, ... ]</i>,
        "<a href="#settings" title="Settings">Settings</a>" : <i>[ <a href="settingsdefinition.md">SettingsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::SqlDatabaseInstance
Properties:
    <a href="#databaseversion" title="DatabaseVersion">DatabaseVersion</a>: <i>String</i>
    <a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>: <i>Boolean</i>
    <a href="#masterinstancename" title="MasterInstanceName">MasterInstanceName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#rootpassword" title="RootPassword">RootPassword</a>: <i>String</i>
    <a href="#clone" title="Clone">Clone</a>: <i>
      - <a href="clonedefinition.md">CloneDefinition</a></i>
    <a href="#replicaconfiguration" title="ReplicaConfiguration">ReplicaConfiguration</a>: <i>
      - <a href="replicaconfigurationdefinition.md">ReplicaConfigurationDefinition</a></i>
    <a href="#restorebackupcontext" title="RestoreBackupContext">RestoreBackupContext</a>: <i>
      - <a href="restorebackupcontextdefinition.md">RestoreBackupContextDefinition</a></i>
    <a href="#settings" title="Settings">Settings</a>: <i>
      - <a href="settingsdefinition.md">SettingsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DatabaseVersion

The MySQL, PostgreSQL or
SQL Server (beta) version to use. Supported values include `MYSQL_5_6`,
`MYSQL_5_7`, `MYSQL_8_0`, `POSTGRES_9_6`,`POSTGRES_10`, `POSTGRES_11`,
`POSTGRES_12`, `POSTGRES_13`, `SQLSERVER_2017_STANDARD`,
`SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`.
[Database Version Policies](https://cloud.google.com/sql/docs/db-versions)
includes an up-to-date reference of supported versions.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeletionProtection

Whether or not to allow Terraform to destroy the instance. Unless this field is set to false
in Terraform state, a `terraform destroy` or `terraform apply` command that deletes the instance will fail.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterInstanceName

The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
`binary_log_enabled` set, as well as existing backups.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the instance. If the name is left
blank, Terraform will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to [one week](https://cloud.google.com/sql/docs/delete-instance).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region the instance will sit in. Note, Cloud SQL is not
available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for instances if the provider
region is not supported with Cloud SQL. If you choose not to provide the `region` argument for this resource,
make sure you understand this.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootPassword

Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Clone

_Required_: No

_Type_: List of <a href="clonedefinition.md">CloneDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicaConfiguration

_Required_: No

_Type_: List of <a href="replicaconfigurationdefinition.md">ReplicaConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestoreBackupContext

_Required_: No

_Type_: List of <a href="restorebackupcontextdefinition.md">RestoreBackupContextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Settings

_Required_: No

_Type_: List of <a href="settingsdefinition.md">SettingsDefinition</a>

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

#### ConnectionName

Returns the <code>ConnectionName</code> value.

#### FirstIpAddress

Returns the <code>FirstIpAddress</code> value.

#### Id

Returns the <code>Id</code> value.

#### IpAddress

Returns the <code>IpAddress</code> value.

#### PrivateIpAddress

Returns the <code>PrivateIpAddress</code> value.

#### PublicIpAddress

Returns the <code>PublicIpAddress</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

#### ServerCaCert

Returns the <code>ServerCaCert</code> value.

#### ServiceAccountEmailAddress

Returns the <code>ServiceAccountEmailAddress</code> value.

