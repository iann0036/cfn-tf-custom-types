# TF::FortiOS::WirelesscontrollerSnmp UserDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authproto" title="AuthProto">AuthProto</a>" : <i>String</i>,
    "<a href="#authpwd" title="AuthPwd">AuthPwd</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#notifyhosts" title="NotifyHosts">NotifyHosts</a>" : <i>String</i>,
    "<a href="#privproto" title="PrivProto">PrivProto</a>" : <i>String</i>,
    "<a href="#privpwd" title="PrivPwd">PrivPwd</a>" : <i>String</i>,
    "<a href="#queries" title="Queries">Queries</a>" : <i>String</i>,
    "<a href="#securitylevel" title="SecurityLevel">SecurityLevel</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#trapstatus" title="TrapStatus">TrapStatus</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#authproto" title="AuthProto">AuthProto</a>: <i>String</i>
<a href="#authpwd" title="AuthPwd">AuthPwd</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#notifyhosts" title="NotifyHosts">NotifyHosts</a>: <i>String</i>
<a href="#privproto" title="PrivProto">PrivProto</a>: <i>String</i>
<a href="#privpwd" title="PrivPwd">PrivPwd</a>: <i>String</i>
<a href="#queries" title="Queries">Queries</a>: <i>String</i>
<a href="#securitylevel" title="SecurityLevel">SecurityLevel</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#trapstatus" title="TrapStatus">TrapStatus</a>: <i>String</i>
</pre>

## Properties

#### AuthProto

Authentication protocol. Valid values: `md5`, `sha`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthPwd

Password for authentication protocol.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

SNMP User Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyHosts

Configure SNMP User Notify Hosts.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivProto

Privacy (encryption) protocol. Valid values: `aes`, `des`, `aes256`, `aes256cisco`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivPwd

Password for privacy (encryption) protocol.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Queries

Enable/disable SNMP queries for this user. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityLevel

Security level for message authentication and encryption. Valid values: `no-auth-no-priv`, `auth-no-priv`, `auth-priv`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

SNMP User Enable Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapStatus

Enable/disable traps for this SNMP user. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

