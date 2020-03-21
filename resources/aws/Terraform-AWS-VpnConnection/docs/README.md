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
        "<a href="#staticroutesonly" title="StaticRoutesOnly">StaticRoutesOnly</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
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
    <a href="#staticroutesonly" title="StaticRoutesOnly">StaticRoutesOnly</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
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

#### StaticRoutesOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

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

Returns the <code>CustomerGatewayConfiguration</code> value.

#### Routes

Returns the <code>Routes</code> value.

#### TransitGatewayAttachmentId

Returns the <code>TransitGatewayAttachmentId</code> value.

#### Tunnel1Address

Returns the <code>Tunnel1Address</code> value.

#### Tunnel1BgpAsn

Returns the <code>Tunnel1BgpAsn</code> value.

#### Tunnel1BgpHoldtime

Returns the <code>Tunnel1BgpHoldtime</code> value.

#### Tunnel1CgwInsideAddress

Returns the <code>Tunnel1CgwInsideAddress</code> value.

#### Tunnel1VgwInsideAddress

Returns the <code>Tunnel1VgwInsideAddress</code> value.

#### Tunnel2Address

Returns the <code>Tunnel2Address</code> value.

#### Tunnel2BgpAsn

Returns the <code>Tunnel2BgpAsn</code> value.

#### Tunnel2BgpHoldtime

Returns the <code>Tunnel2BgpHoldtime</code> value.

#### Tunnel2CgwInsideAddress

Returns the <code>Tunnel2CgwInsideAddress</code> value.

#### Tunnel2VgwInsideAddress

Returns the <code>Tunnel2VgwInsideAddress</code> value.

#### VgwTelemetry

Returns the <code>VgwTelemetry</code> value.

