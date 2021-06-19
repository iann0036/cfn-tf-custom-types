# TF::Volterra::AwsTgwSite TgwSecurityDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#eastwestservicepolicyallowall" title="EastWestServicePolicyAllowAll">EastWestServicePolicyAllowAll</a>" : <i>Boolean</i>,
    "<a href="#forwardproxyallowall" title="ForwardProxyAllowAll">ForwardProxyAllowAll</a>" : <i>Boolean</i>,
    "<a href="#noeastwestpolicy" title="NoEastWestPolicy">NoEastWestPolicy</a>" : <i>Boolean</i>,
    "<a href="#noforwardproxy" title="NoForwardProxy">NoForwardProxy</a>" : <i>Boolean</i>,
    "<a href="#nonetworkpolicy" title="NoNetworkPolicy">NoNetworkPolicy</a>" : <i>Boolean</i>,
    "<a href="#activeeastwestservicepolicies" title="ActiveEastWestServicePolicies">ActiveEastWestServicePolicies</a>" : <i>[ <a href="activeeastwestservicepoliciesdefinition.md">ActiveEastWestServicePoliciesDefinition</a>, ... ]</i>,
    "<a href="#activeforwardproxypolicies" title="ActiveForwardProxyPolicies">ActiveForwardProxyPolicies</a>" : <i>[ <a href="activeforwardproxypoliciesdefinition.md">ActiveForwardProxyPoliciesDefinition</a>, ... ]</i>,
    "<a href="#activenetworkpolicies" title="ActiveNetworkPolicies">ActiveNetworkPolicies</a>" : <i>[ <a href="activenetworkpoliciesdefinition.md">ActiveNetworkPoliciesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#eastwestservicepolicyallowall" title="EastWestServicePolicyAllowAll">EastWestServicePolicyAllowAll</a>: <i>Boolean</i>
<a href="#forwardproxyallowall" title="ForwardProxyAllowAll">ForwardProxyAllowAll</a>: <i>Boolean</i>
<a href="#noeastwestpolicy" title="NoEastWestPolicy">NoEastWestPolicy</a>: <i>Boolean</i>
<a href="#noforwardproxy" title="NoForwardProxy">NoForwardProxy</a>: <i>Boolean</i>
<a href="#nonetworkpolicy" title="NoNetworkPolicy">NoNetworkPolicy</a>: <i>Boolean</i>
<a href="#activeeastwestservicepolicies" title="ActiveEastWestServicePolicies">ActiveEastWestServicePolicies</a>: <i>
      - <a href="activeeastwestservicepoliciesdefinition.md">ActiveEastWestServicePoliciesDefinition</a></i>
<a href="#activeforwardproxypolicies" title="ActiveForwardProxyPolicies">ActiveForwardProxyPolicies</a>: <i>
      - <a href="activeforwardproxypoliciesdefinition.md">ActiveForwardProxyPoliciesDefinition</a></i>
<a href="#activenetworkpolicies" title="ActiveNetworkPolicies">ActiveNetworkPolicies</a>: <i>
      - <a href="activenetworkpoliciesdefinition.md">ActiveNetworkPoliciesDefinition</a></i>
</pre>

## Properties

#### EastWestServicePolicyAllowAll

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyAllowAll

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoEastWestPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoForwardProxy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoNetworkPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveEastWestServicePolicies

_Required_: No

_Type_: List of <a href="activeeastwestservicepoliciesdefinition.md">ActiveEastWestServicePoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveForwardProxyPolicies

_Required_: No

_Type_: List of <a href="activeforwardproxypoliciesdefinition.md">ActiveForwardProxyPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveNetworkPolicies

_Required_: No

_Type_: List of <a href="activenetworkpoliciesdefinition.md">ActiveNetworkPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

