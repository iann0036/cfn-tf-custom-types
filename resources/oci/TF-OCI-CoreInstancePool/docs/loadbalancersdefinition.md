# TF::OCI::CoreInstancePool LoadBalancersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backendsetname" title="BackendSetName">BackendSetName</a>" : <i>String</i>,
    "<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#vnicselection" title="VnicSelection">VnicSelection</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#backendsetname" title="BackendSetName">BackendSetName</a>: <i>String</i>
<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#vnicselection" title="VnicSelection">VnicSelection</a>: <i>String</i>
</pre>

## Properties

#### BackendSetName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnicSelection

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

