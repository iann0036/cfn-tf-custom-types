# TF::Dynatrace::MaintenanceWindow ScheduleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#end" title="End">End</a>" : <i>String</i>,
    "<a href="#recurrencetype" title="RecurrenceType">RecurrenceType</a>" : <i>String</i>,
    "<a href="#start" title="Start">Start</a>" : <i>String</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
    "<a href="#recurrence" title="Recurrence">Recurrence</a>" : <i>[ <a href="recurrencedefinition.md">RecurrenceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#end" title="End">End</a>: <i>String</i>
<a href="#recurrencetype" title="RecurrenceType">RecurrenceType</a>: <i>String</i>
<a href="#start" title="Start">Start</a>: <i>String</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
<a href="#recurrence" title="Recurrence">Recurrence</a>: <i>
      - <a href="recurrencedefinition.md">RecurrenceDefinition</a></i>
</pre>

## Properties

#### End

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurrenceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Start

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recurrence

_Required_: No

_Type_: List of <a href="recurrencedefinition.md">RecurrenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

