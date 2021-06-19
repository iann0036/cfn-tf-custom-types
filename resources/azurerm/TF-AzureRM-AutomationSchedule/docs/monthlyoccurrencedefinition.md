# TF::AzureRM::AutomationSchedule MonthlyOccurrenceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#day" title="Day">Day</a>" : <i>String</i>,
    "<a href="#occurrence" title="Occurrence">Occurrence</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#day" title="Day">Day</a>: <i>String</i>
<a href="#occurrence" title="Occurrence">Occurrence</a>: <i>Double</i>
</pre>

## Properties

#### Day

Day of the occurrence. Must be one of `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Occurrence

Occurrence of the week within the month. Must be between `1` and `5`. `-1` for last week within the month.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

