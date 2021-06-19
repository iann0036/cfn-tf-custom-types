# TF::AzureRM::VpnGatewayConnection RoutingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#associatedroutetable" title="AssociatedRouteTable">AssociatedRouteTable</a>" : <i>String</i>,
    "<a href="#propagatedroutetables" title="PropagatedRouteTables">PropagatedRouteTables</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#associatedroutetable" title="AssociatedRouteTable">AssociatedRouteTable</a>: <i>String</i>
<a href="#propagatedroutetables" title="PropagatedRouteTables">PropagatedRouteTables</a>: <i>
      - String</i>
</pre>

## Properties

#### AssociatedRouteTable

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropagatedRouteTables

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

