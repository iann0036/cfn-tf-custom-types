# TF::NSXT::PolicyTier1Gateway RouteAdvertisementRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#prefixoperator" title="PrefixOperator">PrefixOperator</a>" : <i>String</i>,
    "<a href="#routeadvertisementtypes" title="RouteAdvertisementTypes">RouteAdvertisementTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#subnets" title="Subnets">Subnets</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#prefixoperator" title="PrefixOperator">PrefixOperator</a>: <i>String</i>
<a href="#routeadvertisementtypes" title="RouteAdvertisementTypes">RouteAdvertisementTypes</a>: <i>
      - String</i>
<a href="#subnets" title="Subnets">Subnets</a>: <i>
      - String</i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixOperator

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteAdvertisementTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnets

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

