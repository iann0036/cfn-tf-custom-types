# TF::Thunder::SlbCommon

`thunder_slb_common` Provides details about thunder slb common

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbCommon",
    "Properties" : {
        "<a href="#afterdisable" title="AfterDisable">AfterDisable</a>" : <i>Double</i>,
        "<a href="#autonatnoiprefresh" title="AutoNatNoIpRefresh">AutoNatNoIpRefresh</a>" : <i>String</i>,
        "<a href="#buffthresh" title="BuffThresh">BuffThresh</a>" : <i>Double</i>,
        "<a href="#buffthreshhwbuff" title="BuffThreshHwBuff">BuffThreshHwBuff</a>" : <i>Double</i>,
        "<a href="#buffthreshrelievethresh" title="BuffThreshRelieveThresh">BuffThreshRelieveThresh</a>" : <i>Double</i>,
        "<a href="#buffthreshsysbuffhigh" title="BuffThreshSysBuffHigh">BuffThreshSysBuffHigh</a>" : <i>Double</i>,
        "<a href="#buffthreshsysbufflow" title="BuffThreshSysBuffLow">BuffThreshSysBuffLow</a>" : <i>Double</i>,
        "<a href="#compressblocksize" title="CompressBlockSize">CompressBlockSize</a>" : <i>Double</i>,
        "<a href="#disableadaptiveresourcecheck" title="DisableAdaptiveResourceCheck">DisableAdaptiveResourceCheck</a>" : <i>Double</i>,
        "<a href="#disableserverautoreselect" title="DisableServerAutoReselect">DisableServerAutoReselect</a>" : <i>Double</i>,
        "<a href="#dnscacheage" title="DnsCacheAge">DnsCacheAge</a>" : <i>Double</i>,
        "<a href="#dnscacheenable" title="DnsCacheEnable">DnsCacheEnable</a>" : <i>Double</i>,
        "<a href="#dnscacheentrysize" title="DnsCacheEntrySize">DnsCacheEntrySize</a>" : <i>Double</i>,
        "<a href="#dnsvipstateless" title="DnsVipStateless">DnsVipStateless</a>" : <i>Double</i>,
        "<a href="#dropicmptovipwhenvipdown" title="DropIcmpToVipWhenVipDown">DropIcmpToVipWhenVipDown</a>" : <i>Double</i>,
        "<a href="#dsrhealthcheckenable" title="DsrHealthCheckEnable">DsrHealthCheckEnable</a>" : <i>Double</i>,
        "<a href="#enablel7reqacct" title="EnableL7ReqAcct">EnableL7ReqAcct</a>" : <i>Double</i>,
        "<a href="#entity" title="Entity">Entity</a>" : <i>String</i>,
        "<a href="#excludedestination" title="ExcludeDestination">ExcludeDestination</a>" : <i>String</i>,
        "<a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>" : <i>Double</i>,
        "<a href="#fastpathdisable" title="FastPathDisable">FastPathDisable</a>" : <i>Double</i>,
        "<a href="#gatewayhealthcheck" title="GatewayHealthCheck">GatewayHealthCheck</a>" : <i>Double</i>,
        "<a href="#gracefulshutdown" title="GracefulShutdown">GracefulShutdown</a>" : <i>Double</i>,
        "<a href="#gracefulshutdownenable" title="GracefulShutdownEnable">GracefulShutdownEnable</a>" : <i>Double</i>,
        "<a href="#honorserverresponsettl" title="HonorServerResponseTtl">HonorServerResponseTtl</a>" : <i>Double</i>,
        "<a href="#hwcompression" title="HwCompression">HwCompression</a>" : <i>Double</i>,
        "<a href="#hwsynrr" title="HwSynRr">HwSynRr</a>" : <i>Double</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
        "<a href="#l2l3trunklbdisable" title="L2l3TrunkLbDisable">L2l3TrunkLbDisable</a>" : <i>Double</i>,
        "<a href="#logforresetunknownconn" title="LogForResetUnknownConn">LogForResetUnknownConn</a>" : <i>Double</i>,
        "<a href="#lowlatency" title="LowLatency">LowLatency</a>" : <i>Double</i>,
        "<a href="#maxbuffqueuedperconn" title="MaxBuffQueuedPerConn">MaxBuffQueuedPerConn</a>" : <i>Double</i>,
        "<a href="#maxhttpheadercount" title="MaxHttpHeaderCount">MaxHttpHeaderCount</a>" : <i>Double</i>,
        "<a href="#maxlocalrate" title="MaxLocalRate">MaxLocalRate</a>" : <i>Double</i>,
        "<a href="#maxremoterate" title="MaxRemoteRate">MaxRemoteRate</a>" : <i>Double</i>,
        "<a href="#msltime" title="MslTime">MslTime</a>" : <i>Double</i>,
        "<a href="#msstable" title="MssTable">MssTable</a>" : <i>Double</i>,
        "<a href="#noautouponaflex" title="NoAutoUpOnAflex">NoAutoUpOnAflex</a>" : <i>Double</i>,
        "<a href="#overrideport" title="OverridePort">OverridePort</a>" : <i>Double</i>,
        "<a href="#pktrateforresetunknownconn" title="PktRateForResetUnknownConn">PktRateForResetUnknownConn</a>" : <i>Double</i>,
        "<a href="#playeridcheckenable" title="PlayerIdCheckEnable">PlayerIdCheckEnable</a>" : <i>Double</i>,
        "<a href="#range" title="Range">Range</a>" : <i>Double</i>,
        "<a href="#rangeend" title="RangeEnd">RangeEnd</a>" : <i>Double</i>,
        "<a href="#rangestart" title="RangeStart">RangeStart</a>" : <i>Double</i>,
        "<a href="#ratelimitlogging" title="RateLimitLogging">RateLimitLogging</a>" : <i>Double</i>,
        "<a href="#resetstalesession" title="ResetStaleSession">ResetStaleSession</a>" : <i>Double</i>,
        "<a href="#resolveportconflict" title="ResolvePortConflict">ResolvePortConflict</a>" : <i>Double</i>,
        "<a href="#responsetype" title="ResponseType">ResponseType</a>" : <i>String</i>,
        "<a href="#scaleout" title="ScaleOut">ScaleOut</a>" : <i>Double</i>,
        "<a href="#snatgwyforl3" title="SnatGwyForL3">SnatGwyForL3</a>" : <i>Double</i>,
        "<a href="#snatonvip" title="SnatOnVip">SnatOnVip</a>" : <i>Double</i>,
        "<a href="#software" title="Software">Software</a>" : <i>Double</i>,
        "<a href="#sortres" title="SortRes">SortRes</a>" : <i>Double</i>,
        "<a href="#sslisnihashenable" title="SsliSniHashEnable">SsliSniHashEnable</a>" : <i>Double</i>,
        "<a href="#statelesssgmultibinding" title="StatelessSgMultiBinding">StatelessSgMultiBinding</a>" : <i>Double</i>,
        "<a href="#statsdatadisable" title="StatsDataDisable">StatsDataDisable</a>" : <i>Double</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#ttlthreshold" title="TtlThreshold">TtlThreshold</a>" : <i>Double</i>,
        "<a href="#usemsstab" title="UseMssTab">UseMssTab</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#connratelimit" title="ConnRateLimit">ConnRateLimit</a>" : <i>[ <a href="connratelimitdefinition.md">ConnRateLimitDefinition</a>, ... ]</i>,
        "<a href="#ddosprotection" title="DdosProtection">DdosProtection</a>" : <i>[ <a href="ddosprotectiondefinition.md">DdosProtectionDefinition</a>, ... ]</i>,
        "<a href="#dnsresponseratelimiting" title="DnsResponseRateLimiting">DnsResponseRateLimiting</a>" : <i>[ <a href="dnsresponseratelimitingdefinition.md">DnsResponseRateLimitingDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbCommon
Properties:
    <a href="#afterdisable" title="AfterDisable">AfterDisable</a>: <i>Double</i>
    <a href="#autonatnoiprefresh" title="AutoNatNoIpRefresh">AutoNatNoIpRefresh</a>: <i>String</i>
    <a href="#buffthresh" title="BuffThresh">BuffThresh</a>: <i>Double</i>
    <a href="#buffthreshhwbuff" title="BuffThreshHwBuff">BuffThreshHwBuff</a>: <i>Double</i>
    <a href="#buffthreshrelievethresh" title="BuffThreshRelieveThresh">BuffThreshRelieveThresh</a>: <i>Double</i>
    <a href="#buffthreshsysbuffhigh" title="BuffThreshSysBuffHigh">BuffThreshSysBuffHigh</a>: <i>Double</i>
    <a href="#buffthreshsysbufflow" title="BuffThreshSysBuffLow">BuffThreshSysBuffLow</a>: <i>Double</i>
    <a href="#compressblocksize" title="CompressBlockSize">CompressBlockSize</a>: <i>Double</i>
    <a href="#disableadaptiveresourcecheck" title="DisableAdaptiveResourceCheck">DisableAdaptiveResourceCheck</a>: <i>Double</i>
    <a href="#disableserverautoreselect" title="DisableServerAutoReselect">DisableServerAutoReselect</a>: <i>Double</i>
    <a href="#dnscacheage" title="DnsCacheAge">DnsCacheAge</a>: <i>Double</i>
    <a href="#dnscacheenable" title="DnsCacheEnable">DnsCacheEnable</a>: <i>Double</i>
    <a href="#dnscacheentrysize" title="DnsCacheEntrySize">DnsCacheEntrySize</a>: <i>Double</i>
    <a href="#dnsvipstateless" title="DnsVipStateless">DnsVipStateless</a>: <i>Double</i>
    <a href="#dropicmptovipwhenvipdown" title="DropIcmpToVipWhenVipDown">DropIcmpToVipWhenVipDown</a>: <i>Double</i>
    <a href="#dsrhealthcheckenable" title="DsrHealthCheckEnable">DsrHealthCheckEnable</a>: <i>Double</i>
    <a href="#enablel7reqacct" title="EnableL7ReqAcct">EnableL7ReqAcct</a>: <i>Double</i>
    <a href="#entity" title="Entity">Entity</a>: <i>String</i>
    <a href="#excludedestination" title="ExcludeDestination">ExcludeDestination</a>: <i>String</i>
    <a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>: <i>Double</i>
    <a href="#fastpathdisable" title="FastPathDisable">FastPathDisable</a>: <i>Double</i>
    <a href="#gatewayhealthcheck" title="GatewayHealthCheck">GatewayHealthCheck</a>: <i>Double</i>
    <a href="#gracefulshutdown" title="GracefulShutdown">GracefulShutdown</a>: <i>Double</i>
    <a href="#gracefulshutdownenable" title="GracefulShutdownEnable">GracefulShutdownEnable</a>: <i>Double</i>
    <a href="#honorserverresponsettl" title="HonorServerResponseTtl">HonorServerResponseTtl</a>: <i>Double</i>
    <a href="#hwcompression" title="HwCompression">HwCompression</a>: <i>Double</i>
    <a href="#hwsynrr" title="HwSynRr">HwSynRr</a>: <i>Double</i>
    <a href="#interval" title="Interval">Interval</a>: <i>Double</i>
    <a href="#l2l3trunklbdisable" title="L2l3TrunkLbDisable">L2l3TrunkLbDisable</a>: <i>Double</i>
    <a href="#logforresetunknownconn" title="LogForResetUnknownConn">LogForResetUnknownConn</a>: <i>Double</i>
    <a href="#lowlatency" title="LowLatency">LowLatency</a>: <i>Double</i>
    <a href="#maxbuffqueuedperconn" title="MaxBuffQueuedPerConn">MaxBuffQueuedPerConn</a>: <i>Double</i>
    <a href="#maxhttpheadercount" title="MaxHttpHeaderCount">MaxHttpHeaderCount</a>: <i>Double</i>
    <a href="#maxlocalrate" title="MaxLocalRate">MaxLocalRate</a>: <i>Double</i>
    <a href="#maxremoterate" title="MaxRemoteRate">MaxRemoteRate</a>: <i>Double</i>
    <a href="#msltime" title="MslTime">MslTime</a>: <i>Double</i>
    <a href="#msstable" title="MssTable">MssTable</a>: <i>Double</i>
    <a href="#noautouponaflex" title="NoAutoUpOnAflex">NoAutoUpOnAflex</a>: <i>Double</i>
    <a href="#overrideport" title="OverridePort">OverridePort</a>: <i>Double</i>
    <a href="#pktrateforresetunknownconn" title="PktRateForResetUnknownConn">PktRateForResetUnknownConn</a>: <i>Double</i>
    <a href="#playeridcheckenable" title="PlayerIdCheckEnable">PlayerIdCheckEnable</a>: <i>Double</i>
    <a href="#range" title="Range">Range</a>: <i>Double</i>
    <a href="#rangeend" title="RangeEnd">RangeEnd</a>: <i>Double</i>
    <a href="#rangestart" title="RangeStart">RangeStart</a>: <i>Double</i>
    <a href="#ratelimitlogging" title="RateLimitLogging">RateLimitLogging</a>: <i>Double</i>
    <a href="#resetstalesession" title="ResetStaleSession">ResetStaleSession</a>: <i>Double</i>
    <a href="#resolveportconflict" title="ResolvePortConflict">ResolvePortConflict</a>: <i>Double</i>
    <a href="#responsetype" title="ResponseType">ResponseType</a>: <i>String</i>
    <a href="#scaleout" title="ScaleOut">ScaleOut</a>: <i>Double</i>
    <a href="#snatgwyforl3" title="SnatGwyForL3">SnatGwyForL3</a>: <i>Double</i>
    <a href="#snatonvip" title="SnatOnVip">SnatOnVip</a>: <i>Double</i>
    <a href="#software" title="Software">Software</a>: <i>Double</i>
    <a href="#sortres" title="SortRes">SortRes</a>: <i>Double</i>
    <a href="#sslisnihashenable" title="SsliSniHashEnable">SsliSniHashEnable</a>: <i>Double</i>
    <a href="#statelesssgmultibinding" title="StatelessSgMultiBinding">StatelessSgMultiBinding</a>: <i>Double</i>
    <a href="#statsdatadisable" title="StatsDataDisable">StatsDataDisable</a>: <i>Double</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#ttlthreshold" title="TtlThreshold">TtlThreshold</a>: <i>Double</i>
    <a href="#usemsstab" title="UseMssTab">UseMssTab</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#connratelimit" title="ConnRateLimit">ConnRateLimit</a>: <i>
      - <a href="connratelimitdefinition.md">ConnRateLimitDefinition</a></i>
    <a href="#ddosprotection" title="DdosProtection">DdosProtection</a>: <i>
      - <a href="ddosprotectiondefinition.md">DdosProtectionDefinition</a></i>
    <a href="#dnsresponseratelimiting" title="DnsResponseRateLimiting">DnsResponseRateLimiting</a>: <i>
      - <a href="dnsresponseratelimitingdefinition.md">DnsResponseRateLimitingDefinition</a></i>
</pre>

## Properties

#### AfterDisable

Graceful shutdown after disable server/port and/or virtual server/port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoNatNoIpRefresh

‘enable’: enable; ‘disable’: disable;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuffThresh

Set buffer threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuffThreshHwBuff

Set hardware buffer threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuffThreshRelieveThresh

Relieve threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuffThreshSysBuffHigh

Set high water mark of system buffer.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuffThreshSysBuffLow

Set low water mark of system buffer.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressBlockSize

Set compression block size (Compression block size in bytes).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableAdaptiveResourceCheck

Disable adaptive resource check based on buffer usage.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableServerAutoReselect

Disable auto reselection of server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsCacheAge

Set DNS cache entry age, default is 300 seconds (1-1000000 seconds, default is 300 seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsCacheEnable

Enable DNS cache.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsCacheEntrySize

Set DNS cache entry size, default is 256 bytes (1-4096 bytes, default is 256 bytes).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsVipStateless

Enable DNS VIP stateless mode.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropIcmpToVipWhenVipDown

Drop ICMP to VIP when VIP down.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DsrHealthCheckEnable

Enable dsr-health-check (direct server return health check).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableL7ReqAcct

Enable L7 request accounting.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entity

‘server’: Graceful shutdown server/port only; ‘virtual-server’: Graceful shutdown virtual server/port only;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeDestination

‘local’: Maximum local rate; ‘remote’: Maximum remote rate;  (Maximum rates).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedStats

Enable global slb extended statistics.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FastPathDisable

Disable fast path in SLB processing.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayHealthCheck

Enable gateway health check.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulShutdown

1-65535, in unit of seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulShutdownEnable

Enable graceful shutdown.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HonorServerResponseTtl

Honor the server reponse TTL.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HwCompression

Use hardware compression.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HwSynRr

Configure hardware SYN round robin (range 1-500000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

Specify the healthcheck interval, default is 5 seconds (Interval Value, in seconds (default 5)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L2l3TrunkLbDisable

Disable L2/L3 trunk LB.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogForResetUnknownConn

Log when rate exceed.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LowLatency

Enable low latency mode.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBuffQueuedPerConn

Set per connection buffer threshold (Buffer value range 128-4096).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxHttpHeaderCount

Set maximum number of HTTP headers allowed.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLocalRate

Set maximum local rate.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRemoteRate

Set maximum remote rate.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MslTime

Configure maximum session life, default is 2 seconds (1-40 seconds, default is 2 seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MssTable

Set MSS table (128-750, default is 536).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoAutoUpOnAflex

Don’t automatically mark vport up when aFleX is bound.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverridePort

Enable override port in DSR health check mode.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PktRateForResetUnknownConn

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlayerIdCheckEnable

Enable the Player id check.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Range

auto translate port range.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeEnd

port range end.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeStart

port range start.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimitLogging

Configure rate limit logging.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetStaleSession

Send reset if session in delete queue receives a SYN packet.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolvePortConflict

Enable client port service port conflicts.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseType

‘single-answer’: Only cache DNS response with single answer; ‘round-robin’: Round robin;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleOut

Enable SLB scale out.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnatGwyForL3

Use source NAT gateway for L3 traffic.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnatOnVip

Enable source NAT traffic against VIP.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Software

Software.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SortRes

Enable SLB sorting of resource names.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsliSniHashEnable

Enable SSLi SNI hash table.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatelessSgMultiBinding

Enable stateless service groups to be assigned to multiple L2/L3 DSR VIPs.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatsDataDisable

Disable global slb data statistics.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Specify the healthcheck timeout value, default is 15 seconds (Timeout Value, in seconds (default 15)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TtlThreshold

Only cache DNS response with longer TTL.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseMssTab

Use MSS based on internal table for SLB processing.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnRateLimit

_Required_: No

_Type_: List of <a href="connratelimitdefinition.md">ConnRateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdosProtection

_Required_: No

_Type_: List of <a href="ddosprotectiondefinition.md">DdosProtectionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsResponseRateLimiting

_Required_: No

_Type_: List of <a href="dnsresponseratelimitingdefinition.md">DnsResponseRateLimitingDefinition</a>

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

