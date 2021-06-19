# TF::FortiOS::SystemsnmpCommunity

SNMP community configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemsnmpCommunity",
    "Properties" : {
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#events" title="Events">Events</a>" : <i>String</i>,
        "<a href="#fosid" title="Fosid">Fosid</a>" : <i>Double</i>,
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
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#hosts" title="Hosts">Hosts</a>" : <i>[ <a href="hostsdefinition.md">HostsDefinition</a>, ... ]</i>,
        "<a href="#hosts6" title="Hosts6">Hosts6</a>" : <i>[ <a href="hosts6definition.md">Hosts6Definition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemsnmpCommunity
Properties:
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#events" title="Events">Events</a>: <i>String</i>
    <a href="#fosid" title="Fosid">Fosid</a>: <i>Double</i>
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
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#hosts" title="Hosts">Hosts</a>: <i>
      - <a href="hostsdefinition.md">HostsDefinition</a></i>
    <a href="#hosts6" title="Hosts6">Hosts6</a>: <i>
      - <a href="hosts6definition.md">Hosts6Definition</a></i>
</pre>

## Properties

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Events

SNMP trap events.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fosid

Community ID.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Community name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryV1Port

SNMP v1 query port (default = 161).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryV1Status

Enable/disable SNMP v1 queries. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryV2cPort

SNMP v2c query port (default = 161).

_Required_: No

_Type_: Double

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

#### TrapV1Lport

SNMP v1 trap local port (default = 162).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapV1Rport

SNMP v1 trap remote port (default = 162).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapV1Status

Enable/disable SNMP v1 traps. Valid values: `enable`, `disable`.

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

Enable/disable SNMP v2c traps. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hosts

_Required_: No

_Type_: List of <a href="hostsdefinition.md">HostsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hosts6

_Required_: No

_Type_: List of <a href="hosts6definition.md">Hosts6Definition</a>

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

