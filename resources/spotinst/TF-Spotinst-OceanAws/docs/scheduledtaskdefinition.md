# TF::Spotinst::OceanAws ScheduledTaskDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#shutdownhours" title="ShutdownHours">ShutdownHours</a>" : <i>[ <a href="shutdownhoursdefinition.md">ShutdownHoursDefinition</a>, ... ]</i>,
    "<a href="#tasks" title="Tasks">Tasks</a>" : <i>[ <a href="tasksdefinition.md">TasksDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#shutdownhours" title="ShutdownHours">ShutdownHours</a>: <i>
      - <a href="shutdownhoursdefinition.md">ShutdownHoursDefinition</a></i>
<a href="#tasks" title="Tasks">Tasks</a>: <i>
      - <a href="tasksdefinition.md">TasksDefinition</a></i>
</pre>

## Properties

#### ShutdownHours

_Required_: No

_Type_: List of <a href="shutdownhoursdefinition.md">ShutdownHoursDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tasks

_Required_: No

_Type_: List of <a href="tasksdefinition.md">TasksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

