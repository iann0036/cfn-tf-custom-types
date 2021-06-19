# TF::SumoLogic::PasswordPolicy

Sets the [Sumologic Password Policy][1]. Since there is only a single password policy for an organization,
please ensure that only a single instance of such resource is defined.
The behavior for defining more than one password policy resources is undefined.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SumoLogic::PasswordPolicy",
    "Properties" : {
        "<a href="#accountlockoutdurationinmins" title="AccountLockoutDurationInMins">AccountLockoutDurationInMins</a>" : <i>Double</i>,
        "<a href="#accountlockoutthreshold" title="AccountLockoutThreshold">AccountLockoutThreshold</a>" : <i>Double</i>,
        "<a href="#failedloginresetdurationinmins" title="FailedLoginResetDurationInMins">FailedLoginResetDurationInMins</a>" : <i>Double</i>,
        "<a href="#maxlength" title="MaxLength">MaxLength</a>" : <i>Double</i>,
        "<a href="#maxpasswordageindays" title="MaxPasswordAgeInDays">MaxPasswordAgeInDays</a>" : <i>Double</i>,
        "<a href="#minlength" title="MinLength">MinLength</a>" : <i>Double</i>,
        "<a href="#minuniquepasswords" title="MinUniquePasswords">MinUniquePasswords</a>" : <i>Double</i>,
        "<a href="#mustcontaindigits" title="MustContainDigits">MustContainDigits</a>" : <i>Boolean</i>,
        "<a href="#mustcontainlowercase" title="MustContainLowercase">MustContainLowercase</a>" : <i>Boolean</i>,
        "<a href="#mustcontainspecialchars" title="MustContainSpecialChars">MustContainSpecialChars</a>" : <i>Boolean</i>,
        "<a href="#mustcontainuppercase" title="MustContainUppercase">MustContainUppercase</a>" : <i>Boolean</i>,
        "<a href="#remembermfa" title="RememberMfa">RememberMfa</a>" : <i>Boolean</i>,
        "<a href="#requiremfa" title="RequireMfa">RequireMfa</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SumoLogic::PasswordPolicy
Properties:
    <a href="#accountlockoutdurationinmins" title="AccountLockoutDurationInMins">AccountLockoutDurationInMins</a>: <i>Double</i>
    <a href="#accountlockoutthreshold" title="AccountLockoutThreshold">AccountLockoutThreshold</a>: <i>Double</i>
    <a href="#failedloginresetdurationinmins" title="FailedLoginResetDurationInMins">FailedLoginResetDurationInMins</a>: <i>Double</i>
    <a href="#maxlength" title="MaxLength">MaxLength</a>: <i>Double</i>
    <a href="#maxpasswordageindays" title="MaxPasswordAgeInDays">MaxPasswordAgeInDays</a>: <i>Double</i>
    <a href="#minlength" title="MinLength">MinLength</a>: <i>Double</i>
    <a href="#minuniquepasswords" title="MinUniquePasswords">MinUniquePasswords</a>: <i>Double</i>
    <a href="#mustcontaindigits" title="MustContainDigits">MustContainDigits</a>: <i>Boolean</i>
    <a href="#mustcontainlowercase" title="MustContainLowercase">MustContainLowercase</a>: <i>Boolean</i>
    <a href="#mustcontainspecialchars" title="MustContainSpecialChars">MustContainSpecialChars</a>: <i>Boolean</i>
    <a href="#mustcontainuppercase" title="MustContainUppercase">MustContainUppercase</a>: <i>Boolean</i>
    <a href="#remembermfa" title="RememberMfa">RememberMfa</a>: <i>Boolean</i>
    <a href="#requiremfa" title="RequireMfa">RequireMfa</a>: <i>Boolean</i>
</pre>

## Properties

#### AccountLockoutDurationInMins

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountLockoutThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailedLoginResetDurationInMins

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLength

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPasswordAgeInDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinLength

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinUniquePasswords

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MustContainDigits

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MustContainLowercase

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MustContainSpecialChars

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MustContainUppercase

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RememberMfa

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireMfa

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

