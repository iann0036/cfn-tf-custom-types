# TF::Thunder::VrrpVrid IpDestinationCfgDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#distance" title="Distance">Distance</a>" : <i>Double</i>,
    "<a href="#gateway" title="Gateway">Gateway</a>" : <i>[ <a href="gatewaydefinition.md">GatewayDefinition</a>, ... ]</i>,
    "<a href="#ipdestination" title="IpDestination">IpDestination</a>" : <i>String</i>,
    "<a href="#mask" title="Mask">Mask</a>" : <i>String</i>,
    "<a href="#prioritycost" title="PriorityCost">PriorityCost</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#distance" title="Distance">Distance</a>: <i>Double</i>
<a href="#gateway" title="Gateway">Gateway</a>: <i>
      - <a href="gatewaydefinition.md">GatewayDefinition</a></i>
<a href="#ipdestination" title="IpDestination">IpDestination</a>: <i>String</i>
<a href="#mask" title="Mask">Mask</a>: <i>String</i>
<a href="#prioritycost" title="PriorityCost">PriorityCost</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
</pre>

## Properties

#### Distance

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

_Required_: No

_Type_: List of <a href="gatewaydefinition.md">GatewayDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpDestination

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mask

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PriorityCost

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

