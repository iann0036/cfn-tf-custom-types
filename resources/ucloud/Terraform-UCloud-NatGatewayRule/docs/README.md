# Terraform::UCloud::NatGatewayRule

Provides a Nat Gateway resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::UCloud::NatGatewayRule",
    "Properties" : {
        "<a href="#dstip" title="DstIp">DstIp</a>" : <i>String</i>,
        "<a href="#dstportrange" title="DstPortRange">DstPortRange</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#natgatewayid" title="NatGatewayId">NatGatewayId</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#srceipid" title="SrcEipId">SrcEipId</a>" : <i>String</i>,
        "<a href="#srcportrange" title="SrcPortRange">SrcPortRange</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::UCloud::NatGatewayRule
Properties:
    <a href="#dstip" title="DstIp">DstIp</a>: <i>String</i>
    <a href="#dstportrange" title="DstPortRange">DstPortRange</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#natgatewayid" title="NatGatewayId">NatGatewayId</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#srceipid" title="SrcEipId">SrcEipId</a>: <i>String</i>
    <a href="#srcportrange" title="SrcPortRange">SrcPortRange</a>: <i>String</i>
</pre>

## Properties

#### DstIp

The private ip of instance bound to the jNAT gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstPortRange

The range of port numbers of the private ip, range: 1-65535. (eg: `port` or `port1-port2`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Nat Gateway Rule which contains 6-63 characters and only support Chinese, English, numbers, '-', '_' and '.'. If not specified, terraform will auto-generate a name beginning with `tf-nat-gateway-rule-`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatGatewayId

The ID of the Nat Gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The protocol of the Nat Gateway Rule. Possible values: `tcp`, `udp`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcEipId

The ID of eip associate to the Nat Gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcPortRange

The range of port numbers of the eip, range: 1-65535. (eg: `port` or `port1-port2`).

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

