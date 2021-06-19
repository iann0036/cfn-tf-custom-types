# TF::FortiOS::SwitchcontrollerManagedswitch SnmpCommunityDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#events" title="Events">Events</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#queryv1port" title="QueryV1Port">QueryV1Port</a>" : <i>Double</i>,
    "<a href="#queryv1status" title="QueryV1Status">QueryV1Status</a>" : <i>String</i>,
    "<a href="#queryv2cport" title="QueryV2cPort">QueryV2cPort</a>" : <i>Double</i>,
    "<a href="#queryv2cstatus" title="QueryV2cStatus">QueryV2cStatus</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#trapv1lport" title="TrapV1Lport">TrapV1Lport</a>" : <i>Double</i>,
    "<a href="#trapv1rport" title="TrapV1Rport">TrapV1Rport</a>" : <i>Double</i>,
    "<a href="#trapv1status" title="TrapV1Status">TrapV1Status</a>" : <i>String</i>,
    "<a href="#trapv2clport" title="TrapV2cLport">TrapV2cLport</a>" : <i>Double</i>,
    "<a href="#trapv2crport" title="TrapV2cRport">TrapV2cRport</a>" : <i>Double</i>,
    "<a href="#trapv2cstatus" title="TrapV2cStatus">TrapV2cStatus</a>" : <i>String</i>,
    "<a href="#hosts" title="Hosts">Hosts</a>" : <i>[ <a href="hostsdefinition.md">HostsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#events" title="Events">Events</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#queryv1port" title="QueryV1Port">QueryV1Port</a>: <i>Double</i>
<a href="#queryv1status" title="QueryV1Status">QueryV1Status</a>: <i>String</i>
<a href="#queryv2cport" title="QueryV2cPort">QueryV2cPort</a>: <i>Double</i>
<a href="#queryv2cstatus" title="QueryV2cStatus">QueryV2cStatus</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#trapv1lport" title="TrapV1Lport">TrapV1Lport</a>: <i>Double</i>
<a href="#trapv1rport" title="TrapV1Rport">TrapV1Rport</a>: <i>Double</i>
<a href="#trapv1status" title="TrapV1Status">TrapV1Status</a>: <i>String</i>
<a href="#trapv2clport" title="TrapV2cLport">TrapV2cLport</a>: <i>Double</i>
<a href="#trapv2crport" title="TrapV2cRport">TrapV2cRport</a>: <i>Double</i>
<a href="#trapv2cstatus" title="TrapV2cStatus">TrapV2cStatus</a>: <i>String</i>
<a href="#hosts" title="Hosts">Hosts</a>: <i>
      - <a href="hostsdefinition.md">HostsDefinition</a></i>
</pre>

## Properties

#### Events

SNMP notifications (traps) to send. Valid values: `cpu-high`, `mem-low`, `log-full`, `intf-ip`, `ent-conf-change`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

SNMP community ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

SNMP community name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryV1Port

SNMP v1 query port (default = 161).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryV1Status

Enable/disable SNMP v1 queries. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryV2cPort

SNMP v2c query port (default = 161).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryV2cStatus

Enable/disable SNMP v2c queries. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable this SNMP community. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapV1Lport

SNMP v2c trap local port (default = 162).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapV1Rport

SNMP v2c trap remote port (default = 162).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapV1Status

Enable/disable SNMP v1 traps. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapV2cLport

SNMP v2c trap local port (default = 162).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapV2cRport

SNMP v2c trap remote port (default = 162).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapV2cStatus

Enable/disable SNMP v2c traps. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hosts

_Required_: No

_Type_: List of <a href="hostsdefinition.md">HostsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

