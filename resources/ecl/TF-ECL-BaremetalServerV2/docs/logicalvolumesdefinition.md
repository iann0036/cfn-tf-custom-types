# TF::ECL::BaremetalServerV2 LogicalVolumesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#lvlabel" title="LvLabel">LvLabel</a>" : <i>String</i>,
    "<a href="#size" title="Size">Size</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#lvlabel" title="LvLabel">LvLabel</a>: <i>String</i>
<a href="#size" title="Size">Size</a>: <i>String</i>
</pre>

## Properties

#### LvLabel

Logical volume label. Changing this creates a
new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

Logical volume size. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

