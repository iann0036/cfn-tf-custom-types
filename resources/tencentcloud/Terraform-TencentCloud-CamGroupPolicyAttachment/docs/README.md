# Terraform::TencentCloud::CamGroupPolicyAttachment

Provides a resource to create a CAM group policy attachment.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::CamGroupPolicyAttachment",
    "Properties" : {
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
        "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::CamGroupPolicyAttachment
Properties:
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
    <a href="#policyid" title="PolicyId">PolicyId</a>: <i>String</i>
</pre>

## Properties

#### GroupId

Id of the attached CAM group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyId

Id of the policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateMode

Returns the <code>CreateMode</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### PolicyName

Returns the <code>PolicyName</code> value.

#### PolicyType

Returns the <code>PolicyType</code> value.

