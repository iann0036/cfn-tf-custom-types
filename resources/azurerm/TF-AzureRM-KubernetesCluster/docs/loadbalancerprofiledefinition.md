# TF::AzureRM::KubernetesCluster LoadBalancerProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#idletimeoutinminutes" title="IdleTimeoutInMinutes">IdleTimeoutInMinutes</a>" : <i>Double</i>,
    "<a href="#managedoutboundipcount" title="ManagedOutboundIpCount">ManagedOutboundIpCount</a>" : <i>Double</i>,
    "<a href="#outboundipaddressids" title="OutboundIpAddressIds">OutboundIpAddressIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#outboundipprefixids" title="OutboundIpPrefixIds">OutboundIpPrefixIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#outboundportsallocated" title="OutboundPortsAllocated">OutboundPortsAllocated</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#idletimeoutinminutes" title="IdleTimeoutInMinutes">IdleTimeoutInMinutes</a>: <i>Double</i>
<a href="#managedoutboundipcount" title="ManagedOutboundIpCount">ManagedOutboundIpCount</a>: <i>Double</i>
<a href="#outboundipaddressids" title="OutboundIpAddressIds">OutboundIpAddressIds</a>: <i>
      - String</i>
<a href="#outboundipprefixids" title="OutboundIpPrefixIds">OutboundIpPrefixIds</a>: <i>
      - String</i>
<a href="#outboundportsallocated" title="OutboundPortsAllocated">OutboundPortsAllocated</a>: <i>Double</i>
</pre>

## Properties

#### IdleTimeoutInMinutes

Desired outbound flow idle timeout in minutes for the cluster load balancer. Must be between `4` and `120` inclusive. Defaults to `30`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedOutboundIpCount

Count of desired managed outbound IPs for the cluster load balancer. Must be between `1` and `100` inclusive.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutboundIpAddressIds

The ID of the Public IP Addresses which should be used for outbound communication for the cluster load balancer.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutboundIpPrefixIds

The ID of the outbound Public IP Address Prefixes which should be used for the cluster load balancer.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutboundPortsAllocated

Number of desired SNAT port for each VM in the clusters load balancer. Must be between `0` and `64000` inclusive. Defaults to `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

