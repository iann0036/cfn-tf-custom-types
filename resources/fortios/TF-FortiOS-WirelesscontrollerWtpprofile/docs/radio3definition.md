# TF::FortiOS::WirelesscontrollerWtpprofile Radio3Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#airtimefairness" title="AirtimeFairness">AirtimeFairness</a>" : <i>String</i>,
    "<a href="#amsdu" title="Amsdu">Amsdu</a>" : <i>String</i>,
    "<a href="#aphandoff" title="ApHandoff">ApHandoff</a>" : <i>String</i>,
    "<a href="#apsnifferaddr" title="ApSnifferAddr">ApSnifferAddr</a>" : <i>String</i>,
    "<a href="#apsnifferbufsize" title="ApSnifferBufsize">ApSnifferBufsize</a>" : <i>Double</i>,
    "<a href="#apsnifferchan" title="ApSnifferChan">ApSnifferChan</a>" : <i>Double</i>,
    "<a href="#apsnifferctl" title="ApSnifferCtl">ApSnifferCtl</a>" : <i>String</i>,
    "<a href="#apsnifferdata" title="ApSnifferData">ApSnifferData</a>" : <i>String</i>,
    "<a href="#apsniffermgmtbeacon" title="ApSnifferMgmtBeacon">ApSnifferMgmtBeacon</a>" : <i>String</i>,
    "<a href="#apsniffermgmtother" title="ApSnifferMgmtOther">ApSnifferMgmtOther</a>" : <i>String</i>,
    "<a href="#apsniffermgmtprobe" title="ApSnifferMgmtProbe">ApSnifferMgmtProbe</a>" : <i>String</i>,
    "<a href="#autopowerhigh" title="AutoPowerHigh">AutoPowerHigh</a>" : <i>Double</i>,
    "<a href="#autopowerlevel" title="AutoPowerLevel">AutoPowerLevel</a>" : <i>String</i>,
    "<a href="#autopowerlow" title="AutoPowerLow">AutoPowerLow</a>" : <i>Double</i>,
    "<a href="#autopowertarget" title="AutoPowerTarget">AutoPowerTarget</a>" : <i>String</i>,
    "<a href="#band" title="Band">Band</a>" : <i>String</i>,
    "<a href="#band5gtype" title="Band5gType">Band5gType</a>" : <i>String</i>,
    "<a href="#bandwidthadmissioncontrol" title="BandwidthAdmissionControl">BandwidthAdmissionControl</a>" : <i>String</i>,
    "<a href="#bandwidthcapacity" title="BandwidthCapacity">BandwidthCapacity</a>" : <i>Double</i>,
    "<a href="#beaconinterval" title="BeaconInterval">BeaconInterval</a>" : <i>Double</i>,
    "<a href="#bsscolor" title="BssColor">BssColor</a>" : <i>Double</i>,
    "<a href="#calladmissioncontrol" title="CallAdmissionControl">CallAdmissionControl</a>" : <i>String</i>,
    "<a href="#callcapacity" title="CallCapacity">CallCapacity</a>" : <i>Double</i>,
    "<a href="#channelbonding" title="ChannelBonding">ChannelBonding</a>" : <i>String</i>,
    "<a href="#channelutilization" title="ChannelUtilization">ChannelUtilization</a>" : <i>String</i>,
    "<a href="#coexistence" title="Coexistence">Coexistence</a>" : <i>String</i>,
    "<a href="#darrp" title="Darrp">Darrp</a>" : <i>String</i>,
    "<a href="#drma" title="Drma">Drma</a>" : <i>String</i>,
    "<a href="#drmasensitivity" title="DrmaSensitivity">DrmaSensitivity</a>" : <i>String</i>,
    "<a href="#dtim" title="Dtim">Dtim</a>" : <i>Double</i>,
    "<a href="#fragthreshold" title="FragThreshold">FragThreshold</a>" : <i>Double</i>,
    "<a href="#frequencyhandoff" title="FrequencyHandoff">FrequencyHandoff</a>" : <i>String</i>,
    "<a href="#maxclients" title="MaxClients">MaxClients</a>" : <i>Double</i>,
    "<a href="#maxdistance" title="MaxDistance">MaxDistance</a>" : <i>Double</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#powerlevel" title="PowerLevel">PowerLevel</a>" : <i>Double</i>,
    "<a href="#powersaveoptimize" title="PowersaveOptimize">PowersaveOptimize</a>" : <i>String</i>,
    "<a href="#protectionmode" title="ProtectionMode">ProtectionMode</a>" : <i>String</i>,
    "<a href="#rtsthreshold" title="RtsThreshold">RtsThreshold</a>" : <i>Double</i>,
    "<a href="#shortguardinterval" title="ShortGuardInterval">ShortGuardInterval</a>" : <i>String</i>,
    "<a href="#spectrumanalysis" title="SpectrumAnalysis">SpectrumAnalysis</a>" : <i>String</i>,
    "<a href="#transmitoptimize" title="TransmitOptimize">TransmitOptimize</a>" : <i>String</i>,
    "<a href="#vapall" title="VapAll">VapAll</a>" : <i>String</i>,
    "<a href="#widsprofile" title="WidsProfile">WidsProfile</a>" : <i>String</i>,
    "<a href="#zerowaitdfs" title="ZeroWaitDfs">ZeroWaitDfs</a>" : <i>String</i>,
    "<a href="#channel" title="Channel">Channel</a>" : <i>[ <a href="channeldefinition.md">ChannelDefinition</a>, ... ]</i>,
    "<a href="#vaps" title="Vaps">Vaps</a>" : <i>[ <a href="vapsdefinition.md">VapsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#airtimefairness" title="AirtimeFairness">AirtimeFairness</a>: <i>String</i>
<a href="#amsdu" title="Amsdu">Amsdu</a>: <i>String</i>
<a href="#aphandoff" title="ApHandoff">ApHandoff</a>: <i>String</i>
<a href="#apsnifferaddr" title="ApSnifferAddr">ApSnifferAddr</a>: <i>String</i>
<a href="#apsnifferbufsize" title="ApSnifferBufsize">ApSnifferBufsize</a>: <i>Double</i>
<a href="#apsnifferchan" title="ApSnifferChan">ApSnifferChan</a>: <i>Double</i>
<a href="#apsnifferctl" title="ApSnifferCtl">ApSnifferCtl</a>: <i>String</i>
<a href="#apsnifferdata" title="ApSnifferData">ApSnifferData</a>: <i>String</i>
<a href="#apsniffermgmtbeacon" title="ApSnifferMgmtBeacon">ApSnifferMgmtBeacon</a>: <i>String</i>
<a href="#apsniffermgmtother" title="ApSnifferMgmtOther">ApSnifferMgmtOther</a>: <i>String</i>
<a href="#apsniffermgmtprobe" title="ApSnifferMgmtProbe">ApSnifferMgmtProbe</a>: <i>String</i>
<a href="#autopowerhigh" title="AutoPowerHigh">AutoPowerHigh</a>: <i>Double</i>
<a href="#autopowerlevel" title="AutoPowerLevel">AutoPowerLevel</a>: <i>String</i>
<a href="#autopowerlow" title="AutoPowerLow">AutoPowerLow</a>: <i>Double</i>
<a href="#autopowertarget" title="AutoPowerTarget">AutoPowerTarget</a>: <i>String</i>
<a href="#band" title="Band">Band</a>: <i>String</i>
<a href="#band5gtype" title="Band5gType">Band5gType</a>: <i>String</i>
<a href="#bandwidthadmissioncontrol" title="BandwidthAdmissionControl">BandwidthAdmissionControl</a>: <i>String</i>
<a href="#bandwidthcapacity" title="BandwidthCapacity">BandwidthCapacity</a>: <i>Double</i>
<a href="#beaconinterval" title="BeaconInterval">BeaconInterval</a>: <i>Double</i>
<a href="#bsscolor" title="BssColor">BssColor</a>: <i>Double</i>
<a href="#calladmissioncontrol" title="CallAdmissionControl">CallAdmissionControl</a>: <i>String</i>
<a href="#callcapacity" title="CallCapacity">CallCapacity</a>: <i>Double</i>
<a href="#channelbonding" title="ChannelBonding">ChannelBonding</a>: <i>String</i>
<a href="#channelutilization" title="ChannelUtilization">ChannelUtilization</a>: <i>String</i>
<a href="#coexistence" title="Coexistence">Coexistence</a>: <i>String</i>
<a href="#darrp" title="Darrp">Darrp</a>: <i>String</i>
<a href="#drma" title="Drma">Drma</a>: <i>String</i>
<a href="#drmasensitivity" title="DrmaSensitivity">DrmaSensitivity</a>: <i>String</i>
<a href="#dtim" title="Dtim">Dtim</a>: <i>Double</i>
<a href="#fragthreshold" title="FragThreshold">FragThreshold</a>: <i>Double</i>
<a href="#frequencyhandoff" title="FrequencyHandoff">FrequencyHandoff</a>: <i>String</i>
<a href="#maxclients" title="MaxClients">MaxClients</a>: <i>Double</i>
<a href="#maxdistance" title="MaxDistance">MaxDistance</a>: <i>Double</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#powerlevel" title="PowerLevel">PowerLevel</a>: <i>Double</i>
<a href="#powersaveoptimize" title="PowersaveOptimize">PowersaveOptimize</a>: <i>String</i>
<a href="#protectionmode" title="ProtectionMode">ProtectionMode</a>: <i>String</i>
<a href="#rtsthreshold" title="RtsThreshold">RtsThreshold</a>: <i>Double</i>
<a href="#shortguardinterval" title="ShortGuardInterval">ShortGuardInterval</a>: <i>String</i>
<a href="#spectrumanalysis" title="SpectrumAnalysis">SpectrumAnalysis</a>: <i>String</i>
<a href="#transmitoptimize" title="TransmitOptimize">TransmitOptimize</a>: <i>String</i>
<a href="#vapall" title="VapAll">VapAll</a>: <i>String</i>
<a href="#widsprofile" title="WidsProfile">WidsProfile</a>: <i>String</i>
<a href="#zerowaitdfs" title="ZeroWaitDfs">ZeroWaitDfs</a>: <i>String</i>
<a href="#channel" title="Channel">Channel</a>: <i>
      - <a href="channeldefinition.md">ChannelDefinition</a></i>
<a href="#vaps" title="Vaps">Vaps</a>: <i>
      - <a href="vapsdefinition.md">VapsDefinition</a></i>
</pre>

## Properties

#### AirtimeFairness

Enable/disable airtime fairness (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Amsdu

Enable/disable 802.11n AMSDU support. AMSDU can improve performance if supported by your WiFi clients (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApHandoff

Enable/disable AP handoff of clients to other APs (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApSnifferAddr

MAC address to monitor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApSnifferBufsize

Sniffer buffer size (1 - 32 MB, default = 16).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApSnifferChan

Channel on which to operate the sniffer (default = 6).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApSnifferCtl

Enable/disable sniffer on WiFi control frame (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApSnifferData

Enable/disable sniffer on WiFi data frame (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApSnifferMgmtBeacon

Enable/disable sniffer on WiFi management Beacon frames (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApSnifferMgmtOther

Enable/disable sniffer on WiFi management other frames  (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApSnifferMgmtProbe

Enable/disable sniffer on WiFi management probe frames (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoPowerHigh

The upper bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoPowerLevel

Enable/disable automatic power-level adjustment to prevent co-channel interference (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoPowerLow

The lower bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoPowerTarget

The target of automatic transmit power adjustment in dBm. (-95 to -20, default = -70).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Band

WiFi band that Radio 3 operates on.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Band5gType

WiFi 5G band type. Valid values: `5g-full`, `5g-high`, `5g-low`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BandwidthAdmissionControl

Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. A request to join the wireless network is only allowed if the access point has enough bandwidth to support it. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BandwidthCapacity

Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BeaconInterval

Beacon interval. The time between beacon frames in msec (the actual range of beacon interval depends on the AP platform type, default = 100).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BssColor

BSS color value for this 11ax radio (0 - 63, 0 means disable. default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CallAdmissionControl

Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. New VoIP calls are only accepted if there is enough bandwidth available to support them. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CallCapacity

Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChannelBonding

Channel bandwidth: 160,80, 40, or 20MHz. Channels may use both 20 and 40 by enabling coexistence. Valid values: `160MHz`, `80MHz`, `40MHz`, `20MHz`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChannelUtilization

Enable/disable measuring channel utilization. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Coexistence

Enable/disable allowing both HT20 and HT40 on the same radio (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Darrp

Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Drma

Enable/disable dynamic radio mode assignment (DRMA) (default = disable). Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrmaSensitivity

Network Coverage Factor (NCF) percentage required to consider a radio as redundant (default = low). Valid values: `low`, `medium`, `high`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dtim

Delivery Traffic Indication Map (DTIM) period (1 - 255, default = 1). Set higher to save battery life of WiFi client in power-save mode.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FragThreshold

Maximum packet size that can be sent without fragmentation (800 - 2346 bytes, default = 2346).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrequencyHandoff

Enable/disable frequency handoff of clients to other channels (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxClients

Maximum number of stations (STAs) or WiFi clients supported by the radio. Range depends on the hardware.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDistance

Maximum expected distance between the AP and clients (0 - 54000 m, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

Mode of radio 3. Radio 3 can be disabled, configured as an access point, a rogue AP monitor, or a sniffer. Valid values: `disabled`, `ap`, `monitor`, `sniffer`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PowerLevel

Radio power level as a percentage of the maximum transmit power (0 - 100, default = 100).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PowersaveOptimize

Enable client power-saving features such as TIM, AC VO, and OBSS etc. Valid values: `tim`, `ac-vo`, `no-obss-scan`, `no-11b-rate`, `client-rate-follow`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectionMode

Enable/disable 802.11g protection modes to support backwards compatibility with older clients (rtscts, ctsonly, disable). Valid values: `rtscts`, `ctsonly`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RtsThreshold

Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes, default = 2346).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShortGuardInterval

Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpectrumAnalysis

Enable/disable spectrum analysis to find interference that would negatively impact wireless performance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransmitOptimize

Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc. All are enabled by default. Valid values: `disable`, `power-save`, `aggr-limit`, `retry-limit`, `send-bar`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VapAll

Enable/disable the automatic inheritance of all Virtual Access Points (VAPs) (default = enable).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidsProfile

Wireless Intrusion Detection System (WIDS) profile name to assign to the radio.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZeroWaitDfs

Enable/disable zero wait DFS on radio (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Channel

_Required_: No

_Type_: List of <a href="channeldefinition.md">ChannelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vaps

_Required_: No

_Type_: List of <a href="vapsdefinition.md">VapsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

