# TF::AzureRM::VpnGateway BgpSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#asn" title="Asn">Asn</a>" : <i>Double</i>,
    "<a href="#peerweight" title="PeerWeight">PeerWeight</a>" : <i>Double</i>,
    "<a href="#instance0bgppeeringaddress" title="Instance0BgpPeeringAddress">Instance0BgpPeeringAddress</a>" : <i>[ <a href="instance0bgppeeringaddressdefinition.md">Instance0BgpPeeringAddressDefinition</a>, ... ]</i>,
    "<a href="#instance1bgppeeringaddress" title="Instance1BgpPeeringAddress">Instance1BgpPeeringAddress</a>" : <i>[ <a href="instance1bgppeeringaddressdefinition.md">Instance1BgpPeeringAddressDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#asn" title="Asn">Asn</a>: <i>Double</i>
<a href="#peerweight" title="PeerWeight">PeerWeight</a>: <i>Double</i>
<a href="#instance0bgppeeringaddress" title="Instance0BgpPeeringAddress">Instance0BgpPeeringAddress</a>: <i>
      - <a href="instance0bgppeeringaddressdefinition.md">Instance0BgpPeeringAddressDefinition</a></i>
<a href="#instance1bgppeeringaddress" title="Instance1BgpPeeringAddress">Instance1BgpPeeringAddress</a>: <i>
      - <a href="instance1bgppeeringaddressdefinition.md">Instance1BgpPeeringAddressDefinition</a></i>
</pre>

## Properties

#### Asn

The ASN of the BGP Speaker. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerWeight

The weight added to Routes learned from this BGP Speaker. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instance0BgpPeeringAddress

_Required_: No

_Type_: List of <a href="instance0bgppeeringaddressdefinition.md">Instance0BgpPeeringAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instance1BgpPeeringAddress

_Required_: No

_Type_: List of <a href="instance1bgppeeringaddressdefinition.md">Instance1BgpPeeringAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

