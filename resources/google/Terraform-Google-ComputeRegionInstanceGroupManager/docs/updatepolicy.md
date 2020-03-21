# Terraform::Google::ComputeRegionInstanceGroupManager UpdatePolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#instanceredistributiontype" title="InstanceRedistributionType">InstanceRedistributionType</a>" : <i>String</i>,
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
<a href="#instanceredistributiontype" title="InstanceRedistributionType">InstanceRedistributionType</a>: <i>String</i>
<a href="#maxsurgefixed" title="MaxSurgeFixed">MaxSurgeFixed</a>: <i>Double</i>
<a href="#maxsurgepercent" title="MaxSurgePercent">MaxSurgePercent</a>: <i>Double</i>
<a href="#maxunavailablefixed" title="MaxUnavailableFixed">MaxUnavailableFixed</a>: <i>Double</i>
<a href="#maxunavailablepercent" title="MaxUnavailablePercent">MaxUnavailablePercent</a>: <i>Double</i>
<a href="#minreadysec" title="MinReadySec">MinReadySec</a>: <i>Double</i>
<a href="#minimalaction" title="MinimalAction">MinimalAction</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### InstanceRedistributionType

- The instance redistribution policy for regional managed instance groups. Valid values are: `"PROACTIVE"`, `"NONE"`. If `PROACTIVE` (default), the group attempts to maintain an even distribution of VM instances across zones in the region. If `NONE`, proactive redistribution is disabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSurgeFixed

, The maximum number of instances that can be created above the specified targetSize during the update process. Conflicts with `max_surge_percent`. It has to be either 0 or at least equal to the number of zones.  If fixed values are used, at least one of `max_unavailable_fixed` or `max_surge_fixed` must be greater than 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSurgePercent

, The maximum number of instances(calculated as percentage) that can be created above the specified targetSize during the update process. Conflicts with `max_surge_fixed`. Percent value is only allowed for regional managed instance groups with size at least 10.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUnavailableFixed

, The maximum number of instances that can be unavailable during the update process. Conflicts with `max_unavailable_percent`. It has to be either 0 or at least equal to the number of zones. If fixed values are used, at least one of `max_unavailable_fixed` or `max_surge_fixed` must be greater than 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUnavailablePercent

, The maximum number of instances(calculated as percentage) that can be unavailable during the update process. Conflicts with `max_unavailable_fixed`. Percent value is only allowed for regional managed instance groups with size at least 10.

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

