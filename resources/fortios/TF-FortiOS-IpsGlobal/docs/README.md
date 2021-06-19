# TF::FortiOS::IpsGlobal

Configure IPS global parameter.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::IpsGlobal",
    "Properties" : {
        "<a href="#anomalymode" title="AnomalyMode">AnomalyMode</a>" : <i>String</i>,
        "<a href="#database" title="Database">Database</a>" : <i>String</i>,
        "<a href="#deepappinspdblimit" title="DeepAppInspDbLimit">DeepAppInspDbLimit</a>" : <i>Double</i>,
        "<a href="#deepappinsptimeout" title="DeepAppInspTimeout">DeepAppInspTimeout</a>" : <i>Double</i>,
        "<a href="#enginecount" title="EngineCount">EngineCount</a>" : <i>Double</i>,
        "<a href="#excludesignatures" title="ExcludeSignatures">ExcludeSignatures</a>" : <i>String</i>,
        "<a href="#failopen" title="FailOpen">FailOpen</a>" : <i>String</i>,
        "<a href="#intelligentmode" title="IntelligentMode">IntelligentMode</a>" : <i>String</i>,
        "<a href="#ngfwmaxscanrange" title="NgfwMaxScanRange">NgfwMaxScanRange</a>" : <i>Double</i>,
        "<a href="#packetlogqueuedepth" title="PacketLogQueueDepth">PacketLogQueueDepth</a>" : <i>Double</i>,
        "<a href="#sessionlimitmode" title="SessionLimitMode">SessionLimitMode</a>" : <i>String</i>,
        "<a href="#skypeclientpublicipaddr" title="SkypeClientPublicIpaddr">SkypeClientPublicIpaddr</a>" : <i>String</i>,
        "<a href="#socketsize" title="SocketSize">SocketSize</a>" : <i>Double</i>,
        "<a href="#syncsessionttl" title="SyncSessionTtl">SyncSessionTtl</a>" : <i>String</i>,
        "<a href="#trafficsubmit" title="TrafficSubmit">TrafficSubmit</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#tlsactiveprobe" title="TlsActiveProbe">TlsActiveProbe</a>" : <i>[ <a href="tlsactiveprobedefinition.md">TlsActiveProbeDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::IpsGlobal
Properties:
    <a href="#anomalymode" title="AnomalyMode">AnomalyMode</a>: <i>String</i>
    <a href="#database" title="Database">Database</a>: <i>String</i>
    <a href="#deepappinspdblimit" title="DeepAppInspDbLimit">DeepAppInspDbLimit</a>: <i>Double</i>
    <a href="#deepappinsptimeout" title="DeepAppInspTimeout">DeepAppInspTimeout</a>: <i>Double</i>
    <a href="#enginecount" title="EngineCount">EngineCount</a>: <i>Double</i>
    <a href="#excludesignatures" title="ExcludeSignatures">ExcludeSignatures</a>: <i>String</i>
    <a href="#failopen" title="FailOpen">FailOpen</a>: <i>String</i>
    <a href="#intelligentmode" title="IntelligentMode">IntelligentMode</a>: <i>String</i>
    <a href="#ngfwmaxscanrange" title="NgfwMaxScanRange">NgfwMaxScanRange</a>: <i>Double</i>
    <a href="#packetlogqueuedepth" title="PacketLogQueueDepth">PacketLogQueueDepth</a>: <i>Double</i>
    <a href="#sessionlimitmode" title="SessionLimitMode">SessionLimitMode</a>: <i>String</i>
    <a href="#skypeclientpublicipaddr" title="SkypeClientPublicIpaddr">SkypeClientPublicIpaddr</a>: <i>String</i>
    <a href="#socketsize" title="SocketSize">SocketSize</a>: <i>Double</i>
    <a href="#syncsessionttl" title="SyncSessionTtl">SyncSessionTtl</a>: <i>String</i>
    <a href="#trafficsubmit" title="TrafficSubmit">TrafficSubmit</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#tlsactiveprobe" title="TlsActiveProbe">TlsActiveProbe</a>: <i>
      - <a href="tlsactiveprobedefinition.md">TlsActiveProbeDefinition</a></i>
</pre>

## Properties

#### AnomalyMode

Global blocking mode for rate-based anomalies. Valid values: `periodical`, `continuous`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Database

Regular or extended IPS database. Regular protects against the latest common and in-the-wild attacks. Extended includes protection from legacy attacks. Valid values: `regular`, `extended`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeepAppInspDbLimit

Limit on number of entries in deep application inspection database (1 - 2147483647, 0 = use recommended setting).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeepAppInspTimeout

Timeout for Deep application inspection (1 - 2147483647 sec., 0 = use recommended setting).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineCount

Number of IPS engines running. If set to the default value of 0, FortiOS sets the number to optimize performance depending on the number of CPU cores.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeSignatures

Excluded signatures. Valid values: `none`, `industrial`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailOpen

Enable to allow traffic if the IPS process crashes. Default is disable and IPS traffic is blocked when the IPS process crashes. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntelligentMode

Enable/disable IPS adaptive scanning (intelligent mode). Intelligent mode optimizes the scanning method for the type of traffic. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NgfwMaxScanRange

NGFW policy-mode app detection threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketLogQueueDepth

Packet/pcap log queue depth per IPS engine.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionLimitMode

Method of counting concurrent sessions used by session limit anomalies. Choose between greater accuracy (accurate) or improved performance (heuristics). Valid values: `accurate`, `heuristic`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkypeClientPublicIpaddr

Public IP addresses of your network that receive Skype sessions. Helps identify Skype sessions. Separate IP addresses with commas.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SocketSize

IPS socket buffer size (0 - 256 MB). Default depends on available memory. Can be changed to tune performance.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyncSessionTtl

Enable/disable use of kernel session TTL for IPS sessions. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficSubmit

Enable/disable submitting attack data found by this FortiGate to FortiGuard. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsActiveProbe

_Required_: No

_Type_: List of <a href="tlsactiveprobedefinition.md">TlsActiveProbeDefinition</a>

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

