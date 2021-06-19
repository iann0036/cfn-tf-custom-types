# TF::AWS::SsoadminAccountAssignment

Provides a Single Sign-On (SSO) Account Assignment resource

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SsoadminAccountAssignment",
    "Properties" : {
        "<a href="#instancearn" title="InstanceArn">InstanceArn</a>" : <i>String</i>,
        "<a href="#permissionsetarn" title="PermissionSetArn">PermissionSetArn</a>" : <i>String</i>,
        "<a href="#principalid" title="PrincipalId">PrincipalId</a>" : <i>String</i>,
        "<a href="#principaltype" title="PrincipalType">PrincipalType</a>" : <i>String</i>,
        "<a href="#targetid" title="TargetId">TargetId</a>" : <i>String</i>,
        "<a href="#targettype" title="TargetType">TargetType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SsoadminAccountAssignment
Properties:
    <a href="#instancearn" title="InstanceArn">InstanceArn</a>: <i>String</i>
    <a href="#permissionsetarn" title="PermissionSetArn">PermissionSetArn</a>: <i>String</i>
    <a href="#principalid" title="PrincipalId">PrincipalId</a>: <i>String</i>
    <a href="#principaltype" title="PrincipalType">PrincipalType</a>: <i>String</i>
    <a href="#targetid" title="TargetId">TargetId</a>: <i>String</i>
    <a href="#targettype" title="TargetType">TargetType</a>: <i>String</i>
</pre>

## Properties

#### InstanceArn

The Amazon Resource Name (ARN) of the SSO Instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissionSetArn

The Amazon Resource Name (ARN) of the Permission Set that the admin wants to grant the principal access to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrincipalId

An identifier for an object in SSO, such as a user or group. PrincipalIds are GUIDs (For example, `f81d4fae-7dec-11d0-a765-00a0c91e6bf6`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrincipalType

The entity type for which the assignment will be created. Valid values: `USER`, `GROUP`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetId

An AWS account identifier, typically a 10-12 digit string.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetType

The entity type for which the assignment will be created. Valid values: `AWS_ACCOUNT`.

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

