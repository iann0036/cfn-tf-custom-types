# TF::Thunder::VrrpVrid RouteDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipdestinationcfg" title="IpDestinationCfg">IpDestinationCfg</a>" : <i>[ <a href="ipdestinationcfgdefinition.md">IpDestinationCfgDefinition</a>, ... ]</i>,
    "<a href="#ipv6destinationcfg" title="Ipv6DestinationCfg">Ipv6DestinationCfg</a>" : <i>[ <a href="ipv6destinationcfgdefinition.md">Ipv6DestinationCfgDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipdestinationcfg" title="IpDestinationCfg">IpDestinationCfg</a>: <i>
      - <a href="ipdestinationcfgdefinition.md">IpDestinationCfgDefinition</a></i>
<a href="#ipv6destinationcfg" title="Ipv6DestinationCfg">Ipv6DestinationCfg</a>: <i>
      - <a href="ipv6destinationcfgdefinition.md">Ipv6DestinationCfgDefinition</a></i>
</pre>

## Properties

#### IpDestinationCfg

_Required_: No

_Type_: List of <a href="ipdestinationcfgdefinition.md">IpDestinationCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6DestinationCfg

_Required_: No

_Type_: List of <a href="ipv6destinationcfgdefinition.md">Ipv6DestinationCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

