# TF::AVI::L4policyset MatchDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clientip" title="ClientIp">ClientIp</a>" : <i>[ <a href="clientipdefinition.md">ClientIpDefinition</a>, ... ]</i>,
    "<a href="#port" title="Port">Port</a>" : <i>[ <a href="portdefinition.md">PortDefinition</a>, ... ]</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>[ <a href="protocoldefinition.md">ProtocolDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clientip" title="ClientIp">ClientIp</a>: <i>
      - <a href="clientipdefinition.md">ClientIpDefinition</a></i>
<a href="#port" title="Port">Port</a>: <i>
      - <a href="portdefinition.md">PortDefinition</a></i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>
      - <a href="protocoldefinition.md">ProtocolDefinition</a></i>
</pre>

## Properties

#### ClientIp

_Required_: No

_Type_: List of <a href="clientipdefinition.md">ClientIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: List of <a href="portdefinition.md">PortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: List of <a href="protocoldefinition.md">ProtocolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

