# Terraform::Alicloud::VpnGateway

Provides a VPN gateway resource.

-> **NOTE:** Terraform will auto build vpn instance  while it uses `alicloud_vpn_gateway` to build a vpn resource.

-> Currently International-Site account can open `PostPaid` VPN gateway and China-Site account can open `PrePaid` VPN gateway.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::VpnGateway",
    "Properties" : {
        "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enableipsec" title="EnableIpsec">EnableIpsec</a>" : <i>Boolean</i>,
        "<a href="#enablessl" title="EnableSsl">EnableSsl</a>" : <i>Boolean</i>,
        "<a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#sslconnections" title="SslConnections">SslConnections</a>" : <i>Double</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#vswitchid" title="VswitchId">VswitchId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::VpnGateway
Properties:
    <a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enableipsec" title="EnableIpsec">EnableIpsec</a>: <i>Boolean</i>
    <a href="#enablessl" title="EnableSsl">EnableSsl</a>: <i>Boolean</i>
    <a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#sslconnections" title="SslConnections">SslConnections</a>: <i>Double</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#vswitchid" title="VswitchId">VswitchId</a>: <i>String</i>
</pre>

## Properties

#### Bandwidth

The value should be 10, 100, 200. if the user is postpaid, otherwise it can be 5, 10, 20, 50, 100, 200.
It can't be changed by terraform.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the VPN instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableIpsec

Enable or Disable IPSec VPN. At least one type of VPN should be enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSsl

Enable or Disable SSL VPN.  At least one type of VPN should be enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceChargeType

The charge type for instance. If it is an international site account, the valid value is PostPaid, otherwise PrePaid.
Default to PostPaid.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the VPN. Defaults to null.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

The filed is only required while the InstanceChargeType is PrePaid. Valid values: [1-9, 12, 24, 36]. Default to 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslConnections

The max connections of SSL VPN. Default to 5. The number of connections supported by each account is different.
This field is ignored when enable_ssl is false.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

The VPN belongs the vpc_id, the field can't be changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchId

The VPN belongs the vswitch_id, the field can't be changed.

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

#### BusinessStatus

Returns the <code>BusinessStatus</code> value.

#### InternetIp

Returns the <code>InternetIp</code> value.

#### Status

Returns the <code>Status</code> value.

