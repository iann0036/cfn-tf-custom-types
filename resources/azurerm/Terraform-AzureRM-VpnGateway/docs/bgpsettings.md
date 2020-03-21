# Terraform::AzureRM::VpnGateway BgpSettings

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#asn" title="Asn">Asn</a>" : <i>Double</i>,
    "<a href="#peerweight" title="PeerWeight">PeerWeight</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#asn" title="Asn">Asn</a>: <i>Double</i>
<a href="#peerweight" title="PeerWeight">PeerWeight</a>: <i>Double</i>
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

