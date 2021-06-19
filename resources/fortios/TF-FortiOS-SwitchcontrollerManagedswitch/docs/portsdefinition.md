# TF::FortiOS::SwitchcontrollerManagedswitch PortsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accessmode" title="AccessMode">AccessMode</a>" : <i>String</i>,
    "<a href="#aggregatormode" title="AggregatorMode">AggregatorMode</a>" : <i>String</i>,
    "<a href="#allowedvlansall" title="AllowedVlansAll">AllowedVlansAll</a>" : <i>String</i>,
    "<a href="#arpinspectiontrust" title="ArpInspectionTrust">ArpInspectionTrust</a>" : <i>String</i>,
    "<a href="#bundle" title="Bundle">Bundle</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#dhcpsnoopoption82trust" title="DhcpSnoopOption82Trust">DhcpSnoopOption82Trust</a>" : <i>String</i>,
    "<a href="#dhcpsnooping" title="DhcpSnooping">DhcpSnooping</a>" : <i>String</i>,
    "<a href="#discardmode" title="DiscardMode">DiscardMode</a>" : <i>String</i>,
    "<a href="#edgeport" title="EdgePort">EdgePort</a>" : <i>String</i>,
    "<a href="#exportto" title="ExportTo">ExportTo</a>" : <i>String</i>,
    "<a href="#exporttopool" title="ExportToPool">ExportToPool</a>" : <i>String</i>,
    "<a href="#exporttopoolflag" title="ExportToPoolFlag">ExportToPoolFlag</a>" : <i>Double</i>,
    "<a href="#feccapable" title="FecCapable">FecCapable</a>" : <i>Double</i>,
    "<a href="#fecstate" title="FecState">FecState</a>" : <i>String</i>,
    "<a href="#fgtpeerdevicename" title="FgtPeerDeviceName">FgtPeerDeviceName</a>" : <i>String</i>,
    "<a href="#fgtpeerportname" title="FgtPeerPortName">FgtPeerPortName</a>" : <i>String</i>,
    "<a href="#fiberport" title="FiberPort">FiberPort</a>" : <i>Double</i>,
    "<a href="#flags" title="Flags">Flags</a>" : <i>Double</i>,
    "<a href="#flowcontrol" title="FlowControl">FlowControl</a>" : <i>String</i>,
    "<a href="#fortilinkport" title="FortilinkPort">FortilinkPort</a>" : <i>Double</i>,
    "<a href="#igmpsnooping" title="IgmpSnooping">IgmpSnooping</a>" : <i>[ <a href="igmpsnoopingdefinition.md">IgmpSnoopingDefinition</a>, ... ]</i>,
    "<a href="#igmpsfloodreports" title="IgmpsFloodReports">IgmpsFloodReports</a>" : <i>String</i>,
    "<a href="#igmpsfloodtraffic" title="IgmpsFloodTraffic">IgmpsFloodTraffic</a>" : <i>String</i>,
    "<a href="#ipsourceguard" title="IpSourceGuard">IpSourceGuard</a>" : <i>[ <a href="ipsourceguarddefinition.md">IpSourceGuardDefinition</a>, ... ]</i>,
    "<a href="#isllocaltrunkname" title="IslLocalTrunkName">IslLocalTrunkName</a>" : <i>String</i>,
    "<a href="#islpeerdevicename" title="IslPeerDeviceName">IslPeerDeviceName</a>" : <i>String</i>,
    "<a href="#islpeerportname" title="IslPeerPortName">IslPeerPortName</a>" : <i>String</i>,
    "<a href="#lacpspeed" title="LacpSpeed">LacpSpeed</a>" : <i>String</i>,
    "<a href="#learninglimit" title="LearningLimit">LearningLimit</a>" : <i>Double</i>,
    "<a href="#lldpprofile" title="LldpProfile">LldpProfile</a>" : <i>String</i>,
    "<a href="#lldpstatus" title="LldpStatus">LldpStatus</a>" : <i>String</i>,
    "<a href="#loopguard" title="LoopGuard">LoopGuard</a>" : <i>String</i>,
    "<a href="#loopguardtimeout" title="LoopGuardTimeout">LoopGuardTimeout</a>" : <i>Double</i>,
    "<a href="#macaddr" title="MacAddr">MacAddr</a>" : <i>String</i>,
    "<a href="#maxbundle" title="MaxBundle">MaxBundle</a>" : <i>Double</i>,
    "<a href="#mclag" title="Mclag">Mclag</a>" : <i>String</i>,
    "<a href="#mclagiclport" title="MclagIclPort">MclagIclPort</a>" : <i>Double</i>,
    "<a href="#mediatype" title="MediaType">MediaType</a>" : <i>String</i>,
    "<a href="#memberwithdrawalbehavior" title="MemberWithdrawalBehavior">MemberWithdrawalBehavior</a>" : <i>String</i>,
    "<a href="#minbundle" title="MinBundle">MinBundle</a>" : <i>Double</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#p2pport" title="P2pPort">P2pPort</a>" : <i>Double</i>,
    "<a href="#packetsamplerate" title="PacketSampleRate">PacketSampleRate</a>" : <i>Double</i>,
    "<a href="#packetsampler" title="PacketSampler">PacketSampler</a>" : <i>String</i>,
    "<a href="#pausemeter" title="PauseMeter">PauseMeter</a>" : <i>Double</i>,
    "<a href="#pausemeterresume" title="PauseMeterResume">PauseMeterResume</a>" : <i>String</i>,
    "<a href="#poecapable" title="PoeCapable">PoeCapable</a>" : <i>Double</i>,
    "<a href="#poeprestandarddetection" title="PoePreStandardDetection">PoePreStandardDetection</a>" : <i>String</i>,
    "<a href="#poestatus" title="PoeStatus">PoeStatus</a>" : <i>String</i>,
    "<a href="#portname" title="PortName">PortName</a>" : <i>String</i>,
    "<a href="#portnumber" title="PortNumber">PortNumber</a>" : <i>Double</i>,
    "<a href="#portowner" title="PortOwner">PortOwner</a>" : <i>String</i>,
    "<a href="#portprefixtype" title="PortPrefixType">PortPrefixType</a>" : <i>Double</i>,
    "<a href="#portsecuritypolicy" title="PortSecurityPolicy">PortSecurityPolicy</a>" : <i>String</i>,
    "<a href="#portselectioncriteria" title="PortSelectionCriteria">PortSelectionCriteria</a>" : <i>String</i>,
    "<a href="#ptppolicy" title="PtpPolicy">PtpPolicy</a>" : <i>String</i>,
    "<a href="#qospolicy" title="QosPolicy">QosPolicy</a>" : <i>String</i>,
    "<a href="#rpvstport" title="RpvstPort">RpvstPort</a>" : <i>String</i>,
    "<a href="#sampledirection" title="SampleDirection">SampleDirection</a>" : <i>String</i>,
    "<a href="#sflowcounterinterval" title="SflowCounterInterval">SflowCounterInterval</a>" : <i>Double</i>,
    "<a href="#sflowsamplerate" title="SflowSampleRate">SflowSampleRate</a>" : <i>Double</i>,
    "<a href="#sflowsampler" title="SflowSampler">SflowSampler</a>" : <i>String</i>,
    "<a href="#speed" title="Speed">Speed</a>" : <i>String</i>,
    "<a href="#speedmask" title="SpeedMask">SpeedMask</a>" : <i>Double</i>,
    "<a href="#stackingport" title="StackingPort">StackingPort</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#stickymac" title="StickyMac">StickyMac</a>" : <i>String</i>,
    "<a href="#stormcontrolpolicy" title="StormControlPolicy">StormControlPolicy</a>" : <i>String</i>,
    "<a href="#stpbpduguard" title="StpBpduGuard">StpBpduGuard</a>" : <i>String</i>,
    "<a href="#stpbpduguardtimeout" title="StpBpduGuardTimeout">StpBpduGuardTimeout</a>" : <i>Double</i>,
    "<a href="#stprootguard" title="StpRootGuard">StpRootGuard</a>" : <i>String</i>,
    "<a href="#stpstate" title="StpState">StpState</a>" : <i>String</i>,
    "<a href="#switchid" title="SwitchId">SwitchId</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#virtualport" title="VirtualPort">VirtualPort</a>" : <i>Double</i>,
    "<a href="#vlan" title="Vlan">Vlan</a>" : <i>String</i>,
    "<a href="#allowedvlans" title="AllowedVlans">AllowedVlans</a>" : <i>[ <a href="allowedvlansdefinition.md">AllowedVlansDefinition</a>, ... ]</i>,
    "<a href="#exporttags" title="ExportTags">ExportTags</a>" : <i>[ <a href="exporttagsdefinition.md">ExportTagsDefinition</a>, ... ]</i>,
    "<a href="#members" title="Members">Members</a>" : <i>[ <a href="membersdefinition.md">MembersDefinition</a>, ... ]</i>,
    "<a href="#untaggedvlans" title="UntaggedVlans">UntaggedVlans</a>" : <i>[ <a href="untaggedvlansdefinition.md">UntaggedVlansDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accessmode" title="AccessMode">AccessMode</a>: <i>String</i>
<a href="#aggregatormode" title="AggregatorMode">AggregatorMode</a>: <i>String</i>
<a href="#allowedvlansall" title="AllowedVlansAll">AllowedVlansAll</a>: <i>String</i>
<a href="#arpinspectiontrust" title="ArpInspectionTrust">ArpInspectionTrust</a>: <i>String</i>
<a href="#bundle" title="Bundle">Bundle</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#dhcpsnoopoption82trust" title="DhcpSnoopOption82Trust">DhcpSnoopOption82Trust</a>: <i>String</i>
<a href="#dhcpsnooping" title="DhcpSnooping">DhcpSnooping</a>: <i>String</i>
<a href="#discardmode" title="DiscardMode">DiscardMode</a>: <i>String</i>
<a href="#edgeport" title="EdgePort">EdgePort</a>: <i>String</i>
<a href="#exportto" title="ExportTo">ExportTo</a>: <i>String</i>
<a href="#exporttopool" title="ExportToPool">ExportToPool</a>: <i>String</i>
<a href="#exporttopoolflag" title="ExportToPoolFlag">ExportToPoolFlag</a>: <i>Double</i>
<a href="#feccapable" title="FecCapable">FecCapable</a>: <i>Double</i>
<a href="#fecstate" title="FecState">FecState</a>: <i>String</i>
<a href="#fgtpeerdevicename" title="FgtPeerDeviceName">FgtPeerDeviceName</a>: <i>String</i>
<a href="#fgtpeerportname" title="FgtPeerPortName">FgtPeerPortName</a>: <i>String</i>
<a href="#fiberport" title="FiberPort">FiberPort</a>: <i>Double</i>
<a href="#flags" title="Flags">Flags</a>: <i>Double</i>
<a href="#flowcontrol" title="FlowControl">FlowControl</a>: <i>String</i>
<a href="#fortilinkport" title="FortilinkPort">FortilinkPort</a>: <i>Double</i>
<a href="#igmpsnooping" title="IgmpSnooping">IgmpSnooping</a>: <i>
      - <a href="igmpsnoopingdefinition.md">IgmpSnoopingDefinition</a></i>
<a href="#igmpsfloodreports" title="IgmpsFloodReports">IgmpsFloodReports</a>: <i>String</i>
<a href="#igmpsfloodtraffic" title="IgmpsFloodTraffic">IgmpsFloodTraffic</a>: <i>String</i>
<a href="#ipsourceguard" title="IpSourceGuard">IpSourceGuard</a>: <i>
      - <a href="ipsourceguarddefinition.md">IpSourceGuardDefinition</a></i>
<a href="#isllocaltrunkname" title="IslLocalTrunkName">IslLocalTrunkName</a>: <i>String</i>
<a href="#islpeerdevicename" title="IslPeerDeviceName">IslPeerDeviceName</a>: <i>String</i>
<a href="#islpeerportname" title="IslPeerPortName">IslPeerPortName</a>: <i>String</i>
<a href="#lacpspeed" title="LacpSpeed">LacpSpeed</a>: <i>String</i>
<a href="#learninglimit" title="LearningLimit">LearningLimit</a>: <i>Double</i>
<a href="#lldpprofile" title="LldpProfile">LldpProfile</a>: <i>String</i>
<a href="#lldpstatus" title="LldpStatus">LldpStatus</a>: <i>String</i>
<a href="#loopguard" title="LoopGuard">LoopGuard</a>: <i>String</i>
<a href="#loopguardtimeout" title="LoopGuardTimeout">LoopGuardTimeout</a>: <i>Double</i>
<a href="#macaddr" title="MacAddr">MacAddr</a>: <i>String</i>
<a href="#maxbundle" title="MaxBundle">MaxBundle</a>: <i>Double</i>
<a href="#mclag" title="Mclag">Mclag</a>: <i>String</i>
<a href="#mclagiclport" title="MclagIclPort">MclagIclPort</a>: <i>Double</i>
<a href="#mediatype" title="MediaType">MediaType</a>: <i>String</i>
<a href="#memberwithdrawalbehavior" title="MemberWithdrawalBehavior">MemberWithdrawalBehavior</a>: <i>String</i>
<a href="#minbundle" title="MinBundle">MinBundle</a>: <i>Double</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#p2pport" title="P2pPort">P2pPort</a>: <i>Double</i>
<a href="#packetsamplerate" title="PacketSampleRate">PacketSampleRate</a>: <i>Double</i>
<a href="#packetsampler" title="PacketSampler">PacketSampler</a>: <i>String</i>
<a href="#pausemeter" title="PauseMeter">PauseMeter</a>: <i>Double</i>
<a href="#pausemeterresume" title="PauseMeterResume">PauseMeterResume</a>: <i>String</i>
<a href="#poecapable" title="PoeCapable">PoeCapable</a>: <i>Double</i>
<a href="#poeprestandarddetection" title="PoePreStandardDetection">PoePreStandardDetection</a>: <i>String</i>
<a href="#poestatus" title="PoeStatus">PoeStatus</a>: <i>String</i>
<a href="#portname" title="PortName">PortName</a>: <i>String</i>
<a href="#portnumber" title="PortNumber">PortNumber</a>: <i>Double</i>
<a href="#portowner" title="PortOwner">PortOwner</a>: <i>String</i>
<a href="#portprefixtype" title="PortPrefixType">PortPrefixType</a>: <i>Double</i>
<a href="#portsecuritypolicy" title="PortSecurityPolicy">PortSecurityPolicy</a>: <i>String</i>
<a href="#portselectioncriteria" title="PortSelectionCriteria">PortSelectionCriteria</a>: <i>String</i>
<a href="#ptppolicy" title="PtpPolicy">PtpPolicy</a>: <i>String</i>
<a href="#qospolicy" title="QosPolicy">QosPolicy</a>: <i>String</i>
<a href="#rpvstport" title="RpvstPort">RpvstPort</a>: <i>String</i>
<a href="#sampledirection" title="SampleDirection">SampleDirection</a>: <i>String</i>
<a href="#sflowcounterinterval" title="SflowCounterInterval">SflowCounterInterval</a>: <i>Double</i>
<a href="#sflowsamplerate" title="SflowSampleRate">SflowSampleRate</a>: <i>Double</i>
<a href="#sflowsampler" title="SflowSampler">SflowSampler</a>: <i>String</i>
<a href="#speed" title="Speed">Speed</a>: <i>String</i>
<a href="#speedmask" title="SpeedMask">SpeedMask</a>: <i>Double</i>
<a href="#stackingport" title="StackingPort">StackingPort</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#stickymac" title="StickyMac">StickyMac</a>: <i>String</i>
<a href="#stormcontrolpolicy" title="StormControlPolicy">StormControlPolicy</a>: <i>String</i>
<a href="#stpbpduguard" title="StpBpduGuard">StpBpduGuard</a>: <i>String</i>
<a href="#stpbpduguardtimeout" title="StpBpduGuardTimeout">StpBpduGuardTimeout</a>: <i>Double</i>
<a href="#stprootguard" title="StpRootGuard">StpRootGuard</a>: <i>String</i>
<a href="#stpstate" title="StpState">StpState</a>: <i>String</i>
<a href="#switchid" title="SwitchId">SwitchId</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#virtualport" title="VirtualPort">VirtualPort</a>: <i>Double</i>
<a href="#vlan" title="Vlan">Vlan</a>: <i>String</i>
<a href="#allowedvlans" title="AllowedVlans">AllowedVlans</a>: <i>
      - <a href="allowedvlansdefinition.md">AllowedVlansDefinition</a></i>
<a href="#exporttags" title="ExportTags">ExportTags</a>: <i>
      - <a href="exporttagsdefinition.md">ExportTagsDefinition</a></i>
<a href="#members" title="Members">Members</a>: <i>
      - <a href="membersdefinition.md">MembersDefinition</a></i>
<a href="#untaggedvlans" title="UntaggedVlans">UntaggedVlans</a>: <i>
      - <a href="untaggedvlansdefinition.md">UntaggedVlansDefinition</a></i>
</pre>

## Properties

#### AccessMode

Access mode of the port. Valid values: `normal`, `nac`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AggregatorMode

LACP member select mode. Valid values: `bandwidth`, `count`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedVlansAll

Enable/disable all defined vlans on this port. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArpInspectionTrust

Trusted or untrusted dynamic ARP inspection. Valid values: `untrusted`, `trusted`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bundle

Enable/disable Link Aggregation Group (LAG) bundling for non-FortiLink interfaces. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for port.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpSnoopOption82Trust

Enable/disable allowance of DHCP with option-82 on untrusted interface. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpSnooping

Trusted or untrusted DHCP-snooping interface. Valid values: `untrusted`, `trusted`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiscardMode

Configure discard mode for port. Valid values: `none`, `all-untagged`, `all-tagged`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgePort

Enable/disable this interface as an edge port, bridging connections between workstations and/or computers. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportTo

Export managed-switch port to a tenant VDOM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportToPool

Switch controller export port to pool-list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportToPoolFlag

Switch controller export port to pool-list.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FecCapable

FEC capable.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FecState

State of forward error correction. Valid values: `disabled`, `cl74`, `cl91`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FgtPeerDeviceName

FGT peer device name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FgtPeerPortName

FGT peer port name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FiberPort

Fiber-port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flags

Port properties flags.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlowControl

Flow control direction. Valid values: `disable`, `tx`, `rx`, `both`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortilinkPort

FortiLink uplink port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgmpSnooping

_Required_: No

_Type_: List of <a href="igmpsnoopingdefinition.md">IgmpSnoopingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgmpsFloodReports

Enable/disable flooding of IGMP reports to this interface when igmp-snooping enabled. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgmpsFloodTraffic

Enable/disable flooding of IGMP snooping traffic to this interface. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpSourceGuard

_Required_: No

_Type_: List of <a href="ipsourceguarddefinition.md">IpSourceGuardDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IslLocalTrunkName

ISL local trunk name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IslPeerDeviceName

ISL peer device name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IslPeerPortName

ISL peer port name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LacpSpeed

end Link Aggregation Control Protocol (LACP) messages every 30 seconds (slow) or every second (fast). Valid values: `slow`, `fast`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LearningLimit

Limit the number of dynamic MAC addresses on this Port (1 - 128, 0 = no limit, default).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LldpProfile

LLDP port TLV profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LldpStatus

LLDP transmit and receive status. Valid values: `disable`, `rx-only`, `tx-only`, `tx-rx`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoopGuard

Enable/disable loop-guard on this interface, an STP optimization used to prevent network loops. Valid values: `enabled`, `disabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoopGuardTimeout

Loop-guard timeout (0 - 120 min, default = 45).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddr

Port/Trunk MAC.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBundle

Maximum size of LAG bundle (1 - 24, default = 24).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mclag

Enable/disable multi-chassis link aggregation (MCLAG). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MclagIclPort

MCLAG-ICL port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MediaType

Media type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberWithdrawalBehavior

Port behavior after it withdraws because of loss of control packets. Valid values: `forward`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinBundle

Minimum size of LAG bundle (1 - 24, default = 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

LACP mode: ignore and do not send control messages, or negotiate 802.3ad aggregation passively or actively. Valid values: `static`, `lacp-passive`, `lacp-active`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### P2pPort

General peer to peer tunnel port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketSampleRate

Packet sampling rate (0 - 99999 p/sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketSampler

Enable/disable packet sampling on this interface. Valid values: `enabled`, `disabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PauseMeter

Configure ingress pause metering rate, in kbps (default = 0, disabled).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PauseMeterResume

Resume threshold for resuming traffic on ingress port. Valid values: `75%`, `50%`, `25%`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoeCapable

PoE capable.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoePreStandardDetection

Enable/disable PoE pre-standard detection. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoeStatus

Enable/disable PoE status. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortName

Switch port name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortNumber

Port number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortOwner

Switch port name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortPrefixType

Port prefix type.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortSecurityPolicy

Switch controller authentication policy to apply to this managed switch from available options.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortSelectionCriteria

Algorithm for aggregate port selection. Valid values: `src-mac`, `dst-mac`, `src-dst-mac`, `src-ip`, `dst-ip`, `src-dst-ip`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PtpPolicy

PTP policy configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QosPolicy

Switch controller QoS policy from available options.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RpvstPort

Enable/disable inter-operability with rapid PVST on this interface. Valid values: `disabled`, `enabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SampleDirection

sFlow sample direction. Valid values: `tx`, `rx`, `both`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SflowCounterInterval

sFlow sampler counter polling interval (1 - 255 sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SflowSampleRate

sFlow sampler sample rate (0 - 99999 p/sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SflowSampler

Enable/disable sFlow protocol on this interface. Valid values: `enabled`, `disabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Speed

Switch port speed; default and available settings depend on hardware.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpeedMask

Switch port speed mask.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackingPort

Stacking port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Switch port admin status: up or down. Valid values: `up`, `down`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StickyMac

Enable or disable sticky-mac on the interface. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StormControlPolicy

Switch controller storm control policy from available options.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StpBpduGuard

Enable/disable STP BPDU guard on this interface. Valid values: `enabled`, `disabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StpBpduGuardTimeout

BPDU Guard disabling protection (0 - 120 min).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StpRootGuard

Enable/disable STP root guard on this interface. Valid values: `enabled`, `disabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StpState

Enable/disable Spanning Tree Protocol (STP) on this interface. Valid values: `enabled`, `disabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchId

Switch id.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Interface type: physical or trunk port. Valid values: `physical`, `trunk`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualPort

Virtualized switch port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vlan

Assign switch ports to a VLAN.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedVlans

_Required_: No

_Type_: List of <a href="allowedvlansdefinition.md">AllowedVlansDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportTags

_Required_: No

_Type_: List of <a href="exporttagsdefinition.md">ExportTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Members

_Required_: No

_Type_: List of <a href="membersdefinition.md">MembersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UntaggedVlans

_Required_: No

_Type_: List of <a href="untaggedvlansdefinition.md">UntaggedVlansDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

