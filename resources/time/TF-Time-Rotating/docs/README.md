# TF::Time::Rotating

Manages a rotating time resource, which keeps a rotating UTC timestamp stored in the Terraform state and proposes resource recreation when the locally sourced current time is beyond the rotation time. This rotation only occurs when Terraform is executed, meaning there will be drift between the rotation timestamp and actual rotation. The new rotation timestamp offset includes this drift. This prevents perpetual differences caused by using the [`timestamp()` function](https://www.terraform.io/docs/configuration/functions/timestamp.html) by only forcing a new value on the set cadence.

-> Further manipulation of incoming or outgoing values can be accomplished with the [`formatdate()` function](https://www.terraform.io/docs/configuration/functions/formatdate.html) and the [`timeadd()` function](https://www.terraform.io/docs/configuration/functions/timeadd.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Time::Rotating",
    "Properties" : {
        "<a href="#rfc3339" title="Rfc3339">Rfc3339</a>" : <i>String</i>,
        "<a href="#rotationdays" title="RotationDays">RotationDays</a>" : <i>Double</i>,
        "<a href="#rotationhours" title="RotationHours">RotationHours</a>" : <i>Double</i>,
        "<a href="#rotationminutes" title="RotationMinutes">RotationMinutes</a>" : <i>Double</i>,
        "<a href="#rotationmonths" title="RotationMonths">RotationMonths</a>" : <i>Double</i>,
        "<a href="#rotationrfc3339" title="RotationRfc3339">RotationRfc3339</a>" : <i>String</i>,
        "<a href="#rotationyears" title="RotationYears">RotationYears</a>" : <i>Double</i>,
        "<a href="#triggers" title="Triggers">Triggers</a>" : <i>[ <a href="triggersdefinition.md">TriggersDefinition</a>, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Time::Rotating
Properties:
    <a href="#rfc3339" title="Rfc3339">Rfc3339</a>: <i>String</i>
    <a href="#rotationdays" title="RotationDays">RotationDays</a>: <i>Double</i>
    <a href="#rotationhours" title="RotationHours">RotationHours</a>: <i>Double</i>
    <a href="#rotationminutes" title="RotationMinutes">RotationMinutes</a>: <i>Double</i>
    <a href="#rotationmonths" title="RotationMonths">RotationMonths</a>: <i>Double</i>
    <a href="#rotationrfc3339" title="RotationRfc3339">RotationRfc3339</a>: <i>String</i>
    <a href="#rotationyears" title="RotationYears">RotationYears</a>: <i>Double</i>
    <a href="#triggers" title="Triggers">Triggers</a>: <i>
      - <a href="triggersdefinition.md">TriggersDefinition</a></i>
</pre>

## Properties

#### Rfc3339

Configure the base timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationDays

Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationHours

Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationMinutes

Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationMonths

Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationRfc3339

Configure the rotation timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationYears

Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Triggers

Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions recreate the resource in addition to other rotation arguments. See [the main provider documentation](../index.html) for more information.

_Required_: No

_Type_: List of <a href="triggersdefinition.md">TriggersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Day

Returns the <code>Day</code> value.

#### Hour

Returns the <code>Hour</code> value.

#### Id

Returns the <code>Id</code> value.

#### Minute

Returns the <code>Minute</code> value.

#### Month

Returns the <code>Month</code> value.

#### Second

Returns the <code>Second</code> value.

#### Unix

Returns the <code>Unix</code> value.

#### Year

Returns the <code>Year</code> value.

