# TF::AWS::Route53DelegationSet

Provides a [Route53 Delegation Set](https://docs.aws.amazon.com/Route53/latest/APIReference/API-actions-by-function.html#actions-by-function-reusable-delegation-sets) resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Route53DelegationSet",
    "Properties" : {
        "<a href="#referencename" title="ReferenceName">ReferenceName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Route53DelegationSet
Properties:
    <a href="#referencename" title="ReferenceName">ReferenceName</a>: <i>String</i>
</pre>

## Properties

#### ReferenceName

This is a reference name used in Caller Reference
(helpful for identifying single delegation set amongst others).

_Required_: No

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

#### NameServers

Returns the <code>NameServers</code> value.

