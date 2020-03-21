# Terraform::OCI::LoadBalancerListener

This resource provides the Listener resource in Oracle Cloud Infrastructure Load Balancer service.

Adds a listener to a load balancer.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::LoadBalancerListener",
    "Properties" : {
        "<a href="#defaultbackendsetname" title="DefaultBackendSetName">DefaultBackendSetName</a>" : <i>String</i>,
        "<a href="#hostnamenames" title="HostnameNames">HostnameNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pathroutesetname" title="PathRouteSetName">PathRouteSetName</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#rulesetnames" title="RuleSetNames">RuleSetNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#connectionconfiguration" title="ConnectionConfiguration">ConnectionConfiguration</a>" : <i>[ <a href="connectionconfiguration.md">ConnectionConfiguration</a>, ... ]</i>,
        "<a href="#sslconfiguration" title="SslConfiguration">SslConfiguration</a>" : <i>[ <a href="sslconfiguration.md">SslConfiguration</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::LoadBalancerListener
Properties:
    <a href="#defaultbackendsetname" title="DefaultBackendSetName">DefaultBackendSetName</a>: <i>String</i>
    <a href="#hostnamenames" title="HostnameNames">HostnameNames</a>: <i>
      - String</i>
    <a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pathroutesetname" title="PathRouteSetName">PathRouteSetName</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#rulesetnames" title="RuleSetNames">RuleSetNames</a>: <i>
      - String</i>
    <a href="#connectionconfiguration" title="ConnectionConfiguration">ConnectionConfiguration</a>: <i>
      - <a href="connectionconfiguration.md">ConnectionConfiguration</a></i>
    <a href="#sslconfiguration" title="SslConfiguration">SslConfiguration</a>: <i>
      - <a href="sslconfiguration.md">SslConfiguration</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### DefaultBackendSetName

(Updatable) The name of the associated backend set.  Example: `example_backend_set`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostnameNames

(Updatable) An array of hostname resource names.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the load balancer on which to add a listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A friendly name for the listener. It must be unique and it cannot be changed. Avoid entering confidential information.  Example: `example_listener`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathRouteSetName

(Updatable) The name of the set of path-based routing rules, [PathRouteSet](https://docs.cloud.oracle.com/iaas/api/#/en/loadbalancer/20170115/PathRouteSet/), applied to this listener's traffic.  Example: `example_path_route_set`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

(Updatable) The communication port for the listener.  Example: `80`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

(Updatable) The protocol on which the listener accepts connection requests. To get a list of valid protocols, use the [ListProtocols](https://docs.cloud.oracle.com/iaas/api/#/en/loadbalancer/20170115/LoadBalancerProtocol/ListProtocols) operation.  Example: `HTTP`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleSetNames

(Updatable) The names of the [rule sets](https://docs.cloud.oracle.com/iaas/api/#/en/loadbalancer/20170115/RuleSet/) to apply to the listener.  Example: ["example_rule_set"].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionConfiguration

_Required_: No

_Type_: List of <a href="connectionconfiguration.md">ConnectionConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslConfiguration

_Required_: No

_Type_: List of <a href="sslconfiguration.md">SslConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### State

Returns the <code>State</code> value.

