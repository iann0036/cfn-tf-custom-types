# TF::FortiOS::SystemHa

Configure HA.

Due to the limitations of the current system, the feature is temporarily unavailable. Please use the following resource configuration as an alternative.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemHa",
    "Properties" : {
        "<a href="#arps" title="Arps">Arps</a>" : <i>Double</i>,
        "<a href="#arpsinterval" title="ArpsInterval">ArpsInterval</a>" : <i>Double</i>,
        "<a href="#authentication" title="Authentication">Authentication</a>" : <i>String</i>,
        "<a href="#cputhreshold" title="CpuThreshold">CpuThreshold</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#encryption" title="Encryption">Encryption</a>" : <i>String</i>,
        "<a href="#ftpproxythreshold" title="FtpProxyThreshold">FtpProxyThreshold</a>" : <i>String</i>,
        "<a href="#gratuitousarps" title="GratuitousArps">GratuitousArps</a>" : <i>String</i>,
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>Double</i>,
        "<a href="#groupname" title="GroupName">GroupName</a>" : <i>String</i>,
        "<a href="#hadirect" title="HaDirect">HaDirect</a>" : <i>String</i>,
        "<a href="#haethtype" title="HaEthType">HaEthType</a>" : <i>String</i>,
        "<a href="#hamgmtstatus" title="HaMgmtStatus">HaMgmtStatus</a>" : <i>String</i>,
        "<a href="#hauptimediffmargin" title="HaUptimeDiffMargin">HaUptimeDiffMargin</a>" : <i>Double</i>,
        "<a href="#hbinterval" title="HbInterval">HbInterval</a>" : <i>Double</i>,
        "<a href="#hblostthreshold" title="HbLostThreshold">HbLostThreshold</a>" : <i>Double</i>,
        "<a href="#hbdev" title="Hbdev">Hbdev</a>" : <i>String</i>,
        "<a href="#hcethtype" title="HcEthType">HcEthType</a>" : <i>String</i>,
        "<a href="#helloholddown" title="HelloHolddown">HelloHolddown</a>" : <i>Double</i>,
        "<a href="#httpproxythreshold" title="HttpProxyThreshold">HttpProxyThreshold</a>" : <i>String</i>,
        "<a href="#imapproxythreshold" title="ImapProxyThreshold">ImapProxyThreshold</a>" : <i>String</i>,
        "<a href="#interclustersessionsync" title="InterClusterSessionSync">InterClusterSessionSync</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#l2epethtype" title="L2epEthType">L2epEthType</a>" : <i>String</i>,
        "<a href="#linkfailedsignal" title="LinkFailedSignal">LinkFailedSignal</a>" : <i>String</i>,
        "<a href="#loadbalanceall" title="LoadBalanceAll">LoadBalanceAll</a>" : <i>String</i>,
        "<a href="#logicalsn" title="LogicalSn">LogicalSn</a>" : <i>String</i>,
        "<a href="#memorycompatiblemode" title="MemoryCompatibleMode">MemoryCompatibleMode</a>" : <i>String</i>,
        "<a href="#memorythreshold" title="MemoryThreshold">MemoryThreshold</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#monitor" title="Monitor">Monitor</a>" : <i>String</i>,
        "<a href="#multicastttl" title="MulticastTtl">MulticastTtl</a>" : <i>Double</i>,
        "<a href="#nntpproxythreshold" title="NntpProxyThreshold">NntpProxyThreshold</a>" : <i>String</i>,
        "<a href="#override" title="Override">Override</a>" : <i>String</i>,
        "<a href="#overridewaittime" title="OverrideWaitTime">OverrideWaitTime</a>" : <i>Double</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#pingserverfailoverthreshold" title="PingserverFailoverThreshold">PingserverFailoverThreshold</a>" : <i>Double</i>,
        "<a href="#pingserverfliptimeout" title="PingserverFlipTimeout">PingserverFlipTimeout</a>" : <i>Double</i>,
        "<a href="#pingservermonitorinterface" title="PingserverMonitorInterface">PingserverMonitorInterface</a>" : <i>String</i>,
        "<a href="#pingserversecondaryforcereset" title="PingserverSecondaryForceReset">PingserverSecondaryForceReset</a>" : <i>String</i>,
        "<a href="#pingserverslaveforcereset" title="PingserverSlaveForceReset">PingserverSlaveForceReset</a>" : <i>String</i>,
        "<a href="#pop3proxythreshold" title="Pop3ProxyThreshold">Pop3ProxyThreshold</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#routehold" title="RouteHold">RouteHold</a>" : <i>Double</i>,
        "<a href="#routettl" title="RouteTtl">RouteTtl</a>" : <i>Double</i>,
        "<a href="#routewait" title="RouteWait">RouteWait</a>" : <i>Double</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
        "<a href="#sessionpickup" title="SessionPickup">SessionPickup</a>" : <i>String</i>,
        "<a href="#sessionpickupconnectionless" title="SessionPickupConnectionless">SessionPickupConnectionless</a>" : <i>String</i>,
        "<a href="#sessionpickupdelay" title="SessionPickupDelay">SessionPickupDelay</a>" : <i>String</i>,
        "<a href="#sessionpickupexpectation" title="SessionPickupExpectation">SessionPickupExpectation</a>" : <i>String</i>,
        "<a href="#sessionpickupnat" title="SessionPickupNat">SessionPickupNat</a>" : <i>String</i>,
        "<a href="#sessionsyncdev" title="SessionSyncDev">SessionSyncDev</a>" : <i>String</i>,
        "<a href="#smtpproxythreshold" title="SmtpProxyThreshold">SmtpProxyThreshold</a>" : <i>String</i>,
        "<a href="#ssdfailover" title="SsdFailover">SsdFailover</a>" : <i>String</i>,
        "<a href="#standaloneconfigsync" title="StandaloneConfigSync">StandaloneConfigSync</a>" : <i>String</i>,
        "<a href="#standalonemgmtvdom" title="StandaloneMgmtVdom">StandaloneMgmtVdom</a>" : <i>String</i>,
        "<a href="#syncconfig" title="SyncConfig">SyncConfig</a>" : <i>String</i>,
        "<a href="#syncpacketbalance" title="SyncPacketBalance">SyncPacketBalance</a>" : <i>String</i>,
        "<a href="#unicasthb" title="UnicastHb">UnicastHb</a>" : <i>String</i>,
        "<a href="#unicasthbnetmask" title="UnicastHbNetmask">UnicastHbNetmask</a>" : <i>String</i>,
        "<a href="#unicasthbpeerip" title="UnicastHbPeerip">UnicastHbPeerip</a>" : <i>String</i>,
        "<a href="#uninterruptibleupgrade" title="UninterruptibleUpgrade">UninterruptibleUpgrade</a>" : <i>String</i>,
        "<a href="#vcluster2" title="Vcluster2">Vcluster2</a>" : <i>String</i>,
        "<a href="#vclusterid" title="VclusterId">VclusterId</a>" : <i>Double</i>,
        "<a href="#vdom" title="Vdom">Vdom</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#weight" title="Weight">Weight</a>" : <i>String</i>,
        "<a href="#hamgmtinterfaces" title="HaMgmtInterfaces">HaMgmtInterfaces</a>" : <i>[ <a href="hamgmtinterfacesdefinition.md">HaMgmtInterfacesDefinition</a>, ... ]</i>,
        "<a href="#secondaryvcluster" title="SecondaryVcluster">SecondaryVcluster</a>" : <i>[ <a href="secondaryvclusterdefinition.md">SecondaryVclusterDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemHa
Properties:
    <a href="#arps" title="Arps">Arps</a>: <i>Double</i>
    <a href="#arpsinterval" title="ArpsInterval">ArpsInterval</a>: <i>Double</i>
    <a href="#authentication" title="Authentication">Authentication</a>: <i>String</i>
    <a href="#cputhreshold" title="CpuThreshold">CpuThreshold</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#encryption" title="Encryption">Encryption</a>: <i>String</i>
    <a href="#ftpproxythreshold" title="FtpProxyThreshold">FtpProxyThreshold</a>: <i>String</i>
    <a href="#gratuitousarps" title="GratuitousArps">GratuitousArps</a>: <i>String</i>
    <a href="#groupid" title="GroupId">GroupId</a>: <i>Double</i>
    <a href="#groupname" title="GroupName">GroupName</a>: <i>String</i>
    <a href="#hadirect" title="HaDirect">HaDirect</a>: <i>String</i>
    <a href="#haethtype" title="HaEthType">HaEthType</a>: <i>String</i>
    <a href="#hamgmtstatus" title="HaMgmtStatus">HaMgmtStatus</a>: <i>String</i>
    <a href="#hauptimediffmargin" title="HaUptimeDiffMargin">HaUptimeDiffMargin</a>: <i>Double</i>
    <a href="#hbinterval" title="HbInterval">HbInterval</a>: <i>Double</i>
    <a href="#hblostthreshold" title="HbLostThreshold">HbLostThreshold</a>: <i>Double</i>
    <a href="#hbdev" title="Hbdev">Hbdev</a>: <i>String</i>
    <a href="#hcethtype" title="HcEthType">HcEthType</a>: <i>String</i>
    <a href="#helloholddown" title="HelloHolddown">HelloHolddown</a>: <i>Double</i>
    <a href="#httpproxythreshold" title="HttpProxyThreshold">HttpProxyThreshold</a>: <i>String</i>
    <a href="#imapproxythreshold" title="ImapProxyThreshold">ImapProxyThreshold</a>: <i>String</i>
    <a href="#interclustersessionsync" title="InterClusterSessionSync">InterClusterSessionSync</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#l2epethtype" title="L2epEthType">L2epEthType</a>: <i>String</i>
    <a href="#linkfailedsignal" title="LinkFailedSignal">LinkFailedSignal</a>: <i>String</i>
    <a href="#loadbalanceall" title="LoadBalanceAll">LoadBalanceAll</a>: <i>String</i>
    <a href="#logicalsn" title="LogicalSn">LogicalSn</a>: <i>String</i>
    <a href="#memorycompatiblemode" title="MemoryCompatibleMode">MemoryCompatibleMode</a>: <i>String</i>
    <a href="#memorythreshold" title="MemoryThreshold">MemoryThreshold</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#monitor" title="Monitor">Monitor</a>: <i>String</i>
    <a href="#multicastttl" title="MulticastTtl">MulticastTtl</a>: <i>Double</i>
    <a href="#nntpproxythreshold" title="NntpProxyThreshold">NntpProxyThreshold</a>: <i>String</i>
    <a href="#override" title="Override">Override</a>: <i>String</i>
    <a href="#overridewaittime" title="OverrideWaitTime">OverrideWaitTime</a>: <i>Double</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#pingserverfailoverthreshold" title="PingserverFailoverThreshold">PingserverFailoverThreshold</a>: <i>Double</i>
    <a href="#pingserverfliptimeout" title="PingserverFlipTimeout">PingserverFlipTimeout</a>: <i>Double</i>
    <a href="#pingservermonitorinterface" title="PingserverMonitorInterface">PingserverMonitorInterface</a>: <i>String</i>
    <a href="#pingserversecondaryforcereset" title="PingserverSecondaryForceReset">PingserverSecondaryForceReset</a>: <i>String</i>
    <a href="#pingserverslaveforcereset" title="PingserverSlaveForceReset">PingserverSlaveForceReset</a>: <i>String</i>
    <a href="#pop3proxythreshold" title="Pop3ProxyThreshold">Pop3ProxyThreshold</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#routehold" title="RouteHold">RouteHold</a>: <i>Double</i>
    <a href="#routettl" title="RouteTtl">RouteTtl</a>: <i>Double</i>
    <a href="#routewait" title="RouteWait">RouteWait</a>: <i>Double</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
    <a href="#sessionpickup" title="SessionPickup">SessionPickup</a>: <i>String</i>
    <a href="#sessionpickupconnectionless" title="SessionPickupConnectionless">SessionPickupConnectionless</a>: <i>String</i>
    <a href="#sessionpickupdelay" title="SessionPickupDelay">SessionPickupDelay</a>: <i>String</i>
    <a href="#sessionpickupexpectation" title="SessionPickupExpectation">SessionPickupExpectation</a>: <i>String</i>
    <a href="#sessionpickupnat" title="SessionPickupNat">SessionPickupNat</a>: <i>String</i>
    <a href="#sessionsyncdev" title="SessionSyncDev">SessionSyncDev</a>: <i>String</i>
    <a href="#smtpproxythreshold" title="SmtpProxyThreshold">SmtpProxyThreshold</a>: <i>String</i>
    <a href="#ssdfailover" title="SsdFailover">SsdFailover</a>: <i>String</i>
    <a href="#standaloneconfigsync" title="StandaloneConfigSync">StandaloneConfigSync</a>: <i>String</i>
    <a href="#standalonemgmtvdom" title="StandaloneMgmtVdom">StandaloneMgmtVdom</a>: <i>String</i>
    <a href="#syncconfig" title="SyncConfig">SyncConfig</a>: <i>String</i>
    <a href="#syncpacketbalance" title="SyncPacketBalance">SyncPacketBalance</a>: <i>String</i>
    <a href="#unicasthb" title="UnicastHb">UnicastHb</a>: <i>String</i>
    <a href="#unicasthbnetmask" title="UnicastHbNetmask">UnicastHbNetmask</a>: <i>String</i>
    <a href="#unicasthbpeerip" title="UnicastHbPeerip">UnicastHbPeerip</a>: <i>String</i>
    <a href="#uninterruptibleupgrade" title="UninterruptibleUpgrade">UninterruptibleUpgrade</a>: <i>String</i>
    <a href="#vcluster2" title="Vcluster2">Vcluster2</a>: <i>String</i>
    <a href="#vclusterid" title="VclusterId">VclusterId</a>: <i>Double</i>
    <a href="#vdom" title="Vdom">Vdom</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#weight" title="Weight">Weight</a>: <i>String</i>
    <a href="#hamgmtinterfaces" title="HaMgmtInterfaces">HaMgmtInterfaces</a>: <i>
      - <a href="hamgmtinterfacesdefinition.md">HaMgmtInterfacesDefinition</a></i>
    <a href="#secondaryvcluster" title="SecondaryVcluster">SecondaryVcluster</a>: <i>
      - <a href="secondaryvclusterdefinition.md">SecondaryVclusterDefinition</a></i>
</pre>

## Properties

#### Arps

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArpsInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authentication

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuThreshold

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encryption

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtpProxyThreshold

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GratuitousArps

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaDirect

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaEthType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaMgmtStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaUptimeDiffMargin

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HbInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HbLostThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hbdev

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HcEthType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HelloHolddown

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpProxyThreshold

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImapProxyThreshold

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterClusterSessionSync

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L2epEthType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkFailedSignal

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalanceAll

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogicalSn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryCompatibleMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryThreshold

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitor

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MulticastTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NntpProxyThreshold

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Override

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideWaitTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PingserverFailoverThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PingserverFlipTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PingserverMonitorInterface

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PingserverSecondaryForceReset

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PingserverSlaveForceReset

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pop3ProxyThreshold

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteHold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteWait

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionPickup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionPickupConnectionless

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionPickupDelay

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionPickupExpectation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionPickupNat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionSyncDev

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmtpProxyThreshold

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsdFailover

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StandaloneConfigSync

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StandaloneMgmtVdom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyncConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyncPacketBalance

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnicastHb

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnicastHbNetmask

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnicastHbPeerip

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UninterruptibleUpgrade

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vcluster2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VclusterId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaMgmtInterfaces

_Required_: No

_Type_: List of <a href="hamgmtinterfacesdefinition.md">HaMgmtInterfacesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryVcluster

_Required_: No

_Type_: List of <a href="secondaryvclusterdefinition.md">SecondaryVclusterDefinition</a>

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

