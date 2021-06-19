# TF::AWS::Instance CapacityReservationSpecificationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#capacityreservationpreference" title="CapacityReservationPreference">CapacityReservationPreference</a>" : <i>String</i>,
    "<a href="#capacityreservationtarget" title="CapacityReservationTarget">CapacityReservationTarget</a>" : <i>[ <a href="capacityreservationtargetdefinition.md">CapacityReservationTargetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#capacityreservationpreference" title="CapacityReservationPreference">CapacityReservationPreference</a>: <i>String</i>
<a href="#capacityreservationtarget" title="CapacityReservationTarget">CapacityReservationTarget</a>: <i>
      - <a href="capacityreservationtargetdefinition.md">CapacityReservationTargetDefinition</a></i>
</pre>

## Properties

#### CapacityReservationPreference

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityReservationTarget

_Required_: No

_Type_: List of <a href="capacityreservationtargetdefinition.md">CapacityReservationTargetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

