# Terraform::AzureRM::KubernetesCluster NetworkProfile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dnsserviceip" title="DnsServiceIp">DnsServiceIp</a>" : <i>String</i>,
    "<a href="#dockerbridgecidr" title="DockerBridgeCidr">DockerBridgeCidr</a>" : <i>String</i>,
    "<a href="#loadbalancersku" title="LoadBalancerSku">LoadBalancerSku</a>" : <i>String</i>,
    "<a href="#networkplugin" title="NetworkPlugin">NetworkPlugin</a>" : <i>String</i>,
    "<a href="#networkpolicy" title="NetworkPolicy">NetworkPolicy</a>" : <i>String</i>,
    "<a href="#podcidr" title="PodCidr">PodCidr</a>" : <i>String</i>,
    "<a href="#servicecidr" title="ServiceCidr">ServiceCidr</a>" : <i>String</i>,
    "<a href="#loadbalancerprofile" title="LoadBalancerProfile">LoadBalancerProfile</a>" : <i>[ &lt;a href=&#34;networkprofile-loadbalancerprofile.md&#34;&gt;LoadBalancerProfile&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dnsserviceip" title="DnsServiceIp">DnsServiceIp</a>: <i>String</i>
<a href="#dockerbridgecidr" title="DockerBridgeCidr">DockerBridgeCidr</a>: <i>String</i>
<a href="#loadbalancersku" title="LoadBalancerSku">LoadBalancerSku</a>: <i>String</i>
<a href="#networkplugin" title="NetworkPlugin">NetworkPlugin</a>: <i>String</i>
<a href="#networkpolicy" title="NetworkPolicy">NetworkPolicy</a>: <i>String</i>
<a href="#podcidr" title="PodCidr">PodCidr</a>: <i>String</i>
<a href="#servicecidr" title="ServiceCidr">ServiceCidr</a>: <i>String</i>
<a href="#loadbalancerprofile" title="LoadBalancerProfile">LoadBalancerProfile</a>: <i>
      - &lt;a href=&#34;networkprofile-loadbalancerprofile.md&#34;&gt;LoadBalancerProfile&lt;/a&gt;</i>
</pre>

## Properties

#### DnsServiceIp

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerBridgeCidr

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerSku

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPlugin

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPolicy

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodCidr

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceCidr

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerProfile

_Required_: No
_Type_: List of &lt;a href=&#34;networkprofile-loadbalancerprofile.md&#34;&gt;LoadBalancerProfile&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

