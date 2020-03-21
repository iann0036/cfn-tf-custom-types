# Terraform::AzureRM::ContainerGroup Gpu

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#count" title="Count">Count</a>" : <i>Double</i>,
    "<a href="#sku" title="Sku">Sku</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#count" title="Count">Count</a>: <i>Double</i>
<a href="#sku" title="Sku">Sku</a>: <i>String</i>
</pre>

## Properties

#### Count

The number of GPUs which should be assigned to this container. Allowed values are `1`, `2`, or `4`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

The Sku which should be used for the GPU. Possible values are `K80`, `P100`, or `V100`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

