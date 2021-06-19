# TF::Google::ContainerNodePool UpgradeSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxsurge" title="MaxSurge">MaxSurge</a>" : <i>Double</i>,
    "<a href="#maxunavailable" title="MaxUnavailable">MaxUnavailable</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#maxsurge" title="MaxSurge">MaxSurge</a>: <i>Double</i>
<a href="#maxunavailable" title="MaxUnavailable">MaxUnavailable</a>: <i>Double</i>
</pre>

## Properties

#### MaxSurge

The number of additional nodes that can be added to the node pool during
an upgrade. Increasing `max_surge` raises the number of nodes that can be upgraded simultaneously.
Can be set to 0 or greater.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUnavailable

The number of nodes that can be simultaneously unavailable during
an upgrade. Increasing `max_unavailable` raises the number of nodes that can be upgraded in
parallel. Can be set to 0 or greater.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

