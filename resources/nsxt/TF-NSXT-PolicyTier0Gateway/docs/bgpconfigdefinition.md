# TF::NSXT::PolicyTier0Gateway BgpConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ecmp" title="Ecmp">Ecmp</a>" : <i>Boolean</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#gracefulrestartmode" title="GracefulRestartMode">GracefulRestartMode</a>" : <i>String</i>,
    "<a href="#gracefulrestartstaleroutetimer" title="GracefulRestartStaleRouteTimer">GracefulRestartStaleRouteTimer</a>" : <i>Double</i>,
    "<a href="#gracefulrestarttimer" title="GracefulRestartTimer">GracefulRestartTimer</a>" : <i>Double</i>,
    "<a href="#intersribgp" title="InterSrIbgp">InterSrIbgp</a>" : <i>Boolean</i>,
    "<a href="#localasnum" title="LocalAsNum">LocalAsNum</a>" : <i>String</i>,
    "<a href="#multipathrelax" title="MultipathRelax">MultipathRelax</a>" : <i>Boolean</i>,
    "<a href="#routeaggregation" title="RouteAggregation">RouteAggregation</a>" : <i>[ <a href="routeaggregationdefinition.md">RouteAggregationDefinition</a>, ... ]</i>,
    "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ecmp" title="Ecmp">Ecmp</a>: <i>Boolean</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#gracefulrestartmode" title="GracefulRestartMode">GracefulRestartMode</a>: <i>String</i>
<a href="#gracefulrestartstaleroutetimer" title="GracefulRestartStaleRouteTimer">GracefulRestartStaleRouteTimer</a>: <i>Double</i>
<a href="#gracefulrestarttimer" title="GracefulRestartTimer">GracefulRestartTimer</a>: <i>Double</i>
<a href="#intersribgp" title="InterSrIbgp">InterSrIbgp</a>: <i>Boolean</i>
<a href="#localasnum" title="LocalAsNum">LocalAsNum</a>: <i>String</i>
<a href="#multipathrelax" title="MultipathRelax">MultipathRelax</a>: <i>Boolean</i>
<a href="#routeaggregation" title="RouteAggregation">RouteAggregation</a>: <i>
      - <a href="routeaggregationdefinition.md">RouteAggregationDefinition</a></i>
<a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### Ecmp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulRestartMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulRestartStaleRouteTimer

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulRestartTimer

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterSrIbgp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAsNum

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultipathRelax

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteAggregation

_Required_: No

_Type_: List of <a href="routeaggregationdefinition.md">RouteAggregationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

