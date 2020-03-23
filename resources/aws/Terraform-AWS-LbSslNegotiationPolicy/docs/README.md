# Terraform::AWS::LbSslNegotiationPolicy

Provides a load balancer SSL negotiation policy, which allows an ELB to control the ciphers and protocols that are supported during SSL negotiations between a client and a load balancer.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::LbSslNegotiationPolicy",
    "Properties" : {
        "<a href="#lbport" title="LbPort">LbPort</a>" : <i>Double</i>,
        "<a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#attribute" title="Attribute">Attribute</a>" : <i>[ <a href="attribute.md">Attribute</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::LbSslNegotiationPolicy
Properties:
    <a href="#lbport" title="LbPort">LbPort</a>: <i>Double</i>
    <a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#attribute" title="Attribute">Attribute</a>: <i>
      - <a href="attribute.md">Attribute</a></i>
</pre>

## Properties

#### LbPort

The load balancer port to which the policy
should be applied. This must be an active listener on the load
balancer.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancer

The load balancer to which the policy
should be attached.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the attribute
* `value` - The value of the attribute.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Attribute

_Required_: No

_Type_: List of <a href="attribute.md">Attribute</a>

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

