# TF::AzureRM::LogicAppTriggerRecurrence ScheduleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#atthesehours" title="AtTheseHours">AtTheseHours</a>" : <i>[ Double, ... ]</i>,
    "<a href="#attheseminutes" title="AtTheseMinutes">AtTheseMinutes</a>" : <i>[ Double, ... ]</i>,
    "<a href="#onthesedays" title="OnTheseDays">OnTheseDays</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#atthesehours" title="AtTheseHours">AtTheseHours</a>: <i>
      - Double</i>
<a href="#attheseminutes" title="AtTheseMinutes">AtTheseMinutes</a>: <i>
      - Double</i>
<a href="#onthesedays" title="OnTheseDays">OnTheseDays</a>: <i>
      - String</i>
</pre>

## Properties

#### AtTheseHours

Specifies a list of hours when the trigger should run. Valid values are between 0 and 23.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AtTheseMinutes

Specifies a list of minutes when the trigger should run. Valid values are between 0 and 59.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnTheseDays

Specifies a list of days when the trigger should run. Valid values include `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, and `Sunday`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

