# TF::NSXT::PolicyFixedSegment SubnetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cidr" title="Cidr">Cidr</a>" : <i>String</i>,
    "<a href="#dhcpranges" title="DhcpRanges">DhcpRanges</a>" : <i>[ String, ... ]</i>,
    "<a href="#dhcpv4config" title="DhcpV4Config">DhcpV4Config</a>" : <i>[ <a href="dhcpv4configdefinition.md">DhcpV4ConfigDefinition</a>, ... ]</i>,
    "<a href="#dhcpv6config" title="DhcpV6Config">DhcpV6Config</a>" : <i>[ <a href="dhcpv6configdefinition.md">DhcpV6ConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cidr" title="Cidr">Cidr</a>: <i>String</i>
<a href="#dhcpranges" title="DhcpRanges">DhcpRanges</a>: <i>
      - String</i>
<a href="#dhcpv4config" title="DhcpV4Config">DhcpV4Config</a>: <i>
      - <a href="dhcpv4configdefinition.md">DhcpV4ConfigDefinition</a></i>
<a href="#dhcpv6config" title="DhcpV6Config">DhcpV6Config</a>: <i>
      - <a href="dhcpv6configdefinition.md">DhcpV6ConfigDefinition</a></i>
</pre>

## Properties

#### Cidr

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpRanges

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpV4Config

_Required_: No

_Type_: List of <a href="dhcpv4configdefinition.md">DhcpV4ConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpV6Config

_Required_: No

_Type_: List of <a href="dhcpv6configdefinition.md">DhcpV6ConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

