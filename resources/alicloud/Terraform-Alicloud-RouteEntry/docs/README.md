# Terraform::Alicloud::RouteEntry

Provides a route entry resource. A route entry represents a route item of one VPC route table.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::RouteEntry",
    "Properties" : {
        "<a href="#destinationcidrblock" title="DestinationCidrblock">DestinationCidrblock</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nexthopid" title="NexthopId">NexthopId</a>" : <i>String</i>,
        "<a href="#nexthoptype" title="NexthopType">NexthopType</a>" : <i>String</i>,
        "<a href="#routetableid" title="RouteTableId">RouteTableId</a>" : <i>String</i>,
        "<a href="#routerid" title="RouterId">RouterId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::RouteEntry
Properties:
    <a href="#destinationcidrblock" title="DestinationCidrblock">DestinationCidrblock</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nexthopid" title="NexthopId">NexthopId</a>: <i>String</i>
    <a href="#nexthoptype" title="NexthopType">NexthopType</a>: <i>String</i>
    <a href="#routetableid" title="RouteTableId">RouteTableId</a>: <i>String</i>
    <a href="#routerid" title="RouterId">RouterId</a>: <i>String</i>
</pre>

## Properties

#### DestinationCidrblock

The RouteEntry's target network segment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the route entry. This name can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin or end with a hyphen, and must not begin with http:// or https://.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NexthopId

The route entry's next hop. ECS instance ID or VPC router interface ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NexthopType

The next hop type. Available values:
- `Instance` (Default): Route the traffic destined for the destination CIDR block to an ECS instance in the VPC.
- `RouterInterface`: Route the traffic destined for the destination CIDR block to a router interface.
- `VpnGateway`: Route the traffic destined for the destination CIDR block to a VPN Gateway.
- `HaVip`: Route the traffic destined for the destination CIDR block to an HAVIP.
- `NetworkInterface`: Route the traffic destined for the destination CIDR block to an NetworkInterface.
- `NatGateway`: Route the traffic destined for the destination CIDR block to an Nat Gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteTableId

The ID of the route table.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouterId

This argument has beeb deprecated. Please use other arguments to launch a custom route entry.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

