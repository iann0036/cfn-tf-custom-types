# TF::FortiOS::UserLdap

Configure LDAP server entries.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::UserLdap",
    "Properties" : {
        "<a href="#accountkeyfilter" title="AccountKeyFilter">AccountKeyFilter</a>" : <i>String</i>,
        "<a href="#accountkeyprocessing" title="AccountKeyProcessing">AccountKeyProcessing</a>" : <i>String</i>,
        "<a href="#cacert" title="CaCert">CaCert</a>" : <i>String</i>,
        "<a href="#cnid" title="Cnid">Cnid</a>" : <i>String</i>,
        "<a href="#dn" title="Dn">Dn</a>" : <i>String</i>,
        "<a href="#groupfilter" title="GroupFilter">GroupFilter</a>" : <i>String</i>,
        "<a href="#groupmembercheck" title="GroupMemberCheck">GroupMemberCheck</a>" : <i>String</i>,
        "<a href="#groupobjectfilter" title="GroupObjectFilter">GroupObjectFilter</a>" : <i>String</i>,
        "<a href="#groupsearchbase" title="GroupSearchBase">GroupSearchBase</a>" : <i>String</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>" : <i>String</i>,
        "<a href="#memberattr" title="MemberAttr">MemberAttr</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#obtainuserinfo" title="ObtainUserInfo">ObtainUserInfo</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#passwordexpirywarning" title="PasswordExpiryWarning">PasswordExpiryWarning</a>" : <i>String</i>,
        "<a href="#passwordrenewal" title="PasswordRenewal">PasswordRenewal</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#searchtype" title="SearchType">SearchType</a>" : <i>String</i>,
        "<a href="#secondaryserver" title="SecondaryServer">SecondaryServer</a>" : <i>String</i>,
        "<a href="#secure" title="Secure">Secure</a>" : <i>String</i>,
        "<a href="#server" title="Server">Server</a>" : <i>String</i>,
        "<a href="#serveridentitycheck" title="ServerIdentityCheck">ServerIdentityCheck</a>" : <i>String</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
        "<a href="#sslminprotoversion" title="SslMinProtoVersion">SslMinProtoVersion</a>" : <i>String</i>,
        "<a href="#tertiaryserver" title="TertiaryServer">TertiaryServer</a>" : <i>String</i>,
        "<a href="#twofactor" title="TwoFactor">TwoFactor</a>" : <i>String</i>,
        "<a href="#twofactorauthentication" title="TwoFactorAuthentication">TwoFactorAuthentication</a>" : <i>String</i>,
        "<a href="#twofactornotification" title="TwoFactorNotification">TwoFactorNotification</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#userinfoexchangeserver" title="UserInfoExchangeServer">UserInfoExchangeServer</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::UserLdap
Properties:
    <a href="#accountkeyfilter" title="AccountKeyFilter">AccountKeyFilter</a>: <i>String</i>
    <a href="#accountkeyprocessing" title="AccountKeyProcessing">AccountKeyProcessing</a>: <i>String</i>
    <a href="#cacert" title="CaCert">CaCert</a>: <i>String</i>
    <a href="#cnid" title="Cnid">Cnid</a>: <i>String</i>
    <a href="#dn" title="Dn">Dn</a>: <i>String</i>
    <a href="#groupfilter" title="GroupFilter">GroupFilter</a>: <i>String</i>
    <a href="#groupmembercheck" title="GroupMemberCheck">GroupMemberCheck</a>: <i>String</i>
    <a href="#groupobjectfilter" title="GroupObjectFilter">GroupObjectFilter</a>: <i>String</i>
    <a href="#groupsearchbase" title="GroupSearchBase">GroupSearchBase</a>: <i>String</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>: <i>String</i>
    <a href="#memberattr" title="MemberAttr">MemberAttr</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#obtainuserinfo" title="ObtainUserInfo">ObtainUserInfo</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#passwordexpirywarning" title="PasswordExpiryWarning">PasswordExpiryWarning</a>: <i>String</i>
    <a href="#passwordrenewal" title="PasswordRenewal">PasswordRenewal</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#searchtype" title="SearchType">SearchType</a>: <i>String</i>
    <a href="#secondaryserver" title="SecondaryServer">SecondaryServer</a>: <i>String</i>
    <a href="#secure" title="Secure">Secure</a>: <i>String</i>
    <a href="#server" title="Server">Server</a>: <i>String</i>
    <a href="#serveridentitycheck" title="ServerIdentityCheck">ServerIdentityCheck</a>: <i>String</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
    <a href="#sslminprotoversion" title="SslMinProtoVersion">SslMinProtoVersion</a>: <i>String</i>
    <a href="#tertiaryserver" title="TertiaryServer">TertiaryServer</a>: <i>String</i>
    <a href="#twofactor" title="TwoFactor">TwoFactor</a>: <i>String</i>
    <a href="#twofactorauthentication" title="TwoFactorAuthentication">TwoFactorAuthentication</a>: <i>String</i>
    <a href="#twofactornotification" title="TwoFactorNotification">TwoFactorNotification</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#userinfoexchangeserver" title="UserInfoExchangeServer">UserInfoExchangeServer</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### AccountKeyFilter

Account key filter, using the UPN as the search filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountKeyProcessing

Account key processing operation, either keep or strip domain string of UPN in the token. Valid values: `same`, `strip`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaCert

CA certificate name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cnid

Common name identifier for the LDAP server. The common name identifier for most LDAP servers is "cn".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dn

Distinguished name used to look up entries on the LDAP server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupFilter

Filter used for group matching.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupMemberCheck

Group member checking methods. Valid values: `user-attr`, `group-object`, `posix-group-object`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupObjectFilter

Filter used for group searching.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupSearchBase

Search base used for group searching.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Specify outgoing interface to reach server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceSelectMethod

Specify how to select outgoing interface to reach server. Valid values: `auto`, `sdwan`, `specify`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberAttr

Name of attribute from which to get group membership.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

LDAP server entry name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObtainUserInfo

Enable/disable obtaining of user information. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password for initial binding.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordExpiryWarning

Enable/disable password expiry warnings. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordRenewal

Enable/disable online password renewal. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Port to be used for communication with the LDAP server (default = 389).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchType

Search type. Valid values: `recursive`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryServer

Secondary LDAP server CN domain name or IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secure

Port to be used for authentication. Valid values: `disable`, `starttls`, `ldaps`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

LDAP server CN domain name or IP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerIdentityCheck

Enable/disable LDAP server identity check (verify server domain name/IP address against the server certificate). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

Source IP for communications to LDAP server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMinProtoVersion

Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting). Valid values: `default`, `SSLv3`, `TLSv1`, `TLSv1-1`, `TLSv1-2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TertiaryServer

Tertiary LDAP server CN domain name or IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TwoFactor

Enable/disable two-factor authentication. Valid values: `disable`, `fortitoken-cloud`.

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

Authentication type for LDAP searches. Valid values: `simple`, `anonymous`, `regular`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserInfoExchangeServer

MS Exchange server from which to fetch user information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

Username (full DN) for initial binding.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

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

