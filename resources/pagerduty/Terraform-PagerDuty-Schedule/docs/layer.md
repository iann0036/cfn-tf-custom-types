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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationTurnLengthSeconds

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationVirtualStart

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Start

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restriction

_Required_: No

_Type_: List of <a href="layer-restriction.md">Restriction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

