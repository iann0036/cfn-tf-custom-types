# TF::Vultr::LoadBalancer

Get information about a Vultr load balancer.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Vultr::LoadBalancer",
    "Properties" : {
        "<a href="#attachedinstances" title="AttachedInstances">AttachedInstances</a>" : <i>[ String, ... ]</i>,
        "<a href="#balancingalgorithm" title="BalancingAlgorithm">BalancingAlgorithm</a>" : <i>String</i>,
        "<a href="#cookiename" title="CookieName">CookieName</a>" : <i>String</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#privatenetwork" title="PrivateNetwork">PrivateNetwork</a>" : <i>String</i>,
        "<a href="#proxyprotocol" title="ProxyProtocol">ProxyProtocol</a>" : <i>Boolean</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#sslredirect" title="SslRedirect">SslRedirect</a>" : <i>Boolean</i>,
        "<a href="#firewallrules" title="FirewallRules">FirewallRules</a>" : <i>[ <a href="firewallrulesdefinition.md">FirewallRulesDefinition</a>, ... ]</i>,
        "<a href="#forwardingrules" title="ForwardingRules">ForwardingRules</a>" : <i>[ <a href="forwardingrulesdefinition.md">ForwardingRulesDefinition</a>, ... ]</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>[ <a href="healthcheckdefinition.md">HealthCheckDefinition</a>, ... ]</i>,
        "<a href="#ssl" title="Ssl">Ssl</a>" : <i>[ <a href="ssldefinition.md">SslDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Vultr::LoadBalancer
Properties:
    <a href="#attachedinstances" title="AttachedInstances">AttachedInstances</a>: <i>
      - String</i>
    <a href="#balancingalgorithm" title="BalancingAlgorithm">BalancingAlgorithm</a>: <i>String</i>
    <a href="#cookiename" title="CookieName">CookieName</a>: <i>String</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#privatenetwork" title="PrivateNetwork">PrivateNetwork</a>: <i>String</i>
    <a href="#proxyprotocol" title="ProxyProtocol">ProxyProtocol</a>: <i>Boolean</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#sslredirect" title="SslRedirect">SslRedirect</a>: <i>Boolean</i>
    <a href="#firewallrules" title="FirewallRules">FirewallRules</a>: <i>
      - <a href="firewallrulesdefinition.md">FirewallRulesDefinition</a></i>
    <a href="#forwardingrules" title="ForwardingRules">ForwardingRules</a>: <i>
      - <a href="forwardingrulesdefinition.md">ForwardingRulesDefinition</a></i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>
      - <a href="healthcheckdefinition.md">HealthCheckDefinition</a></i>
    <a href="#ssl" title="Ssl">Ssl</a>: <i>
      - <a href="ssldefinition.md">SslDefinition</a></i>
</pre>

## Properties

#### AttachedInstances

Array of instances that are currently attached to the load balancer.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BalancingAlgorithm

The balancing algorithm for your load balancer. Options are `roundrobin` or `leastconn`. Default value is `roundrobin`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieName

Name for your given sticky session.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

The load balancer's label.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateNetwork

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyProtocol

Boolean value that indicates if Proxy Protocol is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region your load balancer is deployed in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslRedirect

Boolean value that indicates if HTTP calls will be redirected to HTTPS.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallRules

_Required_: No

_Type_: List of <a href="firewallrulesdefinition.md">FirewallRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardingRules

_Required_: No

_Type_: List of <a href="forwardingrulesdefinition.md">ForwardingRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

_Required_: No

_Type_: List of <a href="healthcheckdefinition.md">HealthCheckDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ssl

_Required_: No

_Type_: List of <a href="ssldefinition.md">SslDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### HasSsl

Returns the <code>HasSsl</code> value.

#### Id

Returns the <code>Id</code> value.

#### Ipv4

Returns the <code>Ipv4</code> value.

#### Ipv6

Returns the <code>Ipv6</code> value.

#### Status

Returns the <code>Status</code> value.

