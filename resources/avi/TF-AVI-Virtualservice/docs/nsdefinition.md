# TF::AVI::Virtualservice NsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nsname" title="Nsname">Nsname</a>" : <i>String</i>,
    "<a href="#ip6address" title="Ip6Address">Ip6Address</a>" : <i>[ <a href="ip6addressdefinition.md">Ip6AddressDefinition</a>, ... ]</i>,
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>[ <a href="ipaddressdefinition.md">IpAddressDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nsname" title="Nsname">Nsname</a>: <i>String</i>
<a href="#ip6address" title="Ip6Address">Ip6Address</a>: <i>
      - <a href="ip6addressdefinition.md">Ip6AddressDefinition</a></i>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>
      - <a href="ipaddressdefinition.md">IpAddressDefinition</a></i>
</pre>

## Properties

#### Nsname

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6Address

_Required_: No

_Type_: List of <a href="ip6addressdefinition.md">Ip6AddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No

_Type_: List of <a href="ipaddressdefinition.md">IpAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

