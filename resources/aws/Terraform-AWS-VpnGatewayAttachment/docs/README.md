# Terraform::AWS::VpnGatewayAttachment

Provides a Virtual Private Gateway attachment resource, allowing for an existing
hardware VPN gateway to be attached and/or detached from a VPC.

-> **Note:** The [`aws_vpn_gateway`](vpn_gateway.html)
resource can also automatically attach the Virtual Private Gateway it creates
to an existing VPC by setting the [`vpc_id`](vpn_gateway.html#vpc_id) attribute accordingly.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::VpnGatewayAttachment",
    "Properties" : {
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::VpnGatewayAttachment
Properties:
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>: <i>String</i>
</pre>

## Properties

#### VpcId

The ID of the VPC.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnGatewayId

The ID of the Virtual Private Gateway.

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

