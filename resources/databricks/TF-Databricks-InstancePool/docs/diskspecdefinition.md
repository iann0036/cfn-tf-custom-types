# TF::Databricks::InstancePool DiskSpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#diskcount" title="DiskCount">DiskCount</a>" : <i>Double</i>,
    "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>Double</i>,
    "<a href="#disktype" title="DiskType">DiskType</a>" : <i>[ <a href="disktypedefinition.md">DiskTypeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#diskcount" title="DiskCount">DiskCount</a>: <i>Double</i>
<a href="#disksize" title="DiskSize">DiskSize</a>: <i>Double</i>
<a href="#disktype" title="DiskType">DiskType</a>: <i>
      - <a href="disktypedefinition.md">DiskTypeDefinition</a></i>
</pre>

## Properties

#### DiskCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskType

_Required_: No

_Type_: List of <a href="disktypedefinition.md">DiskTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

