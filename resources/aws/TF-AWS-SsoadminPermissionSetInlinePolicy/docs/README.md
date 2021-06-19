# TF::AWS::SsoadminPermissionSetInlinePolicy

Provides an IAM inline policy for a Single Sign-On (SSO) Permission Set resource

~> **NOTE:** AWS Single Sign-On (SSO) only supports one IAM inline policy per [`aws_ssoadmin_permission_set`](ssoadmin_permission_set.html) resource.
Creating or updating this resource will automatically [Provision the Permission Set](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ProvisionPermissionSet.html) to apply the corresponding updates to all assigned accounts.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SsoadminPermissionSetInlinePolicy",
    "Properties" : {
        "<a href="#inlinepolicy" title="InlinePolicy">InlinePolicy</a>" : <i>String</i>,
        "<a href="#instancearn" title="InstanceArn">InstanceArn</a>" : <i>String</i>,
        "<a href="#permissionsetarn" title="PermissionSetArn">PermissionSetArn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SsoadminPermissionSetInlinePolicy
Properties:
    <a href="#inlinepolicy" title="InlinePolicy">InlinePolicy</a>: <i>String</i>
    <a href="#instancearn" title="InstanceArn">InstanceArn</a>: <i>String</i>
    <a href="#permissionsetarn" title="PermissionSetArn">PermissionSetArn</a>: <i>String</i>
</pre>

## Properties

#### InlinePolicy

The IAM inline policy to attach to a Permission Set.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceArn

The Amazon Resource Name (ARN) of the SSO Instance under which the operation will be executed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissionSetArn

The Amazon Resource Name (ARN) of the Permission Set.

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

