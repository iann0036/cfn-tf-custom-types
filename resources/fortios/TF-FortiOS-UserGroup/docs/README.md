# TF::FortiOS::UserGroup

Configure user groups.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::UserGroup",
    "Properties" : {
        "<a href="#authconcurrentoverride" title="AuthConcurrentOverride">AuthConcurrentOverride</a>" : <i>String</i>,
        "<a href="#authconcurrentvalue" title="AuthConcurrentValue">AuthConcurrentValue</a>" : <i>Double</i>,
        "<a href="#authtimeout" title="Authtimeout">Authtimeout</a>" : <i>Double</i>,
        "<a href="#company" title="Company">Company</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#expire" title="Expire">Expire</a>" : <i>Double</i>,
        "<a href="#expiretype" title="ExpireType">ExpireType</a>" : <i>String</i>,
        "<a href="#fosid" title="Fosid">Fosid</a>" : <i>Double</i>,
        "<a href="#grouptype" title="GroupType">GroupType</a>" : <i>String</i>,
        "<a href="#httpdigestrealm" title="HttpDigestRealm">HttpDigestRealm</a>" : <i>String</i>,
        "<a href="#maxaccounts" title="MaxAccounts">MaxAccounts</a>" : <i>Double</i>,
        "<a href="#mobilephone" title="MobilePhone">MobilePhone</a>" : <i>String</i>,
        "<a href="#multipleguestadd" title="MultipleGuestAdd">MultipleGuestAdd</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#smscustomserver" title="SmsCustomServer">SmsCustomServer</a>" : <i>String</i>,
        "<a href="#smsserver" title="SmsServer">SmsServer</a>" : <i>String</i>,
        "<a href="#sponsor" title="Sponsor">Sponsor</a>" : <i>String</i>,
        "<a href="#ssoattributevalue" title="SsoAttributeValue">SsoAttributeValue</a>" : <i>String</i>,
        "<a href="#userid" title="UserId">UserId</a>" : <i>String</i>,
        "<a href="#username" title="UserName">UserName</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#guest" title="Guest">Guest</a>" : <i>[ <a href="guestdefinition.md">GuestDefinition</a>, ... ]</i>,
        "<a href="#match" title="Match">Match</a>" : <i>[ <a href="matchdefinition.md">MatchDefinition</a>, ... ]</i>,
        "<a href="#member" title="Member">Member</a>" : <i>[ <a href="memberdefinition.md">MemberDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::UserGroup
Properties:
    <a href="#authconcurrentoverride" title="AuthConcurrentOverride">AuthConcurrentOverride</a>: <i>String</i>
    <a href="#authconcurrentvalue" title="AuthConcurrentValue">AuthConcurrentValue</a>: <i>Double</i>
    <a href="#authtimeout" title="Authtimeout">Authtimeout</a>: <i>Double</i>
    <a href="#company" title="Company">Company</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#expire" title="Expire">Expire</a>: <i>Double</i>
    <a href="#expiretype" title="ExpireType">ExpireType</a>: <i>String</i>
    <a href="#fosid" title="Fosid">Fosid</a>: <i>Double</i>
    <a href="#grouptype" title="GroupType">GroupType</a>: <i>String</i>
    <a href="#httpdigestrealm" title="HttpDigestRealm">HttpDigestRealm</a>: <i>String</i>
    <a href="#maxaccounts" title="MaxAccounts">MaxAccounts</a>: <i>Double</i>
    <a href="#mobilephone" title="MobilePhone">MobilePhone</a>: <i>String</i>
    <a href="#multipleguestadd" title="MultipleGuestAdd">MultipleGuestAdd</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#smscustomserver" title="SmsCustomServer">SmsCustomServer</a>: <i>String</i>
    <a href="#smsserver" title="SmsServer">SmsServer</a>: <i>String</i>
    <a href="#sponsor" title="Sponsor">Sponsor</a>: <i>String</i>
    <a href="#ssoattributevalue" title="SsoAttributeValue">SsoAttributeValue</a>: <i>String</i>
    <a href="#userid" title="UserId">UserId</a>: <i>String</i>
    <a href="#username" title="UserName">UserName</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#guest" title="Guest">Guest</a>: <i>
      - <a href="guestdefinition.md">GuestDefinition</a></i>
    <a href="#match" title="Match">Match</a>: <i>
      - <a href="matchdefinition.md">MatchDefinition</a></i>
    <a href="#member" title="Member">Member</a>: <i>
      - <a href="memberdefinition.md">MemberDefinition</a></i>
</pre>

## Properties

#### AuthConcurrentOverride

Enable/disable overriding the global number of concurrent authentication sessions for this user group. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthConcurrentValue

Maximum number of concurrent authenticated connections per user (0 - 100).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authtimeout

Authentication timeout in minutes for this user group. 0 to use the global user setting auth-timeout.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Company

Set the action for the company guest user field. Valid values: `optional`, `mandatory`, `disabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

Enable/disable the guest user email address field. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expire

Time in seconds before guest user accounts expire. (1 - 31536000 sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpireType

Determine when the expiration countdown begins. Valid values: `immediately`, `first-successful-login`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fosid

Group ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupType

Set the group to be for firewall authentication, FSSO, RSSO, or guest users. Valid values: `firewall`, `fsso-service`, `rsso`, `guest`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpDigestRealm

Realm attribute for MD5-digest authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxAccounts

Maximum number of guest accounts that can be created for this group (0 means unlimited).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MobilePhone

Enable/disable the guest user mobile phone number field. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultipleGuestAdd

Enable/disable addition of multiple guests. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Group name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Guest user password type. Valid values: `auto-generate`, `specify`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsCustomServer

SMS server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsServer

Send SMS through FortiGuard or other external server. Valid values: `fortiguard`, `custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sponsor

Set the action for the sponsor guest user field. Valid values: `optional`, `mandatory`, `disabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsoAttributeValue

Name of the RADIUS user group that this local user group represents.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserId

Guest user ID type. Valid values: `email`, `auto-generate`, `specify`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserName

Enable/disable the guest user name entry. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Guest

_Required_: No

_Type_: List of <a href="guestdefinition.md">GuestDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

_Required_: No

_Type_: List of <a href="matchdefinition.md">MatchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Member

_Required_: No

_Type_: List of <a href="memberdefinition.md">MemberDefinition</a>

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

