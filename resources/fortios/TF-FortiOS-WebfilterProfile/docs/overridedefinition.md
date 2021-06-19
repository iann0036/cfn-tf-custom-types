# TF::FortiOS::WebfilterProfile OverrideDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ovrdcookie" title="OvrdCookie">OvrdCookie</a>" : <i>String</i>,
    "<a href="#ovrddur" title="OvrdDur">OvrdDur</a>" : <i>String</i>,
    "<a href="#ovrddurmode" title="OvrdDurMode">OvrdDurMode</a>" : <i>String</i>,
    "<a href="#ovrdscope" title="OvrdScope">OvrdScope</a>" : <i>String</i>,
    "<a href="#profileattribute" title="ProfileAttribute">ProfileAttribute</a>" : <i>String</i>,
    "<a href="#profiletype" title="ProfileType">ProfileType</a>" : <i>String</i>,
    "<a href="#ovrdusergroup" title="OvrdUserGroup">OvrdUserGroup</a>" : <i>[ <a href="ovrdusergroupdefinition.md">OvrdUserGroupDefinition</a>, ... ]</i>,
    "<a href="#profile" title="Profile">Profile</a>" : <i>[ <a href="profiledefinition.md">ProfileDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ovrdcookie" title="OvrdCookie">OvrdCookie</a>: <i>String</i>
<a href="#ovrddur" title="OvrdDur">OvrdDur</a>: <i>String</i>
<a href="#ovrddurmode" title="OvrdDurMode">OvrdDurMode</a>: <i>String</i>
<a href="#ovrdscope" title="OvrdScope">OvrdScope</a>: <i>String</i>
<a href="#profileattribute" title="ProfileAttribute">ProfileAttribute</a>: <i>String</i>
<a href="#profiletype" title="ProfileType">ProfileType</a>: <i>String</i>
<a href="#ovrdusergroup" title="OvrdUserGroup">OvrdUserGroup</a>: <i>
      - <a href="ovrdusergroupdefinition.md">OvrdUserGroupDefinition</a></i>
<a href="#profile" title="Profile">Profile</a>: <i>
      - <a href="profiledefinition.md">ProfileDefinition</a></i>
</pre>

## Properties

#### OvrdCookie

Allow/deny browser-based (cookie) overrides. Valid values: `allow`, `deny`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OvrdDur

Override duration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OvrdDurMode

Override duration mode. Valid values: `constant`, `ask`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OvrdScope

Override scope. Valid values: `user`, `user-group`, `ip`, `browser`, `ask`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileAttribute

Profile attribute to retrieve from the RADIUS server. Valid values: `User-Name`, `NAS-IP-Address`, `Framed-IP-Address`, `Framed-IP-Netmask`, `Filter-Id`, `Login-IP-Host`, `Reply-Message`, `Callback-Number`, `Callback-Id`, `Framed-Route`, `Framed-IPX-Network`, `Class`, `Called-Station-Id`, `Calling-Station-Id`, `NAS-Identifier`, `Proxy-State`, `Login-LAT-Service`, `Login-LAT-Node`, `Login-LAT-Group`, `Framed-AppleTalk-Zone`, `Acct-Session-Id`, `Acct-Multi-Session-Id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileType

Override profile type. Valid values: `list`, `radius`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OvrdUserGroup

_Required_: No

_Type_: List of <a href="ovrdusergroupdefinition.md">OvrdUserGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profile

_Required_: No

_Type_: List of <a href="profiledefinition.md">ProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

