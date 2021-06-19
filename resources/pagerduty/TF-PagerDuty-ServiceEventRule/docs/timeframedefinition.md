# TF::PagerDuty::ServiceEventRule TimeFrameDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#activebetween" title="ActiveBetween">ActiveBetween</a>" : <i>[ <a href="activebetweendefinition.md">ActiveBetweenDefinition</a>, ... ]</i>,
    "<a href="#scheduledweekly" title="ScheduledWeekly">ScheduledWeekly</a>" : <i>[ <a href="scheduledweeklydefinition.md">ScheduledWeeklyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#activebetween" title="ActiveBetween">ActiveBetween</a>: <i>
      - <a href="activebetweendefinition.md">ActiveBetweenDefinition</a></i>
<a href="#scheduledweekly" title="ScheduledWeekly">ScheduledWeekly</a>: <i>
      - <a href="scheduledweeklydefinition.md">ScheduledWeeklyDefinition</a></i>
</pre>

## Properties

#### ActiveBetween

_Required_: No

_Type_: List of <a href="activebetweendefinition.md">ActiveBetweenDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledWeekly

_Required_: No

_Type_: List of <a href="scheduledweeklydefinition.md">ScheduledWeeklyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

