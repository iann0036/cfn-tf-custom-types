# TF::Gridscale::Snapshot

Provides a storage snapshot resource. This can be used to create, modify, and delete storage snapshots.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gridscale::Snapshot",
    "Properties" : {
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#storageuuid" title="StorageUuid">StorageUuid</a>" : <i>String</i>,
        "<a href="#objectstorageexport" title="ObjectStorageExport">ObjectStorageExport</a>" : <i>[ <a href="objectstorageexportdefinition.md">ObjectStorageExportDefinition</a>, ... ]</i>,
        "<a href="#rollback" title="Rollback">Rollback</a>" : <i>[ <a href="rollbackdefinition.md">RollbackDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gridscale::Snapshot
Properties:
    <a href="#labels" title="Labels">Labels</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#storageuuid" title="StorageUuid">StorageUuid</a>: <i>String</i>
    <a href="#objectstorageexport" title="ObjectStorageExport">ObjectStorageExport</a>: <i>
      - <a href="objectstorageexportdefinition.md">ObjectStorageExportDefinition</a></i>
    <a href="#rollback" title="Rollback">Rollback</a>: <i>
      - <a href="rollbackdefinition.md">RollbackDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Labels

The list of labels.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the snapshot.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageUuid

UUID of the storage used to create this snapshot.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectStorageExport

_Required_: No

_Type_: List of <a href="objectstorageexportdefinition.md">ObjectStorageExportDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rollback

_Required_: No

_Type_: List of <a href="rollbackdefinition.md">RollbackDefinition</a>

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

#### Capacity

Returns the <code>Capacity</code> value.

#### ChangeTime

Returns the <code>ChangeTime</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### CurrentPrice

Returns the <code>CurrentPrice</code> value.

#### Id

ID of the rollback request. It can be any string value. Each rollback request has to have a UNIQUE id.

#### LicenseProductNo

Returns the <code>LicenseProductNo</code> value.

#### LocationCountry

Returns the <code>LocationCountry</code> value.

#### LocationIata

Returns the <code>LocationIata</code> value.

#### LocationName

Returns the <code>LocationName</code> value.

#### LocationUuid

Returns the <code>LocationUuid</code> value.

#### Status

Returns the <code>Status</code> value.

#### UsageInMinutes

Returns the <code>UsageInMinutes</code> value.

