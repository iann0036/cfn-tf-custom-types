# Terraform::OpenStack::NetworkingSubnetRouteV2

Creates a routing entry on a OpenStack V2 subnet.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::NetworkingSubnetRouteV2",
    "Properties" : {
        "<a href="#destinationcidr" title="DestinationCidr">DestinationCidr</a>" : <i>String</i>,
        "<a href="#nexthop" title="NextHop">NextHop</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::NetworkingSubnetRouteV2
Properties:
    <a href="#destinationcidr" title="DestinationCidr">DestinationCidr</a>: <i>String</i>
    <a href="#nexthop" title="NextHop">NextHop</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
</pre>

## Properties

#### DestinationCidr

CIDR block to match on the packet’s destination IP. Changing
this creates a new routing entry.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHop

IP address of the next hop gateway.  Changing
this creates a new routing entry.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
routing entry.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

ID of the subnet this routing entry belongs to. Changing
this creates a new routing entry.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

