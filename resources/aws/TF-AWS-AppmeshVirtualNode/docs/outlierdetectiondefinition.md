# TF::AWS::AppmeshVirtualNode OutlierDetectionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxejectionpercent" title="MaxEjectionPercent">MaxEjectionPercent</a>" : <i>Double</i>,
    "<a href="#maxservererrors" title="MaxServerErrors">MaxServerErrors</a>" : <i>Double</i>,
    "<a href="#baseejectionduration" title="BaseEjectionDuration">BaseEjectionDuration</a>" : <i>[ <a href="baseejectiondurationdefinition.md">BaseEjectionDurationDefinition</a>, ... ]</i>,
    "<a href="#interval" title="Interval">Interval</a>" : <i>[ <a href="intervaldefinition.md">IntervalDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#maxejectionpercent" title="MaxEjectionPercent">MaxEjectionPercent</a>: <i>Double</i>
<a href="#maxservererrors" title="MaxServerErrors">MaxServerErrors</a>: <i>Double</i>
<a href="#baseejectionduration" title="BaseEjectionDuration">BaseEjectionDuration</a>: <i>
      - <a href="baseejectiondurationdefinition.md">BaseEjectionDurationDefinition</a></i>
<a href="#interval" title="Interval">Interval</a>: <i>
      - <a href="intervaldefinition.md">IntervalDefinition</a></i>
</pre>

## Properties

#### MaxEjectionPercent

Maximum percentage of hosts in load balancing pool for upstream service that can be ejected. Will eject at least one host regardless of the value.
Minimum value of `0`. Maximum value of `100`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxServerErrors

Number of consecutive `5xx` errors required for ejection. Minimum value of `1`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BaseEjectionDuration

_Required_: No

_Type_: List of <a href="baseejectiondurationdefinition.md">BaseEjectionDurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

_Required_: No

_Type_: List of <a href="intervaldefinition.md">IntervalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

