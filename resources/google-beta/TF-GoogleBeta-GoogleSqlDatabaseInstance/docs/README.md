# TF::GoogleBeta::GoogleSqlDatabaseInstance

CloudFormation equivalent of google_sql_database_instance

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleSqlDatabaseInstance",
    "Properties" : {
        "<a href="#databaseversion" title="DatabaseVersion">DatabaseVersion</a>" : <i>String</i>,
        "<a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>" : <i>Boolean</i>,
        "<a href="#encryptionkeyname" title="EncryptionKeyName">EncryptionKeyName</a>" : <i>String</i>,
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
Type: TF::GoogleBeta::GoogleSqlDatabaseInstance
Properties:
    <a href="#databaseversion" title="DatabaseVersion">DatabaseVersion</a>: <i>String</i>
    <a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>: <i>Boolean</i>
    <a href="#encryptionkeyname" title="EncryptionKeyName">EncryptionKeyName</a>: <i>String</i>
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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeletionProtection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionKeyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterInstanceName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootPassword

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

