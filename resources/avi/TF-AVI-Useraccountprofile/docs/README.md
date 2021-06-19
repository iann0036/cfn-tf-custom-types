# TF::AVI::Useraccountprofile

The UserAccountProfile resource allows the creation and management of Avi UserAccountProfile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Useraccountprofile",
    "Properties" : {
        "<a href="#accountlocktimeout" title="AccountLockTimeout">AccountLockTimeout</a>" : <i>Double</i>,
        "<a href="#credentialstimeoutthreshold" title="CredentialsTimeoutThreshold">CredentialsTimeoutThreshold</a>" : <i>Double</i>,
        "<a href="#maxconcurrentsessions" title="MaxConcurrentSessions">MaxConcurrentSessions</a>" : <i>Double</i>,
        "<a href="#maxloginfailurecount" title="MaxLoginFailureCount">MaxLoginFailureCount</a>" : <i>Double</i>,
        "<a href="#maxpasswordhistorycount" title="MaxPasswordHistoryCount">MaxPasswordHistoryCount</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Useraccountprofile
Properties:
    <a href="#accountlocktimeout" title="AccountLockTimeout">AccountLockTimeout</a>: <i>Double</i>
    <a href="#credentialstimeoutthreshold" title="CredentialsTimeoutThreshold">CredentialsTimeoutThreshold</a>: <i>Double</i>
    <a href="#maxconcurrentsessions" title="MaxConcurrentSessions">MaxConcurrentSessions</a>: <i>Double</i>
    <a href="#maxloginfailurecount" title="MaxLoginFailureCount">MaxLoginFailureCount</a>: <i>Double</i>
    <a href="#maxpasswordhistorycount" title="MaxPasswordHistoryCount">MaxPasswordHistoryCount</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### AccountLockTimeout

Lock timeout period (in minutes). Default is 30 minutes. Unit is min.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CredentialsTimeoutThreshold

The time period after which credentials expire. Default is 180 days. Unit is days.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentSessions

Maximum number of concurrent sessions allowed. There are unlimited sessions by default.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLoginFailureCount

Number of login attempts before lockout. Default is 3 attempts. Allowed values are 3-20. Special values are 0 - 'unlimited login attempts allowed.'.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPasswordHistoryCount

Maximum number of passwords to be maintained in the password history. Default is 4 passwords.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

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

