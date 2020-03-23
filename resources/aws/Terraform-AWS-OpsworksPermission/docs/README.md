# Terraform::AWS::OpsworksPermission

Provides an OpsWorks permission resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::OpsworksPermission",
    "Properties" : {
        "<a href="#allowssh" title="AllowSsh">AllowSsh</a>" : <i>Boolean</i>,
        "<a href="#allowsudo" title="AllowSudo">AllowSudo</a>" : <i>Boolean</i>,
        "<a href="#level" title="Level">Level</a>" : <i>String</i>,
        "<a href="#stackid" title="StackId">StackId</a>" : <i>String</i>,
        "<a href="#userarn" title="UserArn">UserArn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::OpsworksPermission
Properties:
    <a href="#allowssh" title="AllowSsh">AllowSsh</a>: <i>Boolean</i>
    <a href="#allowsudo" title="AllowSudo">AllowSudo</a>: <i>Boolean</i>
    <a href="#level" title="Level">Level</a>: <i>String</i>
    <a href="#stackid" title="StackId">StackId</a>: <i>String</i>
    <a href="#userarn" title="UserArn">UserArn</a>: <i>String</i>
</pre>

## Properties

#### AllowSsh

Whether the user is allowed to use SSH to communicate with the instance.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowSudo

Whether the user is allowed to use sudo to elevate privileges.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Level

The users permission level. Mus be one of `deny`, `show`, `deploy`, `manage`, `iam_only`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackId

The stack to set the permissions for.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserArn

The user's IAM ARN to set permissions for.

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

