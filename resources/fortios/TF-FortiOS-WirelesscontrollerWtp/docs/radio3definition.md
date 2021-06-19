# TF::FortiOS::WirelesscontrollerWtp Radio3Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autopowerhigh" title="AutoPowerHigh">AutoPowerHigh</a>" : <i>Double</i>,
    "<a href="#autopowerlevel" title="AutoPowerLevel">AutoPowerLevel</a>" : <i>String</i>,
    "<a href="#autopowerlow" title="AutoPowerLow">AutoPowerLow</a>" : <i>Double</i>,
    "<a href="#autopowertarget" title="AutoPowerTarget">AutoPowerTarget</a>" : <i>String</i>,
    "<a href="#band" title="Band">Band</a>" : <i>String</i>,
    "<a href="#drmamanualmode" title="DrmaManualMode">DrmaManualMode</a>" : <i>String</i>,
    "<a href="#overrideanalysis" title="OverrideAnalysis">OverrideAnalysis</a>" : <i>String</i>,
    "<a href="#overrideband" title="OverrideBand">OverrideBand</a>" : <i>String</i>,
    "<a href="#overridechannel" title="OverrideChannel">OverrideChannel</a>" : <i>String</i>,
    "<a href="#overridetxpower" title="OverrideTxpower">OverrideTxpower</a>" : <i>String</i>,
    "<a href="#overridevaps" title="OverrideVaps">OverrideVaps</a>" : <i>String</i>,
    "<a href="#powerlevel" title="PowerLevel">PowerLevel</a>" : <i>Double</i>,
    "<a href="#spectrumanalysis" title="SpectrumAnalysis">SpectrumAnalysis</a>" : <i>String</i>,
    "<a href="#vapall" title="VapAll">VapAll</a>" : <i>String</i>,
    "<a href="#channel" title="Channel">Channel</a>" : <i>[ <a href="channeldefinition.md">ChannelDefinition</a>, ... ]</i>,
    "<a href="#vaps" title="Vaps">Vaps</a>" : <i>[ <a href="vapsdefinition.md">VapsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autopowerhigh" title="AutoPowerHigh">AutoPowerHigh</a>: <i>Double</i>
<a href="#autopowerlevel" title="AutoPowerLevel">AutoPowerLevel</a>: <i>String</i>
<a href="#autopowerlow" title="AutoPowerLow">AutoPowerLow</a>: <i>Double</i>
<a href="#autopowertarget" title="AutoPowerTarget">AutoPowerTarget</a>: <i>String</i>
<a href="#band" title="Band">Band</a>: <i>String</i>
<a href="#drmamanualmode" title="DrmaManualMode">DrmaManualMode</a>: <i>String</i>
<a href="#overrideanalysis" title="OverrideAnalysis">OverrideAnalysis</a>: <i>String</i>
<a href="#overrideband" title="OverrideBand">OverrideBand</a>: <i>String</i>
<a href="#overridechannel" title="OverrideChannel">OverrideChannel</a>: <i>String</i>
<a href="#overridetxpower" title="OverrideTxpower">OverrideTxpower</a>: <i>String</i>
<a href="#overridevaps" title="OverrideVaps">OverrideVaps</a>: <i>String</i>
<a href="#powerlevel" title="PowerLevel">PowerLevel</a>: <i>Double</i>
<a href="#spectrumanalysis" title="SpectrumAnalysis">SpectrumAnalysis</a>: <i>String</i>
<a href="#vapall" title="VapAll">VapAll</a>: <i>String</i>
<a href="#channel" title="Channel">Channel</a>: <i>
      - <a href="channeldefinition.md">ChannelDefinition</a></i>
<a href="#vaps" title="Vaps">Vaps</a>: <i>
      - <a href="vapsdefinition.md">VapsDefinition</a></i>
</pre>

## Properties

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

#### DrmaManualMode

Radio mode to be used for DRMA manual mode (default = ncf). Valid values: `ap`, `monitor`, `ncf`, `ncf-peek`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideAnalysis

Enable to override the WTP profile spectrum analysis configuration. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideBand

Enable to override the WTP profile band setting. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideChannel

Enable to override WTP profile channel settings. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideTxpower

Enable to override the WTP profile power level configuration. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideVaps

Enable to override WTP profile Virtual Access Point (VAP) settings. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PowerLevel

Radio power level as a percentage of the maximum transmit power (0 - 100, default = 100).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpectrumAnalysis

Enable/disable spectrum analysis to find interference that would negatively impact wireless performance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VapAll

Enable/disable the automatic inheritance of all Virtual Access Points (VAPs) (default = enable).

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

