# TF::FortiOS::SwitchcontrollerFlowtracking

Configure FortiSwitch flow tracking and export via ipfix/netflow.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SwitchcontrollerFlowtracking",
    "Properties" : {
        "<a href="#collectorip" title="CollectorIp">CollectorIp</a>" : <i>String</i>,
        "<a href="#collectorport" title="CollectorPort">CollectorPort</a>" : <i>Double</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#format" title="Format">Format</a>" : <i>String</i>,
        "<a href="#level" title="Level">Level</a>" : <i>String</i>,
        "<a href="#maxexportpktsize" title="MaxExportPktSize">MaxExportPktSize</a>" : <i>Double</i>,
        "<a href="#samplemode" title="SampleMode">SampleMode</a>" : <i>String</i>,
        "<a href="#samplerate" title="SampleRate">SampleRate</a>" : <i>Double</i>,
        "<a href="#timeoutgeneral" title="TimeoutGeneral">TimeoutGeneral</a>" : <i>Double</i>,
        "<a href="#timeouticmp" title="TimeoutIcmp">TimeoutIcmp</a>" : <i>Double</i>,
        "<a href="#timeoutmax" title="TimeoutMax">TimeoutMax</a>" : <i>Double</i>,
        "<a href="#timeouttcp" title="TimeoutTcp">TimeoutTcp</a>" : <i>Double</i>,
        "<a href="#timeouttcpfin" title="TimeoutTcpFin">TimeoutTcpFin</a>" : <i>Double</i>,
        "<a href="#timeouttcprst" title="TimeoutTcpRst">TimeoutTcpRst</a>" : <i>Double</i>,
        "<a href="#timeoutudp" title="TimeoutUdp">TimeoutUdp</a>" : <i>Double</i>,
        "<a href="#transport" title="Transport">Transport</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#aggregates" title="Aggregates">Aggregates</a>" : <i>[ <a href="aggregatesdefinition.md">AggregatesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SwitchcontrollerFlowtracking
Properties:
    <a href="#collectorip" title="CollectorIp">CollectorIp</a>: <i>String</i>
    <a href="#collectorport" title="CollectorPort">CollectorPort</a>: <i>Double</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#format" title="Format">Format</a>: <i>String</i>
    <a href="#level" title="Level">Level</a>: <i>String</i>
    <a href="#maxexportpktsize" title="MaxExportPktSize">MaxExportPktSize</a>: <i>Double</i>
    <a href="#samplemode" title="SampleMode">SampleMode</a>: <i>String</i>
    <a href="#samplerate" title="SampleRate">SampleRate</a>: <i>Double</i>
    <a href="#timeoutgeneral" title="TimeoutGeneral">TimeoutGeneral</a>: <i>Double</i>
    <a href="#timeouticmp" title="TimeoutIcmp">TimeoutIcmp</a>: <i>Double</i>
    <a href="#timeoutmax" title="TimeoutMax">TimeoutMax</a>: <i>Double</i>
    <a href="#timeouttcp" title="TimeoutTcp">TimeoutTcp</a>: <i>Double</i>
    <a href="#timeouttcpfin" title="TimeoutTcpFin">TimeoutTcpFin</a>: <i>Double</i>
    <a href="#timeouttcprst" title="TimeoutTcpRst">TimeoutTcpRst</a>: <i>Double</i>
    <a href="#timeoutudp" title="TimeoutUdp">TimeoutUdp</a>: <i>Double</i>
    <a href="#transport" title="Transport">Transport</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#aggregates" title="Aggregates">Aggregates</a>: <i>
      - <a href="aggregatesdefinition.md">AggregatesDefinition</a></i>
</pre>

## Properties

#### CollectorIp

Configure collector ip address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CollectorPort

Configure collector port number(0-65535, default=0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

Configure flow tracking protocol. Valid values: `netflow1`, `netflow5`, `netflow9`, `ipfix`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Level

Configure flow tracking level. Valid values: `vlan`, `ip`, `port`, `proto`, `mac`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxExportPktSize

Configure flow max export packet size (512-9216, default=512 bytes).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SampleMode

Configure sample mode for the flow tracking. Valid values: `local`, `perimeter`, `device-ingress`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SampleRate

Configure sample rate for the perimeter and device-ingress sampling(0 - 99999).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutGeneral

Configure flow session general timeout (60-604800, default=3600 seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutIcmp

Configure flow session ICMP timeout (60-604800, default=300 seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutMax

Configure flow session max timeout (60-604800, default=604800 seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutTcp

Configure flow session TCP timeout (60-604800, default=3600 seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutTcpFin

Configure flow session TCP FIN timeout (60-604800, default=300 seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutTcpRst

Configure flow session TCP RST timeout (60-604800, default=120 seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutUdp

Configure flow session UDP timeout (60-604800, default=300 seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Transport

Configure L4 transport protocol for exporting packets. Valid values: `udp`, `tcp`, `sctp`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Aggregates

_Required_: No

_Type_: List of <a href="aggregatesdefinition.md">AggregatesDefinition</a>

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

