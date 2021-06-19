# TF::FortiOS::IpsSensor EntriesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#application" title="Application">Application</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#log" title="Log">Log</a>" : <i>String</i>,
    "<a href="#logattackcontext" title="LogAttackContext">LogAttackContext</a>" : <i>String</i>,
    "<a href="#logpacket" title="LogPacket">LogPacket</a>" : <i>String</i>,
    "<a href="#os" title="Os">Os</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#quarantine" title="Quarantine">Quarantine</a>" : <i>String</i>,
    "<a href="#quarantineexpiry" title="QuarantineExpiry">QuarantineExpiry</a>" : <i>String</i>,
    "<a href="#quarantinelog" title="QuarantineLog">QuarantineLog</a>" : <i>String</i>,
    "<a href="#ratecount" title="RateCount">RateCount</a>" : <i>Double</i>,
    "<a href="#rateduration" title="RateDuration">RateDuration</a>" : <i>Double</i>,
    "<a href="#ratemode" title="RateMode">RateMode</a>" : <i>String</i>,
    "<a href="#ratetrack" title="RateTrack">RateTrack</a>" : <i>String</i>,
    "<a href="#severity" title="Severity">Severity</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#cve" title="Cve">Cve</a>" : <i>[ <a href="cvedefinition.md">CveDefinition</a>, ... ]</i>,
    "<a href="#exemptip" title="ExemptIp">ExemptIp</a>" : <i>[ <a href="exemptipdefinition.md">ExemptIpDefinition</a>, ... ]</i>,
    "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="ruledefinition.md">RuleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#application" title="Application">Application</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#log" title="Log">Log</a>: <i>String</i>
<a href="#logattackcontext" title="LogAttackContext">LogAttackContext</a>: <i>String</i>
<a href="#logpacket" title="LogPacket">LogPacket</a>: <i>String</i>
<a href="#os" title="Os">Os</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#quarantine" title="Quarantine">Quarantine</a>: <i>String</i>
<a href="#quarantineexpiry" title="QuarantineExpiry">QuarantineExpiry</a>: <i>String</i>
<a href="#quarantinelog" title="QuarantineLog">QuarantineLog</a>: <i>String</i>
<a href="#ratecount" title="RateCount">RateCount</a>: <i>Double</i>
<a href="#rateduration" title="RateDuration">RateDuration</a>: <i>Double</i>
<a href="#ratemode" title="RateMode">RateMode</a>: <i>String</i>
<a href="#ratetrack" title="RateTrack">RateTrack</a>: <i>String</i>
<a href="#severity" title="Severity">Severity</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#cve" title="Cve">Cve</a>: <i>
      - <a href="cvedefinition.md">CveDefinition</a></i>
<a href="#exemptip" title="ExemptIp">ExemptIp</a>: <i>
      - <a href="exemptipdefinition.md">ExemptIpDefinition</a></i>
<a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="ruledefinition.md">RuleDefinition</a></i>
</pre>

## Properties

#### Action

Action taken with traffic in which signatures are detected. Valid values: `pass`, `block`, `reset`, `default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Application

Applications to be protected. set application ? lists available applications. all includes all applications. other includes all unlisted applications.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Rule ID in IPS database (0 - 4294967295).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Protect client or server traffic.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Log

Enable/disable logging of signatures included in filter. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAttackContext

Enable/disable logging of attack context: URL buffer, header buffer, body buffer, packet buffer. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogPacket

Enable/disable packet logging. Enable to save the packet that triggers the filter. You can download the packets in pcap format for diagnostic use. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Os

Operating systems to be protected.  all includes all operating systems. other includes all unlisted operating systems.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocols to be examined. set protocol ? lists available protocols. all includes all protocols. other includes all unlisted protocols.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quarantine

Quarantine method. Valid values: `none`, `attacker`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuarantineExpiry

Duration of quarantine. (Format ###d##h##m, minimum 1m, maximum 364d23h59m, default = 5m). Requires quarantine set to attacker.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuarantineLog

Enable/disable quarantine logging. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateCount

Count of the rate.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateDuration

Duration (sec) of the rate.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateMode

Rate limit mode. Valid values: `periodical`, `continuous`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateTrack

Track the packet protocol field. Valid values: `none`, `src-ip`, `dest-ip`, `dhcp-client-mac`, `dns-domain`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

Relative severity of the signature, from info to critical. Log messages generated by the signature include the severity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Status of the signatures included in filter. default enables the filter and only use filters with default status of enable. Filters with default status of disable will not be used. Valid values: `disable`, `enable`, `default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cve

_Required_: No

_Type_: List of <a href="cvedefinition.md">CveDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExemptIp

_Required_: No

_Type_: List of <a href="exemptipdefinition.md">ExemptIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="ruledefinition.md">RuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

