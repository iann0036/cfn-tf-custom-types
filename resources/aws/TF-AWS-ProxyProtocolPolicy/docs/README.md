# TF::AWS::ProxyProtocolPolicy

Provides a proxy protocol policy, which allows an ELB to carry a client connection information to a backend.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ProxyProtocolPolicy",
    "Properties" : {
        "<a href="#instanceports" title="InstancePorts">InstancePorts</a>" : <i>[ String, ... ]</i>,
        "<a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ProxyProtocolPolicy
Properties:
    <a href="#instanceports" title="InstancePorts">InstancePorts</a>: <i>
      - String</i>
    <a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>: <i>String</i>
</pre>

## Properties

#### InstancePorts

List of instance ports to which the policy
should be applied. This can be specified if the protocol is SSL or TCP.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancer

The load balancer to which the policy
should be attached.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

