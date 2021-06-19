# TF::AVI::Authprofile LdapDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#basedn" title="BaseDn">BaseDn</a>" : <i>String</i>,
    "<a href="#bindasadministrator" title="BindAsAdministrator">BindAsAdministrator</a>" : <i>Boolean</i>,
    "<a href="#emailattribute" title="EmailAttribute">EmailAttribute</a>" : <i>String</i>,
    "<a href="#fullnameattribute" title="FullNameAttribute">FullNameAttribute</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#securitymode" title="SecurityMode">SecurityMode</a>" : <i>String</i>,
    "<a href="#server" title="Server">Server</a>" : <i>[ String, ... ]</i>,
    "<a href="#settings" title="Settings">Settings</a>" : <i>[ <a href="settingsdefinition.md">SettingsDefinition</a>, ... ]</i>,
    "<a href="#userbind" title="UserBind">UserBind</a>" : <i>[ <a href="userbinddefinition.md">UserBindDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#basedn" title="BaseDn">BaseDn</a>: <i>String</i>
<a href="#bindasadministrator" title="BindAsAdministrator">BindAsAdministrator</a>: <i>Boolean</i>
<a href="#emailattribute" title="EmailAttribute">EmailAttribute</a>: <i>String</i>
<a href="#fullnameattribute" title="FullNameAttribute">FullNameAttribute</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#securitymode" title="SecurityMode">SecurityMode</a>: <i>String</i>
<a href="#server" title="Server">Server</a>: <i>
      - String</i>
<a href="#settings" title="Settings">Settings</a>: <i>
      - <a href="settingsdefinition.md">SettingsDefinition</a></i>
<a href="#userbind" title="UserBind">UserBind</a>: <i>
      - <a href="userbinddefinition.md">UserBindDefinition</a></i>
</pre>

## Properties

#### BaseDn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BindAsAdministrator

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullNameAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Settings

_Required_: No

_Type_: List of <a href="settingsdefinition.md">SettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserBind

_Required_: No

_Type_: List of <a href="userbinddefinition.md">UserBindDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

