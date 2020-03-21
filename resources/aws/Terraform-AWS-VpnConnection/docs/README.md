# Terraform::AWS::VpnConnection

CloudFormation equivalent of aws_vpn_connection

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::VpnConnection",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#customergatewayconfiguration" title="CustomerGatewayConfiguration">CustomerGatewayConfiguration</a>" : <i>String</i>,
        "<a href="#customergatewayid" title="CustomerGatewayId">CustomerGatewayId</a>" : <i>String</i>,
        "<a href="#routes" title="Routes">Routes</a>" : <i>[ &lt;a href=&#34;routes.md&#34;&gt;Routes&lt;/a&gt;, ... ]</i>,
        "<a href="#staticroutesonly" title="StaticRoutesOnly">StaticRoutesOnly</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#transitgatewayattachmentid" title="TransitGatewayAttachmentId">TransitGatewayAttachmentId</a>" : <i>String</i>,
        "<a href="#transitgatewayid" title="TransitGatewayId">TransitGatewayId</a>" : <i>String</i>,
        "<a href="#tunnel1address" title="Tunnel1Address">Tunnel1Address</a>" : <i>String</i>,
        "<a href="#tunnel1bgpasn" title="Tunnel1BgpAsn">Tunnel1BgpAsn</a>" : <i>String</i>,
        "<a href="#tunnel1bgpholdtime" title="Tunnel1BgpHoldtime">Tunnel1BgpHoldtime</a>" : <i>Double</i>,
        "<a href="#tunnel1cgwinsideaddress" title="Tunnel1CgwInsideAddress">Tunnel1CgwInsideAddress</a>" : <i>String</i>,
        "<a href="#tunnel1insidecidr" title="Tunnel1InsideCidr">Tunnel1InsideCidr</a>" : <i>String</i>,
        "<a href="#tunnel1presharedkey" title="Tunnel1PresharedKey">Tunnel1PresharedKey</a>" : <i>String</i>,
        "<a href="#tunnel1vgwinsideaddress" title="Tunnel1VgwInsideAddress">Tunnel1VgwInsideAddress</a>" : <i>String</i>,
        "<a href="#tunnel2address" title="Tunnel2Address">Tunnel2Address</a>" : <i>String</i>,
        "<a href="#tunnel2bgpasn" title="Tunnel2BgpAsn">Tunnel2BgpAsn</a>" : <i>String</i>,
        "<a href="#tunnel2bgpholdtime" title="Tunnel2BgpHoldtime">Tunnel2BgpHoldtime</a>" : <i>Double</i>,
        "<a href="#tunnel2cgwinsideaddress" title="Tunnel2CgwInsideAddress">Tunnel2CgwInsideAddress</a>" : <i>String</i>,
        "<a href="#tunnel2insidecidr" title="Tunnel2InsideCidr">Tunnel2InsideCidr</a>" : <i>String</i>,
        "<a href="#tunnel2presharedkey" title="Tunnel2PresharedKey">Tunnel2PresharedKey</a>" : <i>String</i>,
        "<a href="#tunnel2vgwinsideaddress" title="Tunnel2VgwInsideAddress">Tunnel2VgwInsideAddress</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vgwtelemetry" title="VgwTelemetry">VgwTelemetry</a>" : <i>[ &lt;a href=&#34;vgwtelemetry.md&#34;&gt;VgwTelemetry&lt;/a&gt;, ... ]</i>,
        "<a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::VpnConnection
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#customergatewayconfiguration" title="CustomerGatewayConfiguration">CustomerGatewayConfiguration</a>: <i>String</i>
    <a href="#customergatewayid" title="CustomerGatewayId">CustomerGatewayId</a>: <i>String</i>
    <a href="#routes" title="Routes">Routes</a>: <i>
      - &lt;a href=&#34;routes.md&#34;&gt;Routes&lt;/a&gt;</i>
    <a href="#staticroutesonly" title="StaticRoutesOnly">StaticRoutesOnly</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#transitgatewayattachmentid" title="TransitGatewayAttachmentId">TransitGatewayAttachmentId</a>: <i>String</i>
    <a href="#transitgatewayid" title="TransitGatewayId">TransitGatewayId</a>: <i>String</i>
    <a href="#tunnel1address" title="Tunnel1Address">Tunnel1Address</a>: <i>String</i>
    <a href="#tunnel1bgpasn" title="Tunnel1BgpAsn">Tunnel1BgpAsn</a>: <i>String</i>
    <a href="#tunnel1bgpholdtime" title="Tunnel1BgpHoldtime">Tunnel1BgpHoldtime</a>: <i>Double</i>
    <a href="#tunnel1cgwinsideaddress" title="Tunnel1CgwInsideAddress">Tunnel1CgwInsideAddress</a>: <i>String</i>
    <a href="#tunnel1insidecidr" title="Tunnel1InsideCidr">Tunnel1InsideCidr</a>: <i>String</i>
    <a href="#tunnel1presharedkey" title="Tunnel1PresharedKey">Tunnel1PresharedKey</a>: <i>String</i>
    <a href="#tunnel1vgwinsideaddress" title="Tunnel1VgwInsideAddress">Tunnel1VgwInsideAddress</a>: <i>String</i>
    <a href="#tunnel2address" title="Tunnel2Address">Tunnel2Address</a>: <i>String</i>
    <a href="#tunnel2bgpasn" title="Tunnel2BgpAsn">Tunnel2BgpAsn</a>: <i>String</i>
    <a href="#tunnel2bgpholdtime" title="Tunnel2BgpHoldtime">Tunnel2BgpHoldtime</a>: <i>Double</i>
    <a href="#tunnel2cgwinsideaddress" title="Tunnel2CgwInsideAddress">Tunnel2CgwInsideAddress</a>: <i>String</i>
    <a href="#tunnel2insidecidr" title="Tunnel2InsideCidr">Tunnel2InsideCidr</a>: <i>String</i>
    <a href="#tunnel2presharedkey" title="Tunnel2PresharedKey">Tunnel2PresharedKey</a>: <i>String</i>
    <a href="#tunnel2vgwinsideaddress" title="Tunnel2VgwInsideAddress">Tunnel2VgwInsideAddress</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vgwtelemetry" title="VgwTelemetry">VgwTelemetry</a>: <i>
      - &lt;a href=&#34;vgwtelemetry.md&#34;&gt;VgwTelemetry&lt;/a&gt;</i>
    <a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerGatewayConfiguration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerGatewayId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routes

_Required_: No

_Type_: List of &lt;a href=&#34;routes.md&#34;&gt;Routes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticRoutesOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGatewayAttachmentId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGatewayId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1Address

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1BgpAsn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1BgpHoldtime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1CgwInsideAddress

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

#### Tunnel1VgwInsideAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2Address

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2BgpAsn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2BgpHoldtime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2CgwInsideAddress

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

#### Tunnel2VgwInsideAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VgwTelemetry

_Required_: No

_Type_: List of &lt;a href=&#34;vgwtelemetry.md&#34;&gt;VgwTelemetry&lt;/a&gt;

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

