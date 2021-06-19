# TF::OCI::MysqlMysqlBackup

This resource provides the Mysql Backup resource in Oracle Cloud Infrastructure MySQL Database service.

Create a backup of a DB System.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::MysqlMysqlBackup",
    "Properties" : {
        "<a href="#backuptype" title="BackupType">BackupType</a>" : <i>String</i>,
        "<a href="#dbsystemid" title="DbSystemId">DbSystemId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="dbsystemsnapshotdefinition.md">DbSystemSnapshotDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="dbsystemsnapshotdefinition2.md">DbSystemSnapshotDefinition2</a>, ... ]</i>,
        "<a href="#retentionindays" title="RetentionInDays">RetentionInDays</a>" : <i>Double</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::MysqlMysqlBackup
Properties:
    <a href="#backuptype" title="BackupType">BackupType</a>: <i>String</i>
    <a href="#dbsystemid" title="DbSystemId">DbSystemId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="dbsystemsnapshotdefinition.md">DbSystemSnapshotDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="dbsystemsnapshotdefinition2.md">DbSystemSnapshotDefinition2</a></i>
    <a href="#retentionindays" title="RetentionInDays">RetentionInDays</a>: <i>Double</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### BackupType

The type of backup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbSystemId

The OCID of the DB System the Backup is associated with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No

_Type_: List of <a href="dbsystemsnapshotdefinition.md">DbSystemSnapshotDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

(Updatable) A user-supplied description for the backup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-supplied display name for the backup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No

_Type_: List of <a href="dbsystemsnapshotdefinition2.md">DbSystemSnapshotDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionInDays

(Updatable) Number of days to retain this backup.

_Required_: No

_Type_: Double

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

#### BackupSizeInGbs

Returns the <code>BackupSizeInGbs</code> value.

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### CreationType

Returns the <code>CreationType</code> value.

#### DataStorageSizeInGb

Returns the <code>DataStorageSizeInGb</code> value.

#### DbSystemSnapshot

Returns the <code>DbSystemSnapshot</code> value.

#### Id

Returns the <code>Id</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### MysqlVersion

Returns the <code>MysqlVersion</code> value.

#### ShapeName

Returns the <code>ShapeName</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeUpdated

Returns the <code>TimeUpdated</code> value.

