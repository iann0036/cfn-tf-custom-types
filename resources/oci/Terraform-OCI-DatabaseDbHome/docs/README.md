# Terraform::OCI::DatabaseDbHome

This resource provides the Db Home resource in Oracle Cloud Infrastructure Database service.

Creates a new Database Home in the specified DB system based on the request parameters you provide. Applies only to bare metal and Exadata DB systems.

The creation of an oci_database_db_system requires that it be created with exactly one oci_database_db_home. Therefore the first db home will have to be a property of the db system resource and any further db homes to be added to the db system will have to be added as first class resources using "oci_database_db_home".

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::DatabaseDbHome",
    "Properties" : {
        "<a href="#dbsystemid" title="DbSystemId">DbSystemId</a>" : <i>String</i>,
        "<a href="#dbversion" title="DbVersion">DbVersion</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#vmclusterid" title="VmClusterId">VmClusterId</a>" : <i>String</i>,
        "<a href="#database" title="Database">Database</a>" : <i>[ <a href="database.md">Database</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#dbbackupconfig" title="DbBackupConfig">DbBackupConfig</a>" : <i>[ <a href="dbbackupconfig.md">DbBackupConfig</a>, ... ]</i>,
        "<a href="#backupdestinationdetails" title="BackupDestinationDetails">BackupDestinationDetails</a>" : <i>[ <a href="backupdestinationdetails.md">BackupDestinationDetails</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::DatabaseDbHome
Properties:
    <a href="#dbsystemid" title="DbSystemId">DbSystemId</a>: <i>String</i>
    <a href="#dbversion" title="DbVersion">DbVersion</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#vmclusterid" title="VmClusterId">VmClusterId</a>: <i>String</i>
    <a href="#database" title="Database">Database</a>: <i>
      - <a href="database.md">Database</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#dbbackupconfig" title="DbBackupConfig">DbBackupConfig</a>: <i>
      - <a href="dbbackupconfig.md">DbBackupConfig</a></i>
    <a href="#backupdestinationdetails" title="BackupDestinationDetails">BackupDestinationDetails</a>: <i>
      - <a href="backupdestinationdetails.md">BackupDestinationDetails</a></i>
</pre>

## Properties

#### DbSystemId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Database

_Required_: No

_Type_: List of <a href="database.md">Database</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbBackupConfig

_Required_: No

_Type_: List of <a href="dbbackupconfig.md">DbBackupConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupDestinationDetails

_Required_: No

_Type_: List of <a href="backupdestinationdetails.md">BackupDestinationDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### DbHomeLocation

Returns the <code>DbHomeLocation</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastPatchHistoryEntryId

Returns the <code>LastPatchHistoryEntryId</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

