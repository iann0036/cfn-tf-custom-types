# TF::Volterra::AwsTgwSite VnConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#noglobalnetwork" title="NoGlobalNetwork">NoGlobalNetwork</a>" : <i>Boolean</i>,
    "<a href="#noinsidestaticroutes" title="NoInsideStaticRoutes">NoInsideStaticRoutes</a>" : <i>Boolean</i>,
    "<a href="#nooutsidestaticroutes" title="NoOutsideStaticRoutes">NoOutsideStaticRoutes</a>" : <i>Boolean</i>,
    "<a href="#allowedvipport" title="AllowedVipPort">AllowedVipPort</a>" : <i>[ <a href="allowedvipportdefinition.md">AllowedVipPortDefinition</a>, ... ]</i>,
    "<a href="#globalnetworklist" title="GlobalNetworkList">GlobalNetworkList</a>" : <i>[ <a href="globalnetworklistdefinition.md">GlobalNetworkListDefinition</a>, ... ]</i>,
    "<a href="#insidestaticroutes" title="InsideStaticRoutes">InsideStaticRoutes</a>" : <i>[ <a href="insidestaticroutesdefinition.md">InsideStaticRoutesDefinition</a>, ... ]</i>,
    "<a href="#outsidestaticroutes" title="OutsideStaticRoutes">OutsideStaticRoutes</a>" : <i>[ <a href="outsidestaticroutesdefinition.md">OutsideStaticRoutesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#noglobalnetwork" title="NoGlobalNetwork">NoGlobalNetwork</a>: <i>Boolean</i>
<a href="#noinsidestaticroutes" title="NoInsideStaticRoutes">NoInsideStaticRoutes</a>: <i>Boolean</i>
<a href="#nooutsidestaticroutes" title="NoOutsideStaticRoutes">NoOutsideStaticRoutes</a>: <i>Boolean</i>
<a href="#allowedvipport" title="AllowedVipPort">AllowedVipPort</a>: <i>
      - <a href="allowedvipportdefinition.md">AllowedVipPortDefinition</a></i>
<a href="#globalnetworklist" title="GlobalNetworkList">GlobalNetworkList</a>: <i>
      - <a href="globalnetworklistdefinition.md">GlobalNetworkListDefinition</a></i>
<a href="#insidestaticroutes" title="InsideStaticRoutes">InsideStaticRoutes</a>: <i>
      - <a href="insidestaticroutesdefinition.md">InsideStaticRoutesDefinition</a></i>
<a href="#outsidestaticroutes" title="OutsideStaticRoutes">OutsideStaticRoutes</a>: <i>
      - <a href="outsidestaticroutesdefinition.md">OutsideStaticRoutesDefinition</a></i>
</pre>

## Properties

#### NoGlobalNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoInsideStaticRoutes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoOutsideStaticRoutes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedVipPort

_Required_: No

_Type_: List of <a href="allowedvipportdefinition.md">AllowedVipPortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalNetworkList

_Required_: No

_Type_: List of <a href="globalnetworklistdefinition.md">GlobalNetworkListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsideStaticRoutes

_Required_: No

_Type_: List of <a href="insidestaticroutesdefinition.md">InsideStaticRoutesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideStaticRoutes

_Required_: No

_Type_: List of <a href="outsidestaticroutesdefinition.md">OutsideStaticRoutesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

