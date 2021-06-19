# TF::AzureStack::LocalNetworkGateway BgpSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#asn" title="Asn">Asn</a>" : <i>Double</i>,
    "<a href="#bgppeeringaddress" title="BgpPeeringAddress">BgpPeeringAddress</a>" : <i>String</i>,
    "<a href="#peerweight" title="PeerWeight">PeerWeight</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#asn" title="Asn">Asn</a>: <i>Double</i>
<a href="#bgppeeringaddress" title="BgpPeeringAddress">BgpPeeringAddress</a>: <i>String</i>
<a href="#peerweight" title="PeerWeight">PeerWeight</a>: <i>Double</i>
</pre>

## Properties

#### Asn

The BGP speaker's ASN.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpPeeringAddress

The BGP peering address and BGP identifier
of this BGP speaker.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerWeight

The weight added to routes learned from this
BGP speaker.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

