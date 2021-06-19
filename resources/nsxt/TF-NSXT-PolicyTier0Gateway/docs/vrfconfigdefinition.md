# TF::NSXT::PolicyTier0Gateway VrfConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#evpntransitvni" title="EvpnTransitVni">EvpnTransitVni</a>" : <i>Double</i>,
    "<a href="#gatewaypath" title="GatewayPath">GatewayPath</a>" : <i>String</i>,
    "<a href="#routedistinguisher" title="RouteDistinguisher">RouteDistinguisher</a>" : <i>String</i>,
    "<a href="#routetarget" title="RouteTarget">RouteTarget</a>" : <i>[ <a href="routetargetdefinition.md">RouteTargetDefinition</a>, ... ]</i>,
    "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#evpntransitvni" title="EvpnTransitVni">EvpnTransitVni</a>: <i>Double</i>
<a href="#gatewaypath" title="GatewayPath">GatewayPath</a>: <i>String</i>
<a href="#routedistinguisher" title="RouteDistinguisher">RouteDistinguisher</a>: <i>String</i>
<a href="#routetarget" title="RouteTarget">RouteTarget</a>: <i>
      - <a href="routetargetdefinition.md">RouteTargetDefinition</a></i>
<a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### EvpnTransitVni

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayPath

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteDistinguisher

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteTarget

_Required_: No

_Type_: List of <a href="routetargetdefinition.md">RouteTargetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

