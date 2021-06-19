# TF::AWS::SsoadminManagedPolicyAttachment

Provides an IAM managed policy for a Single Sign-On (SSO) Permission Set resource

~> **NOTE:** Creating this resource will automatically [Provision the Permission Set](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ProvisionPermissionSet.html) to apply the corresponding updates to all assigned accounts.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SsoadminManagedPolicyAttachment",
    "Properties" : {
        "<a href="#instancearn" title="InstanceArn">InstanceArn</a>" : <i>String</i>,
        "<a href="#managedpolicyarn" title="ManagedPolicyArn">ManagedPolicyArn</a>" : <i>String</i>,
        "<a href="#permissionsetarn" title="PermissionSetArn">PermissionSetArn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SsoadminManagedPolicyAttachment
Properties:
    <a href="#instancearn" title="InstanceArn">InstanceArn</a>: <i>String</i>
    <a href="#managedpolicyarn" title="ManagedPolicyArn">ManagedPolicyArn</a>: <i>String</i>
    <a href="#permissionsetarn" title="PermissionSetArn">PermissionSetArn</a>: <i>String</i>
</pre>

## Properties

#### InstanceArn

The Amazon Resource Name (ARN) of the SSO Instance under which the operation will be executed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedPolicyArn

The IAM managed policy Amazon Resource Name (ARN) to be attached to the Permission Set.

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

#### ManagedPolicyName

Returns the <code>ManagedPolicyName</code> value.

