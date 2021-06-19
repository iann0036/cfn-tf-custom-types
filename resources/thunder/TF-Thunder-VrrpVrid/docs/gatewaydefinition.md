# TF::Thunder::VrrpVrid GatewayDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipv4gatewaylist" title="Ipv4GatewayList">Ipv4GatewayList</a>" : <i>[ <a href="ipv4gatewaylistdefinition.md">Ipv4GatewayListDefinition</a>, ... ]</i>,
    "<a href="#ipv6gatewaylist" title="Ipv6GatewayList">Ipv6GatewayList</a>" : <i>[ <a href="ipv6gatewaylistdefinition.md">Ipv6GatewayListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipv4gatewaylist" title="Ipv4GatewayList">Ipv4GatewayList</a>: <i>
      - <a href="ipv4gatewaylistdefinition.md">Ipv4GatewayListDefinition</a></i>
<a href="#ipv6gatewaylist" title="Ipv6GatewayList">Ipv6GatewayList</a>: <i>
      - <a href="ipv6gatewaylistdefinition.md">Ipv6GatewayListDefinition</a></i>
</pre>

## Properties

#### Ipv4GatewayList

_Required_: No

_Type_: List of <a href="ipv4gatewaylistdefinition.md">Ipv4GatewayListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6GatewayList

_Required_: No

_Type_: List of <a href="ipv6gatewaylistdefinition.md">Ipv6GatewayListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

