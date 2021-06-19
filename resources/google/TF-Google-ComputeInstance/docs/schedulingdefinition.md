# TF::Google::ComputeInstance SchedulingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#automaticrestart" title="AutomaticRestart">AutomaticRestart</a>" : <i>Boolean</i>,
    "<a href="#minnodecpus" title="MinNodeCpus">MinNodeCpus</a>" : <i>Double</i>,
    "<a href="#onhostmaintenance" title="OnHostMaintenance">OnHostMaintenance</a>" : <i>String</i>,
    "<a href="#preemptible" title="Preemptible">Preemptible</a>" : <i>Boolean</i>,
    "<a href="#nodeaffinities" title="NodeAffinities">NodeAffinities</a>" : <i>[ <a href="nodeaffinitiesdefinition.md">NodeAffinitiesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#automaticrestart" title="AutomaticRestart">AutomaticRestart</a>: <i>Boolean</i>
<a href="#minnodecpus" title="MinNodeCpus">MinNodeCpus</a>: <i>Double</i>
<a href="#onhostmaintenance" title="OnHostMaintenance">OnHostMaintenance</a>: <i>String</i>
<a href="#preemptible" title="Preemptible">Preemptible</a>: <i>Boolean</i>
<a href="#nodeaffinities" title="NodeAffinities">NodeAffinities</a>: <i>
      - <a href="nodeaffinitiesdefinition.md">NodeAffinitiesDefinition</a></i>
</pre>

## Properties

#### AutomaticRestart

Specifies if the instance should be
restarted if it was terminated by Compute Engine (not a user).
Defaults to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinNodeCpus

The minimum number of virtual CPUs this instance will consume when running on a sole-tenant node.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnHostMaintenance

Describes maintenance behavior for the
instance. Can be MIGRATE or TERMINATE, for more info, read
[here](https://cloud.google.com/compute/docs/instances/setting-instance-scheduling-options).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preemptible

Specifies if the instance is preemptible.
If this field is set to true, then `automatic_restart` must be
set to false.  Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeAffinities

_Required_: No

_Type_: List of <a href="nodeaffinitiesdefinition.md">NodeAffinitiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

