# Terraform::AzureStack::VirtualMachineScaleSet Sku

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#capacity" title="Capacity">Capacity</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#tier" title="Tier">Tier</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#capacity" title="Capacity">Capacity</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#tier" title="Tier">Tier</a>: <i>String</i>
</pre>

## Properties

#### Capacity

Specifies the number of virtual machines in the scale set.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the size of virtual machines in a scale set.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier

Specifies the tier of virtual machines in a scale set. Possible values, `standard` or `basic`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

