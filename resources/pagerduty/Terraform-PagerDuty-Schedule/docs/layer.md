# Terraform::PagerDuty::Schedule Layer

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#end" title="End">End</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#rotationturnlengthseconds" title="RotationTurnLengthSeconds">RotationTurnLengthSeconds</a>" : <i>Double</i>,
    "<a href="#rotationvirtualstart" title="RotationVirtualStart">RotationVirtualStart</a>" : <i>String</i>,
    "<a href="#start" title="Start">Start</a>" : <i>String</i>,
    "<a href="#users" title="Users">Users</a>" : <i>[ String, ... ]</i>,
    "<a href="#restriction" title="Restriction">Restriction</a>" : <i>[ <a href="layer-restriction.md">Restriction</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#end" title="End">End</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#rotationturnlengthseconds" title="RotationTurnLengthSeconds">RotationTurnLengthSeconds</a>: <i>Double</i>
<a href="#rotationvirtualstart" title="RotationVirtualStart">RotationVirtualStart</a>: <i>String</i>
<a href="#start" title="Start">Start</a>: <i>String</i>
<a href="#users" title="Users">Users</a>: <i>
      - String</i>
<a href="#restriction" title="Restriction">Restriction</a>: <i>
      - <a href="layer-restriction.md">Restriction</a></i>
</pre>

## Properties

#### End

The end time of the schedule layer. If not specified, the layer does not end.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the schedule layer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationTurnLengthSeconds

The duration of each on-call shift in `seconds`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationVirtualStart

The effective start time of the schedule layer. This can be before the start time of the schedule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Start

The start time of the schedule layer. This value will not be read back from the PagerDuty API because the API will always return a new `start` time, which represents the last updated time of the schedule layer.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

The ordered list of users on this layer. The position of the user on the list determines their order in the layer.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restriction

_Required_: No

_Type_: List of <a href="layer-restriction.md">Restriction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

