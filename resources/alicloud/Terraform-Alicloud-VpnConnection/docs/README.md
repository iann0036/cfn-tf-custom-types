# Terraform::Alicloud::VpnConnection

Provides a VPN connection resource.

-> **NOTE:** Terraform will auto build vpn connection while it uses `alicloud_vpn_connection` to build a vpn connection resource.
             The vpn connection depends on VPN and VPN customer gateway.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::VpnConnection",
    "Properties" : {
        "<a href="#customergatewayid" title="CustomerGatewayId">CustomerGatewayId</a>" : <i>String</i>,
        "<a href="#effectimmediately" title="EffectImmediately">EffectImmediately</a>" : <i>Boolean</i>,
        "<a href="#localsubnet" title="LocalSubnet">LocalSubnet</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#remotesubnet" title="RemoteSubnet">RemoteSubnet</a>" : <i>[ String, ... ]</i>,
        "<a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>" : <i>String</i>,
        "<a href="#ikeconfig" title="IkeConfig">IkeConfig</a>" : <i>[ <a href="ikeconfig.md">IkeConfig</a>, ... ]</i>,
        "<a href="#ipsecconfig" title="IpsecConfig">IpsecConfig</a>" : <i>[ <a href="ipsecconfig.md">IpsecConfig</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::VpnConnection
Properties:
    <a href="#customergatewayid" title="CustomerGatewayId">CustomerGatewayId</a>: <i>String</i>
    <a href="#effectimmediately" title="EffectImmediately">EffectImmediately</a>: <i>Boolean</i>
    <a href="#localsubnet" title="LocalSubnet">LocalSubnet</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#remotesubnet" title="RemoteSubnet">RemoteSubnet</a>: <i>
      - String</i>
    <a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>: <i>String</i>
    <a href="#ikeconfig" title="IkeConfig">IkeConfig</a>: <i>
      - <a href="ikeconfig.md">IkeConfig</a></i>
    <a href="#ipsecconfig" title="IpsecConfig">IpsecConfig</a>: <i>
      - <a href="ipsecconfig.md">IpsecConfig</a></i>
</pre>

## Properties

#### CustomerGatewayId

The ID of the customer gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EffectImmediately

Whether to delete a successfully negotiated IPsec tunnel and initiate a negotiation again. Valid value:true,false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSubnet

The CIDR block of the VPC to be connected with the local data center. This parameter is used for phase-two negotiation.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the IPsec connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteSubnet

The CIDR block of the local data center. This parameter is used for phase-two negotiation.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnGatewayId

The ID of the VPN gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeConfig

_Required_: No

_Type_: List of <a href="ikeconfig.md">IkeConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecConfig

_Required_: No

_Type_: List of <a href="ipsecconfig.md">IpsecConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Status

Returns the <code>Status</code> value.

