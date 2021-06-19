# TF::Thunder::VrrpPeerGroup PeerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ippeeraddresscfg" title="IpPeerAddressCfg">IpPeerAddressCfg</a>" : <i>[ <a href="ippeeraddresscfgdefinition.md">IpPeerAddressCfgDefinition</a>, ... ]</i>,
    "<a href="#ipv6peeraddresscfg" title="Ipv6PeerAddressCfg">Ipv6PeerAddressCfg</a>" : <i>[ <a href="ipv6peeraddresscfgdefinition.md">Ipv6PeerAddressCfgDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ippeeraddresscfg" title="IpPeerAddressCfg">IpPeerAddressCfg</a>: <i>
      - <a href="ippeeraddresscfgdefinition.md">IpPeerAddressCfgDefinition</a></i>
<a href="#ipv6peeraddresscfg" title="Ipv6PeerAddressCfg">Ipv6PeerAddressCfg</a>: <i>
      - <a href="ipv6peeraddresscfgdefinition.md">Ipv6PeerAddressCfgDefinition</a></i>
</pre>

## Properties

#### IpPeerAddressCfg

_Required_: No

_Type_: List of <a href="ippeeraddresscfgdefinition.md">IpPeerAddressCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6PeerAddressCfg

_Required_: No

_Type_: List of <a href="ipv6peeraddresscfgdefinition.md">Ipv6PeerAddressCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

