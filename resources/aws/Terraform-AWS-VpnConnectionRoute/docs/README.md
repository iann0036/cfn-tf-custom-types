# Terraform::AWS::VpnConnectionRoute

Provides a static route between a VPN connection and a customer gateway.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::VpnConnectionRoute",
    "Properties" : {
        "<a href="#destinationcidrblock" title="DestinationCidrBlock">DestinationCidrBlock</a>" : <i>String</i>,
        "<a href="#vpnconnectionid" title="VpnConnectionId">VpnConnectionId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::VpnConnectionRoute
Properties:
    <a href="#destinationcidrblock" title="DestinationCidrBlock">DestinationCidrBlock</a>: <i>String</i>
    <a href="#vpnconnectionid" title="VpnConnectionId">VpnConnectionId</a>: <i>String</i>
</pre>

## Properties

#### DestinationCidrBlock

The CIDR block associated with the local subnet of the customer network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnConnectionId

The ID of the VPN connection.

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

