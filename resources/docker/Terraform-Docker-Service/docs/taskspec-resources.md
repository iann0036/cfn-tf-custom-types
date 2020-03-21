# Terraform::Docker::Service TaskSpec Resources

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#limits" title="Limits">Limits</a>" : <i>[ <a href="taskspec-resources-limits.md">Limits</a>, ... ]</i>,
    "<a href="#reservation" title="Reservation">Reservation</a>" : <i>[ <a href="taskspec-resources-reservation.md">Reservation</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#limits" title="Limits">Limits</a>: <i>
      - <a href="taskspec-resources-limits.md">Limits</a></i>
<a href="#reservation" title="Reservation">Reservation</a>: <i>
      - <a href="taskspec-resources-reservation.md">Reservation</a></i>
</pre>

## Properties

#### Limits

_Required_: No

_Type_: List of <a href="taskspec-resources-limits.md">Limits</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reservation

_Required_: No

_Type_: List of <a href="taskspec-resources-reservation.md">Reservation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

