# TF::Intersight::VirtualizationVirtualMachine DiskDefinition2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
    "<a href="#bus" title="Bus">Bus</a>" : <i>String</i>,
    "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
    "<a href="#order" title="Order">Order</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#virtualdisk" title="VirtualDisk">VirtualDisk</a>" : <i>[ <a href="diskdefinition.md">DiskDefinition</a>, ... ]</i>,
    "<a href="#virtualdiskreference" title="VirtualDiskReference">VirtualDiskReference</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
<a href="#bus" title="Bus">Bus</a>: <i>String</i>
<a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
<a href="#order" title="Order">Order</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#virtualdisk" title="VirtualDisk">VirtualDisk</a>: <i>
      - <a href="diskdefinition.md">DiskDefinition</a></i>
<a href="#virtualdiskreference" title="VirtualDiskReference">VirtualDiskReference</a>: <i>String</i>
</pre>

## Properties

#### AdditionalProperties

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Order

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualDisk

_Required_: No

_Type_: List of <a href="diskdefinition.md">DiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualDiskReference

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

