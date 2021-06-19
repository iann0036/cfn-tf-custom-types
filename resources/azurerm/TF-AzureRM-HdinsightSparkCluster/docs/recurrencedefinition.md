# TF::AzureRM::HdinsightSparkCluster RecurrenceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
    "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ <a href="scheduledefinition.md">ScheduleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
<a href="#schedule" title="Schedule">Schedule</a>: <i>
      - <a href="scheduledefinition.md">ScheduleDefinition</a></i>
</pre>

## Properties

#### Timezone

The time zone for the autoscale schedule times.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: List of <a href="scheduledefinition.md">ScheduleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

