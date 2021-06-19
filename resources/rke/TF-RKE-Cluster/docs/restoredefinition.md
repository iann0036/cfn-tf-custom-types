# TF::RKE::Cluster RestoreDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#restore" title="Restore">Restore</a>" : <i>[ <a href="restoredefinition.md">RestoreDefinition</a>, ... ]</i>,
    "<a href="#snapshotname" title="SnapshotName">SnapshotName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#restore" title="Restore">Restore</a>: <i>
      - <a href="restoredefinition.md">RestoreDefinition</a></i>
<a href="#snapshotname" title="SnapshotName">SnapshotName</a>: <i>String</i>
</pre>

## Properties

#### Restore

_Required_: No

_Type_: List of <a href="restoredefinition.md">RestoreDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

