# TF::NSXT::PolicyBgpConfig

This resource provides a method for the management of BGP for T0 Gateway on specific site. A single resource should be specified per T0 Gateway + Site.

~> **NOTE:** This resource should NOT be used together with `bgp_config` clause in gateway resource configuration - such usage may produce inconsistent experience. Please choose one way or the other to configure BGP.

~> **NOTE:** Since BGP config is auto-created on NSX, this resource will update NSX object, but never create or delete it.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicyBgpConfig",
    "Properties" : {
        "<a href="#ecmp" title="Ecmp">Ecmp</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#gatewaypath" title="GatewayPath">GatewayPath</a>" : <i>String</i>,
        "<a href="#gracefulrestartmode" title="GracefulRestartMode">GracefulRestartMode</a>" : <i>String</i>,
        "<a href="#gracefulrestartstaleroutetimer" title="GracefulRestartStaleRouteTimer">GracefulRestartStaleRouteTimer</a>" : <i>Double</i>,
        "<a href="#gracefulrestarttimer" title="GracefulRestartTimer">GracefulRestartTimer</a>" : <i>Double</i>,
        "<a href="#intersribgp" title="InterSrIbgp">InterSrIbgp</a>" : <i>Boolean</i>,
        "<a href="#localasnum" title="LocalAsNum">LocalAsNum</a>" : <i>String</i>,
        "<a href="#multipathrelax" title="MultipathRelax">MultipathRelax</a>" : <i>Boolean</i>,
        "<a href="#sitepath" title="SitePath">SitePath</a>" : <i>String</i>,
        "<a href="#routeaggregation" title="RouteAggregation">RouteAggregation</a>" : <i>[ <a href="routeaggregationdefinition.md">RouteAggregationDefinition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicyBgpConfig
Properties:
    <a href="#ecmp" title="Ecmp">Ecmp</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#gatewaypath" title="GatewayPath">GatewayPath</a>: <i>String</i>
    <a href="#gracefulrestartmode" title="GracefulRestartMode">GracefulRestartMode</a>: <i>String</i>
    <a href="#gracefulrestartstaleroutetimer" title="GracefulRestartStaleRouteTimer">GracefulRestartStaleRouteTimer</a>: <i>Double</i>
    <a href="#gracefulrestarttimer" title="GracefulRestartTimer">GracefulRestartTimer</a>: <i>Double</i>
    <a href="#intersribgp" title="InterSrIbgp">InterSrIbgp</a>: <i>Boolean</i>
    <a href="#localasnum" title="LocalAsNum">LocalAsNum</a>: <i>String</i>
    <a href="#multipathrelax" title="MultipathRelax">MultipathRelax</a>: <i>Boolean</i>
    <a href="#sitepath" title="SitePath">SitePath</a>: <i>String</i>
    <a href="#routeaggregation" title="RouteAggregation">RouteAggregation</a>: <i>
      - <a href="routeaggregationdefinition.md">RouteAggregationDefinition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### Ecmp

A boolean flag to enable/disable ECMP. Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

A boolean flag to enable/disable BGP. Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayPath

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulRestartMode

Setting to control BGP graceful restart mode, one of `DISABLE`, `GR_AND_HELPER`, `HELPER_ONLY`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulRestartStaleRouteTimer

BGP stale route timer. Default is `600`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulRestartTimer

BGP graceful restart timer. Default is `180`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterSrIbgp

A boolean flag to enable/disable inter SR IBGP configuration. Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAsNum

BGP AS number in ASPLAIN/ASDOT Format. This attribute is required for non-VRF configurations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultipathRelax

A boolean flag to enable/disable multipath relax for BGP. Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SitePath

Path for policy site. This attribute is required for Global Manager and is not relevant for Local Manager.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteAggregation

_Required_: No

_Type_: List of <a href="routeaggregationdefinition.md">RouteAggregationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### GatewayId

Returns the <code>GatewayId</code> value.

#### Id

Returns the <code>Id</code> value.

#### LocaleServiceId

Returns the <code>LocaleServiceId</code> value.

#### Path

Returns the <code>Path</code> value.

#### Revision

Returns the <code>Revision</code> value.

