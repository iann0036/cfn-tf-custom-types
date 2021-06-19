# TF::AzureRM::StorageManagementPolicy ActionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#baseblob" title="BaseBlob">BaseBlob</a>" : <i>[ <a href="baseblobdefinition.md">BaseBlobDefinition</a>, ... ]</i>,
    "<a href="#snapshot" title="Snapshot">Snapshot</a>" : <i>[ <a href="snapshotdefinition.md">SnapshotDefinition</a>, ... ]</i>,
    "<a href="#version" title="Version">Version</a>" : <i>[ <a href="versiondefinition.md">VersionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#baseblob" title="BaseBlob">BaseBlob</a>: <i>
      - <a href="baseblobdefinition.md">BaseBlobDefinition</a></i>
<a href="#snapshot" title="Snapshot">Snapshot</a>: <i>
      - <a href="snapshotdefinition.md">SnapshotDefinition</a></i>
<a href="#version" title="Version">Version</a>: <i>
      - <a href="versiondefinition.md">VersionDefinition</a></i>
</pre>

## Properties

#### BaseBlob

_Required_: No

_Type_: List of <a href="baseblobdefinition.md">BaseBlobDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snapshot

_Required_: No

_Type_: List of <a href="snapshotdefinition.md">SnapshotDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: List of <a href="versiondefinition.md">VersionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

