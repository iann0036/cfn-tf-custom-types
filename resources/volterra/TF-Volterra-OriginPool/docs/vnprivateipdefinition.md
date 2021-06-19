# TF::Volterra::OriginPool VnPrivateIpDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
    "<a href="#virtualnetwork" title="VirtualNetwork">VirtualNetwork</a>" : <i>[ <a href="virtualnetworkdefinition.md">VirtualNetworkDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ip" title="Ip">Ip</a>: <i>String</i>
<a href="#virtualnetwork" title="VirtualNetwork">VirtualNetwork</a>: <i>
      - <a href="virtualnetworkdefinition.md">VirtualNetworkDefinition</a></i>
</pre>

## Properties

#### Ip

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetwork

_Required_: No

_Type_: List of <a href="virtualnetworkdefinition.md">VirtualNetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

