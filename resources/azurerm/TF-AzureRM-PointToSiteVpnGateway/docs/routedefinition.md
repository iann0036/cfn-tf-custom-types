# TF::AzureRM::PointToSiteVpnGateway RouteDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#associatedroutetableid" title="AssociatedRouteTableId">AssociatedRouteTableId</a>" : <i>String</i>,
    "<a href="#propagatedroutetable" title="PropagatedRouteTable">PropagatedRouteTable</a>" : <i>[ <a href="propagatedroutetabledefinition.md">PropagatedRouteTableDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#associatedroutetableid" title="AssociatedRouteTableId">AssociatedRouteTableId</a>: <i>String</i>
<a href="#propagatedroutetable" title="PropagatedRouteTable">PropagatedRouteTable</a>: <i>
      - <a href="propagatedroutetabledefinition.md">PropagatedRouteTableDefinition</a></i>
</pre>

## Properties

#### AssociatedRouteTableId

The Virtual Hub Route Table resource id associated with this Routing Configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropagatedRouteTable

_Required_: No

_Type_: List of <a href="propagatedroutetabledefinition.md">PropagatedRouteTableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

