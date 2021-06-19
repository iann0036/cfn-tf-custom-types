# TF::Volterra::GcpVpcSite IngressEgressGwDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#forwardproxyallowall" title="ForwardProxyAllowAll">ForwardProxyAllowAll</a>" : <i>Boolean</i>,
    "<a href="#gcpcertifiedhw" title="GcpCertifiedHw">GcpCertifiedHw</a>" : <i>String</i>,
    "<a href="#gcpzonenames" title="GcpZoneNames">GcpZoneNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#noforwardproxy" title="NoForwardProxy">NoForwardProxy</a>" : <i>Boolean</i>,
    "<a href="#noglobalnetwork" title="NoGlobalNetwork">NoGlobalNetwork</a>" : <i>Boolean</i>,
    "<a href="#noinsidestaticroutes" title="NoInsideStaticRoutes">NoInsideStaticRoutes</a>" : <i>Boolean</i>,
    "<a href="#nonetworkpolicy" title="NoNetworkPolicy">NoNetworkPolicy</a>" : <i>Boolean</i>,
    "<a href="#nooutsidestaticroutes" title="NoOutsideStaticRoutes">NoOutsideStaticRoutes</a>" : <i>Boolean</i>,
    "<a href="#nodenumber" title="NodeNumber">NodeNumber</a>" : <i>Double</i>,
    "<a href="#activeforwardproxypolicies" title="ActiveForwardProxyPolicies">ActiveForwardProxyPolicies</a>" : <i>[ <a href="activeforwardproxypoliciesdefinition.md">ActiveForwardProxyPoliciesDefinition</a>, ... ]</i>,
    "<a href="#activenetworkpolicies" title="ActiveNetworkPolicies">ActiveNetworkPolicies</a>" : <i>[ <a href="activenetworkpoliciesdefinition.md">ActiveNetworkPoliciesDefinition</a>, ... ]</i>,
    "<a href="#globalnetworklist" title="GlobalNetworkList">GlobalNetworkList</a>" : <i>[ <a href="globalnetworklistdefinition.md">GlobalNetworkListDefinition</a>, ... ]</i>,
    "<a href="#insidenetwork" title="InsideNetwork">InsideNetwork</a>" : <i>[ <a href="insidenetworkdefinition.md">InsideNetworkDefinition</a>, ... ]</i>,
    "<a href="#insidestaticroutes" title="InsideStaticRoutes">InsideStaticRoutes</a>" : <i>[ <a href="insidestaticroutesdefinition.md">InsideStaticRoutesDefinition</a>, ... ]</i>,
    "<a href="#insidesubnet" title="InsideSubnet">InsideSubnet</a>" : <i>[ <a href="insidesubnetdefinition.md">InsideSubnetDefinition</a>, ... ]</i>,
    "<a href="#outsidenetwork" title="OutsideNetwork">OutsideNetwork</a>" : <i>[ <a href="outsidenetworkdefinition.md">OutsideNetworkDefinition</a>, ... ]</i>,
    "<a href="#outsidestaticroutes" title="OutsideStaticRoutes">OutsideStaticRoutes</a>" : <i>[ <a href="outsidestaticroutesdefinition.md">OutsideStaticRoutesDefinition</a>, ... ]</i>,
    "<a href="#outsidesubnet" title="OutsideSubnet">OutsideSubnet</a>" : <i>[ <a href="outsidesubnetdefinition.md">OutsideSubnetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#forwardproxyallowall" title="ForwardProxyAllowAll">ForwardProxyAllowAll</a>: <i>Boolean</i>
<a href="#gcpcertifiedhw" title="GcpCertifiedHw">GcpCertifiedHw</a>: <i>String</i>
<a href="#gcpzonenames" title="GcpZoneNames">GcpZoneNames</a>: <i>
      - String</i>
<a href="#noforwardproxy" title="NoForwardProxy">NoForwardProxy</a>: <i>Boolean</i>
<a href="#noglobalnetwork" title="NoGlobalNetwork">NoGlobalNetwork</a>: <i>Boolean</i>
<a href="#noinsidestaticroutes" title="NoInsideStaticRoutes">NoInsideStaticRoutes</a>: <i>Boolean</i>
<a href="#nonetworkpolicy" title="NoNetworkPolicy">NoNetworkPolicy</a>: <i>Boolean</i>
<a href="#nooutsidestaticroutes" title="NoOutsideStaticRoutes">NoOutsideStaticRoutes</a>: <i>Boolean</i>
<a href="#nodenumber" title="NodeNumber">NodeNumber</a>: <i>Double</i>
<a href="#activeforwardproxypolicies" title="ActiveForwardProxyPolicies">ActiveForwardProxyPolicies</a>: <i>
      - <a href="activeforwardproxypoliciesdefinition.md">ActiveForwardProxyPoliciesDefinition</a></i>
<a href="#activenetworkpolicies" title="ActiveNetworkPolicies">ActiveNetworkPolicies</a>: <i>
      - <a href="activenetworkpoliciesdefinition.md">ActiveNetworkPoliciesDefinition</a></i>
<a href="#globalnetworklist" title="GlobalNetworkList">GlobalNetworkList</a>: <i>
      - <a href="globalnetworklistdefinition.md">GlobalNetworkListDefinition</a></i>
<a href="#insidenetwork" title="InsideNetwork">InsideNetwork</a>: <i>
      - <a href="insidenetworkdefinition.md">InsideNetworkDefinition</a></i>
<a href="#insidestaticroutes" title="InsideStaticRoutes">InsideStaticRoutes</a>: <i>
      - <a href="insidestaticroutesdefinition.md">InsideStaticRoutesDefinition</a></i>
<a href="#insidesubnet" title="InsideSubnet">InsideSubnet</a>: <i>
      - <a href="insidesubnetdefinition.md">InsideSubnetDefinition</a></i>
<a href="#outsidenetwork" title="OutsideNetwork">OutsideNetwork</a>: <i>
      - <a href="outsidenetworkdefinition.md">OutsideNetworkDefinition</a></i>
<a href="#outsidestaticroutes" title="OutsideStaticRoutes">OutsideStaticRoutes</a>: <i>
      - <a href="outsidestaticroutesdefinition.md">OutsideStaticRoutesDefinition</a></i>
<a href="#outsidesubnet" title="OutsideSubnet">OutsideSubnet</a>: <i>
      - <a href="outsidesubnetdefinition.md">OutsideSubnetDefinition</a></i>
</pre>

## Properties

#### ForwardProxyAllowAll

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpCertifiedHw

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpZoneNames

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoForwardProxy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoGlobalNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoInsideStaticRoutes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoNetworkPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoOutsideStaticRoutes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveForwardProxyPolicies

_Required_: No

_Type_: List of <a href="activeforwardproxypoliciesdefinition.md">ActiveForwardProxyPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveNetworkPolicies

_Required_: No

_Type_: List of <a href="activenetworkpoliciesdefinition.md">ActiveNetworkPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalNetworkList

_Required_: No

_Type_: List of <a href="globalnetworklistdefinition.md">GlobalNetworkListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsideNetwork

_Required_: No

_Type_: List of <a href="insidenetworkdefinition.md">InsideNetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsideStaticRoutes

_Required_: No

_Type_: List of <a href="insidestaticroutesdefinition.md">InsideStaticRoutesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsideSubnet

_Required_: No

_Type_: List of <a href="insidesubnetdefinition.md">InsideSubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideNetwork

_Required_: No

_Type_: List of <a href="outsidenetworkdefinition.md">OutsideNetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideStaticRoutes

_Required_: No

_Type_: List of <a href="outsidestaticroutesdefinition.md">OutsideStaticRoutesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideSubnet

_Required_: No

_Type_: List of <a href="outsidesubnetdefinition.md">OutsideSubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

