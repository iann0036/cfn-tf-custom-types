# TF::FortiOS::WirelesscontrollerWidsprofile

Configure wireless intrusion detection system (WIDS) profiles.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WirelesscontrollerWidsprofile",
    "Properties" : {
        "<a href="#apautosuppress" title="ApAutoSuppress">ApAutoSuppress</a>" : <i>String</i>,
        "<a href="#apbgscandisableday" title="ApBgscanDisableDay">ApBgscanDisableDay</a>" : <i>String</i>,
        "<a href="#apbgscandisableend" title="ApBgscanDisableEnd">ApBgscanDisableEnd</a>" : <i>String</i>,
        "<a href="#apbgscandisablestart" title="ApBgscanDisableStart">ApBgscanDisableStart</a>" : <i>String</i>,
        "<a href="#apbgscanduration" title="ApBgscanDuration">ApBgscanDuration</a>" : <i>Double</i>,
        "<a href="#apbgscanidle" title="ApBgscanIdle">ApBgscanIdle</a>" : <i>Double</i>,
        "<a href="#apbgscanintv" title="ApBgscanIntv">ApBgscanIntv</a>" : <i>Double</i>,
        "<a href="#apbgscanperiod" title="ApBgscanPeriod">ApBgscanPeriod</a>" : <i>Double</i>,
        "<a href="#apbgscanreportintv" title="ApBgscanReportIntv">ApBgscanReportIntv</a>" : <i>Double</i>,
        "<a href="#apfgscanreportintv" title="ApFgscanReportIntv">ApFgscanReportIntv</a>" : <i>Double</i>,
        "<a href="#apscan" title="ApScan">ApScan</a>" : <i>String</i>,
        "<a href="#apscanpassive" title="ApScanPassive">ApScanPassive</a>" : <i>String</i>,
        "<a href="#apscanthreshold" title="ApScanThreshold">ApScanThreshold</a>" : <i>String</i>,
        "<a href="#asleapattack" title="AsleapAttack">AsleapAttack</a>" : <i>String</i>,
        "<a href="#assocfloodthresh" title="AssocFloodThresh">AssocFloodThresh</a>" : <i>Double</i>,
        "<a href="#assocfloodtime" title="AssocFloodTime">AssocFloodTime</a>" : <i>Double</i>,
        "<a href="#assocframeflood" title="AssocFrameFlood">AssocFrameFlood</a>" : <i>String</i>,
        "<a href="#authfloodthresh" title="AuthFloodThresh">AuthFloodThresh</a>" : <i>Double</i>,
        "<a href="#authfloodtime" title="AuthFloodTime">AuthFloodTime</a>" : <i>Double</i>,
        "<a href="#authframeflood" title="AuthFrameFlood">AuthFrameFlood</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#deauthbroadcast" title="DeauthBroadcast">DeauthBroadcast</a>" : <i>String</i>,
        "<a href="#deauthunknownsrcthresh" title="DeauthUnknownSrcThresh">DeauthUnknownSrcThresh</a>" : <i>Double</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#eapolfailflood" title="EapolFailFlood">EapolFailFlood</a>" : <i>String</i>,
        "<a href="#eapolfailintv" title="EapolFailIntv">EapolFailIntv</a>" : <i>Double</i>,
        "<a href="#eapolfailthresh" title="EapolFailThresh">EapolFailThresh</a>" : <i>Double</i>,
        "<a href="#eapollogoffflood" title="EapolLogoffFlood">EapolLogoffFlood</a>" : <i>String</i>,
        "<a href="#eapollogoffintv" title="EapolLogoffIntv">EapolLogoffIntv</a>" : <i>Double</i>,
        "<a href="#eapollogoffthresh" title="EapolLogoffThresh">EapolLogoffThresh</a>" : <i>Double</i>,
        "<a href="#eapolprefailflood" title="EapolPreFailFlood">EapolPreFailFlood</a>" : <i>String</i>,
        "<a href="#eapolprefailintv" title="EapolPreFailIntv">EapolPreFailIntv</a>" : <i>Double</i>,
        "<a href="#eapolprefailthresh" title="EapolPreFailThresh">EapolPreFailThresh</a>" : <i>Double</i>,
        "<a href="#eapolpresuccflood" title="EapolPreSuccFlood">EapolPreSuccFlood</a>" : <i>String</i>,
        "<a href="#eapolpresuccintv" title="EapolPreSuccIntv">EapolPreSuccIntv</a>" : <i>Double</i>,
        "<a href="#eapolpresuccthresh" title="EapolPreSuccThresh">EapolPreSuccThresh</a>" : <i>Double</i>,
        "<a href="#eapolstartflood" title="EapolStartFlood">EapolStartFlood</a>" : <i>String</i>,
        "<a href="#eapolstartintv" title="EapolStartIntv">EapolStartIntv</a>" : <i>Double</i>,
        "<a href="#eapolstartthresh" title="EapolStartThresh">EapolStartThresh</a>" : <i>Double</i>,
        "<a href="#eapolsuccflood" title="EapolSuccFlood">EapolSuccFlood</a>" : <i>String</i>,
        "<a href="#eapolsuccintv" title="EapolSuccIntv">EapolSuccIntv</a>" : <i>Double</i>,
        "<a href="#eapolsuccthresh" title="EapolSuccThresh">EapolSuccThresh</a>" : <i>Double</i>,
        "<a href="#invalidmacoui" title="InvalidMacOui">InvalidMacOui</a>" : <i>String</i>,
        "<a href="#longdurationattack" title="LongDurationAttack">LongDurationAttack</a>" : <i>String</i>,
        "<a href="#longdurationthresh" title="LongDurationThresh">LongDurationThresh</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nullssidproberesp" title="NullSsidProbeResp">NullSsidProbeResp</a>" : <i>String</i>,
        "<a href="#sensormode" title="SensorMode">SensorMode</a>" : <i>String</i>,
        "<a href="#spoofeddeauth" title="SpoofedDeauth">SpoofedDeauth</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#weakwepiv" title="WeakWepIv">WeakWepIv</a>" : <i>String</i>,
        "<a href="#wirelessbridge" title="WirelessBridge">WirelessBridge</a>" : <i>String</i>,
        "<a href="#apbgscandisableschedules" title="ApBgscanDisableSchedules">ApBgscanDisableSchedules</a>" : <i>[ <a href="apbgscandisableschedulesdefinition.md">ApBgscanDisableSchedulesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WirelesscontrollerWidsprofile
Properties:
    <a href="#apautosuppress" title="ApAutoSuppress">ApAutoSuppress</a>: <i>String</i>
    <a href="#apbgscandisableday" title="ApBgscanDisableDay">ApBgscanDisableDay</a>: <i>String</i>
    <a href="#apbgscandisableend" title="ApBgscanDisableEnd">ApBgscanDisableEnd</a>: <i>String</i>
    <a href="#apbgscandisablestart" title="ApBgscanDisableStart">ApBgscanDisableStart</a>: <i>String</i>
    <a href="#apbgscanduration" title="ApBgscanDuration">ApBgscanDuration</a>: <i>Double</i>
    <a href="#apbgscanidle" title="ApBgscanIdle">ApBgscanIdle</a>: <i>Double</i>
    <a href="#apbgscanintv" title="ApBgscanIntv">ApBgscanIntv</a>: <i>Double</i>
    <a href="#apbgscanperiod" title="ApBgscanPeriod">ApBgscanPeriod</a>: <i>Double</i>
    <a href="#apbgscanreportintv" title="ApBgscanReportIntv">ApBgscanReportIntv</a>: <i>Double</i>
    <a href="#apfgscanreportintv" title="ApFgscanReportIntv">ApFgscanReportIntv</a>: <i>Double</i>
    <a href="#apscan" title="ApScan">ApScan</a>: <i>String</i>
    <a href="#apscanpassive" title="ApScanPassive">ApScanPassive</a>: <i>String</i>
    <a href="#apscanthreshold" title="ApScanThreshold">ApScanThreshold</a>: <i>String</i>
    <a href="#asleapattack" title="AsleapAttack">AsleapAttack</a>: <i>String</i>
    <a href="#assocfloodthresh" title="AssocFloodThresh">AssocFloodThresh</a>: <i>Double</i>
    <a href="#assocfloodtime" title="AssocFloodTime">AssocFloodTime</a>: <i>Double</i>
    <a href="#assocframeflood" title="AssocFrameFlood">AssocFrameFlood</a>: <i>String</i>
    <a href="#authfloodthresh" title="AuthFloodThresh">AuthFloodThresh</a>: <i>Double</i>
    <a href="#authfloodtime" title="AuthFloodTime">AuthFloodTime</a>: <i>Double</i>
    <a href="#authframeflood" title="AuthFrameFlood">AuthFrameFlood</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#deauthbroadcast" title="DeauthBroadcast">DeauthBroadcast</a>: <i>String</i>
    <a href="#deauthunknownsrcthresh" title="DeauthUnknownSrcThresh">DeauthUnknownSrcThresh</a>: <i>Double</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#eapolfailflood" title="EapolFailFlood">EapolFailFlood</a>: <i>String</i>
    <a href="#eapolfailintv" title="EapolFailIntv">EapolFailIntv</a>: <i>Double</i>
    <a href="#eapolfailthresh" title="EapolFailThresh">EapolFailThresh</a>: <i>Double</i>
    <a href="#eapollogoffflood" title="EapolLogoffFlood">EapolLogoffFlood</a>: <i>String</i>
    <a href="#eapollogoffintv" title="EapolLogoffIntv">EapolLogoffIntv</a>: <i>Double</i>
    <a href="#eapollogoffthresh" title="EapolLogoffThresh">EapolLogoffThresh</a>: <i>Double</i>
    <a href="#eapolprefailflood" title="EapolPreFailFlood">EapolPreFailFlood</a>: <i>String</i>
    <a href="#eapolprefailintv" title="EapolPreFailIntv">EapolPreFailIntv</a>: <i>Double</i>
    <a href="#eapolprefailthresh" title="EapolPreFailThresh">EapolPreFailThresh</a>: <i>Double</i>
    <a href="#eapolpresuccflood" title="EapolPreSuccFlood">EapolPreSuccFlood</a>: <i>String</i>
    <a href="#eapolpresuccintv" title="EapolPreSuccIntv">EapolPreSuccIntv</a>: <i>Double</i>
    <a href="#eapolpresuccthresh" title="EapolPreSuccThresh">EapolPreSuccThresh</a>: <i>Double</i>
    <a href="#eapolstartflood" title="EapolStartFlood">EapolStartFlood</a>: <i>String</i>
    <a href="#eapolstartintv" title="EapolStartIntv">EapolStartIntv</a>: <i>Double</i>
    <a href="#eapolstartthresh" title="EapolStartThresh">EapolStartThresh</a>: <i>Double</i>
    <a href="#eapolsuccflood" title="EapolSuccFlood">EapolSuccFlood</a>: <i>String</i>
    <a href="#eapolsuccintv" title="EapolSuccIntv">EapolSuccIntv</a>: <i>Double</i>
    <a href="#eapolsuccthresh" title="EapolSuccThresh">EapolSuccThresh</a>: <i>Double</i>
    <a href="#invalidmacoui" title="InvalidMacOui">InvalidMacOui</a>: <i>String</i>
    <a href="#longdurationattack" title="LongDurationAttack">LongDurationAttack</a>: <i>String</i>
    <a href="#longdurationthresh" title="LongDurationThresh">LongDurationThresh</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nullssidproberesp" title="NullSsidProbeResp">NullSsidProbeResp</a>: <i>String</i>
    <a href="#sensormode" title="SensorMode">SensorMode</a>: <i>String</i>
    <a href="#spoofeddeauth" title="SpoofedDeauth">SpoofedDeauth</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#weakwepiv" title="WeakWepIv">WeakWepIv</a>: <i>String</i>
    <a href="#wirelessbridge" title="WirelessBridge">WirelessBridge</a>: <i>String</i>
    <a href="#apbgscandisableschedules" title="ApBgscanDisableSchedules">ApBgscanDisableSchedules</a>: <i>
      - <a href="apbgscandisableschedulesdefinition.md">ApBgscanDisableSchedulesDefinition</a></i>
</pre>

## Properties

#### ApAutoSuppress

Enable/disable on-wire rogue AP auto-suppression (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApBgscanDisableDay

Optionally turn off scanning for one or more days of the week. Separate the days with a space. By default, no days are set. Valid values: `sunday`, `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApBgscanDisableEnd

End time, using a 24-hour clock in the format of hh:mm, for disabling background scanning (default = 00:00).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApBgscanDisableStart

Start time, using a 24-hour clock in the format of hh:mm, for disabling background scanning (default = 00:00).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApBgscanDuration

Listening time on a scanning channel (10 - 1000 msec, default = 20).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApBgscanIdle

Waiting time for channel inactivity before scanning this channel (0 - 1000 msec, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApBgscanIntv

Period of time between scanning two channels (1 - 600 sec, default = 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApBgscanPeriod

Period of time between background scans (60 - 3600 sec, default = 600).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApBgscanReportIntv

Period of time between background scan reports (15 - 600 sec, default = 30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApFgscanReportIntv

Period of time between foreground scan reports (15 - 600 sec, default = 15).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApScan

Enable/disable rogue AP detection. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApScanPassive

Enable/disable passive scanning. Enable means do not send probe request on any channels (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApScanThreshold

Minimum signal level/threshold in dBm required for the AP to report detected rogue AP (-95 to -20, default = -90).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsleapAttack

Enable/disable asleap attack detection (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssocFloodThresh

The threshold value for association frame flooding.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssocFloodTime

Number of seconds after which a station is considered not connected.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssocFrameFlood

Enable/disable association frame flooding detection (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthFloodThresh

The threshold value for authentication frame flooding.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthFloodTime

Number of seconds after which a station is considered not connected.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthFrameFlood

Enable/disable authentication frame flooding detection (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeauthBroadcast

Enable/disable broadcasting de-authentication detection (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeauthUnknownSrcThresh

Threshold value per second to deauth unknown src for DoS attack (0: no limit).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolFailFlood

Enable/disable EAPOL-Failure flooding (to AP) detection (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolFailIntv

The detection interval for EAPOL-Failure flooding (1 - 3600 sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolFailThresh

The threshold value for EAPOL-Failure flooding in specified interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolLogoffFlood

Enable/disable EAPOL-Logoff flooding (to AP) detection (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolLogoffIntv

The detection interval for EAPOL-Logoff flooding (1 - 3600 sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolLogoffThresh

The threshold value for EAPOL-Logoff flooding in specified interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolPreFailFlood

Enable/disable premature EAPOL-Failure flooding (to STA) detection (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolPreFailIntv

The detection interval for premature EAPOL-Failure flooding (1 - 3600 sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolPreFailThresh

The threshold value for premature EAPOL-Failure flooding in specified interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolPreSuccFlood

Enable/disable premature EAPOL-Success flooding (to STA) detection (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolPreSuccIntv

The detection interval for premature EAPOL-Success flooding (1 - 3600 sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolPreSuccThresh

The threshold value for premature EAPOL-Success flooding in specified interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolStartFlood

Enable/disable EAPOL-Start flooding (to AP) detection (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolStartIntv

The detection interval for EAPOL-Start flooding (1 - 3600 sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolStartThresh

The threshold value for EAPOL-Start flooding in specified interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolSuccFlood

Enable/disable EAPOL-Success flooding (to AP) detection (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolSuccIntv

The detection interval for EAPOL-Success flooding (1 - 3600 sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapolSuccThresh

The threshold value for EAPOL-Success flooding in specified interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InvalidMacOui

Enable/disable invalid MAC OUI detection. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LongDurationAttack

Enable/disable long duration attack detection based on user configured threshold (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LongDurationThresh

Threshold value for long duration attack detection (1000 - 32767 usec, default = 8200).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

WIDS profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NullSsidProbeResp

Enable/disable null SSID probe response detection (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SensorMode

Scan WiFi nearby stations (default = disable). Valid values: `disable`, `foreign`, `both`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpoofedDeauth

Enable/disable spoofed de-authentication attack detection (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeakWepIv

Enable/disable weak WEP IV (Initialization Vector) detection (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WirelessBridge

Enable/disable wireless bridge detection (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApBgscanDisableSchedules

_Required_: No

_Type_: List of <a href="apbgscandisableschedulesdefinition.md">ApBgscanDisableSchedulesDefinition</a>

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

