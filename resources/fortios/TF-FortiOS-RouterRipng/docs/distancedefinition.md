# TF::FortiOS::RouterRipng DistanceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesslist6" title="AccessList6">AccessList6</a>" : <i>String</i>,
    "<a href="#distance" title="Distance">Distance</a>" : <i>[ <a href="distancedefinition.md">DistanceDefinition</a>, ... ]</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#prefix6" title="Prefix6">Prefix6</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#accesslist6" title="AccessList6">AccessList6</a>: <i>String</i>
<a href="#distance" title="Distance">Distance</a>: <i>
      - <a href="distancedefinition.md">DistanceDefinition</a></i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#prefix6" title="Prefix6">Prefix6</a>: <i>String</i>
</pre>

## Properties

#### AccessList6

Access list for route destination.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Distance

_Required_: No

_Type_: List of <a href="distancedefinition.md">DistanceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Distance ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix6

Distance prefix6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

