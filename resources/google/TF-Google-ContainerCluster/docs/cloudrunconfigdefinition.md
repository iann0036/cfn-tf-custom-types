# TF::Google::ContainerCluster CloudrunConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
    "<a href="#loadbalancertype" title="LoadBalancerType">LoadBalancerType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
<a href="#loadbalancertype" title="LoadBalancerType">LoadBalancerType</a>: <i>String</i>
</pre>

## Properties

#### Disabled

The status of the CloudRun addon. It is disabled by default. Set `disabled=false` to enable.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerType

The load balancer type of CloudRun ingress service. It is external load balancer by default.
Set `load_balancer_type=LOAD_BALANCER_TYPE_INTERNAL` to configure it as internal load balancer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

