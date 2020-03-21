# Terraform::Kubernetes::Service Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clusterip" title="ClusterIp">ClusterIp</a>" : <i>String</i>,
    "<a href="#externalips" title="ExternalIps">ExternalIps</a>" : <i>[ String, ... ]</i>,
    "<a href="#externalname" title="ExternalName">ExternalName</a>" : <i>String</i>,
    "<a href="#externaltrafficpolicy" title="ExternalTrafficPolicy">ExternalTrafficPolicy</a>" : <i>String</i>,
    "<a href="#loadbalancerip" title="LoadBalancerIp">LoadBalancerIp</a>" : <i>String</i>,
    "<a href="#loadbalancersourceranges" title="LoadBalancerSourceRanges">LoadBalancerSourceRanges</a>" : <i>[ String, ... ]</i>,
    "<a href="#publishnotreadyaddresses" title="PublishNotReadyAddresses">PublishNotReadyAddresses</a>" : <i>Boolean</i>,
    "<a href="#selector" title="Selector">Selector</a>" : <i>[ &lt;a href=&#34;spec-selector.md&#34;&gt;Selector&lt;/a&gt;, ... ]</i>,
    "<a href="#sessionaffinity" title="SessionAffinity">SessionAffinity</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>[ &lt;a href=&#34;spec-port.md&#34;&gt;Port&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clusterip" title="ClusterIp">ClusterIp</a>: <i>String</i>
<a href="#externalips" title="ExternalIps">ExternalIps</a>: <i>
      - String</i>
<a href="#externalname" title="ExternalName">ExternalName</a>: <i>String</i>
<a href="#externaltrafficpolicy" title="ExternalTrafficPolicy">ExternalTrafficPolicy</a>: <i>String</i>
<a href="#loadbalancerip" title="LoadBalancerIp">LoadBalancerIp</a>: <i>String</i>
<a href="#loadbalancersourceranges" title="LoadBalancerSourceRanges">LoadBalancerSourceRanges</a>: <i>
      - String</i>
<a href="#publishnotreadyaddresses" title="PublishNotReadyAddresses">PublishNotReadyAddresses</a>: <i>Boolean</i>
<a href="#selector" title="Selector">Selector</a>: <i>
      - &lt;a href=&#34;spec-selector.md&#34;&gt;Selector&lt;/a&gt;</i>
<a href="#sessionaffinity" title="SessionAffinity">SessionAffinity</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>
      - &lt;a href=&#34;spec-port.md&#34;&gt;Port&lt;/a&gt;</i>
</pre>

## Properties

#### ClusterIp

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalIps

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalTrafficPolicy

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerIp

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerSourceRanges

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishNotReadyAddresses

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selector

_Required_: No
_Type_: List of &lt;a href=&#34;spec-selector.md&#34;&gt;Selector&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionAffinity

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No
_Type_: List of &lt;a href=&#34;spec-port.md&#34;&gt;Port&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

