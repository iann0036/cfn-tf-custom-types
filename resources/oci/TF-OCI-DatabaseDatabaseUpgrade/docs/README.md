# TF::OCI::DatabaseDatabaseUpgrade

This resource provides the Database Upgrade resource in Oracle Cloud Infrastructure Database service.

Upgrades the specified Oracle Database instance.

Database upgrade requires source to be `DB_VERSION` or `DB_SOFTWARE_IMAGE`.
	`db_home.0.db_version` is updated to target DB version specified in the upgrade request. 
	To avoid a force new create of the db_home on the next apply, add the following to the resource
	```
	lifecycle {
	   	ignore_changes = [
	   		db_home.0.db_version,
	   	]
	}
	```

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::DatabaseDatabaseUpgrade",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#databaseid" title="DatabaseId">DatabaseId</a>" : <i>String</i>,
        "<a href="#databaseupgradesourcedetails" title="DatabaseUpgradeSourceDetails">DatabaseUpgradeSourceDetails</a>" : <i>[ <a href="databaseupgradesourcedetailsdefinition.md">DatabaseUpgradeSourceDetailsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::DatabaseDatabaseUpgrade
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#databaseid" title="DatabaseId">DatabaseId</a>: <i>String</i>
    <a href="#databaseupgradesourcedetails" title="DatabaseUpgradeSourceDetails">DatabaseUpgradeSourceDetails</a>: <i>
      - <a href="databaseupgradesourcedetailsdefinition.md">DatabaseUpgradeSourceDetailsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Action

The database upgrade action.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseId

The database [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseUpgradeSourceDetails

_Required_: No

_Type_: List of <a href="databaseupgradesourcedetailsdefinition.md">DatabaseUpgradeSourceDetailsDefinition</a>

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

#### CharacterSet

Returns the <code>CharacterSet</code> value.

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### ConnectionStrings

Returns the <code>ConnectionStrings</code> value.

#### DatabaseSoftwareImageId

The database software image [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the image to be used to upgrade a database.
* `db_home_id` - (Required when source=DB_HOME) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Database Home.
* `db_version` - (Required when source=DB_VERSION) A valid Oracle Database version. To get a list of supported versions, use the [ListDbVersions](https://docs.cloud.oracle.com/iaas/api/#/en/database/latest/DbVersionSummary/ListDbVersions) operation.
* `options` - (Optional) Additional upgrade options supported by DBUA(Database Upgrade Assistant). Example: "-upgradeTimezone false -keepEvents"
* `source` - (Optional) The source of the Oracle Database software to be used for the upgrade.
* Use `DB_VERSION` to specify a generally-available Oracle Database software version to upgrade the database.
* Use `DB_SOFTWARE_IMAGE` to specify a [database software image](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/databasesoftwareimage.htm) to upgrade the database.

#### DbBackupConfig

Returns the <code>DbBackupConfig</code> value.

#### DbHomeId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Database Home.
* `db_version` - (Required when source=DB_VERSION) A valid Oracle Database version. To get a list of supported versions, use the [ListDbVersions](https://docs.cloud.oracle.com/iaas/api/#/en/database/latest/DbVersionSummary/ListDbVersions) operation.
* `options` - (Optional) Additional upgrade options supported by DBUA(Database Upgrade Assistant). Example: "-upgradeTimezone false -keepEvents"
* `source` - (Optional) The source of the Oracle Database software to be used for the upgrade.
* Use `DB_VERSION` to specify a generally-available Oracle Database software version to upgrade the database.
* Use `DB_SOFTWARE_IMAGE` to specify a [database software image](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/databasesoftwareimage.htm) to upgrade the database.

#### DbName

Returns the <code>DbName</code> value.

#### DbSystemId

Returns the <code>DbSystemId</code> value.

#### DbUniqueName

Returns the <code>DbUniqueName</code> value.

#### DbWorkload

Returns the <code>DbWorkload</code> value.

#### DefinedTags

Returns the <code>DefinedTags</code> value.

#### FreeformTags

Returns the <code>FreeformTags</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastBackupTimestamp

Returns the <code>LastBackupTimestamp</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### NcharacterSet

Returns the <code>NcharacterSet</code> value.

#### PdbName

Returns the <code>PdbName</code> value.

#### SourceDatabasePointInTimeRecoveryTimestamp

Returns the <code>SourceDatabasePointInTimeRecoveryTimestamp</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### VmClusterId

Returns the <code>VmClusterId</code> value.

