# Terraform::AzureRM::KubernetesCluster NetworkProfile LoadBalancerProfile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#managedoutboundipcount" title="ManagedOutboundIpCount">ManagedOutboundIpCount</a>" : <i>Double</i>,
    "<a href="#outboundipaddressids" title="OutboundIpAddressIds">OutboundIpAddressIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#outboundipprefixids" title="OutboundIpPrefixIds">OutboundIpPrefixIds</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#managedoutboundipcount" title="ManagedOutboundIpCount">ManagedOutboundIpCount</a>: <i>Double</i>
<a href="#outboundipaddressids" title="OutboundIpAddressIds">OutboundIpAddressIds</a>: <i>
      - String</i>
<a href="#outboundipprefixids" title="OutboundIpPrefixIds">OutboundIpPrefixIds</a>: <i>
      - String</i>
</pre>

## Properties

#### ManagedOutboundIpCount

Count of desired managed outbound IPs for the cluster load balancer. Must be in the range of [1, 100].

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

