# TF::FortiOS::UserLocal

Configure local users.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::UserLocal",
    "Properties" : {
        "<a href="#authconcurrentoverride" title="AuthConcurrentOverride">AuthConcurrentOverride</a>" : <i>String</i>,
        "<a href="#authconcurrentvalue" title="AuthConcurrentValue">AuthConcurrentValue</a>" : <i>Double</i>,
        "<a href="#authtimeout" title="Authtimeout">Authtimeout</a>" : <i>Double</i>,
        "<a href="#emailto" title="EmailTo">EmailTo</a>" : <i>String</i>,
        "<a href="#fortitoken" title="Fortitoken">Fortitoken</a>" : <i>String</i>,
        "<a href="#fosid" title="Fosid">Fosid</a>" : <i>Double</i>,
        "<a href="#ldapserver" title="LdapServer">LdapServer</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#passwd" title="Passwd">Passwd</a>" : <i>String</i>,
        "<a href="#passwdpolicy" title="PasswdPolicy">PasswdPolicy</a>" : <i>String</i>,
        "<a href="#passwdtime" title="PasswdTime">PasswdTime</a>" : <i>String</i>,
        "<a href="#ppkidentity" title="PpkIdentity">PpkIdentity</a>" : <i>String</i>,
        "<a href="#ppksecret" title="PpkSecret">PpkSecret</a>" : <i>String</i>,
        "<a href="#radiusserver" title="RadiusServer">RadiusServer</a>" : <i>String</i>,
        "<a href="#smscustomserver" title="SmsCustomServer">SmsCustomServer</a>" : <i>String</i>,
        "<a href="#smsphone" title="SmsPhone">SmsPhone</a>" : <i>String</i>,
        "<a href="#smsserver" title="SmsServer">SmsServer</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#tacacsserver" title="TacacsServer">TacacsServer</a>" : <i>String</i>,
        "<a href="#twofactor" title="TwoFactor">TwoFactor</a>" : <i>String</i>,
        "<a href="#twofactorauthentication" title="TwoFactorAuthentication">TwoFactorAuthentication</a>" : <i>String</i>,
        "<a href="#twofactornotification" title="TwoFactorNotification">TwoFactorNotification</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#usernamecaseinsensitivity" title="UsernameCaseInsensitivity">UsernameCaseInsensitivity</a>" : <i>String</i>,
        "<a href="#usernamecasesensitivity" title="UsernameCaseSensitivity">UsernameCaseSensitivity</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#workstation" title="Workstation">Workstation</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::UserLocal
Properties:
    <a href="#authconcurrentoverride" title="AuthConcurrentOverride">AuthConcurrentOverride</a>: <i>String</i>
    <a href="#authconcurrentvalue" title="AuthConcurrentValue">AuthConcurrentValue</a>: <i>Double</i>
    <a href="#authtimeout" title="Authtimeout">Authtimeout</a>: <i>Double</i>
    <a href="#emailto" title="EmailTo">EmailTo</a>: <i>String</i>
    <a href="#fortitoken" title="Fortitoken">Fortitoken</a>: <i>String</i>
    <a href="#fosid" title="Fosid">Fosid</a>: <i>Double</i>
    <a href="#ldapserver" title="LdapServer">LdapServer</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#passwd" title="Passwd">Passwd</a>: <i>String</i>
    <a href="#passwdpolicy" title="PasswdPolicy">PasswdPolicy</a>: <i>String</i>
    <a href="#passwdtime" title="PasswdTime">PasswdTime</a>: <i>String</i>
    <a href="#ppkidentity" title="PpkIdentity">PpkIdentity</a>: <i>String</i>
    <a href="#ppksecret" title="PpkSecret">PpkSecret</a>: <i>String</i>
    <a href="#radiusserver" title="RadiusServer">RadiusServer</a>: <i>String</i>
    <a href="#smscustomserver" title="SmsCustomServer">SmsCustomServer</a>: <i>String</i>
    <a href="#smsphone" title="SmsPhone">SmsPhone</a>: <i>String</i>
    <a href="#smsserver" title="SmsServer">SmsServer</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#tacacsserver" title="TacacsServer">TacacsServer</a>: <i>String</i>
    <a href="#twofactor" title="TwoFactor">TwoFactor</a>: <i>String</i>
    <a href="#twofactorauthentication" title="TwoFactorAuthentication">TwoFactorAuthentication</a>: <i>String</i>
    <a href="#twofactornotification" title="TwoFactorNotification">TwoFactorNotification</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#usernamecaseinsensitivity" title="UsernameCaseInsensitivity">UsernameCaseInsensitivity</a>: <i>String</i>
    <a href="#usernamecasesensitivity" title="UsernameCaseSensitivity">UsernameCaseSensitivity</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#workstation" title="Workstation">Workstation</a>: <i>String</i>
</pre>

## Properties

#### AuthConcurrentOverride

Enable/disable overriding the policy-auth-concurrent under config system global. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthConcurrentValue

Maximum number of concurrent logins permitted from the same user.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authtimeout

Time in minutes before the authentication timeout for a user is reached.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailTo

Two-factor recipient's email address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fortitoken

Two-factor recipient's FortiToken serial number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fosid

User ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapServer

Name of LDAP server with which the user must authenticate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

User name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Passwd

User's password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswdPolicy

Password policy to apply to this user, as defined in config user password-policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswdTime

Time of the last password update.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PpkIdentity

IKEv2 Postquantum Preshared Key Identity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PpkSecret

IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal encoded with a leading 0x).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusServer

Name of RADIUS server with which the user must authenticate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsCustomServer

Two-factor recipient's SMS server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsPhone

Two-factor recipient's mobile phone number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsServer

Send SMS through FortiGuard or other external server. Valid values: `fortiguard`, `custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable allowing the local user to authenticate with the FortiGate unit. Valid values: `enable`, `disable`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TacacsServer

Name of TACACS+ server with which the user must authenticate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TwoFactor

Enable/disable two-factor authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TwoFactorAuthentication

Authentication method by FortiToken Cloud. Valid values: `fortitoken`, `email`, `sms`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TwoFactorNotification

Notification method for user activation by FortiToken Cloud. Valid values: `email`, `sms`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Authentication method. Valid values: `password`, `radius`, `tacacs+`, `ldap`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsernameCaseInsensitivity

Enable/disable case sensitivity when performing username matching (uppercase and lowercase letters are treated either as distinct or equivalent). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsernameCaseSensitivity

Enable/disable case sensitivity when performing username matching (uppercase and lowercase letters are treated either as distinct or equivalent). Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Workstation

Name of the remote user workstation, if you want to limit the user to authenticate only from a particular workstation.

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

