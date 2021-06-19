# TF::AWS::LoadBalancerPolicy

Provides a load balancer policy, which can be attached to an ELB listener or backend server.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::LoadBalancerPolicy",
    "Properties" : {
        "<a href="#loadbalancername" title="LoadBalancerName">LoadBalancerName</a>" : <i>String</i>,
        "<a href="#policyname" title="PolicyName">PolicyName</a>" : <i>String</i>,
        "<a href="#policytypename" title="PolicyTypeName">PolicyTypeName</a>" : <i>String</i>,
        "<a href="#policyattribute" title="PolicyAttribute">PolicyAttribute</a>" : <i>[ <a href="policyattributedefinition.md">PolicyAttributeDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::LoadBalancerPolicy
Properties:
    <a href="#loadbalancername" title="LoadBalancerName">LoadBalancerName</a>: <i>String</i>
    <a href="#policyname" title="PolicyName">PolicyName</a>: <i>String</i>
    <a href="#policytypename" title="PolicyTypeName">PolicyTypeName</a>: <i>String</i>
    <a href="#policyattribute" title="PolicyAttribute">PolicyAttribute</a>: <i>
      - <a href="policyattributedefinition.md">PolicyAttributeDefinition</a></i>
</pre>

## Properties

#### LoadBalancerName

The load balancer on which the policy is defined.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyName

The name of the load balancer policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyTypeName

The policy type.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyAttribute

_Required_: No

_Type_: List of <a href="policyattributedefinition.md">PolicyAttributeDefinition</a>

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

