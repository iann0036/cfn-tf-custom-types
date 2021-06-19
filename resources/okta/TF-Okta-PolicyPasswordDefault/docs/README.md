# TF::Okta::PolicyPasswordDefault

Configures default password policy.

This resource allows you to configure default password policy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::PolicyPasswordDefault",
    "Properties" : {
        "<a href="#callrecovery" title="CallRecovery">CallRecovery</a>" : <i>String</i>,
        "<a href="#emailrecovery" title="EmailRecovery">EmailRecovery</a>" : <i>String</i>,
        "<a href="#passwordautounlockminutes" title="PasswordAutoUnlockMinutes">PasswordAutoUnlockMinutes</a>" : <i>Double</i>,
        "<a href="#passworddictionarylookup" title="PasswordDictionaryLookup">PasswordDictionaryLookup</a>" : <i>Boolean</i>,
        "<a href="#passwordexcludefirstname" title="PasswordExcludeFirstName">PasswordExcludeFirstName</a>" : <i>Boolean</i>,
        "<a href="#passwordexcludelastname" title="PasswordExcludeLastName">PasswordExcludeLastName</a>" : <i>Boolean</i>,
        "<a href="#passwordexcludeusername" title="PasswordExcludeUsername">PasswordExcludeUsername</a>" : <i>Boolean</i>,
        "<a href="#passwordexpirewarndays" title="PasswordExpireWarnDays">PasswordExpireWarnDays</a>" : <i>Double</i>,
        "<a href="#passwordhistorycount" title="PasswordHistoryCount">PasswordHistoryCount</a>" : <i>Double</i>,
        "<a href="#passwordlockoutnotificationchannels" title="PasswordLockoutNotificationChannels">PasswordLockoutNotificationChannels</a>" : <i>[ String, ... ]</i>,
        "<a href="#passwordmaxagedays" title="PasswordMaxAgeDays">PasswordMaxAgeDays</a>" : <i>Double</i>,
        "<a href="#passwordmaxlockoutattempts" title="PasswordMaxLockoutAttempts">PasswordMaxLockoutAttempts</a>" : <i>Double</i>,
        "<a href="#passwordminageminutes" title="PasswordMinAgeMinutes">PasswordMinAgeMinutes</a>" : <i>Double</i>,
        "<a href="#passwordminlength" title="PasswordMinLength">PasswordMinLength</a>" : <i>Double</i>,
        "<a href="#passwordminlowercase" title="PasswordMinLowercase">PasswordMinLowercase</a>" : <i>Double</i>,
        "<a href="#passwordminnumber" title="PasswordMinNumber">PasswordMinNumber</a>" : <i>Double</i>,
        "<a href="#passwordminsymbol" title="PasswordMinSymbol">PasswordMinSymbol</a>" : <i>Double</i>,
        "<a href="#passwordminuppercase" title="PasswordMinUppercase">PasswordMinUppercase</a>" : <i>Double</i>,
        "<a href="#passwordshowlockoutfailures" title="PasswordShowLockoutFailures">PasswordShowLockoutFailures</a>" : <i>Boolean</i>,
        "<a href="#questionminlength" title="QuestionMinLength">QuestionMinLength</a>" : <i>Double</i>,
        "<a href="#questionrecovery" title="QuestionRecovery">QuestionRecovery</a>" : <i>String</i>,
        "<a href="#recoveryemailtoken" title="RecoveryEmailToken">RecoveryEmailToken</a>" : <i>Double</i>,
        "<a href="#skipunlock" title="SkipUnlock">SkipUnlock</a>" : <i>Boolean</i>,
        "<a href="#smsrecovery" title="SmsRecovery">SmsRecovery</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::PolicyPasswordDefault
Properties:
    <a href="#callrecovery" title="CallRecovery">CallRecovery</a>: <i>String</i>
    <a href="#emailrecovery" title="EmailRecovery">EmailRecovery</a>: <i>String</i>
    <a href="#passwordautounlockminutes" title="PasswordAutoUnlockMinutes">PasswordAutoUnlockMinutes</a>: <i>Double</i>
    <a href="#passworddictionarylookup" title="PasswordDictionaryLookup">PasswordDictionaryLookup</a>: <i>Boolean</i>
    <a href="#passwordexcludefirstname" title="PasswordExcludeFirstName">PasswordExcludeFirstName</a>: <i>Boolean</i>
    <a href="#passwordexcludelastname" title="PasswordExcludeLastName">PasswordExcludeLastName</a>: <i>Boolean</i>
    <a href="#passwordexcludeusername" title="PasswordExcludeUsername">PasswordExcludeUsername</a>: <i>Boolean</i>
    <a href="#passwordexpirewarndays" title="PasswordExpireWarnDays">PasswordExpireWarnDays</a>: <i>Double</i>
    <a href="#passwordhistorycount" title="PasswordHistoryCount">PasswordHistoryCount</a>: <i>Double</i>
    <a href="#passwordlockoutnotificationchannels" title="PasswordLockoutNotificationChannels">PasswordLockoutNotificationChannels</a>: <i>
      - String</i>
    <a href="#passwordmaxagedays" title="PasswordMaxAgeDays">PasswordMaxAgeDays</a>: <i>Double</i>
    <a href="#passwordmaxlockoutattempts" title="PasswordMaxLockoutAttempts">PasswordMaxLockoutAttempts</a>: <i>Double</i>
    <a href="#passwordminageminutes" title="PasswordMinAgeMinutes">PasswordMinAgeMinutes</a>: <i>Double</i>
    <a href="#passwordminlength" title="PasswordMinLength">PasswordMinLength</a>: <i>Double</i>
    <a href="#passwordminlowercase" title="PasswordMinLowercase">PasswordMinLowercase</a>: <i>Double</i>
    <a href="#passwordminnumber" title="PasswordMinNumber">PasswordMinNumber</a>: <i>Double</i>
    <a href="#passwordminsymbol" title="PasswordMinSymbol">PasswordMinSymbol</a>: <i>Double</i>
    <a href="#passwordminuppercase" title="PasswordMinUppercase">PasswordMinUppercase</a>: <i>Double</i>
    <a href="#passwordshowlockoutfailures" title="PasswordShowLockoutFailures">PasswordShowLockoutFailures</a>: <i>Boolean</i>
    <a href="#questionminlength" title="QuestionMinLength">QuestionMinLength</a>: <i>Double</i>
    <a href="#questionrecovery" title="QuestionRecovery">QuestionRecovery</a>: <i>String</i>
    <a href="#recoveryemailtoken" title="RecoveryEmailToken">RecoveryEmailToken</a>: <i>Double</i>
    <a href="#skipunlock" title="SkipUnlock">SkipUnlock</a>: <i>Boolean</i>
    <a href="#smsrecovery" title="SmsRecovery">SmsRecovery</a>: <i>String</i>
</pre>

## Properties

#### CallRecovery

Enable or disable voice call password recovery: ACTIVE or INACTIVE.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailRecovery

Enable or disable email password recovery: ACTIVE or INACTIVE.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordAutoUnlockMinutes

Number of minutes before a locked account is unlocked: 0 = no limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordDictionaryLookup

Check Passwords Against Common Password Dictionary.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordExcludeFirstName

User firstName attribute must be excluded from the password.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordExcludeLastName

User lastName attribute must be excluded from the password.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordExcludeUsername

If the username must be excluded from the password.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordExpireWarnDays

Length in days a user will be warned before password expiry: 0 = no warning.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordHistoryCount

Number of distinct passwords that must be created before they can be reused: 0 =
none.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordLockoutNotificationChannels

Notification channels to use to notify a user when their account
has been locked.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordMaxAgeDays

Length in days a password is valid before expiry: 0 = no limit.,.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordMaxLockoutAttempts

Number of unsuccessful login attempts allowed before lockout: 0 = no
limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordMinAgeMinutes

Minimum time interval in minutes between password changes: 0 = no limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordMinLength

Minimum password length. Default is 8.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordMinLowercase

Minimum number of lower case characters in a password.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordMinNumber

Minimum number of numbers in a password.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordMinSymbol

Minimum number of symbols in a password.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordMinUppercase

Minimum number of upper case characters in a password.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordShowLockoutFailures

If a user should be informed when their account is locked.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuestionMinLength

Min length of the password recovery question answer.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuestionRecovery

Enable or disable security question password recovery: ACTIVE or INACTIVE.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryEmailToken

Lifetime in minutes of the recovery email token.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipUnlock

When an Active Directory user is locked out of Okta, the Okta unlock operation should also
attempt to unlock the user's Windows account.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsRecovery

Enable or disable SMS password recovery: ACTIVE or INACTIVE.

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

#### DefaultAuthProvider

Returns the <code>DefaultAuthProvider</code> value.

#### DefaultIncludedGroupId

Returns the <code>DefaultIncludedGroupId</code> value.

#### Description

Returns the <code>Description</code> value.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### Priority

Returns the <code>Priority</code> value.

#### Status

Returns the <code>Status</code> value.

