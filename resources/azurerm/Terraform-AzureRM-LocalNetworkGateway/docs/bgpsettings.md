# Terraform::AzureRM::LocalNetworkGateway BgpSettings

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

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpPeeringAddress

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerWeight

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
