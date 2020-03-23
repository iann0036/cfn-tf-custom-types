# Terraform::AWS::IamUserLoginProfile

Manages an IAM User Login Profile with limited support for password creation during Terraform resource creation. Uses PGP to encrypt the password for safe transport to the user. PGP keys can be obtained from Keybase.

-> To reset an IAM User login password via Terraform, you can use the [`terraform taint` command](https://www.terraform.io/docs/commands/taint.html) or change any of the arguments.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::IamUserLoginProfile",
    "Properties" : {
        "<a href="#passwordlength" title="PasswordLength">PasswordLength</a>" : <i>Double</i>,
        "<a href="#passwordresetrequired" title="PasswordResetRequired">PasswordResetRequired</a>" : <i>Boolean</i>,
        "<a href="#pgpkey" title="PgpKey">PgpKey</a>" : <i>String</i>,
        "<a href="#user" title="User">User</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::IamUserLoginProfile
Properties:
    <a href="#passwordlength" title="PasswordLength">PasswordLength</a>: <i>Double</i>
    <a href="#passwordresetrequired" title="PasswordResetRequired">PasswordResetRequired</a>: <i>Boolean</i>
    <a href="#pgpkey" title="PgpKey">PgpKey</a>: <i>String</i>
    <a href="#user" title="User">User</a>: <i>String</i>
</pre>

## Properties

#### PasswordLength

The length of the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordResetRequired

Whether the user should be forced to reset the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PgpKey

Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:username`. Only applies on resource creation. Drift detection is not possible with this argument.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

The IAM user's name.

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

#### EncryptedPassword

Returns the <code>EncryptedPassword</code> value.

#### Id

Returns the <code>Id</code> value.

#### KeyFingerprint

Returns the <code>KeyFingerprint</code> value.

