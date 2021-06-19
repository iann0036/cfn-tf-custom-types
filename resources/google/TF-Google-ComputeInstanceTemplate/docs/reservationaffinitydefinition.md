# TF::Google::ComputeInstanceTemplate ReservationAffinityDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#specificreservation" title="SpecificReservation">SpecificReservation</a>" : <i>[ <a href="specificreservationdefinition.md">SpecificReservationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#specificreservation" title="SpecificReservation">SpecificReservation</a>: <i>
      - <a href="specificreservationdefinition.md">SpecificReservationDefinition</a></i>
</pre>

## Properties

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpecificReservation

_Required_: No

_Type_: List of <a href="specificreservationdefinition.md">SpecificReservationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

