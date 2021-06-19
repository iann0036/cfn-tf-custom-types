# TF::AVI::Systemconfiguration MgmtIpAccessControlDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#apiaccess" title="ApiAccess">ApiAccess</a>" : <i>[ <a href="apiaccessdefinition.md">ApiAccessDefinition</a>, ... ]</i>,
    "<a href="#shellserveraccess" title="ShellServerAccess">ShellServerAccess</a>" : <i>[ <a href="shellserveraccessdefinition.md">ShellServerAccessDefinition</a>, ... ]</i>,
    "<a href="#snmpaccess" title="SnmpAccess">SnmpAccess</a>" : <i>[ <a href="snmpaccessdefinition.md">SnmpAccessDefinition</a>, ... ]</i>,
    "<a href="#sshaccess" title="SshAccess">SshAccess</a>" : <i>[ <a href="sshaccessdefinition.md">SshAccessDefinition</a>, ... ]</i>,
    "<a href="#sysintaccess" title="SysintAccess">SysintAccess</a>" : <i>[ <a href="sysintaccessdefinition.md">SysintAccessDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#apiaccess" title="ApiAccess">ApiAccess</a>: <i>
      - <a href="apiaccessdefinition.md">ApiAccessDefinition</a></i>
<a href="#shellserveraccess" title="ShellServerAccess">ShellServerAccess</a>: <i>
      - <a href="shellserveraccessdefinition.md">ShellServerAccessDefinition</a></i>
<a href="#snmpaccess" title="SnmpAccess">SnmpAccess</a>: <i>
      - <a href="snmpaccessdefinition.md">SnmpAccessDefinition</a></i>
<a href="#sshaccess" title="SshAccess">SshAccess</a>: <i>
      - <a href="sshaccessdefinition.md">SshAccessDefinition</a></i>
<a href="#sysintaccess" title="SysintAccess">SysintAccess</a>: <i>
      - <a href="sysintaccessdefinition.md">SysintAccessDefinition</a></i>
</pre>

## Properties

#### ApiAccess

_Required_: No

_Type_: List of <a href="apiaccessdefinition.md">ApiAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShellServerAccess

_Required_: No

_Type_: List of <a href="shellserveraccessdefinition.md">ShellServerAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnmpAccess

_Required_: No

_Type_: List of <a href="snmpaccessdefinition.md">SnmpAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshAccess

_Required_: No

_Type_: List of <a href="sshaccessdefinition.md">SshAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SysintAccess

_Required_: No

_Type_: List of <a href="sysintaccessdefinition.md">SysintAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

