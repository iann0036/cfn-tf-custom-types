# TF::FortiOS::WirelesscontrollerArrpprofile

Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles. Applies to FortiOS Version `>= 6.4.2`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WirelesscontrollerArrpprofile",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#includedfschannel" title="IncludeDfsChannel">IncludeDfsChannel</a>" : <i>String</i>,
        "<a href="#includeweatherchannel" title="IncludeWeatherChannel">IncludeWeatherChannel</a>" : <i>String</i>,
        "<a href="#monitorperiod" title="MonitorPeriod">MonitorPeriod</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#selectionperiod" title="SelectionPeriod">SelectionPeriod</a>" : <i>Double</i>,
        "<a href="#thresholdap" title="ThresholdAp">ThresholdAp</a>" : <i>Double</i>,
        "<a href="#thresholdchannelload" title="ThresholdChannelLoad">ThresholdChannelLoad</a>" : <i>Double</i>,
        "<a href="#thresholdnoisefloor" title="ThresholdNoiseFloor">ThresholdNoiseFloor</a>" : <i>String</i>,
        "<a href="#thresholdrxerrors" title="ThresholdRxErrors">ThresholdRxErrors</a>" : <i>Double</i>,
        "<a href="#thresholdspectralrssi" title="ThresholdSpectralRssi">ThresholdSpectralRssi</a>" : <i>String</i>,
        "<a href="#thresholdtxretries" title="ThresholdTxRetries">ThresholdTxRetries</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#weightchannelload" title="WeightChannelLoad">WeightChannelLoad</a>" : <i>Double</i>,
        "<a href="#weightdfschannel" title="WeightDfsChannel">WeightDfsChannel</a>" : <i>Double</i>,
        "<a href="#weightmanagedap" title="WeightManagedAp">WeightManagedAp</a>" : <i>Double</i>,
        "<a href="#weightnoisefloor" title="WeightNoiseFloor">WeightNoiseFloor</a>" : <i>Double</i>,
        "<a href="#weightrogueap" title="WeightRogueAp">WeightRogueAp</a>" : <i>Double</i>,
        "<a href="#weightspectralrssi" title="WeightSpectralRssi">WeightSpectralRssi</a>" : <i>Double</i>,
        "<a href="#weightweatherchannel" title="WeightWeatherChannel">WeightWeatherChannel</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WirelesscontrollerArrpprofile
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#includedfschannel" title="IncludeDfsChannel">IncludeDfsChannel</a>: <i>String</i>
    <a href="#includeweatherchannel" title="IncludeWeatherChannel">IncludeWeatherChannel</a>: <i>String</i>
    <a href="#monitorperiod" title="MonitorPeriod">MonitorPeriod</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#selectionperiod" title="SelectionPeriod">SelectionPeriod</a>: <i>Double</i>
    <a href="#thresholdap" title="ThresholdAp">ThresholdAp</a>: <i>Double</i>
    <a href="#thresholdchannelload" title="ThresholdChannelLoad">ThresholdChannelLoad</a>: <i>Double</i>
    <a href="#thresholdnoisefloor" title="ThresholdNoiseFloor">ThresholdNoiseFloor</a>: <i>String</i>
    <a href="#thresholdrxerrors" title="ThresholdRxErrors">ThresholdRxErrors</a>: <i>Double</i>
    <a href="#thresholdspectralrssi" title="ThresholdSpectralRssi">ThresholdSpectralRssi</a>: <i>String</i>
    <a href="#thresholdtxretries" title="ThresholdTxRetries">ThresholdTxRetries</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#weightchannelload" title="WeightChannelLoad">WeightChannelLoad</a>: <i>Double</i>
    <a href="#weightdfschannel" title="WeightDfsChannel">WeightDfsChannel</a>: <i>Double</i>
    <a href="#weightmanagedap" title="WeightManagedAp">WeightManagedAp</a>: <i>Double</i>
    <a href="#weightnoisefloor" title="WeightNoiseFloor">WeightNoiseFloor</a>: <i>Double</i>
    <a href="#weightrogueap" title="WeightRogueAp">WeightRogueAp</a>: <i>Double</i>
    <a href="#weightspectralrssi" title="WeightSpectralRssi">WeightSpectralRssi</a>: <i>Double</i>
    <a href="#weightweatherchannel" title="WeightWeatherChannel">WeightWeatherChannel</a>: <i>Double</i>
</pre>

## Properties

#### Comment

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeDfsChannel

Enable/disable use of DFS channel in DARRP channel selection phase 1 (default = disable).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeWeatherChannel

Enable/disable use of weather channel in DARRP channel selection phase 1 (default = disable).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorPeriod

Period in seconds to measure average transmit retries and receive errors (default = 300).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

WiFi ARRP profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectionPeriod

Period in seconds to measure average channel load, noise floor, spectral RSSI (default = 3600).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdAp

Threshold to reject channel in DARRP channel selection phase 1 due to surrounding APs (0 - 500, default = 250).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdChannelLoad

Threshold in percentage to reject channel in DARRP channel selection phase 1 due to channel load (0 - 100, default = 60).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdNoiseFloor

Threshold in dBm to reject channel in DARRP channel selection phase 1 due to noise floor (-95 to -20, default = -85).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdRxErrors

Threshold in percentage for receive errors to trigger channel reselection in DARRP monitor stage (0 - 100, default = 50).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdSpectralRssi

Threshold in dBm to reject channel in DARRP channel selection phase 1 due to spectral RSSI (-95 to -20, default = -65).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdTxRetries

Threshold in percentage for transmit retries to trigger channel reselection in DARRP monitor stage (0 - 1000, default = 300).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightChannelLoad

Weight in DARRP channel score calculation for channel load (0 - 2000, default = 20).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightDfsChannel

Weight in DARRP channel score calculation for DFS channel (0 - 2000, default = 500).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightManagedAp

Weight in DARRP channel score calculation for managed APs (0 - 2000, default = 50).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightNoiseFloor

Weight in DARRP channel score calculation for noise floor (0 - 2000, default = 40).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightRogueAp

Weight in DARRP channel score calculation for rogue APs (0 - 2000, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightSpectralRssi

Weight in DARRP channel score calculation for spectral RSSI (0 - 2000, default = 40).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightWeatherChannel

Weight in DARRP channel score calculation for weather channel (0 - 2000, default = 1000).

_Required_: No

_Type_: Double

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

