# TF::FortiOS::SystemsnmpUser

SNMP user configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemsnmpUser",
    "Properties" : {
        "<a href="#authproto" title="AuthProto">AuthProto</a>" : <i>String</i>,
        "<a href="#authpwd" title="AuthPwd">AuthPwd</a>" : <i>String</i>,
        "<a href="#events" title="Events">Events</a>" : <i>String</i>,
        "<a href="#hadirect" title="HaDirect">HaDirect</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notifyhosts" title="NotifyHosts">NotifyHosts</a>" : <i>String</i>,
        "<a href="#notifyhosts6" title="NotifyHosts6">NotifyHosts6</a>" : <i>String</i>,
        "<a href="#privproto" title="PrivProto">PrivProto</a>" : <i>String</i>,
        "<a href="#privpwd" title="PrivPwd">PrivPwd</a>" : <i>String</i>,
        "<a href="#queries" title="Queries">Queries</a>" : <i>String</i>,
        "<a href="#queryport" title="QueryPort">QueryPort</a>" : <i>Double</i>,
        "<a href="#securitylevel" title="SecurityLevel">SecurityLevel</a>" : <i>String</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
        "<a href="#sourceipv6" title="SourceIpv6">SourceIpv6</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#traplport" title="TrapLport">TrapLport</a>" : <i>Double</i>,
        "<a href="#traprport" title="TrapRport">TrapRport</a>" : <i>Double</i>,
        "<a href="#trapstatus" title="TrapStatus">TrapStatus</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemsnmpUser
Properties:
    <a href="#authproto" title="AuthProto">AuthProto</a>: <i>String</i>
    <a href="#authpwd" title="AuthPwd">AuthPwd</a>: <i>String</i>
    <a href="#events" title="Events">Events</a>: <i>String</i>
    <a href="#hadirect" title="HaDirect">HaDirect</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notifyhosts" title="NotifyHosts">NotifyHosts</a>: <i>String</i>
    <a href="#notifyhosts6" title="NotifyHosts6">NotifyHosts6</a>: <i>String</i>
    <a href="#privproto" title="PrivProto">PrivProto</a>: <i>String</i>
    <a href="#privpwd" title="PrivPwd">PrivPwd</a>: <i>String</i>
    <a href="#queries" title="Queries">Queries</a>: <i>String</i>
    <a href="#queryport" title="QueryPort">QueryPort</a>: <i>Double</i>
    <a href="#securitylevel" title="SecurityLevel">SecurityLevel</a>: <i>String</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
    <a href="#sourceipv6" title="SourceIpv6">SourceIpv6</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#traplport" title="TrapLport">TrapLport</a>: <i>Double</i>
    <a href="#traprport" title="TrapRport">TrapRport</a>: <i>Double</i>
    <a href="#trapstatus" title="TrapStatus">TrapStatus</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### AuthProto

Authentication protocol.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthPwd

Password for authentication protocol.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Events

SNMP notifications (traps) to send.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaDirect

Enable/disable direct management of HA cluster members. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

SNMP user name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyHosts

SNMP managers to send notifications (traps) to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyHosts6

IPv6 SNMP managers to send notifications (traps) to.

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

#### QueryPort

SNMPv3 query port (default = 161).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityLevel

Security level for message authentication and encryption. Valid values: `no-auth-no-priv`, `auth-no-priv`, `auth-priv`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

Source IP for SNMP trap.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIpv6

Source IPv6 for SNMP trap.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable this SNMP user. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapLport

SNMPv3 local trap port (default = 162).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapRport

SNMPv3 trap remote port (default = 162).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapStatus

Enable/disable traps for this SNMP user. Valid values: `enable`, `disable`.

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

