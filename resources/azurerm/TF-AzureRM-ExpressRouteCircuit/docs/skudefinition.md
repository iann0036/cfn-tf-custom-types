# TF::AzureRM::ExpressRouteCircuit SkuDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#family" title="Family">Family</a>" : <i>String</i>,
    "<a href="#tier" title="Tier">Tier</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#family" title="Family">Family</a>: <i>String</i>
<a href="#tier" title="Tier">Tier</a>: <i>String</i>
</pre>

## Properties

#### Family

The billing mode for bandwidth. Possible values are `MeteredData` or `UnlimitedData`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier

The service tier. Possible values are `Basic`, `Local`, `Standard` or `Premium`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

