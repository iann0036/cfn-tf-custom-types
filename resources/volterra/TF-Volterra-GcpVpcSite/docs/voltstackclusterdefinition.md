# TF::Volterra::GcpVpcSite VoltstackClusterDefinition

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
    "<a href="#nok8scluster" title="NoK8sCluster">NoK8sCluster</a>" : <i>Boolean</i>,
    "<a href="#nonetworkpolicy" title="NoNetworkPolicy">NoNetworkPolicy</a>" : <i>Boolean</i>,
    "<a href="#nooutsidestaticroutes" title="NoOutsideStaticRoutes">NoOutsideStaticRoutes</a>" : <i>Boolean</i>,
    "<a href="#nodenumber" title="NodeNumber">NodeNumber</a>" : <i>Double</i>,
    "<a href="#activeforwardproxypolicies" title="ActiveForwardProxyPolicies">ActiveForwardProxyPolicies</a>" : <i>[ <a href="activeforwardproxypoliciesdefinition.md">ActiveForwardProxyPoliciesDefinition</a>, ... ]</i>,
    "<a href="#activenetworkpolicies" title="ActiveNetworkPolicies">ActiveNetworkPolicies</a>" : <i>[ <a href="activenetworkpoliciesdefinition.md">ActiveNetworkPoliciesDefinition</a>, ... ]</i>,
    "<a href="#globalnetworklist" title="GlobalNetworkList">GlobalNetworkList</a>" : <i>[ <a href="globalnetworklistdefinition.md">GlobalNetworkListDefinition</a>, ... ]</i>,
    "<a href="#k8scluster" title="K8sCluster">K8sCluster</a>" : <i>[ <a href="k8sclusterdefinition.md">K8sClusterDefinition</a>, ... ]</i>,
    "<a href="#outsidestaticroutes" title="OutsideStaticRoutes">OutsideStaticRoutes</a>" : <i>[ <a href="outsidestaticroutesdefinition.md">OutsideStaticRoutesDefinition</a>, ... ]</i>,
    "<a href="#sitelocalnetwork" title="SiteLocalNetwork">SiteLocalNetwork</a>" : <i>[ <a href="sitelocalnetworkdefinition.md">SiteLocalNetworkDefinition</a>, ... ]</i>,
    "<a href="#sitelocalsubnet" title="SiteLocalSubnet">SiteLocalSubnet</a>" : <i>[ <a href="sitelocalsubnetdefinition.md">SiteLocalSubnetDefinition</a>, ... ]</i>
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
<a href="#nok8scluster" title="NoK8sCluster">NoK8sCluster</a>: <i>Boolean</i>
<a href="#nonetworkpolicy" title="NoNetworkPolicy">NoNetworkPolicy</a>: <i>Boolean</i>
<a href="#nooutsidestaticroutes" title="NoOutsideStaticRoutes">NoOutsideStaticRoutes</a>: <i>Boolean</i>
<a href="#nodenumber" title="NodeNumber">NodeNumber</a>: <i>Double</i>
<a href="#activeforwardproxypolicies" title="ActiveForwardProxyPolicies">ActiveForwardProxyPolicies</a>: <i>
      - <a href="activeforwardproxypoliciesdefinition.md">ActiveForwardProxyPoliciesDefinition</a></i>
<a href="#activenetworkpolicies" title="ActiveNetworkPolicies">ActiveNetworkPolicies</a>: <i>
      - <a href="activenetworkpoliciesdefinition.md">ActiveNetworkPoliciesDefinition</a></i>
<a href="#globalnetworklist" title="GlobalNetworkList">GlobalNetworkList</a>: <i>
      - <a href="globalnetworklistdefinition.md">GlobalNetworkListDefinition</a></i>
<a href="#k8scluster" title="K8sCluster">K8sCluster</a>: <i>
      - <a href="k8sclusterdefinition.md">K8sClusterDefinition</a></i>
<a href="#outsidestaticroutes" title="OutsideStaticRoutes">OutsideStaticRoutes</a>: <i>
      - <a href="outsidestaticroutesdefinition.md">OutsideStaticRoutesDefinition</a></i>
<a href="#sitelocalnetwork" title="SiteLocalNetwork">SiteLocalNetwork</a>: <i>
      - <a href="sitelocalnetworkdefinition.md">SiteLocalNetworkDefinition</a></i>
<a href="#sitelocalsubnet" title="SiteLocalSubnet">SiteLocalSubnet</a>: <i>
      - <a href="sitelocalsubnetdefinition.md">SiteLocalSubnetDefinition</a></i>
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

#### NoK8sCluster

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

#### K8sCluster

_Required_: No

_Type_: List of <a href="k8sclusterdefinition.md">K8sClusterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideStaticRoutes

_Required_: No

_Type_: List of <a href="outsidestaticroutesdefinition.md">OutsideStaticRoutesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteLocalNetwork

_Required_: No

_Type_: List of <a href="sitelocalnetworkdefinition.md">SiteLocalNetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteLocalSubnet

_Required_: No

_Type_: List of <a href="sitelocalsubnetdefinition.md">SiteLocalSubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

