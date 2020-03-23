# Terraform::AWS::Route

Provides a resource to create a routing table entry (a route) in a VPC routing table.

~> **NOTE on Route Tables and Routes:** Terraform currently
provides both a standalone Route resource and a [Route Table](route_table.html) resource with routes
defined in-line. At this time you cannot use a Route Table with in-line routes
in conjunction with any Route resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::Route",
    "Properties" : {
        "<a href="#destinationcidrblock" title="DestinationCidrBlock">DestinationCidrBlock</a>" : <i>String</i>,
        "<a href="#destinationipv6cidrblock" title="DestinationIpv6CidrBlock">DestinationIpv6CidrBlock</a>" : <i>String</i>,
        "<a href="#egressonlygatewayid" title="EgressOnlyGatewayId">EgressOnlyGatewayId</a>" : <i>String</i>,
        "<a href="#gatewayid" title="GatewayId">GatewayId</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#natgatewayid" title="NatGatewayId">NatGatewayId</a>" : <i>String</i>,
        "<a href="#networkinterfaceid" title="NetworkInterfaceId">NetworkInterfaceId</a>" : <i>String</i>,
        "<a href="#routetableid" title="RouteTableId">RouteTableId</a>" : <i>String</i>,
        "<a href="#transitgatewayid" title="TransitGatewayId">TransitGatewayId</a>" : <i>String</i>,
        "<a href="#vpcpeeringconnectionid" title="VpcPeeringConnectionId">VpcPeeringConnectionId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::Route
Properties:
    <a href="#destinationcidrblock" title="DestinationCidrBlock">DestinationCidrBlock</a>: <i>String</i>
    <a href="#destinationipv6cidrblock" title="DestinationIpv6CidrBlock">DestinationIpv6CidrBlock</a>: <i>String</i>
    <a href="#egressonlygatewayid" title="EgressOnlyGatewayId">EgressOnlyGatewayId</a>: <i>String</i>
    <a href="#gatewayid" title="GatewayId">GatewayId</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#natgatewayid" title="NatGatewayId">NatGatewayId</a>: <i>String</i>
    <a href="#networkinterfaceid" title="NetworkInterfaceId">NetworkInterfaceId</a>: <i>String</i>
    <a href="#routetableid" title="RouteTableId">RouteTableId</a>: <i>String</i>
    <a href="#transitgatewayid" title="TransitGatewayId">TransitGatewayId</a>: <i>String</i>
    <a href="#vpcpeeringconnectionid" title="VpcPeeringConnectionId">VpcPeeringConnectionId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### DestinationCidrBlock

The destination CIDR block.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationIpv6CidrBlock

The destination IPv6 CIDR block.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressOnlyGatewayId

Identifier of a VPC Egress Only Internet Gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayId

Identifier of a VPC internet gateway or a virtual private gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

Identifier of an EC2 instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatGatewayId

Identifier of a VPC NAT gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterfaceId

Identifier of an EC2 network interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteTableId

The ID of the routing table.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGatewayId

Identifier of an EC2 Transit Gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcPeeringConnectionId

Identifier of a VPC peering connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DestinationPrefixListId

Returns the <code>DestinationPrefixListId</code> value.

#### Id

Returns the <code>Id</code> value.

#### InstanceOwnerId

Returns the <code>InstanceOwnerId</code> value.

#### Origin

Returns the <code>Origin</code> value.

#### State

Returns the <code>State</code> value.

