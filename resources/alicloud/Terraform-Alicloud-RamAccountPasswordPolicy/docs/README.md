# Terraform::Alicloud::RamAccountPasswordPolicy

Provides a RAM password policy configuration for entire account. Only one resource per account.

-> **NOTE:** This resource overwrites an existing configuration. During action `terraform destroy` it sets values the same as defaults for this resource (it does not preserve any preexisted configuration).

-> **NOTE:** Available in 1.46.0+

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::RamAccountPasswordPolicy",
    "Properties" : {
        "<a href="#hardexpiry" title="HardExpiry">HardExpiry</a>" : <i>Boolean</i>,
        "<a href="#maxloginattempts" title="MaxLoginAttempts">MaxLoginAttempts</a>" : <i>Double</i>,
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
Type: Terraform::Alicloud::RamAccountPasswordPolicy
Properties:
    <a href="#hardexpiry" title="HardExpiry">HardExpiry</a>: <i>Boolean</i>
    <a href="#maxloginattempts" title="MaxLoginAttempts">MaxLoginAttempts</a>: <i>Double</i>
    <a href="#maxpasswordage" title="MaxPasswordAge">MaxPasswordAge</a>: <i>Double</i>
    <a href="#minimumpasswordlength" title="MinimumPasswordLength">MinimumPasswordLength</a>: <i>Double</i>
    <a href="#passwordreuseprevention" title="PasswordReusePrevention">PasswordReusePrevention</a>: <i>Double</i>
    <a href="#requirelowercasecharacters" title="RequireLowercaseCharacters">RequireLowercaseCharacters</a>: <i>Boolean</i>
    <a href="#requirenumbers" title="RequireNumbers">RequireNumbers</a>: <i>Boolean</i>
    <a href="#requiresymbols" title="RequireSymbols">RequireSymbols</a>: <i>Boolean</i>
    <a href="#requireuppercasecharacters" title="RequireUppercaseCharacters">RequireUppercaseCharacters</a>: <i>Boolean</i>
</pre>

## Properties

#### HardExpiry

Specifies if a password can expire in a hard way. Default to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLoginAttempts

Maximum logon attempts with an incorrect password within an hour. Valid value range: [0-32]. Default to 5.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPasswordAge

The number of days after which password expires. A value of 0 indicates that the password never expires. Valid value range: [0-1095]. Default to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumPasswordLength

Minimal required length of password for a user. Valid value range: [8-32]. Default to 12.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordReusePrevention

User is not allowed to use the latest number of passwords specified in this parameter. A value of 0 indicates the password history check policy is disabled. Valid value range: [0-24]. Default to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireLowercaseCharacters

Specifies if the occurrence of a lowercase character in the password is mandatory. Default to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireNumbers

Specifies if the occurrence of a number in the password is mandatory. Default to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireSymbols

(Optional Specifies if the occurrence of a special character in the password is mandatory. Default to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireUppercaseCharacters

Specifies if the occurrence of an uppercase character in the password is mandatory. Default to true.

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

#### Id

Returns the <code>Id</code> value.

