# TF::AWS::IamAccountPasswordPolicy

-> **Note:** There is only a single policy allowed per AWS account. An existing policy will be lost when using this resource as an effect of this limitation.

Manages Password Policy for the AWS Account.
See more about [Account Password Policy](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)
in the official AWS docs.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::IamAccountPasswordPolicy",
    "Properties" : {
        "<a href="#allowuserstochangepassword" title="AllowUsersToChangePassword">AllowUsersToChangePassword</a>" : <i>Boolean</i>,
        "<a href="#hardexpiry" title="HardExpiry">HardExpiry</a>" : <i>Boolean</i>,
        "<a href="#maxpasswordage" title="MaxPasswordAge">MaxPasswordAge</a>" : <i>Double</i>,
        "<a href="#minimumpasswordlength" title="MinimumPasswordLength">MinimumPasswordLength</a>" : <i>Double</i>,
        "<a href="#passwordreuseprevention" title="PasswordReusePrevention">PasswordReusePrevention</a>" : <i>Double</i>,
        "<a href="#requirelowercasecharacters" title="RequireLowercaseCharacters">RequireLowercaseCharacters</a>" : <i>Boolean</i>,
        "<a href="#requirenumbers" title="RequireNumbers">RequireNumbers</a>" : <i>Boolean</i>,
        "<a href="#requiresymbols" title="RequireSymbols">RequireSymbols</a>" : <i>Boolean</i>,
        "<a href="#requireuppercasecharacters" title="RequireUppercaseCharacters">RequireUppercaseCharacters</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::IamAccountPasswordPolicy
Properties:
    <a href="#allowuserstochangepassword" title="AllowUsersToChangePassword">AllowUsersToChangePassword</a>: <i>Boolean</i>
    <a href="#hardexpiry" title="HardExpiry">HardExpiry</a>: <i>Boolean</i>
    <a href="#maxpasswordage" title="MaxPasswordAge">MaxPasswordAge</a>: <i>Double</i>
    <a href="#minimumpasswordlength" title="MinimumPasswordLength">MinimumPasswordLength</a>: <i>Double</i>
    <a href="#passwordreuseprevention" title="PasswordReusePrevention">PasswordReusePrevention</a>: <i>Double</i>
    <a href="#requirelowercasecharacters" title="RequireLowercaseCharacters">RequireLowercaseCharacters</a>: <i>Boolean</i>
    <a href="#requirenumbers" title="RequireNumbers">RequireNumbers</a>: <i>Boolean</i>
    <a href="#requiresymbols" title="RequireSymbols">RequireSymbols</a>: <i>Boolean</i>
    <a href="#requireuppercasecharacters" title="RequireUppercaseCharacters">RequireUppercaseCharacters</a>: <i>Boolean</i>
</pre>

## Properties

#### AllowUsersToChangePassword

Whether to allow users to change their own password.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HardExpiry

Whether users are prevented from setting a new password after their password has expired (i.e. require administrator reset).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPasswordAge

The number of days that an user password is valid.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumPasswordLength

Minimum length to require for user passwords.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordReusePrevention

The number of previous passwords that users are prevented from reusing.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireLowercaseCharacters

Whether to require lowercase characters for user passwords.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireNumbers

Whether to require numbers for user passwords.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireSymbols

Whether to require symbols for user passwords.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireUppercaseCharacters

Whether to require uppercase characters for user passwords.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ExpirePasswords

Returns the <code>ExpirePasswords</code> value.

#### Id

Returns the <code>Id</code> value.

