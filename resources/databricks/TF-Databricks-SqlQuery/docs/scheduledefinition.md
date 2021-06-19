# TF::Databricks::SqlQuery ScheduleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#continuous" title="Continuous">Continuous</a>" : <i>[ <a href="continuousdefinition.md">ContinuousDefinition</a>, ... ]</i>,
    "<a href="#daily" title="Daily">Daily</a>" : <i>[ <a href="dailydefinition.md">DailyDefinition</a>, ... ]</i>,
    "<a href="#weekly" title="Weekly">Weekly</a>" : <i>[ <a href="weeklydefinition.md">WeeklyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#continuous" title="Continuous">Continuous</a>: <i>
      - <a href="continuousdefinition.md">ContinuousDefinition</a></i>
<a href="#daily" title="Daily">Daily</a>: <i>
      - <a href="dailydefinition.md">DailyDefinition</a></i>
<a href="#weekly" title="Weekly">Weekly</a>: <i>
      - <a href="weeklydefinition.md">WeeklyDefinition</a></i>
</pre>

## Properties

#### Continuous

_Required_: No

_Type_: List of <a href="continuousdefinition.md">ContinuousDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Daily

_Required_: No

_Type_: List of <a href="dailydefinition.md">DailyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weekly

_Required_: No

_Type_: List of <a href="weeklydefinition.md">WeeklyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

