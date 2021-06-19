# TF::FortiOS::IpsSensor FilterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#application" title="Application">Application</a>" : <i>String</i>,
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#log" title="Log">Log</a>" : <i>String</i>,
    "<a href="#logpacket" title="LogPacket">LogPacket</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#os" title="Os">Os</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#quarantine" title="Quarantine">Quarantine</a>" : <i>String</i>,
    "<a href="#quarantineexpiry" title="QuarantineExpiry">QuarantineExpiry</a>" : <i>Double</i>,
    "<a href="#quarantinelog" title="QuarantineLog">QuarantineLog</a>" : <i>String</i>,
    "<a href="#severity" title="Severity">Severity</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#application" title="Application">Application</a>: <i>String</i>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#log" title="Log">Log</a>: <i>String</i>
<a href="#logpacket" title="LogPacket">LogPacket</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#os" title="Os">Os</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#quarantine" title="Quarantine">Quarantine</a>: <i>String</i>
<a href="#quarantineexpiry" title="QuarantineExpiry">QuarantineExpiry</a>: <i>Double</i>
<a href="#quarantinelog" title="QuarantineLog">QuarantineLog</a>: <i>String</i>
<a href="#severity" title="Severity">Severity</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
</pre>

## Properties

#### Action

Action of selected rules. Valid values: `pass`, `block`, `reset`, `default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Application

Vulnerable application filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Vulnerability location filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Log

Enable/disable logging of selected rules. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogPacket

Enable/disable packet logging of selected rules. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Filter name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Os

Vulnerable OS filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Vulnerable protocol filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quarantine

Quarantine IP or interface. Valid values: `none`, `attacker`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuarantineExpiry

Duration of quarantine in minute.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuarantineLog

Enable/disable logging of selected quarantine. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

Vulnerability severity filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Selected rules status. Valid values: `disable`, `enable`, `default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

