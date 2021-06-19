# TF::Volterra::HttpLoadbalancer RoutesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customrouteobject" title="CustomRouteObject">CustomRouteObject</a>" : <i>[ <a href="customrouteobjectdefinition.md">CustomRouteObjectDefinition</a>, ... ]</i>,
    "<a href="#directresponseroute" title="DirectResponseRoute">DirectResponseRoute</a>" : <i>[ <a href="directresponseroutedefinition.md">DirectResponseRouteDefinition</a>, ... ]</i>,
    "<a href="#redirectroute" title="RedirectRoute">RedirectRoute</a>" : <i>[ <a href="redirectroutedefinition.md">RedirectRouteDefinition</a>, ... ]</i>,
    "<a href="#simpleroute" title="SimpleRoute">SimpleRoute</a>" : <i>[ <a href="simpleroutedefinition.md">SimpleRouteDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#customrouteobject" title="CustomRouteObject">CustomRouteObject</a>: <i>
      - <a href="customrouteobjectdefinition.md">CustomRouteObjectDefinition</a></i>
<a href="#directresponseroute" title="DirectResponseRoute">DirectResponseRoute</a>: <i>
      - <a href="directresponseroutedefinition.md">DirectResponseRouteDefinition</a></i>
<a href="#redirectroute" title="RedirectRoute">RedirectRoute</a>: <i>
      - <a href="redirectroutedefinition.md">RedirectRouteDefinition</a></i>
<a href="#simpleroute" title="SimpleRoute">SimpleRoute</a>: <i>
      - <a href="simpleroutedefinition.md">SimpleRouteDefinition</a></i>
</pre>

## Properties

#### CustomRouteObject

_Required_: No

_Type_: List of <a href="customrouteobjectdefinition.md">CustomRouteObjectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectResponseRoute

_Required_: No

_Type_: List of <a href="directresponseroutedefinition.md">DirectResponseRouteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectRoute

_Required_: No

_Type_: List of <a href="redirectroutedefinition.md">RedirectRouteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SimpleRoute

_Required_: No

_Type_: List of <a href="simpleroutedefinition.md">SimpleRouteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

