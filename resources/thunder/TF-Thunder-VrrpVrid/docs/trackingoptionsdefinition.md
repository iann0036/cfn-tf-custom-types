# TF::Thunder::VrrpVrid TrackingOptionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#bgp" title="Bgp">Bgp</a>" : <i>[ <a href="bgpdefinition.md">BgpDefinition</a>, ... ]</i>,
    "<a href="#gateway" title="Gateway">Gateway</a>" : <i>[ <a href="gatewaydefinition.md">GatewayDefinition</a>, ... ]</i>,
    "<a href="#interface" title="Interface">Interface</a>" : <i>[ <a href="interfacedefinition.md">InterfaceDefinition</a>, ... ]</i>,
    "<a href="#route" title="Route">Route</a>" : <i>[ <a href="routedefinition.md">RouteDefinition</a>, ... ]</i>,
    "<a href="#trunkcfg" title="TrunkCfg">TrunkCfg</a>" : <i>[ <a href="trunkcfgdefinition.md">TrunkCfgDefinition</a>, ... ]</i>,
    "<a href="#vlancfg" title="VlanCfg">VlanCfg</a>" : <i>[ <a href="vlancfgdefinition.md">VlanCfgDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#bgp" title="Bgp">Bgp</a>: <i>
      - <a href="bgpdefinition.md">BgpDefinition</a></i>
<a href="#gateway" title="Gateway">Gateway</a>: <i>
      - <a href="gatewaydefinition.md">GatewayDefinition</a></i>
<a href="#interface" title="Interface">Interface</a>: <i>
      - <a href="interfacedefinition.md">InterfaceDefinition</a></i>
<a href="#route" title="Route">Route</a>: <i>
      - <a href="routedefinition.md">RouteDefinition</a></i>
<a href="#trunkcfg" title="TrunkCfg">TrunkCfg</a>: <i>
      - <a href="trunkcfgdefinition.md">TrunkCfgDefinition</a></i>
<a href="#vlancfg" title="VlanCfg">VlanCfg</a>: <i>
      - <a href="vlancfgdefinition.md">VlanCfgDefinition</a></i>
</pre>

## Properties

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bgp

_Required_: No

_Type_: List of <a href="bgpdefinition.md">BgpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

_Required_: No

_Type_: List of <a href="gatewaydefinition.md">GatewayDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

_Required_: No

_Type_: List of <a href="interfacedefinition.md">InterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Route

_Required_: No

_Type_: List of <a href="routedefinition.md">RouteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrunkCfg

_Required_: No

_Type_: List of <a href="trunkcfgdefinition.md">TrunkCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanCfg

_Required_: No

_Type_: List of <a href="vlancfgdefinition.md">VlanCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

