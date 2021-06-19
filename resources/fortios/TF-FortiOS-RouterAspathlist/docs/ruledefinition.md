# TF::FortiOS::RouterAspathlist RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#regexp" title="Regexp">Regexp</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#regexp" title="Regexp">Regexp</a>: <i>String</i>
</pre>

## Properties

#### Action

Permit or deny route-based operations, based on the route's AS_PATH attribute. Valid values: `deny`, `permit`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regexp

Regular-expression to match the Border Gateway Protocol (BGP) AS paths.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

