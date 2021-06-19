# TF::AzureRM::VirtualNetworkGateway BgpSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#asn" title="Asn">Asn</a>" : <i>Double</i>,
    "<a href="#peerweight" title="PeerWeight">PeerWeight</a>" : <i>Double</i>,
    "<a href="#peeringaddress" title="PeeringAddress">PeeringAddress</a>" : <i>String</i>,
    "<a href="#peeringaddresses" title="PeeringAddresses">PeeringAddresses</a>" : <i>[ <a href="peeringaddressesdefinition.md">PeeringAddressesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#asn" title="Asn">Asn</a>: <i>Double</i>
<a href="#peerweight" title="PeerWeight">PeerWeight</a>: <i>Double</i>
<a href="#peeringaddress" title="PeeringAddress">PeeringAddress</a>: <i>String</i>
<a href="#peeringaddresses" title="PeeringAddresses">PeeringAddresses</a>: <i>
      - <a href="peeringaddressesdefinition.md">PeeringAddressesDefinition</a></i>
</pre>

## Properties

#### Asn

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerWeight

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeeringAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeeringAddresses

_Required_: No

_Type_: List of <a href="peeringaddressesdefinition.md">PeeringAddressesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

