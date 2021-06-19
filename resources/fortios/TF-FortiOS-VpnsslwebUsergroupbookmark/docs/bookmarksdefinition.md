# TF::FortiOS::VpnsslwebUsergroupbookmark BookmarksDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#additionalparams" title="AdditionalParams">AdditionalParams</a>" : <i>String</i>,
    "<a href="#apptype" title="Apptype">Apptype</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
    "<a href="#folder" title="Folder">Folder</a>" : <i>String</i>,
    "<a href="#host" title="Host">Host</a>" : <i>String</i>,
    "<a href="#listeningport" title="ListeningPort">ListeningPort</a>" : <i>Double</i>,
    "<a href="#loadbalancinginfo" title="LoadBalancingInfo">LoadBalancingInfo</a>" : <i>String</i>,
    "<a href="#logonpassword" title="LogonPassword">LogonPassword</a>" : <i>String</i>,
    "<a href="#logonuser" title="LogonUser">LogonUser</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#preconnectionblob" title="PreconnectionBlob">PreconnectionBlob</a>" : <i>String</i>,
    "<a href="#preconnectionid" title="PreconnectionId">PreconnectionId</a>" : <i>Double</i>,
    "<a href="#remoteport" title="RemotePort">RemotePort</a>" : <i>Double</i>,
    "<a href="#security" title="Security">Security</a>" : <i>String</i>,
    "<a href="#serverlayout" title="ServerLayout">ServerLayout</a>" : <i>String</i>,
    "<a href="#showstatuswindow" title="ShowStatusWindow">ShowStatusWindow</a>" : <i>String</i>,
    "<a href="#sso" title="Sso">Sso</a>" : <i>String</i>,
    "<a href="#ssocredential" title="SsoCredential">SsoCredential</a>" : <i>String</i>,
    "<a href="#ssocredentialsentonce" title="SsoCredentialSentOnce">SsoCredentialSentOnce</a>" : <i>String</i>,
    "<a href="#ssopassword" title="SsoPassword">SsoPassword</a>" : <i>String</i>,
    "<a href="#ssousername" title="SsoUsername">SsoUsername</a>" : <i>String</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>,
    "<a href="#formdata" title="FormData">FormData</a>" : <i>[ <a href="formdatadefinition.md">FormDataDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#additionalparams" title="AdditionalParams">AdditionalParams</a>: <i>String</i>
<a href="#apptype" title="Apptype">Apptype</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#domain" title="Domain">Domain</a>: <i>String</i>
<a href="#folder" title="Folder">Folder</a>: <i>String</i>
<a href="#host" title="Host">Host</a>: <i>String</i>
<a href="#listeningport" title="ListeningPort">ListeningPort</a>: <i>Double</i>
<a href="#loadbalancinginfo" title="LoadBalancingInfo">LoadBalancingInfo</a>: <i>String</i>
<a href="#logonpassword" title="LogonPassword">LogonPassword</a>: <i>String</i>
<a href="#logonuser" title="LogonUser">LogonUser</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#preconnectionblob" title="PreconnectionBlob">PreconnectionBlob</a>: <i>String</i>
<a href="#preconnectionid" title="PreconnectionId">PreconnectionId</a>: <i>Double</i>
<a href="#remoteport" title="RemotePort">RemotePort</a>: <i>Double</i>
<a href="#security" title="Security">Security</a>: <i>String</i>
<a href="#serverlayout" title="ServerLayout">ServerLayout</a>: <i>String</i>
<a href="#showstatuswindow" title="ShowStatusWindow">ShowStatusWindow</a>: <i>String</i>
<a href="#sso" title="Sso">Sso</a>: <i>String</i>
<a href="#ssocredential" title="SsoCredential">SsoCredential</a>: <i>String</i>
<a href="#ssocredentialsentonce" title="SsoCredentialSentOnce">SsoCredentialSentOnce</a>: <i>String</i>
<a href="#ssopassword" title="SsoPassword">SsoPassword</a>: <i>String</i>
<a href="#ssousername" title="SsoUsername">SsoUsername</a>: <i>String</i>
<a href="#url" title="Url">Url</a>: <i>String</i>
<a href="#formdata" title="FormData">FormData</a>: <i>
      - <a href="formdatadefinition.md">FormDataDefinition</a></i>
</pre>

## Properties

#### AdditionalParams

Additional parameters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Apptype

Application type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

Login domain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Folder

Network shared file folder parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

Host name/IP parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListeningPort

Listening port (0 - 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancingInfo

The load balancing information or cookie which should be provided to the connection broker.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogonPassword

Logon password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogonUser

Logon user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Bookmark name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Remote port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreconnectionBlob

An arbitrary string which identifies the RDP source.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreconnectionId

The numeric ID of the RDP source (0-2147483648).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemotePort

Remote port (0 - 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Security

Security mode for RDP connection. Valid values: `rdp`, `nla`, `tls`, `any`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerLayout

Server side keyboard layout.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowStatusWindow

Enable/disable showing of status window. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sso

Single Sign-On. Valid values: `disable`, `static`, `auto`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsoCredential

Single sign-on credentials. Valid values: `sslvpn-login`, `alternative`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsoCredentialSentOnce

Single sign-on credentials are only sent once to remote server. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsoPassword

SSO password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsoUsername

SSO user name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

URL parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FormData

_Required_: No

_Type_: List of <a href="formdatadefinition.md">FormDataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

