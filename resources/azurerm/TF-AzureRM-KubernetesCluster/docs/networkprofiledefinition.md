# TF::AzureRM::KubernetesCluster NetworkProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dnsserviceip" title="DnsServiceIp">DnsServiceIp</a>" : <i>String</i>,
    "<a href="#dockerbridgecidr" title="DockerBridgeCidr">DockerBridgeCidr</a>" : <i>String</i>,
    "<a href="#loadbalancersku" title="LoadBalancerSku">LoadBalancerSku</a>" : <i>String</i>,
    "<a href="#networkmode" title="NetworkMode">NetworkMode</a>" : <i>String</i>,
    "<a href="#networkplugin" title="NetworkPlugin">NetworkPlugin</a>" : <i>String</i>,
    "<a href="#networkpolicy" title="NetworkPolicy">NetworkPolicy</a>" : <i>String</i>,
    "<a href="#outboundtype" title="OutboundType">OutboundType</a>" : <i>String</i>,
    "<a href="#podcidr" title="PodCidr">PodCidr</a>" : <i>String</i>,
    "<a href="#servicecidr" title="ServiceCidr">ServiceCidr</a>" : <i>String</i>,
    "<a href="#loadbalancerprofile" title="LoadBalancerProfile">LoadBalancerProfile</a>" : <i>[ <a href="loadbalancerprofiledefinition.md">LoadBalancerProfileDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dnsserviceip" title="DnsServiceIp">DnsServiceIp</a>: <i>String</i>
<a href="#dockerbridgecidr" title="DockerBridgeCidr">DockerBridgeCidr</a>: <i>String</i>
<a href="#loadbalancersku" title="LoadBalancerSku">LoadBalancerSku</a>: <i>String</i>
<a href="#networkmode" title="NetworkMode">NetworkMode</a>: <i>String</i>
<a href="#networkplugin" title="NetworkPlugin">NetworkPlugin</a>: <i>String</i>
<a href="#networkpolicy" title="NetworkPolicy">NetworkPolicy</a>: <i>String</i>
<a href="#outboundtype" title="OutboundType">OutboundType</a>: <i>String</i>
<a href="#podcidr" title="PodCidr">PodCidr</a>: <i>String</i>
<a href="#servicecidr" title="ServiceCidr">ServiceCidr</a>: <i>String</i>
<a href="#loadbalancerprofile" title="LoadBalancerProfile">LoadBalancerProfile</a>: <i>
      - <a href="loadbalancerprofiledefinition.md">LoadBalancerProfileDefinition</a></i>
</pre>

## Properties

#### DnsServiceIp

IP address within the Kubernetes service address range that will be used by cluster service discovery (kube-dns). Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerBridgeCidr

IP address (in CIDR notation) used as the Docker bridge IP address on nodes. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerSku

Specifies the SKU of the Load Balancer used for this Kubernetes Cluster. Possible values are `Basic` and `Standard`. Defaults to `Standard`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkMode

Network mode to be used with Azure CNI. Possible values are `bridge` and `transparent`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPlugin

Network plugin to use for networking. Currently supported values are `azure` and `kubenet`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPolicy

Sets up network policy to be used with Azure CNI. [Network policy allows us to control the traffic flow between pods](https://docs.microsoft.com/en-us/azure/aks/use-network-policies). Currently supported values are `calico` and `azure`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutboundType

The outbound (egress) routing method which should be used for this Kubernetes Cluster. Possible values are `loadBalancer` and `userDefinedRouting`. Defaults to `loadBalancer`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodCidr

The CIDR to use for pod IP addresses. This field can only be set when `network_plugin` is set to `kubenet`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceCidr

The Network Range used by the Kubernetes service. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerProfile

_Required_: No

_Type_: List of <a href="loadbalancerprofiledefinition.md">LoadBalancerProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

