# TF::Thunder::VrrpVrid BgpDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bgpipv4addresscfg" title="BgpIpv4AddressCfg">BgpIpv4AddressCfg</a>" : <i>[ <a href="bgpipv4addresscfgdefinition.md">BgpIpv4AddressCfgDefinition</a>, ... ]</i>,
    "<a href="#bgpipv6addresscfg" title="BgpIpv6AddressCfg">BgpIpv6AddressCfg</a>" : <i>[ <a href="bgpipv6addresscfgdefinition.md">BgpIpv6AddressCfgDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bgpipv4addresscfg" title="BgpIpv4AddressCfg">BgpIpv4AddressCfg</a>: <i>
      - <a href="bgpipv4addresscfgdefinition.md">BgpIpv4AddressCfgDefinition</a></i>
<a href="#bgpipv6addresscfg" title="BgpIpv6AddressCfg">BgpIpv6AddressCfg</a>: <i>
      - <a href="bgpipv6addresscfgdefinition.md">BgpIpv6AddressCfgDefinition</a></i>
</pre>

## Properties

#### BgpIpv4AddressCfg

_Required_: No

_Type_: List of <a href="bgpipv4addresscfgdefinition.md">BgpIpv4AddressCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpIpv6AddressCfg

_Required_: No

_Type_: List of <a href="bgpipv6addresscfgdefinition.md">BgpIpv6AddressCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

