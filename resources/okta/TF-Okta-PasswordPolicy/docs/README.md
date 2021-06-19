# TF::Okta::PasswordPolicy

CloudFormation equivalent of okta_password_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::PasswordPolicy",
    "Properties" : {
        "<a href="#authprovider" title="AuthProvider">AuthProvider</a>" : <i>String</i>,
        "<a href="#callrecovery" title="CallRecovery">CallRecovery</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#emailrecovery" title="EmailRecovery">EmailRecovery</a>" : <i>String</i>,
        "<a href="#groupsincluded" title="GroupsIncluded">GroupsIncluded</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
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
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#questionminlength" title="QuestionMinLength">QuestionMinLength</a>" : <i>Double</i>,
        "<a href="#questionrecovery" title="QuestionRecovery">QuestionRecovery</a>" : <i>String</i>,
        "<a href="#recoveryemailtoken" title="RecoveryEmailToken">RecoveryEmailToken</a>" : <i>Double</i>,
        "<a href="#skipunlock" title="SkipUnlock">SkipUnlock</a>" : <i>Boolean</i>,
        "<a href="#smsrecovery" title="SmsRecovery">SmsRecovery</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::PasswordPolicy
Properties:
    <a href="#authprovider" title="AuthProvider">AuthProvider</a>: <i>String</i>
    <a href="#callrecovery" title="CallRecovery">CallRecovery</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#emailrecovery" title="EmailRecovery">EmailRecovery</a>: <i>String</i>
    <a href="#groupsincluded" title="GroupsIncluded">GroupsIncluded</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
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
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#questionminlength" title="QuestionMinLength">QuestionMinLength</a>: <i>Double</i>
    <a href="#questionrecovery" title="QuestionRecovery">QuestionRecovery</a>: <i>String</i>
    <a href="#recoveryemailtoken" title="RecoveryEmailToken">RecoveryEmailToken</a>: <i>Double</i>
    <a href="#skipunlock" title="SkipUnlock">SkipUnlock</a>: <i>Boolean</i>
    <a href="#smsrecovery" title="SmsRecovery">SmsRecovery</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
</pre>

## Properties

#### AuthProvider

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CallRecovery

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailRecovery

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupsIncluded

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordAutoUnlockMinutes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordDictionaryLookup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordExcludeFirstName

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordExcludeLastName

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordExcludeUsername

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordExpireWarnDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordHistoryCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordLockoutNotificationChannels

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordMaxAgeDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordMaxLockoutAttempts

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordMinAgeMinutes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordMinLength

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordMinLowercase

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordMinNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordMinSymbol

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordMinUppercase

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordShowLockoutFailures

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuestionMinLength

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuestionRecovery

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryEmailToken

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipUnlock

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsRecovery

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

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

