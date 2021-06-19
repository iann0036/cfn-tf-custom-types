# TF::GoogleBeta::GoogleAppEngineFlexibleAppVersion AutomaticScalingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cooldownperiod" title="CoolDownPeriod">CoolDownPeriod</a>" : <i>String</i>,
    "<a href="#maxconcurrentrequests" title="MaxConcurrentRequests">MaxConcurrentRequests</a>" : <i>Double</i>,
    "<a href="#maxidleinstances" title="MaxIdleInstances">MaxIdleInstances</a>" : <i>Double</i>,
    "<a href="#maxpendinglatency" title="MaxPendingLatency">MaxPendingLatency</a>" : <i>String</i>,
    "<a href="#maxtotalinstances" title="MaxTotalInstances">MaxTotalInstances</a>" : <i>Double</i>,
    "<a href="#minidleinstances" title="MinIdleInstances">MinIdleInstances</a>" : <i>Double</i>,
    "<a href="#minpendinglatency" title="MinPendingLatency">MinPendingLatency</a>" : <i>String</i>,
    "<a href="#mintotalinstances" title="MinTotalInstances">MinTotalInstances</a>" : <i>Double</i>,
    "<a href="#cpuutilization" title="CpuUtilization">CpuUtilization</a>" : <i>[ <a href="cpuutilizationdefinition.md">CpuUtilizationDefinition</a>, ... ]</i>,
    "<a href="#diskutilization" title="DiskUtilization">DiskUtilization</a>" : <i>[ <a href="diskutilizationdefinition.md">DiskUtilizationDefinition</a>, ... ]</i>,
    "<a href="#networkutilization" title="NetworkUtilization">NetworkUtilization</a>" : <i>[ <a href="networkutilizationdefinition.md">NetworkUtilizationDefinition</a>, ... ]</i>,
    "<a href="#requestutilization" title="RequestUtilization">RequestUtilization</a>" : <i>[ <a href="requestutilizationdefinition.md">RequestUtilizationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cooldownperiod" title="CoolDownPeriod">CoolDownPeriod</a>: <i>String</i>
<a href="#maxconcurrentrequests" title="MaxConcurrentRequests">MaxConcurrentRequests</a>: <i>Double</i>
<a href="#maxidleinstances" title="MaxIdleInstances">MaxIdleInstances</a>: <i>Double</i>
<a href="#maxpendinglatency" title="MaxPendingLatency">MaxPendingLatency</a>: <i>String</i>
<a href="#maxtotalinstances" title="MaxTotalInstances">MaxTotalInstances</a>: <i>Double</i>
<a href="#minidleinstances" title="MinIdleInstances">MinIdleInstances</a>: <i>Double</i>
<a href="#minpendinglatency" title="MinPendingLatency">MinPendingLatency</a>: <i>String</i>
<a href="#mintotalinstances" title="MinTotalInstances">MinTotalInstances</a>: <i>Double</i>
<a href="#cpuutilization" title="CpuUtilization">CpuUtilization</a>: <i>
      - <a href="cpuutilizationdefinition.md">CpuUtilizationDefinition</a></i>
<a href="#diskutilization" title="DiskUtilization">DiskUtilization</a>: <i>
      - <a href="diskutilizationdefinition.md">DiskUtilizationDefinition</a></i>
<a href="#networkutilization" title="NetworkUtilization">NetworkUtilization</a>: <i>
      - <a href="networkutilizationdefinition.md">NetworkUtilizationDefinition</a></i>
<a href="#requestutilization" title="RequestUtilization">RequestUtilization</a>: <i>
      - <a href="requestutilizationdefinition.md">RequestUtilizationDefinition</a></i>
</pre>

## Properties

#### CoolDownPeriod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentRequests

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxIdleInstances

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPendingLatency

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTotalInstances

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinIdleInstances

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinPendingLatency

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTotalInstances

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuUtilization

_Required_: No

_Type_: List of <a href="cpuutilizationdefinition.md">CpuUtilizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskUtilization

_Required_: No

_Type_: List of <a href="diskutilizationdefinition.md">DiskUtilizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkUtilization

_Required_: No

_Type_: List of <a href="networkutilizationdefinition.md">NetworkUtilizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestUtilization

_Required_: No

_Type_: List of <a href="requestutilizationdefinition.md">RequestUtilizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

