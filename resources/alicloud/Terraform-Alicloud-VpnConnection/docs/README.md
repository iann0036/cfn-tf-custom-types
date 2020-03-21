# Terraform::Alicloud::VpnConnection

CloudFormation equivalent of alicloud_vpn_connection

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::VpnConnection",
    "Properties" : {
        "<a href="#customergatewayid" title="CustomerGatewayId">CustomerGatewayId</a>" : <i>String</i>,
        "<a href="#effectimmediately" title="EffectImmediately">EffectImmediately</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#localsubnet" title="LocalSubnet">LocalSubnet</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#remotesubnet" title="RemoteSubnet">RemoteSubnet</a>" : <i>[ String, ... ]</i>,
        "<a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>" : <i>String</i>,
        "<a href="#ikeconfig" title="IkeConfig">IkeConfig</a>" : <i>[ &lt;a href=&#34;ikeconfig.md&#34;&gt;IkeConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#ipsecconfig" title="IpsecConfig">IpsecConfig</a>" : <i>[ &lt;a href=&#34;ipsecconfig.md&#34;&gt;IpsecConfig&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::VpnConnection
Properties:
    <a href="#customergatewayid" title="CustomerGatewayId">CustomerGatewayId</a>: <i>String</i>
    <a href="#effectimmediately" title="EffectImmediately">EffectImmediately</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#localsubnet" title="LocalSubnet">LocalSubnet</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#remotesubnet" title="RemoteSubnet">RemoteSubnet</a>: <i>
      - String</i>
    <a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>: <i>String</i>
    <a href="#ikeconfig" title="IkeConfig">IkeConfig</a>: <i>
      - &lt;a href=&#34;ikeconfig.md&#34;&gt;IkeConfig&lt;/a&gt;</i>
    <a href="#ipsecconfig" title="IpsecConfig">IpsecConfig</a>: <i>
      - &lt;a href=&#34;ipsecconfig.md&#34;&gt;IpsecConfig&lt;/a&gt;</i>
</pre>

## Properties

#### CustomerGatewayId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EffectImmediately

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSubnet

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteSubnet

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnGatewayId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeConfig

_Required_: No

_Type_: List of &lt;a href=&#34;ikeconfig.md&#34;&gt;IkeConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecConfig

_Required_: No

_Type_: List of &lt;a href=&#34;ipsecconfig.md&#34;&gt;IpsecConfig&lt;/a&gt;

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

Returns the &lt;code&gt;Status&lt;/code&gt; value.

