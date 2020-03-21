# Terraform::Google::ComputeInstanceGroupManager UpdatePolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxsurgefixed" title="MaxSurgeFixed">MaxSurgeFixed</a>" : <i>Double</i>,
    "<a href="#maxsurgepercent" title="MaxSurgePercent">MaxSurgePercent</a>" : <i>Double</i>,
    "<a href="#maxunavailablefixed" title="MaxUnavailableFixed">MaxUnavailableFixed</a>" : <i>Double</i>,
    "<a href="#maxunavailablepercent" title="MaxUnavailablePercent">MaxUnavailablePercent</a>" : <i>Double</i>,
    "<a href="#minreadysec" title="MinReadySec">MinReadySec</a>" : <i>Double</i>,
    "<a href="#minimalaction" title="MinimalAction">MinimalAction</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#maxsurgefixed" title="MaxSurgeFixed">MaxSurgeFixed</a>: <i>Double</i>
<a href="#maxsurgepercent" title="MaxSurgePercent">MaxSurgePercent</a>: <i>Double</i>
<a href="#maxunavailablefixed" title="MaxUnavailableFixed">MaxUnavailableFixed</a>: <i>Double</i>
<a href="#maxunavailablepercent" title="MaxUnavailablePercent">MaxUnavailablePercent</a>: <i>Double</i>
<a href="#minreadysec" title="MinReadySec">MinReadySec</a>: <i>Double</i>
<a href="#minimalaction" title="MinimalAction">MinimalAction</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### MaxSurgeFixed

, The maximum number of instances that can be created above the specified targetSize during the update process. Conflicts with `max_surge_percent`. If neither is set, defaults to 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSurgePercent

, The maximum number of instances(calculated as percentage) that can be created above the specified targetSize during the update process. Conflicts with `max_surge_fixed`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUnavailableFixed

, The maximum number of instances that can be unavailable during the update process. Conflicts with `max_unavailable_percent`. If neither is set, defaults to 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUnavailablePercent

, The maximum number of instances(calculated as percentage) that can be unavailable during the update process. Conflicts with `max_unavailable_fixed`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinReadySec

, Minimum number of seconds to wait for after a newly created instance becomes available. This value must be from range [0, 3600]
- - -.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimalAction

- Minimal action to be taken on an instance. You can specify either `RESTART` to restart existing instances or `REPLACE` to delete and create new instances from the target template. If you specify a `RESTART`, the Updater will attempt to perform that action only. However, if the Updater determines that the minimal action you specify is not enough to perform the update, it might perform a more disruptive action.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

- The type of update process. You can specify either `PROACTIVE` so that the instance group manager proactively executes actions in order to bring instances to their target versions or `OPPORTUNISTIC` so that no action is proactively executed but the update will be performed as part of other actions (for example, resizes or recreateInstances calls).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

