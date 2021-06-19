# TF::Google::ComputeInstanceTemplate SchedulingDefinition

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

Specifies whether the instance should be
automatically restarted if it is terminated by Compute Engine (not
terminated by a user). This defaults to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinNodeCpus

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnHostMaintenance

Defines the maintenance behavior for this
instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preemptible

Allows instance to be preempted. This defaults to
false. Read more on this
[here](https://cloud.google.com/compute/docs/instances/preemptible).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeAffinities

_Required_: No

_Type_: List of <a href="nodeaffinitiesdefinition.md">NodeAffinitiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

