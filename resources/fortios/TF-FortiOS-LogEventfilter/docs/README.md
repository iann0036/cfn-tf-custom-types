# TF::FortiOS::LogEventfilter

Configure log event filters.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::LogEventfilter",
    "Properties" : {
        "<a href="#cifs" title="Cifs">Cifs</a>" : <i>String</i>,
        "<a href="#compliancecheck" title="ComplianceCheck">ComplianceCheck</a>" : <i>String</i>,
        "<a href="#connector" title="Connector">Connector</a>" : <i>String</i>,
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
        "<a href="#event" title="Event">Event</a>" : <i>String</i>,
        "<a href="#fortiextender" title="Fortiextender">Fortiextender</a>" : <i>String</i>,
        "<a href="#ha" title="Ha">Ha</a>" : <i>String</i>,
        "<a href="#router" title="Router">Router</a>" : <i>String</i>,
        "<a href="#sdwan" title="Sdwan">Sdwan</a>" : <i>String</i>,
        "<a href="#securityrating" title="SecurityRating">SecurityRating</a>" : <i>String</i>,
        "<a href="#switchcontroller" title="SwitchController">SwitchController</a>" : <i>String</i>,
        "<a href="#system" title="System">System</a>" : <i>String</i>,
        "<a href="#user" title="User">User</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#vpn" title="Vpn">Vpn</a>" : <i>String</i>,
        "<a href="#wanopt" title="WanOpt">WanOpt</a>" : <i>String</i>,
        "<a href="#wirelessactivity" title="WirelessActivity">WirelessActivity</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::LogEventfilter
Properties:
    <a href="#cifs" title="Cifs">Cifs</a>: <i>String</i>
    <a href="#compliancecheck" title="ComplianceCheck">ComplianceCheck</a>: <i>String</i>
    <a href="#connector" title="Connector">Connector</a>: <i>String</i>
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
    <a href="#event" title="Event">Event</a>: <i>String</i>
    <a href="#fortiextender" title="Fortiextender">Fortiextender</a>: <i>String</i>
    <a href="#ha" title="Ha">Ha</a>: <i>String</i>
    <a href="#router" title="Router">Router</a>: <i>String</i>
    <a href="#sdwan" title="Sdwan">Sdwan</a>: <i>String</i>
    <a href="#securityrating" title="SecurityRating">SecurityRating</a>: <i>String</i>
    <a href="#switchcontroller" title="SwitchController">SwitchController</a>: <i>String</i>
    <a href="#system" title="System">System</a>: <i>String</i>
    <a href="#user" title="User">User</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#vpn" title="Vpn">Vpn</a>: <i>String</i>
    <a href="#wanopt" title="WanOpt">WanOpt</a>: <i>String</i>
    <a href="#wirelessactivity" title="WirelessActivity">WirelessActivity</a>: <i>String</i>
</pre>

## Properties

#### Cifs

Enable/disable CIFS logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComplianceCheck

Enable/disable PCI DSS compliance check logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Connector

Enable/disable SDN connector logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoint

Enable/disable endpoint event logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Event

Enable/disable event logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fortiextender

Enable/disable FortiExtender logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ha

Enable/disable ha event logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Router

Enable/disable router event logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sdwan

Enable/disable SD-WAN logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityRating

Enable/disable Security Rating result logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchController

Enable/disable Switch-Controller logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### System

Enable/disable system event logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

Enable/disable user authentication event logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpn

Enable/disable VPN event logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WanOpt

Enable/disable WAN optimization event logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WirelessActivity

Enable/disable wireless event logging. Valid values: `enable`, `disable`.

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

