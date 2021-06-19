# TF::FortiOS::RouterMulticast PimSmGlobalDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#acceptregisterlist" title="AcceptRegisterList">AcceptRegisterList</a>" : <i>String</i>,
    "<a href="#acceptsourcelist" title="AcceptSourceList">AcceptSourceList</a>" : <i>String</i>,
    "<a href="#bsrallowquickrefresh" title="BsrAllowQuickRefresh">BsrAllowQuickRefresh</a>" : <i>String</i>,
    "<a href="#bsrcandidate" title="BsrCandidate">BsrCandidate</a>" : <i>String</i>,
    "<a href="#bsrhash" title="BsrHash">BsrHash</a>" : <i>Double</i>,
    "<a href="#bsrinterface" title="BsrInterface">BsrInterface</a>" : <i>String</i>,
    "<a href="#bsrpriority" title="BsrPriority">BsrPriority</a>" : <i>Double</i>,
    "<a href="#ciscocrpprefix" title="CiscoCrpPrefix">CiscoCrpPrefix</a>" : <i>String</i>,
    "<a href="#ciscoignorerpsetpriority" title="CiscoIgnoreRpSetPriority">CiscoIgnoreRpSetPriority</a>" : <i>String</i>,
    "<a href="#ciscoregisterchecksum" title="CiscoRegisterChecksum">CiscoRegisterChecksum</a>" : <i>String</i>,
    "<a href="#ciscoregisterchecksumgroup" title="CiscoRegisterChecksumGroup">CiscoRegisterChecksumGroup</a>" : <i>String</i>,
    "<a href="#joinpruneholdtime" title="JoinPruneHoldtime">JoinPruneHoldtime</a>" : <i>Double</i>,
    "<a href="#messageinterval" title="MessageInterval">MessageInterval</a>" : <i>Double</i>,
    "<a href="#nullregisterretries" title="NullRegisterRetries">NullRegisterRetries</a>" : <i>Double</i>,
    "<a href="#registerratelimit" title="RegisterRateLimit">RegisterRateLimit</a>" : <i>Double</i>,
    "<a href="#registerrpreachability" title="RegisterRpReachability">RegisterRpReachability</a>" : <i>String</i>,
    "<a href="#registersource" title="RegisterSource">RegisterSource</a>" : <i>String</i>,
    "<a href="#registersourceinterface" title="RegisterSourceInterface">RegisterSourceInterface</a>" : <i>String</i>,
    "<a href="#registersourceip" title="RegisterSourceIp">RegisterSourceIp</a>" : <i>String</i>,
    "<a href="#registersupression" title="RegisterSupression">RegisterSupression</a>" : <i>Double</i>,
    "<a href="#rpregisterkeepalive" title="RpRegisterKeepalive">RpRegisterKeepalive</a>" : <i>Double</i>,
    "<a href="#sptthreshold" title="SptThreshold">SptThreshold</a>" : <i>String</i>,
    "<a href="#sptthresholdgroup" title="SptThresholdGroup">SptThresholdGroup</a>" : <i>String</i>,
    "<a href="#ssm" title="Ssm">Ssm</a>" : <i>String</i>,
    "<a href="#ssmrange" title="SsmRange">SsmRange</a>" : <i>String</i>,
    "<a href="#rpaddress" title="RpAddress">RpAddress</a>" : <i>[ <a href="rpaddressdefinition.md">RpAddressDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#acceptregisterlist" title="AcceptRegisterList">AcceptRegisterList</a>: <i>String</i>
<a href="#acceptsourcelist" title="AcceptSourceList">AcceptSourceList</a>: <i>String</i>
<a href="#bsrallowquickrefresh" title="BsrAllowQuickRefresh">BsrAllowQuickRefresh</a>: <i>String</i>
<a href="#bsrcandidate" title="BsrCandidate">BsrCandidate</a>: <i>String</i>
<a href="#bsrhash" title="BsrHash">BsrHash</a>: <i>Double</i>
<a href="#bsrinterface" title="BsrInterface">BsrInterface</a>: <i>String</i>
<a href="#bsrpriority" title="BsrPriority">BsrPriority</a>: <i>Double</i>
<a href="#ciscocrpprefix" title="CiscoCrpPrefix">CiscoCrpPrefix</a>: <i>String</i>
<a href="#ciscoignorerpsetpriority" title="CiscoIgnoreRpSetPriority">CiscoIgnoreRpSetPriority</a>: <i>String</i>
<a href="#ciscoregisterchecksum" title="CiscoRegisterChecksum">CiscoRegisterChecksum</a>: <i>String</i>
<a href="#ciscoregisterchecksumgroup" title="CiscoRegisterChecksumGroup">CiscoRegisterChecksumGroup</a>: <i>String</i>
<a href="#joinpruneholdtime" title="JoinPruneHoldtime">JoinPruneHoldtime</a>: <i>Double</i>
<a href="#messageinterval" title="MessageInterval">MessageInterval</a>: <i>Double</i>
<a href="#nullregisterretries" title="NullRegisterRetries">NullRegisterRetries</a>: <i>Double</i>
<a href="#registerratelimit" title="RegisterRateLimit">RegisterRateLimit</a>: <i>Double</i>
<a href="#registerrpreachability" title="RegisterRpReachability">RegisterRpReachability</a>: <i>String</i>
<a href="#registersource" title="RegisterSource">RegisterSource</a>: <i>String</i>
<a href="#registersourceinterface" title="RegisterSourceInterface">RegisterSourceInterface</a>: <i>String</i>
<a href="#registersourceip" title="RegisterSourceIp">RegisterSourceIp</a>: <i>String</i>
<a href="#registersupression" title="RegisterSupression">RegisterSupression</a>: <i>Double</i>
<a href="#rpregisterkeepalive" title="RpRegisterKeepalive">RpRegisterKeepalive</a>: <i>Double</i>
<a href="#sptthreshold" title="SptThreshold">SptThreshold</a>: <i>String</i>
<a href="#sptthresholdgroup" title="SptThresholdGroup">SptThresholdGroup</a>: <i>String</i>
<a href="#ssm" title="Ssm">Ssm</a>: <i>String</i>
<a href="#ssmrange" title="SsmRange">SsmRange</a>: <i>String</i>
<a href="#rpaddress" title="RpAddress">RpAddress</a>: <i>
      - <a href="rpaddressdefinition.md">RpAddressDefinition</a></i>
</pre>

## Properties

#### AcceptRegisterList

Sources allowed to register packets with this Rendezvous Point (RP).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcceptSourceList

Sources allowed to send multicast traffic.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BsrAllowQuickRefresh

Enable/disable accept BSR quick refresh packets from neighbors. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BsrCandidate

Enable/disable allowing this router to become a bootstrap router (BSR). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BsrHash

BSR hash length (0 - 32, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BsrInterface

Interface to advertise as candidate BSR.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BsrPriority

BSR priority (0 - 255, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CiscoCrpPrefix

Enable/disable making candidate RP compatible with old Cisco IOS. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CiscoIgnoreRpSetPriority

Use only hash for RP selection (compatibility with old Cisco IOS). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CiscoRegisterChecksum

Checksum entire register packet(for old Cisco IOS compatibility). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CiscoRegisterChecksumGroup

Cisco register checksum only these groups.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JoinPruneHoldtime

Join/prune holdtime (1 - 65535, default = 210).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageInterval

Period of time between sending periodic PIM join/prune messages in seconds (1 - 65535, default = 60).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NullRegisterRetries

Maximum retries of null register (1 - 20, default = 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegisterRateLimit

Limit of packets/sec per source registered through this RP (0 - 65535, default = 0 which means unlimited).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegisterRpReachability

Enable/disable check RP is reachable before registering packets. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegisterSource

Override source address in register packets. Valid values: `disable`, `interface`, `ip-address`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegisterSourceInterface

Override with primary interface address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegisterSourceIp

Override with local IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegisterSupression

Period of time to honor register-stop message (1 - 65535 sec, default = 60).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RpRegisterKeepalive

Timeout for RP receiving data on (S,G) tree (1 - 65535 sec, default = 185).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SptThreshold

Enable/disable switching to source specific trees. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SptThresholdGroup

Groups allowed to switch to source tree.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ssm

Enable/disable source specific multicast. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsmRange

Groups allowed to source specific multicast.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RpAddress

_Required_: No

_Type_: List of <a href="rpaddressdefinition.md">RpAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

