# TF::ECL::BaremetalServerV2 PartitionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#lvm" title="Lvm">Lvm</a>" : <i>Boolean</i>,
    "<a href="#partitionlabel" title="PartitionLabel">PartitionLabel</a>" : <i>String</i>,
    "<a href="#size" title="Size">Size</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#lvm" title="Lvm">Lvm</a>: <i>Boolean</i>
<a href="#partitionlabel" title="PartitionLabel">PartitionLabel</a>: <i>String</i>
<a href="#size" title="Size">Size</a>: <i>String</i>
</pre>

## Properties

#### Lvm

LVM flag. Changing this creates a new server.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartitionLabel

Partition label. Changing this creates a
new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

Partition size. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

