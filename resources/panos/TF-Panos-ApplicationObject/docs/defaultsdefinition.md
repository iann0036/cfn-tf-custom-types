# TF::Panos::ApplicationObject DefaultsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#icmp" title="Icmp">Icmp</a>" : <i>[ <a href="icmpdefinition.md">IcmpDefinition</a>, ... ]</i>,
    "<a href="#icmp6" title="Icmp6">Icmp6</a>" : <i>[ <a href="icmp6definition.md">Icmp6Definition</a>, ... ]</i>,
    "<a href="#ipprotocol" title="IpProtocol">IpProtocol</a>" : <i>[ <a href="ipprotocoldefinition.md">IpProtocolDefinition</a>, ... ]</i>,
    "<a href="#port" title="Port">Port</a>" : <i>[ <a href="portdefinition.md">PortDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#icmp" title="Icmp">Icmp</a>: <i>
      - <a href="icmpdefinition.md">IcmpDefinition</a></i>
<a href="#icmp6" title="Icmp6">Icmp6</a>: <i>
      - <a href="icmp6definition.md">Icmp6Definition</a></i>
<a href="#ipprotocol" title="IpProtocol">IpProtocol</a>: <i>
      - <a href="ipprotocoldefinition.md">IpProtocolDefinition</a></i>
<a href="#port" title="Port">Port</a>: <i>
      - <a href="portdefinition.md">PortDefinition</a></i>
</pre>

## Properties

#### Icmp

_Required_: No

_Type_: List of <a href="icmpdefinition.md">IcmpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icmp6

_Required_: No

_Type_: List of <a href="icmp6definition.md">Icmp6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpProtocol

_Required_: No

_Type_: List of <a href="ipprotocoldefinition.md">IpProtocolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: List of <a href="portdefinition.md">PortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

