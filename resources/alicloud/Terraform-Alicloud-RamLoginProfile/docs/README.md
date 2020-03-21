# Terraform::Alicloud::RamLoginProfile

Provides a RAM User Login Profile resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::RamLoginProfile",
    "Properties" : {
        "<a href="#mfabindrequired" title="MfaBindRequired">MfaBindRequired</a>" : <i>Boolean</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#passwordresetrequired" title="PasswordResetRequired">PasswordResetRequired</a>" : <i>Boolean</i>,
        "<a href="#username" title="UserName">UserName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::RamLoginProfile
Properties:
    <a href="#mfabindrequired" title="MfaBindRequired">MfaBindRequired</a>: <i>Boolean</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#passwordresetrequired" title="PasswordResetRequired">PasswordResetRequired</a>: <i>Boolean</i>
    <a href="#username" title="UserName">UserName</a>: <i>String</i>
</pre>

## Properties

#### MfaBindRequired

This parameter indicates whether the MFA needs to be bind when the user first logs in. Default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password of the RAM user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordResetRequired

This parameter indicates whether the password needs to be reset when the user first logs in. Default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserName

Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin with a hyphen.

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

