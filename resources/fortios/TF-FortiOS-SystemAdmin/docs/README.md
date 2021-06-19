# TF::FortiOS::SystemAdmin

Configure admin users.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemAdmin",
    "Properties" : {
        "<a href="#accprofile" title="Accprofile">Accprofile</a>" : <i>String</i>,
        "<a href="#accprofileoverride" title="AccprofileOverride">AccprofileOverride</a>" : <i>String</i>,
        "<a href="#allowremoveadminsession" title="AllowRemoveAdminSession">AllowRemoveAdminSession</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#emailto" title="EmailTo">EmailTo</a>" : <i>String</i>,
        "<a href="#forcepasswordchange" title="ForcePasswordChange">ForcePasswordChange</a>" : <i>String</i>,
        "<a href="#fortitoken" title="Fortitoken">Fortitoken</a>" : <i>String</i>,
        "<a href="#guestauth" title="GuestAuth">GuestAuth</a>" : <i>String</i>,
        "<a href="#guestlang" title="GuestLang">GuestLang</a>" : <i>String</i>,
        "<a href="#hidden" title="Hidden">Hidden</a>" : <i>Double</i>,
        "<a href="#history0" title="History0">History0</a>" : <i>String</i>,
        "<a href="#history1" title="History1">History1</a>" : <i>String</i>,
        "<a href="#ip6trusthost1" title="Ip6Trusthost1">Ip6Trusthost1</a>" : <i>String</i>,
        "<a href="#ip6trusthost10" title="Ip6Trusthost10">Ip6Trusthost10</a>" : <i>String</i>,
        "<a href="#ip6trusthost2" title="Ip6Trusthost2">Ip6Trusthost2</a>" : <i>String</i>,
        "<a href="#ip6trusthost3" title="Ip6Trusthost3">Ip6Trusthost3</a>" : <i>String</i>,
        "<a href="#ip6trusthost4" title="Ip6Trusthost4">Ip6Trusthost4</a>" : <i>String</i>,
        "<a href="#ip6trusthost5" title="Ip6Trusthost5">Ip6Trusthost5</a>" : <i>String</i>,
        "<a href="#ip6trusthost6" title="Ip6Trusthost6">Ip6Trusthost6</a>" : <i>String</i>,
        "<a href="#ip6trusthost7" title="Ip6Trusthost7">Ip6Trusthost7</a>" : <i>String</i>,
        "<a href="#ip6trusthost8" title="Ip6Trusthost8">Ip6Trusthost8</a>" : <i>String</i>,
        "<a href="#ip6trusthost9" title="Ip6Trusthost9">Ip6Trusthost9</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#passwordexpire" title="PasswordExpire">PasswordExpire</a>" : <i>String</i>,
        "<a href="#peerauth" title="PeerAuth">PeerAuth</a>" : <i>String</i>,
        "<a href="#peergroup" title="PeerGroup">PeerGroup</a>" : <i>String</i>,
        "<a href="#radiusvdomoverride" title="RadiusVdomOverride">RadiusVdomOverride</a>" : <i>String</i>,
        "<a href="#remoteauth" title="RemoteAuth">RemoteAuth</a>" : <i>String</i>,
        "<a href="#remotegroup" title="RemoteGroup">RemoteGroup</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
        "<a href="#smscustomserver" title="SmsCustomServer">SmsCustomServer</a>" : <i>String</i>,
        "<a href="#smsphone" title="SmsPhone">SmsPhone</a>" : <i>String</i>,
        "<a href="#smsserver" title="SmsServer">SmsServer</a>" : <i>String</i>,
        "<a href="#sshcertificate" title="SshCertificate">SshCertificate</a>" : <i>String</i>,
        "<a href="#sshpublickey1" title="SshPublicKey1">SshPublicKey1</a>" : <i>String</i>,
        "<a href="#sshpublickey2" title="SshPublicKey2">SshPublicKey2</a>" : <i>String</i>,
        "<a href="#sshpublickey3" title="SshPublicKey3">SshPublicKey3</a>" : <i>String</i>,
        "<a href="#trusthost1" title="Trusthost1">Trusthost1</a>" : <i>String</i>,
        "<a href="#trusthost10" title="Trusthost10">Trusthost10</a>" : <i>String</i>,
        "<a href="#trusthost2" title="Trusthost2">Trusthost2</a>" : <i>String</i>,
        "<a href="#trusthost3" title="Trusthost3">Trusthost3</a>" : <i>String</i>,
        "<a href="#trusthost4" title="Trusthost4">Trusthost4</a>" : <i>String</i>,
        "<a href="#trusthost5" title="Trusthost5">Trusthost5</a>" : <i>String</i>,
        "<a href="#trusthost6" title="Trusthost6">Trusthost6</a>" : <i>String</i>,
        "<a href="#trusthost7" title="Trusthost7">Trusthost7</a>" : <i>String</i>,
        "<a href="#trusthost8" title="Trusthost8">Trusthost8</a>" : <i>String</i>,
        "<a href="#trusthost9" title="Trusthost9">Trusthost9</a>" : <i>String</i>,
        "<a href="#twofactor" title="TwoFactor">TwoFactor</a>" : <i>String</i>,
        "<a href="#twofactorauthentication" title="TwoFactorAuthentication">TwoFactorAuthentication</a>" : <i>String</i>,
        "<a href="#twofactornotification" title="TwoFactorNotification">TwoFactorNotification</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#wildcard" title="Wildcard">Wildcard</a>" : <i>String</i>,
        "<a href="#guestusergroups" title="GuestUsergroups">GuestUsergroups</a>" : <i>[ <a href="guestusergroupsdefinition.md">GuestUsergroupsDefinition</a>, ... ]</i>,
        "<a href="#guidashboard" title="GuiDashboard">GuiDashboard</a>" : <i>[ <a href="guidashboarddefinition.md">GuiDashboardDefinition</a>, ... ]</i>,
        "<a href="#guiglobalmenufavorites" title="GuiGlobalMenuFavorites">GuiGlobalMenuFavorites</a>" : <i>[ <a href="guiglobalmenufavoritesdefinition.md">GuiGlobalMenuFavoritesDefinition</a>, ... ]</i>,
        "<a href="#guinewfeatureacknowledge" title="GuiNewFeatureAcknowledge">GuiNewFeatureAcknowledge</a>" : <i>[ <a href="guinewfeatureacknowledgedefinition.md">GuiNewFeatureAcknowledgeDefinition</a>, ... ]</i>,
        "<a href="#guivdommenufavorites" title="GuiVdomMenuFavorites">GuiVdomMenuFavorites</a>" : <i>[ <a href="guivdommenufavoritesdefinition.md">GuiVdomMenuFavoritesDefinition</a>, ... ]</i>,
        "<a href="#logintime" title="LoginTime">LoginTime</a>" : <i>[ <a href="logintimedefinition.md">LoginTimeDefinition</a>, ... ]</i>,
        "<a href="#vdom" title="Vdom">Vdom</a>" : <i>[ <a href="vdomdefinition.md">VdomDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemAdmin
Properties:
    <a href="#accprofile" title="Accprofile">Accprofile</a>: <i>String</i>
    <a href="#accprofileoverride" title="AccprofileOverride">AccprofileOverride</a>: <i>String</i>
    <a href="#allowremoveadminsession" title="AllowRemoveAdminSession">AllowRemoveAdminSession</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#emailto" title="EmailTo">EmailTo</a>: <i>String</i>
    <a href="#forcepasswordchange" title="ForcePasswordChange">ForcePasswordChange</a>: <i>String</i>
    <a href="#fortitoken" title="Fortitoken">Fortitoken</a>: <i>String</i>
    <a href="#guestauth" title="GuestAuth">GuestAuth</a>: <i>String</i>
    <a href="#guestlang" title="GuestLang">GuestLang</a>: <i>String</i>
    <a href="#hidden" title="Hidden">Hidden</a>: <i>Double</i>
    <a href="#history0" title="History0">History0</a>: <i>String</i>
    <a href="#history1" title="History1">History1</a>: <i>String</i>
    <a href="#ip6trusthost1" title="Ip6Trusthost1">Ip6Trusthost1</a>: <i>String</i>
    <a href="#ip6trusthost10" title="Ip6Trusthost10">Ip6Trusthost10</a>: <i>String</i>
    <a href="#ip6trusthost2" title="Ip6Trusthost2">Ip6Trusthost2</a>: <i>String</i>
    <a href="#ip6trusthost3" title="Ip6Trusthost3">Ip6Trusthost3</a>: <i>String</i>
    <a href="#ip6trusthost4" title="Ip6Trusthost4">Ip6Trusthost4</a>: <i>String</i>
    <a href="#ip6trusthost5" title="Ip6Trusthost5">Ip6Trusthost5</a>: <i>String</i>
    <a href="#ip6trusthost6" title="Ip6Trusthost6">Ip6Trusthost6</a>: <i>String</i>
    <a href="#ip6trusthost7" title="Ip6Trusthost7">Ip6Trusthost7</a>: <i>String</i>
    <a href="#ip6trusthost8" title="Ip6Trusthost8">Ip6Trusthost8</a>: <i>String</i>
    <a href="#ip6trusthost9" title="Ip6Trusthost9">Ip6Trusthost9</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#passwordexpire" title="PasswordExpire">PasswordExpire</a>: <i>String</i>
    <a href="#peerauth" title="PeerAuth">PeerAuth</a>: <i>String</i>
    <a href="#peergroup" title="PeerGroup">PeerGroup</a>: <i>String</i>
    <a href="#radiusvdomoverride" title="RadiusVdomOverride">RadiusVdomOverride</a>: <i>String</i>
    <a href="#remoteauth" title="RemoteAuth">RemoteAuth</a>: <i>String</i>
    <a href="#remotegroup" title="RemoteGroup">RemoteGroup</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
    <a href="#smscustomserver" title="SmsCustomServer">SmsCustomServer</a>: <i>String</i>
    <a href="#smsphone" title="SmsPhone">SmsPhone</a>: <i>String</i>
    <a href="#smsserver" title="SmsServer">SmsServer</a>: <i>String</i>
    <a href="#sshcertificate" title="SshCertificate">SshCertificate</a>: <i>String</i>
    <a href="#sshpublickey1" title="SshPublicKey1">SshPublicKey1</a>: <i>String</i>
    <a href="#sshpublickey2" title="SshPublicKey2">SshPublicKey2</a>: <i>String</i>
    <a href="#sshpublickey3" title="SshPublicKey3">SshPublicKey3</a>: <i>String</i>
    <a href="#trusthost1" title="Trusthost1">Trusthost1</a>: <i>String</i>
    <a href="#trusthost10" title="Trusthost10">Trusthost10</a>: <i>String</i>
    <a href="#trusthost2" title="Trusthost2">Trusthost2</a>: <i>String</i>
    <a href="#trusthost3" title="Trusthost3">Trusthost3</a>: <i>String</i>
    <a href="#trusthost4" title="Trusthost4">Trusthost4</a>: <i>String</i>
    <a href="#trusthost5" title="Trusthost5">Trusthost5</a>: <i>String</i>
    <a href="#trusthost6" title="Trusthost6">Trusthost6</a>: <i>String</i>
    <a href="#trusthost7" title="Trusthost7">Trusthost7</a>: <i>String</i>
    <a href="#trusthost8" title="Trusthost8">Trusthost8</a>: <i>String</i>
    <a href="#trusthost9" title="Trusthost9">Trusthost9</a>: <i>String</i>
    <a href="#twofactor" title="TwoFactor">TwoFactor</a>: <i>String</i>
    <a href="#twofactorauthentication" title="TwoFactorAuthentication">TwoFactorAuthentication</a>: <i>String</i>
    <a href="#twofactornotification" title="TwoFactorNotification">TwoFactorNotification</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#wildcard" title="Wildcard">Wildcard</a>: <i>String</i>
    <a href="#guestusergroups" title="GuestUsergroups">GuestUsergroups</a>: <i>
      - <a href="guestusergroupsdefinition.md">GuestUsergroupsDefinition</a></i>
    <a href="#guidashboard" title="GuiDashboard">GuiDashboard</a>: <i>
      - <a href="guidashboarddefinition.md">GuiDashboardDefinition</a></i>
    <a href="#guiglobalmenufavorites" title="GuiGlobalMenuFavorites">GuiGlobalMenuFavorites</a>: <i>
      - <a href="guiglobalmenufavoritesdefinition.md">GuiGlobalMenuFavoritesDefinition</a></i>
    <a href="#guinewfeatureacknowledge" title="GuiNewFeatureAcknowledge">GuiNewFeatureAcknowledge</a>: <i>
      - <a href="guinewfeatureacknowledgedefinition.md">GuiNewFeatureAcknowledgeDefinition</a></i>
    <a href="#guivdommenufavorites" title="GuiVdomMenuFavorites">GuiVdomMenuFavorites</a>: <i>
      - <a href="guivdommenufavoritesdefinition.md">GuiVdomMenuFavoritesDefinition</a></i>
    <a href="#logintime" title="LoginTime">LoginTime</a>: <i>
      - <a href="logintimedefinition.md">LoginTimeDefinition</a></i>
    <a href="#vdom" title="Vdom">Vdom</a>: <i>
      - <a href="vdomdefinition.md">VdomDefinition</a></i>
</pre>

## Properties

#### Accprofile

Access profile for this administrator. Access profiles control administrator access to FortiGate features.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccprofileOverride

Enable to use the name of an access profile provided by the remote authentication server to control the FortiGate features that this administrator can access. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowRemoveAdminSession

Enable/disable allow admin session to be removed by privileged admin users. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailTo

This administrator's email address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForcePasswordChange

Enable/disable force password change on next login. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fortitoken

This administrator's FortiToken serial number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestAuth

Enable/disable guest authentication. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestLang

Guest management portal language.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hidden

Admin user hidden attribute.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### History0

history0.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### History1

history1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6Trusthost1

Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6Trusthost10

Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6Trusthost2

Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6Trusthost3

Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6Trusthost4

Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6Trusthost5

Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6Trusthost6

Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6Trusthost7

Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6Trusthost8

Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6Trusthost9

Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

User name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Admin user password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordExpire

Password expire time.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAuth

Set to enable peer certificate authentication (for HTTPS admin access). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerGroup

Name of peer group defined under config user group which has PKI members. Used for peer certificate authentication (for HTTPS admin access).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusVdomOverride

Enable to use the names of VDOMs provided by the remote authentication server to control the VDOMs that this administrator can access. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteAuth

Enable/disable authentication using a remote RADIUS, LDAP, or TACACS+ server. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteGroup

User group name used for remote auth.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

Firewall schedule used to restrict when the administrator can log in. No schedule means no restrictions.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsCustomServer

Custom SMS server to send SMS messages to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsPhone

Phone number on which the administrator receives SMS messages.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsServer

Send SMS messages using the FortiGuard SMS server or a custom server. Valid values: `fortiguard`, `custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshCertificate

Select the certificate to be used by the FortiGate for authentication with an SSH client.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPublicKey1

Public key of an SSH client. The client is authenticated without being asked for credentials. Create the public-private key pair in the SSH client application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPublicKey2

Public key of an SSH client. The client is authenticated without being asked for credentials. Create the public-private key pair in the SSH client application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPublicKey3

Public key of an SSH client. The client is authenticated without being asked for credentials. Create the public-private key pair in the SSH client application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost1

Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost10

Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost2

Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost3

Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost4

Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost5

Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost6

Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost7

Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost8

Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost9

Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.

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

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wildcard

Enable/disable wildcard RADIUS authentication. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestUsergroups

_Required_: No

_Type_: List of <a href="guestusergroupsdefinition.md">GuestUsergroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiDashboard

_Required_: No

_Type_: List of <a href="guidashboarddefinition.md">GuiDashboardDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiGlobalMenuFavorites

_Required_: No

_Type_: List of <a href="guiglobalmenufavoritesdefinition.md">GuiGlobalMenuFavoritesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiNewFeatureAcknowledge

_Required_: No

_Type_: List of <a href="guinewfeatureacknowledgedefinition.md">GuiNewFeatureAcknowledgeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuiVdomMenuFavorites

_Required_: No

_Type_: List of <a href="guivdommenufavoritesdefinition.md">GuiVdomMenuFavoritesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoginTime

_Required_: No

_Type_: List of <a href="logintimedefinition.md">LoginTimeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdom

_Required_: No

_Type_: List of <a href="vdomdefinition.md">VdomDefinition</a>

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

