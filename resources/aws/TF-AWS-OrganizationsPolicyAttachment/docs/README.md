# TF::AWS::OrganizationsPolicyAttachment

Provides a resource to attach an AWS Organizations policy to an organization account, root, or unit.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::OrganizationsPolicyAttachment",
    "Properties" : {
        "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>String</i>,
        "<a href="#targetid" title="TargetId">TargetId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::OrganizationsPolicyAttachment
Properties:
    <a href="#policyid" title="PolicyId">PolicyId</a>: <i>String</i>
    <a href="#targetid" title="TargetId">TargetId</a>: <i>String</i>
</pre>

## Properties

#### PolicyId

The unique identifier (ID) of the policy that you want to attach to the target.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetId

The unique identifier (ID) of the root, organizational unit, or account number that you want to attach the policy to.

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

