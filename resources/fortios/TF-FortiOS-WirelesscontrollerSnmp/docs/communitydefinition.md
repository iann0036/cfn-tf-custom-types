# TF::FortiOS::WirelesscontrollerSnmp CommunityDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#queryv1status" title="QueryV1Status">QueryV1Status</a>" : <i>String</i>,
    "<a href="#queryv2cstatus" title="QueryV2cStatus">QueryV2cStatus</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#trapv1status" title="TrapV1Status">TrapV1Status</a>" : <i>String</i>,
    "<a href="#trapv2cstatus" title="TrapV2cStatus">TrapV2cStatus</a>" : <i>String</i>,
    "<a href="#hosts" title="Hosts">Hosts</a>" : <i>[ <a href="hostsdefinition.md">HostsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#queryv1status" title="QueryV1Status">QueryV1Status</a>: <i>String</i>
<a href="#queryv2cstatus" title="QueryV2cStatus">QueryV2cStatus</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#trapv1status" title="TrapV1Status">TrapV1Status</a>: <i>String</i>
<a href="#trapv2cstatus" title="TrapV2cStatus">TrapV2cStatus</a>: <i>String</i>
<a href="#hosts" title="Hosts">Hosts</a>: <i>
      - <a href="hostsdefinition.md">HostsDefinition</a></i>
</pre>

## Properties

#### Id

Community ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Community name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryV1Status

Enable/disable SNMP v1 queries. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryV2cStatus

Enable/disable SNMP v2c queries. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable this SNMP community. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapV1Status

Enable/disable SNMP v1 traps. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapV2cStatus

Enable/disable SNMP v2c traps. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hosts

_Required_: No

_Type_: List of <a href="hostsdefinition.md">HostsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

