# TF::Thunder::VrrpVrid FloatingIpDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipaddresscfg" title="IpAddressCfg">IpAddressCfg</a>" : <i>[ <a href="ipaddresscfgdefinition.md">IpAddressCfgDefinition</a>, ... ]</i>,
    "<a href="#ipaddresspartcfg" title="IpAddressPartCfg">IpAddressPartCfg</a>" : <i>[ <a href="ipaddresspartcfgdefinition.md">IpAddressPartCfgDefinition</a>, ... ]</i>,
    "<a href="#ipv6addresscfg" title="Ipv6AddressCfg">Ipv6AddressCfg</a>" : <i>[ <a href="ipv6addresscfgdefinition.md">Ipv6AddressCfgDefinition</a>, ... ]</i>,
    "<a href="#ipv6addresspartcfg" title="Ipv6AddressPartCfg">Ipv6AddressPartCfg</a>" : <i>[ <a href="ipv6addresspartcfgdefinition.md">Ipv6AddressPartCfgDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipaddresscfg" title="IpAddressCfg">IpAddressCfg</a>: <i>
      - <a href="ipaddresscfgdefinition.md">IpAddressCfgDefinition</a></i>
<a href="#ipaddresspartcfg" title="IpAddressPartCfg">IpAddressPartCfg</a>: <i>
      - <a href="ipaddresspartcfgdefinition.md">IpAddressPartCfgDefinition</a></i>
<a href="#ipv6addresscfg" title="Ipv6AddressCfg">Ipv6AddressCfg</a>: <i>
      - <a href="ipv6addresscfgdefinition.md">Ipv6AddressCfgDefinition</a></i>
<a href="#ipv6addresspartcfg" title="Ipv6AddressPartCfg">Ipv6AddressPartCfg</a>: <i>
      - <a href="ipv6addresspartcfgdefinition.md">Ipv6AddressPartCfgDefinition</a></i>
</pre>

## Properties

#### IpAddressCfg

_Required_: No

_Type_: List of <a href="ipaddresscfgdefinition.md">IpAddressCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddressPartCfg

_Required_: No

_Type_: List of <a href="ipaddresspartcfgdefinition.md">IpAddressPartCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6AddressCfg

_Required_: No

_Type_: List of <a href="ipv6addresscfgdefinition.md">Ipv6AddressCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6AddressPartCfg

_Required_: No

_Type_: List of <a href="ipv6addresspartcfgdefinition.md">Ipv6AddressPartCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

