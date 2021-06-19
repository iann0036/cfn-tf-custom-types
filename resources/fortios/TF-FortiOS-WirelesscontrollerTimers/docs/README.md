# TF::FortiOS::WirelesscontrollerTimers

Configure CAPWAP timers.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WirelesscontrollerTimers",
    "Properties" : {
        "<a href="#blescanreportintv" title="BleScanReportIntv">BleScanReportIntv</a>" : <i>Double</i>,
        "<a href="#clientidletimeout" title="ClientIdleTimeout">ClientIdleTimeout</a>" : <i>Double</i>,
        "<a href="#darrpday" title="DarrpDay">DarrpDay</a>" : <i>String</i>,
        "<a href="#darrpoptimize" title="DarrpOptimize">DarrpOptimize</a>" : <i>Double</i>,
        "<a href="#discoveryinterval" title="DiscoveryInterval">DiscoveryInterval</a>" : <i>Double</i>,
        "<a href="#drmainterval" title="DrmaInterval">DrmaInterval</a>" : <i>Double</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#echointerval" title="EchoInterval">EchoInterval</a>" : <i>Double</i>,
        "<a href="#fakeaplog" title="FakeApLog">FakeApLog</a>" : <i>Double</i>,
        "<a href="#ipsecintfcleanup" title="IpsecIntfCleanup">IpsecIntfCleanup</a>" : <i>Double</i>,
        "<a href="#radiostatsinterval" title="RadioStatsInterval">RadioStatsInterval</a>" : <i>Double</i>,
        "<a href="#rogueaplog" title="RogueApLog">RogueApLog</a>" : <i>Double</i>,
        "<a href="#stacapabilityinterval" title="StaCapabilityInterval">StaCapabilityInterval</a>" : <i>Double</i>,
        "<a href="#stalocatetimer" title="StaLocateTimer">StaLocateTimer</a>" : <i>Double</i>,
        "<a href="#stastatsinterval" title="StaStatsInterval">StaStatsInterval</a>" : <i>Double</i>,
        "<a href="#vapstatsinterval" title="VapStatsInterval">VapStatsInterval</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#darrptime" title="DarrpTime">DarrpTime</a>" : <i>[ <a href="darrptimedefinition.md">DarrpTimeDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WirelesscontrollerTimers
Properties:
    <a href="#blescanreportintv" title="BleScanReportIntv">BleScanReportIntv</a>: <i>Double</i>
    <a href="#clientidletimeout" title="ClientIdleTimeout">ClientIdleTimeout</a>: <i>Double</i>
    <a href="#darrpday" title="DarrpDay">DarrpDay</a>: <i>String</i>
    <a href="#darrpoptimize" title="DarrpOptimize">DarrpOptimize</a>: <i>Double</i>
    <a href="#discoveryinterval" title="DiscoveryInterval">DiscoveryInterval</a>: <i>Double</i>
    <a href="#drmainterval" title="DrmaInterval">DrmaInterval</a>: <i>Double</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#echointerval" title="EchoInterval">EchoInterval</a>: <i>Double</i>
    <a href="#fakeaplog" title="FakeApLog">FakeApLog</a>: <i>Double</i>
    <a href="#ipsecintfcleanup" title="IpsecIntfCleanup">IpsecIntfCleanup</a>: <i>Double</i>
    <a href="#radiostatsinterval" title="RadioStatsInterval">RadioStatsInterval</a>: <i>Double</i>
    <a href="#rogueaplog" title="RogueApLog">RogueApLog</a>: <i>Double</i>
    <a href="#stacapabilityinterval" title="StaCapabilityInterval">StaCapabilityInterval</a>: <i>Double</i>
    <a href="#stalocatetimer" title="StaLocateTimer">StaLocateTimer</a>: <i>Double</i>
    <a href="#stastatsinterval" title="StaStatsInterval">StaStatsInterval</a>: <i>Double</i>
    <a href="#vapstatsinterval" title="VapStatsInterval">VapStatsInterval</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#darrptime" title="DarrpTime">DarrpTime</a>: <i>
      - <a href="darrptimedefinition.md">DarrpTimeDefinition</a></i>
</pre>

## Properties

#### BleScanReportIntv

Time between running Bluetooth Low Energy (BLE) reports (10 - 3600 sec, default = 30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientIdleTimeout

Time after which a client is considered idle and times out (20 - 3600 sec, default = 300, 0 for no timeout).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DarrpDay

Weekday on which to run DARRP optimization. Valid values: `sunday`, `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DarrpOptimize

Time for running Dynamic Automatic Radio Resource Provisioning (DARRP) optimizations (0 - 86400 sec, default = 1800).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiscoveryInterval

Time between discovery requests (2 - 180 sec, default = 5).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrmaInterval

Dynamic radio mode assignment (DRMA) schedule interval in minutes (10 - 1440, default = 60).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EchoInterval

Time between echo requests sent by the managed WTP, AP, or FortiAP (1 - 255 sec, default = 30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FakeApLog

Time between recording logs about fake APs if periodic fake AP logging is configured (0 - 1440 min, default = 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecIntfCleanup

Time period to keep IPsec VPN interfaces up after WTP sessions are disconnected (30 - 3600 sec, default = 120).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadioStatsInterval

Time between running radio reports (1 - 255 sec, default = 15).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RogueApLog

Time between logging rogue AP messages if periodic rogue AP logging is configured (0 - 1440 min, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaCapabilityInterval

Time between running station capability reports (1 - 255 sec, default = 30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaLocateTimer

Time between running client presence flushes to remove clients that are listed but no longer present (0 - 86400 sec, default = 1800).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaStatsInterval

Time between running client (station) reports (1 - 255 sec, default = 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VapStatsInterval

Time between running Virtual Access Point (VAP) reports (1 - 255 sec, default = 15).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DarrpTime

_Required_: No

_Type_: List of <a href="darrptimedefinition.md">DarrpTimeDefinition</a>

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

