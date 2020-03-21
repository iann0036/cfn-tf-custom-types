# Terraform::AWS::VpnConnection

CloudFormation equivalent of aws_vpn_connection

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::VpnConnection",
    "Properties" : {
        "<a href="#customergatewayid" title="CustomerGatewayId">CustomerGatewayId</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#staticroutesonly" title="StaticRoutesOnly">StaticRoutesOnly</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#transitgatewayid" title="TransitGatewayId">TransitGatewayId</a>" : <i>String</i>,
        "<a href="#tunnel1insidecidr" title="Tunnel1InsideCidr">Tunnel1InsideCidr</a>" : <i>String</i>,
        "<a href="#tunnel1presharedkey" title="Tunnel1PresharedKey">Tunnel1PresharedKey</a>" : <i>String</i>,
        "<a href="#tunnel2insidecidr" title="Tunnel2InsideCidr">Tunnel2InsideCidr</a>" : <i>String</i>,
        "<a href="#tunnel2presharedkey" title="Tunnel2PresharedKey">Tunnel2PresharedKey</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::VpnConnection
Properties:
    <a href="#customergatewayid" title="CustomerGatewayId">CustomerGatewayId</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#staticroutesonly" title="StaticRoutesOnly">StaticRoutesOnly</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#transitgatewayid" title="TransitGatewayId">TransitGatewayId</a>: <i>String</i>
    <a href="#tunnel1insidecidr" title="Tunnel1InsideCidr">Tunnel1InsideCidr</a>: <i>String</i>
    <a href="#tunnel1presharedkey" title="Tunnel1PresharedKey">Tunnel1PresharedKey</a>: <i>String</i>
    <a href="#tunnel2insidecidr" title="Tunnel2InsideCidr">Tunnel2InsideCidr</a>: <i>String</i>
    <a href="#tunnel2presharedkey" title="Tunnel2PresharedKey">Tunnel2PresharedKey</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>: <i>String</i>
</pre>

## Properties

#### CustomerGatewayId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticRoutesOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGatewayId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1InsideCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1PresharedKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2InsideCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2PresharedKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnGatewayId

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

#### CustomerGatewayConfiguration

Returns the &lt;code&gt;CustomerGatewayConfiguration&lt;/code&gt; value.

#### Routes

Returns the &lt;code&gt;Routes&lt;/code&gt; value.

#### TransitGatewayAttachmentId

Returns the &lt;code&gt;TransitGatewayAttachmentId&lt;/code&gt; value.

#### Tunnel1Address

Returns the &lt;code&gt;Tunnel1Address&lt;/code&gt; value.

#### Tunnel1BgpAsn

Returns the &lt;code&gt;Tunnel1BgpAsn&lt;/code&gt; value.

#### Tunnel1BgpHoldtime

Returns the &lt;code&gt;Tunnel1BgpHoldtime&lt;/code&gt; value.

#### Tunnel1CgwInsideAddress

Returns the &lt;code&gt;Tunnel1CgwInsideAddress&lt;/code&gt; value.

#### Tunnel1VgwInsideAddress

Returns the &lt;code&gt;Tunnel1VgwInsideAddress&lt;/code&gt; value.

#### Tunnel2Address

Returns the &lt;code&gt;Tunnel2Address&lt;/code&gt; value.

#### Tunnel2BgpAsn

Returns the &lt;code&gt;Tunnel2BgpAsn&lt;/code&gt; value.

#### Tunnel2BgpHoldtime

Returns the &lt;code&gt;Tunnel2BgpHoldtime&lt;/code&gt; value.

#### Tunnel2CgwInsideAddress

Returns the &lt;code&gt;Tunnel2CgwInsideAddress&lt;/code&gt; value.

#### Tunnel2VgwInsideAddress

Returns the &lt;code&gt;Tunnel2VgwInsideAddress&lt;/code&gt; value.

#### VgwTelemetry

Returns the &lt;code&gt;VgwTelemetry&lt;/code&gt; value.

