# TF::AzureRM::AutomationRunbook JobScheduleDefinition2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#jobscheduleid" title="JobScheduleId">JobScheduleId</a>" : <i>String</i>,
    "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="jobscheduledefinition.md">JobScheduleDefinition</a>, ... ]</i>,
    "<a href="#runon" title="RunOn">RunOn</a>" : <i>String</i>,
    "<a href="#schedulename" title="ScheduleName">ScheduleName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#jobscheduleid" title="JobScheduleId">JobScheduleId</a>: <i>String</i>
<a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="jobscheduledefinition.md">JobScheduleDefinition</a></i>
<a href="#runon" title="RunOn">RunOn</a>: <i>String</i>
<a href="#schedulename" title="ScheduleName">ScheduleName</a>: <i>String</i>
</pre>

## Properties

#### JobScheduleId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: No

_Type_: List of <a href="jobscheduledefinition.md">JobScheduleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunOn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

