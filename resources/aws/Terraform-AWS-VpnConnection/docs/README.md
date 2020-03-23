# Terraform::AWS::VpnConnection

Manages an EC2 VPN connection. These objects can be connected to customer gateways, and allow you to establish tunnels between your network and Amazon.

~> **Note:** All arguments including `tunnel1_preshared_key` and `tunnel2_preshared_key` will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

~> **Note:** The CIDR blocks in the arguments `tunnel1_inside_cidr` and `tunnel2_inside_cidr` must have a prefix of /30 and be a part of a specific range.
[Read more about this in the AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpnTunnelOptionsSpecification.html).

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

The ID of the customer gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticRoutesOnly

Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don't support BGP.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Tags to apply to the connection.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGatewayId

The ID of the EC2 Transit Gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1InsideCidr

The CIDR block of the inside IP addresses for the first VPN tunnel.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1PresharedKey

The preshared key of the first VPN tunnel.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2InsideCidr

The CIDR block of the inside IP addresses for the second VPN tunnel.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2PresharedKey

The preshared key of the second VPN tunnel.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of VPN connection. The only type AWS supports at this time is "ipsec.1".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnGatewayId

The ID of the Virtual Private Gateway.

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

#### Id

Returns the <code>Id</code> value.

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

