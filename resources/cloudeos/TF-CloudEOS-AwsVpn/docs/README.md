# TF::CloudEOS::AwsVpn

The `cloudeos_aws_vpn` resource sends the Ipsec Site-Site VPN connections and attachments information created in AWS to
CVaaS to configure the CloudEOS router with the Ipsec VTI Tunnel in a given CNPS segment ( VRF ). This resource works
for Site-Site VPN connections attached to AWS Transit Gateway Route tables and AWS VPN Gateways.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CloudEOS::AwsVpn",
    "Properties" : {
        "<a href="#cgwid" title="CgwId">CgwId</a>" : <i>String</i>,
        "<a href="#cnps" title="Cnps">Cnps</a>" : <i>String</i>,
        "<a href="#routerid" title="RouterId">RouterId</a>" : <i>String</i>,
        "<a href="#tgwid" title="TgwId">TgwId</a>" : <i>String</i>,
        "<a href="#tunnel1awsendpointip" title="Tunnel1AwsEndpointIp">Tunnel1AwsEndpointIp</a>" : <i>String</i>,
        "<a href="#tunnel1awsoverlayip" title="Tunnel1AwsOverlayIp">Tunnel1AwsOverlayIp</a>" : <i>String</i>,
        "<a href="#tunnel1bgpasn" title="Tunnel1BgpAsn">Tunnel1BgpAsn</a>" : <i>String</i>,
        "<a href="#tunnel1bgpholdtime" title="Tunnel1BgpHoldtime">Tunnel1BgpHoldtime</a>" : <i>String</i>,
        "<a href="#tunnel1presharedkey" title="Tunnel1PresharedKey">Tunnel1PresharedKey</a>" : <i>String</i>,
        "<a href="#tunnel1routeroverlayip" title="Tunnel1RouterOverlayIp">Tunnel1RouterOverlayIp</a>" : <i>String</i>,
        "<a href="#tunnel2awsendpointip" title="Tunnel2AwsEndpointIp">Tunnel2AwsEndpointIp</a>" : <i>String</i>,
        "<a href="#tunnel2awsoverlayip" title="Tunnel2AwsOverlayIp">Tunnel2AwsOverlayIp</a>" : <i>String</i>,
        "<a href="#tunnel2bgpasn" title="Tunnel2BgpAsn">Tunnel2BgpAsn</a>" : <i>String</i>,
        "<a href="#tunnel2bgpholdtime" title="Tunnel2BgpHoldtime">Tunnel2BgpHoldtime</a>" : <i>String</i>,
        "<a href="#tunnel2presharedkey" title="Tunnel2PresharedKey">Tunnel2PresharedKey</a>" : <i>String</i>,
        "<a href="#tunnel2routeroverlayip" title="Tunnel2RouterOverlayIp">Tunnel2RouterOverlayIp</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#vpnconnectionid" title="VpnConnectionId">VpnConnectionId</a>" : <i>String</i>,
        "<a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>" : <i>String</i>,
        "<a href="#vpntgwattachmentid" title="VpnTgwAttachmentId">VpnTgwAttachmentId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CloudEOS::AwsVpn
Properties:
    <a href="#cgwid" title="CgwId">CgwId</a>: <i>String</i>
    <a href="#cnps" title="Cnps">Cnps</a>: <i>String</i>
    <a href="#routerid" title="RouterId">RouterId</a>: <i>String</i>
    <a href="#tgwid" title="TgwId">TgwId</a>: <i>String</i>
    <a href="#tunnel1awsendpointip" title="Tunnel1AwsEndpointIp">Tunnel1AwsEndpointIp</a>: <i>String</i>
    <a href="#tunnel1awsoverlayip" title="Tunnel1AwsOverlayIp">Tunnel1AwsOverlayIp</a>: <i>String</i>
    <a href="#tunnel1bgpasn" title="Tunnel1BgpAsn">Tunnel1BgpAsn</a>: <i>String</i>
    <a href="#tunnel1bgpholdtime" title="Tunnel1BgpHoldtime">Tunnel1BgpHoldtime</a>: <i>String</i>
    <a href="#tunnel1presharedkey" title="Tunnel1PresharedKey">Tunnel1PresharedKey</a>: <i>String</i>
    <a href="#tunnel1routeroverlayip" title="Tunnel1RouterOverlayIp">Tunnel1RouterOverlayIp</a>: <i>String</i>
    <a href="#tunnel2awsendpointip" title="Tunnel2AwsEndpointIp">Tunnel2AwsEndpointIp</a>: <i>String</i>
    <a href="#tunnel2awsoverlayip" title="Tunnel2AwsOverlayIp">Tunnel2AwsOverlayIp</a>: <i>String</i>
    <a href="#tunnel2bgpasn" title="Tunnel2BgpAsn">Tunnel2BgpAsn</a>: <i>String</i>
    <a href="#tunnel2bgpholdtime" title="Tunnel2BgpHoldtime">Tunnel2BgpHoldtime</a>: <i>String</i>
    <a href="#tunnel2presharedkey" title="Tunnel2PresharedKey">Tunnel2PresharedKey</a>: <i>String</i>
    <a href="#tunnel2routeroverlayip" title="Tunnel2RouterOverlayIp">Tunnel2RouterOverlayIp</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#vpnconnectionid" title="VpnConnectionId">VpnConnectionId</a>: <i>String</i>
    <a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>: <i>String</i>
    <a href="#vpntgwattachmentid" title="VpnTgwAttachmentId">VpnTgwAttachmentId</a>: <i>String</i>
</pre>

## Properties

#### CgwId

AWS Customer Gateway ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cnps

VRF Segment in which the Ipsec VPN is created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouterId

CloudEOS Router to which the AWS Ipsec VPN terminates.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TgwId

AWS Transit Gateway ID, if the AWS Site-to-Site connection terminates on a TGW.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1AwsEndpointIp

AWS Tunnel1 Underlay IP Address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1AwsOverlayIp

VPN Tunnel1 IP address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1BgpAsn

AWS VPN Tunnel1 BGP ASN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1BgpHoldtime

VPN Tunnel1 BGP Hold time.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1PresharedKey

VPN Tunnel1 Ipsec Preshared key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1RouterOverlayIp

CloudEOS Router Tunnel1 IP address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2AwsEndpointIp

AWS VPN Tunnel2 Underlay IP Address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2AwsOverlayIp

AWS VPN Tunnel2 IP address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2BgpAsn

AWS VPN Tunnel2 BGP ASN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2BgpHoldtime

VPN Tunnel2 BGP Hold time.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2PresharedKey

VPN Tunnel2 Ipsec Preshared key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2RouterOverlayIp

CloudEOS Router Tunnel2 IP address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnConnectionId

AWS Site-to-Site VPN Connection ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnGatewayId

AWS VPN Gateway ID, if the AWS Site-to-Site connection terminates on a VPN Gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnTgwAttachmentId

AWS VPN Transit Gateway Attachment ID.

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

#### Id

Returns the <code>Id</code> value.

#### TfId

Returns the <code>TfId</code> value.

