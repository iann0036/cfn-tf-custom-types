# TF::AzureRM::VirtualHubConnection PropagatedRouteTableDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ String, ... ]</i>,
    "<a href="#routetableids" title="RouteTableIds">RouteTableIds</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#labels" title="Labels">Labels</a>: <i>
      - String</i>
<a href="#routetableids" title="RouteTableIds">RouteTableIds</a>: <i>
      - String</i>
</pre>

## Properties

#### Labels

The list of labels to assign to this route table.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteTableIds

A list of Route Table ID's to associated with this Virtual Hub Connection.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

