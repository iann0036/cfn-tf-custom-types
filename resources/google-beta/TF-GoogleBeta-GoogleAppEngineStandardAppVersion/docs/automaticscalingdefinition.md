# TF::GoogleBeta::GoogleAppEngineStandardAppVersion AutomaticScalingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxconcurrentrequests" title="MaxConcurrentRequests">MaxConcurrentRequests</a>" : <i>Double</i>,
    "<a href="#maxidleinstances" title="MaxIdleInstances">MaxIdleInstances</a>" : <i>Double</i>,
    "<a href="#maxpendinglatency" title="MaxPendingLatency">MaxPendingLatency</a>" : <i>String</i>,
    "<a href="#minidleinstances" title="MinIdleInstances">MinIdleInstances</a>" : <i>Double</i>,
    "<a href="#minpendinglatency" title="MinPendingLatency">MinPendingLatency</a>" : <i>String</i>,
    "<a href="#standardschedulersettings" title="StandardSchedulerSettings">StandardSchedulerSettings</a>" : <i>[ <a href="standardschedulersettingsdefinition.md">StandardSchedulerSettingsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#maxconcurrentrequests" title="MaxConcurrentRequests">MaxConcurrentRequests</a>: <i>Double</i>
<a href="#maxidleinstances" title="MaxIdleInstances">MaxIdleInstances</a>: <i>Double</i>
<a href="#maxpendinglatency" title="MaxPendingLatency">MaxPendingLatency</a>: <i>String</i>
<a href="#minidleinstances" title="MinIdleInstances">MinIdleInstances</a>: <i>Double</i>
<a href="#minpendinglatency" title="MinPendingLatency">MinPendingLatency</a>: <i>String</i>
<a href="#standardschedulersettings" title="StandardSchedulerSettings">StandardSchedulerSettings</a>: <i>
      - <a href="standardschedulersettingsdefinition.md">StandardSchedulerSettingsDefinition</a></i>
</pre>

## Properties

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

#### MinIdleInstances

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinPendingLatency

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StandardSchedulerSettings

_Required_: No

_Type_: List of <a href="standardschedulersettingsdefinition.md">StandardSchedulerSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

