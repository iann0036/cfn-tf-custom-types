# TF::FortiOS::IpsSensor OverrideDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#log" title="Log">Log</a>" : <i>String</i>,
    "<a href="#logpacket" title="LogPacket">LogPacket</a>" : <i>String</i>,
    "<a href="#quarantine" title="Quarantine">Quarantine</a>" : <i>String</i>,
    "<a href="#quarantineexpiry" title="QuarantineExpiry">QuarantineExpiry</a>" : <i>Double</i>,
    "<a href="#quarantinelog" title="QuarantineLog">QuarantineLog</a>" : <i>String</i>,
    "<a href="#ruleid" title="RuleId">RuleId</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#exemptip" title="ExemptIp">ExemptIp</a>" : <i>[ <a href="exemptipdefinition.md">ExemptIpDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#log" title="Log">Log</a>: <i>String</i>
<a href="#logpacket" title="LogPacket">LogPacket</a>: <i>String</i>
<a href="#quarantine" title="Quarantine">Quarantine</a>: <i>String</i>
<a href="#quarantineexpiry" title="QuarantineExpiry">QuarantineExpiry</a>: <i>Double</i>
<a href="#quarantinelog" title="QuarantineLog">QuarantineLog</a>: <i>String</i>
<a href="#ruleid" title="RuleId">RuleId</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#exemptip" title="ExemptIp">ExemptIp</a>: <i>
      - <a href="exemptipdefinition.md">ExemptIpDefinition</a></i>
</pre>

## Properties

#### Action

Action of override rule. Valid values: `pass`, `block`, `reset`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Log

Enable/disable logging. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogPacket

Enable/disable packet logging. Valid values: `disable`, `enable`.

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

#### RuleId

Override rule ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable status of override rule. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExemptIp

_Required_: No

_Type_: List of <a href="exemptipdefinition.md">ExemptIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

