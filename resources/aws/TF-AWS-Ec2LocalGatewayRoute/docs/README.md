# TF::AWS::Ec2LocalGatewayRoute

Manages an EC2 Local Gateway Route. More information can be found in the [Outposts User Guide](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-networking-components.html#routing).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Ec2LocalGatewayRoute",
    "Properties" : {
        "<a href="#destinationcidrblock" title="DestinationCidrBlock">DestinationCidrBlock</a>" : <i>String</i>,
        "<a href="#localgatewayroutetableid" title="LocalGatewayRouteTableId">LocalGatewayRouteTableId</a>" : <i>String</i>,
        "<a href="#localgatewayvirtualinterfacegroupid" title="LocalGatewayVirtualInterfaceGroupId">LocalGatewayVirtualInterfaceGroupId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Ec2LocalGatewayRoute
Properties:
    <a href="#destinationcidrblock" title="DestinationCidrBlock">DestinationCidrBlock</a>: <i>String</i>
    <a href="#localgatewayroutetableid" title="LocalGatewayRouteTableId">LocalGatewayRouteTableId</a>: <i>String</i>
    <a href="#localgatewayvirtualinterfacegroupid" title="LocalGatewayVirtualInterfaceGroupId">LocalGatewayVirtualInterfaceGroupId</a>: <i>String</i>
</pre>

## Properties

#### DestinationCidrBlock

IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalGatewayRouteTableId

Identifier of EC2 Local Gateway Route Table.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalGatewayVirtualInterfaceGroupId

Identifier of EC2 Local Gateway Virtual Interface Group.

_Required_: Yes

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

#### Id

Returns the <code>Id</code> value.

